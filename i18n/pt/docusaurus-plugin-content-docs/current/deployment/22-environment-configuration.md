---
sidebar_position: 22
title: "Configuração do Ambiente"
---

# 22. Configuração do Ambiente

O ficheiro `.env` é gerado automaticamente pelo script `01` e colocado em `/var/www/proenergia/app/.env`. Variáveis principais:

| Variável | Descrição |
|---|---|
| `DJANGO_SECRET_KEY` | Chave secreta Django gerada automaticamente. Nunca partilhe nem confirme em repositório. |
| `DJANGO_DEBUG` | Defina como `False` em produção. |
| `DATABASE_URL` | String de ligação PostGIS. Formato: `postgis://utilizador:palavra-passe@localhost:5432/proenergia_db` |
| `ALLOWED_HOSTS` | Nomes de host permitidos separados por vírgulas (o seu domínio e subdomínio www). |
| `CSRF_TRUSTED_ORIGINS` | Origens de confiança separadas por vírgulas para protecção CSRF. |
| `STATIC_ROOT` | Caminho do sistema de ficheiros onde `collectstatic` escreve ficheiros estáticos. |
| `MEDIA_ROOT` | Caminho do sistema de ficheiros onde os ficheiros carregados e PMTiles são armazenados. |
| `CELERY_BROKER_URL` | Ligação RabbitMQ: `amqp://proenergia:<palavra-passe>@localhost:5672/proenergia_vhost` |
| `CELERY_WORKERS` | Número de processos trabalhadores Celery (predefinição: 2). |
| `CELERY_WORKER_CONCURRENCY` | Concorrência por trabalhador (predefinição: 4). |
| `CACHE_BACKEND` | Backend de cache da base de dados: `django.core.cache.backends.db.DatabaseCache` |
| `CACHE_LOCATION` | Nome da tabela de cache: `summaries_cache_table` |

:::warning Segurança
O ficheiro `.env` tem permissões `600` (apenas leitura/escrita do proprietário). Nunca o confirme no controlo de versão.
:::

:::note Nome da base de dados
A base de dados de produção chama-se `proenergia_db` (não `proenergia`). O vhost RabbitMQ é `proenergia_vhost`. Estes diferem de uma configuração típica de desenvolvimento local.
:::
