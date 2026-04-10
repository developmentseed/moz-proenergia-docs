---
sidebar_position: 26
title: "Deployment Troubleshooting"
---

# 26. Deployment Troubleshooting

| Issue | Cause & Resolution |
|---|---|
| 502 Bad Gateway from Nginx | Gunicorn not running. Check: `sudo systemctl status proenergia`. View logs: `sudo journalctl -u proenergia -n 50` |
| PMTiles not generating | Celery worker not running. Check: `sudo systemctl status proenergia-celery`. Also verify RabbitMQ: `sudo rabbitmqctl status` |
| Connection refused to RabbitMQ | RabbitMQ stopped. Run: `sudo systemctl start rabbitmq-server` |
| Database connection errors | Check `DATABASE_URL` in `.env`. Verify PostgreSQL: `sudo systemctl status postgresql` |
| Settings import errors at startup | `DJANGO_SECRET_KEY` is not set. Verify `.env` exists and is readable by the `proenergia` user. |
| Static files returning 404 | Run: `python manage.py collectstatic --noinput`. Verify Nginx serves the `STATIC_ROOT` path. |
| Migrations fail on restart | Run `migrate` manually and check for errors before restarting services. |
| Translation errors (compilemessages) | `gettext` tools may be missing. Install: `sudo apt install gettext`. Then rerun `compilemessages`. |
| SSL certificate issues | Run: `sudo certbot renew --dry-run`. Check Nginx config: `sudo nginx -t` |
| Webhook not triggering | Check: `sudo systemctl status proenergia-webhook`. View secret: `sudo cat /var/www/proenergia/webhook_secret.txt`. Check GitHub webhook delivery logs. |
| Database cache table missing | Run: `python manage.py createcachetable`. The table `summaries_cache_table` must exist for the application to start. |
