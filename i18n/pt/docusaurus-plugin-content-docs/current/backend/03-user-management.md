---
sidebar_position: 3
title: "Gestão de Utilizadores"
---

# 3. Gestão de Utilizadores

## 3.1 Funções e Permissões dos Utilizadores

| Permissão | Utilizador | Administrador | Super Administrador |
|------------|:----:|:-----:|:-----------:|
| **VER TODOS OS DADOS** | | | |
| Ver e explorar Modelos de Dados públicos (frontend) | ✓ | ✓ | ✓ |
| Ver Modelos de Dados privados (frontend / API) | — | — | ✓ |
| Transferir conjuntos de dados públicos | ✓ | ✓ | ✓ |
| Transferir conjuntos de dados privados | — | ✓ | ✓ |
| **GESTÃO DE DADOS** | | | |
| Carregar ficheiros vectoriais / raster / referência | — | ✓ | ✓ |
| Editar metadados de conjuntos de dados e configuração JSON | — | ✓ | ✓ |
| Eliminar conjuntos de dados | — | — | ✓ |
| Adicionar / editar Modelos de Dados | — | ✓ | ✓ |
| Definir flag `is_public` do Modelo de Dados | — | — | ✓ |
| Adicionar / editar Cenários e Ficheiros de Cenário | — | ✓ | ✓ |
| Publicar / despublicar conjuntos de dados (`is_approved`) | — | — | ✓ |
| **GESTÃO DE UTILIZADORES** | | | |
| Criar / editar / eliminar contas de utilizador | — | — | ✓ |

### Como as funções mapeiam para os flags Django

| Flags Django | Função |
|---|---|
| `is_staff = False`, `is_superuser = False` | Utilizador Padrão — apenas frontend, sem acesso ao painel de administração. |
| `is_staff = True`, `is_superuser = False` | Administrador — pode aceder ao painel de administração, gerir os seus próprios conjuntos de dados e cenários. Não pode gerir utilizadores nem publicar conjuntos de dados. |
| `is_staff = True`, `is_superuser = True` | Super Administrador — ignora todas as verificações de permissão. Acesso total a tudo. |

## 3.2 Criar um Novo Utilizador

1. Vá a **Autenticação e Autorização → Utilizadores → + Adicionar Utilizador**.
2. Introduza um nome de utilizador e palavra-passe, depois clique em **Guardar e continuar a editar**.
3. Preencha as informações pessoais (nome próprio, apelido, correio electrónico).
4. Defina o nível de permissão adequado (consulte a Secção 3.3). Clique em **Guardar**.

## 3.3 Definir a Função de um Utilizador

| Caixa de verificação | Efeito |
|---|---|
| **Activo** (marcado) | A conta está activa. Desmarque para desactivar sem eliminar. |
| **Estado de pessoal** (marcado) | Concede acesso ao Painel de Administração Django. Necessário para as funções de Administrador e Super Administrador. |
| **Estado de superutilizador** (marcado) | Acesso total sem restrições. Necessário para a função de Super Administrador. |

- **Utilizador Padrão:** Deixe ambas as caixas desmarcadas.
- **Administrador:** Marque apenas o Estado de pessoal. Opcionalmente, atribua permissões específicas ao nível do modelo.
- **Super Administrador:** Marque tanto o Estado de pessoal como o Estado de superutilizador.

## 3.4 Atribuir Permissões Específicas a Utilizadores Administradores

No multi-selecção **Permissões do Utilizador**, conceda:

- `conjuntos de dados | modelo de dados | Pode adicionar/alterar/ver modelo de dados`
- `conjuntos de dados | conjunto de dados vectorial | Pode adicionar/alterar/ver conjunto de dados vectorial`
- `conjuntos de dados | ficheiro vectorial | Pode adicionar/alterar/ver ficheiro vectorial`
- `conjuntos de dados | conjunto de dados raster | Pode adicionar/alterar/ver conjunto de dados raster`
- `conjuntos de dados | conjunto de dados de referência | Pode adicionar/alterar/ver conjunto de dados de referência`
- `conjuntos de dados | cenário | Pode adicionar/alterar/ver cenário`
- `conjuntos de dados | ficheiro de cenário | Pode adicionar/alterar/ver ficheiro de cenário`

:::note
As contas de Super Administrador ignoram todas as verificações de permissão granular. As permissões específicas só precisam de ser definidas para contas de Administrador ao nível de pessoal.
:::

## 3.5 Editar e Desactivar Utilizadores

Vá a **Autenticação e Autorização → Utilizadores** e clique num nome de utilizador para editar. Para desactivar sem eliminar, desmarque a caixa de verificação **Activo** e clique em **Guardar**.
