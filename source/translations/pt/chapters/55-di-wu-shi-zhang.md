---
id: di-wu-shi-zhang
num: 50
part: an-zhuo-kai-fa-pian
nav: Capítulo 50: Kotlin em ritmo acelerado — a primeira linguagem do desenvolvimento Android
toc: default
kind: chapter
---

### Capítulo 50: Kotlin em ritmo acelerado — a primeira linguagem do desenvolvimento Android

{class="chapter-intro mb-4"}
Neste capítulo vamos estudar a linguagem de verdade. Sem medo — o Kotlin é famoso por ser "amigável para iniciantes" e você não precisa decorar a gramática: dominando 20% da sintaxe, você já entende e escreve 80% do código do dia a dia. O resto você consulta enquanto desenvolve o projeto. Lembre do nosso princípio de estudo: entender > decorar, saber usar > ser perfeito.

#### 1. Variáveis e tipos: dando nome aos dados

Um programa é "dados + lógica". Variável é dar um nome aos dados para guardá-los. Em Kotlin há duas formas de declarar:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Variáveis</span><span class="dots">···</span>
:::

```
val name = João        // val: variável somente leitura (o padrão recomendado)
var age = 18             // var: variável mutável (pode mudar depois)

age = 19                 // <i class="fas fa-check-circle mr-1"></i> var pode mudar
// name = "Maria"         // <i class="fas fa-times-circle mr-1"></i> val não pode mudar: erro de compilação

val score: Int = 100     // também é possível declarar o tipo explicitamente
val pi = 3.14            // se omitir, é inferido automaticamente
```
:::

Os tipos mais usados são poucos; memorize com uma tabela:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Tipo</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">O que guarda</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Exemplo</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Int</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Números inteiros</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">42</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Double</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Números decimais</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3.14</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">String</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Texto</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"Olá"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Boolean</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Verdadeiro/falso</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">true / false</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">List&lt; T&gt;</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Um conjunto de dados</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">listOf(1, 2, 3)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Tipos básicos mais usados do Kotlin

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Dica: o princípio do val primeiro

{class="mt-1"}
A regra de ferro da comunidade Kotlin: por padrão use val e só use var quando realmente for necessário. Se usar var onde daria val, o IDE avisa com texto amarelo. Esse hábito elimina uma grande família de bugs de "variável alterada sem querer" — quanto menos o código muda, mais fácil raciocinar sobre ele.
:::

#### 2. Funções: empacotando a lógica em "botões"

Uma função é um trecho de lógica com nome, como um botão do controle remoto — aperta (chama), e uma sequência de ações acontece. Em Kotlin, declaramos com fun:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Funções</span><span class="dots">···</span>
:::

```
fun greet(name: String): String {
    return "Olá, $name!"     // o símbolo $ insere a variável na string
}

println(greet(João))        // imprime: Olá, João!

// funções de uma linha podem ser escritas como expressões
fun add(a: Int, b: Int) = a + b

println(add(3, 5))            // imprime: 8
```
:::

Alguns pontos-chave: os parâmetros ficam entre parênteses (nome primeiro, tipo depois, separados por dois-pontos); o tipo de retorno vem depois dos parênteses; e o template de string $nomeDaVariavel é a conveniência marca registrada do Kotlin — sem precisar concatenar "string + variável" como no Java.

#### 3. Condicionais e laços: ensinando o programa a "pensar"

A inteligência de um programa vem de duas coisas: saber decidir (if/when) e saber repetir (for/while).

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Condições e loops</span><span class="dots">···</span>
:::

```
// Decisão: if / else
val age = 17
if (age >= 18) {
    println("adulto")
} else {
    println("menor de idade")
}

// Multiramo: when (cem vezes mais prático que switch)
val score = 85
val level = when {
    score >= 90 -> "excelente"
    score >= 60 -> "na média"
    else -> "Continue assim!"
}

// Repetição: um loop for
val fruits = listOf("maçã", "banana", "laranja")
for (fruit in fruits) {
    println("Eu gosto de $fruit")
}
```
:::

O when é a forma mais usada de múltiplas escolhas em Kotlin; no desenvolvimento Android você vai usá-lo todos os dias (por exemplo, para mostrar telas diferentes conforme o estado).

#### 4. Segurança contra nulos: o "amuleto de proteção" do Kotlin

O bug mais famoso da era Java chama-se NullPointerException (exceção de ponteiro nulo) — o programa acessa algo "que não existe" e trava na hora. Nas estatísticas, ele lidera constantemente o ranking de travamentos do Android. O Kotlin resolveu isso no nível da linguagem: por padrão, valores nulos não são permitidos.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Segurança contra nulos</span><span class="dots">···</span>
:::

```
var name: String = "João"   // tipo comum: nunca pode ser null
// name = null                // <i class="fas fa-times-circle mr-1"></i> erro de compilação — te barra na hora

var nickname: String? = null // adicione um ponto de interrogação: null permitido
nickname = "Zé"

// Com tipos anuláveis, é preciso tratar com segurança:
println(nickname?.length)    // chamada segura: retorna null em vez de travar
val len = nickname?.length ?: 0   // operador Elvis: valor padrão quando null
println(len)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Atenção: não confunda ? e ?:

{class="mt-1"}
String? significa "pode ser nulo"; a ?: b significa "se a for nulo, use b" (o símbolo lembra o cabelo do Elvis, por isso se chama operador Elvis). No começo, quando o compilador reclamar de "erro relacionado a null", quase certamente foi você quem esqueceu de tratar um tipo anulável — é justamente a linguagem te protegendo.
:::

#### 5. Classes e objetos: o molde que fabrica "peças"

A classe é o "molde" do objeto, e o objeto é o "produto pronto" da classe. Tudo no Android — telas, botões, dados — é um objeto. O Kotlin tem uma joia chamada data class (classe de dados), feita sob medida para "guardar dados": uma linha vale dezenas em Java:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Classes e data classes</span><span class="dots">···</span>
:::

```
// Classe comum: um molde
class Dog(val name: String) {
    fun bark() = println("$name: Au au!")
}

val dog = Dog("Rex")      // cria um objeto
dog.bark()                 // Rex: Au au!

// data class: uma caixa para dados (com equals/copy automáticos)
data class User(val id: Int, val name: String, val email: String)

val me = User(1, João, "zhangsan@example.com")
val twin = me.copy(name = "Joãozinho")   // copia e muda um campo
```
:::

Quando você for fazer o seu aplicativo de controle de gastos, cada lançamento será uma data class: data class Record(val amount: Double, val category: String, val date: String). Viu? Você já consegue escrever a estrutura de código de um projeto real.

#### 6. Lambdas e funções de alta ordem: o "açúcar sintático" do Kotlin

No código Android você verá todos os dias funções "sem nome" como { ... }; elas se chamam lambdas (funções anônimas). O onClick = { count++ } de um Button é um lambda — empacota "o que fazer ao clicar" num pacote só e entrega ao botão.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Primeira experiência com lambda</span><span class="dots">···</span>
:::

```
// Jeito comum: definir uma função com nome e passar
fun double(x: Int) = x * 2
val result = listOf(1, 2, 3).map(::double)

// Com lambda: definida na hora, leve e direta
val result2 = listOf(1, 2, 3).map { it * 2 }   // it = elemento atual

// Combinação filtro + transformação (comum demais em projetos reais)
val bills = listOf(12.5, 88.0, 5.0, 200.0)
val bigBills = bills.filter { it > 50 }.sorted()
// [88.0, 200.0] — "contas acima de 50, ordenadas"
```
:::

Guarde alguns "combos de coleção" muito usados: filter (filtrar), map (transformar), sorted (ordenar) e sum (somar). Nos próximos tempos, 90% do processamento de listas será combinação dessas quatro jogadas. A filosofia do Kotlin é: se a lógica cabe em uma frase, jamais escreva cinco.

#### 7. Cartão de consulta rápida da sintaxe para quem parte do zero

Não tente decorar toda a sintaxe num dia. Salve este cartão, consulte-o enquanto programa e, em duas semanas, a familiaridade vem naturalmente:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">O que você quer fazer</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Como se escreve</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Definir variável somente leitura</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">val x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Definir variável mutável</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">var x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Definir função</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">fun nome(parâmetros): tipoDeRetorno { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Decisão</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if (condição) {...} else {...}</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Múltiplas escolhas</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">when { condição -> resultado }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Percorrer</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">for (x in lista) { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Concatenação de strings</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"Olá, $name"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tratar nulos</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">x?.length ?: 0</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Definir data class</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">data class X(val a: Int, val b: String)</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Cartão de consulta rápida da sintaxe Kotlin (edição iniciante)

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mão na massa: jogue 10 minutos de Kotlin sem instalar nada

{class="mt-1"}
Abra play.kotlinlang.org no navegador (o playground oficial online do Kotlin), cole e rode cada trecho de código deste capítulo, mude números e textos e observe como a saída muda. Esses 10 minutos de "brincar antes de estudar" vão deixar o início do Capítulo 51 duas vezes mais leve.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumo do capítulo

- val primeiro, var com cautela; o tipo pode ser inferido automaticamente, ou declarado explicitamente depois dos dois-pontos
- Função = lógica empacotada; o template de string com $ é a conveniência da casa
- if/when para decisões, for para laços; o when é o "coringa" do desenvolvimento Android
- A segurança contra nulos é o amuleto do Kotlin: tipos comuns recusam null; tipos anuláveis exigem tratamento com ? / ?:
- A data class é a caixa que guarda dados, um campo por linha, usada todos os dias em projetos reais
- 20% da sintaxe fazem 80% do trabalho: primeiro saiba usar, depois busque a maestria
:::
