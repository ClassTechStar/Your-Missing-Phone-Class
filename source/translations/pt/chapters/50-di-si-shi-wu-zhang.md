---
id: di-si-shi-wu-zhang
num: 45
part: ai-biancheng-pian
nav: Capítulo 45: Garantia de qualidade — tornando o código da IA confiável
toc: default
kind: chapter
---

### Capítulo 45: Garantia de qualidade — deixando confiável o código escrito pela IA

{class="chapter-intro mb-4"}
O código escrito pela IA tem uma característica: geralmente 'parece muito correto' — nomes de variáveis padronizados, comentários completos, lógica clara. Mas 'parecer correto' não é o mesmo que 'estar correto'. Os problemas escondidos no código da IA costumam ser mais difíceis de detectar do que no código escrito à mão, porque a qualidade de superfície é tão alta que relaxa a vigilância. Este capítulo ensina a montar um sistema eficaz de garantia de qualidade para o código da IA — com três linhas de defesa (testes, revisão e controle de versão) para transformar 'parecer correto' em 'estar correto'.

#### 1. Guiar pelos testes: peça que a IA escreva os testes

Os testes são a primeira linha de defesa da qualidade na programação com IA. A boa notícia: pedir que a IA escreva testes é mais fácil e mais confiável do que pedir que ela escreva o código funcional — porque o comportamento esperado dos testes é claro e é menos provável surgir código que 'parece certo mas não é'.

O fluxo da programação com IA orientada a testes é: primeiro deixe a IA escrever o código da funcionalidade; depois de validar que o básico passou, peça imediatamente que ela escreva os casos de teste. Os casos de teste devem cobrir o caminho normal, os casos-limite e as situações de exceção. Depois, deixe a IA corrigir o código funcional conforme o retorno dos testes. A vantagem desse fluxo: uma vez prontos, os testes viram uma ferramenta de verificação contínua — qualquer mudança futura pode ser conferida rodando os testes, para garantir que nenhuma regressão foi introduzida.

::: div .code-block
:::inline div .code-head
<span>Instrução para a IA: escreva testes</span><span class="dots">···</span>
:::

```
Escreva testes unitários para a função calculate_discount.
Os casos de teste devem cobrir:
1. Caminho normal:
   - item de 100 yuan com 20% de desconto -> 80
   - item de 200 yuan com 50% de desconto -> 100
2. Casos limite:
   - item de 0 yuan com 20% de desconto -> 0
   - item de 100 yuan com 0% de desconto -> 100 (sem desconto)
   - item de 100 yuan com 10% de desconto -> 100 (preço cheio)
3. Casos de erro:
   - preço negativo -> deve lançar erro
   - desconto > 1 -> deve lançar erro
   - entrada não numérica -> deve lançar erro
Use o framework Vitest e dê o arquivo de testes completo.
```
:::

Repare nas características dessa instrução: ela lista explicitamente as três classes de casos de teste (normal, limite e exceção), sem deixar espaço para a IA fazer 'testes seletivos' à vontade. Às vezes, a IA escreve só testes do caminho normal para 'entregar rápido'; listar todas as classes evita esse problema.

#### 2. Técnicas de revisão de código

Mesmo com cobertura de testes, você ainda precisa revisar manualmente o código produzido pela IA. Revisar não é ler linha por linha — isso consome tempo demais e depende demais do seu nível de programação. Uma revisão eficaz do código da IA deve se atentar aos seguintes pontos-chave:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Dimensão da revisão</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">O que observar</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Problemas comuns</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Segurança</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Validação de entradas, tratamento de chaves, proteção contra injeção de SQL</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">A IA costuma esquecer de validar entradas e deixar chaves escritas direto no código</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tratamento de erros</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Se as exceções são capturadas e se as mensagens de erro fazem sentido</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">A IA adora usar blocos catch vazios ou apenas console.log</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Desempenho</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Se há problemas de desempenho evidentes, como consultas N+1 e loops infinitos</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Às vezes a IA escreve algoritmos O(n²)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Manutenibilidade</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Se a estrutura do código está clara e os nomes fazem sentido</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">De vez em quando a IA gera código abstrato demais</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gerenciamento de dependências</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Se as dependências introduzidas são necessárias e as versões estão explícitas</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">A IA tende a introduzir bibliotecas desnecessárias</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Dimensões-chave para revisar código de IA

Na revisão, você não precisa verificar tudo sozinho — pode pedir à IA para fazer a primeira rodada. Uma instrução como: "Revise a segurança, o tratamento de erros e o desempenho deste código e aponte os problemas em potencial." A capacidade de autorrevisão da IA melhora sem parar; embora não substitua totalmente a revisão humana, ela ajuda a filtrar a maior parte dos problemas evidentes.

#### 3. Controle de versão: o papel do Git na programação com IA

O papel do Git na programação com IA é ainda mais importante do que na programação tradicional. Como cada modificação da IA pode introduzir mudanças imprevisíveis, você precisa de um "remédio para o arrependimento" confiável — e o controle de versão é exatamente esse remédio.

A melhor prática do Git na programação com IA é "commitar com frequência e avançar em passos curtos". A cada ponto de funcionalidade verificável concluído, faça um commit. Assim, quando alguma modificação da IA der problema, você pode voltar com precisão ao último estado funcional, sem precisar jogar fora todo o trabalho.

Outra técnica útil é o "isolamento por branch". Para modificações da IA com resultado incerto (como uma refatoração grande), crie antes um branch novo e faça o trabalho nele. Se o resultado agradar, faça o merge de volta ao branch principal; se não, basta apagar o branch, sem afetar o principal. Isso é muito mais seguro do que ficar mexendo no branch principal repetidamente.

1. Antes de cada modificação da IA, garanta que o diretório de trabalho está limpo (sem alterações não commitadas). Assim, se você não gostar do que a IA fez, pode reverter rapidinho com git checkout .
2. Depois de cada modificação da IA, assim que a validação passar, faça o commit imediatamente. A mensagem do commit descreve o que aquela alteração fez, por exemplo "feat: adiciona cadastro de usuário".
3. Para refatorações grandes, crie primeiro um branch: git checkout -b refactor/auth-system. Faça as alterações no branch e só faça o merge depois de os testes passarem.
4. Crie o hábito de olhar o diff. Depois de cada modificação da IA, use git diff para ver exatamente o que mudou. Isso não só ajuda a encontrar problemas, como também ajuda você a aprender com o código.

#### 4. Armadilhas comuns e como escapar delas

Na programação com IA, há algumas armadilhas que se repetem e nas quais quase todo iniciante acaba caindo. Conhecê-las com antecedência economiza muita volta desnecessária.

##### 1. Armadilha 1: a armadilha da confiança

"O código escrito pela IA parece bem profissional, com certeza não tem problema, né?" — Essa é a armadilha mais perigosa de todas. O código gerado pela IA é muito caprichado na superfície — nomes padronizados, comentários completos, estrutura clara — e essa "aparência de profissionalismo" faz a gente baixar a guarda. Mas capricho superficial não significa lógica correta. O antídoto: valide sempre por meio de testes, nunca julgando pela "aparência".

##### 2. Armadilha 2: a armadilha do inchaço

"Já que a IA escreve código por mim, que tal caprichar e deixar os recursos bem completos?" — É assim que o código incha. A IA é mestre em "dar a mais": você pede uma tela de login e ela entrega um sistema completo de gerenciamento de usuários. Recurso supérfluo não só aumenta a complexidade, como também aumenta a chance de bugs. O antídoto: siga com rigor o princípio Simplicity First e diga com clareza à IA "faça apenas este recurso, não acrescente nada além".

##### 3. Armadilha 3: a armadilha da compreensão

"A IA deve ter entendido o que eu quis dizer, né?" — Não necessariamente. Por mais forte que seja a compreensão da IA, diante de pedidos vagos ela ainda "chuta". Quando o chute sai errado, o código gerado sai errado. E o pior: o código nascido de um chute errado costuma "parecer bastante razoável", fazendo você acreditar que ela entendeu. O antídoto: coloque detalhes concretos suficientes na instrução para reduzir o espaço que a IA precisa "chutar".

##### 4. Armadilha 4: a armadilha do contexto

"Eu já falei isso na conversa anterior, a IA deve lembrar, né?" — Provavelmente não. Conforme a conversa cresce ou uma nova sessão é aberta, a IA perde o contexto inicial. Se uma restrição importante não foi registrada no arquivo de memória do projeto, é bem provável que ela seja ignorada nas alterações seguintes. O antídoto: registre as restrições importantes no arquivo de memória do projeto; não dependa da memória da conversa.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Guia rápido das quatro armadilhas

{class="mt-1"}
Armadilha da confiança — não confie no "parece certo"; armadilha do inchaço — a IA adora "dar a mais"; armadilha da compreensão — com pedido vago, ela "chuta"; armadilha do contexto — a memória da conversa "esquece". Os antídotos correspondentes são: validar com testes, cortar o excesso, dar detalhes suficientes e registrar no arquivo de memória.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mão na massa: monte três linhas de defesa no seu projeto

{class="mt-1"}
Se você já começou o Projeto 1 (site de ferramentas): 1) peça à IA que escreva 3 tipos de casos de teste para as funções centrais; 2) revise o código nos cinco critérios (segurança/tratamento de erros/desempenho/manutenibilidade/dependências); 3) inicialize o projeto com git e faça o primeiro commit. Com as três linhas de defesa de pé, o projeto passa a ser realmente seu.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumo do capítulo

- Código de IA: "parece certo" ≠ "é certo" — qualidade superficial alta demais faz você baixar a guarda
- Peça testes à IA: liste explicitamente os três tipos de casos (normais/limítrofes/excepcionais) para evitar "testes seletivos"
- Cinco critérios de revisão: segurança, tratamento de erros, desempenho, manutenibilidade e gerenciamento de dependências
- Git é o "remédio para o arrependimento": commits frequentes, passos curtos, isolamento por branch e olhar o diff sempre
- Quatro armadilhas: confiança (valide com testes), inchaço (corte o excesso), compreensão (dê detalhes suficientes) e contexto (registre no arquivo de memória)
:::
