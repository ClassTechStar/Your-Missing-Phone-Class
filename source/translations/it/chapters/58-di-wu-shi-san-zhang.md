---
id: di-wu-shi-san-zhang
num: 53
part: an-zhuo-kai-fa-pian
nav: Capitolo 53: Archiviazione dei dati e richieste di rete
toc: default
kind: chapter
---

### Capitolo 53: Conservare i dati e parlare con la rete

{class="chapter-intro mb-4"}
Un'app che serve solo a «guardare» è morta; un'app che salva dati e si collega alla rete è viva. In questo capitolo conosci il «trio» del livello dati di Android: DataStore (le piccole configurazioni), Room (i dati strutturati), Retrofit (chi parla con il server), più il loro «direttore d'orchestra» — le coroutine. A capitolo finito potrai scrivere app vere, capaci di ricordare le abitudini dell'utente e di aggiornare i contenuti in tempo reale.

#### 1. Come scegliere dove salvare i dati: prima guarda questa tabella

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Soluzione</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Adatta a salvare cosa</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Caratteristiche</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Dove si usa in questo libro</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DataStore</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Configurazioni sparse (tema, interruttori)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Coppie chiave-valore, semplice e sicuro</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Le impostazioni del registro delle spese, capitolo 54</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Dati strutturati (voci di spesa, utenti)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Una vera incapsulazione del database SQLite, interrogabile</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Le voci del registro, capitolo 54</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Dati del server (non si salvano, si scaricano dalla rete)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lo standard di facto per le richieste HTTP</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">I dati meteo, capitolo 55</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
La ripartizione dei compiti del trio dei dati

Impara questa filastrocca: «le piccole configurazioni in DataStore, i dati in blocco in Room, i dati fuori porta passano da Retrofit». Le SharedPreferences, comuni nei vecchi tutorial, sono state sostituite da DataStore, e il SQLite scritto a mano da Room — impara direttamente il nuovo, non riprendere la vecchia strada.

#### 2. DataStore: salvare le piccole configurazioni

Per ricordare valori sparsi come «la valuta scelta l'ultima volta dall'utente» o «se la modalità scura è attiva», usa DataStore (versione Preferences):

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Esempio DataStore</span><span class="dots">···</span>
:::

```
val Context.dataStore by preferencesDataStore(name = "settings")

// Scrittura: salva un valore
suspend fun saveTheme(isDark: Boolean) {
    context.dataStore.edit { prefs ->
        prefs[THEME_KEY] = isDark
    }
}

// Lettura: preleva (il Flow notifica i cambiamenti da solo)
val themeFlow: Flow<Boolean> = context.dataStore.data
    .map { it[THEME_KEY] ?: false }
```
:::

Nota che viene restituito un Flow — un flusso di dati che «scorre». Appena il valore cambia, tutti i punti che lo osservano ricevono da soli il nuovo valore. Questo concetto (la reattività) è la pietra angolare dell'Android moderno: lo metterai in pratica nel capitolo 54.

#### 3. Room: dare ai dati una «casa vera»

Un registro delle spese ha centinaia o migliaia di voci, e deve interrogare e riepilogare per categoria e per mese — serve un database. Room è l'incapsulamento ufficiale di SQLite e rende «creare tabelle e interrogare i dati» naturale quanto scrivere Kotlin. Servono tre cose:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Il trittico di Room: Entity / Dao / Database</span><span class="dots">···</span>
:::

```
// 1. Entity: la struttura della tabella (una tabella = un data class)
@Entity(tableName = "records")
data class Record(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val amount: Double,
    val category: String,
    val note: String,
    val date: String
)

// 2. Dao: l'interfaccia delle operazioni (CRUD)
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

// 3. Database: assemblaggio finale
@Database(entities = [Record::class], version = 1)
abstract class AppDatabase : RoomDatabase() {
    abstract fun recordDao(): RecordDao
}
```
:::

Questo modello a «tre pezzi» si può copiare identico in qualunque tuo progetto — basta cambiare i nomi dei campi. Le query restituiscono Flow e l'interfaccia si aggiorna da sola al passo con i dati: una meraviglia.

#### 4. Retrofit: parlare con il server

Meteo, notizie, tassi di cambio... questi dati non stanno nel telefono, stanno sui server degli altri. Retrofit rende «chiedere dati al server» semplice come chiamare una funzione. Tre passi:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Retrofit in tre passi</span><span class="dots">···</span>
:::

```
// 1. Definisci l'interfaccia: descrivi le richieste HTTP come funzioni
interface WeatherApi {
    @GET("v1/weather")
    suspend fun getWeather(@Query("city") city: String): WeatherResponse
}

// 2. Crea l'istanza
val api = Retrofit.Builder()
    .baseUrl("https://api.example.com/")
    .addConverterFactory(GsonConverterFactory.create())
    .build()
    .create(WeatherApi::class.java)

// 3. Chiamala come una funzione (in una coroutine)
val result = api.getWeather("Pechino")
```
:::

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Attenzione alle trappole: le due regole d'oro della rete

{class="mt-1"}
① Le richieste di rete non si fanno mai nel thread principale — congela l'interfaccia e può far crashare l'app (NetworkOnMainThreadException). Tutte le chiamate di rete vanno messe in una coroutine (viewModelScope.launch). ② L'HTTP in chiaro è vietato per impostazione predefinita: da Android 9 in poi serve l'HTTPS. Se per i test devi usare un indirizzo locale in http://, devi dichiarare esplicitamente usesCleartextTraffic nel Manifest — ma un prodotto vero deve viaggiare tutto in HTTPS.
:::

#### 5. Il parsing del JSON: «tradurre» i dati di rete

I dati che restituisce il server sono per lo più JSON — una fila di testo che sembra un «dizionario annidato». Retrofit ha bisogno di un «interprete» che li trasformi in oggetti Kotlin. Le due soluzioni più diffuse nel 2026:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Soluzione</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Caratteristiche</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Quando consigliarla</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gson / Moshi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">La soluzione classica basata sulla riflessione, a costo di configurazione zero</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Piccoli progetti partiti in fretta, con pochi campi</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">kotlinx.serialization</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">La soluzione ufficiale a compile-time, più veloce e più sicura</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Prima scelta per i nuovi progetti (la corrente principale del 2026)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Le due grandi soluzioni per il parsing del JSON

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Esempio kotlinx.serialization</span><span class="dots">···</span>
:::

```
// Aggiungi l'annotazione @Serializable al data class
@Serializable
data class WeatherResponse(
    val weather: List<Weather>,
    val main: Main,
    val name: String
)

// Retrofit riceve il Converter corrispondente (supporto ufficiale da Retrofit 2.11+):
// .addConverterFactory(json.asConverterFactory("application/json".toMediaType()))
```
:::

Con qualunque soluzione la regola d'oro è una: prima guarda il JSON realmente restituito, poi definisci i campi. Tanti bug di «parsing fallito» nascono da nomi di campo sbagliati o livelli di annidamento indovinati a caso — stampa il JSON originale e confrontalo: in dieci secondi trovi il punto esatto.

#### 6. Le coroutine: la «lingua franca» della concorrenza in Android

I suspend e launch che compaiono più volte sopra vengono dalle coroutine di Kotlin (Coroutine) — la soluzione di concorrenza ufficiale di Android. Puoi capirlo alla buona così: far sì che le operazioni che «chiedono di aspettare» (rete, database) non blocchino l'interfaccia.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Primo assaggio di coroutine</span><span class="dots">···</span>
:::

```
// Avvia una coroutine nel ViewModel
viewModelScope.launch {
    val records = dao.getAll().first()  // suspend: si sospende e attende da solo
    // aggiorna lo stato dell'interfaccia...
}

// Promemoria delle parole chiave:
// suspend   — "devo aspettare, non bloccate gli altri"
// launch    — "Al lavoro!"
// viewModelScope — l'"officina" legata alla schermata; si chiude da sola quando la schermata viene distrutta
```
:::

Se parti da zero, per ora basta ricordarne l'uso; il principio del «sospendere e riprendere» che c'è dietro potrai approfondirlo più avanti. Nel lavoro di tutti i giorni il 90% di quello che scriverai è questo schema identico.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mani all'opera: crea una mini app «una frase al giorno»

{class="mt-1"}
Trova un'API gratuita di citazioni (per esempio hitokoto o simili), usa Retrofit per scaricare la «frase del giorno», mostrala al centro dello schermo e aggiungi un pulsante «Cambia frase» (che richiede di nuovo dentro una coroutine). Poi salva le frasi che ti piacciono in una «raccolta» con Room. Questo esercizio usa tutti assieme DataStore/Room/Retrofit/coroutine — finito quello, i capitoli 7 e 8 saranno un gioco da ragazzi.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Riepilogo del capitolo

- Filastrocca: piccole configurazioni in DataStore, dati in blocco in Room, dati fuori porta via Retrofit
- DataStore restituisce un Flow: se il valore cambia, gli osservatori lo ricevono da soli
- Il trio di Room: @Entity (tabella) + @Dao (operazioni) + @Database (assemblaggio), modello riutilizzabile così com'è
- I tre passi di Retrofit: definisci l'interfaccia → crea l'istanza → la chiami in una coroutine
- Le due regole d'oro: la rete non va nel thread principale; un prodotto vero viaggia solo in HTTPS
- Coroutine = un'attesa che non blocca l'interfaccia; viewModelScope è l'officina riservata alla schermata
:::
