---
sidebar_position: 15
title: "The Map Panel"
---

# 15. The Map Panel

## 15.1 Map Controls and Navigation

| Control | Description |
|---|---|
| Zoom | Scroll wheel, pinch gesture, or the +/- buttons. |
| Pan | Click and drag. |
| Re-centre | Click the re-centre button (bottom right) to return to the default Mozambique extent. |
| **Geocoder (address search)** | Search bar in the top-left. Search for place names via OpenStreetMap Nominatim. Matching locations are shown with a marker. |
| **Share button** | Copies the current page URL (including all active filters and scenario) to the clipboard for sharing. |

## 15.2 Map Controls Toolbar

| Control | Description |
|---|---|
| **Basemap selector** | Switch between light, dark, and other available basemap styles. |
| **Opacity control** | Adjust the opacity of the active scenario's data layer. |
| **Legend** | Colour key for the active visualization column. Corresponds to the `color_coding` configuration. |
| **Contextual layer panel** | Toggle individual vector layers (from Data Model's Contextual Layers) on/off. |
| **Raster layer panel** | Toggle individual raster layers (from Data Model's Raster Layers) on/off as additional map overlays. |

## 15.3 Feature Interaction

Clicking a feature on the map switches the right-hand panel to **feature detail mode**, showing the attributes configured in `popup_fields`.

The panel header shows the feature identifier. Click the **back arrow** to return to the national summary view.
