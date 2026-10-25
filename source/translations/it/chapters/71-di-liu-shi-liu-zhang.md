---
id: di-liu-shi-liu-zhang
num: 66
part: ios-kai-fa-pian
nav: Capitolo 66: Progetto 2 — App meteo (versione in rete)
toc: default
kind: chapter
---

### Capitolo 66: Progetto 2 — app meteo (versione in rete)

{class="chapter-intro mb-4"}
Il registro delle spese è allenamento "interiore", l'app meteo è la prima uscita "nel mondo": deve trattare con internet. In questo progetto imparerai a: richiedere un'API gratuita, analizzare il JSON, gestire i tre stati dell'interfaccia "caricamento/riuscito/fallito" e nascondere bene la chiave API. Portato a termine, avrai la capacità di fare qualsiasi "app connessa": notizie, tassi di cambio, traduzioni; lo schema è identico.

#### 1. Richiedere un'API meteo gratuita

Per allenarsi a livello personale, consiglio OpenWeatherMap oppure il cinese QWeather — entrambi offrono una quota gratuita e si usano subito dopo la registrazione. Prendiamo OpenWeatherMap come esempio:

1. Registrati → nella pagina API keys genera una chiave (apikey);
2. La versione gratuita può chiamare l'interfaccia Current Weather: api.openweathermap.org/data/2.5/weather? q=beijing&appid=tuaChiave&units=metric;
3. Prima fai una prova nel browser e guarda com'è fatto il JSON restituito — è il "compito a casa" obbligatorio prima di collegare qualsiasi API.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Attenzione alle trappole: la chiave non va mai scritta a mano nel codice

{class="mt-1"}
La chiave API è come la "password del portafoglio": se la scrivi nel codice e fai un commit su GitHub, nel giro di poche ore crawler la scannerizzano e la consumeranno a tua insaputa. Il metodo corretto su iOS: mettila in Config.xcconfig (file di configurazione, già ignorato da gitignore) e leggila nel codice tramite Info.plist. Cerca "gestione chiavi iOS xcconfig" e segui le istruzioni.
:::

#### 2. Il livello di rete: URLSession + Codable

Prima definisci il modello in base al JSON restituito dall'API, poi scrivi il servizio:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Modello dati + servizio</span><span class="dots">···</span>
:::

```
// JSON: {"weather":[{"description":"Sereno"}],"main":{"temp":26.5,"humidity":40},"name":"Pechino"}
struct WeatherResponse: Codable {
    let weather: [Weather]
    let main: Main
    let name: String
}
struct Weather: Codable { let description: String }
struct Main: Codable { let temp: Double; let humidity: Int }

struct WeatherService {
    let key: String   // letto da xcconfig

    func fetchWeather(city: String) async throws -> WeatherResponse {
        var comps = URLComponents(string: "https://api.openweathermap.org/data/2.5/weather")!
        comps.queryItems = [
            URLQueryItem(name: "q", value: city),
            URLQueryItem(name: "appid", value: key),
            URLQueryItem(name: "units", value: "metric"),
            URLQueryItem(name: "lang", value: "it")
        ]
        let (data, _) = try await URLSession.shared.data(from: comps.url!)
        return try JSONDecoder().decode(WeatherResponse.self, from: data)
    }
}
```
:::

#### 3. I tre stati dell'interfaccia: caricamento / riuscito / fallito

L'anima di un'app connessa è la "gestione degli stati". Rete lenta, rete assente, nome della città sbagliato… per ogni situazione l'interfaccia deve dare conto all'utente. Rappresentali con eleganza usando un enum + switch:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Stato dell'interfaccia</span><span class="dots">···</span>
:::

```
enum LoadState {
    case loading                  // spinner in rotazione
    case success(WeatherResponse) // successo
    case error(String)            // errore
}

@Observable
class WeatherViewModel {
    var state: LoadState = .loading
    private let service = WeatherService(key: Config.apiKey)

    func search(city: String) async {
        state = .loading
        do {
            let data = try await service.fetchWeather(city: city)
            state = .success(data)
        } catch {
            state = .error("Città non trovata — provare con un altro nome?")
        }
    }
}

// Nell'interfaccia:
switch vm.state {
case .loading: ProgressView("Caricamento…")
case .success(let d): WeatherContent(data: d)
case .error(let msg): Text(msg).foregroundColor(.secondary)
}
```
:::

Lo schema in tre fasi loading/success/error è il "modello universale" delle interfacce connesse: imparalo a memoria, e per tutte le app connesse del futuro basterà ricalcarlo.

#### 4. Codice dell'interfaccia sul campo: disegnare il meteo

::: div .code-block
:::inline div .code-head
<span>SWIFT · Schermata meteo (brano essenziale)</span><span class="dots">···</span>
:::

```
struct WeatherContent: View {
    let data: WeatherResponse

    var body: some View {
        VStack(spacing: 12) {
            Text(data.name)
                .font(.title.bold())
            Text("\(Int(data.main.temp))°C")
                .font(.system(size: 76, weight: .thin))
            Text(data.weather.first?.description ?? "Sconosciuto")
                .font(.title3)
                .foregroundColor(.secondary)
            HStack(spacing: 24) {
                Label("Umidità \(data.main.humidity)%", systemImage: "humidity")
                Label("Percepiti \(Int(data.main.temp))°C", systemImage: "thermometer")
            }
        }
        .padding()
    }
}
```
:::

Alcuni dettagli meritano di essere imparati: first? prende in sicurezza il primo elemento (l'elenco potrebbe essere vuoto), ?? "Sconosciuto" fornisce il testo di riserva; il numero della temperatura a 76 punti in peso sottile è la ricetta classica delle app meteo; Label è il componente ufficiale "icona+testo", più corretto che assemblare un HStack a mano.

#### 5. Dettagli d'interazione e città preferite

- Campo di ricerca: il modificatore .searchable in alto offre l'interazione di ricerca di sistema; all'invio chiama vm.search;
- Città preferite: salva le città consultate di frequente in UserDefaults e alla prossima apertura cercale automaticamente;
- Aggiornamento trascinando in basso: una riga con .refreshable { await vm.search(...) };
- Icone del meteo: usa Image(systemName:) mappando in base alla descrizione (sun.max / cloud.rain / snowflake): l'interfaccia prende vita all'istante.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Consiglio: la "magagna" dei nomi di città in cinese

{class="mt-1"}
OpenWeatherMap supporta mediamente i nomi di città in cinese: cercare il nome in caratteri cinesi può non dare risultati, mentre "beijing" funziona normalmente. In un prodotto vero si incorpora una tabella di corrispondenza "nome città → inglese/coordinate" oppure si collega un servizio meteo cinese. Nella fase di allenamento basta supportare i nomi in pinyin/inglese: non litigarci.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mettiti alla prova: la checklist di collaudo dell'app meteo

#### 6. Come fare il debug delle richieste di rete: stampa, packet capture e simulazione di rete lenta

Quando un'app connessa dà problemi, nove volte su dieci è perché "la richiesta non è stata inviata bene" o "la risposta non è stata analizzata bene". Tre strumenti di debug:

1. Stampa dei dati grezzi: stampa String(data: data, encoding: .utf8) per vedere il JSON originale — nomi dei campi e tipi a colpo d'occhio, dieci volte più veloce che tirare a indovinare;
2. Strumenti di packet capture: Proxyman (gratuito su Mac) o Charles open source intercettano tutte le richieste e le risposte dell'app e rendono il livello di rete trasparente come una radiografia;
3. Simulare la rete debole: dal menu del simulatore, Features → Network Link Conditioner (lo strumento va scaricato dal sito per sviluppatori), per emulare 3G e alta latenza — così scoperchi i problemi di esperienza tipo "la rotella che gira mezz'ora".

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Consiglio: la richiesta non passa ATS?

{class="mt-1"}
Se la richiesta fallisce appena inviata con un errore "App Transport Security", quasi sicuramente hai usato un indirizzo http:// in chiaro. Le interfacce ufficiali devono essere in HTTPS; per il debug locale apri temporaneamente un'eccezione (aggiungi NSAllowsLocalNetworking all'Info.plist) e prima di pubblicare ricorda di ripulire tutto.
:::

{class="mt-1"}
① La ricerca del meteo funziona regolarmente; ② disconnetti la rete: l'app segnala l'errore con eleganza senza crashare (fai la prova dal simulatore spegnendo la rete del Mac!); ③ digiti una città inesistente: il messaggio è amichevole; ④ salvi due città nei preferiti e dopo il riavvio dell'app ci sono ancora; ⑤ in modalità scura l'interfaccia non acceca. Solo superando tutti e cinque i punti il progetto può dirsi laureato.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Riepilogo del capitolo

- Prima provare l'API nel browser e capire il JSON, poi scrivere il codice — "prepararsi in anticipo" non costa mai nulla
- La chiave API nascosta nel xcconfig, mai dentro il repository del codice
- Modello Codable + URLSession async/await: campi corrispondenti, JSON analizzato in automatico
- Gli stati in tre fasi loading/success/error sono l'asso nella manica delle interfacce connesse
- Rete assente, input vuoto, città inesistente — la gestione degli errori è la sufficienza di un'app connessa
:::
