---
id: di-wu-shi-san-zhang
num: 53
part: an-zhuo-kai-fa-pian
nav: Kapitel 53: Daten speichern und Netzwerk anfragen
toc: default
kind: chapter
---

### Kapitel 53: Datenspeicherung und Netzwerkanfragen

{class="chapter-intro mb-4"}
Eine App, die nur "angucken" kann, ist tot; erst eine App, die Daten speichern und sich vernetzen kann, lebt. In diesem Kapitel lernst du das "Trio" der Android-Datenschicht kennen: DataStore (kleine Einstellungen speichern), Room (strukturierte Daten speichern), Retrofit (mit dem Server sprechen) – plus ihr "Dispositionszentrum", die Koroutinen. Nach diesem Kapitel kannst du echte Apps schreiben, die sich Nutzer-Gewohnheiten merken und Inhalte live aktualisieren.

#### 1. Welches Speicherkonzept wofür? Erst diese Tabelle anschauen

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Konzept</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Wofür geeignet?</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Eigenschaften</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Wo im Buch genutzt?</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DataStore</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Verstreute Einstellungen (Theme, Schalter)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Schlüssel-Wert-Paare, einfach und sicher</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kapitel 54: Einstellungen des Haushaltsbuchs</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Strukturierte Daten (Buchungen, Nutzer)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Eine echte SQLite-Datenbank verpackt, abfragbar</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kapitel 54: Buchungseinträge</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Serverdaten (nicht speichern, online abrufen)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Der De-facto-Standard unter den HTTP-Bibliotheken</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kapitel 55: Wetterdaten</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Die Arbeitsteilung des Daten-Trios

Merksatz: "Kleine Einstellungen ins DataStore, Daten in Mengen ins Room, Daten von draußen über Retrofit." Das in alten Tutorials allgegenwärtige SharedPreferences ist von DataStore abgelöst, handgeschriebenes SQLite-SQL von Room – lern gleich das Neue, geh nicht den alten Weg.

#### 2. DataStore: Kleine Einstellungen wegspeichern

Werte wie "die zuletzt gewählte Währung" oder "ist der Dunkelmodus an?" willst du verstreut abspeichern – dafür ist DataStore (Preferences-Variante) da:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · DataStore-Beispiel</span><span class="dots">···</span>
:::

```
val Context.dataStore by preferencesDataStore(name = "settings")

// schreiben: Wert speichern
suspend fun saveTheme(isDark: Boolean) {
    context.dataStore.edit { prefs ->
        prefs[THEME_KEY] = isDark
    }
}

// lesen: herausholen (Flow meldet Änderungen automatisch)
val themeFlow: Flow<Boolean> = context.dataStore.data
    .map { it[THEME_KEY] ?: false }
```
:::

Achte darauf: Zurückgegeben wird ein Flow – ein Datenstrom, der "fließt". Sobald sich der Wert ändert, bekommen alle Stellen, die ihn beobachten, automatisch den neuen Wert. Dieses Konzept (Reaktivität) ist der Grundstein des modernen Android – in Kapitel 54 kommt es zum Praxiseinsatz.

#### 3. Room: Den Daten ein "richtiges Zuhause" geben

Ein Haushaltsbuch hat hunderte, tausende Buchungen, die nach Kategorie und Monat abgefragt und ausgewertet werden sollen – dafür braucht es eine Datenbank. Room ist die offizielle Hülle um SQLite und macht "Tabellen anlegen, Daten abfragen" so natürlich wie Kotlin-Schreiben. Drei Dinge:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Das Room-Trio: Entity / Dao / Database</span><span class="dots">···</span>
:::

```
// 1. Entity: die Tabellenstruktur (eine Tabelle = eine Data Class)
@Entity(tableName = "records")
data class Record(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val amount: Double,
    val category: String,
    val note: String,
    val date: String
)

// 2. Dao: das Operations-Interface (anlegen, löschen, ändern, lesen)
@Dao
interface RecordDao {
    @Query("SELECT * FROM records ORDER BY date DESC")
    fun getAll(): Flow<List<Record>>

    @Insert
    suspend fun insert(record: Record)

    @Delete
    suspend fun delete(record: Record)

    @Query("SELECT SUM(amount) FROM records WHERE category = :c")
    suspend fun sumByCategory(c: String): Double
}

// 3. Database: die Endmontage
@Database(entities = [Record::class], version = 1)
abstract class AppDatabase : RoomDatabase() {
    abstract fun recordDao(): RecordDao
}
```
:::

Dieses "Trio"-Template kannst du unverändert in jedes deiner Projekte übernehmen – einfach die Feldnamen austauschen. Die Abfragen liefern Flow, die Oberfläche aktualisiert sich automatisch mit den Daten – herrlich.

#### 4. Retrofit: Mit dem Server sprechen

Wetter, Nachrichten, Wechselkurse … Diese Daten liegen nicht auf dem Telefon, sondern auf den Servern von anderen. Retrofit macht "Daten vom Server anfordern" so einfach wie einen Funktionsaufruf. In drei Schritten:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Retrofit in drei Schritten</span><span class="dots">···</span>
:::

```
// 1. Interface definieren: HTTP-Anfragen als Funktionen beschreiben
interface WeatherApi {
    @GET("v1/weather")
    suspend fun getWeather(@Query("city") city: String): WeatherResponse
}

// 2. Instanz erzeugen
val api = Retrofit.Builder()
    .baseUrl("https://api.example.com/")
    .addConverterFactory(GsonConverterFactory.create())
    .build()
    .create(WeatherApi::class.java)

// 3. aufrufen wie eine Funktion (in einer Koroutine)
val result = api.getWeather("Berlin")
```
:::

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Stolperfalle: Zwei eiserne Netzwerk-Regeln

{class="mt-1"}
① Netzwerkanfragen dürfen niemals im Hauptthread laufen – die Oberfläche friert ein oder die App stürzt ab (NetworkOnMainThreadException). Alle Netzwerkaufrufe gehören in eine Koroutine (viewModelScope.launch). ② Klartext-HTTP ist standardmäßig verboten: Ab Android 9 wird HTTPS verlangt. Für Tests mit lokalen http://-Adressen musst du im Manifest usesCleartextTraffic explizit deklarieren – ein echtes Produkt muss aber komplett über HTTPS laufen.
:::

#### 5. JSON-Parsen: Den Netzdaten eine "Übersetzung" geben

Was der Server zurückgibt, ist meist JSON – ein Text wie ein "verschachteltes Wörterbuch". Retrofit braucht einen "Dolmetscher", der daraus Kotlin-Objekte macht. 2026 gibt es zwei Mainstream-Lösungen:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Konzept</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Eigenschaften</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Empfohlen für</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gson / Moshi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Der klassische Reflection-Ansatz, null Konfigurationsaufwand</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Schneller Start, kleine Projekte mit wenigen Feldern</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">kotlinx.serialization</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Die offizielle Lösung zur Compiler-Zeit, schneller und sicherer</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Erste Wahl für neue Projekte (2026er Mainstream)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Die beiden großen JSON-Lösungen

::: div .code-block
:::inline div .code-head
<span>KOTLIN · kotlinx.serialization-Beispiel</span><span class="dots">···</span>
:::

```
// versieh die Data Class mit @Serializable
@Serializable
data class WeatherResponse(
    val weather: List<Weather>,
    val main: Main,
    val name: String
)

// Retrofit bekommt den passenden Converter angehängt (Beispiel mit offizieller Unterstützung ab Retrofit 2.11+):
// .addConverterFactory(json.asConverterFactory("application/json".toMediaType()))
```
:::

Gleich welche Lösung – das eiserne Gesetz lautet: Erst das echte zurückgegebene JSON anschauen, dann die Felder definieren. Viele "Parsen fehlgeschlagen"-Bugs entstehen, weil Feldnamen verschrieben oder Verschachtelungsebenen falsch geraten sind – gib das rohe JSON aus und gleiche ab, in zehn Sekunden ist der Fehler geortet.

#### 6. Koroutinen: Die "Gemeinsprache" der Android-Concurrency

Das immer wieder auftauchende suspend und launch stammen aus den Kotlin-Koroutinen – der offiziellen Concurrency-Lösung von Android. Grob gesagt: Operationen, die "ein Weilchen dauern" (Netzwerk, Datenbank), blockieren die Oberfläche nicht.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Erste Schritte mit Koroutinen</span><span class="dots">···</span>
:::

```
// starte eine Koroutine im ViewModel
viewModelScope.launch {
    val records = dao.getAll().first()  // suspend: hält automatisch an und wartet
    // Zustand der Oberfläche aktualisieren …
}

// Spickzettel der Schlüsselwörter:
// suspend   —— "ich muss warten, halte andere nicht auf"
// launch    —— "auf geht's!"
// viewModelScope —— die "Werkstatt", die der Ansicht folgt; räumt sich beim Zerstören selbst ab
```
:::

Als Einsteiger musst du zunächst nur die Anwendung kennen; das Prinzip dahinter ("Anhalten und Fortsetzen") kannst du später vertiefen. 90 % dessen, was du im Alltag schreibst, ist diese eine Schablone.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Selbst ausprobieren: Eine kleine App "Satz des Tages" bauen

{class="mt-1"}
Such dir eine kostenlose Zitate-API (z. B. hitokoto o. Ä.), hole mit Retrofit den "Satz des Tages" und zeige ihn mitten auf dem Bildschirm; füge einen Button "Noch einen" hinzu (neue Anfrage in einer Koroutine). Speichere Lieblingssätze mit Room in eine "Favoriten"-Sammlung. Diese Übung nutzt DataStore/Room/Retrofit/Korouten je einmal – danach sind Kapitel 7 und 8 ein Kinderspiel.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Zusammenfassung des Kapitels

- Merksatz: kleine Einstellungen ins DataStore, Daten in Mengen ins Room, Daten von draußen über Retrofit
- DataStore liefert Flow: Ändert sich der Wert, bekommen Beobachter ihn automatisch
- Room-Trio: @Entity (Tabelle) + @Dao (Operationen) + @Database (Endmontage) – die Schablone ist direkt wiederverwendbar
- Retrofit in drei Schritten: Interface definieren → Instanz erzeugen → in der Koroutine aufrufen
- Zwei eiserne Regeln: Netzwerk nie im Hauptthread; echte Produkte immer über HTTPS
- Koroutine = Warten, ohne die Oberfläche zu blockieren; viewModelScope ist die eigene Werkstatt jeder Seite
:::
