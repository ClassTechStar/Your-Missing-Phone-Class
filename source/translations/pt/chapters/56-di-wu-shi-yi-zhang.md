---
id: di-wu-shi-yi-zhang
num: 51
part: an-zhuo-kai-fa-pian
nav: Capítulo 51: Desenvolvimento de interface — introdução ao Jetpack Compose
toc: default
kind: chapter
---

### Capítulo 51: Desenvolvimento de interface — introdução ao Jetpack Compose

{class="chapter-intro mb-4"}
A interface é tudo o que o usuário vê. Antes do Compose, as interfaces Android eram escritas em XML — trabalhosas como um exercício de preencher lacunas; em 2021, o Google lançou o Jetpack Compose: a interface é "desenhada" direto em código Kotlin, o que você vê é o que você tem, e mudar uma linha atualiza a pré-visualização na hora. Em 2026, o Compose é o padrão absoluto dos projetos novos. Neste capítulo, vamos aprender a "desenhar".

#### 1. A ideia do Compose: a interface é uma função

A ideia central do Compose em uma frase: interface = função. Cada coisa que aparece na tela (texto, botão, imagem) é uma "função combinável" (Composable), marcada com @Composable. Encaixá-las como blocos de montar é fazer a interface.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Primeira tela com Compose</span><span class="dots">···</span>
:::

```
@Composable
fun Greeting(name: String) {
    Text(text = "Olá, $name!")     // um "bloco de texto"
}

// Composição aninhada: blocos grandes com blocos pequenos
@Composable
fun HomeScreen() {
    Column {                          // empilhado na vertical
        Greeting(name = João)
        Greeting(name = Maria)
        Button(onClick = { /* o que fazer ao clicar */ }) {
            Text("Toque aqui")
        }
    }
}
```
:::

Repare no "chapéu" @Composable — ele diz ao compilador: "isto é um bloco de interface". Os blocos podem ser encaixados sem limite; esse é todo o segredo do Compose.

#### 2. Componentes básicos: texto, botão, campo de entrada e imagem

Os componentes do Compose são "blocos de montar"; os quatro mais comuns:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Componente</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">O que faz</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Parâmetros essenciais</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mostrar texto</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">text (o texto a exibir)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Botão</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onClick (callback de clique)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Campo de entrada</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">value, onValueChange (callback de mudança na entrada)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Image</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mostrar imagem</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">painter (recurso de imagem)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Os quatro componentes básicos do Compose

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Exemplo de widgets básicos</span><span class="dots">···</span>
:::

```
@Composable
fun BasicWidgets() {
    Column {
        Text(text = "Isto é um texto")
        Button(onClick = { println("clicado") }) {
            Text("Botão")
        }
        var input by remember { mutableStateOf("") }
        TextField(
            value = input,
            onValueChange = { input = it },
            label = { Text("Digite algo") }
        )
    }
}
```
:::

No trecho do campo de entrada aparece remember { mutableStateOf("") } — é aí que mora a mágica do "estado" do Compose, detalhada na quinta seção deste capítulo. Por ora, apenas tome contato.

#### 3. O trio de layouts: Column, Row e Box

Com os componentes em mãos, como organizá-los na tela? Guarde três "caixas":

- Column: empilha na vertical (como fila de refeitório);
- Row: alinha na horizontal (como pessoas sentadas lado a lado);
- Box: sobrepõe (como cartas de baralho empilhadas; ótimo para selos de canto e máscaras).

::: div .code-block
:::inline div .code-head
<span>KOTLIN · O trio de layouts</span><span class="dots">···</span>
:::

```
Column {
    Text("Primeira linha")
    Row {
        Text("Esquerda")
        Text("Direita")
    }
    Box {
        Text("Camada de baixo")
        Text("Distintivo sobreposto")
    }
}
```
:::

Quer deixar o layout mais bonito? Adicione Modifier aos componentes — é como maquiar os blocos de montar:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Truques úteis do Modifier</span><span class="dots">···</span>
:::

```
Text(
    text = "Texto bonito",
    modifier = Modifier
        .padding(16.dp)          // espaço nas bordas
        .fillMaxWidth()          // preencher a largura
        .background(Color.Blue)  // cor de fundo
        .clickable { /* clique */ }// clicável
)
// Chamadas em cadeia: uma após a outra, a ordem importa (padding primeiro, depois o fundo — o fundo não inclui o espaço)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Atenção: a ordem do Modifier faz diferença

{class="mt-1"}
padding(16.dp).background(Blue) e background(Blue).padding(16.dp) produzem efeitos diferentes — o primeiro é "espaçar antes de pintar" (o fundo não inclui a margem), o segundo é "pintar antes de espaçar" (o fundo inclui a margem). É aqui que o iniciante mais desenha aquelas "bordas brancas estranhas". Na dúvida, troque a ordem e teste: a pré-visualização responde na hora.
:::

#### 4. Estado: fazendo a interface "viver"

Interface estática é sem graça. Para o contador somar +1 ao clicar no botão e o campo de entrada aceitar digitação, você precisa de estado (State). A regra do Compose: a interface sempre reflete fielmente o estado; mudou o estado, a interface se redesenha sozinha.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Estado: contador de toques</span><span class="dots">···</span>
:::

```
@Composable
fun Counter() {
    // remember + mutableStateOf: lembra esse valor que muda
    var count by remember { mutableStateOf(0) }

    Column {
        Text(text = "Você tocou $count vezes")
        Button(onClick = { count++ }) {   // muda o estado
            Text("Toque +1")                // a tela atualiza sozinha
        }
    }
}
```
:::

Três linhas de código e um contador vivo. É daqui que vem a alegria do Compose em relação ao jeito antigo: não é preciso "atualizar a interface" à mão; basta mudar os dados. Guarde duas funções-chave: remember (impede que o valor se perca quando a interface se reorganiza) e mutableStateOf (avisa ao Compose: "este valor mudou, é preciso redesenhar").

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hand-pointer mr-1"></i> Usuário toca</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> O estado muda (count++)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> O Compose percebe a mudança</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> A tela redesenha sozinha (recomposição)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figura 3: O fluxo de dados unidirecional "estado → interface" do Compose
:::

#### 5. Tema e modo escuro: configure uma vez, vale no todo

O MyFirstAppTheme { ... } do projeto modelo é o tema. Baseado nas diretrizes de design do Material 3, ele gerencia cores, fontes e formas de forma unificada. Para dar suporte ao modo escuro, bastam três passos:

1. Defina no tema as duas paletas, clara e escura (o modelo já gera o ColorScheme automaticamente);
2. Quando o sistema entra no modo escuro, isSystemInDarkTheme() detecta automaticamente;
3. Use as cores fornecidas pelo tema (como MaterialTheme.colorScheme.primary) em vez de fixar valores de cor no código.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Dica: cores dinâmicas do Material 3

{class="mt-1"}
Desde o Android 12, o "Material You" permite que o app extraia cores do seu papel de parede. O modelo do Compose já traz suporte por padrão (dynamicColor). O seu app "troca de roupa sozinho" no celular de cada usuário — esse é o romantismo do Android moderno.
:::

#### 6. Pré-visualização, animações e edição em tempo real: os "cheats" do Compose

São três "cheats" de experiência de desenvolvimento no Compose; depois de usá-los, não há volta:

- Pré-visualização com @Preview: adicione a anotação @Preview ao Composable e o Android Studio renderiza a interface na hora, no painel direito — você edita o código vendo o resultado, sem instalar no celular a cada mudança;
- Edição em tempo real (Live Edit): o Android Studio de 2026 suporta "atualização a quente" de certas mudanças no emulador/aparelho real; ajustes pequenos, como mudar a cor de um texto, aparecem no dispositivo em segundos;
- APIs de animação: animateFloatAsState e AnimatedVisibility fazem elementos transitarem com suavidade em poucas linhas de código — a "aparência premium" muitas vezes está a exatamente essas poucas linhas de distância.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Animações em dez minutos</span><span class="dots">···</span>
:::

```
@Composable
fun AnimatedBox() {
    var big by remember { mutableStateOf(false) }
    // quando o valor muda, transita suavemente até o alvo
    val size by animateDpAsState(if (big) 120.dp else 60.dp)

    Box(Modifier
        .size(size)
        .background(MaterialTheme.colorScheme.primary)
        .clickable { big = !big }
    )
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Dica: primeiro a função, depois a animação

{class="mt-1"}
O deslize típico do iniciante é "a interface ainda nem está certa e já se anda brigando com animação". Faça a funcionalidade funcionar primeiro e só depois acrescente os efeitos, de uma vez — é também o princípio do "simplicidade em primeiro lugar": animação é enfeite; funcionalidade é socorro.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mão na massa: faça um "botão do humor"

{class="mt-1"}
Transforme o projeto modelo em um seletor de humor: um único botão que, a cada toque, alterna entre 😀Feliz → 😢Triste → 😡Nervoso, mudando o texto e a cor de fundo junto. Dica: use o when para escolher o texto e a cor conforme o estado. Quando terminar, mande para os amigos brincarem e colha a primeira leva de 'Uau, você já sabe fazer App!'.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumo do capítulo

- A mentalidade do Compose: interface = funções @Composable, aninhadas como blocos de montar
- Os quatro componentes básicos: Text / Button / TextField / Image
- O trio de layouts: Column empilha na vertical, Row alinha na horizontal, Box sobrepõe camadas
- O Modifier encadeado, como quem 'se maquia': padding, fillMaxWidth, background, clickable — a ordem faz diferença
- O estado é a alma: remember + mutableStateOf; mude os dados e a interface se redesenha sozinha
- Tema com Material 3 + cores dinâmicas; o modo escuro se configura uma vez e vale no App inteiro
:::
