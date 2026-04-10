---
sidebar_position: 20
title: "Requisitos do Servidor"
---

# 20. Requisitos do Servidor e Pré-requisitos

**SO:** Ubuntu 24.04 LTS (recomendado). Mínimo de 4 GB de RAM; 16 GB+ recomendado para produção.

| Requisito | Detalhes |
|---|---|
| Domínio | Um nome de domínio registado com DNS a apontar para o IP público do servidor. |
| Python | 3.12+ (instalado pelo script de configuração). |
| PostgreSQL 16 + PostGIS | Base de dados. PostGIS necessário para consultas espaciais. |
| RabbitMQ | Intermediário de mensagens para Celery. |
| GDAL / gdal-bin | Conversão de formato de ficheiros geoespaciais (`ogr2ogr`). |
| Tippecanoe | Geração de PMTiles a partir de dados vectoriais. |
| Nginx | Servidor web / proxy inverso. |
| Certbot | Gestão de certificados SSL Let's Encrypt. |

Todos os requisitos são instalados automaticamente pelos scripts de configuração.
