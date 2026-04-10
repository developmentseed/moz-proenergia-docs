---
sidebar_position: 7
title: "Vector Datasets & Vector Files"
---

# 7. Vector Datasets and Vector Files

## 7.1 What Is a Vector Dataset?

A Vector Dataset is a named container for spatial geometry — the collection of points, lines, or polygons rendered on the map. Scenarios reference a Vector Dataset to obtain their spatial geometry.

## 7.2 Adding a New Vector Dataset

1. Go to **Datasets → Vector Datasets → + Add Vector Dataset**.
2. Fill in the metadata fields (see Section 7.3).
3. Click **Save**. You can then upload Vector Files.

## 7.3 Vector Dataset Fields Reference

| Field | Description |
|---|---|
| **Name / Name (PT)** | Unique name (max 155 chars). Supports EN/PT translations. |
| **Description / Description (PT)** | Optional abstract. Supports translations. |
| **Data Owner** (`source`) | Optional attribution (max 155 chars). |
| **Point of Contact** (`contact`) | Optional contact person or team. |
| **Publication Date** (`published`) | Optional date the dataset was published at the source. |
| **Temporal Extent** | Optional time period the data covers (e.g. `"2020–2024"`). |
| **CRS** | Optional. Document the source CRS (e.g. `"EPSG:4326"`). All files are reprojected to EPSG:4326 during processing. |
| **Maintenance Frequency** | Optional. How often the dataset is updated at the source. |
| **Lineage** | Optional. Data provenance or processing notes. |
| **Legal License** | Optional. Licence under which the data is provided. |
| **Attribute Definitions** | Optional. Link or note describing the attribute schema. |
| **Is Public** | Superuser only. If ticked, dataset visible to unauthenticated users. |
| **Is Approved** | Superuser only. Must be approved before the dataset can be used in Scenarios or shown on the frontend. |

## 7.4 Adding Vector Files

Uploading triggers a Celery task: file → FlatGeobuf (GDAL) → PMTiles (Tippecanoe).

1. Go to **Datasets → Vector Files → + Add Vector File**.
2. Select the parent Vector Dataset.
3. Upload a file. Accepted formats:

| Format | Notes |
|---|---|
| `.geojson` | GeoJSON. Must use WGS84 (EPSG:4326). Preferred format. |
| `.gpkg` | GeoPackage. Fully supported. |
| `.zip` | ZIP archive containing a Shapefile (`.shp`, `.shx`, `.dbf`, `.prj`). |
| `.kml` | Keyhole Markup Language. Fully supported. |

4. Click **Save**. Processing begins automatically.

## 7.5 Monitoring File Processing

Status: `Created → Processing → Ready` (or `Error`). If a file enters Error state, open the record and read the **Error Message**. Use **Reprocess files** to re-queue.

## 7.6 Publishing a Dataset

Only superusers can publish datasets. Select datasets in the list view and use the **Actions** dropdown:

| Action | Effect |
|---|---|
| Make dataset public | Sets `is_public = True` |
| Make dataset private | Sets `is_public = False` |
| Publish dataset | Sets `is_approved = True` |
| Unpublish dataset | Sets `is_approved = False` |

:::note Visibility rule
A dataset is visible to unauthenticated users only when both `is_public = True` AND `is_approved = True`. Authenticated users can see any dataset where `is_approved = True`, regardless of `is_public`.
:::
