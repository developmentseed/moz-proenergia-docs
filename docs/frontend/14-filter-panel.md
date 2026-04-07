---
sidebar_position: 14
title: "14. The Filter Panel"
---

# 14. The Filter Panel

## 14.1 Overview

The Filter Panel contains all filter controls defined in the Data Model's `filter_fields` configuration. Filters simultaneously narrow the features displayed on the map and update the Analysis Summary statistics.

## 14.2 Administrative Area Filters

Geographic filters are rendered as searchable multi-select **Combobox** controls for columns matching administrative geography keywords. The Mozambique administrative hierarchy:

- **Province** (Província / Região)
  - **District** (Distrito)
    - **Administrative Post** (Posto Administrativo)
      - **Locality** (Localidade)

## 14.3 Technology / Category Filters

**Checkbox** filters are shown for string-valued columns. By default all values are selected (visible). Uncheck any value to hide features with that value. Values are colour-coded consistently with the map legend.

## 14.4 Numeric Range Filters

**Dual text-input range** controls are shown for numeric columns. Enter a minimum and/or maximum to restrict the displayed features.

Common uses: Settlement Population, Investment Cost, Distance to Grid.

:::tip
Combine range filters with technology checkboxes — e.g. all mini-grid sites with population over 1,000 and investment cost under $500,000.
:::

## 14.5 Applying and Clearing Filters

Filter changes are **staged**. A visual indicator on each filter shows pending or active (changed from default) state.

- Click **Apply** to commit all pending changes.
- Click **Reset** to clear all filters to their defaults.

Applied filter state is encoded in the URL for bookmarking and sharing.
