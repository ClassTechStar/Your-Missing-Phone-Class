---
id: di-wu-shi-wu-zhang
num: 55
part: an-zhuo-kai-fa-pian
nav: Kapitel 55: Projekt 2 – Wetter-App (Netzwerkversion)
toc: default
kind: chapter
---

### Kapitel 55: Projekt 2 – Wetter-App (Netzversion)

{class="chapter-intro mb-4"}
Das Haushaltsbuch trainiert die "inneren Kräfte", die Wetter-App zeigt dir die "große Welt" – sie verkehrt mit dem Internet. In diesem Projekt lernst du: eine kostenlose API beantragen, JSON parsen, drei Oberflächenzustände ("lädt/erfolgreich/gescheitert") behandeln und den API-Schlüssel gut verstecken. Danach kannst du jede beliebige "Online-App" bauen – Nachrichten, Wechselkurse, Übersetzung, immer dasselbe Rezept.

#### 1. Eine kostenlose Wetter-API beantragen

Zum Üben empfehle ich OpenWeatherMap oder QWeather (Hefeng Weather) – beide haben kostenlose Kontingente, registrieren und loslegen. Am Beispiel OpenWeatherMap:

1. Konto registrieren → auf der Seite API keys einen Key erzeugen (apikey);
2. Die kostenlose Version darf die Schnittstelle Current Weather (aktuelles Wetter) aufrufen: api.openweathermap.org/data/2.5/weather? q=beijing&appid=deinKey&units=metric;
3. Probier sie erst einmal im Browser aus und schau an, wie das zurückgegebene JSON aussieht – diese "Vorbereitung" ist Pflicht, bevor du irgendeine API anbindest.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Stolperfalle: Der Schlüssel darf niemals fest im Code stehen

{class="mt-1"}
Ein API-Key ist quasi dein "Wallet-Passwort" – landet er im Code und wird nach GitHub gepusht, spinnen ihn Crawler binnen Stunden auf und missbrauchen ihn. Richtig: Ab in local.properties (diese Datei ist über gitignore bereits ignoriert) und von dort über Gradles buildConfig in den Code einlesen. Suche nach "Best Practices Android API Key verstecken" und richte es entsprechend ein.
:::

#### 2. Die Netzwerkschicht: Retrofit + JSON-Parsen

Definiere zuerst das "Datenmodell" nach dem JSON, das die API zurückgibt; alles, was kein Gegenstück hat, wird ignoriert:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Datenmodell + Interface</span><span class="dots">···</span>
:::

```
// JSON: {"weather":[{"description":"Klar"}],"main":{"temp":26.5,"humidity":40},"name":"Berlin"}
data class WeatherResponse(
    val weather: List&lt;Weather&gt;,
    val main: Main,
    val name: String
)
data class Weather(val description: String)
data class Main(val temp: Double, val humidity: Int)

interface WeatherApi {
    @GET("data/2.5/weather")
    suspend fun getWeather(
        @Query("q") city: String,
        @Query("appid") key: String,
        @Query("units") metric: String = "metric",
        @Query("lang") lang: String = "zh_cn"
    ): WeatherResponse
}
```
:::

Gson stopft das JSON automatisch in diese data classes – stimmen die Feldnamen, passiert die Magie von ganz allein.

#### 3. Drei Oberflächenzustände: lädt / erfolgreich / gescheitert

Die Seele einer Online-App ist das "Zustandsmanagement". Langsames Netz, keine Verbindung, falsch geschriebener Stadtname … Für jeden Fall braucht die Oberfläche eine Antwort. Mit einer sealed class (versiegelten Klasse) lässt sich das elegant ausdrücken:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · UI-Zustand</span><span class="dots">···</span>
:::

```
sealed class UiState {
    object Loading : UiState()                    // lädt
    data class Success(val data: WeatherResponse) : UiState()  // Erfolg
    data class Error(val message: String) : UiState()          // Fehler
}

// im ViewModel:
fun search(city: String) {
    viewModelScope.launch {
        _state.value = UiState.Loading
        _state.value = try {
            UiState.Success(api.getWeather(city))
        } catch (e: Exception) {
            UiState.Error("Stadt nicht gefunden, probier einen anderen Namen?")
        }
    }
}

// in der Oberfläche:
when (val s = state) {
    is UiState.Loading -&gt; CircularProgressIndicator()   // Ladekreis
    is UiState.Success -&gt; WeatherContent(s.data)        // anzeigen
    is UiState.Error -&gt; Text(s.message)                 // Fehler anzeigen
}
```
:::

Dieses Loading/Success/Error-Dreigestirn ist das "Universal-Template" für vernetzte Oberflächen – präg es dir ein, danach baust du jede Online-App nach demselben Muster.

#### 4. Oberflächen-Code in der Praxis: Das Wetter auf den Bildschirm malen

Die Zustände stehen, so sieht die Oberfläche aus (die entscheidenden Ausschnitte):

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Wetteransicht (Kernauszug)</span><span class="dots">···</span>
:::

```
@Composable
fun WeatherContent(data: WeatherResponse) {
    Column(
        Modifier.fillMaxSize().padding(24.dp),
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Text(data.name, fontSize = 28.sp, fontWeight = FontWeight.Bold)
        Text(
            "${data.main.temp}°C",
            fontSize = 72.sp,
            fontWeight = FontWeight.Light
        )
        Text(
            data.weather.firstOrNull()?.description ?: "Unbekannt",
            fontSize = 20.sp,
            color = Color.Gray
        )
        Spacer(Modifier.height(16.dp))
        Row {
            Text("💧 Luftfeuchtigkeit ${data.main.humidity}%")
            Spacer(Modifier.width(24.dp))
            Text("🌡️ Gefühlt ${data.main.temp}°C")
        }
    }
}
```
:::

Ein paar Details lohnen sich zum Lernen: firstOrNull() holt sicher das erste Element (die Liste kann leer sein), ?: "unbekannt" liefert den Notfalltext – das Prinzip der Null-Sicherheit gilt auch in der Oberfläche. Die Temperatur mit 72.sp in großer Schrift als Blickfang und in geringer Schriftstärke (Light) wirkt elegant – der klassische Wetter-App-Stil.

#### 5. Oberflächen- und Interaktionsdetails

- Suchfeld: oben ein TextField, Städtenamen eingeben und auf Suchen tippen (auf der Tastatur die Aktion "Suchen" setzen – Enter startet die Suche);
- Wetterkarte: Temperatur in großer Schrift (26,5°), Wetterbeschreibung (sonnig), Luftfeuchtigkeit, Stadtname;
- Favoritenstädte: oft besuchte Städte im DataStore speichern und beim nächsten Start automatisch abfragen – eine beiläufige Wiederholung von Kapitel 6;
- Pull-to-Refresh: In Compose nimmst du PullToRefreshBox (von Material 3 bereitgestellt) – schon fühlt sich die App sofort professionell an.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tipp: Bilder bringen die Oberfläche zum Leben

{class="mt-1"}
Gib jedem Wetter ein Emoji oder ein Symbol (☀️🌧️❄️) und mappe es mit when(description) – drei Zeilen Code, und die Oberfläche wirkt gleich doppelt so lebendig. Du kannst auch eine Drittanbieter-Bibliothek mit Wetter-Icons laden, aber für die Übungsphase reichen Emojis völlig.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Jetzt bist du dran: die Abnahme-Checkliste für die Wetter-App

{class="mt-1"}
① Das Wetter lässt sich normal suchen; ② trennst du das Netz, meldet die App den Fehler elegant, statt abzustürzen (teste das im Flugmodus!); ③ gibst du eine nicht existierende Stadt ein, kommt eine freundliche Meldung; ④ zwei Städte als Favoriten bleiben auch nach einem App-Neustart erhalten; ⑤ beim Drehen des Bildschirms geht kein Zustand verloren. Erst wenn alle fünf Punkte erfüllt sind, hat das Projekt bestanden.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Zusammenfassung des Kapitels

- Erst die API im Browser testen und JSON verstehen, dann Code schreiben – „Vorarbeit“ lohnt sich immer
- Den API-Key in local.properties verstecken – niemals ins Code-Repository
- Retrofit-Interface + data class: Passen die Felder, wird das JSON automatisch geparst
- Das Drei-Zustände-Schema Loading/Success/Error ist das Allzweckmittel für vernetzte Oberflächen
- Kein Netz, leere Eingabe, Stadt existiert nicht – Fehlerbehandlung ist die Bestehensgrenze für vernetzte Apps
:::
