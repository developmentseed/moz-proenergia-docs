---
sidebar_position: 25
title: "Backup & Recovery"
---

# 25. Backup and Recovery

## 25.1 Database Backup

```bash
# Backup
sudo -u postgres pg_dump proenergia_db > backup_$(date +%Y%m%d).sql

# Restore
sudo -u postgres psql proenergia_db < backup_20240101.sql
```

## 25.2 Media Files Backup

```bash
# Backup all uploaded files and PMTiles
tar -czf media_backup_$(date +%Y%m%d).tar.gz /var/www/proenergia/app/media/

# Backup the environment config
cp /var/www/proenergia/app/.env ~/env_backup_$(date +%Y%m%d)
```

## 25.3 PostgreSQL Performance Tuning

Script `01` automatically applies PostgreSQL optimizations based on system RAM: `shared_buffers`, `work_mem`, `maintenance_work_mem`, `effective_cache_size`, `max_connections`, checkpoint settings, and autovacuum parameters.

To monitor slow queries:

```sql
SELECT query, total_exec_time, calls
FROM pg_stat_statements
ORDER BY total_exec_time DESC
LIMIT 10;
```
