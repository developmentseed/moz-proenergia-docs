---
sidebar_position: 103
title: "Appendix D — Glossary"
---

# Appendix D — Glossary

| Term | Definition |
|---|---|
| **Data Model** | A thematic analysis category (e.g., Least Cost Electrification). Container and configuration for Scenarios, Vector Datasets, and display settings. Can be public or private (`is_public`). |
| **Scenario** | A specific model run within a Data Model (e.g., Baseline 2025). Linked to a Vector Dataset and one or more Scenario Files. Ordered by `presentation_order`. |
| **Scenario File** | A CSV uploaded to a Scenario containing modeled output attributes. Must include an `id` column. Supports `low_zoom_as_points` rendering option. |
| **ScenarioData** | Database table (JSONB) storing all imported Scenario File attribute data per feature. Powers the `/feature/` API endpoint. |
| **ScenarioDataMetrics** | Denormalized key-value table for fast aggregation queries. Auto-populated on Scenario File import. Powers the `/summaries/` API endpoint. |
| **Vector Dataset** | Named container for spatial geometry files (`.geojson`, `.gpkg`, `.zip`, `.kml`). Includes rich metadata fields. Supports EN/PT translations. |
| **Raster Dataset** | Container for Cloud-Optimized GeoTIFF (COG) imagery files. Displayed as raster overlay layers on the map. |
| **Reference Dataset** | Container for supporting documents and tables (`.pdf`, `.csv`, `.xlsx`, `.docx`, etc.). Listed in the Downloads section. |
| **PMTiles** | Single-file vector tile archive served via HTTP range requests. Generated from vector files using Tippecanoe. |
| **COG** | Cloud-Optimized GeoTIFF. A raster format optimised for streaming from object storage. Must be in EPSG:3857 with 256×256 block size for the platform's raster rendering. |
| **presentation_order** | Integer field on DataModel and Scenario controlling sort order in the frontend sidebar and dropdown. Lower numbers appear first. |
| **is_public (DataModel)** | Boolean on DataModel. If `False`, the model is hidden from the API for non-superusers and does not appear on the frontend. |
| **metric_field_types** | JSON dict on DataModel mapping CSV column names to `"numeric"` or `"string"`. Auto-populated on Scenario File import. Powers the summaries API. |
| **visualization_column** | The CSV column whose unique values determine map feature colours, as configured by `color_coding`. |
| **low_zoom_as_points** | ScenarioFile option that renders polygon centroids at low zoom (5–10) and full geometry at high zoom (11–14). Improves performance for large polygon datasets. |
| **Celery** | Distributed task queue for async processing (PMTiles generation, CSV import). |
| **RabbitMQ** | Message broker for Celery. In production, uses a dedicated vhost: `proenergia_vhost`. |
| **Tippecanoe** | Command-line tool that generates PMTiles from FlatGeobuf vector data. |
| **tile-join** | Tippecanoe companion tool that merges multiple PMTiles files (used for `low_zoom_as_points`). |
| **GDAL / ogr2ogr** | Geospatial data library for format conversion and reprojection. |
| **i18n** | Internationalisation. The platform supports Portuguese (default) and English via i18next. Backend models support `name_pt` and `description_pt` translation fields. |
| **proenergia_db** | The production PostgreSQL database name. |
| **DATABASE_URL** | Primary environment variable for the database connection (`postgis://...`). |
