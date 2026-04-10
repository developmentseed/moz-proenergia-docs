---
sidebar_position: 104
title: "Apêndice E — Actualizar Strings de Idioma"
---

# Apêndice E — Actualizar Strings de Idioma do Frontend

O frontend do PROENERGIA+ suporta **português** (predefinição) e **inglês**. Este apêndice é uma referência completa para qualquer pessoa que precise de adicionar, editar ou traduzir texto visível ao utilizador na aplicação.

Existem três mecanismos de tradução distintos dependendo do tipo de conteúdo. Compreender qual se aplica à sua alteração é o primeiro passo.

| Tipo de conteúdo | Mecanismo | Onde vivem as traduções |
|---|---|---|
| Strings da interface (botões, rótulos, mensagens) | Ficheiros JSON de localidade i18next | `src/i18n/locales/{en,pt}.json` |
| Dados de backend (nomes de modelos/cenários/camadas) | Campos `_pt` nos registos de administração | Campos de formulário do Painel de Administração Django |
| Conteúdo de página extenso | Ficheiros MDX específicos de localidade | `src/app/<página>/<slug>.pt.mdx` |

---

## 1. Strings da Interface (Ficheiros de Localidade i18next)

Todo o texto de interface estático — rótulos de navegação, texto de botões, mensagens de erro, texto de marcador de posição e rótulos de campo — reside em dois ficheiros JSON:

- `src/i18n/locales/en.json` — Strings em inglês
- `src/i18n/locales/pt.json` — Strings em português

A aplicação usa por predefinição o português no primeiro carregamento. Se uma string em português estiver em falta para uma determinada chave, o i18next recorre silenciosamente ao valor em inglês.

### Estrutura de espaços de nomes

As strings são organizadas em espaços de nomes com base na área da interface a que pertencem. Ambos os ficheiros JSON devem usar estruturas de chave idênticas.

| Espaço de nomes | Abrange |
|---|---|
| `nav` | Ligações de navegação do cabeçalho, rótulos de início/fim de sessão, nome do site |
| `home` | Cabeçalho da página de destino, descrição, botões de chamada para acção |
| `auth.login` | Campos do formulário de início de sessão, mensagens de validação, feedback de sucesso |
| `auth.logout` | Botão de fim de sessão e confirmação |
| `explorer` | Painel de modelo, selector de cenários, separadores Controlos/Camadas, Aplicar/Repor filtro, estados de erro |
| `downloads` | Marcador de posição de pesquisa, rótulos de metadados de cartão, botão de transferência |
| `filters` | Marcador de posição do Combobox, apresentação de contagem seleccionada, estado vazio |
| `map` | Título da legenda, rótulo do painel de camadas adicionais |
| `models` | Strings da página de listagem de modelos |
| `breadcrumbs` | Rótulos de migalhas de pão ao nível da página |
| `labels` | Rótulos de campos de dados chaveados por nome de coluna CSV (ex. `labels.Admin_1.label`) |

### Como editar uma string existente

1. Abra `src/i18n/locales/en.json` e `src/i18n/locales/pt.json`.
2. Encontre a chave que pretende alterar. As chaves seguem o padrão `{espaço_nomes}.{contexto}.{elemento}`.
3. Actualize o valor em **ambos os ficheiros**.
4. Guarde e a alteração fica activa na próxima compilação (ou recarregada em modo de desenvolvimento).

**Exemplo:** Alterar o rótulo do botão de transferência.

```json
// en.json
{
  "downloads": {
    "download": "Download"
  }
}

// pt.json
{
  "downloads": {
    "download": "Baixar"
  }
}
```

### Como adicionar uma nova string

1. Escolha o espaço de nomes adequado, ou adicione uma nova chave de nível superior se a sua funcionalidade não se enquadrar num existente.
2. Adicione a chave e o seu valor a **ambos** `en.json` e `pt.json`.
3. Use a string no seu componente com `useTranslation()`. O componente deve ser um ficheiro `"use client"`.

```tsx
"use client";
import { useTranslation } from "react-i18next";

function MeuComponente() {
  const { t } = useTranslation();
  return <button>{t("explorer.novoBotao")}</button>;
}
```

:::warning Ambos os ficheiros devem permanecer sincronizados
As chaves em falta recorrem silenciosamente ao inglês — não há erro em tempo de execução. Adicione sempre a chave a ambos os ficheiros ao mesmo tempo. Se adicionar um espaço de nomes a um ficheiro, adicione-o ao outro também e actualize a tabela acima.
:::

### Valores dinâmicos (interpolação)

Use marcadores de posição `{{variável}}` — nunca concatenação de strings.

```json
// en.json
{ "filters": { "selected": "{{count}} selected" } }

// pt.json
{ "filters": { "selected": "{{count}} seleccionados" } }
```

```tsx
t("filters.selected", { count: 5 })   // → "5 selected" ou "5 seleccionados"
```

### O espaço de nomes `labels` — rótulos de campos de dados

O espaço de nomes `labels` mapeia nomes de colunas CSV para rótulos e descrições legíveis por humanos. É assim que nomes de colunas genéricos como `Admin_1` ou `ElecStart` são apresentados em filtros e popups.

```json
// en.json
{
  "labels": {
    "Admin_1": { "label": "Province", "description": "Administrative level 1" },
    "Technology2030": { "label": "Technology", "description": "Chosen least-cost technology" }
  }
}

// pt.json
{
  "labels": {
    "Admin_1": { "label": "Província", "description": "Nível administrativo 1" },
    "Technology2030": { "label": "Tecnologia", "description": "Tecnologia de menor custo" }
  }
}
```

Para adicionar um rótulo para uma nova coluna CSV, adicione a sua chave a ambos os ficheiros de localidade em `labels`. A chave deve corresponder exactamente ao nome da coluna como aparece nos dados CSV do cenário (sensível a maiúsculas/minúsculas).

---

## 2. Nomes e Descrições de Dados de Backend

Os nomes de modelos, nomes de cenários, nomes de camadas e as suas descrições provêm da API de backend Django. Estes são traduzidos usando campos `_pt` complementares em cada registo da base de dados — não nos ficheiros de localidade do frontend.

### Onde definir traduções

Todas as traduções para dados de backend são definidas na **interface do Painel de Administração Django**. Quando abre o formulário de edição de um Modelo de Dados, Conjunto de Dados Vectorial, Cenário ou registo similar, os campos de nome e descrição aparecem como entradas com separadores — um separador por idioma.

| Tipo de registo de administração | Campos traduzíveis |
|---|---|
| Modelo de Dados | Nome, Descrição |
| Cenário | Nome |
| Conjunto de Dados Vectorial | Nome, Descrição |
| Conjunto de Dados Raster | Nome, Descrição |
| Conjunto de Dados de Referência | Nome, Descrição |

### Como funciona no frontend

Quando o frontend obtém dados da API, cada registo inclui tanto `name` (inglês) como `name_pt` (português). A camada de transformação de dados regista-os no armazenamento em tempo de execução do i18next no momento do carregamento:

```ts
// Acontece automaticamente em src/utils/data-transformation.ts
registerI18nResource(`model.${m.id}`, {
  name: { en: m.name, pt: m.name_pt },
  description: { en: m.description, pt: m.description_pt },
});
```

Os componentes lêem com um valor de recuo para que tenham sempre algo para apresentar:

```tsx
t(`model.${model.id}.name`, { defaultValue: model.name })
```

### Tipos de entidade actualmente registados

| Entidade | Padrão de chave i18next | Campos da API usados |
|---|---|---|
| Modelo de Dados | `model.{id}.name`, `model.{id}.description` | `name_pt`, `description_pt` |
| Cenário | `scenario.{id}.name` | `name_pt` |
| Camada vectorial | `layer.{sourceId}.label`, `layer.{sourceId}.description` | `name_pt`, `description_pt` |

### Para actualizar um nome ou descrição traduzido

1. Inicie sessão no Painel de Administração Django em `/admin/`.
2. Navegue até ao registo relevante (ex. Conjuntos de Dados → Modelos de Dados → seleccione o modelo).
3. Clique no separador de idioma (EN / PT) acima do campo Nome ou Descrição.
4. Introduza ou actualize a tradução no separador português.
5. Clique em **Guardar**.

A alteração reflecte-se no frontend no próximo carregamento de página (ou após a expiração da cache da API).

:::note Não é necessária alteração de código
A actualização de traduções de dados de backend requer apenas uma edição no Painel de Administração Django — não é necessária nenhuma implantação de código.
:::

---

## 3. Conteúdo de Página Extenso (Ficheiros MDX)

As páginas com conteúdo escrito substancial — como a página Sobre — usam ficheiros MDX específicos de localidade em vez de chaves de tradução. Isto é adequado para conteúdo que é mais como um artigo do que um rótulo de interface.

### Convenção de nomenclatura de ficheiros

```
src/app/<página>/<slug>.mdx        ← Inglês (predefinição)
src/app/<página>/<slug>.pt.mdx     ← Português
```

### Páginas MDX actuais

| Rota | Ficheiro inglês | Ficheiro português |
|---|---|---|
| `/about` | `src/app/about/about.mdx` | `src/app/about/about.pt.mdx` |

### Como funciona a mudança de idioma da página

O componente de página importa ambos os ficheiros e serve o correcto com base no idioma activo do utilizador:

```tsx
"use client";
import { useTranslation } from "react-i18next";
import ContentEn from "./about.mdx";
import ContentPt from "./about.pt.mdx";

export default function Page() {
  const { i18n } = useTranslation();
  const Content = i18n.language?.startsWith("pt") ? ContentPt : ContentEn;
  return <Content />;
}
```

### Para actualizar conteúdo de página

1. Edite o ficheiro `.mdx` adequado directamente no repositório.
2. Se estiver a adicionar novo conteúdo em inglês, adicione o conteúdo em português correspondente ao ficheiro `.pt.mdx` ao mesmo tempo.
3. Confirme e envie — a alteração fica activa após a próxima implantação.

### Para adicionar uma nova página de conteúdo bilingue

1. Crie `src/app/<página>/<slug>.mdx` com o conteúdo em inglês.
2. Crie `src/app/<página>/<slug>.pt.mdx` com o conteúdo em português.
3. Crie `src/app/<página>/page.tsx` seguindo o padrão acima para alternar entre os dois ficheiros com base no idioma.
4. Adicione a rota à barra lateral do Docusaurus se for uma página de documentação, ou à navegação da aplicação se for uma página de frontend.

---

## 4. Selector de Idioma

Os utilizadores alternam entre português e inglês usando o botão de alternância **PT / EN** no canto superior direito do cabeçalho da aplicação. A preferência é armazenada em `localStorage` sob a chave `language` e persiste entre sessões do navegador.

O idioma predefinido na primeira visita (quando nenhuma preferência está armazenada) é o **português**:

```ts
// src/i18n/config.ts
if (typeof window !== 'undefined' && !localStorage.getItem('language')) {
  i18next.changeLanguage('pt');
}
```

Não há detecção de idioma do lado do servidor. O idioma é sempre resolvido do lado do cliente a partir do localStorage.

---

## 5. Lista de Verificação para Qualquer Alteração de i18n

Antes de submeter um pull request que toque qualquer texto visível ao utilizador, verifique:

- [ ] Ambos `en.json` e `pt.json` têm as mesmas chaves. As chaves em falta recorrem silenciosamente ao inglês.
- [ ] Nenhuma string visível ao utilizador está codificada directamente em JSX — use `t()`.
- [ ] Qualquer componente que use `t()` ou `useTranslation()` está marcado `"use client"`.
- [ ] As strings usam interpolação `{{variável}}`, nunca concatenação de strings.
- [ ] Se adicionou um novo espaço de nomes, a tabela na Secção 1 deste apêndice foi actualizada.
- [ ] Se actualizou a tradução de um registo de backend, a alteração foi guardada no Painel de Administração Django e verificada no frontend nas definições de idioma `/en` e `/pt`.
- [ ] Se adicionou ou actualizou uma página MDX, ambos os ficheiros `.mdx` e `.pt.mdx` foram actualizados.
