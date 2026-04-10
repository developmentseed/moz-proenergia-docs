---
sidebar_position: 5
title: "Campos de Configuração JSON"
---

# 5. Campos de Configuração JSON

Quatro arrays JSON em cada Modelo de Dados configuram o comportamento do frontend. O painel de administração valida a estrutura ao guardar e reporta erros para chaves obrigatórias em falta ou valores inválidos.

:::note
Todo o JSON deve utilizar aspas duplas para chaves e valores de string, sem vírgulas no final. Os arrays devem estar envolvidos em `[ ]`.
:::

---

## 5.1 `filter_fields`

Define os controlos de filtro apresentados no painel esquerdo. Cada entrada mapeia para um controlo de filtro interactivo.

### Esquema

| Chave | Tipo | Obrigatório? | Descrição |
|---|---|---|---|
| `label` | string | **obrigatório** | Rótulo legível por humanos apresentado acima do controlo de filtro. |
| `description` | string | **obrigatório** | Texto de dica. Pode ser uma string vazia. |
| `column` | string | **obrigatório** | Nome exacto da coluna no CSV do cenário. **Sensível a maiúsculas/minúsculas.** |
| `label_pt` | string | opcional | Tradução portuguesa do rótulo. |
| `description_pt` | string | opcional | Tradução portuguesa da descrição. |

### Como o tipo de filtro é determinado

O frontend deriva o tipo de controlo em tempo de execução a partir do nome da coluna e dos valores dos dados:

| Tipo Derivado | Condição | Controlo Renderizado |
|---|---|---|
| `admin` | O nome da coluna corresponde a uma palavra-chave de geografia administrativa (Admin_1–4, Province, Província, District, Distrito, Posto, Localidade, Region, Região, e variantes no plural/com acento) | Combobox de multi-selecção com pesquisa |
| `numeric` | Os dados da coluna contêm valores numéricos (não todos 0 ou 1) | Controlo de intervalo com dois campos de texto |
| `checkbox` | Todos os outros casos (strings, booleanos) | Grupo de caixas de verificação |

### Exemplo

```json
[
  {
    "label": "Province",
    "description": "Administrative province",
    "label_pt": "Provincia",
    "description_pt": "Provincia administrativa",
    "column": "Admin_1"
  },
  {
    "label": "Electrification Technology",
    "description": "Recommended technology for 2030",
    "column": "Technology2030"
  },
  {
    "label": "Population (2030)",
    "description": "Projected settlement population",
    "column": "Pop2030"
  }
]
```

:::tip
`Admin_1` → combobox administrativo. `Technology2030` → grupo de caixas de verificação (valores de string). `Pop2030` → controlo de intervalo numérico.
:::

---

## 5.2 `popup_fields`

Define quais os atributos apresentados quando um utilizador clica numa característica no mapa. Os campos aparecem na ordem listada.

### Esquema

| Chave | Tipo | Obrigatório? | Descrição |
|---|---|---|---|
| `label` | string | **obrigatório** | Rótulo de apresentação para o atributo. |
| `description` | string | **obrigatório** | Texto de dica. Pode ser uma string vazia. |
| `column` | string | **obrigatório** | Nome exacto da coluna CSV. **Sensível a maiúsculas/minúsculas.** |
| `label_pt` | string | opcional | Tradução portuguesa do rótulo. |
| `description_pt` | string | opcional | Tradução portuguesa da descrição. |

:::note
Quando um utilizador clica numa característica, o frontend chama `GET /api/v1/scenario/{id}/feature/{feature_id}/` e mostra apenas as colunas listadas aqui, por ordem.
:::

### Exemplo

```json
[
  {
    "label": "Settlement Name",
    "description": "Name of the settlement",
    "label_pt": "Nome do Assentamento",
    "description_pt": "Nome do assentamento",
    "column": "SettlementName"
  },
  { "label": "Population (2030)", "description": "Projected population", "column": "Pop2030" },
  { "label": "Recommended Technology", "description": "Least-cost technology", "column": "Technology2030" },
  { "label": "Total Investment", "description": "Total investment (USD)", "column": "InvestmentCostTotal" }
]
```

---

## 5.3 `summary_fields`

Define as estatísticas agregadas apresentadas no painel de Resumo do lado direito.

### Esquema

| Chave | Tipo | Obrigatório? | Descrição |
|---|---|---|---|
| `label` | string | **obrigatório** | Cabeçalho de apresentação para este item de resumo. |
| `description` | string | **obrigatório** | Descrição de dica. Pode ser uma string vazia. |
| `columns` | array de strings | **obrigatório** | Um ou mais nomes de colunas CSV. **Sempre um array.** Múltiplas colunas tornam-se sub-linhas. |
| `method` | string | opcional | `sum` \| `average` \| `count` \| `min` \| `max`. Por omissão: `sum`. |
| `unit` | string | opcional | Sufixo de unidade após o valor, por ex. `"USD"`, `"kW"`, `"km"`. |
| `group_by` | string ou array | opcional | Nome(s) de coluna(s) para agrupar resultados. String única ou array de até 2 strings para agrupamento aninhado. |
| `category` | string | opcional | Agrupa itens sob um cabeçalho recolhível no painel de resumo. |
| `chartType` | string | opcional | `bar` \| `donut` \| `stacked` \| `column` \| `area` \| `highlight`. O painel de administração valida todos os seis valores. |
| `colors` | objecto | opcional | Mapa de cores para gráficos. As chaves são valores de dados; os valores são strings hexadecimais. Ex. `{"SHS": "#F1C40F"}`. |
| `hasDecimal` | booleano | opcional | Se `true`, os valores são apresentados com casas decimais. Deve ser exactamente `true` ou `false`. |
| `showChartValueRows` | booleano | opcional | Se `true`, mostra uma tabela de valores brutos abaixo do gráfico. |
| `showBarChartAverage` | booleano | opcional | Se `true`, sobrepõe uma linha de média nos gráficos de barras. |
| `label_pt` | string | opcional | Tradução portuguesa do rótulo. |
| `description_pt` | string | opcional | Tradução portuguesa da descrição. |

:::note
Se `method` for omitido, o sistema usa `sum` por omissão. Para colunas do tipo string, o frontend usa sempre `count` independentemente da definição do método.
:::

### Exemplos

**Agregado numérico simples:**
```json
{
  "label": "Total Population (2030)",
  "description": "Sum of projected population across all settlements",
  "columns": ["Pop2030"],
  "method": "sum"
}
```

**Distribuição de tecnologia como gráfico de barras com cores:**
```json
{
  "label": "Technology Mix (2030)",
  "description": "Count per electrification technology",
  "columns": ["Technology2030"],
  "method": "count",
  "chartType": "bar",
  "colors": { "SHS": "#F1C40F", "MiniGrid": "#27AE60", "Grid": "#2980B9" },
  "showChartValueRows": true
}
```

**Campo numérico agrupado por tecnologia:**
```json
{
  "label": "Investment by Technology",
  "description": "Total investment grouped by technology type",
  "columns": ["InvestmentCostTotal"],
  "method": "sum",
  "unit": "USD",
  "group_by": "Technology2030",
  "chartType": "bar",
  "showBarChartAverage": true
}
```

**Agregado de múltiplas colunas:**
```json
{
  "label": "Capacity by Type",
  "description": "New capacity installed by technology category",
  "columns": ["NewCapacityGrid", "NewCapacityMiniGrid", "NewCapacitySHS"],
  "method": "sum",
  "unit": "kW"
}
```

---

## 5.4 `color_coding`

Mapeia valores de `visualization_column` para cores específicas no mapa. O valor especial `"default"` define a cor de recuo. O painel de administração valida que cada `color` é uma string hexadecimal válida (3 ou 6 dígitos hexadecimais, com ou sem `#` inicial).

### Esquema

| Chave | Tipo | Obrigatório? | Descrição |
|---|---|---|---|
| `value` | string | **obrigatório** | O valor da coluna a corresponder. Use `"default"` como recuo geral. |
| `color` | string | **obrigatório** | String de cor hexadecimal válida. Ex. `"#E74C3C"` ou `"E74C3C"`. Validada pelo painel de administração. |

### Exemplo

```json
[
  { "value": "SHS",      "color": "#F1C40F" },
  { "value": "MiniGrid", "color": "#27AE60" },
  { "value": "Grid",     "color": "#2980B9" },
  { "value": "default",  "color": "#95A5A6" }
]
```

:::warning
O painel de administração valida os códigos hexadecimais. Um valor inválido como `"red"` ou `"#GG0000"` produzirá um erro ao guardar.
:::
