---
id: intro
sidebar_position: 1
title: Introduction
---

# IEP PROENERGIA+ Platform User Guide

**MIREME UIPCE · SE4ALL · Development Seed** — Version 1.2 · 2026

PROENERGIA+ IEP is a spatial data infrastructure and visualization platform for integrated electrification planning in Mozambique. It enables national and provincial decision-makers to explore energy access scenarios using the latest geospatial data, analyze settlement-level outcomes, and export actionable insights.

This guide is divided into three parts:

- **[Backend](./backend/accessing-admin)** — Django Admin interface, user management, data model configuration, scenario and dataset management, JSON configuration, and API reference.
- **[Frontend](./frontend/interface-overview)** — Visualization interface, filter controls, map interaction, scenario selection, analysis summaries, and downloads.
- **[Deployment](./deployment/server-requirements)** — Server setup, systemd services, Nginx, Celery, RabbitMQ, environment variables, and update procedures.

## System Architecture

| Component | Description |
|-----------|-------------|
| Backend API (Django REST) | Serves data to the frontend. Django + DRF, backed by PostgreSQL 16 / PostGIS. Admin at `/admin/`. API at `/api/v1/`. |
| Task Queue (Celery / RabbitMQ) | Background workers for file conversion (GDAL → FlatGeobuf → PMTiles via Tippecanoe). |
| Frontend (Next.js / TypeScript) | MapLibre GL mapping + Chakra UI. Supports English and Portuguese (default). |
| File Storage | Stores uploaded source files and derived PMTiles. |
| Tile Delivery (PMTiles) | Vector tiles via HTTP range requests. Raster layers via Cloud-Optimized GeoTIFF (COG). |
