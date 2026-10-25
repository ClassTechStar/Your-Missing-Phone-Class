---
id: di-si-shi-si-zhang
num: 44
part: ai-biancheng-pian
nav: Capítulo 44: Prática do zero ao um — o fluxo completo de um projeto
toc: default
kind: chapter
---

### Capítulo 44: Prática do 0 ao 1 — o fluxo completo de um projeto inteiro

{class="chapter-intro mb-4"}
A teoria acabou; agora é hora de colocar a mão na massa. Este capítulo não é um tutorial simples de 'digitar junto', mas uma metodologia prática de 'como pensar, como pedir e como validar'. Usaremos três projetos de dificuldades diferentes para mostrar o processo completo de raciocínio, dos requisitos ao produto final. Não importa qual ferramenta você use: esse fluxo serve para todos.

#### 1. Projeto 1: site pessoal minimalista de ferramentas (nível iniciante)

##### 1. Pensando nos requisitos

Objetivo: criar uma página pessoal de ferramentas que exiba os atalhos para 3 ou 4 utilitários práticos. É um projeto puramente de front-end, sem back-end nem banco de dados. O ponto principal não é a complexidade das ferramentas, mas vivenciar o fluxo completo 'dos requisitos ao produto final'.

Seguindo os cinco elementos de requisitos: Who (quem) — uso pessoal. What (o quê) — uma página que exibe os atalhos das ferramentas. Why (por quê) — reunir as ferramentas mais usadas em uma única página para facilitar o acesso. How (como) — um único arquivo HTML+CSS+JS, sem frameworks. Constraint (restrição) — pronto em até 30 minutos, sem precisar fazer deploy.

##### 2. Passando as instruções

Seguindo o princípio Think Before Coding, a sua instrução deve conter informações suficientes para a IA entender o objetivo, sem precisar especificar cada detalhe de implementação:

::: div .code-block
:::inline div .code-head
<span>Instrução para a IA</span><span class="dots">···</span>
:::

```
Crie uma página web de caixa de ferramentas pessoal, requisitos:
1. HTML em arquivo único (CSS e JS inline), sem frameworks
2. Tema escuro, estilo minimalista moderno
3. Mostrar 4 cards de ferramentas:
   - Resumidor de texto
   - Contador de palavras
   - Seletor de cores
   - Gerador de QR code
4. Cada card tem ícone, título e descrição curta
5. Os cards têm animação ao passar o mouse
6. Layout responsivo, utilizável no celular
7. Uma barra de título no topo
Dê diretamente o arquivo HTML completo.
```
:::

##### 3. Aceitação e iteração

Depois que a IA entregar o código, faça a aceitação com as três camadas de verificação da iteração. Primeira camada, verificação funcional: o arquivo abre no navegador? Os 4 cartões aparecem? A animação ao passar o mouse funciona? Segunda camada, verificação de limites: o layout fica correto no tamanho de tela de celular? Os cartões quebram a linha quando a janela é muito estreita? Terceira camada, verificação de arquitetura: o código é legível? O CSS está embutido em uma única tag style? Há redundâncias evidentes?

Se você também quiser implementar a função de algum cartão de ferramenta (e não apenas o atalho), adicione aos poucos — implemente a função de uma ferramenta por vez, valide e só depois adicione a próxima. É a aplicação prática da estratégia de 'passos pequenos e rápidos'.

#### 2. Projeto 2: sistema de controle financeiro full stack (nível intermediário)

##### 1. Requisitos e PRD

Objetivo: uma aplicação de controle financeiro full stack, com front-end, back-end e banco de dados. Este projeto é bem mais complexo que o primeiro e vai usar os métodos de engenharia de requisitos do Capítulo 40.

Comece escrevendo o PRD. Usando o modelo da Seção 3 do Capítulo 40, escreva a visão geral do projeto, a lista de funcionalidades, a solução técnica, o modelo de dados e o plano de desenvolvimento. Na escolha da solução técnica, considere o princípio Simplicity First — front-end em React, mas sem gerenciamento de estado complexo como o Redux; back-end em Node.js, mas sem microsserviços; banco de dados SQLite em vez de PostgreSQL (na fase de desenvolvimento).

O plano de desenvolvimento se divide em 5 passos: Passo 1, esqueleto da API no back-end (servidor Express + SQLite + endpoints CRUD); Passo 2, páginas básicas do front-end (lista de lançamentos + formulário de adição); Passo 3, integração entre front-end e back-end (chamadas de API + exibição dos dados); Passo 4, categorias e filtros; Passo 5, resumo mensal e gráficos simples. Ao fim de cada passo, você tem algo 'que funciona'.

##### 2. Criando o arquivo de memória do projeto

Antes de começar a programar, crie o arquivo de memória do projeto. Essa é a prática central da engenharia de contexto — fazer a IA conhecer o histórico do projeto no início de cada conversa.

::: div .code-block
:::inline div .code-head
<span>CLAUDE.md</span><span class="dots">···</span>
:::

```
# Projeto: app de finanças full-stack
## Visão geral
App de finanças pessoais com registros de receitas/despesas, categorias e totais mensais.
## Stack tecnológica
- Frontend: React + TypeScript + Vite
- Backend: Node.js + Express + TypeScript
- Banco de dados: SQLite (via better-sqlite3)
- Definições de tipo compartilhadas entre frontend e backend
## Convenções de API
- Caminho base: /api
- Formato de resposta:{ success: boolean, data: any, error: string }
- Estilo RESTful
## Modelo de dados
Record { id, amount, type, category, note, date }
## Padrões de código
- Modo estrito do TypeScript
- Indentação de 2 espaços
- Funções com comentários JSDoc
- Comentários e mensagens de commit em português
```
:::

##### 3. Implementando passo a passo

Siga o plano de desenvolvimento usando uma conversa independente para cada passo. Abaixo, um exemplo de instrução para o primeiro passo:

::: div .code-block
:::inline div .code-head
<span>Instrução para a IA (Step 1)</span><span class="dots">···</span>
:::

```
Preciso de um esqueleto de API backend.
Requisitos:
1. Servidor Express, porta 3001
2. Banco de dados SQLite, tabela records
3. Campos da tabela records:
   id (TEXT PRIMARY KEY)
   amount (REAL)
   type (TEXT: 'income'|'expense')
   category (TEXT)
   note (TEXT)
   date (TEXT: YYYY-MM-DD)
4. Endpoints CRUD:
   GET /api/records - obter todos os registros
   POST /api/records - adicionar registro
   PUT /api/records/:id - atualizar registro
   DELETE /api/records/:id - excluir registro
5. Middleware de tratamento de erros
Dê a estrutura completa do código backend.
```
:::

Repare nas características dessa instrução: ela descreve apenas o passo atual (o esqueleto do back-end), sem misturar requisitos de front-end; lista explicitamente os campos e os endpoints (dando restrições suficientes à IA), mas deixa a implementação concreta a cargo da IA; e segue o princípio Goal-Driven Execution — dizer 'o que fazer', e não 'como fazer'.

Assim que a IA entregar o código, valide na hora: rode o servidor e teste cada endpoint com curl ou Postman para ver se funciona. Confirmado que está tudo certo, abra uma nova conversa para o Passo 2 (páginas básicas do front-end). Cada passo segue o ciclo 'instrução – validação – nova conversa'.

#### 3. Projeto 3: aplicação turbinada com IA (nível avançado)

##### 1. Concepção do projeto

Objetivo: uma aplicação que consome a API de grandes modelos — por exemplo, um 'assistente de estudos com IA', em que o usuário insere o conteúdo de estudo e a IA gera resumos, conecta tópicos relacionados e recomenda materiais. O diferencial deste projeto: a sua aplicação, ela mesma, chama a IA, e você vai precisar lidar com questões novas como chamadas de API, engenharia de prompt e tratamento de erros.

A lição mais importante deste projeto é: quando você 'usa a IA para escrever o código que chama a IA', precisa dar atenção redobrada à engenharia de prompt. Os prompts que a sua aplicação usa ao chamar a API do grande modelo também devem seguir os princípios discutidos neste guia — clareza, concisão e orientação a objetivos.

##### 2. Pontos técnicos decisivos

Este projeto envolve alguns pontos técnicos que você não encontrou nos dois projetos anteriores:

- Gerenciamento da chave da API: a chave jamais deve ficar escrita no código; gerencie-a com variáveis de ambiente;
- Tratamento de respostas em streaming: as respostas dos grandes modelos normalmente chegam em streaming e precisam ser exibidas em tempo real, trecho a trecho;
- Controle do consumo de Tokens: os grandes modelos cobram por token, então o consumo precisa ser controlado no nível da aplicação;
- Gerenciamento de templates de prompt: funcionalidades diferentes usam templates de prompt diferentes, o que exige uma gestão estruturada.

Todos esses pontos técnicos podem ser implementados com a ajuda da IA, mas você precisa entender o 'porquê' de cada um — por que a chave não pode ficar no código? Por que é preciso streaming? Por que o consumo de tokens precisa ser controlado? Só entendendo o 'porquê' você consegue julgar se a solução proposta pela IA faz sentido.

#### 4. Checklist universal do fluxo prático

Não importa o tamanho do projeto: a seguir está um checklist universal do fluxo prático de programação com IA. Sempre que começar um projeto novo, percorra essa lista para garantir que nenhum passo essencial fique de fora.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Etapa</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">O que fazer</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Princípio correspondente</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1. Pensar nos requisitos</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Percorrer os cinco elementos de requisitos e esclarecer o que será feito</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Think Before Coding</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2. Decompor os requisitos</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Dividir a demanda grande em pequenos passos que possam ser validados de forma independente</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Simplicity First</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3. Escrever o PRD</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Organizar em um documento estruturado para servir de referência</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Goal-Driven</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">4. Configurar o arquivo de memória</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Criar o CLAUDE.md ou arquivo equivalente</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Harness Engineering</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">5. Implementar passo a passo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Uma conversa por passo: instrução – validação – próximo passo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Surgical Changes</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">6. Testar e validar</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Testar a correção da funcionalidade imediatamente após cada passo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Iterate &amp; Verify</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">7. Revisar o código</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Verificar sanidade da arquitetura, segurança e facilidade de manutenção</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Iterate &amp; Verify</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">8. Iterar e otimizar</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Melhorar em iterações conforme os resultados dos testes e da revisão</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Iterate &amp; Verify</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Checklist universal do fluxo prático de programação com IA

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mãos à obra: conclua o 'Projeto 1' nesta semana

{class="mt-1"}
Trate o 'site de ferramentas pessoais' da Seção 1 do Capítulo 44 como a sua primeira tarefa de programação com IA: dedique 5 minutos aos cinco elementos, envie a instrução à IA (qualquer ferramenta serve) e faça a aceitação com as três camadas de verificação. Termine em até 30 minutos — e a sua primeira obra de programação com IA estará pronta. Guarde bem o resultado: é a lembrança da sua passagem de 'leitor' a 'praticante'.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumo do capítulo

- Projeto 1 (iniciante): site de ferramentas só com front-end — vivencie o fluxo completo; dá para terminar em 30 minutos
- Projeto 2 (intermediário): sistema de controle financeiro full stack — PRD + arquivo de memória + implementação em 5 passos, com algo 'que funciona' ao fim de cada um
- Projeto 3 (avançado): assistente de estudos com IA — use a IA para escrever o código que chama a IA, com atenção à engenharia de prompt
- Fluxo universal em oito passos: requisitos → decomposição → PRD → arquivo de memória → implementação passo a passo → testes → revisão → iteração
- Cada passo segue o ciclo 'instrução – validação – nova conversa'
:::
