---
sidebar_position: 10
title: "Monitoring & Troubleshooting"
---

# 10. Monitoring and Troubleshooting

## 10.1 Monitoring Background Tasks

- **In Django Admin:** Go to **Django Celery Results → Task Results** to see all completed, failed, and pending tasks.
- **Via Flower (local dev):** Run `celery -A proenergia flower --address=127.0.0.1 --port=5555` and access `http://localhost:5555`.

## 10.2 Admin Troubleshooting

| Issue | Cause & Resolution |
|---|---|
| VectorFile stuck in Processing | Celery worker is not running. Restart: `sudo systemctl restart proenergia-celery` |
| VectorFile / ScenarioFile shows Error | Open the record and read the **Error Message**. Common causes: unsupported CRS, corrupt file, or CSV missing the `id` column. |
| `filter_fields` fails: Missing a required key | Each entry must have all three keys: `label`, `description`, `column`. |
| `summary_fields` fails: columns key should be a list | The `columns` key must be a JSON array even for one column: `["MyColumn"]` |
| `summary_fields` fails: invalid chartType | Valid values: `bar`, `donut`, `stacked`, `column`, `area`, `highlight`. |
| `color_coding` fails: invalid color | Each color must be a valid 3 or 6-digit hex code (e.g. `#FF0000`). |
| Frontend shows no features (blank map) | The Scenario's ScenarioFile must be in Ready status. Check file processing. |
| Summary panel shows all zeros | `metric_field_types` may not be populated. It auto-populates on successful Scenario File import. |
| Admin login shows 403 | User exists but lacks Staff status. A Super Admin must enable it. |
| Model not visible on frontend | Data Model's `is_public` flag is `False`. Only superusers can see private models. |
