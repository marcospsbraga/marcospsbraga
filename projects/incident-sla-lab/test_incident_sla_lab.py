"""Testes unitários com cenários completamente sintéticos."""
from __future__ import annotations

import csv
import json
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from incident_sla_lab import Incident, analyze, load_csv, parse_instant, render_text, SLA_HOURS

HERE = Path(__file__).resolve().parent
SAMPLE = HERE / "exemplos" / "incidentes.csv"
REFERENCE = parse_instant("2026-10-30T12:00:00Z", "teste")


class IncidentSlaLabTests(unittest.TestCase):
    def test_sample_summary(self):
        result = analyze(load_csv(SAMPLE), REFERENCE)["resumo"]
        self.assertEqual(result["total"], 6)
        self.assertEqual(result["resolvidos"], 4)
        self.assertEqual(result["abertos"], 2)
        self.assertEqual(result["fora_sla_resolvidos"], 1)
        self.assertEqual(result["abertos_atrasados"], 1)
        self.assertEqual(result["cumprimento_sla_pct"], 75.0)
        self.assertEqual(result["tempo_medio_resolucao_h"], 12.12)
        self.assertEqual(result["tempo_medio_primeira_resposta_min"], 40.0)

    def test_sample_by_priority(self):
        priorities = analyze(load_csv(SAMPLE), REFERENCE)["por_prioridade"]
        self.assertEqual(priorities["P1"]["total"], 3)
        self.assertEqual(priorities["P1"]["abertos_atrasados"], 1)
        self.assertEqual(priorities["P2"]["fora_sla_resolvidos"], 1)
        self.assertEqual(priorities["P3"]["resolvidos"], 1)

    def test_exact_sla_limit_is_not_breach(self):
        start = parse_instant("2026-10-29T08:00:00Z", "inicio")
        end = parse_instant("2026-10-29T12:00:00Z", "fim")
        incident = Incident("X", "Acesso", "P1", start, start, end)
        result = analyze([incident], REFERENCE)
        self.assertEqual(result["resumo"]["fora_sla_resolvidos"], 0)
        self.assertEqual(SLA_HOURS["P1"], 4)

    def test_empty_report_has_no_division_by_zero(self):
        result = analyze([], REFERENCE)["resumo"]
        self.assertEqual(result["total"], 0)
        self.assertIsNone(result["cumprimento_sla_pct"])
        self.assertIsNone(result["tempo_medio_resolucao_h"])

    def test_timezone_is_required(self):
        with self.assertRaisesRegex(ValueError, "fuso horário"):
            parse_instant("2026-10-30T12:00:00", "teste")

    def test_utc_offsets_are_normalized(self):
        a = parse_instant("2026-10-30T09:00:00-03:00", "teste")
        self.assertEqual(a, REFERENCE)

    def _make_csv(self, rows):
        temp = tempfile.TemporaryDirectory()
        path = Path(temp.name) / "data.csv"
        with path.open("w", newline="", encoding="utf-8") as stream:
            writer = csv.writer(stream)
            writer.writerow(("id", "servico", "prioridade", "aberto_em", "respondido_em", "resolvido_em"))
            writer.writerows(rows)
        self.addCleanup(temp.cleanup)
        return path

    def test_reject_duplicate_identifiers(self):
        row = ["X", "Acesso", "P1", "2026-10-29T08:00:00Z", "", ""]
        with self.assertRaisesRegex(ValueError, "duplicado"):
            load_csv(self._make_csv([row, row]))

    def test_reject_unknown_priority(self):
        with self.assertRaisesRegex(ValueError, "prioridade desconhecida"):
            load_csv(self._make_csv([["A", "Acesso", "P4", "2026-10-29T08:00:00Z", "", ""]]))

    def test_reject_reversed_resolution(self):
        with self.assertRaisesRegex(ValueError, "anterior"):
            load_csv(self._make_csv([["A", "Acesso", "P1", "2026-10-29T08:00:00Z", "", "2026-10-28T08:00:00Z"]]))

    def test_reject_future_event_for_reference_date(self):
        future = Incident("X", "Acesso", "P1", parse_instant("2026-11-01T08:00:00Z", "futuro"), None, None)
        with self.assertRaisesRegex(ValueError, "posterior"):
            analyze([future], REFERENCE)

    def test_rendered_text_is_readable(self):
        output = render_text(analyze(load_csv(SAMPLE), REFERENCE))
        self.assertIn("75.00%", output)
        self.assertIn("6 | Resolvidos: 4", output)

    def test_cli_json_output(self):
        completed = subprocess.run(
            [sys.executable, str(HERE / "incident_sla_lab.py"), str(SAMPLE), "--as-of",
             "2026-10-30T12:00:00Z", "--format", "json"],
            text=True, encoding="utf-8", capture_output=True, check=False
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        report = json.loads(completed.stdout)
        self.assertEqual(report["resumo"]["abertos_atrasados"], 1)


if __name__ == "__main__":
    unittest.main()
