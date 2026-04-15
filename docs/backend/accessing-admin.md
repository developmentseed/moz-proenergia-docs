---
title: "Accessing the Admin Interface"
---

# Accessing the Django Admin Interface

## URL and Login

The Django Admin is accessible at:

- **Production:** `https://<your-deployment-domain>/admin/`
- **Local development:** `http://localhost:8000/admin/`

Log in with a staff or superuser account. Navigate to the login page, enter your credentials, and click **Log In**.

:::note
On a fresh deployment, a superuser must be created via the command line before anyone can log in. See [Creating the Initial Superuser](#creating-the-initial-superuser-cli) below.
:::

## Admin Home Screen

After logging in, the admin home lists all registered model groups:

- **Authentication and Authorization** — User and Group management
- **Datasets** — DataModel, VectorDataset, VectorFile, RasterDataset, RasterFile, ReferenceDataset, ReferenceFile, Scenario, ScenarioFile

## Creating the Initial Superuser (CLI)

```bash
cd /var/www/proenergia/app
source venv/bin/activate
python manage.py createsuperuser
```

:::note
Superuser accounts should be restricted to a small number of trusted administrators. Use staff-level Admin accounts for day-to-day management.
:::
