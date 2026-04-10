---
sidebar_position: 1
title: Introdução
---

# Guia do Utilizador da Plataforma IEP PROENERGIA+

**MIREME UIPCE · SE4ALL · Development Seed** — Versão 1.2 · 2026

O PROENERGIA+ IEP é uma infraestrutura de dados espaciais e plataforma de visualização para o planeamento integrado da electrificação em Moçambique. Permite que os decisores nacionais e provinciais explorem cenários de acesso à energia utilizando os dados geoespaciais mais recentes, analisem resultados ao nível de assentamentos e exportem informações úteis para a tomada de decisão.

Este guia está dividido em três partes:

- **[Backend](./backend/accessing-admin)** — Interface de administração Django, gestão de utilizadores, configuração do modelo de dados, gestão de cenários e conjuntos de dados, configuração JSON e referência da API.
- **[Frontend](./frontend/interface-overview)** — Interface de visualização, controlos de filtro, interacção com o mapa, selecção de cenários, resumos de análise e transferências.
- **[Implantação](./deployment/server-requirements)** — Configuração do servidor, serviços systemd, Nginx, Celery, RabbitMQ, variáveis de ambiente e procedimentos de actualização.

## Arquitectura do Sistema

| Componente | Descrição |
|-----------|-------------|
| API de Backend (Django REST) | Fornece dados ao frontend. Django + DRF, suportado por PostgreSQL 16 / PostGIS. Administração em `/admin/`. API em `/api/v1/`. |
| Fila de Tarefas (Celery / RabbitMQ) | Trabalhadores em segundo plano para conversão de ficheiros (GDAL → FlatGeobuf → PMTiles via Tippecanoe). |
| Frontend (Next.js / TypeScript) | Cartografia MapLibre GL + Chakra UI. Suporta inglês e português (predefinição). |
| Armazenamento de Objectos | Armazena ficheiros fonte carregados e PMTiles derivados. |
| Entrega de Tiles (PMTiles) | Tiles vectoriais via pedidos de intervalo HTTP. Camadas raster via Cloud-Optimized GeoTIFF (COG). |
