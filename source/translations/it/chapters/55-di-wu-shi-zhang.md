---
id: di-wu-shi-zhang
num: 50
part: an-zhuo-kai-fa-pian
nav: Capitolo 50: Kotlin al volo — Il primo linguaggio dello sviluppo Android
toc: default
kind: chapter
---

### Capitolo 50: Kotlin a guida rapida — il primo linguaggio dello sviluppo Android

{class="chapter-intro mb-4"}
In questo capitolo iniziamo davvero con il linguaggio. Niente ansia — Kotlin è famoso per essere «amichevole con i principianti», e non devi imparare a memoria la grammatica: padroneggiando il 20% della sintassi capisci e scrivi l'80% del codice di ogni giorno. Il resto lo cercherai man mano che fai i progetti. Ricorda il nostro principio di studio: capire > memorizzare, saper usare > essere perfetti.

#### 1. Variabili e tipi: dare un nome ai dati

Un programma è «dati + logica». La variabile è il nome che diamo ai dati per conservarli. In Kotlin si dichiara in due modi:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Variabili</span><span class="dots">···</span>
:::

```
val name = Marco        // val: variabile di sola lettura (il consigliato per default)
var age = 18             // var: variabile mutabile (si può cambiare dopo)

age = 19                 // <i class="fas fa-check-circle mr-1"></i> var si può cambiare
// name = "Anna"         // <i class="fas fa-times-circle mr-1"></i> val non si può cambiare: errore di compilazione

val score: Int = 100     // puoi anche dichiarare il tipo esplicitamente
val pi = 3.14            // se lo ometti viene dedotto automaticamente
```
:::

I tipi più usati sono pochi: con una tabella li ricordi tutti:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Tipo</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Cosa contiene</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Esempio</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Int</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Numeri interi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">42</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Double</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Numeri decimali</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3.14</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">String</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Testo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">«Ciao»</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Boolean</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Vero/falso</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">true / false</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">List&lt; T&gt;</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Un insieme di dati</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">listOf(1, 2, 3)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
I tipi base più usati di Kotlin

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Consiglio: il principio «val prima di tutto»

{class="mt-1"}
La regola d'oro della community Kotlin: per impostazione predefinita usa val, e var solo se serve davvero. Se usi var dove basterebbe val, l'IDE ti segnala in giallo. Questa abitudine ti risparmia tutta una famiglia di bug «variabile modificata per sbaglio» — meno cose cambiano nel codice, più è facile ragionarci.
:::

#### 2. Le funzioni: la logica impacchettata in «pulsanti»

Una funzione è un pezzo di logica con un nome, come un pulsante del telecomando — lo premi (la chiami) e parte una serie di azioni. In Kotlin si dichiara con fun:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Funzioni</span><span class="dots">···</span>
:::

```
fun greet(name: String): String {
    return "Ciao, $name!"     // il simbolo $ inserisce la variabile nella stringa
}

println(greet(Marco))        // stampa: Ciao, Marco!

// le funzioni di una riga si possono scrivere come espressioni
fun add(a: Int, b: Int) = a + b

println(add(3, 5))            // stampa: 8
```
:::

Qualche punto chiave: i parametri vanno tra parentesi (prima il nome, poi il tipo, separati dai due punti); il tipo di ritorno va dopo le parentesi; il template di stringa $nomeVariabile è la comodità di punta di Kotlin — niente più incastri alla Java tra «stringa + variabile».

#### 3. Condizioni e cicli: far «pensare» il programma

L'intelligenza di un programma nasce da due cose: saper decidere (if/when) e saper ripetere (for/while).

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Condizioni e cicli</span><span class="dots">···</span>
:::

```
// Decisioni: if / else
val age = 17
if (age >= 18) {
    println("maggiorenne")
} else {
    println("minorenne")
}

// Multi-ramo: when (cento volte più comodo di switch)
val score = 85
val level = when {
    score >= 90 -> "ottimo"
    score >= 60 -> "sufficiente"
    else -> "Continua così!"
}

// Ripetizione: un ciclo for
val fruits = listOf("mela", "banana", "arancia")
for (fruit in fruits) {
    println("Mi piace la $fruit")
}
```
:::

when è la costruzione a più rami più usata in Kotlin: nello sviluppo Android la userai ogni giorno (per esempio per mostrare interfacce diverse a seconda dello stato).

#### 4. La null safety: l'«amuleto salvavita» di Kotlin

Il bug più celebre dell'era Java si chiama NullPointerException (eccezione di puntatore nullo) — il programma tocca qualcosa che «non c'è» e va subito in crash. Secondo le statistiche è da sempre primo nella classifica dei crash di Android. Kotlin lo risolve a livello di linguaggio: per impostazione predefinita i valori nulli non sono ammessi.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Null safety</span><span class="dots">···</span>
:::

```
var name: String = "Marco"   // tipo normale: non può mai essere null
// name = null                // <i class="fas fa-times-circle mr-1"></i> errore di compilazione — ti blocca subito

var nickname: String? = null // aggiungi un punto di domanda: null consentito
nickname = "Nino"

// Con i tipi nullable devi gestirli in sicurezza:
println(nickname?.length)    // chiamata sicura: restituisce null invece di crashare
val len = nickname?.length ?: 0   // operatore Elvis: valore predefinito se null
println(len)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Attenzione: non confondere ? e ?:

{class="mt-1"}
String? significa «può essere nullo», a ?: b significa «se a è nullo usa b» (assomiglia alla pettinatura di Elvis, per questo si chiama operatore Elvis). Quando inizi a scrivere codice e il compilatore ti segnala «errori legati a null», nel 90% dei casi hai dimenticato di gestire un tipo nullable — è proprio il linguaggio che ti sta proteggendo.
:::

#### 5. Classi e oggetti: gli stampi per fabbricare «pezzi»

La classe è lo «stampo» degli oggetti, l'oggetto è il «prodotto finito» della classe. In Android tutto — schermate, pulsanti, dati — è un oggetto. In Kotlin c'è un'arma segreta chiamata data class (classe di dati), fatta apposta per «contenere dati»: una riga vale decine di righe di Java:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Classi e data class</span><span class="dots">···</span>
:::

```
// Classe normale: uno stampo
class Dog(val name: String) {
    fun bark() = println("$name: Bau!")
}

val dog = Dog("Fido")      // crea un oggetto
dog.bark()                 // Fido: Bau!

// data class: una scatola per dati (con equals/copy incluse)
data class User(val id: Int, val name: String, val email: String)

val me = User(1, Marco, "zhangsan@example.com")
val twin = me.copy(name = "Marco Rossi")   // copia e cambia un campo
```
:::

Quando farai il registro delle spese, ogni voce sarà una data class: data class Record(val amount: Double, val category: String, val date: String). Visto? Sei già capace di scrivere la struttura di codice di un progetto vero.

#### 6. Lambda e funzioni di ordine superiore: lo «zucchero sintattico» di Kotlin

Nel codice Android vedrai ogni giorno «funzioni senza nome» come { ... }: si chiamano lambda (funzioni anonime). onClick = { count++ } su un Button è una lambda — impacchetta «cosa fare al tocco» in un blocco e lo consegna al pulsante.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Primo assaggio di lambda</span><span class="dots">···</span>
:::

```
// Modo classico: definisci una funzione con nome e passala
fun double(x: Int) = x * 2
val result = listOf(1, 2, 3).map(::double)

// Colle lambda: definita al volo, snella e diretta
val result2 = listOf(1, 2, 3).map { it * 2 }   // it = elemento corrente

// Combinazione filtro + trasformazione (frequentissima nei progetti reali)
val bills = listOf(12.5, 88.0, 5.0, 200.0)
val bigBills = bills.filter { it > 50 }.sorted()
// [88.0, 200.0] — "fatture oltre 50, ordinate"
```
:::

Segna qualche «combo» ad alta frequenza sulle collezioni: filter (filtra), map (trasforma), sorted (ordina), sum (somma). Il 90% dei lavori sulle liste che farai è una combinazione di queste quattro mosse. La filosofia di Kotlin è: se una logica si spiega in una frase, non scriverla mai in cinque.

#### 7. La scheda di sintassi rapida per chi parte da zero

Non provare a imparare tutta la sintassi in un giorno. Salva questa scheda, consultala mentre scrivi codice e tra due settimane ti verrà naturale:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Cosa vuoi fare</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Come si scrive</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Definire una variabile di sola lettura</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">val x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Definire una variabile modificabile</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">var x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Definire una funzione</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">fun nome(parametri): TipoRitorno { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Decidere</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if (condizione) {...} else {...}</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Scelte multiple</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">when { condizione -> risultato }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Scorrere</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">for (x in lista) { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Unire le stringhe</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"Ciao, $name"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gestire i valori nulli</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">x?.length ?: 0</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Definire una data class</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">data class X(val a: Int, val b: String)</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Scheda di sintassi rapida Kotlin (versione principianti)

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mani all'opera: gioca 10 minuti con Kotlin senza installare nulla

{class="mt-1"}
Apri nel browser play.kotlinlang.org (il playground ufficiale online di Kotlin), incolla e fai girare ogni pezzo di codice di questo capitolo, cambia numeri e testi e guarda come cambia l'output. Questi 10 minuti di «prima si gioca, poi si studia» ti renderanno il capitolo 51 due volte più facile.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Riepilogo del capitolo

- val prima di tutto, var con cautela; i tipi si deducono da soli, ma puoi dichiararli esplicitamente dopo i due punti
- Funzione = logica impacchettata; il template di stringa $ è la comodità di punta
- if/when per decidere, for per ciclare; when è il «tuttofare» dello sviluppo Android
- La null safety è il salvavita di Kotlin: i tipi normali rifiutano null, quelli nullable vanno gestiti con ? / ?:
- La data class è una scatola per i dati, un campo per riga: nei progetti veri si usa ogni giorno
- Il 20% della sintassi fa l'80% del lavoro: prima impari a usarlo, poi diventi esperto
:::
