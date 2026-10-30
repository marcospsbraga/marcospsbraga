#!/usr/bin/env python3
"""Laboratório didático de indicadores de incidentes, sem dados reais."""
from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean

SLA_HOURS = {"P1": 4, "P2": 12, "P3": 48}
COLUMNS = ("id", "servico", "prioridade", "aberto_em", "respondido_em", "resolvido_em")


@dataclass(frozen=True)
class Incident:
    identifier: str
    service: str
    priority: str
    opened: datetime
    acknowledged: datetime | None
    resolved: datetime | None


def parse_instant(value: str, field: str) -> datetime:
    if not value.strip():
        raise ValueError(f"{field}: data obrigatória")
    try:
        parsed = datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError(f"{field}: data ISO 8601 inválida") from exc
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError(f"{field}: inclua fuso horário, ex.: 2026-10-30T12:00:00Z")
    return parsed.astimezone(timezone.utc)


def optional_instant(value: str | None, field: str) -> datetime | None:
    return parse_instant(value, field) if value and value.strip() else None


def load_csv(path: Path) -> list[Incident]:
    with path.open("r", newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None or set(COLUMNS) - set(reader.fieldnames):
            raise ValueError(f"CSV deve conter as colunas: {', '.join(COLUMNS)}")
        incidents: list[Incident] = []
        seen: set[str] = set()
        for line, row in enumerate(reader, start=2):
            if None in row:
                raise ValueError(f"linha {line}: número de colunas inválido")
            identifier = (row["id"] or "").strip()
            service = (row["servico"] or "").strip()
            priority = (row["prioridade"] or "").strip().upper()
            if not identifier or not service:
                raise ValueError(f"linha {line}: id e serviço são obrigatórios")
            if identifier in seen:
                raise ValueError(f"linha {line}: ID duplicado: {identifier}")
            if priority not in SLA_HOURS:
                raise ValueError(f"linha {line}: prioridade desconhecida: {priority}")
            opened = parse_instant(row["aberto_em"] or "", f"linha {line}, aberto_em")
            acknowledged = optional_instant(row["respondido_em"], f"linha {line}, respondido_em")
            resolved = optional_instant(row["resolvido_em"], f"linha {line}, resolvido_em")
            if acknowledged is not None and acknowledged < opened:
                raise ValueError(f"linha {line}: primeira resposta anterior à abertura")
            if resolved is not None and resolved < opened:
                raise ValueError(f"linha {line}: resolução anterior à abertura")
            if acknowledged is not None and resolved is not None and acknowledged > resolved:
                raise ValueError(f"linha {line}: primeira resposta posterior à resolução")
            seen.add(identifier)
            incidents.append(Incident(identifier, service, priority, opened, acknowledged, resolved))
    return incidents


def _average(values: list[float]) -> float | None:
    return round(mean(values), 2) if values else None


def analyze(incidents: list[Incident], as_of: datetime) -> dict:
    if as_of.tzinfo is None or as_of.utcoffset() is None:
        raise ValueError("as_of deve ter fuso horário")
    as_of = as_of.astimezone(timezone.utc)
    closed: list[float] = []
    response_minutes: list[float] = []
    resolved_breaches = 0
    open_overdue = 0
    open_count = 0
    priorities = {
        p: {"total": 0, "resolvidos": 0, "abertos": 0, "fora_sla_resolvidos": 0, "abertos_atrasados": 0}
        for p in SLA_HOURS
    }
    for inc in incidents:
        if inc.opened > as_of:
            raise ValueError(f"{inc.identifier}: abertura posterior à data de referência")
        if inc.acknowledged is not None and inc.acknowledged > as_of:
            raise ValueError(f"{inc.identifier}: resposta posterior à data de referência")
        if inc.resolved is not None and inc.resolved > as_of:
            raise ValueError(f"{inc.identifier}: resolução posterior à data de referência")
        item = priorities[inc.priority]
        item["total"] += 1
        if inc.acknowledged is not None:
            response_minutes.append((inc.acknowledged - inc.opened).total_seconds() / 60)
        if inc.resolved is not None:
            hours = (inc.resolved - inc.opened).total_seconds() / 3600
            closed.append(hours)
            item["resolvidos"] += 1
            if hours > SLA_HOURS[inc.priority]:
                resolved_breaches += 1
                item["fora_sla_resolvidos"] += 1
        else:
            open_count += 1
            item["abertos"] += 1
            age_hours = (as_of - inc.opened).total_seconds() / 3600
            if age_hours > SLA_HOURS[inc.priority]:
                open_overdue += 1
                item["abertos_atrasados"] += 1
    return {
        "referencia_utc": as_of.isoformat().replace("+00:00", "Z"),
        "sla_horas_por_prioridade": SLA_HOURS,
        "resumo": {
            "total": len(incidents),
            "resolvidos": len(closed),
            "abertos": open_count,
            "fora_sla_resolvidos": resolved_breaches,
            "abertos_atrasados": open_overdue,
            "cumprimento_sla_pct": round(100 * (len(closed) - resolved_breaches) / len(closed), 2) if closed else None,
            "tempo_medio_resolucao_h": _average(closed),
            "tempo_medio_primeira_resposta_min": _average(response_minutes),
        },
        "por_prioridade": priorities,
    }


def render_text(report: dict) -> str:
    info = report["resumo"]
    compliant = info["cumprimento_sla_pct"]
    return "\n".join([
        "INCIDENT SLA LAB — cenário demonstrativo",
        f"Referência (UTC): {report['referencia_utc']}",
        f"Incidentes: {info['total']} | Resolvidos: {info['resolvidos']} | Abertos: {info['abertos']}",
        f"Resolvidos fora do SLA: {info['fora_sla_resolvidos']} | Abertos em atraso: {info['abertos_atrasados']}",
        f"Cumprimento SLA (resolvidos): {f'{compliant:.2f}%' if compliant is not None else 'N/A'}",
        f"Resolução média (h): {info['tempo_medio_resolucao_h'] if info['tempo_medio_resolucao_h'] is not None else 'N/A'}",
        f"Primeira resposta média (min): {info['tempo_medio_primeira_resposta_min'] if info['tempo_medio_primeira_resposta_min'] is not None else 'N/A'}",
    ])


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Relatório de incidentes com SLA fictício.")
    parser.add_argument("csv_file", type=Path, help="Arquivo CSV com incidentes")
    parser.add_argument("--as-of", help="Data UTC ISO 8601 de referência (padrão: agora)")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args(argv)
    try:
        as_of = parse_instant(args.as_of, "--as-of") if args.as_of else datetime.now(timezone.utc)
        report = analyze(load_csv(args.csv_file), as_of)
    except (OSError, UnicodeError, csv.Error, ValueError) as exc:
        print(f"Erro: {exc}", file=sys.stderr)
        return 2
    if args.format == "json":
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(render_text(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
