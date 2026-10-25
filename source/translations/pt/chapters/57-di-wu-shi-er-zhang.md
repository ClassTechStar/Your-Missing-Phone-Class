---
id: di-wu-shi-er-zhang
num: 52
part: an-zhuo-kai-fa-pian
nav: Capítulo 52: Os quatro componentes principais e o ciclo de vida da Activity
toc: default
kind: chapter
---

### Capítulo 52: Os quatro componentes básicos e o ciclo de vida da Activity

{class="chapter-intro mb-4"}
Se o Compose é o 'rosto' do App, este capítulo trata do 'esqueleto' dele. O Android define quatro componentes básicos, e todo App é montado com eles; o mais importante deles, a Activity, tem um 'mapa do ciclo de vida' que todo desenvolvedor Android precisa gravar na cabeça. Ao terminar este capítulo, você vai entender mistérios de longa data como 'por que, quando o meu App volta do segundo plano, o estado dele desapareceu?'.

#### 1. Os quatro componentes básicos: os 'pilares' do Android

O Android define oficialmente quatro componentes básicos, cada um responsável por um tipo de tarefa:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Componente</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Função</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Uma analogia</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Activity</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Uma interface visível</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">A fachada da loja — o usuário vê e interage</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Service</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">O 'invisível' que trabalha em segundo plano</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">O operário do armazém — toca música, baixa arquivos; não precisa de interface</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">BroadcastReceiver</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Recebe avisos do sistema</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">A portaria — o alto-falante que anuncia 'a bateria está acabando', 'a internet caiu'</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ContentProvider</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Compartilha dados entre Apps</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">O arquivo público — por exemplo, compartilhar os contatos com outros Apps</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Visão rápida dos quatro componentes do Android

Na fase de iniciante, você passa 95% do tempo lidando com a Activity; o Service e o BroadcastReceiver entram em cena ao reproduzir música e enviar notificações push; o ContentProvider é o menos usado (o sistema já encapsula os dados mais comuns). E atenção: os quatro componentes precisam ser 'registrados' no AndroidManifest.xml — sem o registro, o sistema não os encontra.

#### 2. O ciclo de vida da Activity: o primeiro 'mapa do tesouro' do desenvolvedor Android

No celular, um App pode ser interrompido a qualquer momento: chega uma ligação, o usuário troca de app para responder o WeChat, o sistema fica sem memória e encerra o seu processo... A vida de uma Activity é uma viagem em loop por este mapa:

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onCreate (nascimento: inicialização)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onStart (visível)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onResume (em primeiro plano, interagindo)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center">onPause (parcialmente coberto)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center">onStop (totalmente oculto)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center">onDestroy (destruído)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center">🔁 onRestart / onStart / onResume: ao voltar ao primeiro plano, o mesmo caminho de volta</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figura 4: Ciclo de vida da Activity (sentido de avanço: nasce na linha de cima → sai na de baixo; na volta, retorna pelo mesmo caminho)
:::

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Callback</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Quando é disparado</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Uso típico</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onCreate</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Quando a Activity é criada (uma vez)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Carregar a interface e inicializar os dados</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onStart</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">A interface fica visível</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Iniciar algumas lógicas leves</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onResume</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Recebe o foco e fica interativa</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Iniciar animações, retomar a reprodução</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onPause</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">No momento em que é parcialmente coberta ou trocada de tela</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pausar animações, salvar rascunhos</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onStop</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Totalmente invisível</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Liberar recursos pesados, pausar downloads</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onDestroy</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Antes de ser destruída</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">A limpeza final</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Usos típicos dos seis callbacks do ciclo de vida

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Alerta de armadilha: girar a tela 'mata' a Activity

{class="mt-1"}
O clássico tombo de iniciante: você gira a tela do App e o texto dos campos de entrada desaparece. Motivo: por padrão, girar a tela destrói e recria a Activity (passando por onDestroy → onCreate). Solução: use rememberSaveable para guardar o estado (o substituto do remember no Compose); ele recupera o valor automaticamente na recriação. Isso será usado repetidamente nos capítulos 6 e 7.
:::

#### 3. Intent: o 'bilhete' de passagem dentro e fora do App

A Intent (intenção) é o 'bilhete' de comunicação entre componentes. Para saltar de uma tela a outra, abrir o navegador ou acionar a câmera, é preciso 'comprar o bilhete e embarcar':

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Navegar com Intent</span><span class="dots">···</span>
:::

```
// Modo 1: Intent explícito — você indica exatamente para qual tela ir
val intent = Intent(this, DetailActivity::class.java)
intent.putExtra("name", João)     // leva a "bagagem" (dados) junto
startActivity(intent)

// Modo 2: Intent implícito — você diz o que quer e o sistema acha quem faz
val web = Intent(Intent.ACTION_VIEW, Uri.parse("https://developer.android.com"))
startActivity(web)   // o sistema abre o navegador / ou deixa você escolher
```
:::

Cada modo tem seu uso: o explícito serve para navegar entre telas dentro do seu próprio App; o implícito serve para acionar recursos do sistema ou de outros Apps (abrir páginas, ligar, compartilhar). Em projetos Compose, dentro de um Composable, basta obter o Context com LocalContext.current para poder chamar startActivity.

#### 4. Múltiplas telas e navegação

Apps de verdade têm várias telas. A solução de navegação recomendada oficialmente pelo Compose é o Navigation Compose (biblioteca androidx.navigation):

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Esqueleto do Navigation Compose</span><span class="dots">···</span>
:::

```
val navController = rememberNavController()

NavHost(navController, startDestination = "home") {
    composable("home") { HomeScreen(navController) }
    composable("detail/{name}") { entry ->
        val name = entry.arguments?.getString("name")
        DetailScreen(name ?: "Desconhecido")
    }
}

// Navegar dentro da tela:
navController.navigate("detail/João")     // com argumentos
navController.popBackStack()              // voltar
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Dica: e quando as telas se multiplicam?

{class="mt-1"}
Quando o projeto crescer, centralize todas as rotas de telas em um único arquivo (por exemplo, AppNavGraph.kt) e gerencie tudo de um só lugar; não deixe a lógica de 'para onde saltar' espalhada pelas telas. Esse é o primeiro passo para sair do 'funciona' e chegar ao 'fácil de manter'.
:::

#### 5. De quebra: o que é Fragment (e por que este livro não o ensina)

Folheando tutoriais antigos, você certamente vai esbarrar no Fragment — um 'trecho de interface reutilizável' dentro da Activity, protagonista absoluto da arquitetura antiga de múltiplas telas. Mas na era do Compose, as telas se resolvem com funções Composable + rotas de Navigation, e a própria Google já reduziu o papel do Fragment. Por isso este livro não o colocou na linha principal.

Sugestão: em projetos novos, não use Fragment por iniciativa própria; mas, ao ler código antigo ou se o tema surgir numa entrevista, basta saber que é um 'trecho de interface embutido na Activity'. Ao buscar material de estudo, priorize sempre o que é de 2023 em diante — o 'almanaque' do ecossistema Android envelhece mais rápido do que se imagina.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mãos à obra: dê 'memória' ao contador

{class="mt-1"}
Modifique o contador do capítulo 51: ① troque remember por rememberSaveable e gire a tela para conferir que o número continua lá; ② adicione um botão 'Sobre' que use o Navigation para saltar a uma segunda tela e mostrar o número da versão; ③ imprima logs (Log.d) no onCreate/onPause das duas telas e observe no Logcat a ordem de chamada do ciclo de vida. Feitos esses três passos, o ciclo de vida deixa de ser teoria de papel.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumo do capítulo

- Os quatro componentes: Activity (fachada), Service (segundo plano), BroadcastReceiver (alto-falante), ContentProvider (arquivo)
- Os seis callbacks do ciclo de vida: onCreate → onStart → onResume → onPause → onStop → onDestroy
- Girar a tela destrói e recria a Activity: use rememberSaveable para preservar o estado
- A Intent é o 'bilhete': explícita para navegar nas telas de casa, implícita para acionar recursos do sistema
- Múltiplas telas com Navigation Compose: NavHost + rotas composable
:::
