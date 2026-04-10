---
sidebar_position: 103
title: "Apêndice D — Glossário"
---

# Apêndice D — Glossário

| Termo | Definição |
|---|---|
| **Modelo de Dados** | Uma categoria de análise temática (ex. Electrificação de Menor Custo). Contentor e configuração para Cenários, Conjuntos de Dados Vectoriais e definições de visualização. Pode ser público ou privado (`is_public`). |
| **Cenário** | Uma execução específica de modelo dentro de um Modelo de Dados (ex. Linha de Base 2025). Ligado a um Conjunto de Dados Vectorial e um ou mais Ficheiros de Cenário. Ordenado por `presentation_order`. |
| **Ficheiro de Cenário** | Um CSV carregado para um Cenário contendo atributos de saída modelados. Deve incluir uma coluna `id`. Suporta opção de renderização `low_zoom_as_points`. |
| **ScenarioData** | Tabela da base de dados (JSONB) que armazena todos os dados de atributos do Ficheiro de Cenário importados por característica. Alimenta o endpoint da API `/feature/`. |
| **ScenarioDataMetrics** | Tabela de chave-valor desnormalizada para consultas de agregação rápidas. Preenchida automaticamente na importação do Ficheiro de Cenário. Alimenta o endpoint da API `/summaries/`. |
| **Conjunto de Dados Vectorial** | Contentor nomeado para ficheiros de geometria espacial (`.geojson`, `.gpkg`, `.zip`, `.kml`). Inclui campos de metadados ricos. Suporta traduções EN/PT. |
| **Conjunto de Dados Raster** | Contentor para ficheiros de imagem Cloud-Optimized GeoTIFF (COG). Apresentado como camadas de sobreposição raster no mapa. |
| **Conjunto de Dados de Referência** | Contentor para documentos de suporte e tabelas (`.pdf`, `.csv`, `.xlsx`, `.docx`, etc.). Listado na secção de Transferências. |
| **PMTiles** | Arquivo de tiles vectoriais de ficheiro único servido via pedidos de intervalo HTTP. Gerado a partir de ficheiros vectoriais usando Tippecanoe. |
| **COG** | Cloud-Optimized GeoTIFF. Um formato raster optimizado para streaming a partir de armazenamento de objectos. Deve estar em EPSG:3857 com tamanho de bloco 256×256 para a renderização raster da plataforma. |
| **presentation_order** | Campo inteiro no ModeloDados e Cenário que controla a ordem de ordenação na barra lateral do frontend e no menu suspenso. Os números mais baixos aparecem primeiro. |
| **is_public (ModeloDados)** | Booleano no ModeloDados. Se `False`, o modelo fica oculto da API para não-superutilizadores e não aparece no frontend. |
| **metric_field_types** | Dicionário JSON no ModeloDados que mapeia nomes de colunas CSV para `"numeric"` ou `"string"`. Preenchido automaticamente na importação do Ficheiro de Cenário. Alimenta a API de resumos. |
| **visualization_column** | A coluna CSV cujos valores únicos determinam as cores das características do mapa, conforme configurado por `color_coding`. |
| **low_zoom_as_points** | Opção do FicheiroCenário que renderiza centróides de polígonos em zoom baixo (5–10) e geometria completa em zoom alto (11–14). Melhora o desempenho para grandes conjuntos de dados de polígonos. |
| **Celery** | Fila de tarefas distribuída para processamento assíncrono (geração de PMTiles, importação de CSV). |
| **RabbitMQ** | Intermediário de mensagens para Celery. Em produção, usa um vhost dedicado: `proenergia_vhost`. |
| **Tippecanoe** | Ferramenta de linha de comandos que gera PMTiles a partir de dados vectoriais FlatGeobuf. |
| **tile-join** | Ferramenta complementar do Tippecanoe que combina múltiplos ficheiros PMTiles (usada para `low_zoom_as_points`). |
| **GDAL / ogr2ogr** | Biblioteca de dados geoespaciais para conversão de formato e reprojecção. |
| **i18n** | Internacionalização. A plataforma suporta português (predefinição) e inglês via i18next. Os modelos de backend suportam campos de tradução `name_pt` e `description_pt`. |
| **proenergia_db** | O nome da base de dados PostgreSQL de produção. |
| **DATABASE_URL** | Variável de ambiente principal para a ligação à base de dados (`postgis://...`). |
