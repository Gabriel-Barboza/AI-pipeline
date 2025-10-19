# Regras para Geração de Mensagens de Commit

Ao gerar mensagens de commit, siga estritamente o padrão Conventional Commits:
`<tipo>(<escopo opcional>): <descrição>`

## 1. Tipos Permitidos:
* **feat**: (Nova funcionalidade)
* **fix**: (Correção de bug)
* **docs**: (Mudanças apenas na documentação)
* **style**: (Formatação, ponto e vírgula, etc; sem mudança de lógica)
* **refactor**: (Refatoração de código, sem mudança de comportamento)
* **test**: (Adicionando ou corrigindo testes)
* **chore**: (Atualização de dependências, tarefas de build, etc)

## 2. Escopo:
* Opcional. Se usado, deve estar entre parênteses.
* Deve ser um substantivo em minúsculo descrevendo a área do código (ex: `api`, `ui`, `auth`).

## 3. Descrição:
* Obrigatória.
* Comece com letra minúscula.
* Use o modo imperativo (ex: "adicionar", "corrigir", "remover" em vez de "adicionado" ou "adicionando").
* Seja curta e direta.
* Não termine com ponto final.

## Exemplos:
* `feat(api): adicionar endpoint de criação de usuário`
* `fix(ui): corrigir bug de alinhamento no modal de login`
* `docs: atualizar o README com instruções de setup`
* `chore: atualizar versão do react para 18.2.0`