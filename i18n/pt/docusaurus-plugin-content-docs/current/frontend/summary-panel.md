---
title: "O Painel de Resumo de Análise"
---

# O Painel de Resumo de Análise

## Visão Geral

O Painel de Resumo de Análise apresenta estatísticas agregadas que se actualizam em tempo real quando os filtros são aplicados. Todas as estatísticas correspondem a entradas na configuração `summary_fields` do Modelo de Dados.

## Formatos de Apresentação de Estatísticas

| Tipo de apresentação | Quando mostrado |
|---|---|
| **Valor único (simples)** | Coluna única, sem `group_by`, sem `chartType`. Mostra o valor calculado com unidade opcional. |
| **Distribuição por grupo** | `group_by` definido mas sem `chartType`. Mostra o valor por grupo como uma lista com rótulo. |
| **Gráfico** (barra/donut/empilhado/coluna/área) | `chartType` definido. Mostra um gráfico interactivo. `showChartValueRows: true` adiciona uma tabela abaixo. |
| **Destaque** | `chartType: "highlight"`. Mostra um cartão de destaque de valor único proeminente. |
| **Grupo de múltiplas colunas** | `columns` tem múltiplas entradas. Cada coluna é uma sub-linha agregada por `method`. |
| **Grupo aninhado** | `group_by` definido para duas colunas. Mostra uma distribuição agrupada de dois níveis. |

## Categorias de Resumo

Os itens que partilham o mesmo valor de `category` são agrupados sob um cabeçalho recolhível no painel de resumo.
