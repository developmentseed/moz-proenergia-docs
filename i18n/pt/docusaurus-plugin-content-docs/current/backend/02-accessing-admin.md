---
sidebar_position: 2
title: "Aceder ao Painel de Administração"
---

# 2. Aceder ao Painel de Administração Django

## 2.1 URL e Início de Sessão

O Painel de Administração Django está acessível em:

- **Produção:** `https://<domínio-de-implantação>/admin/`
- **Desenvolvimento local:** `http://localhost:8000/admin/`

Inicie sessão com uma conta de pessoal ou superutilizador. Navegue até à página de início de sessão, introduza as suas credenciais e clique em **Iniciar Sessão**.

:::note
Numa implantação nova, é necessário criar um superutilizador através da linha de comandos antes de qualquer pessoa poder iniciar sessão. Consulte a Secção 2.3.
:::

## 2.2 Ecrã Inicial do Painel de Administração

Após iniciar sessão, o painel de administração lista todos os grupos de modelos registados:

- **Autenticação e Autorização** — Gestão de Utilizadores e Grupos
- **Conjuntos de Dados** — ModeloDados, ConjuntoDadosVectorial, FicheiroVectorial, ConjuntoDadosRaster, FicheiroRaster, ConjuntoDadosReferência, FicheiroReferência, Cenário, FicheiroCenário

## 2.3 Criar o Superutilizador Inicial (CLI)

```bash
cd /var/www/proenergia/app
source venv/bin/activate
python manage.py createsuperuser
```

:::note
As contas de superutilizador devem ser restritas a um pequeno número de administradores de confiança. Utilize contas de Administrador ao nível de pessoal para a gestão do dia-a-dia.
:::
