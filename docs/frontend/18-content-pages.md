---
sidebar_position: 18
title: "18. Content & Documentation Pages"
---

# 18. Content and Documentation Pages

## 18.1 MDX-Based Content System

The platform includes static documentation pages authored in **MDX** (Markdown with embedded React components). These pages support bilingual content via locale-specific MDX files.

**File naming convention:**

```
src/app/<page>/<slug>.mdx       # English (default)
src/app/<page>/<slug>.pt.mdx    # Portuguese
```

The correct file is served automatically based on the user's selected language.

**Currently available pages:**

| Page | English | Portuguese |
|---|---|---|
| `/about` | `src/app/about/about.mdx` | `src/app/about/about.pt.mdx` |

To add or update content pages, a developer must edit the `.mdx` files in the repository and redeploy. Non-developer administrators should coordinate with Development Seed for content updates.
