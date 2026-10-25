---
id: di-wu-shi-yi-zhang
num: 51
part: an-zhuo-kai-fa-pian
nav: Capitolo 51: Sviluppare l'interfaccia — Introduzione a Jetpack Compose
toc: default
kind: chapter
---

### Capitolo 51: Sviluppare l'interfaccia — introduzione a Jetpack Compose

{class="chapter-intro mb-4"}
L'interfaccia è tutto ciò che l'utente vede. Prima che arrivasse Compose, le interfacce Android si scrivevano in XML — un grattacapo simile a un esercizio da riempire; nel 2021 Google ha lanciato Jetpack Compose: l'interfaccia si «disegna» direttamente in codice Kotlin, quello che vedi è quello che ottieni, cambi una riga e l'anteprima si aggiorna all'istante. Nel 2026 Compose è assolutamente lo standard dei nuovi progetti. In questo capitolo impariamo a «disegnare».

#### 1. L'idea di Compose: l'interfaccia è una funzione

L'idea centrale di Compose in una frase: interfaccia = funzione. Ogni cosa che può comparire sullo schermo (testo, pulsanti, immagini) è una «funzione componibile» (Composable), marcata con @Composable. Incastonandole l'una dentro l'altra come mattoncini si costruisce l'interfaccia.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Il primo schermo Compose</span><span class="dots">···</span>
:::

```
@Composable
fun Greeting(name: String) {
    Text(text = "Ciao, $name!")     // un "mattoncino di testo"
}

// Composizione annidata: mattoni grandi dentro mattoni piccoli
@Composable
fun HomeScreen() {
    Column {                          // disposizione verticale
        Greeting(name = Marco)
        Greeting(name = Anna)
        Button(onClick = { /* cosa fare al tocco */ }) {
            Text("Toccami")
        }
    }
}
```
:::

Occhio al «cappello» @Composable — dice al compilatore «questo è un mattoncino di interfaccia». I mattoncini si possono annidare all'infinito: questo è tutto il segreto di Compose.

#### 2. I componenti base: testo, pulsante, campo di input, immagine

I componenti di Compose sono «mattoncini»: i quattro più comuni sono:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Componente</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">A cosa serve</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Parametri obbligatori</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mostrare testo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">text (il testo da mostrare)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pulsante</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onClick (callback al tocco)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Campo di input</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">value, onValueChange (callback al cambiamento dell'input)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Image</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mostrare un'immagine</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">painter (risorsa grafica)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
I quattro componenti base di Compose

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Esempio di widget di base</span><span class="dots">···</span>
:::

```
@Composable
fun BasicWidgets() {
    Column {
        Text(text = "Questo è un testo")
        Button(onClick = { println("cliccato") }) {
            Text("Pulsante")
        }
        var input by remember { mutableStateOf("") }
        TextField(
            value = input,
            onValueChange = { input = it },
            label = { Text("Scrivi qualcosa") }
        )
    }
}
```
:::

Nelle due righe del campo di input compare remember { mutableStateOf("") } — è la magia dello «stato» di Compose, che approfondiremo nella sezione 5 di questo capitolo. Per ora basta prenderci confidenza.

#### 3. Il trio dei layout: Column, Row, Box

I componenti ci sono: come disporli? Ricorda tre «scatole»:

- Column: li mette in colonna (come la fila alla mensa);
- Row: li mette in riga (come sedersi uno accanto all'altro);
- Box: li sovrappone (come carte da gioco impilate, perfetto per badge e coperture).

::: div .code-block
:::inline div .code-head
<span>KOTLIN · I tre elementi di layout</span><span class="dots">···</span>
:::

```
Column {
    Text("Prima riga")
    Row {
        Text("Sinistra")
        Text("Destra")
    }
    Box {
        Text("Livello sotto")
        Text("Badge sovrapposto")
    }
}
```
:::

Vuoi un layout più bello? Aggiungi ai componenti un Modifier (modificatore) — è come truccare i mattoncini:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Mosse utili di Modifier</span><span class="dots">···</span>
:::

```
Text(
    text = "Testo carino",
    modifier = Modifier
        .padding(16.dp)          // margine su tutti i lati
        .fillMaxWidth()          // occupa tutta la larghezza
        .background(Color.Blue)  // colore di sfondo
        .clickable { /* tocco */ }// cliccabile
)
// Chiamate a catena: una dopo l'altra, l'ordine conta (prima padding poi background, lo sfondo non include il margine)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Attenzione: l'ordine dei Modifier ha il suo perché

{class="mt-1"}
padding(16.dp).background(Blue) e background(Blue).padding(16.dp) danno risultati diversi — la prima è «prima lo spazio, poi il colore» (lo sfondo non include il margine), la seconda è «prima il colore, poi lo spazio» (lo sfondo include il margine). È qui che i principianti più spesso si ritrovano con «bordi bianchi inspiegabili». Nel dubbio, scambia l'ordine e prova: l'anteprima ti dà subito la risposta.
:::

#### 4. Lo stato: far «vivere» l'interfaccia

Un'interfaccia statica non diverte nessuno. Per far sì che il pulsante aumenti il numero a ogni tocco e che nel campo di input si possa scrivere, serve lo stato (State). La regola di Compose: l'interfaccia riflette sempre fedelmente lo stato; cambia lo stato e l'interfaccia si ridisegna da sola.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Stato: contatore di tocchi</span><span class="dots">···</span>
:::

```
@Composable
fun Counter() {
    // remember + mutableStateOf: ricorda questo valore che cambia
    var count by remember { mutableStateOf(0) }

    Column {
        Text(text = "Hai toccato $count volte")
        Button(onClick = { count++ }) {   // cambia lo stato
            Text("Toccami +1")                // l'interfaccia si aggiorna da sola
        }
    }
}
```
:::

Tre righe di codice, e il contatore è vivo. È qui che Compose fa comodo rispetto al vecchio stile: non serve «aggiornare l'interfaccia» a mano, basta cambiare i dati. Ricorda due funzioni chiave: remember (fa sì che il valore non venga azzerato quando l'interfaccia si ricompone) e mutableStateOf (dice a Compose «questo valore è cambiato, ridisegna»).

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hand-pointer mr-1"></i> L'utente tocca</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> Lo stato cambia (count++)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> Compose rileva il cambiamento</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> L'interfaccia si ridisegna da sola (ricomposizione)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figura 3: il flusso di dati a senso unico «stato → interfaccia» di Compose
:::

#### 5. Tema e modalità scura: si configura una volta, vale ovunque

Nel progetto modello, MyFirstAppTheme { ... } è il tema. Si basa sulle specifiche di design di Material 3 e ti aiuta a gestire in modo unitario colori, font e forme. Per supportare la modalità scura bastano tre passi:

1. definisci nel tema entrambe le palette chiara/scura (il modello genera già da solo il ColorScheme);
2. quando il sistema passa alla modalità scura, isSystemInDarkTheme() lo rileva da solo;
3. usa i colori forniti dal tema (come MaterialTheme.colorScheme.primary) invece di scrivere valori di colore fissi.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Consiglio: i colori dinamici di Material 3

{class="mt-1"}
Da Android 12 in poi, «Material You» permette all'app di ricavare i colori dal tuo sfondo. I modelli Compose lo supportano già (dynamicColor). La tua app si «cambierà d'abito» da sola sul telefono di ogni utente: è il romanticismo dell'Android moderno.
:::

#### 6. Preview, animazioni e Live Edit: i «power-up» di Compose

Tre «power-up» di Compose per l'esperienza di sviluppo: una volta provati, non torni più indietro:

- L'anteprima @Preview: aggiungi l'annotazione @Preview a una Composable e Android Studio la renderizza subito a destra — vedi il risultato mentre scrivi il codice, senza installare ogni volta sul telefono;
- Live Edit: la versione 2026 di Android Studio supporta l'«hot update» di alcune modifiche su emulatore/dispositivo reale: ritocchi come cambiare il colore di un testo appaiono sul dispositivo in un batter d'occhio;
- Le API di animazione: animateFloatAsState, AnimatedVisibility — poche righe per far muovere gli elementi con dolcezza — spesso quella sensazione di «qualità alta» dipende proprio da una ventina di righe così.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Animazioni in dieci minuti</span><span class="dots">···</span>
:::

```
@Composable
fun AnimatedBox() {
    var big by remember { mutableStateOf(false) }
    // quando il valore cambia, transita dolcemente verso il target
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
Consiglio: prima le funzioni, poi le animazioni

{class="mt-1"}
Il difetto tipico dei principianti è «l'interfaccia non è ancora giusta e già si litiga sulle animazioni». Prima fai funzionare le cose, poi aggiungi le animazioni in un colpo solo — è anche il principio «la semplicità prima di tutto»: le animazioni sono la ciliegina sulla torta, le funzioni sono il pane quotidiano.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mani all'opera: crea un «pulsante dell'umore»

{class="mt-1"}
Trasforma il progetto modello in un cambio-umore: un pulsante che a ogni tocco cicla tra 😀 felice → 😢 triste → 😡 arrabbiato, con testo e colore di sfondo che seguono. Suggerimento: usa when per scegliere testi e colori in base allo stato. Quando hai finito, mandalo agli amici: raccoglierai il primo giro di «wow, sai fare le app!».
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Riepilogo del capitolo

- L'idea di Compose: interfaccia = funzione @Composable, annidata come mattoncini
- I quattro componenti base: Text / Button / TextField / Image
- Il trio dei layout: Column in colonna, Row in riga, Box sovrapposto
- Modifier a catena per «truccare»: padding, fillMaxWidth, background, clickable — l'ordine ha un significato
- Lo stato è l'anima: remember + mutableStateOf, cambi i dati e l'interfaccia si ridisegna da sola
- Tema con Material 3 + colori dinamici: la modalità scura si configura una volta e vale ovunque
:::
