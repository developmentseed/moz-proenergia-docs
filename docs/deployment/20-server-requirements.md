---
sidebar_position: 20
title: "Server Requirements"
---

# 20. Server Requirements and Prerequisites

**OS:** Ubuntu 24.04 LTS (recommended). Minimum 4 GB RAM; 16 GB+ recommended for production.

| Requirement | Details |
|---|---|
| Domain | A registered domain name with DNS pointing to the server's public IP. |
| Python | 3.12+ (installed by setup script). |
| PostgreSQL 16 + PostGIS | Database. PostGIS required for spatial queries. |
| RabbitMQ | Message broker for Celery. |
| GDAL / gdal-bin | Geospatial file format conversion (`ogr2ogr`). |
| Tippecanoe | PMTiles generation from vector data. |
| Nginx | Web server / reverse proxy. |
| Certbot | Let's Encrypt SSL certificate management. |

All requirements are installed automatically by the setup scripts.
