---
sidebar_position: 10
title: "Monitorização e Resolução de Problemas"
---

# 10. Monitorização e Resolução de Problemas

## 10.1 Monitorizar Tarefas em Segundo Plano

- **No Painel de Administração Django:** Vá a **Django Celery Results → Resultados de Tarefas** para ver todas as tarefas concluídas, falhadas e pendentes.
- **Via Flower (desenvolvimento local):** Execute `celery -A proenergia flower --address=127.0.0.1 --port=5555` e aceda a `http://localhost:5555`.

## 10.2 Resolução de Problemas do Painel de Administração

| Problema | Causa e Resolução |
|---|---|
| FicheiroVectorial bloqueado em Processamento | O trabalhador Celery não está em execução. Reinicie: `sudo systemctl restart proenergia-celery` |
| FicheiroVectorial / FicheiroCenário mostra Erro | Abra o registo e leia a **Mensagem de Erro**. Causas comuns: SRC não suportado, ficheiro corrompido, ou CSV sem a coluna `id`. |
| `filter_fields` falha: Falta uma chave obrigatória | Cada entrada deve ter as três chaves: `label`, `description`, `column`. |
| `summary_fields` falha: a chave columns deve ser uma lista | A chave `columns` deve ser um array JSON mesmo para uma coluna: `["MinhaColuna"]` |
| `summary_fields` falha: chartType inválido | Valores válidos: `bar`, `donut`, `stacked`, `column`, `area`, `highlight`. |
| `color_coding` falha: cor inválida | Cada cor deve ser um código hexadecimal válido de 3 ou 6 dígitos (ex. `#FF0000`). |
| O frontend não mostra características (mapa em branco) | O FicheiroCenário do Cenário deve estar em estado Pronto. Verifique o processamento do ficheiro. |
| O painel de resumo mostra todos os zeros | `metric_field_types` pode não estar preenchido. É preenchido automaticamente na importação bem-sucedida do Ficheiro de Cenário. |
| O início de sessão no painel de administração mostra 403 | O utilizador existe mas não tem Estado de pessoal. Um Super Administrador deve activá-lo. |
| O modelo não é visível no frontend | O flag `is_public` do Modelo de Dados é `False`. Apenas os superutilizadores podem ver modelos privados. |
