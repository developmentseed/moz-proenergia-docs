---
sidebar_position: 6
title: "6. Scenarios & Scenario Files"
---

# 6. Scenarios and Scenario Files

## 6.1 What Is a Scenario?

A Scenario represents a specific model run within a Data Model — for example, *Baseline 2025* or *Accelerated Grid Expansion 2035*. Each Scenario links to a Vector Dataset for spatial geometry and holds analysis results via one or more Scenario Files (CSV).

## 6.2 Adding a New Scenario

1. Go to **Datasets → Scenarios → + Add Scenario**.
2. Fill in the fields (see Section 6.3).
3. Click **Save**. You can then add Scenario Files.

## 6.3 Scenario Fields Reference

| Field | Description |
|---|---|
| **Name / Name (PT)** | Unique name (max 155 chars). Displayed in the frontend scenario dropdown. Supports EN/PT translations. |
| **Model** | The Data Model this scenario belongs to (foreign key). |
| **Vector Dataset** | The Vector Dataset providing spatial geometry for this scenario's map layer. Must have at least one file in Ready status. |
| **Presentation Order** | Integer controlling sort order in the frontend dropdown. Lower numbers appear first. |

:::note
A single Vector Dataset can be shared across multiple Scenarios. Scenarios are ordered in the dropdown by Presentation Order, then by ID.
:::

## 6.4 Adding Scenario Files

A Scenario File is a CSV containing analysis result data. Each row corresponds to a spatial feature identified by a numeric `id` column. Uploading triggers a Celery task that merges the CSV with vector geometry to generate a PMTiles map layer, then imports the CSV into the database for summary queries.

1. Go to **Datasets → Scenario Files → + Add Scenario File**.
2. Select the parent Scenario.
3. Upload a CSV file. The CSV **must include an `id` column** matching feature IDs in the linked Vector Dataset.
4. Optionally tick **Represent features as points in lower zoom levels** (see Section 6.5).
5. Click **Save**.

:::note CSV format
Delimiter is auto-detected (comma or semicolon). Numeric strings are automatically converted to numbers; all other values are stored as strings. The `id` column is used as the join key and is not stored as metadata. Files with UTF-8 BOM are handled correctly.
:::

## 6.5 Low Zoom as Points Option

The **Represent features as points in lower zoom levels** checkbox (`low_zoom_as_points`) optimises rendering for large polygon datasets.

When enabled, the pipeline generates:
- Centroid points for zoom levels 5–10
- Full polygon geometry for zoom levels 11–14
- These are joined into a single PMTiles file using Tippecanoe's `tile-join` tool.

:::tip
Recommended for large datasets (10,000+ features) composed of uniform square polygons. Not necessary for point or line data.
:::

## 6.6 Scenario File Status Indicator

The Scenario Files list includes an **Is Active** column indicating whether a file is the currently active (latest Ready) file for its scenario. Only the most recently processed Ready file is active.

## 6.7 Monitoring Scenario File Processing

Status progresses: `Created → Processing → Ready` (or `Error`).

If a file enters Error state, open the record and read the **Error Message** field. Use the **Reprocess files** action to re-queue files in Ready or Error state.

:::note Cache
Summary responses are cached for 24 hours. After uploading new data, use `DELETE /api/v1/scenario/{id}/summaries/cache/` to clear stale cached results.
:::
