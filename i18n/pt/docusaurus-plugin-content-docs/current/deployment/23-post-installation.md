---
sidebar_position: 23
title: "Configuração Pós-Instalação"
---

# 23. Configuração Pós-Instalação

## 23.1 Criar Superutilizador do Painel de Administração Django

```bash
cd /var/www/proenergia/app
source venv/bin/activate
python manage.py createsuperuser
```

## 23.2 Configurar Webhook do GitHub (Opcional)

O script `03` gera um segredo de webhook apresentado no final da sua saída (também guardado em `/var/www/proenergia/webhook_secret.txt`).

1. Vá a **Repositório GitHub → Definições → Webhooks → Adicionar webhook**.
2. Defina o **URL de Payload** como `https://o-seu-dominio.com/deploy-webhook`.
3. Defina o **Tipo de conteúdo** como `application/json`.
4. Cole o segredo do webhook no campo **Segredo**.
5. Seleccione **Apenas o evento de push**. Clique em **Adicionar webhook**.

## 23.3 Serviços systemd

| Serviço | Propósito |
|---|---|
| `proenergia.service` | Servidor de aplicação WSGI Gunicorn. Serve a API REST Django. |
| `proenergia-celery.service` | Trabalhador Celery. Processa tarefas de geração de PMTiles e importação de CSV. |
| `proenergia-celerybeat.service` | Agendador Celery Beat. Trata de tarefas periódicas/agendadas. |
| `proenergia-webhook.service` | Ouvinte de webhook para implantações automatizadas via git push. |

```bash
# Estado e registos
sudo systemctl status proenergia
sudo journalctl -u proenergia -f
sudo journalctl -u proenergia-celery -f

# Reiniciar após alterações
sudo systemctl restart proenergia
sudo systemctl restart proenergia-celery
sudo systemctl restart proenergia-celerybeat
```
