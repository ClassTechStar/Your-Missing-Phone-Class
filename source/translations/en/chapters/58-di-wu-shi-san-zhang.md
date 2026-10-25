---
id: di-wu-shi-san-zhang
num: 53
part: an-zhuo-kai-fa-pian
nav: Chapter 53: Data Storage and Network Requests
toc: default
kind: chapter
---

### Chapter 53: Data Storage and Network Requests

{class="chapter-intro mb-4"}
An app you can only look at is dead; an app that can save data and reach the network is alive. This chapter introduces the "three-piece set" of Android's data layer: DataStore (for small settings), Room (for structured data), and Retrofit (for talking to servers), plus their "head dispatcher" — coroutines. After this chapter you'll be able to write real apps that remember user preferences and update their content in real time.

#### 1. Choosing a Storage Option: Look at This Table First

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Option</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Good for storing</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Traits</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Where this book uses it</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DataStore</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Scattered settings (theme, toggles)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Key-value pairs; simple and safe</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Chapter 54, expense tracker settings</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Structured data (transactions, users)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">A real wrapper over the SQLite database; queryable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Chapter 54, transaction records</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">(Not stored; fetched online) server data</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">The de facto standard HTTP request library</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Chapter 55, weather data</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
How the data trio divides the work

Memorize this mantra: "small settings go in DataStore, batches of data go in Room, outside data travels via Retrofit." SharedPreferences, common in older tutorials, has been replaced by DataStore, and hand-written SQL for SQLite has been replaced by Room — learn the new way and skip the old road.

#### 2. DataStore: Saving Small Settings

To remember scattered values like "the currency the user picked last time" or "whether dark mode is on," use DataStore (the Preferences flavor):

::: div .code-block
:::inline div .code-head
<span>KOTLIN · DataStore example</span><span class="dots">···</span>
:::

```
val Context.dataStore by preferencesDataStore(name = "settings")

// Write: store a value
suspend fun saveTheme(isDark: Boolean) {
    context.dataStore.edit { prefs ->
        prefs[THEME_KEY] = isDark
    }
}

// Read: fetch it (a Flow notifies about changes automatically)
val themeFlow: Flow<Boolean> = context.dataStore.data
    .map { it[THEME_KEY] ?: false }
```
:::

Note that what comes back is a Flow — a data stream that "flows." The moment a value changes, everywhere that observes it automatically receives the new value. This concept (reactivity) is a cornerstone of modern Android; you'll put it into practice in Chapter 54.

#### 3. Room: Giving Your Data a "Real Home"

An expense tracker holds hundreds or thousands of entries, and you'll want to query and summarize by category and by month — that takes a database. Room is the official wrapper around SQLite that makes "creating tables and querying data" feel as natural as writing Kotlin. Three pieces:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Room's three pieces: Entity / Dao / Database</span><span class="dots">···</span>
:::

```
// 1. Entity: the table structure (one table = one data class)
@Entity(tableName = "records")
data class Record(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val amount: Double,
    val category: String,
    val note: String,
    val date: String
)

// 2. Dao: the operations interface (CRUD)
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

// 3. Database: final assembly
@Database(entities = [Record::class], version = 1)
abstract class AppDatabase : RoomDatabase() {
    abstract fun recordDao(): RecordDao
}
```
:::

You can lift this "trio" template straight into any of your projects — just change the field names. Queries return a Flow, so the UI refreshes automatically as the data changes. Simply delightful.

#### 4. Retrofit: Talking to Servers

Weather, news, exchange rates... that data isn't on the phone; it's on someone else's server. Retrofit makes "asking a server for data" as easy as calling a function. Three steps:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Retrofit in three steps</span><span class="dots">···</span>
:::

```
// 1. Define the interface: describe HTTP requests as functions
interface WeatherApi {
    @GET("v1/weather")
    suspend fun getWeather(@Query("city") city: String): WeatherResponse
}

// 2. Create the instance
val api = Retrofit.Builder()
    .baseUrl("https://api.example.com/")
    .addConverterFactory(GsonConverterFactory.create())
    .build()
    .create(WeatherApi::class.java)

// 3. Call it like a function (inside a coroutine)
val result = api.getWeather("Beijing")
```
:::

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Watch out: two iron rules of networking

{class="mt-1"}
(1) Never make network requests on the main thread — it will freeze the UI or even crash the app (NetworkOnMainThreadException). All network calls must go inside a coroutine (viewModelScope.launch). (2) Plain-text HTTP is blocked by default: Android 9 and up requires HTTPS. If you need an http:// local address while testing, you must explicitly declare usesCleartextTraffic in the Manifest — but a real product must use HTTPS everywhere.
:::

#### 5. JSON Parsing: Translating Network Data

Most data a server returns is JSON — text that looks like a "nested dictionary." Retrofit needs a "translator" to turn it into Kotlin objects. The two mainstream options in 2026:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Option</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Traits</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Best for</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gson / Moshi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">The veteran reflection-based option; zero configuration</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Quick starts and small projects without many fields</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">kotlinx.serialization</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">The official compile-time option; faster and safer</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">The first choice for new projects (mainstream in 2026)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
The two major JSON parsing options

::: div .code-block
:::inline div .code-head
<span>KOTLIN · kotlinx.serialization example</span><span class="dots">···</span>
:::

```
// Add the @Serializable annotation to the data class
@Serializable
data class WeatherResponse(
    val weather: List<Weather>,
    val main: Main,
    val name: String
)

// Retrofit gets the matching Converter (official support since Retrofit 2.11+):
// .addConverterFactory(json.asConverterFactory("application/json".toMediaType()))
```
:::

Whichever option you pick, the iron rule is: look at the real JSON response first, then define your fields. Many "parsing failed" bugs come from misspelled field names or wrongly guessed nesting — print out the raw JSON and compare, and you'll pinpoint the issue in ten seconds.

#### 6. Coroutines: The "Common Language" of Android Concurrency

The suspend and launch you keep seeing above come from Kotlin coroutines — Android's official concurrency solution. A rough way to think of it: operations that "need to wait a while" (network, database) don't block the UI.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · First taste of coroutines</span><span class="dots">···</span>
:::

```
// Launch a coroutine in the ViewModel
viewModelScope.launch {
    val records = dao.getAll().first()  // suspend: pauses and waits automatically
    // update the UI state...
}

// Keyword cheat sheet:
// suspend   — "I need to wait, don't block the others"
// launch    — "Get to work!"
// viewModelScope — the "workshop" tied to the screen; it wraps up automatically when the screen is destroyed
```
:::

If you're starting from zero, just memorize the usage for now; you can dig into the "suspend and resume" mechanics later. In everyday development, 90% of what you write is this one template.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Hands-on: Build a "Quote of the Day" Mini App

{class="mt-1"}
Find a free quotes API (something like hitokoto), use Retrofit to fetch a "quote of the day," show it in the center of the screen, and add a "New quote" button (re-request inside a coroutine). Then use Room to save favorite quotes into a "collection." This one exercise uses DataStore/Room/Retrofit/coroutines all together — finish it, and Chapters 7 and 8 will be a piece of cake.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Chapter Summary

- The mantra: small settings in DataStore, batches of data in Room, outside data via Retrofit
- DataStore returns a Flow: when a value changes, observers get the new one automatically
- Room's trio: @Entity (table) + @Dao (operations) + @Database (final assembly) — the template can be reused as-is
- Retrofit in three steps: define the interface → create the instance → call it inside a coroutine
- Two iron rules: no networking on the main thread; real products must use HTTPS
- Coroutines = waiting without blocking the UI; viewModelScope is the screen's own workshop
:::
