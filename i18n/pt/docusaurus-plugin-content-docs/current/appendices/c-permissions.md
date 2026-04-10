---
sidebar_position: 102
title: "Apêndice C — Matriz de Permissões"
---

# Apêndice C — Resumo da Matriz de Permissões

| Acção | Utilizador | Administrador | Super Administrador |
|--------|:----:|:-----:|:-----------:|
| **VER E TRANSFERIR** | | | |
| Ver e explorar Modelos de Dados públicos (frontend) | ✓ | ✓ | ✓ |
| Ver Modelos de Dados privados (frontend / API) | — | — | ✓ |
| Transferir conjuntos de dados públicos | ✓ | ✓ | ✓ |
| Transferir conjuntos de dados privados | — | ✓ | ✓ |
| **ADMINISTRAÇÃO DE BACKEND** | | | |
| Aceder ao Painel de Administração Django | — | ✓ | ✓ |
| Carregar ficheiros vectoriais / raster / referência | — | ✓ | ✓ |
| Editar configuração JSON do Modelo de Dados | — | ✓ | ✓ |
| Definir flag `is_public` do Modelo de Dados | — | — | ✓ |
| Adicionar / editar Cenários e Ficheiros de Cenário | — | ✓ | ✓ |
| Publicar / despublicar conjuntos de dados (`is_approved`) | — | — | ✓ |
| Definir flag `is_public` nos conjuntos de dados | — | — | ✓ |
| Eliminar qualquer registo de dados | — | — | ✓ |
| Criar e gerir contas de utilizador | — | — | ✓ |
