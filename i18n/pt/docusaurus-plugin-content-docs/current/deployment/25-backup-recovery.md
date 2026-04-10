---
sidebar_position: 25
title: "Cópia de Segurança e Recuperação"
---

# 25. Cópia de Segurança e Recuperação

## 25.1 Cópia de Segurança da Base de Dados

```bash
# Cópia de segurança
sudo -u postgres pg_dump proenergia_db > copia_seguranca_$(date +%Y%m%d).sql

# Restauro
sudo -u postgres psql proenergia_db < copia_seguranca_20240101.sql
```

## 25.2 Cópia de Segurança de Ficheiros de Média

```bash
# Cópia de segurança de todos os ficheiros carregados e PMTiles
tar -czf copia_seguranca_media_$(date +%Y%m%d).tar.gz /var/www/proenergia/app/media/

# Cópia de segurança da configuração do ambiente
cp /var/www/proenergia/app/.env ~/copia_seguranca_env_$(date +%Y%m%d)
```

## 25.3 Ajuste de Desempenho do PostgreSQL

O script `01` aplica automaticamente optimizações do PostgreSQL baseadas na RAM do sistema: `shared_buffers`, `work_mem`, `maintenance_work_mem`, `effective_cache_size`, `max_connections`, definições de checkpoint e parâmetros de autovacuum.

Para monitorizar consultas lentas:

```sql
SELECT query, total_exec_time, calls
FROM pg_stat_statements
ORDER BY total_exec_time DESC
LIMIT 10;
```
