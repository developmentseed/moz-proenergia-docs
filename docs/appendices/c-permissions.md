---
sidebar_position: 102
title: "Appendix C — Permissions Matrix"
---

# Appendix C — Permissions Matrix Summary

| Action | User | Admin | Super Admin |
|--------|:----:|:-----:|:-----------:|
| **VIEW & DOWNLOAD** | | | |
| View & explore public Data Models (frontend) | ✓ | ✓ | ✓ |
| View private Data Models (frontend / API) | — | — | ✓ |
| Download public datasets | ✓ | ✓ | ✓ |
| Download private datasets | — | ✓ | ✓ |
| **BACKEND ADMINISTRATION** | | | |
| Access Django Admin interface | — | ✓ | ✓ |
| Upload vector / raster / reference files | — | ✓ | ✓ |
| Edit Data Model JSON configuration | — | ✓ | ✓ |
| Set Data Model `is_public` flag | — | — | ✓ |
| Add / edit Scenarios and Scenario Files | — | ✓ | ✓ |
| Publish / unpublish datasets (`is_approved`) | — | — | ✓ |
| Set `is_public` flag on datasets | — | — | ✓ |
| Delete any data record | — | — | ✓ |
| Create and manage user accounts | — | — | ✓ |
