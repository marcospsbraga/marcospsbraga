# Incident SLA Lab

**Projeto público de demonstração · Python 3.10+ · biblioteca padrão (sem dependências externas)**

Uma ferramenta de linha de comando que calcula indicadores de incidentes, compara tempos de resolução com um SLA fictício e aponta ocorrências abertas em atraso.

O objetivo é demonstrar **tratamento de dados, validação de entradas, métricas, testes unitários e apresentação de resultados**, em um cenário próximo à rotina de operações e monitoramento.

> **Atenção:** todos os registros do exemplo são inventados. Os prazos P1 = 4h, P2 = 12h e P3 = 48h são apenas hipóteses didáticas, não metas reais de qualquer empresa.

## Executar

Na pasta deste projeto:

```powershell
python incident_sla_lab.py exemplos/incidentes.csv --as-of 2026-10-30T12:00:00Z
```

Saída esperada:

```text
INCIDENT SLA LAB — cenário demonstrativo
Referência (UTC): 2026-10-30T12:00:00Z
Incidentes: 6 | Resolvidos: 4 | Abertos: 2
Resolvidos fora do SLA: 1 | Abertos em atraso: 1
Cumprimento SLA (resolvidos): 75.00%
Resolução média (h): 12.12
Primeira resposta média (min): 40.0
```

Para obter os resultados em JSON:

```powershell
python incident_sla_lab.py exemplos/incidentes.csv --as-of 2026-10-30T12:00:00Z --format json
```

O argumento `--as-of` fixa uma data de referência para resultados reproduzíveis. Sem ele, o programa utiliza o horário UTC atual.

## Testes

```powershell
python -m unittest discover -s . -p "test_*.py" -v
```

Cobertura inicial: leitura e consistência do CSV, datas com fuso horário, métricas, limites do SLA, tratamento de entradas inválidas e saída JSON.

## Estrutura de entrada

Colunas esperadas: `id,servico,prioridade,aberto_em,respondido_em,resolvido_em`. Datas devem estar no formato ISO 8601 com fuso horário, por exemplo `2026-10-30T12:00:00Z`. Campos de resposta e resolução podem ficar vazios.

Para incidentes resolvidos, o cálculo considera o tempo entre abertura e resolução. Para incidentes abertos, considera o intervalo entre a abertura e a data de referência. O percentual de cumprimento do SLA usa **somente incidentes resolvidos**; abertos atrasados são mostrados separadamente.

## Limites

É uma demonstração educacional, **não um sistema de produção**: não inclui autenticação, base de dados, integração com redes, tratamento de calendário comercial nem um modelo formal de contratos de serviço. O código foi construído com assistência de IA e validado por testes locais.
