---
id: di-san-shi-ba-zhang
num: 38
part: ai-biancheng-pian
nav: Capítulo 38: Os cinco princípios de pensamento da programação com IA
toc: default
kind: chapter
---

### Capítulo 38: As cinco grandes regras de pensamento da programação com IA

{class="chapter-intro mb-4"}
Se deste livro você só puder guardar um capítulo, que seja este. As cinco regras são o coração da obra; tudo o que vem depois — contexto, requisitos, prompt, qualidade — é a aplicação delas em cada cenário. Fique tranquilo: nenhuma é difícil, mas todas merecem ser "internalizadas" com alguns projetos.

A história começa de um jeito curioso: ao abrir o projeto, Andrej Karpathy anexou um CLAUDE.md de só 70 linhas com quatro princípios de colaboração com IA. O arquivo recebeu mais de 70.000 Stars no GitHub e virou a referência mais citada entre quem programa com IA. Não são slogans vazios: são hábitos mentais práticos, destilados da prática. Este livro acrescenta o quinto — iteração e verificação — completando as cinco regras.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Por que 70 linhas valem tanto?

{class="mt-1"}
70.000 Stars? A maioria dos projetos no GitHub nunca chega perto disso. Que um arquivo de 70 linhas alcance esse número prova uma coisa: na era da IA, o mais raro não é código — é a capacidade de "pensar com clareza". Essas 70 linhas são a versão concentrada desse pensamento.
:::

#### 1. Regra 1: Think Before Coding (pense antes de codar)

É a regra mais contra-intuitiva das cinco. Se a IA escreve o código, por que "pensar antes"? Resposta simples: a qualidade da saída é proporcional à da entrada. Se você mesmo não sabe o que quer, a IA só te leva a um ciclo infinito de "muda e muda de novo" — o famoso "a IA se perde junto com você".

"Pensar antes" significa responder três perguntas antes de dar a instrução; juntas, formam o "triângulo do pensamento":

1. Qual problema quero resolver? (objetivo)
2. Como deve ser o resultado esperado? (critério de aceite)
3. Quais restrições preciso respeitar? (limites)

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Dimensão</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Entrada vaga (ruim)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Entrada clara (boa)</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Definição do problema</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Faz um site pra mim</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Faz uma página de ferramentas pessoais com cartões de entrada para 3 miniapps de IA</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Resultado esperado</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Que fique bonito</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Layout responsivo, tema escuro, animação ao passar o mouse, funciona no celular</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Restrições</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">(não dito)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sem frameworks, HTML+CSS+JS puro, deploy em arquivo único, sem backend</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Comparação entre entrada vaga e clara para o mesmo pedido

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Atenção: pensar antes ≠ escrever um documento perfeito

{class="mt-1"}
"Pensar antes" não é "fazer um PRD perfeito e só então começar". É um processo rápido e organizado: 30 segundos para clarear as três perguntas valem mais do que 30 minutos de vaivém no chat. Em tarefas pequenas, as respostas podem ser curtas; em projetos grandes, viram um documento de requisitos completo (Capítulo 40).
:::

#### 2. Regra 2: Simplicity First (simplicidade em primeiro lugar)

A maior armadilha da programação com IA não é "não conseguir fazer", e sim "fazer demais". Se você pede "um sistema de usuários", a IA pode gerar autenticação, permissões, papéis, logs de auditoria, exportação… quando você só queria uma tela de login. Excesso de geração é a principal causa de código inchado.

"Simplicidade em primeiro lugar" é aplicar o princípio do "mínimo viável" a cada instrução: menos código para a função central, a solução mais simples para o problema, o mínimo de recursos para validar a ideia. Karpathy tem uma comparação precisa: "para calcular um preço com desconto, você não precisa de um motor de e-commerce."

Na prática, significa alguns hábitos:

- Peça à IA uma função de cada vez, não o sistema inteiro de uma vez;
- Prefira a biblioteca padrão e soluções simples a dependências complexas;
- Se cabe em 50 linhas, não deixe a IA escrever 500;
- Se a entrega passou do escopo, mande cortar o excesso sem medo.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Cenário</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Solução exagerada (evite)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Solução simples (recomendada)</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Armazenar dados</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Montar MySQL + ORM</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Começar com arquivo JSON ou SQLite</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Login de usuário</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OAuth2.0 + JWT + papéis e permissões</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Começar com validação simples de senha</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Framework de front-end</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">React + Redux + Router</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Testar HTML + JavaScript puro</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Publicar online</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Docker + CI/CD + K8s</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Fazer rodar local primeiro</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Soluções exageradas vs. simples em cenários comuns

#### 3. Regra 3: Surgical Changes (modificações cirúrgicas)

Ao iterar um projeto existente, cada mudança deve ser cirúrgica: mexa só onde precisa. Em programação com IA, isso é crucial — a IA adora "aproveitar e melhorar mais um pouco": você pede para corrigir um bug e ela refaz metade do arquivo.

O coração da regra: toda instrução deve fixar o escopo e os limites da mudança. Diga "modifique só a função calculate_discount", "não mexa no resto", "mantenha o estilo atual". Se a IA ultrapassar o pedido, mande reverter o excesso na hora.

Karpathy ilustra com um exemplo de diff: pedir à IA para adicionar "preço de membro" à função de desconto do carrinho. A boa entrega altera só essa função e acrescenta poucas linhas; a má entrega refaz o arquivo inteiro — o código novo pode até parecer "mais elegante", mas você não sabe se introduziu bugs. Em programação com IA, "parecer melhor" nunca é motivo para sair do pedido.

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
Instrução ruim (escopo vago)

{class="font-mono text-xs leading-relaxed"}
Otimiza a lógica de desconto deste projeto
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
Instrução boa (escopo preciso)

{class="font-mono text-xs leading-relaxed"}
Modifique apenas a função calculate_discount em cart.py: | 1. Adicione lógica de preço de membro sobre o desconto atual | 2. Membros ganham 10% extras | 3. Não altere a assinatura da função nem outras funções | 4. Mantenha o estilo atual de nomes de variáveis
:::
:::

#### 4. Regra 4: Goal-Driven Execution (execução orientada a objetivo)

Esta regra responde a uma pergunta-chave: instruir a IA sobre "como fazer" ou sobre "o que fazer"? Karpathy prefere a segunda. Em vez de "crie uma classe, depois adicione métodos, depois escreva testes", diga "preciso de uma ferramenta que leia um CSV e conte os valores únicos de cada coluna". A IA escolhe o caminho; você valida o resultado.

Os benefícios são duplos. Para a IA, há mais autonomia para escolher a melhor implementação em vez de seguir seus passos intermediários; para você, a atenção sai do "como" e vai para o "está certo?" — exatamente o papel de um Conductor.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Atenção: orientado a objetivo ≠ deixar solto

{class="mt-1"}
Depois da execução, você valida com rigor: o resultado atende ao pedido? Casos de borda foram tratados? Há overdesign óbvio? Se algo saiu errado, dê feedback concreto — não "refaça", e sim "com lista vazia o código lança IndexError; adicione verificação de nulo".
:::

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Estilo de instrução</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Exemplo</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Característica do resultado</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Imperativo (como fazer)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"Crie uma classe Python chamada DataParser, adicione um método parse que receba filename e use o módulo csv…"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">A IA vira digitadora; seus passos intermediários podem não ser o caminho ótimo</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Por objetivo (o que fazer)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"Preciso de uma ferramenta: ler CSV, contar valores únicos por coluna e sair em JSON. Entregue a implementação completa."</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">A IA escolhe a melhor rota; você valida o resultado</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Comparação entre instrução imperativa e orientada a objetivo

#### 5. Regra 5: Iterate and Verify (iterar e verificar)

É a quinta regra que este livro acrescenta às quatro de Karpathy. A crença central: a primeira entrega da IA quase nunca é a versão final. Programação eficaz com IA é um ciclo "gerar–verificar–corrigir", não um único "pedir–receber".

"Iterar e verificar" não é um "está errado, tenta de novo" passivo; é um fluxo estruturado. A cada entrega, valide em três camadas:

- 1ª · Funcional: roda? Entradas e saídas estão corretas?
- 2ª · Borda: e com entrada vazia, gigante ou inválida?
- 3ª · Arquitetura: a estrutura faz sentido? Há hardcoded? Dá para evoluir?

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-bullseye mr-1"></i> Definir a meta</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-robot mr-1"></i> A IA gera código</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> Verificação funcional</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> Aprovado</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> Verificação de casos limite</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> Aprovado</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-landmark mr-1"></i> Revisão da arquitetura</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> Aprovado — vai para a próxima etapa</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-times-circle mr-1"></i> Reprovado</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> Dar feedback específico</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> Regenerar</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figura 2: ciclo de iteração e verificação na programação com IA
:::

O ponto crucial é o "feedback específico". Em vez de "está errado, refaça", diga "com lista vazia a função lança IndexError; adicione verificação na linha 15". Feedback preciso permite correção cirúrgica; feedback vago só faz a IA adivinhar de novo.

#### 6. Harness Engineering: Agente = Modelo + Harness

Por volta de meados de 2026, o conceito Harness Engineering começou a popularizar-se na comunidade. A fórmula é simples:

:::inline div .quote-line .text-center .text-base .font-bold
<strong>A capacidade de um agent = capacidade do modelo × qualidade do harness</strong>
:::

A capacidade do modelo é o teto intelectual da IA; o Harness é o "ambiente de trabalho" em volta do modelo — gestão de contexto, integração de ferramentas, orquestração de fluxo, sistema de memória etc.

Isso explica uma dúvida comum: por que, com o mesmo GPT-4 ou Claude, uns fazem projetos incríveis e outros saem com código medíocre? A diferença não está no modelo, e sim no Harness. Um bom Harness tem: especificação clara do projeto, ferramentas bem integradas, contexto organizado e fluxo de verificação sólido. O modelo define o teto; o Harness define quanto dele você alcança.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
A metáfora do estagiário genial

{class="mt-1"}
Imagine o modelo como um estagiário genial: altíssimo QI, mas sem documento de contexto, sem ferramentas, sem prazo e sem critérios de aceite, não entrega nada de bom. Harness Engineering é a engenharia de "como montar o ambiente de trabalho do estagiário genial".
:::

Os próximos capítulos ensinam a construir esse Harness: Capítulo 39, contexto (memória do projeto); 40, requisitos (PRD); 43, prompt em camadas; 45, garantia de qualidade (verificação). Juntos, formam o seu Harness.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mão na massa: use o "triângulo do pensamento" na sua próxima ideia

{class="mt-1"}
Escolha um projetinho que você adia há tempo (uma página de contagem regressiva, um script de lembrete de beber água). Em 3 minutos responda: ① que problema resolve? ② como fica pronto? ③ quais restrições (tempo, tecnologia, ambiente)? Escreva as respostas em um parágrafo. Parabéns: você acabou de fazer o seu primeiro "Think Before Coding" — e esse parágrafo já é uma instrução de qualidade.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumo do capítulo

- As cinco regras vêm do CLAUDE.md de 70 linhas de Karpathy (70 mil Stars); este livro acrescenta a quinta: "iterar e verificar"
- Think Before Coding: responda três perguntas — o que fazer? como fica o resultado? quais limites?
- Simplicity First: a maior armadilha é "fazer demais" — para calcular desconto não se precisa de um e-commerce
- Surgical Changes: mudanças cirúrgicas, sem o "aproveitar e melhorar" da IA
- Goal-Driven Execution: diga o que fazer, não como fazer — deixe a IA escolher o caminho
- Iterate and Verify: três camadas (funcional/borda/arquitetura) + feedback concreto, em ciclo
- Harness Engineering: capacidade = modelo × Harness; trate a IA como "estagiário genial" e monte o ambiente
:::
