---
sidebar_position: 11
title: "Referência da API"
---

# 11. Referência da API

- **URL Base:** `/api/v1/`
- **Documentação Swagger:** `/api/v1/docs/`
- **Esquema OpenAPI:** `/api/v1/schema/`

## Endpoints

| Endpoint | Descrição |
|---|---|
| `GET /api/v1/model/` | Lista todos os Modelos de Dados públicos. Os não-superutilizadores vêem apenas modelos com `is_public=True`. Retorna `filter_fields`, `popup_fields`, `summary_fields`, `color_coding`, `metric_field_types`, `scenarios`, `name_pt`, `description_pt`, `presentation_order`. |
| `GET /api/v1/model/{id}/` | Recupera um único Modelo de Dados por ID. |
| `GET /api/v1/vector/` | Lista ConjuntosDadosVectoriais. Público+aprovado para anónimos; todos os aprovados para autenticados; todos para superutilizadores. |
| `GET /api/v1/vector/{id}/` | Recupera um único ConjuntoDadosVectorial. |
| `GET /api/v1/raster/` | Lista ConjuntosDadosRaster. As mesmas regras de visibilidade que os conjuntos de dados vectoriais. |
| `GET /api/v1/raster/{id}/` | Recupera um único ConjuntoDadosRaster. |
| `GET /api/v1/reference/` | Lista ConjuntosDadosReferência. As mesmas regras de visibilidade que os conjuntos de dados vectoriais. |
| `GET /api/v1/reference/{id}/` | Recupera um único ConjuntoDadosReferência. |
| `GET /api/v1/scenario/{id}/feature/{feature_id}/` | Recupera todos os metadados armazenados para uma única característica. Usado para preencher popups do mapa. |
| `GET /api/v1/scenario/{id}/summaries/` | Calcula resumos estatísticos. Consulte a Secção 11.1. |
| `DELETE /api/v1/scenario/{id}/summaries/cache/` | Limpa as respostas de resumo em cache para um cenário. |
| `POST /api/v1/token-auth/` | Obtém um token de autenticação. Corpo: `{"username": "...", "password": "..."}` |

## 11.1 Endpoint de Resumos

`GET /api/v1/scenario/{id}/summaries/`

| Parâmetro | Descrição |
|---|---|
| `fields` (obrigatório) | Nomes de colunas separados por vírgulas para agregar. Ex. `fields=Pop2030,Technology2030` |
| `q` (opcional) | Expressão de filtro. Condições separadas por vírgulas: `campo=valor` (igualdade); `campo__min=N` e `campo__max=N` (intervalo numérico); `campo__in=val1;val2` (string de múltiplos valores). |
| `group_by` (opcional) | Nome(s) de coluna(s) do tipo string separados por vírgulas. Deve estar em `metric_field_types`. Máximo 2 campos para agrupamento aninhado. |

### Exemplos de Filtros

```bash
# Correspondência de valor único
?fields=Pop2030&q=Technology2030=SHS

# Intervalo numérico
?fields=InvestmentCostTotal&q=Pop2030__min=100,Pop2030__max=5000

# Filtro de string de múltiplos valores
?fields=Pop2030&q=Technology2030__in=SHS;MiniGrid

# Com agrupamento
?fields=Pop2030&q=Admin_1=Maputo&group_by=Technology2030

# Agrupamento aninhado de dois níveis
?fields=Pop2030&group_by=Admin_1,Technology2030
```

### Estrutura da Resposta

```json
{
  "scenario_id": 1,
  "filters_applied": "Admin_1=Maputo",
  "summaries": {
    "Pop2030": {
      "type": "numeric",
      "count": 7354,
      "min": 3.69,
      "max": 3620782.55,
      "sum": 4466719.88
    },
    "Technology2030": {
      "type": "string",
      "count": 7354,
      "values": { "SHS": 2100, "MiniGrid": 850, "Grid": 4404 }
    }
  }
}
```

:::note Cache
As respostas de resumo são armazenadas em cache por 24 horas. Use `DELETE /summaries/cache/` após carregar novos dados de Ficheiro de Cenário.
:::
