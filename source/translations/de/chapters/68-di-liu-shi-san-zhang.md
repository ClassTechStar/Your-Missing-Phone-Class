---
id: di-liu-shi-san-zhang
num: 63
part: ios-kai-fa-pian
nav: Kapitel 63: Views, State und Navigation
toc: default
kind: chapter
---

### Kapitel 63: Views, State und Navigation

{class="chapter-intro mb-4"}
Einseitige Spielereien kannst du bereits. Dieses Kapitel löst die zwei Fragen des „Erwachsenwerdens“: wie du zwischen mehreren Seiten hin- und herspringst (Navigation) und wie Daten zwischen den Seiten fließen (State-Management). Nach diesem Kapitel baust du das klassische Mehrseiten-Gerüst „Liste → Detail → Bearbeiten“.

#### 1. Das Datenfluss-Panorama des State-Managements

SwiftUI hat mehr als nur @State als State-Werkzeug. Sieh dir zuerst diese Übersicht an, um zu verstehen, „wann du welches einsetzt“:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Werkzeug</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Zuständig für</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Wer es nutzt</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Typischer Einsatzfall</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@State</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Seiteneigener, temporärer Zustand</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Das aktuelle View</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Zähler, Textfeldeingaben</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Binding</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Zustand von jemand anderem ausleihen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kind-View ändert Eltern-View</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Eigene Komponenten</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@StateObject / @Observable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Seitenübergreifend geteilte Logik</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ViewModel</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Datenladen, Geschäftslogik</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@EnvironmentObject / .environment</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Global geteilter Zustand</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Die ganze App</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Anmeldestatus, Theme-Einstellungen</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Überblick über SwiftUIs State-Werkzeuge (2026: @Observable ist längst Standard)

::: div .code-block
:::inline div .code-head
<span>SWIFT · Standard 2026: View Models mit @Observable</span><span class="dots">···</span>
:::

```
// der moderne Weg ab iOS 17+: das @Observable-Makro (für neue Projekte empfohlen)
import Observation

@Observable
class CounterModel {                 // das View Model
    var count = 0
    func increment() { count += 1 }
}

struct CounterView: View {
    @State private var model = CounterModel()   // hält das Modell

    var body: some View {
        VStack {
            Text("Du hast \(model.count) Mal geklickt")
            Button("Klick mich") { model.increment() }
        }
    }
}
```
:::

Knallharter Rat für Einsteiger: Seiteneigen → @State; seitenübergreifend oder mit Logik → @Observable-Klasse. @StateObject/@ObservableObject aus älteren Tutorials ist die Schreibweise der Vorgängergeneration – lesen können genügt, für neuen Code gilt das oben Gesagte.

#### 2. NavigationStack: der „Stapel“ für Seitenwechsel

Ab iOS 16 übernimmt NavigationStack die Mehrseiten-Navigation – wie ein Stapel Teller: einer kommt oben drauf, und beim Zurückgehen wird jeder einzeln wieder abgenommen:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Navigation mit NavigationStack</span><span class="dots">···</span>
:::

```
struct HomeView: View {
    var body: some View {
        NavigationStack {
            List {
                NavigationLink("Max' Ausgabenbuch") {
                    DetailView(name: "Max' Ausgabenbuch")   // Zielseite
                }
                NavigationLink("Lenas Ausgabenbuch") {
                    DetailView(name: "Lenas Ausgabenbuch")
                }
            }
            .navigationTitle("Liste der Ausgabenbücher")   // große Überschrift oben
        }
    }
}

struct DetailView: View {
    let name: String
    var body: some View {
        Text("Details zu \(name)")
            .navigationTitle(name)
            .navigationBarTitleDisplayMode(.inline)
    }
}
```
:::

NavigationLink ist schlicht ein „antippbarer Sprunglink“; navigationTitle erzeugt automatisch Navigationstitel und Zurück-Button. Für programmatisches Navigieren (etwa nach „Speichern“ automatisch zurück) schließt du die aktuelle Seite mit @Environment(\.dismiss) – mit dieser Kombination hast du 90 % aller Navigationsbedürfnisse abgedeckt.

#### 3. Dialoge und untere Reiter: sheet und TabView

Neben dem „Seitenschieben“ gibt es zwei klassische Interaktionsformen:

::: div .code-block
:::inline div .code-head
<span>SWIFT · sheet-Dialoge + Tabs mit TabView</span><span class="dots">···</span>
:::

```
// 1. Sheet von unten, halber oder ganzer Bildschirm (der Liebling von Eingabeformularen)
struct HomeView: View {
    @State private var showAdd = false
    var body: some View {
        Button("Ausgabe erfassen") { showAdd = true }
            .sheet(isPresented: $showAdd) {
                AddRecordView()     // die sich öffnende Erfassungsansicht
            }
    }
}

// 2. untere Tab-Leiste (das "Skelett" der App)
struct MainTabView: View {
    var body: some View {
        TabView {
            RecordListView()
                .tabItem { Label("Buch", systemImage: "book") }
            StatsView()
                .tabItem { Label("Statistik", systemImage: "chart.pie") }
            SettingsView()
                .tabItem { Label("Einstellungen", systemImage: "gear") }
        }
    }
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tipp: Wann nimmt man was?

{class="mt-1"}
Faustregel: Für den Hauptablauf Seiten mit NavigationStack schieben (Liste → Detail), für kurzzeitige Aktionen den sheet-Dialog (Anlegen, Bearbeiten, Bestätigen) und für gleichrangige Hauptbereiche TabView (untere Reiter). Die Kombination aus allen dreien ist das Gerüst der allermeisten Apps.
:::

#### 4. List: iOS' Alleskönner-Liste

Der meistgenutzte und am typischsten „apple-artige“ Baustein unter iOS ist List – mit Trennlinien, Wisch-löschen und Tipp-Highlight ab Werk:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Listen mit List + Wisch-Löschen</span><span class="dots">···</span>
:::

```
struct RecordListView: View {
    @State private var records = ["Mittagessen 25.5", "U-Bahn 6.0", "Gehalt +8000"]

    var body: some View {
        List {
            ForEach(records, id: \.self) { r in
                Text(r)
            }
            .onDelete { indexSet in          // nach links wischen zum Löschen
                records.remove(atOffsets: indexSet)
            }
        }
    }
}
```
:::

Liste + NavigationLink + sheet + TabView – kombiniere diese vier Bausteine, und du kannst bereits das komplette App-Gerüst „Buchungsliste → Detail öffnen → auf + tippen, Eingabe-Dialog erscheint“ bauen. Genau so entsteht das Haushaltsbuch-Projekt im nächsten Kapitel.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Jetzt bist du dran: Baue ein „Drei-Seiten-Gerüst“

#### 5. Der App-Lebenszyklus: Vordergrund und Hintergrund

Ähnlich wie der Activity-Lebenszyklus bei Android durchläuft auch eine iOS-App Zustandswechsel von „Geburt, Vordergrund, Hintergrund, Tod“. In SwiftUI beobachtest du das über den Environment-Wert scenePhase:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Vorder-/Hintergrundwechsel beobachten</span><span class="dots">···</span>
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
            case .active:    print("wieder vorn: Aktualisierung fortsetzen")
            case .inactive:  print("im Übergang (Anruf oder Moment des Wechsels nach hinten)")
            case .background: print("in den Hintergrund: Entwurf sichern")
            @unknown default: break
            }
        }
    }
}
```
:::

Typische Einsätze: Daten auffrischen, wenn die App wieder in den Vordergrund kommt; Entwürfe speichern, wenn sie in den Hintergrund geht. iOS geht mit Hintergrundbetrieb streng ins Gericht – normale Apps werden bald nach dem Wechsel in den Hintergrund angehalten (eingefroren). Rechne nicht damit, heimlich Schwerstarbeit im Hintergrund zu leisten; für zeitgesteuerte Aufgaben nutze die lokalen Benachrichtigungen aus Kapitel 68, keinen „Dauerbetrieb im Hintergrund“.

{class="mt-1"}
Baue eine Fake-Daten-Version des Haushaltsbuch-Gerüsts: TabView mit drei Reitern (Buchungen/Statistik/Einstellungen) → die Buchungsseite zeigt Fake-Daten in einer List, ein Tipp auf eine Zeile springt zum Detail (NavigationStack) → der "+"-Button oben rechts öffnet den Eingabe-Dialog als sheet. Kein Speichern, kein Netz – reine Gerüstübung. Steht dieses Gerüst, ist es in Kapitel 65 nur noch ein Katzensprung, echte Daten einzufüllen.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Kapitelfazit

- Die vier State-Werkzeuge: @State (seiteneigen), @Binding (ausgeliehen), @Observable (Logik), .environment (global)
- In neuen Projekten schreibst du ViewModels mit dem @Observable-Makro; @ObservableObject aus alten Tutorials: lesen können genügt
- NavigationStack schiebt Seiten; @Environment(\.dismiss) ermöglicht programmatisches Zurück
- Hauptablauf: Seiten schieben; kurzzeitige Aktionen: sheet; gleichrangige Hauptbereiche: TabView
- List ist die Alltagsliste: Trennlinien und Wisch-löschen ab Werk
:::
