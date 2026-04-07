---
sidebar_position: 100
title: "Appendix A — JSON Skeletons"
---

# Appendix A — Complete JSON Skeletons

## `filter_fields`

```json
[
  {
    "label":          "Human-readable label",
    "description":    "Tooltip text (or empty string)",
    "column":         "CSV_Column_Name",
    "label_pt":       "Rótulo em Português",
    "description_pt": "Descrição em Português"
  }
]
```

## `popup_fields`

```json
[
  {
    "label":          "Human-readable label",
    "description":    "Tooltip text (or empty string)",
    "column":         "CSV_Column_Name",
    "label_pt":       "Rótulo em Português",
    "description_pt": "Descrição em Português"
  }
]
```

## `summary_fields`

```json
[
  {
    "label":               "Display heading",
    "description":         "Tooltip (or empty string)",
    "columns":             ["CSV_Column_Name"],
    "method":              "sum",
    "unit":                "USD",
    "group_by":            "OtherColumn",
    "category":            "Section Heading",
    "chartType":           "bar",
    "colors":              { "Value": "#HEX" },
    "hasDecimal":          false,
    "showChartValueRows":  false,
    "showBarChartAverage": false,
    "label_pt":            "Rótulo em Português",
    "description_pt":      "Descrição em Português"
  }
]
```

`method` values: `sum` | `average` | `count` | `min` | `max`

`chartType` values: `bar` | `donut` | `stacked` | `column` | `area` | `highlight`

## `color_coding`

```json
[
  { "value": "DataValue1", "color": "#RRGGBB" },
  { "value": "DataValue2", "color": "#RRGGBB" },
  { "value": "default",   "color": "#RRGGBB" }
]
```
