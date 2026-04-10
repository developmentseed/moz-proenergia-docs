---
sidebar_position: 8
title: "Conjuntos de Dados Raster e Ficheiros Raster"
---

# 8. Conjuntos de Dados Raster e Ficheiros Raster

Os Conjuntos de Dados Raster armazenam imagens georeferenciadas (fotografias de satélite, modelos de terreno, resultados raster derivados). São apresentados como camadas Cloud-Optimized GeoTIFF (COG). Ao contrário dos dados vectoriais, os ficheiros raster não requerem conversão PMTiles — são servidos directamente a partir do armazenamento de objectos.

## 8.1 Adicionar um Conjunto de Dados Raster

1. Vá a **Conjuntos de Dados → Conjuntos de Dados Raster → + Adicionar Conjunto de Dados Raster**.
2. Preencha os mesmos campos de metadados que os Conjuntos de Dados Vectoriais (nome, descrição, fonte, contacto, SRC, etc.). Suporta traduções EN/PT.
3. Clique em **Guardar**. Em seguida, adicione um Ficheiro Raster.

## 8.2 Adicionar Ficheiros Raster

1. Vá a **Conjuntos de Dados → Ficheiros Raster → + Adicionar Ficheiro Raster**.
2. Seleccione o Conjunto de Dados Raster pai.
3. Carregue um ficheiro raster. Formatos aceites: `.tiff`, `.tif`, `.geotiff`, `.gtiff`, `.vrt`.
4. Clique em **Guardar**.

:::warning Requisitos COG
Para melhor desempenho, os ficheiros raster devem ser Cloud-Optimized GeoTIFFs em **EPSG:3857** com **tamanho de bloco 256×256** e o esquema de mosaico do Google Maps.

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

## 8.3 Ligar Conjuntos de Dados Raster a Modelos de Dados

Adicione um Conjunto de Dados Raster à multi-selecção **Camadas Raster** de um Modelo de Dados para o tornar disponível como uma camada de mapa opcional no explorador. Apenas os Conjuntos de Dados Raster aprovados aparecem neste selector.
