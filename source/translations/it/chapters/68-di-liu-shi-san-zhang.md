---
id: di-liu-shi-san-zhang
num: 63
part: ios-kai-fa-pian
nav: Capitolo 63: View, stato e navigazione
toc: default
kind: chapter
---

### Capitolo 63: Viste, stato e navigazione

{class="chapter-intro mb-4"}
Sai già costruire i giocattoli a pagina singola. Questo capitolo risolve i due problemi della "crescita": come spostarsi tra più pagine (navigazione) e come fluiscono i dati tra le pagine (gestione dello stato). A fine capitolo saprai costruire lo scheletro classico di un'app multipagina: "elenco → dettaglio → modifica".

#### 1. Il "panorama del flusso di dati" della gestione dello stato

In SwiftUI @State non è l'unico strumento di stato. Guarda prima questo quadro d'insieme per capire "quando usare quale":

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Strumento</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Cosa gestisce</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Chi lo usa</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Scenario tipico</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@State</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Stato temporaneo privato della pagina</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">La vista corrente</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Un contatore, il testo di un campo di input</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Binding</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Prendere in prestito lo stato di altri</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Una vista figlia modifica quella padre</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Componenti personalizzati</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@StateObject / @Observable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Logica condivisa tra più pagine</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">View model (ViewModel)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Caricamento dei dati, logica di business</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@EnvironmentObject / .environment</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Stato condiviso a livello globale</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tutta l'app</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Stato di accesso dell'utente, impostazioni del tema</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Panorama degli strumenti di stato di SwiftUI (nel 2026 @Observable è già lo standard)

::: div .code-block
:::inline div .code-head
<span>SWIFT · Il mainstream 2026: view model con @Observable</span><span class="dots">···</span>
:::

```
// Il modo moderno su iOS 17+: la macro @Observable (consigliata per i nuovi progetti)
import Observation

@Observable
class CounterModel {                 // il view model
    var count = 0
    func increment() { count += 1 }
}

struct CounterView: View {
    @State private var model = CounterModel()   // contiene il modello

    var body: some View {
        VStack {
            Text("Hai toccato \(model.count) volte")
            Button("Toccami") { model.increment() }
        }
    }
}
```
:::

Il consiglio senza giri di parole per i principianti: @State per lo stato privato della pagina, classi @Observable per ciò che attraversa le pagine o contiene logica. @StateObject/@ObservableObject dei vecchi tutorial sono scritture di generazione precedente: basta saperli leggere; nel nuovo codice tieniti a quanto sopra.

#### 2. NavigationStack: la "pila" dei salti di pagina

Dall'iOS 16 in poi la navigazione tra più pagine usa NavigationStack: come una pila di piatti, ne metti uno sopra l'altro e tornando indietro li togli uno alla volta:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Navigazione con NavigationStack</span><span class="dots">···</span>
:::

```
struct HomeView: View {
    var body: some View {
        NavigationStack {
            List {
                NavigationLink("Il registro di Marco") {
                    DetailView(name: "Il registro di Marco")   // schermata di destinazione
                }
                NavigationLink("Il registro di Anna") {
                    DetailView(name: "Il registro di Anna")
                }
            }
            .navigationTitle("Elenco dei registri")   // titolo grande in alto
        }
    }
}

struct DetailView: View {
    let name: String
    var body: some View {
        Text("Dettagli di \(name)")
            .navigationTitle(name)
            .navigationBarTitleDisplayMode(.inline)
    }
}
```
:::

NavigationLink è il "collegamento cliccabile" verso un'altra pagina; navigationTitle genera da solo il titolo della barra di navigazione e il pulsante Indietro. Per la navigazione via codice (per esempio tornare indietro automaticamente dopo "Salva") usa @Environment(\.dismiss) per chiudere la pagina corrente: con questi due strumenti copri il 90% delle esigenze di navigazione.

#### 3. Finestre modali e schede in basso: sheet e TabView

Oltre "spingere le pagine" esistono due interazioni classiche:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Finestre sheet + schede TabView</span><span class="dots">···</span>
:::

```
// 1. Sale dal basso a mezza/full screen (il preferito per i form di inserimento)
struct HomeView: View {
    @State private var showAdd = false
    var body: some View {
        Button("Aggiungi voce") { showAdd = true }
            .sheet(isPresented: $showAdd) {
                AddRecordView()     // la finestra di inserimento
            }
    }
}

// 2. La barra delle schede in basso (lo "scheletro" dell'app)
struct MainTabView: View {
    var body: some View {
        TabView {
            RecordListView()
                .tabItem { Label("Registro", systemImage: "book") }
            StatsView()
                .tabItem { Label("Statistiche", systemImage: "chart.pie") }
            SettingsView()
                .tabItem { Label("Impostazioni", systemImage: "gear") }
        }
    }
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Consiglio: quando usare quale?

{class="mt-1"}
Regola pratica: il flusso principale si spinge con NavigationStack (elenco→dettaglio), le operazioni temporanee vanno in finestre sheet (aggiungere, modificare, confermare), i blocchi principali affiancati si organizzano con TabView (le schede in basso). Combinati insieme, sono lo scheletro della stragrande maggioranza delle app.
:::

#### 4. List: la lista "per tutti" di iOS

Il componente più usato e più "Apple" su iOS è List: offre di serie separatori, eliminazione con scorrimento ed evidenziazione al tocco:

::: div .code-block
:::inline div .code-head
<span>SWIFT · List + elimina con swipe</span><span class="dots">···</span>
:::

```
struct RecordListView: View {
    @State private var records = ["Pranzo 25.5", "Metro 6.0", "Stipendio +8000"]

    var body: some View {
        List {
            ForEach(records, id: \.self) { r in
                Text(r)
            }
            .onDelete { indexSet in          // swipe a sinistra per eliminare
                records.remove(atOffsets: indexSet)
            }
        }
    }
}
```
:::

Elenco + NavigationLink + sheet + TabView: combinando questi quattro elementi puoi già costruire lo scheletro completo di un'app: "elenco delle voci → aprire il dettaglio → toccare + e aprire l'inserimento". Il progetto registro delle spese del prossimo capitolo è costruito esattamente così.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mettiti alla prova: costruisci uno "scheletro a tre pagine"

#### 5. Il ciclo di vita dell'app: primo piano e sfondo

Come il ciclo di vita delle Activity su Android, anche un'app iOS attraversa stati come "nascita, primo piano, sfondo, morte". In SwiftUI li osservi con il valore d'ambiente scenePhase:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Osservare i passaggi primo piano/sfondo</span><span class="dots">···</span>
:::

```
@main
struct MyApp: App {
    @Environment(\.scenePhase) private var phase

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .onChange(of: phase) { _, newPhase in
            switch newPhase {
            case .active:    print("Di nuovo in primo piano, riprendo l'aggiornamento")
            case .inactive:  print("In transizione (chiamata / appena in background)")
            case .background: print("In background, salvo la bozza")
            @unknown default: break
            }
        }
    }
}
```
:::

Usi tipici: aggiornare i dati al ritorno in primo piano, salvare la bozza quando si passa in sfondo. iOS è molto severo sull'esecuzione in background: un'app normale appena va in sfondo viene presto sospesa (congelata), quindi non contare di fare lavori pesanti di nascosto; se ti serve davvero un'attività programmata, usa le notifiche locali del capitolo 68, non la "residenza permanente in background".

{class="mt-1"}
Costruisci la versione con dati fittizi dello scheletro del registro: una TabView con tre schede (registro/statistiche/impostazioni) → la pagina registro mostra i dati fittizi con List e toccando una riga si va al dettaglio (NavigationStack) → il pulsante "+" in alto a destra apre la sheet di inserimento. Niente salvataggi, niente rete: solo allenamento sullo scheletro. Con questo scheletro pronto, riempirlo di dati veri al capitolo 65 sarà un gioco.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Riepilogo del capitolo

- I quattro strumenti di stato: @State (privato della pagina), @Binding (in prestito), @Observable (logica), .environment (globale)
- Nei nuovi progetti scrivi i view model con la macro @Observable; di @ObservableObject dei vecchi tutorial basta saper leggere
- NavigationStack spinge le pagine; @Environment(\.dismiss) torna indietro via codice
- Flusso principale con pagine spinte, operazioni temporanee con sheet, blocchi affiancati con TabView
- List è la lista "per tutti": separatori ed eliminazione con scorrimento pronti all'uso
:::
