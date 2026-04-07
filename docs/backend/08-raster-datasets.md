---
sidebar_position: 8
title: "8. Raster Datasets & Raster Files"
---

# 8. Raster Datasets and Raster Files

Raster Datasets store georeferenced imagery (satellite photos, terrain models, derived raster outputs). They are displayed as Cloud-Optimized GeoTIFF (COG) layers. Unlike vector data, raster files do not require PMTiles conversion — they are served directly from object storage.

## 8.1 Adding a Raster Dataset

1. Go to **Datasets → Raster Datasets → + Add Raster Dataset**.
2. Fill in the same metadata fields as Vector Datasets (name, description, source, contact, CRS, etc.). Supports EN/PT translations.
3. Click **Save**. Then add a Raster File.

## 8.2 Adding Raster Files

1. Go to **Datasets → Raster Files → + Add Raster File**.
2. Select the parent Raster Dataset.
3. Upload a raster file. Accepted formats: `.tiff`, `.tif`, `.geotiff`, `.gtiff`, `.vrt`.
4. Click **Save**.

:::warning COG requirements
For best performance, raster files must be Cloud-Optimized GeoTIFFs in **EPSG:3857** with **256×256 block size** and the Google Maps tiling scheme.

**Single-band data:**
```bash
gdalwarp <source.tif> <dest.tif> -of COG -t_srs EPSG:3857 \
  -co BLOCKSIZE=256 -co TILING_SCHEME=GoogleMapsCompatible
```

**RGB imagery (satellite):**
```bash
gdalwarp <source.tif> <dest.tif> -of COG -t_srs EPSG:3857 \
  -co BLOCKSIZE=256 -co TILING_SCHEME=GoogleMapsCompatible \
  -co COMPRESS=JPEG -co ADD_ALPHA=NO -dstnodata NaN
```
:::

## 8.3 Linking Raster Datasets to Data Models

Add a Raster Dataset to a Data Model's **Raster Layers** multi-select to make it available as an optional map layer in the explorer. Only approved Raster Datasets appear in this selector.
