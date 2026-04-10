---
sidebar_position: 19
title: "Resolução de Problemas do Frontend"
---

# 19. Resolução de Problemas do Frontend

| Problema | Causa e Resolução |
|---|---|
| Tiles do mapa não carregam (mapa em branco) | Verifique a conectividade de rede e actualize. Os PMTiles do FicheiroCenário podem não ter sido gerados — contacte um administrador para verificar o estado do ficheiro. |
| O painel de filtros aparece vazio | O Modelo de Dados não tem `filter_fields`, ou os metadados falharam ao carregar. Recarregue a página. O administrador deve verificar a configuração JSON. |
| As estatísticas de resumo não actualizam | Certifique-se de que os filtros foram aplicados com o botão **Aplicar**. Verifique a consola do navegador (F12) para erros de rede. |
| Não consigo iniciar sessão | Verifique o nome de utilizador e a palavra-passe. Contacte o seu Super Administrador para repor as credenciais. |
| O botão de transferência está desactivado | Certifique-se de que tem sessão iniciada. Os conjuntos de dados privados requerem uma sessão autenticada. |
| O popup mostra valores em branco ou indefinidos | O nome da coluna `popup_fields` não corresponde ao nome da propriedade CSV (sensível a maiúsculas/minúsculas). O administrador deve verificar o nome do campo. |
| O menu suspenso de cenários mostra apenas uma opção | Apenas os cenários com um FicheiroCenário em estado Pronto são mostrados. Carregue e processe Ficheiros de Cenário através do painel de administração. |
| O botão de alternância de idioma não está disponível | O selector de idioma aparece na navegação do cabeçalho. Recarregue a página se estiver em falta. |
| Dados no idioma errado | Clique no botão PT/EN no cabeçalho. Se o conteúdo traduzido estiver em falta, um administrador deve preencher os campos `name_pt` / `description_pt` no painel de administração. |
| O modelo não aparece na barra lateral | O flag `is_public` do Modelo de Dados é `False`. Contacte um Super Administrador para activá-lo. |
