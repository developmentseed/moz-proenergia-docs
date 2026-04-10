---
sidebar_position: 100
title: "Apêndice A — Esqueletos JSON"
---

# Apêndice A — Esqueletos JSON Completos

## `filter_fields`

```json
[
  {
    "label":          "Rótulo legível por humanos",
    "description":    "Texto de dica (ou string vazia)",
    "column":         "Nome_Coluna_CSV",
    "label_pt":       "Rótulo em Português",
    "description_pt": "Descrição em Português"
  }
]
```

## `popup_fields`

```json
[
  {
    "label":          "Rótulo legível por humanos",
    "description":    "Texto de dica (ou string vazia)",
    "column":         "Nome_Coluna_CSV",
    "label_pt":       "Rótulo em Português",
    "description_pt": "Descrição em Português"
  }
]
```

## `summary_fields`

```json
[
  {
    "label":               "Cabeçalho de apresentação",
    "description":         "Dica (ou string vazia)",
    "columns":             ["Nome_Coluna_CSV"],
    "method":              "sum",
    "unit":                "USD",
    "group_by":            "OutraColuna",
    "category":            "Cabeçalho de Secção",
    "chartType":           "bar",
    "colors":              { "Valor": "#HEX" },
    "hasDecimal":          false,
    "showChartValueRows":  false,
    "showBarChartAverage": false,
    "label_pt":            "Rótulo em Português",
    "description_pt":      "Descrição em Português"
  }
]
```

Valores de `method`: `sum` | `average` | `count` | `min` | `max`

Valores de `chartType`: `bar` | `donut` | `stacked` | `column` | `area` | `highlight`

## `color_coding`

```json
[
  { "value": "ValorDado1", "color": "#RRGGBB" },
  { "value": "ValorDado2", "color": "#RRGGBB" },
  { "value": "default",   "color": "#RRGGBB" }
]
```
