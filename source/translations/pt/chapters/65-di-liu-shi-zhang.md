---
id: di-liu-shi-zhang
num: 60
part: ios-kai-fa-pian
nav: Capítulo 60: Configurando o ambiente de desenvolvimento — Xcode e o primeiro projeto
toc: default
kind: chapter
---

### Capítulo 60: Preparando o ambiente de desenvolvimento — Xcode e o primeiro projeto

{class="chapter-intro mb-4"}
Para fazer bem feito, comece pelas ferramentas. Neste capítulo vamos montar a “cozinha”: instalar o Xcode, rodar o simulador, criar o primeiro projeto iOS da sua vida e entender a estrutura do projeto em detalhes. Com o ambiente pronto, você vai ver pela primeira vez o seu código virar um botão que responde ao toque — um momento que muita gente guarda para sempre.

#### 1. Prepare um Mac

Começando pela exigência: desenvolver para iOS precisa ser feito no macOS. Se você não tem um Mac, há três saídas: comprar um (até um Mac mini ou MacBook Air usado serve), alugar um Mac na nuvem por um tempo ou começar pela oitava parte, “Prática de desenvolvimento Android” (que dá para fazer no Windows).

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Item</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Mínimo</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Confortável (recomendado)</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Chip</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple Silicon (a partir do M1)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">M2 ou mais novo</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Memória</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">8GB</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">16GB</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Disco</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Reserve 40 GB ou mais (o Xcode é bem gordinho)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">A partir de 256 GB</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sistema</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">macOS mais recente</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mantenha a atualização automática</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Referência de configuração de um Mac para desenvolvimento (agosto de 2026)

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Dica: dá para aprender a linguagem antes de ter um Mac

{class="mt-1"}
O Swift Playgrounds, gratuito no iPad, ensina o básico da linguagem Swift (sem precisar de Mac); dá até para instalar no iPhone. Aprenda bem o conteúdo do Capítulo 61 brincando no Playgrounds e, quando chegar o Mac, você decola. Afiar o machado não atrasa o corte — é exatamente disso que se trata.
:::

#### 2. Instale o Xcode

O Xcode é o ambiente de desenvolvimento integrado oficial da Apple, e é gratuito. Instalação em três passos:

1. No Mac, abra a App Store, busque “Xcode” e clique em instalar — atenção, ele tem vários GB, então escolha um horário com boa conexão;
2. Ao abrir pela primeira vez depois da instalação, aceite o acordo e deixe os componentes terminarem de baixar (é automático);
3. No menu Xcode > Settings > Locations, confira se o Command Line Tools está selecionado — as ferramentas de linha de comando são pré-requisito de muitos scripts e ferramentas de terceiros.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Atenção: o “jogo de encaixe” entre versões e sistema

{class="mt-1"}
O Xcode novo costuma exigir o macOS mais recente, e Macs antigos ficam presos em versões antigas. Para publicar na App Store, a Apple pede builds feitos com um Xcode relativamente novo (geralmente com um período de tolerância). Por isso, não demore para atualizar o sistema — desenvolvedores iOS estão entre os que mais correm atrás das versões novas.
:::

#### 3. Crie seu primeiro projeto

Abra o Xcode > Create New Project > escolha iOS > modelo App e preencha:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Item</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">O que preencher</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Explicação</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Product Name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstApp</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Nome do app</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Team</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Seu Apple ID (gratuito)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Para a assinatura; conta pessoal serve</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Organization Identifier</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">com.example</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Forma o identificador do pacote junto com o Product Name</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Interface</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Framework principal deste livro</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Language</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Fala por si</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
As cinco coisas a preencher ao criar o projeto

Depois de clicar em Create, o Xcode gera um projeto pronto para rodar. No canto superior esquerdo, escolha um simulador (por exemplo, iPhone 17) e clique no ▶ para executar — em poucos segundos, uma janela com “Hello, world!” aparece na tela do simulador. Seu primeiro app iOS acabou de nascer.

#### 4. Anatomia do projeto: para que serve cada arquivo

À esquerda fica o navegador do projeto; para começar, você só precisa conhecer estes:

::: div .figure
```html
<svg style="max-width:100%;height:auto" width="600" height="290" viewBox="0 0 600 290" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="600" height="290" fill="#fafafa" rx="8"/>
      <text x="20" y="28" font-size="13" font-weight="bold" fill="#111827">MyFirstApp/ raiz do projeto</text>
      <rect x="30" y="42" width="540" height="225" fill="#ffffff" stroke="#d1d5db" rx="6"/>
      <rect x="45" y="56" width="250" height="196" fill="#eef2ff" rx="5"/>
      <text x="56" y="78" font-size="11" fill="#1e1b4b" font-weight="bold">MyFirstApp/ (pasta de código)</text>
      <text x="66" y="100" font-size="10" fill="#374151">├ MyFirstAppApp.swift  ← ponto de entrada do app</text>
      <text x="66" y="120" font-size="10" fill="#374151">├ ContentView.swift  ← tela principal</text>
      <text x="66" y="140" font-size="10" fill="#374151">└ Assets.xcassets  ← ícones, imagens, cores</text>
      <text x="56" y="166" font-size="10" fill="#6b7280">(os arquivos novos vão todos nesta pasta)</text>
      <text x="56" y="196" font-size="10" fill="#1e1b4b" font-weight="bold">Aba Info / Info.plist</text>
      <text x="66" y="216" font-size="10" fill="#6b7280">Declarações do app: nome, permissões, configurações</text>
      <rect x="310" y="56" width="245" height="196" fill="#f0fdf4" rx="5"/>
      <text x="321" y="78" font-size="11" fill="#065f46" font-weight="bold">Outros lugares importantes</text>
      <text x="331" y="100" font-size="10" fill="#374151">📁 Preview Content/  ← recursos de pré-visualização</text>
      <text x="331" y="122" font-size="10" fill="#374151"><i class="fas fa-bullseye mr-1"></i> Configurações do Target (o ícone azul do projeto)</text>
      <text x="331" y="142" font-size="10" fill="#6b7280">— número de versão, sistema mínimo, assinatura: tudo aqui</text>
      <text x="331" y="168" font-size="10" fill="#374151"><i class="fas fa-flask mr-1"></i> MyFirstAppTests/  ← testes unitários</text>
      <text x="331" y="188" font-size="10" fill="#374151">📱 MyFirstAppUITests/ ← testes de interface</text>
      <text x="331" y="216" font-size="10" fill="#9ca3af">(os modelos de teste já estão gerados; usados no Capítulo 67)</text>
    </svg>
```

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figura 2: a estrutura de projeto do Xcode que todo iniciante precisa conhecer
:::

- MyFirstAppApp.swift: o ponto de entrada do programa; no SwiftUI ele tem só algumas linhas — “inicie e mostre a tela principal”;
- ContentView.swift: a view da tela principal; tudo o que você vê agora está aqui;
- Assets.xcassets: o depósito de recursos — ícones, imagens e cores ficam aqui;
- Configurações do Target: clique no ícone azul do projeto à esquerda para entrar; número da versão, versão mínima do iOS e assinatura ficam aí. O nome de exibição e o ícone do app também se configuram nesse lugar.

#### 5. Truques de eficiência no Xcode: os cinco “cheats de atalhos” do iniciante

Dominando estes, você vai parecer “bem profissional”:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ação</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Atalho</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Função</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Executar</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘R</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Compila e roda o app</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Abrir/alternar a pré-visualização do canvas</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌥⌘↩</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">O interruptor do “o que você vê é o que você tem”</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Formatar a indentação</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌃I</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Organiza automaticamente a indentação do código selecionado</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Abrir arquivo rapidamente</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘O</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Digite o nome do arquivo e ele abre na hora (o mais usado!)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Comentar/descomentar</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ligar e desligar trechos de código durante o debug</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Atalhos mais usados do Xcode (o kit do iniciante)

Mais dois benefícios escondidos: rodar vários simuladores ao mesmo tempo (iPhone e iPad lado a lado para comparar layouts) e a biblioteca de snippets de código (arraste as linhas que você usa sempre para o painel de Snippets à direita e insira com um clique na próxima vez) — use as ferramentas de eficiência desde cedo e a fluidez vem naturalmente.

#### 6. Testes no aparelho: colocando o app no seu iPhone

O simulador é ótimo, mas o aparelho de verdade é o destino final. Dá para testar no aparelho até com um Apple ID gratuito:

1. Conecte o iPhone pelo cabo de dados (ou faça o debug sem fio no mesmo Wi-Fi);
2. Na lista de aparelhos no topo do Xcode, selecione seu celular; na primeira vez, ele pedirá para entrar com o Apple ID e configurará a assinatura automaticamente;
3. No iPhone, vá em [Ajustes] > [Geral] > [VPN e Gerenciamento de Dispositivos] e confie no seu certificado de desenvolvedor;
4. Clique no ▶ e o app é instalado no aparelho.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Atenção: a “regra dos sete dias” da conta gratuita

{class="mt-1"}
Um app assinado com Apple ID gratuito expira depois de 7 dias (basta rodar de novo uma vez para renovar). É um mecanismo da Apple contra abuso e, na fase de aprendizado, dá e sobra; a conta de desenvolvedor paga (99 dólares/ano) não tem essa limitação — detalhes no Capítulo 67.
:::

#### 7. Um primeiro teste + primeiros socorros para erros comuns

Abra o ContentView.swift, troque o texto de Text("Hello, world!") pelo seu nome e pressione ⌘R para rodar de novo — em poucos segundos, seu nome aparece no simulador. Parabéns: você acabou de completar o primeiro ciclo completo de “editar código > compilar > instalar > executar”.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Sintoma do erro</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Causa comum</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Solução</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Erro de Signing</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Team não selecionado ou certificado vencido</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Em Target > Signing, marque sua conta; com conta gratuita, rode de novo uma vez</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Simulador com tela preta / não abre</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Imagem corrompida</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menu Device > Erase All Content; ou apague o simulador e crie outro</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode baixa devagar / não instala</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Instabilidade de rede na App Store</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Troque de horário; ou baixe o pacote .xip no site de desenvolvedores da Apple</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Tabela de primeiros socorros para erros de ambiente de iniciantes

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mãos à obra: complete sua lista de “ritual de desenvolvedor”

{class="mt-1"}
① Instale o Xcode e faça o simulador funcionar; ② rode seu app no aparelho de verdade e tire uma captura de tela para guardar; ③ troque o texto de Hello pelo seu nome; ④ nas configurações do Target, mude o nome de exibição do app para “Meu primeiro app”. Com esses quatro passos feitos, você já é alguém com uma obra própria.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumo do capítulo

- Exigências: Mac + Xcode; sem Mac, aprenda a linguagem primeiro no Swift Playgrounds do iPad
- Instale o Xcode pela App Store; versões novas exigem sistema novo — não adie a atualização
- Os cinco pontos ao criar um projeto: nome, Team, identificador da organização, SwiftUI e Swift
- Regra de bolso do projeto: o código fica todo na pasta MyFirstApp/; as configurações do Target cuidam de versão e assinatura
- Com Apple ID gratuito, o debug no aparelho tem limite de 7 dias de assinatura; a conta paga não tem essa limitação
- A rotina de desenvolvimento = editar código > ⌘R > ver o resultado, em ciclo contínuo
:::
