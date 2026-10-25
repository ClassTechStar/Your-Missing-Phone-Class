---
id: di-liu-shi-si-zhang
num: 64
part: ios-kai-fa-pian
nav: Capitolo 64: Archiviazione dei dati e richieste di rete
toc: default
kind: chapter
---

### Capitolo 64: Archiviazione dei dati e richieste di rete

{class="chapter-intro mb-4"}
Un'app che serve solo a "guardare" è morta; un'app che salva dati e si collega alla rete è viva. In questo capitolo conosci il "trio" del livello dati di iOS: UserDefaults (le piccole configurazioni), SwiftData (i dati strutturati), URLSession (il dialogo con i server), più Codable per analizzare il JSON e il moderno async/await. A fine capitolo potrai scrivere app vere, capaci di ricordare le abitudini dell'utente e di aggiornare i contenuti in tempo reale.

#### 1. Come scegliere lo schema di archiviazione: guarda prima questa tabella

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Soluzione</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Cosa conviene salvare</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Caratteristiche</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Dove lo usiamo in questo libro</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UserDefaults</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Configurazioni sparse (interruttori, preferenze)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Coppie chiave-valore, semplice e diretto</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Impostazioni del capitolo 65, città preferite del capitolo 66</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftData</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Dati strutturati (voci, registrazioni)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Wrapper ufficiale del database, dichiarato con una riga @Model</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Voci di spesa del capitolo 65</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">URLSession</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Dati del server (non salvati, presi dalla rete)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Framework di rete di sistema, nessuna dipendenza di terze parti</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Dati meteo del capitolo 66</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
La divisione dei compiti del trio dei dati

Impara questa filastrocca: "le piccole configurazioni vanno in UserDefaults, i dati in blocco in SwiftData, i dati dall'esterno passano per URLSession". Core Data dei vecchi tutorial funziona ancora (SwiftData è il suo moderno travestimento), mentre SQLite scritto a mano ormai non si tocca quasi mai: impara direttamente il nuovo, non prendere la strada vecchia.

#### 2. UserDefaults: salvare piccole configurazioni

::: div .code-block
:::inline div .code-head
<span>SWIFT · Esempio UserDefaults</span><span class="dots">···</span>
:::

```
// Scrittura: salva un valore
UserDefaults.standard.set(true, forKey: "isDarkMode")
UserDefaults.standard.set("Pechino", forKey: "favoriteCity")

// Lettura: preleva (se assente restituisce il predefinito)
let isDark = UserDefaults.standard.bool(forKey: "isDarkMode")
let city = UserDefaults.standard.string(forKey: "favoriteCity") ?? "Pechino"

// Cancellazione: rimuove una chiave
UserDefaults.standard.removeObject(forKey: "isDarkMode")
```
:::

Tieni presente che è adatto solo a piccole configurazioni sparse: decine o centinaia di registrazioni vanno affidate a SwiftData, e non usare UserDefaults come database (rallenterebbe l'avvio e rende scomode le ricerche).

#### 3. SwiftData: dare ai dati una "casa vera"

SwiftData è la soluzione di database ufficiale dall'iOS 17 e semplifica all'estremo "creare le tabelle e aggiungere, eliminare, modificare, cercare": con una sola annotazione @Model la classe dei dati diventa una tabella del database:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Esempio SwiftData</span><span class="dots">···</span>
:::

```
import SwiftData

// 1. @Model: questa classe diventa automaticamente una "tabella"
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

// 2. Collega il contenitore all'ingresso dell'app
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .modelContainer(for: Record.self)   // database pronto
    }
}

// 3. Nelle view leggi con @Query e scrivi con @Environment
struct RecordListView: View {
    @Query(sort: \Record.date, order: .reverse) var records: [Record]
    @Environment(\.modelContext) private var context

    var body: some View {
        List(records) { r in
            Text("\(r.category) \(r.amount) yuan")
        }
    }

    func add(amount: Double, category: String) {
        let r = Record(amount: amount, category: category, note: "", date: Date())
        context.insert(r)     // inserisce
        try? context.save()   // salva su disco
    }
}
```
:::

Questo modello "@Model + modelContainer + @Query" puoi portarlo identico in qualsiasi tuo progetto: basta cambiare i nomi dei campi. Appena i dati cambiano, @Query aggiorna l'interfaccia da solo: una meraviglia.

#### 4. Codable: fare da "interprete" al JSON

I dati dei server sono per lo più testo JSON. Il protocollo Codable di Swift fa avvenire da sola la conversione "JSON ⇄ struct": se i nomi dei campi corrispondono, la magia funziona:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Analizzare JSON con Codable</span><span class="dots">···</span>
:::

```
// JSON: {"name":"Pechino","main":{"temp":26.5},"weather":[{"description":"Sereno"}]}
struct WeatherResponse: Codable {
    let name: String
    let main: Main
    let weather: [Weather]
}
struct Main: Codable { let temp: Double }
struct Weather: Codable { let description: String }

// Stringa JSON → struct
let decoder = JSONDecoder()
let data = jsonString.data(using: .utf8)!
let result = try decoder.decode(WeatherResponse.self, from: data)
print(result.weather[0].description)   // "Sereno"
```
:::

Regola ferrea: guarda prima il JSON realmente restituito, poi definisci i campi. Molti bug di "analisi fallita" nascono da nomi di campo sbagliati o tipi indovinati a caso (il server manda la stringa "26.5" e tu dichiari un Double): stampa il JSON grezzo, confrontalo e in dieci secondi trovi il colpevole.

#### 5. URLSession + async/await: parlare con il server

Su iOS la rete si gestisce con URLSession, incluso nel sistema, insieme ad async/await di Swift (le funzioni asincrone): "aspettare la rete" diventa naturale come "aspettare un pacco":

::: div .code-block
:::inline div .code-head
<span>SWIFT · URLSession + async/await</span><span class="dots">···</span>
:::

```
struct WeatherService {
    // Funzioni asincrone: async significa "devo aspettare un attimo", throws significa "può fallire"
    func fetchWeather(city: String) async throws -> WeatherResponse {
        let url = URL(string:
            "https://api.example.com/weather?city=\(city)")!
        let (data, _) = try await URLSession.shared.data(from: url)
        return try JSONDecoder().decode(WeatherResponse.self, from: data)
    }
}

// Punto di chiamata (dentro .task):
.task {
    do {
        let weather = try await service.fetchWeather(city: "Pechino")
        // aggiorna l'interfaccia...
    } catch {
        print("Qualcosa è andato storto: \(error)")
    }
}
```
:::

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Attenzione alle trappole: le due regole ferree della rete

{class="mt-1"}
① Le connessioni di rete devono usare async/await e non bloccano mai il thread principale: un'interfaccia bloccata è un'esperienza da crash. La concorrenza strutturata di Swift rende tutto naturale, ma non dimenticare try await e do/catch. ② ATS vieta per impostazione predefinita l'HTTP in chiaro: iOS esige HTTPS. Per testare un servizio http:// locale devi aprire temporaneamente un'eccezione nell'Info.plist (NSAppTransportSecurity), ma il prodotto ufficiale deve viaggiare tutto in HTTPS: anche la revisione lo controlla.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mettiti alla prova: crea una piccola app "frase del giorno"

#### 6. Anche gli errori di rete vanno "classificati": non scaricare ogni errore addosso all'utente

Rete assente, timeout, 404, errore 500 del server… Per ogni errore diverso, l'utente dovrebbe leggere messaggi diversi:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Gestione degli errori per gravità</span><span class="dots">···</span>
:::

```
func friendlyMessage(_ error: Error) -> String {
    if let urlError = error as? URLError {
        switch urlError.code {
        case .notConnectedToInternet: return "Rete assente — controlli la connessione?"
        case .timedOut:               return "Richiesta scaduta — riprovare più tardi?"
        case .cannotFindHost:         return "Server non trovato"
        default:                      return "Problema di rete: \(urlError.code)"
        }
    }
    if let d = error as? DecodingError {
        return "Formato dati inatteso (l'API potrebbe essere cambiata)"
    }
    return "Qualcosa è andato storto: \(error.localizedDescription)"
}
```
:::

Mostra all'utente "parole comprensibili" e registra nei log la "frase originale" (stampa l'error completo). Non scaricare in faccia all'utente il gergo inglese di error.localizedDescription: è in questi dettagli che si nasconde la qualità di prodotto.

{class="mt-1"}
Trova un'API gratuita di citazioni (per esempio hitokoto o simili), usa URLSession + async/await per scaricare la "frase del giorno", mostrala al centro dello schermo e aggiungi un pulsante "Cambia frase". Poi salva le frasi che ti piacciono nei "preferiti" con SwiftData. Questo esercizio usa insieme UserDefaults, SwiftData, Codable e URLSession: finito questo, i capitoli 7 e 8 saranno un gioco da ragazzi.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Riepilogo del capitolo

- Filastrocca: le piccole configurazioni in UserDefaults, i dati in blocco in SwiftData, i dati esterni via URLSession
- I tre colpi di SwiftData: @Model dichiara la tabella, modelContainer aggancia il contenitore, @Query legge e context.insert scrive
- Codable "traduce" il JSON in automatico: se i campi corrispondono, la magia funziona
- URLSession + async/await: stare in rete è come aspettare un pacco; do/catch gestisce i fallimenti
- Due regole ferree: non bloccare mai il thread principale; il prodotto ufficiale deve usare HTTPS (ATS)
:::
