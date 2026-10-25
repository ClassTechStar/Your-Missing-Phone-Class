---
id: di-san-shi-jiu-zhang
num: 39
part: ai-biancheng-pian
nav: Capítulo 39: Engenharia de contexto — fazendo a IA entender suas intenções
toc: default
kind: chapter
---

### Capítulo 39: Engenharia de contexto — fazer a IA entender a sua intenção

{class="chapter-intro mb-4"}
Já aconteceu de trocar de conversa e a IA "esquecer" tudo do seu projeto? Não é de propósito: ela é naturalmente esquecida. Este capítulo ensina a instalar um "sistema de memória de longo prazo" na IA e apresenta um dos paradigmas mais quentes de 2026 — o desenvolvimento orientado a especificação.

#### 1. Arquivo de memória do projeto: a "memória de longo prazo" da IA

Os modelos de IA têm uma limitação fundamental: a memória é de curto prazo. A cada nova conversa, a IA começa do zero sobre o seu projeto. Você precisa repetir "usamos React", "o backend é Node.js", "o banco é PostgreSQL", "o estilo usa aspas duplas". É ineficiente e fácil de esquecer — como treinar um estagiário novo todo dia.

A solução é o "arquivo de memória do projeto": um texto na raiz do projeto que a ferramenta de IA lê automaticamente ao iniciar a conversa. Cada ferramenta tem o seu nome:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ferramenta</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Nome do arquivo</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cursor</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.cursorrules</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Code</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">CLAUDE.md</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GitHub Copilot</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">copilot-instructions.md</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Solução genérica</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">AGENTS.md</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Convenções de nome do arquivo de memória por ferramenta

Os nomes mudam, o princípio é o mesmo: escreva no arquivo o que a IA deve "sempre lembrar". Um bom arquivo traz: visão geral do projeto (o que é), stack (tecnologias), padrões de código (nomenclatura, indentação, comentários), estrutura de pastas e convenções (branches, commits, testes). O CLAUDE.md de Karpathy tem só 70 linhas, mas cobre o essencial — conciso e completo.

::: div .code-block
:::inline div .code-head
<span>CLAUDE.md</span><span class="dots">···</span>
:::

```
# Projeto: app pessoal de controle financeiro
## Visão geral
Um app full-stack de finanças pessoais que ajuda a registrar receitas e despesas do dia a dia.
## Stack tecnológica
- Frontend: React + TypeScript + Tailwind CSS
- Backend: Node.js + Express + TypeScript
- Banco de dados: SQLite (dev) / PostgreSQL (produção)
- Testes: Vitest
## Padrões de código
- Usar aspas duplas
- Indentação de 2 espaços
- Nomes de função em camelCase
- Definições de tipo em PascalCase
- Toda função deve ter comentário JSDoc
## Estrutura de diretórios
/src
  /frontend  - código frontend
  /backend   - código backend
  /shared    - tipos compartilhados entre frontend e backend
  /tests     - arquivos de teste
## Convenções de desenvolvimento
- Mensagens de commit em português
- Recursos novos exigem testes primeiro
- APIs sempre retornam { success, data, error }
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Atenção: não vire um "segundo documento de requisitos"

{class="mt-1"}
Cuidado com o tamanho: não escreva dezenas de páginas. O objetivo é "dar contexto rápido à IA", não "descrever cada função em detalhe". Mantenha curto, estruturado e só com "o que a IA precisa saber".
:::

#### 2. Desenvolvimento orientado a especificação (SDD)

O Spec-Driven Development (SDD) amadureceu em 2026, com uma ideia em uma frase: escreva a especificação antes do código. Diferente do TDD clássico, a "spec" do SDD não é só casos de teste: inclui requisitos, definição de interfaces, modelos de dados etc. A IA gera o código a partir dela; os humanos escrevem e mantêm a especificação.

Fluxo do SDD em cinco passos:

1. Descreva os requisitos em linguagem natural (em um arquivo .md);
2. Defina interfaces e estruturas de dados (no mesmo arquivo);
3. Peça à IA que gere a implementação a partir da spec;
4. Rode testes para validar se a entrega segue a spec;
5. Se não seguir, corrija a spec ou peça à IA para corrigir o código.

Nesse fluxo, o arquivo de especificação é a "fonte única da verdade": o código pode ser regenerado, mas a spec precisa estar correta primeiro.

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> Escrever o arquivo de especificações</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> A especificação está completa?</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> Completa</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-robot mr-1"></i> A IA gera código a partir da especificação</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> Rodar testes para verificar o resultado</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-times-circle mr-1"></i> Incompleta / testes falham</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-tools mr-1"></i> Problema no código → corrige o código; problema na especificação → corrige a especificação</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> De volta à verificação</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> Tudo aprovado → entregar</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figura 3: fluxo de trabalho do desenvolvimento orientado a especificação (SDD)
:::

A vantagem do SDD é que a spec é mais estável que o código. Quando o modelo ou a ferramenta muda, a sua spec continua valendo — basta gerar o código de novo. É por isso que o livro insiste que "metodologia vale mais que ferramenta": a spec é o veículo concreto da sua metodologia.

#### 3. Gestão da janela de contexto

Mesmo com o arquivo de memória, ainda faltará contexto em conversas longas. A janela de contexto (quanto a IA processa ao mesmo tempo) é limitada. Com chat muito extenso e muitos arquivos citados, a IA "esquece" o começo e a qualidade cai — como uma conversa de seis horas em que o amigo já não lembra o que você disse na abertura.

A estratégia central é a "referência em camadas":

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Camada de contexto</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Conteúdo</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Como gerenciar</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1ª · Memória do projeto</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Stack, convenções, estrutura de pastas</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Em CLAUDE.md etc., carregado automaticamente, sem repetir</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2ª · Referência de arquivos</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Código envolvido na tarefa atual</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cite com @ com precisão; não cole o arquivo inteiro no chat</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3ª · Contexto da conversa</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Histórico do chat da tarefa atual</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ao concluir uma tarefa, abra um chat novo e evite inflar o contexto</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">4ª · Instrução imediata</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">O que se pede neste passo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Clara, curta e objetiva; sem descrições intermináveis</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Estratégia de gestão da janela de contexto em camadas

#### 4. Pontos práticos de engenharia de contexto

Engenharia de contexto não é uma configuração única; é um processo de melhoria contínua. Alguns pontos comprovados na prática:

1. Atualize o arquivo de memória junto com o projeto. Ao adotar uma tecnologia nova ou mudar a arquitetura, atualize o arquivo na hora — não explique de improviso no chat.
2. Prefira @ a colar textões. A maioria das ferramentas aceita @arquivo ou @pasta, injetando o conteúdo no contexto em segundo plano — mais eficiente e sem poluir a conversa.
3. Conversas curtas e cirúrgicas. Cada chat, uma tarefa ou um ponto de função. Ao concluir, abra outro. Conversas longas gastam a janela de contexto e "distraem" a IA.
4. Mostre o resultado em vez de descrever. Em bugs, @cite o log de erro em vez de dizer "parece que tem algum erro". A IA responde melhor à informação original do que à sua versão.
5. Limpe e arquive com regularidade. Conversas concluídas e arquivos temporários ocupam o espaço de trabalho. Manter o diretório limpo também ajuda a IA a entender a estrutura.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mão na massa: escreva um arquivo de memória de 70 linhas

{class="mt-1"}
Escolha um projeto em andamento (ou pretendido) e escreva um CLAUDE.md: visão geral (2–3 frases), stack (liste), padrões de código (3–5), estrutura de pastas (árvore) e convenções (2–3). Fique em até 70 linhas — ao final, a sua visão do projeto já estará mais clara.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumo do capítulo

- A memória da IA é de curto prazo: a cada conversa, começa do zero
- O arquivo de memória (CLAUDE.md etc.) é a memória de longo prazo e carrega sozinho em cada sessão
- Bom arquivo = visão + stack + padrões + pastas + convenções; 70 linhas bastam
- SDD: escreva a spec antes do código; a spec é a fonte única da verdade e é mais estável
- Contexto em quatro camadas: memória do projeto → @arquivos → histórico → instrução imediata
- Cinco práticas: atualizar, usar @, chat curto, mostrar o original, limpar
:::
