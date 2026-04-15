---
title: "Configuração do Frontend"
---

# Configuração do Frontend

Nem todo o comportamento da plataforma é controlado da mesma forma. Esta página traça uma linha clara entre as definições que são **geridas através do Painel de Administração Django** (e entram em vigor imediatamente sem qualquer alteração de código) e as definições que são **codificadas na base de código do frontend** (e requerem uma alteração de código e reimplantação para actualizar).

Compreender esta distinção é importante quando se integram novos modelos, se actualiza a identidade visual ou se diagnostica por que uma alteração efectuada no painel de administração não está a aparecer como esperado.

---

## O Que o Painel de Administração Controla (sem necessidade de implantação)

Os seguintes são inteiramente controlados pelo Painel de Administração Django e servidos ao frontend via API. Alterá-los no painel de administração entra em vigor no próximo carregamento de página.

| Definição | Onde alterar | Campo da API |
|---|---|---|
| Rótulos, descrições e mapeamentos de colunas de filtro | Modelo de Dados → Campos de Filtro (JSON) | `filter_fields` |
| Lista de atributos do popup do mapa | Modelo de Dados → Campos Popup (JSON) | `popup_fields` |
| Estatísticas e gráficos do painel de resumo | Modelo de Dados → Campos de Resumo (JSON) | `summary_fields` |
| Codificação de cores das características do mapa | Modelo de Dados → Codificação de Cores (JSON) | `color_coding` |
| Coluna de visualização (que coluna define as cores) | Modelo de Dados → Coluna de Visualização | `visualization_column` |
| Nomes e descrições de modelos (EN + PT) | Modelo de Dados → campos Nome / Descrição | `name`, `name_pt`, `description_pt` |
| Nomes de cenários (EN + PT) | Cenário → campos Nome | `name`, `name_pt` |
| Nomes e descrições de conjuntos de dados (EN + PT) | Painel de administração de Conjuntos de Dados Vectoriais/Raster/Referência | `name`, `name_pt`, `description_pt` |
| Quais os conjuntos de dados vectoriais/raster/referência que aparecem por modelo | Modelo de Dados → Camadas Contextuais / Camadas Raster / Conjuntos de Dados de Referência | campos M2M |
| Se um modelo é publicamente visível | Modelo de Dados → É Público | `is_public` |

Consulte [Campos de Configuração JSON](/backend/json-configuration) para a referência completa de esquema para configuração de filtro, popup, resumo e codificação de cores.

---

## O Que o Código do Frontend Controla (implantação necessária)

Os seguintes são definidos em ficheiros sob `src/config/` no repositório do frontend. Alterá-los requer editar o ficheiro, confirmar e implantar.

### `map.json` — Níveis de Zoom do Mapa e Nome da Camada de Tile

**Ficheiro:** `src/config/map.json`  
**Estado:** Activo — importado em `map/index.tsx`, `map/main-layer.tsx` e `utils/data-transformation.ts`

```json
{
  "minZoom": 5,
  "polygonMinZoom": 7,
  "maxZoom": 11,
  "sourceLayerName": "data"
}
```

| Chave | Efeito | Quando alterar |
|---|---|---|
| `minZoom` | O nível de zoom mínimo que o mapa permite e o zoom mínimo integrado nas definições de fonte PMTiles | Se as definições de geração de tiles mudarem |
| `polygonMinZoom` | O nível de zoom a partir do qual as camadas de preenchimento de polígono, linha e círculo ficam visíveis | Se quiser que as características apareçam mais cedo ou mais tarde no zoom |
| `maxZoom` | Actualmente comentado nas definições de fonte de tiles — não aplicado activamente | N/A por agora |
| `sourceLayerName` | O nome interno da camada PMTiles de que todas as camadas do mapa lêem | Deve corresponder ao argumento `-l` passado ao Tippecanoe durante a geração de tiles. Actualmente `"data"`. Altere apenas se regenerar todos os tiles com um nome de camada diferente |

:::warning
`sourceLayerName` deve corresponder exactamente ao que o Tippecanoe escreve nos ficheiros PMTiles. Se diferirem, não aparecerão características no mapa. O valor actual `"data"` corresponde ao flag `-l data` na função `call_tippecanoe` em `tasks.py`.
:::

### `model.json` — Atribuição de Ícone por Modelo

**Ficheiro:** `src/config/model.json`  
**Estado:** Activo — lido por `utils/model-icon.ts` → `getIconPath()`, que é chamado por `side-nav.tsx` e `model-switcher-menu.tsx`

```json
[
  { "model": 1, "icon": "lightbulb.svg" },
  { "model": 2, "icon": "tractor.svg" },
  { "model": 3, "icon": "grid-3x3.svg" },
  { "model": 4, "icon": "landmark.svg" },
  { "model": 5, "icon": "cooking-pot.svg" }
]
```

Cada entrada mapeia o ID numérico da base de dados de um Modelo de Dados para um nome de ficheiro de ícone SVG. Os ícones encontram-se em `public/model-icon/`. Se nenhuma entrada corresponder ao ID de um modelo, é usado `default.svg`.

**Quando alterar:** Quando um novo Modelo de Dados é criado no painel de administração e quer que tenha um ícone específico na barra lateral. Adicione uma nova entrada com o ID do modelo (visível no URL do Painel de Administração Django ao visualizar o modelo: `/admin/datasets/datamodel/<id>/change/`) e o nome de ficheiro de um SVG em `public/model-icon/`.

Ícones disponíveis: `lightbulb.svg`, `tractor.svg`, `grid-3x3.svg`, `landmark.svg`, `cooking-pot.svg`, `default.svg`. Para adicionar um novo ícone, coloque o ficheiro SVG em `public/model-icon/` e referencie-o aqui.

### `website.ts` — Título do Site, Descrição e URL do Portal SDI

**Ficheiro:** `src/config/website.ts`  
**Estado:** Activo — `WEBSITE_TITLE` e `WEBSITE_DESC` usados em `app/layout.tsx` para o `<title>` HTML e meta descrição; `SDI_PORTAL_URL` usado no menu suspenso do cabeçalho

```ts
export const WEBSITE_TITLE = "Plataforma Integrada de Electrificação de Moçambique - PIE";
export const WEBSITE_DESC = "Proenergia";
export const SDI_PORTAL_URL = "https://proenergia-staging.ds.io/admin/";
```

| Exportação | Efeito | Quando alterar |
|---|---|---|
| `WEBSITE_TITLE` | O título do separador do navegador e o título OpenGraph do site | Em rebrand ou ao passar de staging para produção |
| `WEBSITE_DESC` | A meta descrição HTML (usada por motores de pesquisa e pré-visualizações de ligações) | Em rebrand ou actualização de conteúdo |
| `SDI_PORTAL_URL` | O URL para o qual a ligação "Portal SDI" no menu suspenso do cabeçalho navega | **Deve ser actualizado do URL de staging para o URL de administração de produção antes do lançamento** |

:::warning Actualizar SDI_PORTAL_URL antes do lançamento em produção
O valor actual aponta para o Painel de Administração Django de staging (`proenergia-staging.ds.io/admin/`). Deve ser alterado para o URL de administração de produção antes de a plataforma entrar em funcionamento.
:::

### `filters.ts` — Ordem de Ordenação de Filtros Baseada em Grau

**Ficheiro:** `src/config/filters.ts`  
**Estado:** Activo — `sortFilterOptions()` é importado e chamado em `utils/data-transformation.ts` ao construir listas de opções de filtro de caixas de verificação

Este ficheiro define uma ordem de prioridade para valores de grau qualitativos para que apareçam numa sequência lógica (Muito Alto → Alto → Médio → Baixo → Muito Baixo) em vez de alfabeticamente nos menus suspensos de filtro.

```ts
const DEGREE_ORDER = {
  'very high': 0,
  'high': 1,
  'medium': 2,
  'low': 3,
  'very low': 4,
};
```

Os valores que correspondem a estas chaves (sem distinção de maiúsculas/minúsculas) são ordenados para o topo das listas de filtros de caixas de verificação, na ordem definida. Todos os outros valores aparecem depois, na sua ordem de resposta da API original.

**Quando alterar:** Raramente. Apenas se um novo conjunto de dados introduzir valores de escala de grau diferentes que devam ser ordenados numa ordem específica, ou se a ordem existente precisar de ajuste.

### `api.ts` — Endpoints de URL da API e de Média

**Ficheiro:** `src/utils/api.ts` (não em `/config` mas funcionalmente equivalente)  
**Estado:** Activo — usado em toda a aplicação para todas as chamadas à API e construção de URL de ficheiros de média

```ts
export const API_ENDPOINT = 'https://proenergia-staging.ds.io/api/v1/';
export const MEDIA_URL_PREFIX = 'https://proenergia-staging.ds.io/media/';
```

| Exportação | Efeito |
|---|---|
| `API_ENDPOINT` | URL base para todos os pedidos da API REST (modelos, cenários, conjuntos de dados, resumos) |
| `MEDIA_URL_PREFIX` | Prefixado aos caminhos de ficheiros brutos retornados pela API para construir URLs completos de PMTiles e média |

:::warning Também requer actualização antes do lançamento em produção
Ambos os valores apontam actualmente para o servidor de staging. Devem ser actualizados para URLs de produção antes da implantação.
:::

---

- **Rótulos de campos de filtro, popup e resumo** → definidos na configuração JSON `filter_fields`, `popup_fields` e `summary_fields` do Modelo de Dados no painel de administração
- **Rótulos de colunas partilhadas** → definidos em `src/i18n/locales/en.json` e `src/i18n/locales/pt.json` sob o espaço de nomes `labels`

Consulte [Apêndice E — Actualizar Strings de Idioma](../appendices/e-language-strings) para saber como actualizar os ficheiros de localidade.

---

## Resumo

| Ficheiro | Estado | A alteração requer implantação? |
|---|:---:|:---:|
| `map.json` | Activo | Sim |
| `model.json` | Activo | Sim |
| `website.ts` | Activo | Sim |
| `filters.ts` | Activo | Sim |
| `api.ts` (em `/utils`) | Activo | Sim |
| Painel de Administração Django → Campos JSON do Modelo de Dados | Activo | **Não** |
| Painel de Administração Django → Nomes de Conjuntos de Dados/Cenários | Activo | **Não** |
