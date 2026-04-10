---
sidebar_position: 24
title: "Procedimentos de Actualização"
---

# 24. Procedimentos de Actualização

## 24.1 Actualização Manual

```bash
# Executar como utilizador proenergia
sudo -u proenergia /var/www/proenergia/app/deploy/scripts/05_update_app.sh

# Ou usar o comando instalado (requer configuração sudoers do script 03)
sudo deploy-proenergia
```

O script de actualização (`05_update_app.sh`) executa estes passos por ordem:

1. `git pull origin main`
2. Activar virtualenv e `pip install -r requirements.txt --upgrade`
3. `python manage.py migrate`
4. `python manage.py createcachetable`
5. `python manage.py collectstatic --noinput`
6. `python manage.py compilemessages -f`

:::warning
Execute sempre as migrações **antes** de reiniciar a aplicação após uma actualização de código que contém alterações de esquema.
:::

## 24.2 Reversão

```bash
cd /var/www/proenergia/app
git log --oneline -5            # encontrar commit anterior
git checkout <commit-anterior>
sudo systemctl restart proenergia
sudo systemctl restart proenergia-celery
```

## 24.3 Verificação Após Actualização

```bash
# Verificação de estado (com ciclo de repetição)
bash /var/www/proenergia/app/deploy/scripts/health-check.sh --wait

# Suite de verificação completa
bash /var/www/proenergia/app/deploy/scripts/04_verify_setup.sh

# Verificação manual da API
curl https://o-seu-dominio.com/api/v1/model/
```
