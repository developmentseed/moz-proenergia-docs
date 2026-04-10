---
sidebar_position: 14
title: "O Painel de Filtros"
---

# 14. O Painel de Filtros

## 14.1 Visão Geral

O Painel de Filtros contém todos os controlos de filtro definidos na configuração `filter_fields` do Modelo de Dados. Os filtros reduzem simultaneamente as características apresentadas no mapa e actualizam as estatísticas do Resumo de Análise.

## 14.2 Filtros de Área Administrativa

Os filtros geográficos são apresentados como controlos **Combobox** de multi-selecção com pesquisa para colunas que correspondem a palavras-chave de geografia administrativa. A hierarquia administrativa de Moçambique:

- **Província** (Província / Região)
  - **Distrito** (Distrito)
    - **Posto Administrativo** (Posto Administrativo)
      - **Localidade** (Localidade)

## 14.3 Filtros de Tecnologia / Categoria

Os filtros de **Caixa de verificação** são mostrados para colunas com valores de string. Por omissão, todos os valores estão seleccionados (visíveis). Desmarque qualquer valor para ocultar características com esse valor. Os valores são codificados por cores de forma consistente com a legenda do mapa.

## 14.4 Filtros de Intervalo Numérico

Os controlos de **intervalo com dois campos de texto** são mostrados para colunas numéricas. Introduza um mínimo e/ou máximo para restringir as características apresentadas.

Usos comuns: População do Assentamento, Custo de Investimento, Distância à Rede.

:::tip
Combine filtros de intervalo com caixas de verificação de tecnologia — por ex. todos os locais de mini-rede com população acima de 1.000 e custo de investimento abaixo de 500.000 USD.
:::

## 14.5 Aplicar e Limpar Filtros

As alterações de filtro são **encenadas**. Um indicador visual em cada filtro mostra o estado pendente ou activo (alterado em relação à predefinição).

- Clique em **Aplicar** para confirmar todas as alterações pendentes.
- Clique em **Repor** para limpar todos os filtros para os seus valores predefinidos.

O estado do filtro aplicado é codificado no URL para marcação e partilha.
