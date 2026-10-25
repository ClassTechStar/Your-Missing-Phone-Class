---
id: di-liu-shi-si-zhang
num: 64
part: ios-kai-fa-pian
nav: Kapitel 64: Daten speichern und Netzwerk anfragen
toc: default
kind: chapter
---

### Kapitel 64: Datenspeicherung und Netzwerkanfragen

{class="chapter-intro mb-4"}
Eine App, die nur „angeschaut“ werden kann, ist tot; erst eine App, die Daten speichern und sich mit dem Netz verbinden kann, lebt. In diesem Kapitel lernst du das „Trio“ der iOS-Datenschicht kennen: UserDefaults (kleine Einstellungen speichern), SwiftData (strukturierte Daten speichern), URLSession (mit dem Server sprechen), dazu Codable fürs JSON-Parsen und das moderne async/await. Danach schreibst du echte Apps, die sich Gewohnheiten ihrer Nutzer merken und ihre Inhalte aktuell halten.

#### 1. Welche Speicherlösung passt? Erst ein Blick auf diese Tabelle

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Lösung</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Wofür geeignet</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Eigenschaften</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Wo in diesem Buch verwendet</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UserDefaults</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Verstreute Kleinkonfiguration (Schalter, Präferenzen)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Schlüssel-Wert-Paare, simpel und direkt</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Einstellungen in Kapitel 65, Lieblingsstädte in Kapitel 66</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftData</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Strukturierte Daten (Buchungen, Einträge)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Offizieller Datenbank-Wrapper, Deklaration mit einer @Model-Zeile</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Buchungseinträge in Kapitel 65</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">URLSession</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">(nicht speichern, aus dem Netz holen) Serverdaten</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Netzwerkframework ab Werk, keine Drittanbieter-Abhängigkeiten</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Wetterdaten in Kapitel 66</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Die Arbeitsteilung des Daten-Trios

Merke dir den Spruch: „Kleine Einstellungen in UserDefaults, Datenmengen in SwiftData, Daten von außen über URLSession“. Core Data aus älteren Tutorials funktioniert weiterhin (SwiftData ist im Grunde sein modernes Gewand), und handgeschriebenes SQLite fasst du praktisch nie an – lerne gleich das Neue und geh nicht den alten Weg.

#### 2. UserDefaults: kleine Einstellungen ablegen

::: div .code-block
:::inline div .code-head
<span>SWIFT · UserDefaults-Beispiel</span><span class="dots">···</span>
:::

```
// schreiben: Wert speichern
UserDefaults.standard.set(true, forKey: "isDarkMode")
UserDefaults.standard.set("Berlin", forKey: "favoriteCity")

// lesen: herausholen (gibt es nichts, kommt der Standardwert)
let isDark = UserDefaults.standard.bool(forKey: "isDarkMode")
let city = UserDefaults.standard.string(forKey: "favoriteCity") ?? "Berlin"

// löschen: einen Schlüssel entfernen
UserDefaults.standard.removeObject(forKey: "isDarkMode")
```
:::

Beachte: Es taugt nur für verstreute Mini-Einstellungen – bei Dutzenden bis Hunderten von Einträgen gib die Sache an SwiftData weiter. Missbrauche UserDefaults nicht als Datenbank (das bremst den App-Start und macht Abfragen umständlich).

#### 3. SwiftData: den Daten ein „richtiges Zuhause“ geben

SwiftData ist Apples offizielle Datenbanklösung ab iOS 17 und vereinfacht „Tabelle anlegen, hinzufügen, löschen, ändern, abfragen“ aufs Äußerste – eine einzige @Model-Anmerkung, und aus der Datenklasse wird eine Datenbanktabelle:

::: div .code-block
:::inline div .code-head
<span>SWIFT · SwiftData-Beispiel</span><span class="dots">···</span>
:::

```
import SwiftData

// 1. @Model: diese Klasse wird automatisch zur "Tabelle"
@Model
class Record {
    var amount: Double
    var category: String
    var note: String
    var date: Date

    init(amount: Double, category: String, note: String, date: Date) {
        self.amount = amount
        self.category = category
        self.note = note
        self.date = date
    }
}

// 2. den Container am App-Einstiegspunkt anhängen
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .modelContainer(for: Record.self)   // Datenbank bereit
    }
}

// 3. in der View liest man mit @Query und schreibt mit @Environment
struct RecordListView: View {
    @Query(sort: \Record.date, order: .reverse) var records: [Record]
    @Environment(\.modelContext) private var context

    var body: some View {
        List(records) { r in
            Text("\(r.category) \(r.amount) Yuan")
        }
    }

    func add(amount: Double, category: String) {
        let r = Record(amount: amount, category: category, note: "", date: Date())
        context.insert(r)     // speichern
        try? context.save()   // auf Disk schreiben
    }
}
```
:::

Diese Vorlage aus „@Model + modelContainer + @Query“ kannst du wortwörtlich in jedes deiner Projekte übernehmen – einfach die Feldnamen austauschen. Ändern sich die Daten, aktualisiert @Query die Oberfläche automatisch – einfach wunderbar.

#### 4. Codable: JSON „übersetzen“

Serverdaten liegen meist als JSON-Text vor. Swifts Codable-Protokoll lässt die Umwandlung „JSON ⇄ Struct“ automatisch geschehen – passen die Feldnamen, tritt der Zauber in Kraft:

::: div .code-block
:::inline div .code-head
<span>SWIFT · JSON parsen mit Codable</span><span class="dots">···</span>
:::

```
// JSON: {"name":"Berlin","main":{"temp":26.5},"weather":[{"description":"Klar"}]}
struct WeatherResponse: Codable {
    let name: String
    let main: Main
    let weather: [Weather]
}
struct Main: Codable { let temp: Double }
struct Weather: Codable { let description: String }

// von JSON-String zu Struct
let decoder = JSONDecoder()
let data = jsonString.data(using: .utf8)!
let result = try decoder.decode(WeatherResponse.self, from: data)
print(result.weather[0].description)   // "Klar"
```
:::

Eisernes Gesetz: Erst das real zurückkommende JSON ansehen, dann die Felder definieren. Viele „Parsing fehlgeschlagen“-Bugs beruhen auf vertippten Feldnamen oder falsch geratenen Typen (der Server schickt den String "26.5", du deklarierst Double) – gib das Roh-JSON per print aus und gleiche es ab, dann sitzt die Ursache in zehn Sekunden.

#### 5. URLSession + async/await: mit dem Server sprechen

Für Netzwerkzugriffe nutzt iOS das ab Werk mitgelieferte URLSession, kombiniert mit Swifts async/await (asynchronen Funktionen) – „aufs Netz warten“ wird so selbstverständlich wie „aufs Paket warten“:

::: div .code-block
:::inline div .code-head
<span>SWIFT · URLSession + async/await</span><span class="dots">···</span>
:::

```
struct WeatherService {
    // asynchrone Funktion: async markiert "ich muss kurz warten", throws markiert "kann fehlschlagen"
    func fetchWeather(city: String) async throws -> WeatherResponse {
        let url = URL(string:
            "https://api.example.com/weather?city=\(city)")!
        let (data, _) = try await URLSession.shared.data(from: url)
        return try JSONDecoder().decode(WeatherResponse.self, from: data)
    }
}

// Aufrufstelle (in .task):
.task {
    do {
        let weather = try await service.fetchWeather(city: "Berlin")
        // Oberfläche aktualisieren …
    } catch {
        print("Fehler: \(error)")
    }
}
```
:::

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Stolperfalle: zwei eiserne Netzwerkgesetze

{class="mt-1"}
1) Netzwerkzugriffe immer mit async/await, den Haupt-Thread niemals blockieren – eine eingefrorene Oberfläche ist eine katastrophale Erfahrung. Swifts strukturierte Nebenläufigkeit macht das sehr natürlich, aber vergiss try await und do/catch nicht. 2) ATS verbietet standardmäßig Klartext-HTTP: iOS verlangt HTTPS. Beim Testen eines lokalen http://-Dienstes musst du in Info.plist vorübergehend eine Ausnahme öffnen (NSAppTransportSecurity), doch ein echtes Produkt muss komplett über HTTPS laufen – auch das Review schaut genau darauf.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Jetzt bist du dran: eine kleine „Zitat-des-Tages“-App

#### 6. Auch Netzwerkfehler „staffeln“: nicht jeden Fehler wahllos an den Nutzer werfen

Keine Verbindung, Zeitüberschreitung, 404, Serverfehler 500 … Bei verschiedenen Fehlern sollte der Nutzer verschiedene Worte zu sehen bekommen:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Fehlerbehandlung nach Stufen</span><span class="dots">···</span>
:::

```
func friendlyMessage(_ error: Error) -> String {
    if let urlError = error as? URLError {
        switch urlError.code {
        case .notConnectedToInternet: return "Kein Netz, Verbindung prüfen?"
        case .timedOut:               return "Zeitüberschreitung, später nochmal versuchen?"
        case .cannotFindHost:         return "Server nicht gefunden"
        default:                      return "Netzwerkproblem: \(urlError.code)"
        }
    }
    if let d = error as? DecodingError {
        return "Falsches Datenformat (die API hat sich vielleicht geändert)"
    }
    return "Fehler: \(error.localizedDescription)"
}
```
:::

Dem Nutzer „verständliche Worte“ zeigen, dem Log die „Originalworte“ (das komplette error per print ausgeben). Wirf dem Nutzer den englischen Fachchinesisch-Text von error.localizedDescription nicht direkt hin – Produktqualität steckt genau in solchen Details.

{class="mt-1"}
Such dir eine kostenlose Zitate-API (etwa hitokoto und Ähnliches), hole mit URLSession + async/await das „Zitat des Tages“, zeige es mitten auf dem Bildschirm und ergänze einen Button „Nächstes Zitat“. Speichere Lieblingssätze zusätzlich mit SwiftData in einer „Favoriten“-Sammlung. Diese Übung nutzt UserDefaults/SwiftData/Codable/URLSession allesamt einmal durch – hast du sie fertig, sind Kapitel 7 und 8 ein Kinderspiel.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Kapitelfazit

- Merkspruch: Kleine Einstellungen in UserDefaults, Datenmengen in SwiftData, Daten von außen über URLSession
- SwiftDatas drei Kernzüge: die Tabelle mit @Model deklarieren, den Container mit modelContainer anhängen, mit @Query lesen und mit context.insert schreiben
- Codable „übersetzt“ JSON automatisch: Passen die Felder, tritt der Zauber in Kraft
- URLSession + async/await: aufs Netz warten wie aufs Paket; do/catch fängt Fehler ab
- Zwei eiserne Gesetze: Haupt-Thread nicht blockieren; echte Produkte müssen HTTPS nutzen (ATS)
:::
