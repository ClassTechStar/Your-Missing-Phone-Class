---
id: di-wu-shi-liu-zhang
num: 56
part: an-zhuo-kai-fa-pian
nav: Capítulo 56: Refinamento e publicação — colocando o app no Google Play
toc: default
kind: chapter
---

### Capítulo 56: Polimento e publicação — testes, depuração e publicação na Google Play

{class="chapter-intro mb-4"}
O App ficou pronto, e agora? Este capítulo responde a três coisas que levam do 'funciona' ao 'pronto para entregar': como depurar com eficiência para achar bugs, como escrever testes para evitar regressões e como colocar o App na Google Play para o mundo inteiro baixar. Publicar não é só cerimônia — é a linha divisória entre obra e produto.

#### 1. O trio da depuração: Logcat, breakpoints e inspetor de UI

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ferramenta</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Para que serve</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Como usar</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Logcat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ver os logs do sistema e os seus próprios</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">No código, Log.d("TAG","valor=$x"); no painel, busque o TAG para filtrar</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Depuração com breakpoints</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Fazer o programa parar numa linha e ver os valores das variáveis</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Clique ao lado do número da linha para surgir o ponto vermelho, execute em modo Debug e avance passo a passo</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Layout Inspector</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ver a estrutura da interface em execução</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menu Tools → Layout Inspector, para ver a árvore de componentes em tempo real</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
O trio da depuração

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Dica: como ler uma mensagem de erro?

{class="mt-1"}
Depois de uma queda, o Logcat mostra uma pilha vermelha (Stacktrace); de baixo para cima, procure a primeira linha que começa com o nome do seu próprio pacote (por exemplo, com.example.yourapp) — essa linha é praticamente a cena do crime. Primeiro veja o 'tipo da Exception' (ponteiro nulo? conversão de tipo?), depois o 'at ... seuArquivo:linha'. Esse truque resolve 80% das quedas.
:::

#### 2. Testes: um seguro para o código

Teste manual não é confiável — você mexe numa função e outra quebra por baixo. Testes são o 'remédio do arrependimento' e o 'colete à prova de balas'. Os testes Android têm três camadas; como iniciante, domine primeiro a primeira:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Camada</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">O que testa</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Onde fica</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Velocidade</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Testes de unidade</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lógica pura (cálculos, validações)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">app/src/test/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Segundos</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Testes instrumentados</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Comportamento da interface em aparelho real</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">app/src/androidTest/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Minutos</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Teste manual</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">A percepção e a experiência de uma pessoa real</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">——</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sempre necessário</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
As três camadas de teste

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Exemplo de teste unitário</span><span class="dots">···</span>
:::

```
// Extraia lógica como "string de valor para número" numa função pura
fun parseAmount(input: String): Double? {
    val v = input.trim().toDoubleOrNull()
    return if (v != null && v > 0) v else null
}

// Testando (JUnit4)
@Test
fun emptyInputReturnsNull() {
    assertEquals(null, parseAmount(""))
}
@Test
fun negativeReturnsNull() {
    assertEquals(null, parseAmount("-5"))
}
@Test
fun normalValueParses() {
    assertEquals(12.5, parseAmount("12.5"))
}
```
:::

A validação de valores e os cálculos de estatística do controle de gastos merecem testes de unidade por cima. Para rodar: clique com o botão direito na pasta test → Run. Tudo verde, pode alterar o código tranquilo.

#### 3. Assinatura e empacotamento: carimbando o App

O Android exige que todo pacote de instalação seja assinado — como um carimbo oficial que prova 'este pacote saiu de mim e não foi adulterado'. Na depuração, o Android Studio usa a assinatura debug automaticamente; para publicar, use a sua própria assinatura release. O fluxo:

1. Menu Build → Generate Signed Bundle / APK;
2. Crie o arquivo keystore (cofre de chaves) — defina a senha e guarde-a com cuidado;
3. Escolha release + formato AAB e a compilação está pronta.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Alerta de armadilha: perder o keystore = perder o App

{class="mt-1"}
Depois de publicar, toda atualização do App precisa da mesma assinatura, senão a loja recusa. Se o arquivo keystore e a senha se perderem, restará criar um app novo e publicar de novo — e os usuários antigos ficam todos sem atualização. Faça backup do keystore e da senha em local seguro (nuvem criptografada + caderno de anotações); é uma das lições mais caras de um desenvolvedor Android.
:::

#### 4. O processo completo de publicação na Google Play

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> Registrar conta de desenvolvedor</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-invoice mr-1"></i> Preparar materiais da loja</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-box mr-1"></i> Enviar o AAB</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-clipboard-list mr-1"></i> Preencher o formulário de segurança de dados</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> Revisão (de horas a dias)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-party-horn mr-1"></i> Publicado</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figura 6: Os seis passos para publicar na Google Play
:::

- Cadastro: taxa única de 25 dólares; é preciso ter uma conta Google utilizável;
- Materiais: ícone do app (512×512), capturas de tela (no mínimo 2), descrição das funções e link da política de privacidade (obrigatório se coleta dados);
- Formulário de segurança de dados: declare com sinceridade quais dados são coletados — um controle de gastos sem internet pode declarar 'zero coleta';
- Revisão: na primeira publicação, contas novas costumam passar por revisão humana, que leva de horas a dias; se devolverem, corrija conforme as observações.

Atenção para quem está na China: a Google Play exige um ambiente de rede especial, e a distribuição na China continental costuma ser feita pelas lojas locais (Huawei, Xiaomi, Yingyongbao etc.). O processo nessas lojas é parecido, mas cada uma tem o seu próprio gosto na revisão — o mesmo AAB/APK pode ser distribuído em várias. Para fins de estudo, conseguir passar em uma já é vitória.

#### 5. Como fazer os materiais da loja: a primeira impressão vale downloads

A página da loja é a vitrine que o usuário vê ao 'dar uma volta na loja'. Três materiais definem a primeira impressão:

- Ícone: 512×512; não use uma captura de tela improvisada. Se você não tem jeito para design, gere uma forma geométrica simples com ferramentas de IA; só passa se continuar reconhecível de relance quando reduzida na tela inicial do celular;
- Capturas: no mínimo 2, de preferência 4 a 6, mostrando os cenários centrais do app; cada uma com uma frase em linguagem de gente ('Registre um gasto em um segundo' vale dez vezes mais que 'Solução eficiente de gestão financeira');
- Descrição: a primeira frase deve deixar claro 'o que é + para quem é'; nada de empilhar 'o mais profissional, o mais poderoso' — o peso na busca das lojas depende de palavras-chave e de conversão em downloads; sinceridade funciona melhor que exagero.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Dica: faça um A/B olhando os concorrentes

{class="mt-1"}
Antes de publicar, dê uma volta pelos dez primeiros Apps da mesma categoria na loja e compare as capturas: que estilo de ícone eles usam? que argumento as capturas vendem? como escrevem o título? Imitar não é plagiar — aprenda a fórmula e troque pelo seu conteúdo; essa é a aula mais rápida de partida a frio que existe para qualquer produto.
:::

#### 6. Mini-lista de otimização de desempenho e relatório de quedas

Antes de publicar o App, vale dedicar meia hora a cada uma destas duas tarefas:

##### 1. Quatro checagens de desempenho

1. Listas com LazyColumn: jamais monte listas longas com Column na força bruta — o carregamento preguiçoso é a primeira lição de desempenho no Android;
2. Não coloque a imagem original na marra: use a biblioteca de imagens Coil para redimensionar e cachear automaticamente; uma imagem original de 5 MB é capaz de travar um aparelho de entrada;
3. Evite trabalho pesado na thread principal: banco de dados, rede e arquivos grandes vão para dentro de corrotinas;
4. Meça com o Profiler: o analisador de desempenho nativo do Android Studio mostra memória, CPU e consumo de bateria — meça primeiro, otimize depois; nada de confiar no feeling.

##### 2. Relatório de quedas

O App não cair nos seus testes não significa que não caia no celular do usuário. Antes de publicar, integre o Firebase Crashlytics (oficial do Google, gratuito): poucas linhas de configuração e, quando houver queda, a pilha é reportada automaticamente; no painel você vê 'qual aparelho, qual versão, em qual linha caiu'. Publicar sem monitoramento de quedas é dirigir de olhos fechados.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mãos à obra: 'entregue' o controle de gastos uma vez

{class="mt-1"}
① Complete 3 testes de unidade para lógicas como o parseAmount; ② capture com as próprias mãos, pelo Logcat, uma queda que você mesmo provocou, e conserte; ③ gere um APK assinado em release e mande para um amigo instalar (essa é a cerimônia de 'obra concluída'); ④ se sobrar energia, crie a conta de desenvolvedor e suba o controle de gastos de verdade. Os três primeiros itens dão para fazer ainda hoje à noite.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumo do capítulo

- Trio da depuração: Logcat para ver logs, breakpoints para ver variáveis, Layout Inspector para ver a interface
- Ler uma queda: da base da pilha para cima, ache a primeira linha com o nome do seu pacote
- Três camadas de teste: unidade (segundos, aprenda esta primeiro) / instrumentados / manual
- Publicar exige assinatura: faça backup do keystore e da senha; se perder, o App 'troca de dono'
- Seis passos de publicação: cadastro → materiais → upload do AAB → formulário de segurança de dados → revisão → publicação
:::
