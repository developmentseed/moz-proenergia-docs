---
sidebar_position: 7
title: "Conjuntos de Dados Vectoriais e Ficheiros Vectoriais"
---

# 7. Conjuntos de Dados Vectoriais e Ficheiros Vectoriais

## 7.1 O Que É um Conjunto de Dados Vectorial?

Um Conjunto de Dados Vectorial é um contentor nomeado para geometria espacial — a colecção de pontos, linhas ou polígonos renderizados no mapa. Os Cenários referenciam um Conjunto de Dados Vectorial para obter a sua geometria espacial.

## 7.2 Adicionar um Novo Conjunto de Dados Vectorial

1. Vá a **Conjuntos de Dados → Conjuntos de Dados Vectoriais → + Adicionar Conjunto de Dados Vectorial**.
2. Preencha os campos de metadados (consulte a Secção 7.3).
3. Clique em **Guardar**. Em seguida, pode carregar Ficheiros Vectoriais.

## 7.3 Referência dos Campos do Conjunto de Dados Vectorial

| Campo | Descrição |
|---|---|
| **Nome / Nome (PT)** | Nome único (máx. 155 caracteres). Suporta traduções EN/PT. |
| **Descrição / Descrição (PT)** | Resumo opcional. Suporta traduções. |
| **Proprietário dos Dados** (`source`) | Atribuição opcional (máx. 155 caracteres). |
| **Ponto de Contacto** (`contact`) | Pessoa ou equipa de contacto opcional. |
| **Data de Publicação** (`published`) | Data opcional em que o conjunto de dados foi publicado na fonte. |
| **Extensão Temporal** | Período de tempo opcional coberto pelos dados (ex. `"2020–2024"`). |
| **SRC** | Opcional. Documente o SRC fonte (ex. `"EPSG:4326"`). Todos os ficheiros são reprojectados para EPSG:4326 durante o processamento. |
| **Frequência de Manutenção** | Opcional. Com que frequência o conjunto de dados é actualizado na fonte. |
| **Linhagem** | Opcional. Proveniência dos dados ou notas de processamento. |
| **Licença Legal** | Opcional. Licença sob a qual os dados são fornecidos. |
| **Definições de Atributos** | Opcional. Ligação ou nota descrevendo o esquema de atributos. |
| **É Público** | Apenas superutilizador. Se marcado, o conjunto de dados é visível para utilizadores não autenticados. |
| **Está Aprovado** | Apenas superutilizador. Deve ser aprovado antes de o conjunto de dados poder ser usado em Cenários ou apresentado no frontend. |

## 7.4 Adicionar Ficheiros Vectoriais

O carregamento desencadeia uma tarefa Celery: ficheiro → FlatGeobuf (GDAL) → PMTiles (Tippecanoe).

1. Vá a **Conjuntos de Dados → Ficheiros Vectoriais → + Adicionar Ficheiro Vectorial**.
2. Seleccione o Conjunto de Dados Vectorial pai.
3. Carregue um ficheiro. Formatos aceites:

| Formato | Notas |
|---|---|
| `.geojson` | GeoJSON. Deve usar WGS84 (EPSG:4326). Formato preferido. |
| `.gpkg` | GeoPackage. Totalmente suportado. |
| `.zip` | Arquivo ZIP contendo um Shapefile (`.shp`, `.shx`, `.dbf`, `.prj`). |
| `.kml` | Keyhole Markup Language. Totalmente suportado. |

4. Clique em **Guardar**. O processamento começa automaticamente.

## 7.5 Monitorizar o Processamento de Ficheiros

Estado: `Criado → Em Processamento → Pronto` (ou `Erro`). Se um ficheiro entrar em estado de Erro, abra o registo e leia a **Mensagem de Erro**. Use **Reprocessar ficheiros** para re-enfileirar.

## 7.6 Publicar um Conjunto de Dados

Apenas os superutilizadores podem publicar conjuntos de dados. Seleccione conjuntos de dados na vista de lista e use o menu suspenso **Acções**:

| Acção | Efeito |
|---|---|
| Tornar conjunto de dados público | Define `is_public = True` |
| Tornar conjunto de dados privado | Define `is_public = False` |
| Publicar conjunto de dados | Define `is_approved = True` |
| Despublicar conjunto de dados | Define `is_approved = False` |

:::note Regra de visibilidade
Um conjunto de dados é visível para utilizadores não autenticados apenas quando `is_public = True` E `is_approved = True`. Os utilizadores autenticados podem ver qualquer conjunto de dados onde `is_approved = True`, independentemente de `is_public`.
:::
