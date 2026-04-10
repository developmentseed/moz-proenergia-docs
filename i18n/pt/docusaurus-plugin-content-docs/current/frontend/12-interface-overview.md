---
sidebar_position: 12
title: "Visão Geral da Interface"
---

# 12. Visão Geral da Interface do Frontend

## 12.1 Como Começar

A interface de visualização do PROENERGIA+ é uma aplicação web — não é necessária instalação. Funciona em qualquer navegador moderno (Chrome, Firefox, Edge ou Safari).

| Nível de Acesso | O que pode fazer |
|---|---|
| **Público (não autenticado)** | Ver e explorar todos os Modelos de Dados públicos e aprovados. Aplicar filtros, ver popups e dados públicos. |
| **Utilizador Autenticado** | Aceder a todos os conjuntos de dados públicos mais quaisquer conjuntos de dados e modelos privados aprovados. Transferir todos os conjuntos de dados disponíveis a partir do frontend. |

## 12.2 Selecção de Idioma

A plataforma suporta **inglês** e **português** (predefinição). Para mudar de idioma, clique no botão **PT / EN** no canto superior direito do cabeçalho. A sua preferência é guardada no navegador e persiste entre sessões.

O conteúdo traduzido inclui: rótulos de navegação, rótulos de filtro, nomes de cenários, nomes de modelos, nomes de camadas e todas as strings da interface. As traduções em português provêm de:
- Ficheiros JSON de localidade para strings da interface
- Os campos `name_pt` / `description_pt` definidos nos Modelos de Dados, Cenários e Conjuntos de Dados na plataforma administrativa

## 12.3 Disposição em Três Painéis

| Painel | Localização / Função |
|---|---|
| **Barra Lateral de Navegação de Modelos** | Extrema esquerda. Lista todos os Modelos de Dados públicos com ícones únicos, ordenados pela Ordem de Apresentação. Clique em qualquer ícone para activar esse modelo. |
| **Painel de Filtros / Controlo** | Painel esquerdo. Contém o selector de cenários e todos os controlos de filtro. Pode ser recolhido usando o botão de alternância na sua margem direita. |
| **Painel do Mapa** | Centro. Mapa MapLibre GL interactivo que apresenta a camada de tiles vectoriais PMTiles do cenário activo. |
| **Painel de Resumo de Análise** | Direita. Apresenta estatísticas agregadas para o cenário actual e filtros activos. Também mostra o detalhe de características quando uma característica do mapa é clicada. |
