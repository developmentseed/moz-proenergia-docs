---
sidebar_position: 12
title: "Interface Overview"
---

# 12. Frontend Interface Overview

## 12.1 Getting Started

The PROENERGIA+ visualization interface is a web application — no installation required. It runs in any modern browser (Chrome, Firefox, Edge, or Safari).

| Access Level | What you can do |
|---|---|
| **Public (unauthenticated)** | View and explore all public, approved Data Models. Apply filters, view popups and public data. |
| **Authenticated User** | Access all public datasets plus any private approved datasets and models. Download all available datasets from the frontend. |

## 12.2 Language Selection

The platform supports **English** and **Portuguese** (default). To switch languages, click the **PT / EN** toggle in the top-right of the header. Your preference is saved in the browser and persists across sessions.

Translated content includes: navigation labels, filter labels, scenario names, model names, layer names, and all UI strings. Portuguese translations come from:
- Locale JSON files for UI strings
- The `name_pt` / `description_pt` fields set on Data Models, Scenarios, and Datasets in the administrative platform

## 12.3 Three-Panel Layout

| Panel | Location / Function |
|---|---|
| **Model Navigation Sidebar** | Far left. Lists all public Data Models with unique icons, ordered by Presentation Order. Click any icon to activate that model. |
| **Filter / Control Panel** | Left panel. Contains the scenario selector and all filter controls. Can be collapsed using the toggle button on its right edge. |
| **Map Panel** | Centre. Interactive MapLibre GL map displaying the active scenario's PMTiles vector layer. |
| **Analysis Summary Panel** | Right. Displays aggregated statistics for the current scenario and active filters. Also shows feature detail when a map feature is clicked. |
