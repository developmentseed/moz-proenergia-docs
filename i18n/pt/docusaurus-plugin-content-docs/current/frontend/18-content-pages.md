---
sidebar_position: 18
title: "Páginas de Conteúdo e Documentação"
---

# 18. Páginas de Conteúdo e Documentação

## 18.1 Sistema de Conteúdo Baseado em MDX

A plataforma inclui páginas de documentação estáticas criadas em **MDX** (Markdown com componentes React integrados). Estas páginas suportam conteúdo bilingue através de ficheiros MDX específicos de localidade.

**Convenção de nomenclatura de ficheiros:**

```
src/app/<página>/<slug>.mdx       # Inglês (predefinição)
src/app/<página>/<slug>.pt.mdx    # Português
```

O ficheiro correcto é servido automaticamente com base no idioma seleccionado pelo utilizador.

**Páginas actualmente disponíveis:**

| Página | Inglês | Português |
|---|---|---|
| `/about` | `src/app/about/about.mdx` | `src/app/about/about.pt.mdx` |

Para adicionar ou actualizar páginas de conteúdo, um programador deve editar os ficheiros `.mdx` no repositório e reimplantar. Os administradores não programadores devem coordenar com os programadores para actualizações de conteúdo.
