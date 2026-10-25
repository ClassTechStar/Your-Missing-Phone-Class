---
id: di-liu-shi-liu-zhang
num: 66
part: ios-kai-fa-pian
nav: Kapitel 66: Projekt 2 – Wetter-App (Netzwerkversion)
toc: default
kind: chapter
---

### Kapitel 66: Projekt 2 – Wetter-App (Netzwerkversion)

{class="chapter-intro mb-4"}
Das Haushaltsbuch trainiert die inneren Fähigkeiten, die Wetter-App erweitert den Horizont – sie muss mit dem Internet verkehren. In diesem Projekt lernst du: eine kostenlose API beantragen, JSON parsen, die drei Oberflächenzustände „lädt / erfolgreich / fehlgeschlagen“ behandeln und den API-Schlüssel sicher verstecken. Danach bist du in der Lage, jede „vernetzte App“ zu bauen – Nachrichten, Wechselkurse, Übersetzung: immer dasselbe Prinzip.

#### 1. Eine kostenlose Wetter-API beantragen

Zum privaten Üben empfehle ich OpenWeatherMap oder das in China verbreitete QWeather (He-Feng-Tianqi) – beide haben kostenlose Kontingente und sind direkt nach der Registrierung nutzbar. Am Beispiel von OpenWeatherMap:

1. Konto registrieren → auf der API-keys-Seite einen Schlüssel (apikey) erzeugen;
2. Die Gratisversion darf den Current-Weather-Endpunkt aufrufen: api.openweathermap.org/data/2.5/weather? q=beijing&appid=DEIN_KEY&units=metric;
3. Probiere es zuerst einmal im Browser und schau dir an, wie das zurückkommende JSON aussieht – dieses „Vorbereiten“ ist vor dem Anbinden jeder API Pflicht.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Stolperfalle: Der Schlüssel darf niemals fest in den Code

{class="mt-1"}
Ein API-Key ist so etwas wie das „Passwort zu deiner Brieftasche“: Steht er im Code und wird zu GitHub hochgeladen, sammeln ihn Crawler binnen Stunden auf und missbrauchen ihn. Der richtige Weg unter iOS: in Config.xcconfig ablegen (eine Konfigurationsdatei, die gitignore bereits ignoriert) und über Info.plist in den Code einlesen. Suche nach „iOS xcconfig API-Schlüssel verwalten“ und richte dich nach der Anleitung.
:::

#### 2. Die Netzwerkschicht: URLSession + Codable

Definiere das Modell zuerst nach dem JSON, das die API liefert, und schreibe dann den Service:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Datenmodell + Service</span><span class="dots">···</span>
:::

```
// JSON: {"weather":[{"description":"Klar"}],"main":{"temp":26.5,"humidity":40},"name":"Berlin"}
struct WeatherResponse: Codable {
    let weather: [Weather]
    let main: Main
    let name: String
}
struct Weather: Codable { let description: String }
struct Main: Codable { let temp: Double; let humidity: Int }

struct WeatherService {
    let key: String   // aus xcconfig gelesen

    func fetchWeather(city: String) async throws -> WeatherResponse {
        var comps = URLComponents(string: "https://api.openweathermap.org/data/2.5/weather")!
        comps.queryItems = [
            URLQueryItem(name: "q", value: city),
            URLQueryItem(name: "appid", value: key),
            URLQueryItem(name: "units", value: "metric"),
            URLQueryItem(name: "lang", value: "zh_cn")
        ]
        let (data, _) = try await URLSession.shared.data(from: comps.url!)
        return try JSONDecoder().decode(WeatherResponse.self, from: data)
    }
}
```
:::

#### 3. Die drei Oberflächenzustände: lädt / erfolgreich / fehlgeschlagen

Die Seele einer vernetzten App liegt im „State-Management“. Langsames Netz, keine Verbindung, falsch geschriebener Stadtname … In jedem Fall muss die Oberfläche dem Nutzer Rechenschaft geben. Eleganz erreichst du mit enum + switch:

::: div .code-block
:::inline div .code-head
<span>SWIFT · UI-Zustand</span><span class="dots">···</span>
:::

```
enum LoadState {
    case loading                  // lädt
    case success(WeatherResponse) // Erfolg
    case error(String)            // Fehler
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
            state = .error("Stadt nicht gefunden, probier einen anderen Namen?")
        }
    }
}

// in der View:
switch vm.state {
case .loading: ProgressView("Lädt …")
case .success(let d): WeatherContent(data: d)
case .error(let msg): Text(msg).foregroundColor(.secondary)
}
```
:::

Dieses Dreistufen-Schema loading/success/error ist das „Universalmuster“ für vernetzte Oberflächen: lerne es erstmal auswendig, dann baust du künftig alle vernetzten Apps nach demselben Vorbild.

#### 4. Oberflächencode in der Praxis: das Wetter zeichnen

::: div .code-block
:::inline div .code-head
<span>SWIFT · Wetteransicht (Kernauszug)</span><span class="dots">···</span>
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
            Text(data.weather.first?.description ?? "Unbekannt")
                .font(.title3)
                .foregroundColor(.secondary)
            HStack(spacing: 24) {
                Label("Luftfeuchtigkeit \(data.main.humidity)%", systemImage: "humidity")
                Label("Gefühlt \(Int(data.main.temp))°C", systemImage: "thermometer")
            }
        }
        .padding()
    }
}
```
:::

Ein paar kleine Details sind es wert, gelernt zu werden: first? holt sicher das erste Element (die Liste kann leer sein), ?? "Unbekannt" liefert den Ausweichtext; die Temperatur in Schriftgröße 76 mit feiner Schriftstärke ist der Klassiker unter Wetter-Apps; Label ist Apples offizielle Komponente für „Icon + Text“ und sauberer als ein handgebautes HStack.

#### 5. Interaktionsdetails und Lieblingsstädte

- Suchfeld: der Modifier .searchable oben; die Suchinteraktion kommt aus dem System, beim Absenden rufst du vm.search auf;
- Lieblingsstädte: oft angesehene Städte in UserDefaults speichern, beim nächsten Start automatisch abfragen;
- Zum-Aktualisieren-Ziehen: eine Zeile mit .refreshable { await vm.search(...) };
- Wettericons: Mit Image(systemName:) nach Beschreibung zuordnen (sun.max / cloud.rain / snowflake) – die Oberfläche lebt sofort auf.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tipp: das „Manko“ bei chinesischen Städtenamen

{class="mt-1"}
OpenWeatherMap unterstützt chinesische Städtenamen nur mäßig: Die Suche nach dem chinesischen Namen für Peking kann ins Leere laufen, während "beijing" problemlos funktioniert. Für ein echtes Produkt legst du eine eingebaute Zuordnungstabelle „Stadtname → Englisch/Koordinaten“ bei oder bindest einen chinesischen Wetterdienst an. In der Übungsphase genügt es zunächst, Pinyin-/englische Städtenamen zu unterstützen – kämpfe nicht dagegen an.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Jetzt bist du dran: die Abnahme-Checkliste für die Wetter-App

#### 6. Netzwerkanfragen debuggen: Ausgabe, Mitschnitt und simuliertes langsames Netz

Wenn eine vernetzte App Probleme macht, liegt es in neun von zehn Fällen daran, dass „die Anfrage falsch abgesetzt“ oder „die Antwort falsch geparst“ wurde. Drei Debug-Mittel:

1. Rohdaten ausgeben: String(data: data, encoding: .utf8) per print ausgeben und das Roh-JSON ansehen – Feldnamen und Typen auf einen Blick, zehnmal schneller als Raten;
2. Mitschnitt-Tools: Auf dem Mac fängt das kostenlose Proxyman beziehungsweise das Open-Source-Charles alle Anfragen und Antworten der App ab – die Netzwerkschicht wird sichtbar wie auf einem Röntgenbild;
3. Schwaches Netz simulieren: Im Simulator-Menü unter Features → Network Link Conditioner (das Tool musst du von der Entwickler-Website laden) lassen sich 3G und hohe Latenz simulieren – so entlarvst du Erfahrungsprobleme wie das „endlose Warten mit Ladekreisen“.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tipp: Die Anfrage scheitert an ATS?

{class="mt-1"}
Kommt direkt beim Absenden der Anfrage ein „App Transport Security“-Fehler, hast du höchstwahrscheinlich eine Klartext-http://-Adresse verwendet. Echte Endpunkte müssen HTTPS nutzen; zum lokalen Debuggen öffnest du vorübergehend eine Ausnahme (in Info.plist NSAllowsLocalNetworking ergänzen) und räumst sie vor dem Store-Upload sauber weg.
:::

{class="mt-1"}
1) Normale Suche liefert das Wetter; 2) Netz trennen – die App meldet den Fehler elegant, ohne abzustürzen (teste, indem du im Simulator das Netz des Macs abschaltest!); 3) eine nicht existierende Stadt eingeben – die Meldung ist freundlich; 4) zwei Städte speichern, App neu starten – sie sind noch da; 5) im Dunkelmodus ist die Oberfläche nicht grell. Erst wenn alle fünf Punkte bestehen, hat dieses Projekt bestanden.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Kapitelfazit

- Erst die API im Browser testen und das JSON verstehen, dann Code schreiben – „Vorbereitung“ zahlt sich immer aus
- API-Key versteckt in der xcconfig, niemals ins Code-Repository
- Codable-Modell + URLSession mit async/await: Passen die Felder, parst sich das JSON automatisch
- Das Dreistufen-Schema loading/success/error ist das Allzweckmuster für vernetzte Oberflächen
- Kein Netz, leere Eingabe, nicht existierende Stadt – Fehlerbehandlung ist die Bestehensgrenze vernetzter Apps
:::
