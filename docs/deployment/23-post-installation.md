---
sidebar_position: 23
title: "23. Post-Installation Setup"
---

# 23. Post-Installation Setup

## 23.1 Create Django Admin Superuser

```bash
cd /var/www/proenergia/app
source venv/bin/activate
python manage.py createsuperuser
```

## 23.2 Configure GitHub Webhook (Optional)

Script `03` generates a webhook secret displayed at the end of its output (also saved to `/var/www/proenergia/webhook_secret.txt`).

1. Go to **GitHub repository → Settings → Webhooks → Add webhook**.
2. Set **Payload URL** to `https://your-domain.com/deploy-webhook`.
3. Set **Content type** to `application/json`.
4. Paste the webhook secret into the **Secret** field.
5. Select **Just the push event**. Click **Add webhook**.

## 23.3 systemd Services

| Service | Purpose |
|---|---|
| `proenergia.service` | Gunicorn WSGI application server. Serves the Django REST API. |
| `proenergia-celery.service` | Celery worker. Processes PMTiles generation and CSV import tasks. |
| `proenergia-celerybeat.service` | Celery Beat scheduler. Handles periodic/scheduled tasks. |
| `proenergia-webhook.service` | Webhook listener for automated git-push deployments. |

```bash
# Status and logs
sudo systemctl status proenergia
sudo journalctl -u proenergia -f
sudo journalctl -u proenergia-celery -f

# Restart after changes
sudo systemctl restart proenergia
sudo systemctl restart proenergia-celery
sudo systemctl restart proenergia-celerybeat
```
