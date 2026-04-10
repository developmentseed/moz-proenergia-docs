---
sidebar_position: 5
title: "JSON Configuration Fields"
---

# 5. JSON Configuration Fields

Four JSON arrays on each Data Model configure frontend behaviour. The admin validates structure on save and reports errors for missing required keys or invalid values.

:::note
All JSON must use double quotes for keys and string values, with no trailing commas. Arrays must be wrapped in `[ ]`.
:::

---

## 5.1 `filter_fields`

Defines the filter controls shown in the left panel. Each entry maps to one interactive filter control.

### Schema

| Key | Type | Required? | Description |
|---|---|---|---|
| `label` | string | **required** | Human-readable label shown above the filter control. |
| `description` | string | **required** | Tooltip text. Can be an empty string. |
| `column` | string | **required** | Exact column name in the scenario CSV. **Case-sensitive.** |
| `label_pt` | string | optional | Portuguese translation of the label. |
| `description_pt` | string | optional | Portuguese translation of the description. |

### How filter type is determined

The frontend derives the control type at runtime from the column name and data values:

| Derived Type | Condition | Rendered Control |
|---|---|---|
| `admin` | Column name matches an administrative geography keyword (Admin_1–4, Province, Província, District, Distrito, Posto, Localidade, Region, Região, and plural/accented variants) | Searchable multi-select Combobox |
| `numeric` | Column data contains numeric values (not all 0 or 1) | Dual text-input range control |
| `checkbox` | All other cases (strings, booleans) | Checkbox group |

### Example

```json
[
  {
    "label": "Province",
    "description": "Administrative province",
    "label_pt": "Provincia",
    "description_pt": "Provincia administrativa",
    "column": "Admin_1"
  },
  {
    "label": "Electrification Technology",
    "description": "Recommended technology for 2030",
    "column": "Technology2030"
  },
  {
    "label": "Population (2030)",
    "description": "Projected settlement population",
    "column": "Pop2030"
  }
]
```

:::tip
`Admin_1` → admin combobox. `Technology2030` → checkbox group (string values). `Pop2030` → numeric range control.
:::

---

## 5.2 `popup_fields`

Defines which attributes are displayed when a user clicks a feature on the map. Fields appear in the order listed.

### Schema

| Key | Type | Required? | Description |
|---|---|---|---|
| `label` | string | **required** | Display label for the attribute. |
| `description` | string | **required** | Tooltip text. Can be an empty string. |
| `column` | string | **required** | Exact CSV column name. **Case-sensitive.** |
| `label_pt` | string | optional | Portuguese translation of the label. |
| `description_pt` | string | optional | Portuguese translation of the description. |

:::note
When a user clicks a feature, the frontend calls `GET /api/v1/scenario/{id}/feature/{feature_id}/` and shows only the columns listed here, in order.
:::

### Example

```json
[
  {
    "label": "Settlement Name",
    "description": "Name of the settlement",
    "label_pt": "Nome do Assentamento",
    "description_pt": "Nome do assentamento",
    "column": "SettlementName"
  },
  { "label": "Population (2030)", "description": "Projected population", "column": "Pop2030" },
  { "label": "Recommended Technology", "description": "Least-cost technology", "column": "Technology2030" },
  { "label": "Total Investment", "description": "Total investment (USD)", "column": "InvestmentCostTotal" }
]
```

---

## 5.3 `summary_fields`

Defines the aggregated statistics shown in the right-hand Summary panel.

### Schema

| Key | Type | Required? | Description |
|---|---|---|---|
| `label` | string | **required** | Display heading for this summary item. |
| `description` | string | **required** | Tooltip description. Can be empty string. |
| `columns` | array of strings | **required** | One or more CSV column names. **Always an array.** Multiple columns become sub-rows. |
| `method` | string | optional | `sum` \| `average` \| `count` \| `min` \| `max`. Defaults to `sum`. |
| `unit` | string | optional | Unit suffix after the value, e.g. `"USD"`, `"kW"`, `"km"`. |
| `group_by` | string or array | optional | Column name(s) to group results by. Single string or array of up to 2 strings for nested grouping. |
| `category` | string | optional | Groups items under a collapsible heading in the summary panel. |
| `chartType` | string | optional | `bar` \| `donut` \| `stacked` \| `column` \| `area` \| `highlight`. Admin validates all six values. |
| `colors` | object | optional | Colour map for charts. Keys are data values; values are hex strings. E.g. `{"SHS": "#F1C40F"}`. |
| `hasDecimal` | boolean | optional | If `true`, values display with decimal places. Must be exactly `true` or `false`. |
| `showChartValueRows` | boolean | optional | If `true`, shows a table of raw values beneath the chart. |
| `showBarChartAverage` | boolean | optional | If `true`, overlays an average line on bar charts. |
| `label_pt` | string | optional | Portuguese translation of the label. |
| `description_pt` | string | optional | Portuguese translation of the description. |

:::note
If `method` is omitted the system defaults to `sum`. For string-type columns, the frontend always uses `count` regardless of the method setting.
:::

### Examples

**Simple numeric aggregate:**
```json
{
  "label": "Total Population (2030)",
  "description": "Sum of projected population across all settlements",
  "columns": ["Pop2030"],
  "method": "sum"
}
```

**Technology breakdown as a bar chart with colours:**
```json
{
  "label": "Technology Mix (2030)",
  "description": "Count per electrification technology",
  "columns": ["Technology2030"],
  "method": "count",
  "chartType": "bar",
  "colors": { "SHS": "#F1C40F", "MiniGrid": "#27AE60", "Grid": "#2980B9" },
  "showChartValueRows": true
}
```

**Numeric field grouped by technology:**
```json
{
  "label": "Investment by Technology",
  "description": "Total investment grouped by technology type",
  "columns": ["InvestmentCostTotal"],
  "method": "sum",
  "unit": "USD",
  "group_by": "Technology2030",
  "chartType": "bar",
  "showBarChartAverage": true
}
```

**Multi-column aggregate:**
```json
{
  "label": "Capacity by Type",
  "description": "New capacity installed by technology category",
  "columns": ["NewCapacityGrid", "NewCapacityMiniGrid", "NewCapacitySHS"],
  "method": "sum",
  "unit": "kW"
}
```

---

## 5.4 `color_coding`

Maps values of `visualization_column` to specific colours on the map. The special value `"default"` sets the fallback colour. The admin validates that each `color` is a valid hex string (3 or 6 hex digits, with or without leading `#`).

### Schema

| Key | Type | Required? | Description |
|---|---|---|---|
| `value` | string | **required** | The column value to match. Use `"default"` as a catch-all fallback. |
| `color` | string | **required** | Valid hex colour string. E.g. `"#E74C3C"` or `"E74C3C"`. Validated by the admin. |

### Example

```json
[
  { "value": "SHS",      "color": "#F1C40F" },
  { "value": "MiniGrid", "color": "#27AE60" },
  { "value": "Grid",     "color": "#2980B9" },
  { "value": "default",  "color": "#95A5A6" }
]
```

:::warning
The admin validates hex codes. An invalid value like `"red"` or `"#GG0000"` will produce an error on save.
:::
