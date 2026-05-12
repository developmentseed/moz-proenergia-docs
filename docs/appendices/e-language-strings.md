---
sidebar_position: 104
title: "Appendix E — Updating Language Strings"
---

# Appendix E — Updating Frontend Language Strings

The PROENERGIA+ frontend supports **Portuguese** (default) and **English**. This appendix is a complete reference for anyone who needs to add, edit, or translate user-facing text in the application.

There are three distinct translation mechanisms depending on the type of content. Understanding which one applies to your change is the first step.

| Content type | Mechanism | Where translations live |
|---|---|---|
| UI strings (buttons, labels, messages) | i18next locale JSON files | `src/i18n/locales/{en,pt}.json` |
| Backend data (model/scenario/layer names) | `_pt` fields read directly via `useLocalize` | `src/utils/i18n.ts` |
| Long-form page content | Locale-specific MDX files | `src/app/<page>/<slug>.pt.mdx` |

---

## 1. UI Strings (i18next Locale Files)

All static interface text — navigation labels, button text, error messages, placeholder text, and field labels — lives in two JSON files:

- `src/i18n/locales/en.json` — English strings
- `src/i18n/locales/pt.json` — Portuguese strings

The application defaults to Portuguese on first load. If a Portuguese string is missing for a given key, i18next silently falls back to the English value.

### Namespace structure

Strings are organised into namespaces based on the area of the interface they belong to. Both JSON files must use identical key structures.

| Namespace | Covers |
|---|---|
| `nav` | Header navigation links, login/logout labels, site name |
| `home` | Landing page heading, description, call-to-action buttons |
| `auth.login` | Login form fields, validation messages, success feedback |
| `auth.logout` | Logout button and confirmation |
| `explorer` | Model panel, scenario selector, Controls/Layers tabs, filter Apply/Reset, error states |
| `downloads` | Search placeholder, card metadata labels, download button |
| `filters` | Combobox placeholder, selected-count display, empty state |
| `map` | Legend title, additional layers panel label |
| `models` | Model listing page strings |
| `breadcrumbs` | Page-level breadcrumb labels |

### How to edit an existing string

1. Open both `src/i18n/locales/en.json` and `src/i18n/locales/pt.json`.
2. Find the key you want to change. Keys follow the pattern `{namespace}.{context}.{element}`.
3. Update the value in **both files**.
4. Save and the change is live on next build (or hot-reloaded in dev).

**Example:** Changing the download button label.

```json
// en.json
{
  "downloads": {
    "download": "Download"
  }
}

// pt.json
{
  "downloads": {
    "download": "Baixar"
  }
}
```

### How to add a new string

1. Choose the appropriate namespace, or add a new top-level key if your feature doesn't fit an existing one.
2. Add the key and its value to **both** `en.json` and `pt.json`.
3. Use the string in your component with `useTranslation()`. The component must be a `"use client"` file.

```tsx
"use client";
import { useTranslation } from "react-i18next";

function MyComponent() {
  const { t } = useTranslation();
  return <button>{t("explorer.newButton")}</button>;
}
```

:::warning Both files must stay in sync
Missing keys fall back to English silently — there is no runtime error. Always add the key to both files at the same time. If you add a namespace to one file, add it to the other too and update this table above.
:::

### Dynamic values (interpolation)

Use `{{variable}}` placeholders — never string concatenation.

```json
// en.json
{ "filters": { "selected": "{{count}} selected" } }

// pt.json
{ "filters": { "selected": "{{count}} selecionados" } }
```

```tsx
t("filters.selected", { count: 5 })   // → "5 selected" or "5 selecionados"
```

### The `labels` namespace — data field labels

The `labels` namespace maps CSV column names to human-readable labels and descriptions. This is how generic column names like `Admin_1` or `ElecStart` get displayed in filters and popups.

```json
// en.json
{
  "labels": {
    "Admin_1": { "label": "Province", "description": "Administrative level 1" },
    "Technology2030": { "label": "Technology", "description": "Chosen least-cost technology" }
  }
}

// pt.json
{
  "labels": {
    "Admin_1": { "label": "Província", "description": "Nível administrativo 1" },
    "Technology2030": { "label": "Tecnologia", "description": "Tecnologia de menor custo" }
  }
}
```

To add a label for a new CSV column, add its key to both locale files under `labels`. The key must exactly match the column name as it appears in the scenario CSV data (case-sensitive).

---

## 2. Backend Data Names and Descriptions

Model names, scenario names, layer names, and their descriptions come from the Django backend API. These are translated using `_pt` companion fields on each database record — not in the frontend locale files.

### Where to set translations

All translations for backend data are set in the **Django Admin interface**. When you open the edit form for a Data Model, Vector Dataset, Scenario, or similar record, the name and description fields appear as tabbed inputs — one tab per language.

| Admin record type | Translatable fields |
|---|---|
| Data Model | Name, Description |
| Scenario | Name |
| Vector Dataset | Name, Description |
| Raster Dataset | Name, Description |
| Reference Dataset | Name, Description |

### How it works in the frontend

`src/utils/i18n.ts` exports a single hook:

```ts
import { useLocalize } from "@/utils/i18n";

function MyComponent({ layer }: { layer: Layer }) {
  const localize = useLocalize();
  return <Text>{localize(layer.label, layer.label_pt)}</Text>;
}
```

`localize(en, pt)` returns `pt` when the active language is Portuguese and `pt` is non-empty, otherwise returns `en`.

Reactivity is automatic: `useLocalize` calls `useTranslation()` internally, so the component re-renders whenever the user switches language.

### API fields by entity

| Entity | EN field | PT field |
|--------|----------|----------|
| Model (group list) | `name`, `description` | `name_pt`, `description_pt` |
| Model (detail) | `name`, `description` | `name_pt`, `description_pt` |
| Scenario | `name` / `label`, `description` | `name_pt`, `description_pt` |
| Vector / raster layer | `label`, `description` | `label_pt`, `description_pt` |
| Filter / popup / summary field | `label`, `description` | `label_pt`, `description_pt` |


### Missing translations

If a `_pt` field is `null` or absent in the API response, `localize()` automatically falls back to the English value. No special handling is needed in components. To fix a missing translation, populate the `_pt` field in the backend admin.


### To update a translated name or description

1. Log into the Django Admin at `/admin/`.
2. Navigate to the relevant record (e.g. Datasets → Data Models → select the model).
3. Click the language tab (EN / PT) above the Name or Description field.
4. Enter or update the translation in the Portuguese tab.
5. Click **Save**.

The change is reflected in the frontend on the next page load (or after the API cache expires).

:::note No code change required
Updating backend data translations requires only a Django Admin edit — no code deployment is needed unless there is new API entity types with `_pt` fields.
:::

---

## 3. Long-Form Page Content (MDX Files)

Pages with substantial written content — such as the About page — use locale-specific MDX files rather than translation keys. This is appropriate for content that is more like an article than a UI label.

### File naming convention

```
src/app/<page>/<slug>.mdx        ← English (default)
src/app/<page>/<slug>.pt.mdx     ← Portuguese
```

### Current MDX pages

| Route | English file | Portuguese file |
|---|---|---|
| `/about` | `src/app/about/about.mdx` | `src/app/about/about.pt.mdx` |

### How page language switching works

The page component imports both files and serves the correct one based on the user's active language:

```tsx
"use client";
import { useTranslation } from "react-i18next";
import ContentEn from "./about.mdx";
import ContentPt from "./about.pt.mdx";

export default function Page() {
  const { i18n } = useTranslation();
  const Content = i18n.language?.startsWith("pt") ? ContentPt : ContentEn;
  return <Content />;
}
```

### To update page content

1. Edit the appropriate `.mdx` file directly in the repository.
2. If you are adding new content in English, add the corresponding Portuguese content to the `.pt.mdx` file at the same time.
3. Commit and push — the change is live after the next deployment.

### To add a new bilingual content page

1. Create `src/app/<page>/<slug>.mdx` with the English content.
2. Create `src/app/<page>/<slug>.pt.mdx` with the Portuguese content.
3. Create `src/app/<page>/page.tsx` following the pattern above to switch between the two files based on language.
4. Add the route to the Docusaurus sidebar if it is a documentation page, or to the application navigation if it is a frontend page.

---

## 4. Language Switcher

Users switch between Portuguese and English using the **PT / EN** toggle button in the top-right of the application header. The preference is stored in `localStorage` under the key `language` and persists across browser sessions.

The default language on first visit (when no preference is stored) is **Portuguese**:

```ts
// src/i18n/config.ts
if (typeof window !== 'undefined' && !localStorage.getItem('language')) {
  i18next.changeLanguage('pt');
}
```

There is no server-side language detection. The language is always resolved client-side from localStorage.

---

## 5. Checklist for Any i18n Change

Before submitting a pull request that touches any user-facing text, verify:

- [ ] Both `en.json` and `pt.json` have the same keys. Missing keys fall back to English silently.
- [ ] No user-facing string is hardcoded in JSX — use `t()` for UI strings, `useLocalize` for data fields.
- [ ] Components using `t()`, `useTranslation`, or `useLocalize` are marked `"use client"`.
- [ ] Strings use `{{variable}}` interpolation, never string concatenation.
- [ ] If you added a new namespace, the table in Section 1 of this appendix has been updated.
- [ ] If you updated a backend record's translation, the change has been saved in the Django Admin and verified in the frontend at both `/en` and `/pt` language settings.
- [ ] If you added or updated an MDX page, both the `.mdx` and `.pt.mdx` files have been updated.