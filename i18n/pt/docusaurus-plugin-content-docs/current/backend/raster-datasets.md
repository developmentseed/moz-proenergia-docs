---
title: "Conjuntos de Dados Raster e Ficheiros Raster"
---

# Conjuntos de Dados Raster e Ficheiros Raster

Os Conjuntos de Dados Raster armazenam imagens georeferenciadas (fotografias de satélite, modelos de terreno, resultados raster derivados). A aplicação suporta a visualização de camadas Cloud-Optimized GeoTIFF (COG). Ao contrário dos dados vectoriais, os ficheiros raster não requerem conversão PMTiles — são servidos directamente a partir do armazenamento de ficheiros.

## Adicionar um Conjunto de Dados Raster

1. Vá a **Datasets → Datasets Raster → + Adicionar Dataset Raster**.
2. Preencha os mesmos campos de metadados que os Conjuntos de Dados Vectoriais (nome, descrição, fonte, contacto, SRC, etc.). Suporta traduções EN/PT.
3. Clique em **Gravar**. Em seguida, adicione um Ficheiro Raster.

## Adicionar Ficheiros Raster

  1. Vá a **Datasets → Arquivos Raster → + Adicionar Ficheiro Raster**.
2. Seleccione o Dataset Raster.
3. Carregue um ficheiro raster. Formatos aceitos: `.tiff`, `.tif`, `.geotiff`, `.gtiff`, `.vrt`.
4. Clique em **Gravar**.

:::warning Requisitos COG
Para melhor desempenho, os ficheiros raster devem ser Cloud-Optimized GeoTIFFs em **EPSG:3857** com **tamanho de tile 256×256** e o esquema de mosaico do Google Maps.

**Dados de banda única:**
```bash
gdalwarp <source.tif> <dest.tif> -of COG -t_srs EPSG:3857 \
  -co BLOCKSIZE=256 -co TILING_SCHEME=GoogleMapsCompatible
```

**Imagens RGB (satélite):**
```bash
gdalwarp <source.tif> <dest.tif> -of COG -t_srs EPSG:3857 \
  -co BLOCKSIZE=256 -co TILING_SCHEME=GoogleMapsCompatible \
  -co COMPRESS=JPEG -co ADD_ALPHA=NO -dstnodata NaN
```
:::

## Ligar Conjuntos de Dados Raster a Modelos de Dados

Adicione um Conjunto de Dados Raster à multi-selecção **Camadas Raster** de um Modelo de Dados para o tornar disponível como uma camada de mapa opcional no explorador. Apenas os Datasets Raster aprovados aparecem neste selector.
