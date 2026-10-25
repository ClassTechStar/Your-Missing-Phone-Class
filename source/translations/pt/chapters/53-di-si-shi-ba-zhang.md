---
id: di-si-shi-ba-zhang
num: 48
part: an-zhuo-kai-fa-pian
nav: Capítulo 48: Conhecendo o Android — do sistema operacional ao ecossistema de desenvolvimento
toc: default
kind: chapter
---

### Capítulo 48: Conhecendo o Android — do sistema operacional ao ecossistema de desenvolvimento

{class="chapter-intro mb-4"}
Parabéns por tomar essa decisão — deixar de ser "quem usa o celular" para virar "quem faz aplicativos de celular". Antes de pôr a mão na massa, vamos abrir o mapa: de onde vem o Android? Por que desenvolvedores do mundo inteiro escrevem aplicativos para ele? O que acontece entre você bater no teclado e o app chegar ao celular do usuário?

#### 1. As origens do Android: do "robozinho" ao "maior sistema do mundo"

A história do Android começa em 2003 — um engenheiro chamado Andy Rubin fundou a Android Inc., com um objetivo bem modesto: criar um sistema operacional inteligente que "entendesse melhor de câmeras". Depois, o Google a comprou em 2005; em 2007, uniu dezenas de fabricantes para fundar a Open Handset Alliance (OHA); e, em setembro de 2008, o primeiro celular Android, o HTC Dream (G1), chegou oficialmente ao mercado.

Daí em diante, todo mundo conhece a história: em 2026, o Android é o sistema operacional móvel com a maior fatia de mercado do mundo, com bilhões de dispositivos ativos. Seu celular, seu aparelho de TV, a central multimídia do carro e o seu smartwatch muito provavelmente rodam Android. O que isso significa? Que cada linha de código que você escrever tem chance de ser usada pelo maior número de pessoas do planeta.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Dica: o DNA de código aberto do Android

{class="mt-1"}
O núcleo do código do Android (AOSP, Android Open Source Project) é de código aberto — qualquer fabricante pode pegar, modificar e personalizar. Por isso a Xiaomi tem a MIUI (hoje HyperOS), a Huawei tem a camada de compatibilidade HarmonyOS e a Samsung tem a One UI. Para quem desenvolve, isso é uma boa: você aprende "desenvolvimento Android", e não "desenvolvimento para uma marca" — um só aprendizado serve para todo o ecossistema.
:::

A evolução dos números de versão também é divertida: a partir do 1.5, o Cupcake, cada versão grande recebeu nome de sobremesa — Donut, Eclair, Frozen Yogurt, Gingerbread... só em 2019, com o Android 10, passou a ser só números. Em agosto de 2026, a versão estável mais recente é o Android 17; já a "versão mínima suportada", que é o que de fato importa ao desenvolver, nos apps principais costuma ficar entre o Android 8 (API 26) e o Android 10 (API 29) — suportando aparelhos de alguns anos atrás é que a sua base de usuários fica grande o suficiente.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Versão</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Codinome/ano</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">O que importa para quem desenvolve</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 8 (API 26)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Oreo · 2017</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Canais de notificação, limites em segundo plano — o piso de muitos aparelhos antigos</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 10 (API 29)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2019</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Chegada do armazenamento com escopo, grande mudança nas regras de acesso a arquivos</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 12 (API 31)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2021</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cores dinâmicas do Material You, grande salto visual na interface</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 13 (API 33)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2022</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Permissão de notificação em tempo de execução, com pop-up perguntando "pode enviar notificações?"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 14-15 (API 34-35)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2023-2024</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retorno preditivo, páginas de 16 KB e privacidade ainda mais apertada</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 16-17 (API 36-37)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2025-2026</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ritmo mais rápido de versões menores e integração de recursos de IA (como extensões do Gemini)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Breve história das versões do Android (até agosto de 2026; destaques para desenvolvimento)

#### 2. Em que linguagem escrever: Java ou Kotlin?

Ao longo da história do desenvolvimento Android, duas linguagens dominaram. O Java é o "veterano fundador" — esteve lá desde o nascimento do Android; o Kotlin foi apadrinhado pelo Google em 2017 como "cidadão de primeira classe" e, desde 2019, a posição oficial é "Kotlin first". Em 2026, praticamente todos os projetos novos usam Kotlin, e a maioria dos antigos vem migrando aos poucos.

Falando francamente: se você parte do zero absoluto, aprenda Kotlin direto e não volte para o Java. São três motivos: primeiro, o código Kotlin é 30% a 40% menor que o Java (a mesma funcionalidade fica mais curta e mais clara em Kotlin); segundo, ele protege de fábrica contra o "ponteiro nulo", o pesadelo dos iniciantes; terceiro, todos os tutoriais modernos, a documentação oficial e as ferramentas de programação com IA (lembra do nosso livro de programação com IA?) tomam o Kotlin como padrão. O Java só aparece quando você mantém projetos antigos ou lê código legado.

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
Estilo Java (versão prolixa)

{class="font-mono text-xs leading-relaxed"}
public class MainActivity extends Activity {<br>&nbsp;&nbsp;@Override<br>&nbsp;&nbsp;protected void onCreate(Bundle b) {<br>&nbsp;&nbsp;&nbsp;&nbsp; super.onCreate(b);<br>&nbsp;&nbsp;&nbsp;&nbsp; setContentView(R.layout.activity);<br>&nbsp;&nbsp;}<br>}
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
Estilo Kotlin (versão enxuta)

{class="font-mono text-xs leading-relaxed"}
class MainActivity : ComponentActivity() {<br>&nbsp;&nbsp;override fun onCreate(b: Bundle?) {<br>&nbsp;&nbsp;&nbsp;&nbsp; super.onCreate(b)<br>&nbsp;&nbsp;&nbsp;&nbsp;setContent { App() }<br>&nbsp;&nbsp;}<br>}
:::
:::

Para a mesma tarefa, o Kotlin dispensa um monte de chaves e código repetitivo. No Capítulo 50 vamos estudá-lo a sério; por ora, basta guardar: o "idioma oficial" do desenvolvimento Android se chama Kotlin.

#### 3. Como um app nasce?

Muita gente acha que "desenvolver um app" é abrir o computador e escrever código sem parar. Na prática, da ideia até o celular do usuário, um app passa, em linhas gerais, por esta linha de produção:

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-lightbulb mr-1"></i> Ideia</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center">📐 Design (interface + funções)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-keyboard mr-1"></i> Escrever código</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hammer mr-1"></i> Compilar e empacotar (APK/AAB)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> Teste (emulador + aparelho real)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-rocket mr-1"></i> Publicação (loja/instalador)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figura 1: O fluxo completo de um app Android, da ideia à publicação na loja
:::

Nesse fluxo há dois conceitos que você precisa conhecer desde já:

- APK: o formato de pacote de instalação dos aplicativos Android (.apk); dá para instalar no celular com dois toques, como o .exe do Windows. Use-o para testar por conta própria ou passar para um amigo experimentar.
- AAB: o Android App Bundle (.aab), o "formato de empacotamento avançado" usado para publicar no Google Play. A loja recorta o pacote dinamicamente conforme o modelo do celular de cada usuário, deixando o download de cada um menor. Você não consegue instalar um .aab por conta própria; ele só pode ser entregue pela loja.

Outro termo que você vai ouvir sem parar: SDK (Software Development Kit, kit de desenvolvimento de software). É todo o "equipamento de desenvolvimento" fornecido oficialmente pelo Android — inclui as bibliotecas de API de cada versão, ferramentas de depuração, imagens de emulador e mais. As classes como Activity e Button, que você usa ao programar, vêm do SDK.

#### 4. Panorama da stack Android: a sua "lista de armas"

Antes de estudar de fato, conheça a configuração padrão dos projetos Android mainstream em 2026 — tudo bem se esta lista não fizer sentido agora; quando você terminar o livro e voltar a ela, tudo se esclarecerá:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Camada</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Escolha dominante (2026)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Para que serve</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Linguagem</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin 2.x</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">A linguagem em que se escreve a lógica</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Interface</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Jetpack Compose + Material 3</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Desenhar a interface com código (fio condutor deste livro)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Arquitetura</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MVVM + ViewModel</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Separa a interface da lógica para o código não virar bagunça</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Armazenamento de dados</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room (banco de dados) + DataStore (configurações)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Guardar dados no celular</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Rede</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit + OkHttp + corrotinas do Kotlin</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Conversar com o servidor</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ferramenta de build</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gradle + Kotlin DSL</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Transformar o código em pacote de instalação</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ambiente de desenvolvimento</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android Studio</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">O IDE "tudo-em-um" oficial do Google</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Visão rápida da stack Android dominante em 2026

Não se assuste com essa sequência de termos em inglês. Eles são como as panelas e as vasilhas da cozinha — por ora basta saber que "para cozinhar, é preciso entrar na cozinha"; como cada ferramenta funciona, os próximos capítulos vão desmontando uma a uma. E a boa notícia: ao criar um projeto novo, o Android Studio configura todo esse conjunto automaticamente; você só precisa cozinhar.

#### 5. Android vs iOS: a primeira "aula de escolha de lado" de quem desenvolve

Talvez você tenha, ao mesmo tempo, aparelhos Android e Apple. Como desenvolvedor, vale conhecer com antecedência as diferenças de experiência entre os dois lados — não é uma torcida por "qual é melhor", e sim a conta real de "por qual lado é mais adequado começar":

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Critério</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Desenvolvimento Android</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Desenvolvimento iOS</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Computador de desenvolvimento</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Windows, Mac ou Linux, qualquer um serve</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Precisa ser Mac (o Xcode é exclusivo)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ferramentas de desenvolvimento</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android Studio (gratuito)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode (gratuito) + taxa anual de US$ 99 para publicar</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Revisão para publicação</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Flexível, de algumas horas a alguns dias</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Rígida, de 1 a 7 dias é o comum</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Instalar e testar</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">APK: envia e instala à vontade</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Distribuição restrita; testar exige assinatura/TestFlight</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cenário de receita</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Predomínio de anúncios e canais locais</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">A App Store tem hábito de compra dentro do app melhor</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Custo de aprendizado</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mais conceitos (os quatro grandes componentes etc.)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ecossistema fechado, mas coeso e com documentação caprichada</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Comparação dos caminhos de desenvolvimento Android e iOS (agosto de 2026)

Falando francamente: se o seu computador não é um Mac, essa questão nem se põe — o Android é a única opção. Se você tem um Mac, dá para ler a Oitava e a Nona Partes deste livro lado a lado: a lógica de programação se transfere, e aprender o segundo lado depois do primeiro fica bem mais rápido.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mão na massa: conheça o "Android" dentro do seu celular

{class="mt-1"}
Abra, no celular, [Configurações] → [Sobre o telefone] (ou "Informações do telefone") e localize a linha "Versão do Android" — toque nela várias vezes seguidas e você ainda dispara o minigame secreto do sistema. Anote o número da sua versão e confira na tabela de versões acima a qual geração ele pertence. O seu celular é a sua primeira "máquina de testes de desenvolvimento".
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumo do capítulo

- O Android nasceu em 2008; em 2026, é o sistema móvel com a maior fatia de mercado, com bilhões de dispositivos ativos
- A versão estável mais recente é o Android 17; os apps principais suportam no mínimo o Android 8-10, para a base de usuários ficar grande o suficiente
- Projetos novos usam Kotlin sem exceção: 30%+ menos código, proteção contra ponteiro nulo e escolha oficial
- APK para instalar por conta própria, AAB para a loja; o SDK é o kit oficial de equipamento de desenvolvimento
- Stack padrão de 2026: Kotlin + Compose + MVVM + Room + Retrofit + Gradle + Android Studio
:::
