---
id: di-liu-shi-yi-zhang
num: 61
part: ios-kai-fa-pian
nav: Capítulo 61: Swift em ritmo acelerado — a primeira linguagem do desenvolvimento Apple
toc: default
kind: chapter
---

### Capítulo 61: Swift em ritmo acelerado — a primeira linguagem do desenvolvimento Apple

{class="chapter-intro mb-4"}
Neste capítulo vamos finalmente estudar a linguagem. Sem pânico — o Swift é famoso por ser “amigável com iniciantes”, e você não precisa decorar um livro de sintaxe: dominando 20% da gramática, você já entende e escreve 80% do código do dia a dia. O resto, você consulta conforme os projetos avançam. Lembre do nosso princípio de aprendizado: entender > decorar, saber usar > ser mestre.

#### 1. Variáveis e tipos: dando nomes aos dados

Um programa é “dados + lógica”. Variável é dar um nome aos dados e guardá-los. No Swift, usamos let e var para declarar:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Variáveis</span><span class="dots">···</span>
:::

```
let name = "João"        // let: constante (o padrão recomendado)
var age = 18             // var: variável (pode mudar depois)

age = 19                 // <i class="fas fa-check-circle mr-1"></i> var pode mudar
// name = "Maria"         // <i class="fas fa-times-circle mr-1"></i> let não pode mudar: erro de compilação

let score: Int = 100     // também é possível declarar o tipo explicitamente
let pi = 3.14            // se omitir, é inferido automaticamente

print("Olá, \(name)")   // interpolação de string: barra invertida + parênteses
```
:::

Decore os tipos mais usados com uma tabela:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Tipo</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Guarda o quê</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Exemplo</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Int</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Número inteiro</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">42</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Double</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Número decimal</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3.14</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">String</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Texto</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">“Olá”</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bool</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Verdadeiro/falso</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">true / false</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">[Int] (array)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Um conjunto de dados</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">[1, 2, 3]</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Tipos básicos mais usados do Swift

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Dica: a regra do “let primeiro”

{class="mt-1"}
Regra de ferro da comunidade Swift: use let por padrão e só recorra ao var quando for realmente necessário. Se você usar var onde daria para usar let, o Xcode avisa com um alerta amarelo. Esse hábito elimina toda uma família de bugs de “variável alterada sem querer” — quanto menos o código muda, mais fácil raciocinar sobre ele.
:::

#### 2. Opcionais (Optional): o amuleto anticrash do Swift

Este é o conceito mais importante do Swift, sem concorrência. Em uma frase: quando um valor pode “não existir”, o Swift te obriga a lidar com isso — eliminando, no nível da linguagem, o pesadelo da indústria chamado “crash de ponteiro nulo”.

::: div .code-block
:::inline div .code-head
<span>SWIFT · Opcionais</span><span class="dots">···</span>
:::

```
var name: String = "João"   // tipo comum: nunca pode ser nil
// name = nil                // <i class="fas fa-times-circle mr-1"></i> erro de compilação — te barra direto

var nickname: String? = nil  // adicione um ponto de interrogação: nil permitido (opcional)
nickname = "Zé"

// Para usar um opcional, é preciso fazer o "unwrap":
if let n = nickname {        // if let: unwrap seguro
    print("Olá, \(n)")
} else {
    print("Ainda sem apelido")
}

let len = nickname?.count ?? 0   // ?? fornece valor padrão (operador de coalescência)
print(len)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Atenção: o ! é uma “operação de alto risco”

{class="mt-1"}
Escrever nickname! no código (desempacotamento forçado) é como gritar para o compilador “eu garanto que não é nil” — se você errar, o app trava na hora. Princípio para iniciantes: prefira sempre if let / ?? e evite o !. Às vezes o autocomplete do Xcode adiciona um ! sem cerimônia; lembre de trocá-lo.
:::

#### 3. Funções e closures: empacotando a lógica em “botões”

Uma função é um trecho de lógica com nome, como um botão do controle remoto. Já a closure é uma “função sem nome”, que você pode passar adiante a qualquer momento:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Funções e closures</span><span class="dots">···</span>
:::

```
// Funções: nome primeiro, parâmetros e tipo de retorno depois
func greet(name: String) -> String {
    return "Olá, \(name)!"
}
print(greet(name: "João"))     // na chamada é preciso o nome do parâmetro

// Closures: definidas na hora, leves e diretas
let numbers = [1, 2, 3, 4]
let doubled = numbers.map { $0 * 2 }   // $0 = elemento atual
// [2, 4, 6, 8]

let big = numbers.filter { $0 > 2 }    // filtro
// [3, 4]
```
:::

No SwiftUI, closures estão em toda parte: as chaves depois de Button("Toque aqui") { ... } formam uma closure. Grave bem os “golpes combinados” de coleções map, filter e sorted — no futuro, 90% do processamento de listas será combinação deles.

#### 4. Structs e protocolos: o sistema de “blocos de montar” do Swift

A preferência oficial do Swift é clara: use struct primeiro e recorra à class apenas quando precisar de herança. Structs são “tipos de valor” — ao copiar, cada um segue seu caminho, o que naturalmente elimina uma família de bugs:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Structs e protocolos</span><span class="dots">···</span>
:::

```
// A struct: uma caixa para dados
struct Record {
    var id = UUID()
    var amount: Double
    var category: String
    var date: Date

    // Structs já vêm com o "memberwise initializer": dá para criar direto
}
let r = Record(amount: 25.5, category: "Alimentação", date: Date())

// O protocolo: um contrato de "quais habilidades são exigidas"
protocol Identifiable {
    var id: UUID { get }
}
struct Record: Identifiable { ... }   // conformar-se a um protocolo = prometer cumprir seus requisitos
```
:::

No SwiftUI, quase tudo é struct (View é um protocolo). Se isso não ficou claro agora, sem problema: você vai se deparar com isso todos os dias no Capítulo 62 — no mundo do Swift, abrace o struct primeiro.

#### 5. Cartão de consulta rápida da sintaxe, escrito para quem parte do zero

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">O que fazer</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Como escrever</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Definir constante/variável</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">let x = 1</code> / <code class="inline">var x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Interpolação de strings</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"Olá, \(name)"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Definir função</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">func nome(parâmetro: Tipo) -> TipoDeRetorno { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Condicional</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if condição { ... } else { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Percorrer</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">for x in array { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Desempacotamento seguro</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if let x = opcional { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Valor padrão</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">x ?? valorPadrão</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Definir struct</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">struct X { var a: Int; var b: String }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Closure</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">{ $0 * 2 }</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Cartão de consulta rápida da sintaxe Swift (edição iniciante)

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mãos à obra: brinque 15 minutos com Swift no Playgrounds

{class="mt-1"}
Se você tem Mac, abra o Xcode > Playground; se não tem, use o Swift Playgrounds no iPad ou o playground na versão web. Rode cada trecho de código deste capítulo, mude números e textos e provoque alguns erros de propósito para ver como o Xcode avisa. Esses 15 minutos de “brincar primeiro, estudar depois” vão deixar o Capítulo 62 duas vezes mais fácil.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumo do capítulo

- Prefira let e use var com parcimônia; os tipos são inferidos automaticamente, mas dá para declarar explicitamente depois dos dois-pontos
- Opcional é a alma do Swift: se pode estar vazio, precisa ser tratado; if let / ?? são o amuleto, e ! é operação de alto risco
- Na chamada de funções, inclua os nomes dos parâmetros; closure = função sem nome, onipresente no SwiftUI
- Prefira struct e adote protocolos (Protocol); no SwiftUI, quase tudo é struct
- 20% da sintaxe resolve 80% do trabalho: primeiro aprenda a usar, depois busque a maestria
:::
