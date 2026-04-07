---
sidebar_position: 101
title: "Appendix B — Admin Column Keywords"
---

# Appendix B — Administrative Column Keywords

Columns with these **exact names** (case-sensitive) are rendered as searchable multi-select Combobox controls rather than checkboxes or range controls:

```
Admin_1, Admin_2, Admin_3, Admin_4
Region, Regions, Região, Regiões
Province, Provinces, Província, Províncias
District, Districts, Distrito, Distritos
Posto, Postos
Localidade, Localidades
```

:::warning
Column names are matched exactly and case-sensitively. A column named `"province"` (lowercase) will **not** be treated as an admin filter — use `"Province"`.
:::
