---
sidebar_position: 24
title: "Update Procedures"
---

# 24. Update Procedures

## 24.1 Manual Update

```bash
# Run as the proenergia user
sudo -u proenergia /var/www/proenergia/app/deploy/scripts/05_update_app.sh

# Or use the installed command (requires sudoers config from script 03)
sudo deploy-proenergia
```

The update script (`05_update_app.sh`) performs these steps in order:

1. `git pull origin main`
2. Activate virtualenv and `pip install -r requirements.txt --upgrade`
3. `python manage.py migrate`
4. `python manage.py createcachetable`
5. `python manage.py collectstatic --noinput`
6. `python manage.py compilemessages -f`

:::warning
Always run migrations **before** restarting the application after a code update that contains schema changes.
:::

## 24.2 Rollback

```bash
cd /var/www/proenergia/app
git log --oneline -5            # find previous commit
git checkout <previous-commit>
sudo systemctl restart proenergia
sudo systemctl restart proenergia-celery
```

## 24.3 Verification After Update

```bash
# Health check (with retry loop)
bash /var/www/proenergia/app/deploy/scripts/health-check.sh --wait

# Full verification suite
bash /var/www/proenergia/app/deploy/scripts/04_verify_setup.sh

# Manual API check
curl https://your-domain.com/api/v1/model/
```
