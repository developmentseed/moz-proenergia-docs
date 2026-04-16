---
title: "Fluxos de Trabalho Comuns de Administração"
---

# Fluxos de Trabalho Comuns de Administração

As secções deste guia abordam cada componente da plataforma de forma independente. Esta página reúne tudo em sequências passo a passo que irá seguir na gestão da plataforma.

---

## Adicionar um Novo Modelo de Dados

Um Modelo de Dados é o contentor de nível superior para uma categoria de análise de planeamento. Cada Modelo de Dados requer um Dataset Vetorial como unidade base de análise — o Dataset Vetorial fornece as características geográficas (assentamentos, linhas de rede, polígonos) às quais os dados do seu cenário serão associados.

:::note O que é um Dataset Vetorial?
Um Dataset Vetorial é um contentor nomeado para geometria espacial — a colecção de pontos, linhas ou polígonos que são renderizados no mapa. Armazena um ou mais ficheiros geoespaciais carregados (.geojson, .gpkg, .zip, .kml) e converte-os em PMTiles optimizados para entrega de mapa. Pense nele como a "camada de mapa base" à qual todos os dados de cenários são associados.
:::

### Passo 1 — Preparar um Dataset Vetorial

Antes de criar um Modelo de Dados, precisa de um Dataset Vetorial com pelo menos um ficheiro em estado **Pronto**.

- **Usar um dataset existente:** Vá a Datasets → Datasets Vetoriais e confirme que o conjunto de dados que pretende tem um ficheiro Pronto. Se tiver, avance para o Passo 2.
- **Criar um novo dataset:** Consulte [Datasets Vectoriais e Ficheiros Vectoriais](./vector-datasets). Em resumo:
  1. Vá a Datasets → Datasets Vectoriais → + Adicionar Dataset Vetorial.
  2. Preencha o nome e os campos de metadados. Clique em Guardar.
  3. Vá a Datasets → Ficheiros Vectoriais → + Adicionar Ficheiro Vetorial. Seleccione o seu novo conjunto de dados, carregue o ficheiro geoespacial e clique em Guardar.
  4. Aguarde que o processamento em segundo plano conclua — o estado do ficheiro deve atingir **Pronto** antes de poder continuar. Actualize a lista de Ficheiros Vectoriais para verificar.

### Passo 2 — Criar a Configuração do Modelo de Dados

Vá a Datasets → Modelos de Dados → + Adicionar Modelo de Dados.

Preencha o nome, a descrição e a ordem de apresentação. Depois configure os quatro campos JSON:

- **`filter_fields`** — define os controlos de filtro no painel esquerdo
- **`popup_fields`** — define os atributos mostrados quando um utilizador clica numa característica
- **`summary_fields`** — define as estatísticas agregadas no painel direito
- **`color_coding`** — mapeia os valores da coluna de visualização para cores do mapa

:::warning Verifique os nomes das colunas antes de guardar
Cada valor `"column"` em `filter_fields` e `popup_fields`, e cada entrada em `"columns"` em `summary_fields`, deve corresponder exactamente a um nome de coluna no CSV do cenário que planeia carregar — incluindo maiúsculas/minúsculas. O painel de administração não pode verificar isto por si. Um nome de coluna mal configurado resultará em valores popup em branco ou estatísticas de resumo a zero.

Consulte [Campos de Configuração JSON](./json-configuration) para referência completa de esquema e exemplos.
:::

Clique em Guardar.

### Passo 3 — Criar o Cenário

Vá a Datasets → Cenários → + Adicionar Cenário.

- Defina o **Nome** como um rótulo descritivo (aparece no menu suspenso de cenários do frontend).
- Defina o **Modelo** para o Modelo de Dados que acabou de criar.
- Defina o **Dataset Vetorial** para o conjunto de dados do Passo 1.
- Defina a **Ordem de Apresentação** se tiver múltiplos cenários e quiser controlar a sua ordem no menu suspenso.

Clique em Guardar.

### Passo 4 — Carregar o Ficheiro de Cenário

Vá a Datasets → Ficheiros de Cenário → + Adicionar Ficheiro de Cenário.

Seleccione o seu novo Cenário no menu suspenso e, em seguida, carregue o seu ficheiro CSV.

:::note Requisitos do CSV
- **Formato:** Apenas CSV. O delimitador é detectado automaticamente (vírgula ou ponto e vírgula).
- **Codificação:** UTF-8. Use UTF-8 com BOM se os seus dados contiverem caracteres especiais (letras acentuadas, etc.).
- **Coluna obrigatória:** O ficheiro deve conter uma coluna `id` cujos valores correspondam aos IDs de características no Dataset Vetorial ligado.
- **Sem IDs duplicados:** Cada valor de `id` deve aparecer apenas uma vez.
- **Completude de colunas:** O ficheiro deve conter todas as colunas referenciadas na configuração `filter_fields`, `popup_fields` e `summary_fields` do Modelo de Dados.
:::

Opcionalmente, marque **Representar características como pontos em níveis de zoom inferiores** se o seu conjunto de dados for uma grande grelha de polígonos e quiser melhor desempenho do mapa à escala nacional.

Clique em Guardar. O processamento em segundo plano começa automaticamente — o ficheiro passará por **Criado → Em Processamento → Pronto**. Se atingir **Erro**, abra o registo para ler a Mensagem de Erro.

### Passo 5 — Verificar

Assim que o Ficheiro de Cenário atingir o estado Pronto:

1. Abra o frontend e navegue para o seu novo modelo na barra lateral.
2. Confirme que o cenário aparece no menu suspenso de cenários.
3. Confirme que as características do mapa são visíveis.
4. Verifique que os controlos de filtro correspondem à sua configuração `filter_fields`.
5. Verifique que o painel de resumo é preenchido com valores.

Se o painel de resumo mostrar todos os zeros, o campo `metric_field_types` no Modelo de Dados pode não ter sido preenchido ainda. Este é preenchido automaticamente quando a importação do Ficheiro de Cenário conclui. Verifique que a tarefa de importação concluiu sem erros em Painel de Administração Django → Django Celery Results → Resultados de Tarefas.

---

## Adicionar um Novo Cenário a um Modelo Existente

Use este fluxo de trabalho quando um Modelo de Dados já existe e quer adicionar uma nova execução de cenário (por ex. um novo ano, uma suposição de procura diferente, ou resultados de modelo actualizados).

### Passo 1 — Confirmar o Dataset Vetorial

Identifique qual Dataset Vetorial o novo cenário deve usar. Deve ter um ficheiro em estado **Pronto**. Pode reutilizar o mesmo Dataset Vetorial de um cenário existente neste modelo — os cenários partilham geometria.

### Passo 2 — Criar o Cenário

Vá a Datasets → Cenários → + Adicionar Cenário.

- Defina o **Modelo** para o Modelo de Dados existente.
- Defina o **Dataset Vetorial** para o conjunto de dados adequado.
- Defina o **Nome** e a **Ordem de Apresentação**.

Clique em Guardar.

### Passo 3 — Carregar o Ficheiro de Cenário

Siga o mesmo processo do Passo 4 no fluxo de trabalho acima. O CSV deve conter as mesmas colunas referenciadas na configuração JSON do Modelo de Dados existente, uma vez que a configuração do Modelo de Dados é partilhada por todos os cenários.

:::tip
Não precisa de alterar a configuração do Modelo de Dados para adicionar um novo cenário. Os filtros, popups e campos de resumo são definidos uma vez no Modelo de Dados e aplicam-se a todos os cenários sob ele.
:::

---

## Reprocessar Ficheiros de Cenário Após Alterações ao Modelo de Dados

Se actualizar a configuração `filter_fields`, `popup_fields` ou `summary_fields` de um Modelo de Dados depois de os ficheiros de cenário já terem sido processados, os **tiles de mapa** (PMTiles) e as **métricas de resumo** podem estar dessincronizados com a nova configuração.

### Quando o reprocessamento é necessário

| Alteração efectuada | Reprocessamento de PMTiles necessário? | Reprocessamento de métricas necessário? |
|---|:---:|:---:|
| Adicionada uma nova coluna a `filter_fields` | Sim | Sim |
| Alterado apenas um `label` ou `description` | Não | Não |
| Alteradas as colunas ou o método de `summary_fields` | Não | Sim |
| Alterada a coluna de `popup_fields` | Não | Não |
| Alterado `color_coding` ou `visualization_column` | Sim | Não |

### Reprocessar tiles de mapa (PMTiles)

Os PMTiles são gerados a partir de uma combinação da geometria vectorial e apenas as colunas listadas em `filter_fields` (mais o `visualization_column`). Se adicionar uma nova coluna de filtro, os PMTiles existentes não a conterão e a filtragem ao nível do mapa não funcionará correctamente.

1. Vá a Datasets → Ficheiros de Cenário.
2. Seleccione o(s) Ficheiro(s) de Cenário afectado(s) usando as caixas de verificação.
3. No menu suspenso **Acções**, seleccione **Reprocessar ficheiros** e clique em Ir.
4. Aguarde que o estado retorne a **Pronto**.

:::note
Apenas os ficheiros em estado **Pronto** ou **Erro** podem ser re-enfileirados. Os ficheiros em estado **Criado** ou **Em Processamento** não podem ser reprocessados.
:::

### Reprocessar métricas de resumo

As métricas de resumo são armazenadas numa tabela desnormalizada (`ScenarioDataMetrics`) que é preenchida a partir do CSV do cenário na importação. Se adicionar colunas a `summary_fields`, as métricas existentes não incluirão essas colunas e o painel de resumo mostrará zeros para os novos campos.

Use o comando de gestão para ressincronizar as métricas de um cenário específico:

```bash
cd /var/www/proenergia/app
source venv/bin/activate
python manage.py sync_scenario_metrics --scenario-id <scenario_id>
```

Substitua `<scenario_id>` pelo ID numérico do cenário (visível no URL quando visualiza o cenário no painel de administração).

O comando irá limpar as métricas existentes para esse cenário e re-extrair todos os campos configurados dos dados CSV armazenados. Também actualiza o mapeamento `metric_field_types` no Modelo de Dados, que é necessário para a API de resumos reconhecer novos tipos de colunas.

:::tip Encontrar o ID do cenário
Vá a Datasets → Cenários e clique no nome do cenário. O ID aparece no URL do navegador: `/admin/datasets/scenario/<id>/change/`.
:::

### Reprocessar ambos

Se a alteração ao Modelo de Dados afectar tanto os tiles como as métricas (por ex. adicionar uma coluna que é simultaneamente um campo de filtro e de resumo), execute ambos os passos: reprocesse o Ficheiro de Cenário através da acção do painel de administração primeiro, depois execute o comando `sync_scenario_metrics` após o ficheiro atingir o estado Pronto.
