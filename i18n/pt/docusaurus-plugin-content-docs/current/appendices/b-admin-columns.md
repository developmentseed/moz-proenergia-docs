---
sidebar_position: 101
title: "Apêndice B — Palavras-chave de Colunas Administrativas"
---

# Apêndice B — Palavras-chave de Colunas Administrativas

As colunas com estes **nomes exactos** (sensíveis a maiúsculas/minúsculas) são apresentadas como controlos Combobox de multi-selecção com pesquisa em vez de caixas de verificação ou controlos de intervalo:

```
Admin_1, Admin_2, Admin_3, Admin_4
Region, Regions, Região, Regiões
Province, Provinces, Província, Províncias
District, Districts, Distrito, Distritos
Posto, Postos
Localidade, Localidades
```

:::warning
Os nomes de colunas são correspondidos de forma exacta e sensível a maiúsculas/minúsculas. Uma coluna chamada `"province"` (minúsculas) **não** será tratada como um filtro administrativo — use `"Province"`.
:::
