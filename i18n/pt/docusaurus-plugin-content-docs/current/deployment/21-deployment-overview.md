---
sidebar_position: 21
title: "Visão Geral da Implantação"
---

# 21. Visão Geral da Implantação: Processo de Cinco Scripts

O directório `deploy/scripts/` contém cinco scripts shell numerados que automatizam a implantação completa. Execute-os por ordem.

## Início Rápido

```bash
git clone https://github.com/developmentseed/moz-proenergia-backend.git
cd moz-proenergia-backend/deploy/scripts
chmod +x *.sh

./00_setup_system.sh
./01_setup_infrastructure.sh o-seu-dominio.com       # DOMÍNIO NECESSÁRIO
sudo -u proenergia ./02_setup_application.sh
./03_setup_services.sh o-seu-dominio.com admin@email  # DOMÍNIO + email opcional
./04_verify_setup.sh
```

## Referência de Scripts

| Script | Executar como | Propósito |
|---|---|---|
| `00_setup_system.sh` | root | Instalar pacotes do sistema (Python, PostgreSQL 16+PostGIS, RabbitMQ, Nginx, Certbot, Tippecanoe, GDAL). Criar utilizador de sistema `proenergia` e directórios de aplicação. |
| `01_setup_infrastructure.sh <domínio>` | root | Configurar PostgreSQL (BD, utilizador, extensões PostGIS + pg_trgm + unaccent, optimizar definições). Configurar RabbitMQ (utilizador dedicado + vhost). Gerar chave secreta Django. Escrever ficheiro `.env` completo em `/var/www/proenergia/app/.env`. **Guarde as credenciais apresentadas.** |
| `02_setup_application.sh` | utilizador proenergia | Clonar repositório para `/var/www/proenergia/app`. Criar virtualenv Python, instalar requisitos. Executar `migrate`, `createcachetable`, `collectstatic`, `compilemessages`. |
| `03_setup_services.sh <domínio> [email]` | root | Instalar configuração nginx, serviço Gunicorn, serviços Celery, ouvinte de webhook. Gerar segredo de webhook. Instalar SSL via certbot. Configurar firewall. Iniciar todos os serviços. |
| `04_verify_setup.sh` | qualquer | Verificar todos os serviços em execução, ligação à base de dados, permissões de ficheiros, acessibilidade web. Imprime resumo de aprovação/reprovação. |

:::warning A ordem importa
Os scripts devem ser executados em sequência. O script `01` gera o ficheiro `.env` que o script `02` requer. O script `02` instala os ficheiros de aplicação que o script `03` configura.
:::

## Localizações de Ficheiros

| Caminho | Descrição |
|---|---|
| `/var/www/proenergia/app/` | Raiz da aplicação |
| `/var/www/proenergia/app/.env` | Configuração do ambiente (chmod 600) |
| `/var/www/proenergia/app/staticfiles/` | Ficheiros estáticos recolhidos |
| `/var/www/proenergia/app/media/` | Ficheiros carregados e PMTiles |
| `/var/log/proenergia/` | Registos da aplicação |
| `/etc/nginx/sites-available/proenergia.conf` | Configuração Nginx |
| `/etc/systemd/system/proenergia*.service` | Ficheiros de serviço systemd |
