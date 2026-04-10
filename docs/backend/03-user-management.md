---
sidebar_position: 3
title: "User Management"
---

# 3. User Management

## 3.1 User Roles and Permissions

| Permission | User | Admin | Super Admin |
|------------|:----:|:-----:|:-----------:|
| **VIEW ALL DATA** | | | |
| View & explore public Data Models (frontend) | ✓ | ✓ | ✓ |
| View private Data Models (frontend / API) | — | — | ✓ |
| Download public datasets | ✓ | ✓ | ✓ |
| Download private datasets | — | ✓ | ✓ |
| **DATA MANAGEMENT** | | | |
| Upload vector / raster / reference files | — | ✓ | ✓ |
| Edit dataset metadata and JSON configuration | — | ✓ | ✓ |
| Delete datasets | — | — | ✓ |
| Add / edit Data Models | — | ✓ | ✓ |
| Set Data Model `is_public` flag | — | — | ✓ |
| Add / edit Scenarios and Scenario Files | — | ✓ | ✓ |
| Publish / unpublish datasets (`is_approved`) | — | — | ✓ |
| **USER MANAGEMENT** | | | |
| Create / edit / delete user accounts | — | — | ✓ |

### How roles map to Django flags

| Django flags | Role |
|---|---|
| `is_staff = False`, `is_superuser = False` | Standard User — frontend only, no admin access. |
| `is_staff = True`, `is_superuser = False` | Admin — can access admin, manage their own datasets and scenarios. Cannot manage users or publish datasets. |
| `is_staff = True`, `is_superuser = True` | Super Admin — bypasses all permission checks. Full access to everything. |

## 3.2 Creating a New User

1. Go to **Authentication and Authorization → Users → + Add User**.
2. Enter a username and password, then click **Save and continue editing**.
3. Fill in personal information (first name, last name, email).
4. Set the appropriate permission level (see Section 3.3). Click **Save**.

## 3.3 Setting a User's Role

| Checkbox | Effect |
|---|---|
| **Active** (checked) | Account is active. Uncheck to disable without deleting. |
| **Staff status** (checked) | Grants access to the Django Admin. Required for Admin and Super Admin roles. |
| **Superuser status** (checked) | Full unrestricted access. Required for Super Admin role. |

- **Standard User:** Leave both unchecked.
- **Admin:** Check Staff status only. Optionally assign specific model-level permissions.
- **Super Admin:** Check both Staff status and Superuser status.

## 3.4 Assigning Specific Permissions to Admin Users

In the **User Permissions** multi-select, grant:

- `datasets | data model | Can add/change/view data model`
- `datasets | vector dataset | Can add/change/view vector dataset`
- `datasets | vector file | Can add/change/view vector file`
- `datasets | raster dataset | Can add/change/view raster dataset`
- `datasets | reference dataset | Can add/change/view reference dataset`
- `datasets | scenario | Can add/change/view scenario`
- `datasets | scenario file | Can add/change/view scenario file`

:::note
Super Admin accounts bypass all granular permission checks. Specific permissions only need to be set for staff-level Admin accounts.
:::

## 3.5 Editing and Deactivating Users

Go to **Authentication and Authorization → Users** and click a username to edit. To deactivate without deleting, uncheck the **Active** checkbox and click **Save**.
