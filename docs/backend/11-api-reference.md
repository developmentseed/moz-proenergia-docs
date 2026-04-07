---
sidebar_position: 11
title: "11. API Reference"
---

# 11. API Reference

- **Base URL:** `/api/v1/`
- **Swagger docs:** `/api/v1/docs/`
- **OpenAPI schema:** `/api/v1/schema/`

## Endpoints

| Endpoint | Description |
|---|---|
| `GET /api/v1/model/` | List all public Data Models. Non-superusers see only `is_public=True` models. Returns `filter_fields`, `popup_fields`, `summary_fields`, `color_coding`, `metric_field_types`, `scenarios`, `name_pt`, `description_pt`, `presentation_order`. |
| `GET /api/v1/model/{id}/` | Retrieve a single Data Model by ID. |
| `GET /api/v1/vector/` | List VectorDatasets. Public+approved for anonymous; all approved for authenticated; all for superusers. |
| `GET /api/v1/vector/{id}/` | Retrieve a single VectorDataset. |
| `GET /api/v1/raster/` | List RasterDatasets. Same visibility rules as vector datasets. |
| `GET /api/v1/raster/{id}/` | Retrieve a single RasterDataset. |
| `GET /api/v1/reference/` | List ReferenceDatasets. Same visibility rules as vector datasets. |
| `GET /api/v1/reference/{id}/` | Retrieve a single ReferenceDataset. |
| `GET /api/v1/scenario/{id}/feature/{feature_id}/` | Retrieve all stored metadata for a single feature. Used to populate map popups. |
| `GET /api/v1/scenario/{id}/summaries/` | Compute statistical summaries. See Section 11.1. |
| `DELETE /api/v1/scenario/{id}/summaries/cache/` | Purge cached summary responses for a scenario. |
| `POST /api/v1/token-auth/` | Obtain an authentication token. Body: `{"username": "...", "password": "..."}` |

## 11.1 Summaries Endpoint

`GET /api/v1/scenario/{id}/summaries/`

| Parameter | Description |
|---|---|
| `fields` (required) | Comma-separated column names to aggregate. E.g. `fields=Pop2030,Technology2030` |
| `q` (optional) | Filter expression. Comma-separated conditions: `field=value` (equality); `field__min=N` and `field__max=N` (numeric range); `field__in=val1;val2` (multi-value string). |
| `group_by` (optional) | Comma-separated string-type column name(s). Must be in `metric_field_types`. Maximum 2 fields for nested grouping. |

### Filter Examples

```bash
# Single value match
?fields=Pop2030&q=Technology2030=SHS

# Numeric range
?fields=InvestmentCostTotal&q=Pop2030__min=100,Pop2030__max=5000

# Multi-value string filter
?fields=Pop2030&q=Technology2030__in=SHS;MiniGrid

# With grouping
?fields=Pop2030&q=Admin_1=Maputo&group_by=Technology2030

# Two-level nested grouping
?fields=Pop2030&group_by=Admin_1,Technology2030
```

### Response Structure

```json
{
  "scenario_id": 1,
  "filters_applied": "Admin_1=Maputo",
  "summaries": {
    "Pop2030": {
      "type": "numeric",
      "count": 7354,
      "min": 3.69,
      "max": 3620782.55,
      "sum": 4466719.88
    },
    "Technology2030": {
      "type": "string",
      "count": 7354,
      "values": { "SHS": 2100, "MiniGrid": 850, "Grid": 4404 }
    }
  }
}
```

:::note Caching
Summary responses are cached for 24 hours. Use `DELETE /summaries/cache/` after uploading new Scenario File data.
:::
