---
title: "Modelos de Dados"
---

# Modelos de Dados

## O Que É um Modelo de Dados?

Um Modelo de Dados representa uma categoria de planeamento ou análise — como Electrificação de Menor Custo, Cadeia de Frio Agrícola ou Cozinha Limpa. Cada Modelo de Dados agrupa Cenários, Conjuntos de Dados Vectoriais e configuração de visualização (filtros, popups, resumos, codificação de cores). Também pode referenciar camadas Raster (imagens COG) e conjuntos de dados de Referência (documentos).

## Adicionar um Novo Modelo de Dados

1. Vá a **Conjuntos de Dados → Modelos de Dados → + Adicionar Modelo de Dados**.
2. Preencha os campos de nível superior (consulte a tabela de campos abaixo).
3. Adicione a configuração JSON para `filter_fields`, `popup_fields`, `summary_fields` e `color_coding` (consulte [Campos de Configuração JSON](./json-configuration)).
4. Clique em **Gravar**, ou **Guardar e continuar a editar**.

## Referência dos Campos do Modelo de Dados

| Campo | Descrição |
|---|---|
| **Nome / Nome (PT)** | Nome único (máx. 155 caracteres). Suporta inglês e português através do formulário com separadores. Apresentado na barra lateral de navegação do frontend. |
| **Descrição / Descrição (PT)** | Descrição opcional. Suporta traduções. |
| **Ordem de Apresentação** | Número inteiro que controla a ordem de ordenação na barra lateral do frontend. Os números mais baixos aparecem primeiro. Predefinição: 0. |
| **É Público** | Booleano (predefinição: Verdadeiro). Se Falso, o modelo fica oculto da API para não-superutilizadores e não aparece no frontend. |
| **Coluna de Visualização** | Opcional. O nome exacto da coluna CSV cujos valores únicos codificam por cores as características do mapa. Deixe em branco para uma única cor predefinida. |
| **Codificação de Cores (JSON)** | Mapeia cada valor da coluna de visualização para uma cor hexadecimal. Consulte [color_coding](./json-configuration#color_coding). |
| **Campos de Filtro (JSON)** | Controla os filtros no painel esquerdo. Consulte [filter_fields](./json-configuration#filter_fields). |
| **Campos Popup (JSON)** | Define os atributos mostrados quando um utilizador clica numa característica do mapa. Consulte [popup_fields](./json-configuration#popup_fields). |
| **Campos de Resumo (JSON)** | Especifica as estatísticas agregadas no resumo do painel direito. Consulte [summary_fields](./json-configuration#summary_fields). |
| **Camadas Contextuais** | Multi-selecção de ConjuntosDadosVectoriais aprovados para activar/desactivar juntamente com os dados principais. |
| **Camadas Raster** | Multi-selecção de ConjuntosDadosRaster aprovados (imagens COG). |
| **Conjuntos de Dados de Referência** | Multi-selecção de ConjuntosDadosReferência aprovados (documentos, tabelas). |

:::warning
As alterações nos campos de configuração JSON afectam todos os utilizadores imediatamente. Teste cuidadosamente antes de guardar em produção.
:::

:::tip Editor JSON
Os campos JSON utilizam um editor interactivo de árvore/formulário/vista/código. Alterne entre modos utilizando os separadores acima de cada campo. O modo **Código** aceita texto JSON bruto.
:::
