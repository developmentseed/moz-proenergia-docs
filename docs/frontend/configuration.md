---
title: "Frontend Configuration"
---

# Frontend Configuration

Not all platform behaviour is controlled the same way. This page draws a clear line between settings that are **managed through the Django Admin** (and take effect immediately without any code change) and settings that are **hardcoded in the frontend codebase** (and require a code change and redeployment to update).

Understanding this distinction matters when onboarding new models, updating branding, or diagnosing why a change you made in the admin isn't appearing as expected.

---

## What the Admin Controls (no deployment needed)

The following are entirely driven by the Django Admin and served to the frontend via the API. Changing them in the admin takes effect on the next page load.

| Setting | Where to change it | API field |
|---|---|---|
| Filter labels, descriptions, and column mappings | Data Model → Filter Fields (JSON) | `filter_fields` |
| Map popup attribute list | Data Model → Popup Fields (JSON) | `popup_fields` |
| Summary panel statistics and charts | Data Model → Summary Fields (JSON) | `summary_fields` |
| Map feature colour coding | Data Model → Color Coding (JSON) | `color_coding` |
| Visualization column (which column drives colour) | Data Model → Visualization Column | `visualization_column` |
| Model names and descriptions (EN + PT) | Data Model → Name / Description fields | `name`, `name_pt`, `description_pt` |
| Scenario names (EN + PT) | Scenario → Name fields | `name`, `name_pt` |
| Dataset names and descriptions (EN + PT) | Vector/Raster/Reference Dataset admin | `name`, `name_pt`, `description_pt` |
| Which vector/raster/reference datasets appear per model | Data Model → Contextual Layers / Raster Layers / Reference Datasets | M2M fields |
| Whether a model is publicly visible | Data Model → Is Public | `is_public` |

See [JSON Configuration Fields](/backend/json-configuration) for the full schema reference for filter, popup, summary, and colour coding configuration.

---

## What the Frontend Code Controls (deployment required)

The following are set in files under `src/config/` in the frontend repository. Changing them requires editing the file, committing, and deploying.

### `map.json` — Map Zoom Levels and Tile Layer Name

**File:** `src/config/map.json`  
**Status:** Active — imported in `map/index.tsx`, `map/main-layer.tsx`, and `utils/data-transformation.ts`

```json
{
  "minZoom": 5,
  "polygonMinZoom": 7,
  "maxZoom": 11,
  "sourceLayerName": "data"
}
```

| Key | Effect | When to change |
|---|---|---|
| `minZoom` | The minimum zoom level the map allows and the minimum zoom embedded in PMTiles source definitions | If tile generation settings change |
| `polygonMinZoom` | The zoom level at which polygon fill, line, and circle layers become visible | If you want features to appear earlier or later on zoom |
| `maxZoom` | Currently commented out in tile source definitions — not actively applied | N/A for now |
| `sourceLayerName` | The PMTiles internal layer name that all map layers read from | Must match the `-l` argument passed to Tippecanoe during tile generation. Currently `"data"`. Only change this if you regenerate all tiles with a different layer name |

:::warning
`sourceLayerName` must match exactly what Tippecanoe writes into the PMTiles files. If they differ, no features will appear on the map. The current value `"data"` corresponds to the `-l data` flag in the `call_tippecanoe` function in `tasks.py`.
:::

### `model.json` — Icon Assignment per Model

**File:** `src/config/model.json`  
**Status:** Active — read by `utils/model-icon.ts` → `getIconPath()`, which is called by `side-nav.tsx` and `model-switcher-menu.tsx`

```json
[
  { "model": 1, "icon": "lightbulb.svg" },
  { "model": 2, "icon": "tractor.svg" },
  { "model": 3, "icon": "grid-3x3.svg" },
  { "model": 4, "icon": "landmark.svg" },
  { "model": 5, "icon": "cooking-pot.svg" }
]
```

Each entry maps a Data Model's numeric database ID to an SVG icon filename. The icons live in `public/model-icon/`. If no entry matches a model's ID, `default.svg` is used.

**When to change:** When a new Data Model is created in the admin and you want it to have a specific icon in the sidebar. Add a new entry with the model's ID (visible in the Django Admin URL when viewing the model: `/admin/datasets/datamodel/<id>/change/`) and the filename of an SVG in `public/model-icon/`.

Available icons: `lightbulb.svg`, `tractor.svg`, `grid-3x3.svg`, `landmark.svg`, `cooking-pot.svg`, `default.svg`. To add a new icon, place the SVG file in `public/model-icon/` and reference it here.

### `website.ts` — Site Title, Description, and SDI Portal URL

**File:** `src/config/website.ts`  
**Status:** Active — `WEBSITE_TITLE` and `WEBSITE_DESC` used in `app/layout.tsx` for the HTML `<title>` and meta description; `SDI_PORTAL_URL` used in the header dropdown menu

```ts
export const WEBSITE_TITLE = "Plataforma Integrada de Electrificação de Moçambique - PIE";
export const WEBSITE_DESC = "Proenergia";
export const SDI_PORTAL_URL = "https://proenergia-staging.ds.io/admin/";
```

| Export | Effect | When to change |
|---|---|---|
| `WEBSITE_TITLE` | The browser tab title and OpenGraph title for the site | On rebrand or when moving from staging to production |
| `WEBSITE_DESC` | The HTML meta description (used by search engines and link previews) | On rebrand or content update |
| `SDI_PORTAL_URL` | The URL the "SDI Portal" link in the header dropdown navigates to | **Must be updated from the staging URL to the production admin URL before launch** |

:::warning Update SDI_PORTAL_URL before production launch
The current value points to the staging Django Admin (`proenergia-staging.ds.io/admin/`). This must be changed to the production admin URL before the platform goes live.
:::

### `filters.ts` — Degree-Based Filter Sort Order

**File:** `src/config/filters.ts`  
**Status:** Active — `sortFilterOptions()` is imported and called in `utils/data-transformation.ts` when building checkbox filter option lists

This file defines a priority ordering for qualitative degree values so they appear in a logical sequence (Very High → High → Medium → Low → Very Low) rather than alphabetically in filter dropdowns.

```ts
const DEGREE_ORDER = {
  'very high': 0,
  'high': 1,
  'medium': 2,
  'low': 3,
  'very low': 4,
};
```

Values that match these keys (case-insensitive) are sorted to the top of checkbox filter lists, in the order defined. All other values appear after, in their original API response order.

**When to change:** Rarely. Only if a new dataset introduces different degree-scale values that should be sorted in a specific order, or if the existing order needs adjustment.

### `api.ts` — API and Media URL Endpoints

**File:** `src/utils/api.ts` (not in `/config` but functionally equivalent)  
**Status:** Active — used throughout the application for all API calls and media file URL construction

```ts
export const API_ENDPOINT = 'https://proenergia-staging.ds.io/api/v1/';
export const MEDIA_URL_PREFIX = 'https://proenergia-staging.ds.io/media/';
```

| Export | Effect |
|---|---|
| `API_ENDPOINT` | Base URL for all REST API requests (models, scenarios, datasets, summaries) |
| `MEDIA_URL_PREFIX` | Prepended to raw file paths returned by the API to construct full PMTiles and media URLs |

:::warning Also requires updating before production launch
Both values currently point to the staging server. They must be updated to production URLs before deployment.
:::

---

- **Filter, popup, and summary field labels** → set in the Data Model's `filter_fields`, `popup_fields`, and `summary_fields` JSON configuration in the admin
- **Shared column labels** → set in `src/i18n/locales/en.json` and `src/i18n/locales/pt.json` under the `labels` namespace

See [Appendix E — Updating Language Strings](../appendices/e-language-strings) for how to update the locale files.


---

## Summary

| File | Status | Change requires deployment? |
|---|:---:|:---:|
| `map.json` | Active | Yes |
| `model.json` | Active | Yes |
| `website.ts` | Active | Yes |
| `filters.ts` | Active | Yes |
| `api.ts` (in `/utils`) | Active | Yes |
| Django Admin → Data Model JSON fields | Active | **No** |
| Django Admin → Dataset/Scenario names | Active | **No** |