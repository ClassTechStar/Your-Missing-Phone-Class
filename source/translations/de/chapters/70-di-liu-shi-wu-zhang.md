---
id: di-liu-shi-wu-zhang
num: 65
part: ios-kai-fa-pian
nav: Kapitel 65: Projekt 1 – mein Haushaltsbuch (Lokalversion)
toc: default
kind: chapter
---

### Kapitel 65: Projekt 1 – Mein Haushaltsbuch (Lokalversion)

{class="chapter-intro mb-4"}
Willkommen bei deinem ersten „richtigen Projekt“. Dieses Haushaltsbuch kommt zwar ohne Netz aus, ist aber komplett ausgestattet: Buchungen erfassen, Verlauf ansehen, monatliche Auswertung, Löschen und Ändern. Wenn du fertig bist, hast du den kompletten Ablauf „Daten → Logik → Oberfläche“ einmal durchlaufen. Wilde nicht gleich den Code ab – erst durchdenken, dann anpacken; das ist unser bewährtes Prinzip.

#### 1. Anforderungen überdenken: erst fünf Fragen stellen

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Element</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Antwort</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who (für wen?)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Für dich selbst; Familie und Freunde gehen auch</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What (was?)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Einnahmen/Ausgaben erfassen, Verlauf ansehen, Monatsbilanz, Auswertung nach Kategorien</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why (warum?)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Übung + herausfinden, wohin das Geld geht</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How (wie?)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift + SwiftUI + SwiftData + MVVM, rein lokal ohne Backend</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint (Randbedingungen)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">In einer Woche fertig; mindestens iOS 17 (SwiftData-Voraussetzung)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Die fünf Anforderungselemente des Haushaltsbuchs

Dann zerlegst du das Ganze in kleine Schritte, nach denen jeweils etwas Benutzbares entsteht: 1) die SwiftData-Datenschicht bauen (eine Buchung speichern können); 2) die Listenseite (Verlauf ansehen); 3) den Eingabe-Dialog (Buchung hinzufügen); 4) Löschen und Bearbeiten; 5) die Monatsbilanz-Karte. Nach jedem erledigten Schritt ist die App ein „brauchbares Ding“.

#### 2. Die Datenschicht: den „Buchungen“ ein Zuhause geben

Definiere zuerst, wie eine Buchung aussieht – die Felder sollen ausreichen, aber nicht gierig sein:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Record.swift (Modell)</span><span class="dots">···</span>
:::

```
import SwiftData

@Model
class Record {
    var type: String      // "income" Einnahme | "expense" Ausgabe
    var amount: Double    // Betrag (Yuan)
    var category: String  // Kategorie: Essen, Verkehr, Gehalt …
    var note: String      // Notiz (optional)
    var date: Date        // Buchungsdatum

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
Tipp: Warum Double für den Betrag?

{class="mt-1"}
Seröse Finanz-Apps verwenden Decimal (exakte Dezimalzahlen), um Rundungsfehler bei Gleitkommazahlen zu vermeiden (das alte Problem, dass 0,1 + 0,2 ≠ 0,3). Für ein Übungsprojekt reicht Double völlig; baust du eines Tages ein echtes Finanzprodukt, denk an den Wechsel zu Decimal oder ein „Int in Cent“ – eine Falle, in die unzählige Vorgänger getappt sind.
:::

#### 3. MVVM: Oberfläche und Logik „ziehen getrennte Wege“

Die Oberfläche direkt auf die Datenbank zugreifen lassen? Läuft zwar, aber der Oberflächencode wird lang und unappetitlich. Die MVVM-Architektur sorgt für klare Zuständigkeit: View (Oberfläche) zeichnet nur, ViewModel (Logikzentrale) kümmert sich um die Daten, Model (SwiftData) um die Speicherung.

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> View (SwiftUI-Oberfläche)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> ViewModel (@Observable als Logik-Zentrale)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-database mr-1"></i> Model (Datenlayer mit SwiftData)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Abbildung 4: Die drei Ebenen von MVVM – Daten fließen nur in eine Richtung, und keine Ebene greift einer anderen ins Handwerk
:::

::: div .code-block
:::inline div .code-head
<span>SWIFT · RecordViewModel.swift (Grundgerüst)</span><span class="dots">···</span>
:::

```
import Observation

@Observable
class RecordViewModel {
    var records: [Record] = []
    private let context: ModelContext

    init(context: ModelContext) { self.context = context }

    func load() {
        // Filtern mit #Predicate von SwiftData + Sortierung
        let descriptor = FetchDescriptor<Record>(
            sortBy: [SortDescriptor(\.date, order: .reverse)]
        )
        records = (try? context.fetch(descriptor)) ?? []
    }

    func add(type: String, amount: Double, category: String, note: String) {
        let r = Record(type: type, amount: amount, category: category, note: note)
        context.insert(r)
        try? context.save()
        load()                       // neu laden; die Oberfläche aktualisiert sich
    }

    func delete(_ record: Record) {
        context.delete(record)
        try? context.save()
        load()
    }
}
```
:::

In der Oberfläche @State private var vm = RecordViewModel(...) anlegen und die Liste direkt aus vm.records rendern – ändern sich die Daten, aktualisiert sich die Oberfläche automatisch.

#### 4. Die Oberfläche: Listenseite + Eingabe-Dialog

::: div .code-block
:::inline div .code-head
<span>SWIFT · Ausgabenlisten-Ansicht (Kernauszug)</span><span class="dots">···</span>
:::

```
struct RecordListView: View {
    @State private var vm: RecordViewModel
    @State private var showAdd = false

    var body: some View {
        NavigationStack {
            List {
                Section("Saldo des Monats") {          // Zusammenfassungs-Karte
                    SummaryRow(records: vm.records)
                }
                Section("Umsätze") {
                    ForEach(vm.records) { r in
                        RecordRow(record: r)
                    }
                    .onDelete { idx in
                        idx.forEach { vm.delete(vm.records[$0]) }
                    }
                }
            }
            .navigationTitle("Mein Ausgabenbuch")
            .toolbar {
                Button { showAdd = true } label: {
                    Image(systemName: "plus")
                }
            }
            .sheet(isPresented: $showAdd) {
                AddRecordView(vm: vm)          // Eingabedialog
            }
        }
    }
}
```
:::

Wichtige Punkte für den Eingabe-Dialog: für das Betragsfeld .keyboardType(.decimalPad) (Zifferntastatur) verwenden, für Einnahmen/Ausgaben ein segmentiertes Steuerelement (Picker), die Kategorie über ein Menü wählen, und bei „Speichern“ vm.add(...) aufrufen und den Dialog mit dismiss() schließen.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Achtung: Bei der Eingabeprüfung nicht faulenzen

{class="mt-1"}
Das Betragsfeld musst du unbedingt prüfen: Leere Werte, negative Zahlen und unzulässige Eingaben wie "abc" müssen abgefangen werden (mit Double(text) prüfen; im Fehlerfall kommt nil zurück). Einer der häufigsten Gründe für App-Abstürze ist, „die Eingaben der Nutzer für brav zu halten“. Denk dran: Alles, was Nutzer eingeben, musst du wie einen Gegner unter die Lupe nehmen.
:::

#### 5. Bearbeiten, Löschen und Bilanz

- Löschen: .onDelete in List fürs Löschen per Linkswischen + Bestätigungsdialog (versehentliches Löschen ist das, was Nutzer von Buchhaltungs-Apps am meisten hassen);
- Bearbeiten: ein Tipp auf die Zeile öffnet den Bearbeitungsdialog mit vorausgefüllten Originalwerten (ein Wort ändern ist bequemer als alles neu eintippen);
- Bilanz: mit filter + reduce „Einnahmen / Ausgaben / Saldo des Monats“ berechnen und oben in einer Karte anzeigen:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Monatszusammenfassung berechnen</span><span class="dots">···</span>
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

#### 6. Abnahme: Prüfung auf drei Ebenen + zwei Zusatzaufgaben für Fortgeschrittene

Nach Fertigstellung prüfst du das Projekt auf drei Ebenen entlang von „Funktion → Grenzfälle → Architektur“: Lässt sich erfassen, lässt sich löschen, sind die Daten nach einem Neustart noch da (Funktion)? Stürzt die App ab, wenn du 0 oder negative Beträge eingibst (Grenzfälle)? Sind Oberfläche und Daten vermischt, sind Felder fest einprogrammiert (Architektur)?

Nach bestandener Abnahme der Basisversion gönnst du dir zwei „Fortgeschrittenen-Gerichte“:

1. Kategorien-Auswertung: Ergänze einen „Statistik“-Reiter und zeichne mit Swift Charts die Ausgaben je Kategorie als Kreis-/Balkendiagramm – Apples offizielle Diagrammbibliothek, mit wenigen Codezeilen zum fertigen Chart;
2. iCloud-Sync: Für iCloud-Synchronisation mit SwiftData genügen ein paar Einstellungen – das Haushaltsbuch synct automatisch zwischen iPhone und iPad, und auf einen Schlag wirkt alles „profihaft“.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Jetzt bist du dran: diese Woche fertigstellen

{class="mt-1"}
Arbeite in der Reihenfolge „Datenschicht → ViewModel → Listenseite → Eingabe-Dialog → Bilanz-Karte“, jeden Tag ein Schritt. Wenn du hängst, wirf die Fehlermeldung wortwörtlich einer Suchmaschine oder einer KI hin (erinnerst du dich an Teil 7, „KI-Programmierung in der Praxis“? Beschreibe beim Schildern des Problems klar „erwartetes Verhalten, tatsächliches Verhalten, Schritte zur Reproduktion“). Wenn du fertig bist, führe damit eine Woche lang dein Haushaltsbuch – eine selbst gebaute App zu benutzen gibt ein Erfolgserlebnis, das dich weiter antreibt.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Kapitelfazit

- Fünf Anforderungselemente → in kleine Schritte zerlegen, nach denen jeweils etwas Benutzbares entsteht, dann loslegen
- Datenschicht: @Model-Modell + modelContainer-Container + FetchDescriptor-Abfragen
- MVVM-Arbeitsteilung: View zeichnet nur, das @Observable-ViewModel kümmert sich um die Logik, SwiftData um die Speicherung
- Oberfläche: List + Section + toolbar + sheet als Eingabe-Dialog
- Abnahme auf drei Ebenen (Funktion/Grenzfälle/Architektur) + Zusatzaufgaben (Swift Charts, iCloud-Sync)
:::
