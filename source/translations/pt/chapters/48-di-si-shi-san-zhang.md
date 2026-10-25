---
id: di-si-shi-san-zhang
num: 43
part: ai-biancheng-pian
nav: Capítulo 43: Engenharia de diálogo — técnicas para conversas eficientes
toc: default
kind: chapter
---

### Capítulo 43: Engenharia de diálogo — técnicas de conversa para colaborar com a IA com eficiência

{class="chapter-intro mb-4"}
O diálogo é a forma central de interação na programação com IA. Mas atenção: 'diálogo' não é a mesma coisa que 'conversa fiada' — um diálogo eficiente de programação com IA é uma técnica de comunicação estruturada, que chamamos de 'engenharia de diálogo'. Ela estuda como obter o código de maior qualidade com o menor número possível de rodadas de conversa. Simplificando, este capítulo ensina como deixar as coisas claras ao conversar com a IA.

#### 1. Estratégia de camadas de Prompt

O diálogo com a IA pode ser dividido em três camadas, e cada uma tem uma função diferente. Ao entender essas três camadas, você combina Prompts eficientes como quem empilha blocos de montar.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Camada</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Função</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Exemplo</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Frequência</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Camada de sistema</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Define o papel da IA e as restrições globais</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">'Você é um especialista em React e o código deve ser em TypeScript'</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Configurada uma vez no início do projeto</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Camada de tarefa</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Descreve a tarefa específica a fazer agora</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">'Implemente um componente de formulário com campos de nome de usuário e senha'</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Enviada no início de cada tarefa</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Camada de feedback</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Avalia e corrige o que a IA produziu</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">'O campo de senha está sem alternar mostrar/ocultar; adicione, por favor'</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Enviada conforme a qualidade do resultado</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
As três camadas do Prompt de diálogo

O Prompt da camada de sistema geralmente fica no arquivo de memória do projeto (como o CLAUDE.md) e não precisa ser repetido a cada conversa. A camada de tarefa é a que você mais usa na conversa — ela deve conter três elementos: 'o que fazer', 'com qual tecnologia' e 'quais restrições'. A camada de feedback é a que mais exige habilidade — um bom feedback permite que a IA corrija com precisão; um feedback ruim só a faz ficar chutando de novo.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Dica: os três golpes do feedback

{class="mt-1"}
Um modelo prático de feedback é 'apontar o problema + explicar o esperado + fornecer contexto'. Por exemplo: 'o tratamento de erros da linha 25 usa apenas console.log (aponta o problema), em produção deveria usar um handler de erros unificado e devolver mensagens amigáveis ao usuário (explica o esperado), e o projeto já tem uma função handleError que pode ser usada (fornece o contexto)'. Esse tipo de feedback é dez vezes mais eficaz do que 'melhora o tratamento de erros'.
:::

#### 2. Diálogo de depuração: como descrever erros para a IA localizar rápido

A depuração é um dos cenários mais frequentes na programação com IA. Quando você encontra um bug, o jeito de descrever o problema à IA determina diretamente se ela vai conseguir localizar e corrigir rápido. A seguir, os quatro pontos-chave do diálogo de depuração:

1. Mostre à IA a informação original, e não o seu relato. Mencione diretamente com @ o log de erros, a pilha de exceções e o código relevante, em vez de descrever com um 'parece que deu algum erro'. Para a IA, ver a informação original é mais preciso do que ver a sua interpretação.
2. Descreva a diferença entre o 'comportamento esperado' e o 'comportamento real'. 'Eu esperava que, ao clicar no botão, fosse para a página inicial (esperado), mas, na verdade, nada acontece ao clicar (real)' — esse tipo de descrição é muito mais útil do que 'o botão está quebrado'.
3. Forneça os passos para reproduzir. 'Primeiro digito o nome de usuário, depois clico no botão de entrar, e o erro aparece' — os passos de reprodução permitem que a IA simule o seu caminho de operação e localize o problema mais facilmente.
4. Diga claramente o que você já tentou. 'Já verifiquei a requisição de rede: retorna 200 e os dados estão normais' — isso ajuda a IA a descartar caminhos já verificados e a não perder tempo repetindo verificações.

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
Descrição de depuração ruim

{class="font-mono text-xs leading-relaxed"}
O botão não responde ao clique, dá uma olhada aí
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
Descrição de depuração boa

{class="font-mono text-xs leading-relaxed"}
Após clicar no botão Entrar, a página não reage. Comportamento esperado: após o clique, ir para a página /home Comportamento real: nada acontece ao clicar e não há erros no console Passos para reproduzir: 1. Na página de login, digitar o usuário admin e a senha 123456 2. Clicar no botão 'Entrar' 3. A página não reage Já verificado: - Requisição de rede normal, retorna 200 - Evento onClick já vinculado - Código do componente LoginButton revisado Arquivos relacionados: @src/components/LoginButton.tsx @src/pages/Login.tsx
:::
:::

#### 3. Estratégias de iteração: passos pequenos e rápidos vs. refatoração em grandes passos

A iteração na programação com IA tem duas estratégias básicas, para cenários diferentes. Entender a diferença entre elas ajuda você a escolher corretamente em cada situação.

A estratégia de 'passos pequenos e rápidos' serve para o desenvolvimento de funcionalidades e a correção de bugs. A essência: a cada vez, peça à IA apenas uma pequena alteração e só passe para a próxima depois de validar. Vantagens: cada passo é verificável e reversível, com risco controlado; desvantagens: é mais lento e exige interações frequentes de conversa. Ideal para: desenvolvimento de novas funcionalidades, exploração quando você não tem certeza da melhor solução e iteração cautelosa quando não confia muito no resultado da IA.

A estratégia de 'refatoração em grandes passos' serve para modificações em larga escala quando o objetivo está claro. A essência: descreva o objetivo completo de uma vez e deixe a IA planejar e executar toda a mudança de forma autônoma. Vantagens: é rápido e a IA enxerga o quadro geral, tomando decisões de arquitetura melhores; desvantagens: o risco é alto e, se a IA entender errado, corrigir custa caro. Ideal para: upgrades de arquitetura bem definidos, migrações de código em grande escala e refatorações com cobertura de testes sólida.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Dimensão</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Passos pequenos e rápidos</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Refatoração em grandes passos</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Volume por alteração</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Um ponto de funcionalidade ou um bug</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Um módulo ou uma camada de arquitetura</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Frequência de validação</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Valida imediatamente após cada alteração</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Valida tudo junto, após concluir todas as alterações</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Rodadas de conversa</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Muitas (5 a 10 por funcionalidade)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Poucas (1 a 3 por módulo)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Risco</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Baixo; cada passo é reversível</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Alto; corrigir desvios custa caro</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cenários adequados</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Novas funcionalidades, desenvolvimento exploratório</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Refatorações e migrações com objetivo claro</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pré-requisitos</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Nenhum requisito especial</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Precisa de cobertura de testes</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Comparação entre as duas estratégias de iteração

Na prática, as duas estratégias costumam ser combinadas. Por exemplo, ao refatorar um módulo, primeiro use a 'refatoração em grandes passos' para a IA apresentar o plano geral; depois de revisar o plano, execute aos poucos com 'passos pequenos e rápidos'. Assim você mantém a visão global e controla o risco de execução.

#### 4. Gerenciamento de contexto em conversas de múltiplas rodadas

Conforme o número de rodadas aumenta, você precisa gerenciar ativamente o contexto da conversa para evitar o problema de 'a IA esqueceu as informações do início'. A seguir, algumas técnicas práticas de gerenciamento de contexto.

Primeiro, 'ancore' as informações-chave. No início da conversa, deixe as restrições importantes claras por escrito e reafirme-as nos momentos certos ao longo do diálogo. Por exemplo: 'lembre-se: nossos dados ficam no localStorage, não podemos usar banco de dados' — reitere essa restrição nas solicitações de alteração relacionadas, para evitar que a IA esqueça.

Segundo, use bem a técnica de 'resumir e continuar'. Quando a conversa ficar muito longa, peça à IA que 'resuma o progresso atual e as pendências' e então abra uma nova conversa tomando esse resumo como ponto de partida. Assim você preserva o contexto essencial e evita a degradação das conversas longas.

Terceiro, 'uma conversa, uma tarefa'. Essa é a estratégia de gerenciamento de contexto mais simples e mais eficaz. Cada conversa trata apenas de uma tarefa ou de um ponto de funcionalidade; ao concluir, abra uma nova conversa para o próximo. Isso limita naturalmente o comprimento da conversa e mantém o contexto claro.

Quarto, aproveite os recursos de gerenciamento de contexto das ferramentas. A maioria das ferramentas de programação com IA tem botões de 'limpar contexto' ou 'nova sessão' — quando sentir que a qualidade das respostas da IA piorou, não hesite: abra uma nova sessão. Perder parte do histórico da conversa é muito melhor do que continuar sofrendo com um contexto degradado.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mãos à obra: seja o 'paciente' da sua IA uma vez

{class="mt-1"}
Monte de propósito uma pequena página no navegador com um bug (por exemplo, um botão que não reage). Depois, descreva tudo à IA uma vez, seguindo o formato de 'boa descrição de depuração' deste capítulo: informação original, esperado vs. real, passos de reprodução e o que já foi verificado. Sinta a diferença na velocidade com que a IA localiza o problema — você vai entender por que 'saber descrever o problema' é, em si, uma habilidade.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumo do capítulo

- Três camadas do Prompt: sistema (vai no arquivo de memória), tarefa (o que fazer + tecnologia + restrições) e feedback (problema + esperado + contexto)
- Quatro pontos da depuração: mostrar a informação original, esperado vs. real, passos de reprodução e o que já foi verificado
- Passos pequenos e rápidos: risco baixo e muitas rodadas, ideal para novas funcionalidades; refatoração em grandes passos: risco alto e poucas rodadas, exige cobertura de testes
- Quatro truques de contexto: ancorar as informações-chave, resumir e continuar, uma conversa por tarefa e abrir uma nova sessão sem hesitar
:::
