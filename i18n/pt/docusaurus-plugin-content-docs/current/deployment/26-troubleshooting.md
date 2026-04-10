---
sidebar_position: 26
title: "Resolução de Problemas de Implantação"
---

# 26. Resolução de Problemas de Implantação

| Problema | Causa e Resolução |
|---|---|
| 502 Bad Gateway do Nginx | Gunicorn não está em execução. Verifique: `sudo systemctl status proenergia`. Ver registos: `sudo journalctl -u proenergia -n 50` |
| PMTiles não estão a ser gerados | Trabalhador Celery não está em execução. Verifique: `sudo systemctl status proenergia-celery`. Também verifique RabbitMQ: `sudo rabbitmqctl status` |
| Ligação recusada ao RabbitMQ | RabbitMQ parado. Execute: `sudo systemctl start rabbitmq-server` |
| Erros de ligação à base de dados | Verifique `DATABASE_URL` no `.env`. Verifique PostgreSQL: `sudo systemctl status postgresql` |
| Erros de importação de definições no arranque | `DJANGO_SECRET_KEY` não está definido. Verifique se `.env` existe e é legível pelo utilizador `proenergia`. |
| Ficheiros estáticos retornam 404 | Execute: `python manage.py collectstatic --noinput`. Verifique se o Nginx serve o caminho `STATIC_ROOT`. |
| Migrações falham no reinício | Execute `migrate` manualmente e verifique erros antes de reiniciar os serviços. |
| Erros de tradução (compilemessages) | As ferramentas `gettext` podem estar em falta. Instale: `sudo apt install gettext`. Depois reexecute `compilemessages`. |
| Problemas com certificado SSL | Execute: `sudo certbot renew --dry-run`. Verifique configuração Nginx: `sudo nginx -t` |
| Webhook não está a disparar | Verifique: `sudo systemctl status proenergia-webhook`. Ver segredo: `sudo cat /var/www/proenergia/webhook_secret.txt`. Verifique os registos de entrega do webhook do GitHub. |
| Tabela de cache da base de dados em falta | Execute: `python manage.py createcachetable`. A tabela `summaries_cache_table` deve existir para a aplicação iniciar. |
