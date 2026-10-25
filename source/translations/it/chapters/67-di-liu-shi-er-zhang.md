---
id: di-liu-shi-er-zhang
num: 62
part: ios-kai-fa-pian
nav: Capitolo 62: Sviluppare l'interfaccia — Introduzione a SwiftUI
toc: default
kind: chapter
---

### Capitolo 62: Sviluppare l'interfaccia — introduzione a SwiftUI

{class="chapter-intro mb-4"}
L'interfaccia è tutto ciò che l'utente vede. SwiftUI è il framework dichiarativo presentato da Apple nel 2019: ti basta "dichiarare" come deve apparire l'interfaccia e il sistema si occupa da solo di disegnarla, adattarla alla modalità scura e ai vari schermi. Nel 2026 SwiftUI è ormai lo standard assoluto dei nuovi progetti. In questo capitolo impariamo a "disegnare".

#### 1. L'idea di SwiftUI: dichiarativo, non imperativo

Lo sviluppo delle interfacce all'antica è "imperativo": dici al sistema "crea il pulsante → mettilo a (20,30) → imposta il colore", una istruzione alla volta. SwiftUI è "dichiarativo": descrivi direttamente "sull'interfaccia c'è un pulsante rosso con scritto 'Toccami'", e come disegnarlo e quando ridisegnarlo se lo pensa il sistema.

::: div .code-block
:::inline div .code-head
<span>SWIFT · La prima view SwiftUI</span><span class="dots">···</span>
:::

```
import SwiftUI

struct ContentView: View {
    var body: some View {      // body: descrive "come appare lo schermo"
        VStack {               // disposizione verticale
            Text("Ciao, mondo!")
                .font(.largeTitle)      // modificatore: titolo grande
            Button("Toccami") {
                print("cliccato")
            }
            .buttonStyle(.borderedProminent)  // pulsante blu pieno
        }
        .padding()
    }
}
```
:::

Punti chiave: una vista è uno struct conforme al protocollo View, la proprietà body descrive l'interfaccia, e i .modificatori() si concatenano a catena come una "truccatura". Questo è tutto il fondamento di SwiftUI.

#### 2. Le viste di base: testo, pulsanti, campi di input, immagini

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Vista</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">A cosa serve</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Esempio</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mostrare testo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text("Ciao")</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pulsante</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button("Toccami") { azione }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Campo di input</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField("Segnaposto", text: $testo)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Image</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mostrare un'immagine</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Image(systemName: "star.fill")</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Le quattro viste fondamentali di SwiftUI

Nota bene Image(systemName:): Apple include la libreria di icone SF Symbols (migliaia di icone gratuite) e basta un nome come "star.fill" per mostrare all'istante una stella piena. È un vantaggio nascosto dello sviluppo iOS: per costruire interfacce quasi non serve cercare materiale grafico.

#### 3. Il trio del layout: VStack, HStack e ZStack

- VStack: dispone in verticale (come la fila alla mensa);
- HStack: dispone in orizzontale (come sedersi fianco a fianco);
- ZStack: sovrappone (come carte da gioco impilate, ideale per badge e coperture).

::: div .code-block
:::inline div .code-head
<span>SWIFT · I tre stack di layout + modificatori comuni</span><span class="dots">···</span>
:::

```
VStack(alignment: .leading, spacing: 12) {
    HStack {
        Text("Conto")
        Spacer()                 // spazio elastico: spinge la parte destra al bordo
        Text("-25.5 yuan").foregroundColor(.red)
    }
    Divider()                    // divisore
    Text("Nota: pranzo")
}
.padding(16)                     // margine su tutti i lati
.background(Color(.systemGray6)) // sfondo grigio chiaro
.cornerRadius(12)                // angoli arrotondati

// L'ordine dei modificatori conta: prima padding poi background, lo sfondo non include il margine
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Attenzione: l'ordine dei modificatori conta

{class="mt-1"}
padding(16).background(grigio) e background(grigio).padding(16) danno risultati diversi: nel primo caso "prima lo spazio, poi il colore" (lo sfondo non include i margini), nel secondo "prima il colore, poi lo spazio" (lo sfondo include i margini). Da qui nasce il "bordo bianco misterioso" più comune tra i principianti. Se hai dubbi, scambia l'ordine: l'anteprima ti dà subito la risposta.
:::

#### 4. Stato e binding: far "vivere" l'interfaccia

Un'interfaccia statica è noiosa. La regola di SwiftUI: l'interfaccia rispecchia sempre fedelmente lo stato; quando lo stato cambia, l'interfaccia si ridisegna da sola.

::: div .code-block
:::inline div .code-head
<span>SWIFT · Um contador com @State</span><span class="dots">···</span>
:::

```
struct CounterView: View {
    @State private var count = 0   // @State: se questo valore cambia, ridisegna

    var body: some View {
        VStack {
            Text("Hai toccato \(count) volte")
            Button("Toccami +1") {
                count += 1          // cambia lo stato; l'interfaccia si aggiorna da sola
            }
        }
    }
}
```
:::

I campi di input usano il "binding bidirezionale": il simbolo $ passa insieme "il valore e il diritto di modificarlo":

::: div .code-block
:::inline div .code-head
<span>SWIFT · Binding bidirezionale con @Binding</span><span class="dots">···</span>
:::

```
struct InputView: View {
    @State private var text = ""

    var body: some View {
        TextField("Scrivi qualcosa", text: $text)  // $ binding bidirezionale
            .textFieldStyle(.roundedBorder)
        Text("Hai digitato: \(text)")   // si aggiorna in tempo reale
    }
}
```
:::

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hand-pointer mr-1"></i> Azione dell'utente</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> Lo stato cambia (count += 1)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> SwiftUI rileva il cambiamento</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> L'interfaccia si ridisegna da sola (body ricalcolato)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figura 3: il flusso di dati a senso unico "stato → interfaccia" di SwiftUI
:::

#### 5. Anteprime, tema e animazioni: i "potenziamenti" di SwiftUI

- La macro #Preview: aggiungi in fondo al file #Preview { ContentView() } e il canvas a destra esegue il rendering in tempo reale: modifichi il codice e vedi subito l'effetto;
- Modalità scura gratis: usa i colori di sistema (Color(.systemGray6), .primary) invece dei colori fissi e l'adattamento alla modalità scura avviene da solo, senza scrivere una riga in più;
- Animazioni in una riga: withAnimation { count += 1 } oppure aggiungi .animation(.default, value: count) alla vista: transizioni scorrevoli al punto giusto.

::: div .code-block
:::inline div .code-head
<span>SWIFT · Animazioni in dieci minuti</span><span class="dots">···</span>
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
Consiglio: prima le funzioni, poi le animazioni

{class="mt-1"}
Il difetto tipico dei principianti è "mettersi a dibattere le animazioni prima che l'interfaccia sia giusta". Fai prima funzionare tutto e aggiungi gli effetti alla fine, in un colpo solo: l'animazione è la ciliegina sulla torta, la funzione è il pane quotidiano. È anche il nostro principio di sempre: "la semplicità prima di tutto".
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mettiti alla prova: crea un "pulsante dell'umore"

#### 6. Scheda rapida dei modificatori più usati: una pagina a portata di mano e l'interfaccia non è più un problema

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Cosa vuoi ottenere</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Modificatore</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Spaziatura</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.padding(16)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Angoli arrotondati</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.cornerRadius(12)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Colore di sfondo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.background(Color(.systemGray6))</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Carattere e corpo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.font(.title.bold())</code> / <code class="inline">.font(.system(size: 20))</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Colore in primo piano (testo/icone)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.foregroundColor(.red)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Riempi la larghezza</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.frame(maxWidth: .infinity)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Dimensione fissa</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.frame(width:100, height: 44)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Allineamento</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">VStack(alignment: .leading)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Trasparenza</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.opacity(0.6)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ombra</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.shadow(radius: 5)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gesto di tocco</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.onTapGesture { ... }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tipo di tastiera</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.keyboardType(.decimalPad)</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Scheda rapida dei modificatori più usati di SwiftUI

Se non li ricordi non importa: questa pagina serve proprio da consultazione. In realtà i più usati sono i primi quattro: padding, angoli arrotondati, sfondo e carattere.

{class="mt-1"}
Trasforma il progetto modello in un selettore d'umore: un pulsante che a ogni tocco cicla tra 😀 felice → 😢 triste → 😡 arrabbiato, con testo e colore di sfondo che cambiano di conseguenza. Suggerimento: salva in un array le tre coppie (testo+colore), tieni l'indice in un @State e al tocco usa (index + 1) % 3. A lavoro finito mandalo agli amici e raccogli la prima ondata di "Wow, sai creare app!".
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Riepilogo del capitolo

- SwiftUI è dichiarativo: descrivi "come deve apparire" e il sistema si occupa di disegnare e ridisegnare
- Vista = uno struct conforme al protocollo View; body descrive l'interfaccia; i modificatori si concatenano come un "trucco"
- Le quattro viste di base: Text / Button / TextField / Image; la libreria di icone SF Symbols è gratuita e in abbondanza
- Il trio del layout: VStack in verticale, HStack in orizzontale, ZStack in sovrapposizione; Spacer è lo spazio elastico
- @State dà vita all'interfaccia; il $ del binding bidirezionale alimenta i campi di input
- #Preview fa vedere subito il risultato; i colori di sistema si adattano da soli alla modalità scura; withAnimation aggiunge effetti in una riga
:::
