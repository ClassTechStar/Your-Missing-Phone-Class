---
id: di-si-shi-jiu-zhang
num: 49
part: an-zhuo-kai-fa-pian
nav: Capítulo 49: Configurando o ambiente de desenvolvimento — Android Studio e o primeiro projeto
toc: default
kind: chapter
---

### Capítulo 49: Montando o ambiente de desenvolvimento — Android Studio e o primeiro projeto

{class="chapter-intro mb-4"}
Para fazer bem o trabalho, é preciso primeiro afiar as ferramentas. Neste capítulo montamos a "cozinha": instalar o Android Studio, fazer o emulador rodar, criar o primeiro projeto Android da sua vida e desmontar a estrutura do projeto para entender cada peça. Com o ambiente pronto, você verá pela primeira vez o código que escreveu virar um botão clicável — um momento que muita gente guarda a vida inteira.

#### 1. Instalando o Android Studio

O Android Studio é o ambiente de desenvolvimento integrado (IDE) oficial do Google, gratuito e do tipo "tudo-em-um": escrever código, ver a pré-visualização da interface, depurar e gerar o pacote, tudo nele. Quatro passos para instalar:

1. Abra o site oficial developer.android.com/studio e baixe a versão estável mais recente (em agosto de 2026, a versão posterior à Narwhal; há versões para Windows/Mac/Linux);
2. Execute o instalador e vá dando "Avançar" — o assistente já inclui automaticamente o Android SDK e os componentes do emulador;
3. No primeiro início, baixe os componentes do SDK conforme as instruções (deixe as opções padrão marcadas; pode levar alguns minutos e alguns GB de espaço);
4. No fim, você verá a tela de boas-vindas — parabéns, a "cozinha" está pronta.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Atenção: tenha os requisitos de hardware na ponta do lápis

{class="mt-1"}
O Android Studio é um "come-memória": o ideal é partir de 16 GB de RAM (8 GB até rodam, mas o emulador fica travado), reserve mais de 20 GB de disco e use uma CPU com suporte a virtualização (ative VT-x/AMD-V na BIOS). Se o computador for realmente antigo, use a "depuração em aparelho real" no lugar do emulador (falaremos na quarta seção deste capítulo); a experiência sai até mais fluida.
:::

#### 2. Criando o seu primeiro projeto

Na tela de boas-vindas, clique em New Project, escolha o modelo Empty Activity (o mais limpo para iniciantes) e preencha três coisas:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Item de configuração</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">O que preencher</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Descrição</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">My First App</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">O nome do app, exibido na tela inicial do celular</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Package name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">com.example.myfirstapp</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Identificador único no mundo; o costume é "domínio invertido", deixe o padrão por ora</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Minimum SDK</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">API 26(Android 8.0)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Versão mínima suportada, cobrindo 95%+ dos aparelhos</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
As três coisas a preencher ao criar um projeto

Depois de clicar em Finish, o Android Studio usa o Gradle para baixar as dependências e construir o projeto automaticamente (na primeira vez são alguns minutos; depois fica bem mais rápido). Com a build concluída, você já tem um app que roda — embora, por ora, ele só saiba mostrar um "Hello Android!".

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Dica: os segredos do nome de pacote

{class="mt-1"}
O nome de pacote (package name) é como o "número de identidade" do app: não pode repetir no mundo inteiro e não pode mais ser mudado depois da publicação. Para praticar, com.example.xxx serve; em produto formal, troque pelo seu próprio domínio invertido (por exemplo, com.seunome.nome-do-app). Não publique com com.example — a loja recusa o pacote.
:::

#### 3. Colocando para rodar: emulador e aparelho real

Com o código pronto, é preciso encontrar um "celular" para rodá-lo. Você tem duas opções:

##### 1. O emulador (Emulator)

O emulador é um celular Android virtual dentro do computador. No Android Studio, abra Device Manager → Create Device, escolha um aparelho (recomendo a linha Pixel) → selecione uma imagem de sistema (com Google APIs) → baixe → inicie. Depois clique no triângulo verde Run, na barra de ferramentas; em alguns segundos, o seu app aparecerá na tela do "celular".

##### 2. Depuração em aparelho real (a mais recomendada)

O aparelho real é sempre o ambiente de teste mais fiel — o toque ao deslizar, a rede de verdade, os sensores reais; nada disso o emulador reproduz. Depurar num celular Android é simples:

1. No celular, abra [Configurações] → [Sobre o telefone] e toque 7 vezes seguidas em "Número da versão" para ativar as "Opções do desenvolvedor";
2. Em [Opções do desenvolvedor], ative a Depuração USB;
3. Conecte o celular ao computador com o cabo de dados e, no pop-up do celular, escolha "Permitir depuração USB";
4. Volte ao Android Studio: o seu celular vai aparecer na lista de dispositivos da barra de ferramentas; clique em Run.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Alerta de armadilha: não deixe a Depuração USB sempre ativada

{class="mt-1"}
A Depuração USB funciona como abrir uma "porta dos fundos" para o computador. Ao carregar em lugares públicos ou conectar a computadores que não são de confiança, desative a Depuração USB sem falta, para evitar que outros leiam os seus dados por ela. No dia a dia, desligue assim que terminar de desenvolver; faça disso um hábito.
:::

#### 4. Desmontando a estrutura do projeto: para que serve cada arquivo

Ao abrir o projeto pela primeira vez, a árvore de arquivos à esquerda pode deixar você tonto. Calma: no dia a dia, 90% do seu tempo será com estes poucos itens:

::: div .figure
```html
<svg style="max-width:100%;height:auto" width="600" height="300" viewBox="0 0 600 300" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="600" height="300" fill="#fafafa" rx="8"/>
      <text x="20" y="30" font-size="13" font-weight="bold" fill="#111827">MyFirstApp/ raiz do projeto</text>
      <rect x="30" y="45" width="540" height="230" fill="#ffffff" stroke="#d1d5db" rx="6"/>
      <text x="45" y="70" font-size="11" fill="#4f46e5" font-weight="bold">app/ ← onde você escreve código</text>
      <rect x="60" y="82" width="240" height="178" fill="#eef2ff" rx="5"/>
      <text x="70" y="102" font-size="10" fill="#1e1b4b" font-weight="bold">src/main/</text>
      <text x="80" y="120" font-size="10" fill="#374151">├ java/…/MainActivity.kt  ← código de lógica</text>
      <text x="80" y="138" font-size="10" fill="#374151">├ res/  ← recursos (imagens, textos, cores)</text>
      <text x="80" y="156" font-size="10" fill="#374151">└ AndroidManifest.xml  ← a "certidão de nascimento" do app</text>
      <text x="70" y="180" font-size="10" fill="#1e1b4b" font-weight="bold">build.gradle.kts</text>
      <text x="80" y="198" font-size="10" fill="#6b7280">Declara as bibliotecas dependentes (versão do SDK, Compose etc.)</text>
      <text x="70" y="222" font-size="10" fill="#1e1b4b" font-weight="bold">src/androidTest/ e test/</text>
      <text x="80" y="240" font-size="10" fill="#6b7280">Código de testes automatizados (usado no Capítulo 56)</text>
      <rect x="320" y="82" width="230" height="178" fill="#f0fdf4" rx="5"/>
      <text x="330" y="102" font-size="10" fill="#065f46" font-weight="bold">Outros arquivos na raiz</text>
      <text x="340" y="122" font-size="10" fill="#374151">gradle/ + gradlew.bat  ← scripts de build</text>
      <text x="340" y="142" font-size="10" fill="#374151">settings.gradle.kts  ← configurações do projeto</text>
      <text x="340" y="162" font-size="10" fill="#6b7280">(Regra do iniciante: mexa só na pasta app/,</text>
      <text x="340" y="180" font-size="10" fill="#6b7280">trate o resto como uma "caixa-preta" por enquanto — não mexa)</text>
      <text x="340" y="208" font-size="10" fill="#9ca3af">.gitignore  ← lista de exclusão do controle de versão</text>
    </svg>
```

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figura 2: A estrutura do projeto que todo iniciante precisa entender (regra de bolso: mexa só na pasta app/)
:::

- MainActivity.kt: a "porta de entrada" do app. Quando o usuário toca no ícone, é ela a primeira a ser despertada. No modelo atual, ela é a responsável por mostrar "Hello Android!".
- AndroidManifest.xml: o "registro de residência" do app — declara como o app se chama, qual é o ícone, quais telas existem e quais permissões ele usa (câmera, localização etc.).
- A pasta res/: o depósito de recursos, onde ficam imagens, ícones, textos e cores. Colocar os textos em arquivos de recurso em vez de deixá-los fixos no código é um bom hábito do desenvolvimento Android (facilita trocar idioma e tema).
- build.gradle.kts: a "receita" da build — declara a versão mínima suportada e quais bibliotecas são dependências (como o Compose).

#### 5. Primeira prova: troque o "Hello" pelo seu nome

Abra o MainActivity.kt e você verá o código gerado pelo modelo do Compose. Localize a linha Text("Hello Android!"), troque o texto entre aspas pelo seu nome, por exemplo Text("Olá, João! Este é o meu primeiro app"), e pressione Ctrl+R (Cmd+R no Mac) para rodar de novo. Em poucos segundos, o seu nome aparece no emulador.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · MainActivity.kt (mude esta linha)</span><span class="dots">···</span>
:::

```
setContent {
    MyFirstAppTheme {
        Surface(modifier = Modifier.fillMaxSize()) {
            // ▼ mude isto para o seu texto
            Text("Olá, João! Este é meu primeiro app")
        }
    }
}
```
:::

Parabéns: você acabou de completar um ciclo inteiro de "editar o código → compilar → instalar → rodar". Esse ciclo é a rotina diária de desenvolvimento de agora em diante. Aproveite a empolgação e tente mudar mais coisas: aumente o tamanho da fonte, troque a cor — no próximo capítulo você vai aprender de onde vem essa "mágica".

#### 6. Primeiros socorros para erros comuns: o "pronto-socorro" das duas primeiras semanas

Na fase de configuração do ambiente e da primeira build, é bem provável que você esbarre nestes três erros. Sem pânico: todos têm antídoto:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Erro observado</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Causa comum</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Antídoto</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gradle sync failed / download lento das dependências</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Acesso de rede aos repositórios instável</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Configure espelhos de repositório para o Gradle (espelhos maven da Alibaba Cloud/Tencent Cloud); pesquise "gradle mirror" na internet e ajuste seguindo o tutorial</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Componentes do SDK faltando</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">O download do SDK foi pulado na instalação</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Em Settings → SDK Manager, instale as plataformas e ferramentas que faltam</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">O emulador não inicia / tela preta</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Virtualização desativada ou imagem corrompida</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ative VT-x/AMD-V na BIOS; apague o emulador e recrie; ou vá direto para a depuração em aparelho real</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Tabela de primeiros socorros para erros de ambiente de iniciante

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Dica: a metodologia para pesquisar erros

{class="mt-1"}
A primeira linha da mensagem de erro é a mais valiosa — copie-a exatamente como está no buscador e acrescente a palavra-chave "android studio". Não pesquise perguntas vagas como "não consigo configurar o ambiente, e agora?"; pesquise erros concretos como "Gradle sync failed: Could not resolve com.android.tools.build". Só pergunta precisa recebe resposta precisa.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mão na massa: complete a sua lista de "rituais de desenvolvedor"

{class="mt-1"}
1) Instale o Android Studio e faça o emulador rodar; 2) rode o seu app num aparelho real e tire um print para guardar; 3) troque o texto do Hello pelo seu nome; 4) compacte o projeto e guarde uma cópia. Completados esses quatro passos, você pode anunciar aos amigos: agora eu também sou desenvolvedor Android (com print como prova).
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumo do capítulo

- Android Studio = IDE oficial gratuito; recomenda-se 16 GB de RAM + 20 GB de disco + virtualização ativada
- Os três essenciais do projeto novo: nome, nome de pacote (único no mundo; não publique com com.example) e SDK mínimo (a partir da API 26)
- Duas formas de rodar: emulador (celular virtual dentro do computador) e aparelho real (ative a Depuração USB e lembre de desligar depois)
- Regra de bolso do projeto: mexa só na pasta app/ — MainActivity.kt é a porta de entrada, o Manifest é o registro de residência e res/ é o depósito de recursos
- Rotina de desenvolvimento = editar o código → Run → ver o resultado, em ciclo constante
:::
