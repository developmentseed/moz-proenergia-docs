---
sidebar_position: 21
title: "Deployment Overview"
---

# 21. Deployment Overview: Five-Script Process

The `deploy/scripts/` directory contains five numbered shell scripts that automate the full deployment. Run them in order.

## Quick Start

```bash
git clone https://github.com/developmentseed/moz-proenergia-backend.git
cd moz-proenergia-backend/deploy/scripts
chmod +x *.sh

./00_setup_system.sh
./01_setup_infrastructure.sh your-domain.com       # DOMAIN REQUIRED
sudo -u proenergia ./02_setup_application.sh
./03_setup_services.sh your-domain.com admin@email  # DOMAIN + optional email
./04_verify_setup.sh
```

## Script Reference

| Script | Run as | Purpose |
|---|---|---|
| `00_setup_system.sh` | root | Install system packages (Python, PostgreSQL 16+PostGIS, RabbitMQ, Nginx, Certbot, Tippecanoe, GDAL). Create `proenergia` system user and application directories. |
| `01_setup_infrastructure.sh <domain>` | root | Configure PostgreSQL (DB, user, PostGIS + pg_trgm + unaccent extensions, optimize settings). Configure RabbitMQ (dedicated user + vhost). Generate Django secret key. Write complete `.env` file to `/var/www/proenergia/app/.env`. **Save the displayed credentials.** |
| `02_setup_application.sh` | proenergia user | Clone repo to `/var/www/proenergia/app`. Create Python virtualenv, install requirements. Run `migrate`, `createcachetable`, `collectstatic`, `compilemessages`. |
| `03_setup_services.sh <domain> [email]` | root | Install nginx config, Gunicorn service, Celery services, webhook listener. Generate webhook secret. Install SSL via certbot. Configure firewall. Start all services. |
| `04_verify_setup.sh` | any | Verify all services running, database connection, file permissions, web accessibility. Prints pass/fail summary. |

:::warning Order matters
Scripts must be run in sequence. Script `01` generates the `.env` file that script `02` requires. Script `02` installs the application files that script `03` configures.
:::

## File Locations

| Path | Description |
|---|---|
| `/var/www/proenergia/app/` | Application root |
| `/var/www/proenergia/app/.env` | Environment configuration (chmod 600) |
| `/var/www/proenergia/app/staticfiles/` | Collected static files |
| `/var/www/proenergia/app/media/` | Uploaded files and PMTiles |
| `/var/log/proenergia/` | Application logs |
| `/etc/nginx/sites-available/proenergia.conf` | Nginx configuration |
| `/etc/systemd/system/proenergia*.service` | systemd service files |
