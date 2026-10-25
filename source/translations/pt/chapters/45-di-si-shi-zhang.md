---
id: di-si-shi-zhang
num: 40
part: ai-biancheng-pian
nav: Capítulo 40: Engenharia de requisitos — transformando ideias em instruções para a IA
toc: default
kind: chapter
---

### Capítulo 40: Engenharia de requisitos — transformar ideias em instruções executáveis pela IA

{class="chapter-intro mb-4"}
Se a engenharia de contexto faz a IA "entender o fundo", a de requisitos faz a IA "saber o que fazer agora". É o elo que mais separa pessoas na programação com IA: com as mesmas ferramentas e modelos, uns criam projetos incríveis e outros só saem com brinquedos medianos. A diferença costuma estar na capacidade de expressar o que se quer, não na técnica.

#### 1. Da ideia vaga à demanda estruturada

Todo projeto começa com uma ideia vaga: "quero um app de finanças", "quero um site pessoal", "quero uma lista de tarefas". Não há problema nisso; o problema é jogar isso direto na IA e depender da sorte. A engenharia de requisitos transforma a ideia vaga em algo estruturado, que a IA executa com precisão.

Boa notícia: não é preciso um PRD de dezenas de páginas. Basta responder cinco perguntas — os "cinco elementos do requisito":

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Elemento</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Pergunta</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Exemplo: app de finanças</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Para quem?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Uso pessoal, registrar receitas e despesas do dia a dia</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">O que fazer?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Um app que registra cada lançamento, resume por mês e visualiza os dados</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Por quê?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Entender a estrutura de gastos e cortar o desnecessário</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Como, mais ou menos?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Front em React, dados no navegador; sem backend e sem login por enquanto</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Quais limites?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Desenvolvimento solo, pronto em 2 semanas, sem necessidade de publicar</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Os cinco elementos e um exemplo

Não precisa virar documento formal — basta passar rapidamente pela cabeça. O importante é o hábito de "pensar antes de falar". Respondendo bem às cinco perguntas, a sua descrição já fica naturalmente estruturada.

#### 2. A arte de decompor requisitos em camadas

Em projetos maiores, uma descrição só não basta. É preciso quebrar o pedido grande em sub-requisitos pequenos, verificáveis de forma independente. O princípio é: cada sub-requisito deve poder ser concluído, validado e entregue sozinho.

No exemplo "fazer um app pessoal de finanças", uma decomposição razoável é:

1. Registro básico de receitas e despesas (adicionar, ver, excluir);
2. Categorias (etiquetar cada lançamento como alimentação, transporte etc.);
3. Resumo mensal (totais por mês);
4. Visualização (gráficos da estrutura de gastos).

Cada etapa é um incremento que roda e pode ser validado isoladamente.

:::inline div .quote-line
A regra de ouro da quebra de requisitos: após cada etapa, o projeto deve continuar sendo uma "coisa que funciona" — mesmo que tosca. Nunca deixe o projeto no estado em que "tudo está pela metade e nada funciona".
:::

Vantagens: você vê progresso o tempo todo — a cada passo, o app ganha uma função; em projetos longos, essa recompensa é essencial. Além disso, cada tarefa fica pequena o suficiente para reduzir desvios de entendimento da IA: quanto menor a tarefa, mais precisa a interpretação e melhor a entrega.

#### 3. Modelo de PRD e prática

Em projetos maiores (aplicação full stack com vários módulos), os cinco elementos podem não bastar. Aí vale escrever um PRD. Um detalhe que costuma confundir: o PRD não é para a IA ler — é para você organizar as ideias e, só então, dar instruções mais precisas.

Um bom PRD não precisa ser longo, mas deve ter seis partes: visão geral (o que fazer em um parágrafo), lista de funcionalidades, solução técnica (stack e arquitetura em linhas gerais), modelo de dados, descrição das telas e plano de desenvolvimento (em quantos passos).

::: div .code-block
:::inline div .code-head
<span>PRD.md</span><span class="dots">···</span>
:::

```
# PRD do app de finanças pessoais
## Visão geral do projeto
Um app leve de finanças pessoais com registro de receitas/despesas, categorias, totais mensais e visualização de dados.
## Lista de recursos
1. Registrar receitas/despesas: valor, tipo (receita/despesa), categoria, observação, data
2. Gerenciamento de categorias: presets de alimentação, transporte, compras, lazer, outros
3. Resumo mensal: receita total, despesa total e saldo por mês
4. Visualização de gastos: gráfico de pizza com a fatia de cada categoria
5. Exportação de dados: exportar como CSV
## Solução técnica
- Frontend: React + TypeScript + Tailwind CSS
- Armazenamento: localStorage (sem backend)
- Gráficos: Chart.js
- Build: Vite
## Modelo de dados
Record {
  id: string
  amount: number
  type: 'income' | 'expense'
  category: string
  note: string
  date: string  // YYYY-MM-DD
}
## Plano de desenvolvimento
Step 1: funções básicas de registro (CRUD)
Step 2: gerenciamento de categorias
Step 3: resumo mensal
Step 4: visualização de dados
Step 5: exportação de dados
```
:::

Observe o estilo: listas curtas e formato estruturado, sem prosa interminável. Cada função com definição clara e o modelo de dados em tipos simples. Assim, você entende — e a IA também interpreta cada ponto com precisão.

#### 4. Na prática: da ideia à solução

Teoria sozinha é chata; vamos percorrer um exemplo completo. Suponha a ideia: "quero um rastreador de estudos que registre o que aprendi todo dia".

Passo 1: os cinco elementos.

- Who: uso pessoal.
- What: registrar o conteúdo diário, acompanhar o tempo de estudo e revisar o progresso.
- Why: criar o hábito de estudar com constância e ver o acúmulo.
- How: começar com uma versão web, dados no navegador.
- Constraint: desenvolvedor iniciante, funções centrais em 1 semana.

Passo 2: decompor.

1. Etapa 1: registrar entradas de estudo (data, conteúdo, duração);
2. Etapa 2: estatísticas de tempo (hoje e acumulado da semana);
3. Etapa 3: visualização em calendário de estudo (como o gráfico de contribuições do GitHub);
4. Etapa 4: revisão (mostrar registros aleatórios de dias passados para reforçar o aprendizado).

Passo 3: PRD curto. A decomposição acima já é o corpo; organize em um .md na raiz do projeto como referência comum para você e a IA.

Passo 4: começar a etapa 1. Uma instrução possível para a IA:

::: div .code-block
:::inline div .code-head
<span>Instrução para a IA</span><span class="dots">···</span>
:::

```
Preciso da primeira função de um rastreador de estudos — registrar itens de estudo.
O usuário pode adicionar um registro com data, conteúdo estudado e duração em minutos.
Os dados ficam no localStorage.
O frontend usa React + TypeScript.
Dê uma implementação completa.
```
:::

Note as características: descreve só o objetivo do passo atual (registro), sem misturar outras funções; deixa as restrições técnicas claras (React, TypeScript, localStorage); dá informação suficiente para "o que" e o "como" em linhas gerais, mas a implementação fica por conta da IA. É uma instrução de qualidade, passada pela engenharia de requisitos.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mão na massa: faça um cartão dos cinco elementos

{class="mt-1"}
Escolha um pequeno projeto antigo e preencha em 5 minutos: Who / What / Why / How / Constraint, uma frase cada. Depois, quebre em 3–5 passos em que "cada etapa já funciona". Verá que a ideia deixa de ser sonho e vira lista de tarefas.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumo do capítulo

- Cinco elementos: Who / What / Why / How / Constraint — pense antes de falar
- Regra de ouro da decomposição: a cada etapa, o projeto continua "usável"
- O PRD é para você: visão, funções, solução técnica, dados, telas, plano
- Boa instrução = só o passo atual + restrições claras + "o que fazer", sem prescrever o "como"
- Modelo completo: cinco elementos → decompor → PRD → instrução, em quatro passos
:::
