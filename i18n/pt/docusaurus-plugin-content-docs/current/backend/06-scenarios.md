---
sidebar_position: 6
title: "Cenários e Ficheiros de Cenário"
---

# 6. Cenários e Ficheiros de Cenário

## 6.1 O Que É um Cenário?

Um Cenário representa uma execução específica de modelo dentro de um Modelo de Dados — por exemplo, *Linha de Base 2025* ou *Expansão Acelerada da Rede 2035*. Cada Cenário está ligado a um Conjunto de Dados Vectorial para geometria espacial e contém resultados de análise através de um ou mais Ficheiros de Cenário (CSV).

## 6.2 Adicionar um Novo Cenário

1. Vá a **Conjuntos de Dados → Cenários → + Adicionar Cenário**.
2. Preencha os campos (consulte a Secção 6.3).
3. Clique em **Guardar**. Em seguida, pode adicionar Ficheiros de Cenário.

## 6.3 Referência dos Campos do Cenário

| Campo | Descrição |
|---|---|
| **Nome / Nome (PT)** | Nome único (máx. 155 caracteres). Apresentado no menu suspenso de cenários do frontend. Suporta traduções EN/PT. |
| **Modelo** | O Modelo de Dados ao qual este cenário pertence (chave estrangeira). |
| **Conjunto de Dados Vectorial** | O Conjunto de Dados Vectorial que fornece geometria espacial para a camada de mapa deste cenário. Deve ter pelo menos um ficheiro em estado Pronto. |
| **Ordem de Apresentação** | Número inteiro que controla a ordem de ordenação no menu suspenso do frontend. Os números mais baixos aparecem primeiro. |

:::note
Um único Conjunto de Dados Vectorial pode ser partilhado entre múltiplos Cenários. Os Cenários são ordenados no menu suspenso pela Ordem de Apresentação e, em seguida, pelo ID.
:::

## 6.4 Adicionar Ficheiros de Cenário

Um Ficheiro de Cenário é um CSV contendo dados de resultados de análise. Cada linha corresponde a uma característica espacial identificada por uma coluna numérica `id`. O carregamento desencadeia uma tarefa Celery que combina o CSV com a geometria vectorial para gerar uma camada de mapa PMTiles, depois importa o CSV para a base de dados para consultas de resumo.

1. Vá a **Conjuntos de Dados → Ficheiros de Cenário → + Adicionar Ficheiro de Cenário**.
2. Seleccione o Cenário pai.
3. Carregue um ficheiro CSV. O CSV **deve incluir uma coluna `id`** correspondente aos IDs de características no Conjunto de Dados Vectorial ligado.
4. Opcionalmente, marque **Representar características como pontos em níveis de zoom inferiores** (consulte a Secção 6.5).
5. Clique em **Guardar**.

:::note Formato CSV
O delimitador é detectado automaticamente (vírgula ou ponto e vírgula). As strings numéricas são automaticamente convertidas para números; todos os outros valores são armazenados como strings. A coluna `id` é usada como chave de junção e não é armazenada como metadados. Os ficheiros com BOM UTF-8 são tratados correctamente.
:::

## 6.5 Opção de Zoom Baixo como Pontos

A caixa de verificação **Representar características como pontos em níveis de zoom inferiores** (`low_zoom_as_points`) optimiza a renderização para grandes conjuntos de dados de polígonos.

Quando activada, o pipeline gera:
- Pontos de centróide para os níveis de zoom 5–10
- Geometria de polígono completa para os níveis de zoom 11–14
- Estes são combinados num único ficheiro PMTiles usando a ferramenta `tile-join` do Tippecanoe.

:::tip
Recomendado para grandes conjuntos de dados (10.000+ características) compostos por polígonos quadrados uniformes. Não é necessário para dados de pontos ou linhas.
:::

## 6.6 Indicador de Estado do Ficheiro de Cenário

A lista de Ficheiros de Cenário inclui uma coluna **Está Activo** que indica se um ficheiro é o ficheiro activo actualmente (o mais recente em estado Pronto) para o seu cenário. Apenas o ficheiro Pronto processado mais recentemente está activo.

## 6.7 Monitorizar o Processamento de Ficheiros de Cenário

O estado progride: `Criado → Em Processamento → Pronto` (ou `Erro`).

Se um ficheiro entrar em estado de Erro, abra o registo e leia o campo **Mensagem de Erro**. Use a acção **Reprocessar ficheiros** para re-enfileirar ficheiros em estado Pronto ou Erro.

:::note Cache
As respostas de resumo são armazenadas em cache por 24 horas. Após carregar novos dados, use `DELETE /api/v1/scenario/{id}/summaries/cache/` para limpar resultados em cache obsoletos.
:::
