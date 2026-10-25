---
id: di-liu-shi-er-zhang
num: 62
part: ios-kai-fa-pian
nav: Capítulo 62: Desenvolvimento de interface — introdução ao SwiftUI
toc: default
kind: chapter
---

### Capítulo 62: Desenvolvimento de interface — introdução ao SwiftUI

{class="chapter-intro mb-4"}
A interface é tudo o que o usuário vê. O SwiftUI é o framework de interface declarativa lançado pela Apple em 2019 — você apenas “declara” como a interface deve ficar, e o sistema cuida sozinho da renderização, do modo escuro e da adaptação às várias telas. Em 2026, o SwiftUI já é o padrão absoluto para projetos novos. Neste capítulo, vamos aprender a “pintar”.

#### 1. A ideia do SwiftUI: declarativo, não imperativo

O desenvolvimento de interface antigo é “imperativo”: você diz ao sistema “crie um botão > coloque em (20,30) > defina a cor”, dando ordens passo a passo. O SwiftUI é “declarativo”: você simplesmente descreve “na tela há um botão vermelho escrito ‘Toque aqui’”, e o sistema se vira sozinho para desenhar e redesenhar quando for preciso.

::: div .code-block
:::inline div .code-head
<span>SWIFT · Primeira view SwiftUI</span><span class="dots">···</span>
:::

```
import SwiftUI

struct ContentView: View {
    var body: some View {      // body: descreve "como a tela fica"
        VStack {               // empilhado na vertical
            Text("Olá, mundo!")
                .font(.largeTitle)      // modificador: título grande
            Button("Toque aqui") {
                print("clicado")
            }
            .buttonStyle(.borderedProminent)  // botão azul sólido
        }
        .padding()
    }
}
```
:::

Ponto-chave: uma view é uma struct que adota o protocolo View, a propriedade body descreve a interface e os .modificadores() se encadeiam como “maquiagem”. Esse é todo o alicerce do SwiftUI.

#### 2. Views básicas: texto, botão, campo de texto e imagem

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">View</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Para que serve</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Exemplo</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mostrar texto</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text("Olá")</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Botão</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button("Toque aqui") { ação }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Campo de texto</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField("Dica", text: $texto)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Image</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mostrar imagem</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Image(systemName: "star.fill")</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
As quatro views básicas do SwiftUI

Repare no Image(systemName:) — a Apple inclui a biblioteca de ícones SF Symbols (milhares de ícones gratuitos): um nome como “star.fill” já exibe uma estrela preenchida na hora. É um benefício escondido do desenvolvimento iOS: para montar interfaces, quase não é preciso procurar ícones.

#### 3. O trio de layout: VStack, HStack e ZStack

- VStack: organiza na vertical (como uma fila do bandejão);
- HStack: organiza na horizontal (como gente sentada lado a lado);
- ZStack: empilha (como cartas de baralho umas sobre as outras, ótimo para selos e sobreposições).

::: div .code-block
:::inline div .code-head
<span>SWIFT · O trio de layouts + modificadores comuns</span><span class="dots">···</span>
:::

```
VStack(alignment: .leading, spacing: 12) {
    HStack {
        Text("Conta")
        Spacer()                 // espaço elástico: empurra a direita até o fim
        Text("-25.5 yuan").foregroundColor(.red)
    }
    Divider()                    // divisor
    Text("Obs.: almoço")
}
.padding(16)                     // espaço nas bordas
.background(Color(.systemGray6)) // fundo cinza claro
.cornerRadius(12)                // cantos arredondados

// A ordem dos modificadores importa: padding primeiro, depois background — o fundo não inclui o espaço
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Atenção: a ordem dos modificadores importa

{class="mt-1"}
padding(16).background(cinza) e background(cinza).padding(16) dão resultados diferentes — o primeiro “deixa o espaço e depois pinta” (o fundo não inclui a margem), o segundo “pinta e depois deixa o espaço” (o fundo inclui a margem). Daí vêm as “bordas brancas estranhas” que tanto atormentam iniciantes. Na dúvida, inverta a ordem: a pré-visualização responde na hora.
:::

#### 4. Estado e binding: dando vida à interface

Interface estática não tem graça. A regra do SwiftUI: a interface reflete fielmente o estado, e quando o estado muda, ela se redesenha sozinha.

::: div .code-block
:::inline div .code-head
<span>SWIFT · Um contador com @State</span><span class="dots">···</span>
:::

```
struct CounterView: View {
    @State private var count = 0   // @State: se esse valor muda, redesenha

    var body: some View {
        VStack {
            Text("Você tocou \(count) vezes")
            Button("Toque +1") {
                count += 1          // muda o estado; a tela atualiza sozinha
            }
        }
    }
}
```
:::

O campo de texto usa “binding bidirecional” — o símbolo $ entrega junto o valor e o poder de alterá-lo:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Vínculo bidirecional com @Binding</span><span class="dots">···</span>
:::

```
struct InputView: View {
    @State private var text = ""

    var body: some View {
        TextField("Digite algo", text: $text)  // $ vínculo bidirecional
            .textFieldStyle(.roundedBorder)
        Text("Você digitou: \(text)")   // atualiza em tempo real
    }
}
```
:::

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hand-pointer mr-1"></i> Ação do usuário</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> O estado muda (count += 1)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> O SwiftUI percebe a mudança</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> A tela redesenha sozinha (body recalculado)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figura 3: o fluxo de dados unidirecional “estado → interface” do SwiftUI
:::

#### 5. Prévia, tema e animação: os “cheats” do SwiftUI

- Macro #Preview: adicione #Preview { ContentView() } no fim do arquivo e o canvas à direita renderiza em tempo real — editar vendo o resultado na hora;
- Modo escuro de graça: use cores do sistema (Color(.systemGray6), .primary) em vez de cores fixas e o modo escuro se adapta sozinho, sem uma linha a mais;
- Animação em uma linha: withAnimation { count += 1 } ou .animation(.default, value: count) na view — transições sedosas.

::: div .code-block
:::inline div .code-head
<span>SWIFT · Animações em dez minutos</span><span class="dots">···</span>
:::

```
struct AnimatedHeartView: View {
    @State private var liked = false

    var body: some View {
        Button {
            withAnimation(.spring(duration: 0.4)) {
                liked.toggle()
            }
        } label: {
            Image(systemName: liked ? "heart.fill" : "heart")
                .font(.system(size: 48))
                .foregroundColor(liked ? .red : .gray)
                .scaleEffect(liked ? 1.3 : 1.0)
        }
    }
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Dica: primeiro a função, depois a animação

{class="mt-1"}
O defeito clássico do iniciante é “ainda não ter acertado a interface e já ficar remoendo a animação”. Faça a função funcionar primeiro e deixe os efeitos para o final — animação é enfeite no bolo pronto; função é remédio na hora da dor. É também o nosso princípio de sempre: simplicidade acima de tudo.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mãos à obra: crie um “botão do humor”

#### 6. Consulta rápida dos modificadores mais usados: com esta página, a interface se resolve

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">O que você quer fazer</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Modificador</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Espaçamento</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.padding(16)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cantos arredondados</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.cornerRadius(12)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cor de fundo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.background(Color(.systemGray6))</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Fonte e tamanho</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.font(.title.bold())</code> / <code class="inline">.font(.system(size: 20))</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cor de primeiro plano (texto/ícone)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.foregroundColor(.red)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ocupar toda a largura</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.frame(maxWidth: .infinity)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tamanho fixo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.frame(width:100, height: 44)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Alinhamento</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">VStack(alignment: .leading)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Transparência</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.opacity(0.6)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sombra</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.shadow(radius: 5)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gesto de toque</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.onTapGesture { ... }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tipo de teclado</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.keyboardType(.decimalPad)</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Consulta rápida dos modificadores mais usados do SwiftUI

Se não decorar tudo, sem problema — esta página existe para consulta. Na prática, os quatro primeiros são os mais usados: padding, cantos arredondados, fundo e fonte.

{class="mt-1"}
Transforme o projeto modelo em um alternador de humor: um botão que, a cada toque, cicla entre 😀 feliz → 😢 triste → 😡 bravo, com o texto e a cor de fundo mudando junto. Dica: guarde os três pares (texto + cor) em um array, o índice em um @State e, ao tocar, use (index + 1) % 3. Mande para os amigos testarem e colha a primeira leva de “uau, você faz apps!”.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumo do capítulo

- O SwiftUI é declarativo: você descreve “como deve ficar”, e o sistema desenha e redesenha
- View = struct que adota o protocolo View; o body descreve a interface; os modificadores se encadeiam como “maquiagem”
- As quatro views básicas: Text / Button / TextField / Image; a biblioteca SF Symbols dá ícones de graça e de montão
- O trio de layout: VStack empilha na vertical, HStack na horizontal, ZStack em camadas; o Spacer é o espaço elástico
- @State dá vida à interface; o $ faz o binding bidirecional que alimenta o campo de texto
- #Preview mostra o resultado na hora; as cores do sistema se adaptam ao modo escuro sozinhas; withAnimation dá o efeito em uma linha
:::
