---
title: "The Analysis Summary Panel"
---

# The Analysis Summary Panel

## Overview

The Analysis Summary Panel displays aggregated statistics that update in real time when filters are applied. All statistics correspond to entries in the Data Model's `summary_fields` configuration.

## Statistics Display Formats

| Display type | When shown |
|---|---|
| **Single value (flat)** | Single column, no `group_by`, no `chartType`. Shows the computed value with optional unit. |
| **Group breakdown** | `group_by` set but no `chartType`. Shows value per group as a labelled list. |
| **Chart** (bar/donut/stacked/column/area) | `chartType` set. Shows an interactive chart. `showChartValueRows: true` adds a table beneath. |
| **Highlight** | `chartType: "highlight"`. Shows a prominent single-value highlight card. |
| **Multi-column group** | `columns` has multiple entries. Each column is a sub-row aggregated by `method`. |
| **Nested group** | `group_by` set to two columns. Shows a two-level grouped breakdown. |

## Summary Categories

Items sharing the same `category` value are grouped under a collapsible heading in the summary panel.
