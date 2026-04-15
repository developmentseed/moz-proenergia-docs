---
title: "Common Admin Workflows"
---

# Common Admin Workflows

The sections in this guide cover each component of the platform independently. This page ties them together into the step-by-step sequences you'll actually follow when managing the platform.

---

## Adding a New Data Model

A Data Model is the top-level container for a planning analysis category. Every Data Model requires a Vector Dataset as its base unit of analysis — the Vector Dataset provides the geographic features (settlements, grid lines, polygons) that your scenario data will be joined to.

:::note What is a Vector Dataset?
A Vector Dataset is a named container for spatial geometry — the collection of points, lines, or polygons that get rendered on the map. It stores one or more uploaded geospatial files (.geojson, .gpkg, .zip, .kml) and converts them into optimised PMTiles for map delivery. Think of it as the "base map layer" that all scenario data is joined to.
:::

### Step 1 — Prepare a Vector Dataset

Before creating a Data Model, you need a Vector Dataset with at least one file in **Ready** status.

- **Using an existing dataset:** Go to Datasets → Vector Datasets and confirm the dataset you want has a Ready file. If it does, proceed to Step 2.
- **Creating a new dataset:** See [Vector Datasets and Vector Files](./vector-datasets). In brief:
  1. Go to Datasets → Vector Datasets → + Add Vector Dataset.
  2. Fill in the name and metadata fields. Click Save.
  3. Go to Datasets → Vector Files → + Add Vector File. Select your new dataset, upload the geospatial file, and click Save.
  4. Wait for the background processing to complete — the file status must reach **Ready** before you can proceed. Refresh the Vector Files list to check.

### Step 2 — Create the Data Model Configuration

Go to Datasets → Data Models → + Add Data Model.

Fill in the name, description, and presentation order. Then configure the four JSON fields:

- **`filter_fields`** — defines the filter controls in the left panel
- **`popup_fields`** — defines the attributes shown when a user clicks a feature
- **`summary_fields`** — defines the aggregated statistics in the right panel
- **`color_coding`** — maps visualization column values to map colours

:::warning Verify your column names before saving
Every `"column"` value in `filter_fields` and `popup_fields`, and every entry in `"columns"` in `summary_fields`, must exactly match a column name in the scenario CSV you plan to upload — including capitalisation. The admin cannot verify this for you. A misconfigured column name will result in blank popup values or zero summary statistics.

See [JSON Configuration Fields](./json-configuration) for full schema reference and examples.
:::

Click Save.

### Step 3 — Create the Scenario

Go to Datasets → Scenarios → + Add Scenario.

- Set **Name** to a descriptive label (this appears in the frontend scenario dropdown).
- Set **Model** to the Data Model you just created.
- Set **Vector Dataset** to the dataset from Step 1.
- Set **Presentation Order** if you have multiple scenarios and want to control their dropdown order.

Click Save.

### Step 4 — Upload the Scenario File

Go to Datasets → Scenario Files → + Add Scenario File.

Select your new Scenario from the dropdown, then upload your CSV file.

:::note CSV requirements
- **Format:** CSV only. Delimiter is auto-detected (comma or semicolon).
- **Encoding:** UTF-8. Use UTF-8 with BOM if your data contains special characters (accented letters, etc.).
- **Required column:** The file must contain an `id` column whose values correspond to the feature IDs in the linked Vector Dataset.
- **No duplicate IDs:** Each `id` value must appear only once.
- **Column completeness:** The file must contain all columns referenced in the Data Model's `filter_fields`, `popup_fields`, and `summary_fields` configuration.
:::

Optionally tick **Represent features as points in lower zoom levels** if your dataset is a large polygon grid and you want better map performance at country scale.

Click Save. Background processing begins automatically — the file will move through **Created → Processing → Ready**. If it reaches **Error**, open the record to read the Error Message.

### Step 5 — Verify

Once the Scenario File reaches Ready status:

1. Open the frontend and navigate to your new model in the sidebar.
2. Confirm the scenario appears in the scenario dropdown.
3. Confirm map features are visible.
4. Check that filter controls match your `filter_fields` configuration.
5. Check that the summary panel populates with values.

If the summary panel shows all zeros, the `metric_field_types` field on the Data Model may not have been populated yet. This is auto-populated when the Scenario File import completes. Check that the import task finished without error in Django Admin → Django Celery Results → Task Results.

---

## Adding a New Scenario to an Existing Model

Use this workflow when a Data Model already exists and you want to add a new scenario run (e.g. a new year, a different demand assumption, or updated model outputs).

### Step 1 — Confirm the Vector Dataset

Identify which Vector Dataset the new scenario should use. It must have a file in **Ready** status. You can reuse the same Vector Dataset as an existing scenario on this model — scenarios share geometry.

### Step 2 — Create the Scenario

Go to Datasets → Scenarios → + Add Scenario.

- Set **Model** to the existing Data Model.
- Set **Vector Dataset** to the appropriate dataset.
- Set **Name** and **Presentation Order**.

Click Save.

### Step 3 — Upload the Scenario File

Follow the same process as Step 4 in the workflow above. The CSV must contain the same columns referenced in the existing Data Model's JSON configuration, since the Data Model configuration is shared across all scenarios.

:::tip
You do not need to change the Data Model configuration to add a new scenario. The filters, popups, and summary fields are defined once on the Data Model and apply to every scenario under it.
:::

---

## Reprocessing Scenario Files After Data Model Changes

If you update a Data Model's `filter_fields`, `popup_fields`, or `summary_fields` configuration after scenario files have already been processed, the **map tiles** (PMTiles) and **summary metrics** may be out of sync with the new configuration.

### When reprocessing is required

| Change made | PMTiles reprocessing needed? | Metrics reprocessing needed? |
|---|:---:|:---:|
| Added a new column to `filter_fields` | Yes | Yes |
| Changed a `label` or `description` only | No | No |
| Changed `summary_fields` columns or method | No | Yes |
| Changed `popup_fields` column | No | No |
| Changed `color_coding` or `visualization_column` | Yes | No |

### Reprocessing map tiles (PMTiles)

PMTiles are generated from a merge of the vector geometry and only the columns listed in `filter_fields` (plus the `visualization_column`). If you add a new filter column, existing PMTiles won't contain it and map-level filtering will not work correctly.

1. Go to Datasets → Scenario Files.
2. Select the affected Scenario File(s) using the checkboxes.
3. From the **Actions** dropdown, select **Reprocess files** and click Go.
4. Wait for the status to return to **Ready**.

:::note
Only files in **Ready** or **Error** status can be requeued. Files in **Created** or **Processing** state cannot be reprocessed.
:::

### Reprocessing summary metrics

Summary metrics are stored in a denormalized table (`ScenarioDataMetrics`) that is populated from the scenario CSV on import. If you add columns to `summary_fields`, existing metrics won't include those columns and the summary panel will show zeros for new fields.

Use the management command to re-sync metrics for a specific scenario:

```bash
cd /var/www/proenergia/app
source venv/bin/activate
python manage.py sync_scenario_metrics --scenario-id <scenario_id>
```

Replace `<scenario_id>` with the numeric ID of the scenario (visible in the URL when viewing the scenario in the admin).

The command will clear existing metrics for that scenario and re-extract all configured fields from the stored CSV data. It also updates the `metric_field_types` mapping on the Data Model, which is required for the summaries API to recognise new column types.

:::tip Finding the scenario ID
Go to Datasets → Scenarios and click the scenario name. The ID appears in the browser URL: `/admin/datasets/scenario/<id>/change/`.
:::

### Reprocessing both

If your Data Model change affects both tiles and metrics (e.g. adding a column that is both a filter and a summary field), do both steps: reprocess the Scenario File via the admin action first, then run the `sync_scenario_metrics` command after the file reaches Ready status.