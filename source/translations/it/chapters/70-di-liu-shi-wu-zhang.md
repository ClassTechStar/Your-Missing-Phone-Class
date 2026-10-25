---
id: di-liu-shi-wu-zhang
num: 65
part: ios-kai-fa-pian
nav: Capitolo 65: Progetto 1 — Il mio registro delle spese (versione locale)
toc: default
kind: chapter
---

### Capitolo 65: Progetto 1 — il mio registro delle spese (versione locale)

{class="chapter-intro mb-4"}
Benvenuto nel tuo primo "progetto serio". Questo registro delle spese, pur senza connessione alla rete, ha tutto il necessario: registrare una voce, consultare i movimenti, statistiche mensili, eliminare e modificare. Portandolo a termine avrai percorso per intero il flusso "dati → logica → interfaccia". Non avere fretta di copiare il codice: pensa prima con chiarezza, poi agisci; è il nostro principio di sempre.

#### 1. Riflettere sui requisiti: poni prima cinque domande

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Elemento</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Risposta</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who (per chi è)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Per te; va bene anche per famiglia e amici</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What (cosa fa)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Registrare entrate e uscite, consultare i movimenti, riepiloghi mensili, statistiche per categoria</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why (perché)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Fare pratica + capire dove finiscono i soldi</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How (come)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift + SwiftUI + SwiftData + MVVM, tutto in locale senza backend</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint (vincoli)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Completarlo in una settimana; iOS 17 come minimo (soglia di SwiftData)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
I cinque elementi dei requisiti del registro delle spese

Poi scomponi il lavoro in piccoli passi "utili fin da subito": ① creare il livello dati con SwiftData (salvare una voce); ② la pagina elenco (vedere i movimenti); ③ la finestra di inserimento (aggiungere una voce); ④ eliminazione e modifica; ⑤ la card del riepilogo mensile. A ogni passo completato l'app resta una "cosa utilizzabile".

#### 2. Il livello dati: dare una casa alle "voci"

Prima definisci come è fatta una voce di conto — servono campi sufficienti, ma senza esagerare:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Record.swift (modello)</span><span class="dots">···</span>
:::

```
import SwiftData

@Model
class Record {
    var type: String      // "income" entrata | "expense" uscita
    var amount: Double    // importo (in yuan)
    var category: String  // categoria: pasti, trasporti, stipendio…
    var note: String      // nota (facoltativa)
    var date: Date        // data della voce

    init(type: String, amount: Double, category: String, note: String = "", date: Date = Date()) {
        self.type = type
        self.amount = amount
        self.category = category
        self.note = note
        self.date = date
    }
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Consiglio: perché l'importo è un Double?

{class="mt-1"}
Le app finanziarie rigorose usano Decimal (decimale esatto) per evitare gli errori di virgola mobile (il vecchio problema 0.1+0.2≠0.3). Per un progetto di allenamento Double basta e avanza; se un giorno realizzassi un vero prodotto finanziario, ricordati di passare a Decimal o a un "Int in centesimi": è una trappola che innumerevoli colleghi hanno già pagato.
:::

#### 3. MVVM: interfaccia e logica "dividono le stanze"

Far agire il database direttamente dall'interfaccia? Funziona, ma il codice dell'interfaccia diventa lungo e impossibile da mantenere. L'architettura MVVM assegna a ciascuno il suo compito: View (l'interfaccia) si occupa solo di disegnare, ViewModel (il centro della logica) gestisce i dati, Model (SwiftData) si occupa dell'archiviazione.

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> View (interfaccia SwiftUI)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> ViewModel (il centro logico @Observable)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-database mr-1"></i> Model (livello dati SwiftData)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figura 4: la struttura a tre livelli di MVVM — i dati fluiscono a senso unico e nessun livello invade il campo degli altri
:::

::: div .code-block
:::inline div .code-head
<span>SWIFT · RecordViewModel.swift (scheletro)</span><span class="dots">···</span>
:::

```
import Observation

@Observable
class RecordViewModel {
    var records: [Record] = []
    private let context: ModelContext

    init(context: ModelContext) { self.context = context }

    func load() {
        // filtro + ordinamento con #Predicate di SwiftData
        let descriptor = FetchDescriptor<Record>(
            sortBy: [SortDescriptor(\.date, order: .reverse)]
        )
        records = (try? context.fetch(descriptor)) ?? []
    }

    func add(type: String, amount: Double, category: String, note: String) {
        let r = Record(type: type, amount: amount, category: category, note: note)
        context.insert(r)
        try? context.save()
        load()                       // ricarica; l'interfaccia si aggiorna
    }

    func delete(_ record: Record) {
        context.delete(record)
        try? context.save()
        load()
    }
}
```
:::

Nell'interfaccia scrivi @State private var vm = RecordViewModel(...) e poi renderizzi l'elenco direttamente con vm.records: appena i dati cambiano, l'interfaccia si aggiorna da sola.

#### 4. L'interfaccia: pagina elenco + finestra di inserimento

::: div .code-block
:::inline div .code-head
<span>SWIFT · Schermata elenco spese (brano essenziale)</span><span class="dots">···</span>
:::

```
struct RecordListView: View {
    @State private var vm: RecordViewModel
    @State private var showAdd = false

    var body: some View {
        NavigationStack {
            List {
                Section("Bilancio del mese") {          // card riepilogo
                    SummaryRow(records: vm.records)
                }
                Section("Movimenti") {
                    ForEach(vm.records) { r in
                        RecordRow(record: r)
                    }
                    .onDelete { idx in
                        idx.forEach { vm.delete(vm.records[$0]) }
                    }
                }
            }
            .navigationTitle("Il mio registro spese")
            .toolbar {
                Button { showAdd = true } label: {
                    Image(systemName: "plus")
                }
            }
            .sheet(isPresented: $showAdd) {
                AddRecordView(vm: vm)          // finestra di inserimento
            }
        }
    }
}
```
:::

Punti chiave della finestra di inserimento: per il campo dell'importo usa la tastiera .keyboardType(.decimalPad) (tastiera numerica), per entrata/uscita un controllo a segmenti (Picker), per la categoria una scelta a menu; al tocco di "Salva" chiama vm.add(...) e chiude la finestra con dismiss().

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Attenzione: non lesinare sulla validazione dell'input

{class="mt-1"}
Il campo dell'importo va sempre validato: blocca valori vuoti, negativi e input illegali tipo "abc" (usa Double(text): se fallisce restituisce nil). Una delle cause più comuni di app che crashano è "prendere l'input dell'utente per un bambino buono". Ricorda: tutto ciò che l'utente digita va esaminato come un nemico.
:::

#### 5. Modifica, eliminazione e riepilogo

- Eliminazione: .onDelete di List cancella con uno scorrimento a sinistra + finestra di conferma (l'eliminazione per sbaglio è ciò che gli utenti delle app di contabilità detestano di più);
- Modifica: toccando la riga si apre la finestra di modifica con i valori originali già compilati (correggere una parola è più comodo che ridigitare tutto);
- Riepilogo: calcola "entrate / uscite / saldo del mese" con filter + reduce e mostrali in una card in alto:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Calcolo dei totali mensili</span><span class="dots">···</span>
:::

```
func monthSummary(_ records: [Record]) -> (income: Double, expense: Double) {
    let cal = Calendar.current
    let monthRecords = records.filter {
        cal.isDate($0.date, equalTo: Date(), toGranularity: .month)
    }
    let income = monthRecords
        .filter { $0.type == "income" }
        .reduce(0) { $0 + $1.amount }
    let expense = monthRecords
        .filter { $0.type == "expense" }
        .reduce(0) { $0 + $1.amount }
    return (income, expense)
}
```
:::

#### 6. Collaudo: tre livelli di controllo + due sfide avanzate

A progetto finito, collaudalo su tre livelli "funzioni → casi limite → architettura": si riesce a registrare? si può eliminare? i dati sopravvivono al riavvio dell'app (funzioni); l'app crasha se l'importo è 0 o negativo (casi limite); interfaccia e dati sono mescolati? ci sono campi scritti a mano nel codice (architettura)?

Superato il collaudo della versione base, aggiungiti due "portate avanzate":

1. Statistiche per categoria: aggiungi una scheda "Statistiche" e disegna le uscite per categoria come grafico a torta/a barre con Swift Charts — la libreria grafica ufficiale di Apple fa grafici con poche righe di codice;
2. Sincronizzazione iCloud: attivare la sincronizzazione iCloud in SwiftData richiede solo qualche impostazione — il registro si sincronizza da solo tra iPhone e iPad e all'improvviso sembra "professionale".

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mettiti alla prova: completalo questa settimana

{class="mt-1"}
Lavora nell'ordine "livello dati → ViewModel → pagina elenco → finestra di inserimento → card di riepilogo", un passo al giorno. Se ti blocchi, getta l'errore così com'è a un motore di ricerca o a un'IA (ti ricordi la Parte 7, "Programmazione pratica con l'IA"? Quando descrivi un problema indica con chiarezza "comportamento atteso, comportamento reale, passi per riprodurlo"). Una volta finito, usalo per tenere le spese di una settimana: usare un'app fatta da te ti darà una spinta ad andare avanti.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Riepilogo del capitolo

- Cinque elementi dei requisiti → scomposti in piccoli passi "utili a ogni passo", poi si agisce
- Livello dati: modello @Model + contenitore modelContainer + query con FetchDescriptor
- Divisione MVVM: View disegna soltanto, il ViewModel @Observable gestisce la logica, SwiftData gestisce l'archiviazione
- Interfaccia: List + Section + toolbar + sheet per la finestra di inserimento
- Collaudo a tre livelli (funzioni/casi limite/architettura) + sfide avanzate (Swift Charts, sincronizzazione iCloud)
:::
