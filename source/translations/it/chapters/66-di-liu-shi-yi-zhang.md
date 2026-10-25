---
id: di-liu-shi-yi-zhang
num: 61
part: ios-kai-fa-pian
nav: Capitolo 61: Swift al volo — Il primo linguaggio dello sviluppo Apple
toc: default
kind: chapter
---

### Capitolo 61: Swift in fretta — il primo linguaggio dello sviluppo Apple

{class="chapter-intro mb-4"}
In questo capitolo impariamo davvero il linguaggio. Niente timore — Swift è famoso per essere «amichevole coi principianti» e non serve imparare a mente il manuale di sintassi: prendendo il 20% della grammatica, leggi e scrivi l'80% del codice quotidiano. Il resto lo cerchi mentre costruisci i progetti. Ricorda il nostro principio di studio: capire > memorizzare, saper usare > padroneggiare.

#### 1. Variabili e tipi: dare un nome ai dati

Un programma è «dati + logica». La variabile è un nome che dai ai dati per conservarli. Swift dichiara con let e var:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Variabili</span><span class="dots">···</span>
:::

```
let name = "Marco"        // let: costante (il consigliato per default)
var age = 18             // var: variabile (si può cambiare dopo)

age = 19                 // <i class="fas fa-check-circle mr-1"></i> var si può cambiare
// name = "Anna"         // <i class="fas fa-times-circle mr-1"></i> let non si può cambiare: errore di compilazione

let score: Int = 100     // puoi anche dichiarare il tipo esplicitamente
let pi = 3.14            // se lo ometti viene dedotto automaticamente

print("Ciao, \(name)")   // interpolazione di stringa: backslash + parentesi
```
:::

I tipi di uso quotidiano, da fissare con una tabella:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Tipo</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Cosa contiene</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Esempio</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Int</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Numero intero</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">42</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Double</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Numero decimale</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3.14</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">String</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Testo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"ciao"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bool</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Vero/falso</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">true / false</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">[Int] (array)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Un gruppo di dati</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">[1, 2, 3]</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
I tipi di base di uso quotidiano in Swift

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Consiglio: la regola «prima let»

{class="mt-1"}
La regola ferrea della community Swift: per default usa let, e ricorri a var solo quando serve davvero. Dove basterebbe let, se metti var Xcode ti avverte in giallo. Questa abitudine ti risparmia tutta una famiglia di bug da «variabile cambiata per sbaglio» — meno cose cambiano nel codice, più è facile ragionarci.
:::

#### 2. I valori opzionali (Optional): il «talismano anti-crash» di Swift

È il concetto più importante di Swift, e non c'è il secondo. In una frase: quando un valore può «non esserci», Swift ti obbliga a gestirlo — a livello di linguaggio fa sparire il «crash da puntatore nullo», l'incubo di tutto il mestiere.

::: div .code-block
:::inline div .code-head
<span>SWIFT · Opzionali</span><span class="dots">···</span>
:::

```
var name: String = "Marco"   // tipo normale: non può mai essere nil
// name = nil                // <i class="fas fa-times-circle mr-1"></i> errore di compilazione — ti blocca sul posto

var nickname: String? = nil  // aggiungi un punto di domanda: nil consentito (opzionale)
nickname = "Nino"

// Per usare un opzionale bisogna fare l'"unwrap":
if let n = nickname {        // if let: unwrap sicuro
    print("Ciao, \(n)")
} else {
    print("Ancora nessun nickname")
}

let len = nickname?.count ?? 0   // ?? fornisce un valore predefinito (operatore di coalescenza)
print(len)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Attenzione: ! è un'«operazione ad alto rischio»

{class="mt-1"}
Scrivere nel codice nickname! (unwrapping forzato) equivale a gridare al compilatore «ti garantisco che non è nil» — se sbagli il colpo, l'app crasha all'istante. Regola da principiante: per quanto possibile usa if let / ??, mai !. A volte Xcode, completando il codice, aggiunge un ! di sua iniziativa: ricorda di toglierlo.
:::

#### 3. Funzioni e closure: impacchettare la logica in "pulsanti"

Una funzione è un pezzo di logica con un nome, come un pulsante sul telecomando. Le closure invece sono "funzioni senza nome", che puoi passare a qualcuno al volo:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Funzioni e closure</span><span class="dots">···</span>
:::

```
// Funzioni: prima il nome, poi parametri e tipo di ritorno
func greet(name: String) -> String {
    return "Ciao, \(name)!"
}
print(greet(name: "Marco"))     // alla chiamata serve il nome del parametro

// Closure: definite al volo, snelle e dirette
let numbers = [1, 2, 3, 4]
let doubled = numbers.map { $0 * 2 }   // $0 = elemento corrente
// [2, 4, 6, 8]

let big = numbers.filter { $0 > 2 }    // filtro
// [3, 4]
```
:::

In SwiftUI le closure sono ovunque: le graffe dopo Button("Toccami") { ... } sono una closure. Impara a memoria le "combo delle collezioni" map, filter e sorted: nel futuro il 90% del lavoro con le liste sarà una loro combinazione.

#### 4. Struct e protocolli: il sistema "LEGO" di Swift

Le preferenze ufficiali di Swift sono chiare: prima gli struct, e le class solo quando serve l'ereditarietà. Gli struct sono "tipi valore": quando li copi, ognuno vive di vita propria, eliminando di natura tutta una categoria di bug:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Struct e protocolli</span><span class="dots">···</span>
:::

```
// La struct: una scatola per dati
struct Record {
    var id = UUID()
    var amount: Double
    var category: String
    var date: Date

    // Le struct hanno un "memberwise initializer" integrato: si creano subito
}
let r = Record(amount: 25.5, category: "Pasti", date: Date())

// Il protocollo: un patto su "quali capacità sono richieste"
protocol Identifiable {
    var id: UUID { get }
}
struct Record: Identifiable { ... }   // conformarsi a un protocollo = promettere di soddisfarne i requisiti
```
:::

In SwiftUI quasi tutto è uno struct (View è un protocollo). Se per ora non ti è chiaro, nessun problema: dal capitolo 62 ci ritroverai ogni giorno. Nel mondo di Swift, abbraccia subito gli struct.

#### 5. La scheda rapida di sintassi per chi parte da zero

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Cosa vuoi fare</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Come si scrive</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Definire una costante/variabile</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">let x = 1</code> / <code class="inline">var x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Interpolazione di stringhe</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"Ciao, \(name)"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Definire una funzione</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">func nome(parametro: Tipo) -> TipoRisultato { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Prendere decisioni</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if condizione { ... } else { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Iterare</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">for x in array { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Unwrapping sicuro</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if let x = valoreOpzionale { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Valore predefinito</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">x ?? valorePredefinito</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Definire uno struct</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">struct X { var a: Int; var b: String }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Closure</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">{ $0 * 2 }</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Scheda rapida della sintassi Swift (versione principianti)

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mettiti alla prova: gioca 15 minuti con Swift nei Playgrounds

{class="mt-1"}
Con un Mac apri Xcode → Playground; senza Mac usa Swift Playgrounds su iPad oppure l'arena di prova sul web. Esegui ogni blocco di codice di questo capitolo, cambia numeri e testi, provoca di proposito qualche errore e guarda come te lo segnala Xcode. Questi 15 minuti di "prima giocare, poi imparare" ti renderanno il capitolo 62 due volte più facile.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Riepilogo del capitolo

- Prima let, var con cautela; i tipi si deducono da soli, ma puoi anche dichiararli esplicitamente dopo i due punti
- Gli optional sono l'anima di Swift: ciò che può essere vuoto va gestito; if let e ?? sono il tuo amuleto, ! è un'operazione ad alto rischio
- Nelle chiamate di funzione va indicato il nome dei parametri; closure = funzione senza nome, presente ovunque in SwiftUI
- Prima gli struct, conformandosi ai protocolli; in SwiftUI quasi tutto è uno struct
- Il 20% della sintassi fa l'80% del lavoro: prima impara a usarla, poi perfezionala
:::
