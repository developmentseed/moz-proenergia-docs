---
sidebar_position: 4
title: "4. Data Models"
---

# 4. Data Models

## 4.1 What Is a Data Model?

A Data Model represents a planning or analysis category — such as Least Cost Electrification, Agricultural Cold Chain, or Clean Cooking. Each Data Model groups together Scenarios, Vector Datasets, and display configuration (filters, popups, summaries, colour coding). It can also reference Raster layers (COG imagery) and Reference datasets (documents).

## 4.2 Adding a New Data Model

1. Go to **Datasets → Data Models → + Add Data Model**.
2. Fill in the top-level fields (see Section 4.3).
3. Add JSON configuration for `filter_fields`, `popup_fields`, `summary_fields`, and `color_coding` (see [Section 5](./05-json-configuration)).
4. Click **Save**, or **Save and continue editing**.

## 4.3 Data Model Fields Reference

| Field | Description |
|---|---|
| **Name / Name (PT)** | Unique name (max 155 chars). Supports English and Portuguese via the tabbed form. Displayed in the frontend navigation sidebar. |
| **Description / Description (PT)** | Optional description. Supports translations. |
| **Presentation Order** | Integer controlling sort order in the frontend sidebar. Lower numbers appear first. Default: 0. |
| **Is Public** | Boolean (default: True). If False, the model is hidden from the API for non-superusers and does not appear on the frontend. |
| **Visualization Column** | Optional. The exact CSV column name whose unique values colour-code map features. Leave blank for a single default colour. |
| **Color Coding (JSON)** | Maps each visualization column value to a hex colour. See [Section 5.4](./05-json-configuration#54-color_coding). |
| **Filter Fields (JSON)** | Controls filter controls in the left panel. See [Section 5.1](./05-json-configuration#51-filter_fields). |
| **Popup Fields (JSON)** | Defines attributes shown when a user clicks a map feature. See [Section 5.2](./05-json-configuration#52-popup_fields). |
| **Summary Fields (JSON)** | Specifies aggregated statistics in the right-panel summary. See [Section 5.3](./05-json-configuration#53-summary_fields). |
| **Contextual Layers** | Multi-select of approved VectorDatasets to toggle on/off alongside the main data. |
| **Raster Layers** | Multi-select of approved RasterDatasets (COG imagery). |
| **Reference Datasets** | Multi-select of approved ReferenceDatasets (documents, tables). |

:::warning
Changes to JSON configuration fields affect all users immediately. Test carefully before saving in production.
:::

:::tip JSON editor
The JSON fields use an interactive tree/form/view/code editor. Switch between modes using the tabs above each field. **Code** mode accepts raw JSON text.
:::
