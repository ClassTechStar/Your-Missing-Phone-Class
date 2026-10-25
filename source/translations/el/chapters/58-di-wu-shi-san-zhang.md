---
id: di-wu-shi-san-zhang
num: 53
part: an-zhuo-kai-fa-pian
nav: Κεφάλαιο 53: Αποθήκευση δεδομένων και αιτήματα δικτύου
toc: default
kind: chapter
---

### Κεφάλαιο 53: Αποθήκευση δεδομένων και αιτήματα δικτύου

{class="chapter-intro mb-4"}
Μια εφαρμογή που μόνο «κοιτάζεται» είναι νεκρή· ζωντανή είναι όση μπορεί να αποθηκεύει δεδομένα και να συνδέεται στο διαδίκτυο. Σε αυτό το κεφάλαιο θα γνωρίσεις το «τρίο» του στρώματος δεδομένων του Android: DataStore (για μικρές ρυθμίσεις), Room (για δομημένα δεδομένα), Retrofit (για να μιλάς με τον διακομιστή) — και τον «γενικό διευθυντή» τους, τα coroutines. Όταν το τελειώσεις, θα μπορείς να γράφεις αληθινές εφαρμογές που θυμούνται τις συνήθειες του χρήστη και ανανεώνουν το περιεχόμενό τους σε πραγματικό χρόνο.

#### 1. Πώς διαλέγεις λύση αποθήκευσης: κοίτα πρώτα αυτόν τον πίνακα

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Λύση</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Τι αποθηκεύει</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Χαρακτηριστικά</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Πού το χρησιμοποιεί το βιβλίο</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DataStore</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Σκόρπιες ρυθμίσεις (θέμα, διακόπτες)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ζεύγη κλειδιού-τιμής, απλό και ασφαλές</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Οι ρυθμίσεις του βιβλίου εξόδων (κεφάλαιο 54)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Δομημένα δεδομένα (εγγραφές, χρήστες)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Πραγματική περιτύλιξη βάσης SQLite, με ερωτήματα</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Οι εγγραφές εξόδων (κεφάλαιο 54)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Δεδομένα από διακομιστή (δεν αποθηκεύονται, τα παίρνουμε από το δίκτυο)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Το ντε φάκτο πρότυπο βιβλιοθήκη για αιτήματα HTTP</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Τα δεδομένα καιρού (κεφάλαιο 55)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Ο καταμερισμός εργασίας του «τρίου» των δεδομένων

Κράτα έναν στίχο: «τις μικρές ρυθμίσεις στο DataStore, τα δεδομένα σε όγκο στο Room, τα εξωτερικά δεδομένα μέσω Retrofit». Τα SharedPreferences που συναντάς σε παλιούς οδηγούς έχουν αντικατασταθεί από το DataStore, και το SQL γραμμένο στο χέρι για SQLite από το Room — μάθε τα νέα κατευθείαν, μην πας τον παλιό δρόμο.

#### 2. DataStore: για να αποθηκεύεις μικρές ρυθμίσεις

Για να θυμάσαι σκόρπιες τιμές όπως «ποιο νόμισμα διάλεξε τελευταία φορά ο χρήστης» ή «αν είναι ενεργό το σκοτεινό θέμα», χρησιμοποίησε το DataStore (έκδοση Preferences):

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Παράδειγμα DataStore</span><span class="dots">···</span>
:::

```
val Context.dataStore by preferencesDataStore(name = "settings")

// Γράψιμο: αποθήκευση τιμής
suspend fun saveTheme(isDark: Boolean) {
    context.dataStore.edit { prefs ->
        prefs[THEME_KEY] = isDark
    }
}

// Διάβασμα: ανάκτηση τιμής (το Flow ειδοποιεί αυτόματα για αλλαγές)
val themeFlow: Flow<Boolean> = context.dataStore.data
    .map { it[THEME_KEY] ?: false }
```
:::

Πρόσεξε ότι επιστρέφεται ένα Flow — μια ροή δεδομένων που «ρέει». Μόλις αλλάξει η τιμή, όλα τα σημεία που την παρατηρούν λαμβάνουν αυτόματα τη νέα τιμή. Η έννοια αυτή (αντιδραστικότητα) είναι ακρογωνιαίος λίθος του σύγχρονου Android, και στο κεφάλαιο 54 θα την εφαρμόσεις στην πράξη.

#### 3. Room: να δώσεις στα δεδομένα «αληθινό σπίτι»

Ένα βιβλίο εξόδων έχει εκατοντάδες ή χιλιάδες εγγραφές, και χρειάζεται αναζητήσεις και στατιστικά ανά κατηγορία και ανά μήνα — αυτό θέλει βάση δεδομένων. Το Room είναι η επίσημη περιτύλιξη της SQLite και κάνει τη «δημιουργία πινάκων και την αναζήτηση δεδομένων» τόσο φυσική όσο το να γράφεις Kotlin. Χρειάζεσαι τρία πράγματα:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Τριάδα Room: Entity / Dao / Database</span><span class="dots">···</span>
:::

```
// 1. Entity: δομή πίνακα (ένας πίνακας = ένα data class)
@Entity(tableName = "records")
data class Record(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val amount: Double,
    val category: String,
    val note: String,
    val date: String
)

// 2. Dao: διεπαφή λειτουργιών (προσθήκη, διαγραφή, αλλαγή, αναζήτηση)
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

// 3. Database: τελική συναρμολόγηση
@Database(entities = [Record::class], version = 1)
abstract class AppDatabase : RoomDatabase() {
    abstract fun recordDao(): RecordDao
}
```
:::

Αυτό το πρότυπο «τρίο» μπορείς να το μεταφέρεις αυτούσιο σε οποιοδήποτε έργο σου — άλλαξε απλώς τα ονόματα των πεδίων. Τα ερωτήματα επιστρέφουν Flow και η διεπαφή ανανεώνεται αυτόματα μαζί με τα δεδομένα — μαγεία.

#### 4. Retrofit: να μιλάς με τον διακομιστή

Καιρός, ειδήσεις, συναλλαγματικές ισοτιμίες… αυτά τα δεδομένα δεν είναι μέσα στο κινητό, είναι στους διακομιστές των άλλων. Το Retrofit κάνει το «ζήτα δεδομένα από τον διακομιστή» τόσο απλό όσο μια κλήση συνάρτησης. Τρία βήματα:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Retrofit σε τρία βήματα</span><span class="dots">···</span>
:::

```
// 1. Ορισμός διεπαφής: το αίτημα HTTP γίνεται συνάρτηση
interface WeatherApi {
    @GET("v1/weather")
    suspend fun getWeather(@Query("city") city: String): WeatherResponse
}

// 2. Δημιουργία στιγμιότυπου
val api = Retrofit.Builder()
    .baseUrl("https://api.example.com/")
    .addConverterFactory(GsonConverterFactory.create())
    .build()
    .create(WeatherApi::class.java)

// 3. Κλήση σαν συνάρτηση (μέσα σε coroutine)
val result = api.getWeather("Πεκίνο")
```
:::

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Προσοχή στην παγίδα: δύο σιδερένιοι κανόνες δικτύου

{class="mt-1"}
① Τα αιτήματα δικτύου δεν πρέπει ποτέ να γίνονται στο κύριο νήμα — θα «παγώσουν» τη διεπαφή ή θα προκαλέσουν κατάρρευση (NetworkOnMainThreadException). Όλες οι κλήσεις δικτύου μπαίνουν μέσα σε coroutine (viewModelScope.launch). ② Το HTTP σε καθαρό κείμενο απαγορεύεται από προεπιλογή: από το Android 9 απαιτείται HTTPS. Αν για δοκιμές χρειαστείς τοπική διεύθυνση http://, πρέπει να δηλώσεις ρητά το usesCleartextTraffic στο Manifest — αλλά στο τελικό προϊόν όλα πρέπει να πηγαίνουν μέσω HTTPS.
:::

#### 5. Ανάλυση JSON: «μετάφρασε» τα δεδομένα δικτύου

Τα δεδομένα που επιστρέφει ο διακομιστής είναι ως επί το πλείστον JSON — ένα κείμενο που μοιάζει με «εμφωλευμένο λεξικό». Το Retrofit χρειάζεται έναν «διερμηνέα» για να τα μετατρέψει σε αντικείμενα Kotlin. Οι δύο κύριες λύσεις του 2026:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Λύση</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Χαρακτηριστικά</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Προτεινόμενη περίπτωση</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gson / Moshi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Κλασική λύση με reflection, μηδενικό κόστος ρύθμισης</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Γρήγορη εκκίνηση, μικρά έργα με λίγα πεδία</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">kotlinx.serialization</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Η επίσημη λύση χρόνου μεταγλώττισης, πιο γρήγορη και πιο ασφαλής</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Πρώτη επιλογή για νέα έργα (το κύριο ρεύμα του 2026)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Οι δύο μεγάλες λύσεις ανάλυσης JSON

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Παράδειγμα kotlinx.serialization</span><span class="dots">···</span>
:::

```
// Προσθήκη annotation @Serializable στο data class
@Serializable
data class WeatherResponse(
    val weather: List<Weather>,
    val main: Main,
    val name: String
)

// Το Retrofit συνδέει τον αντίστοιχο Converter (παράδειγμα με επίσημη υποστήριξη Retrofit 2.11+):
// .addConverterFactory(json.asConverterFactory("application/json".toMediaType()))
```
:::

Όποια λύση κι αν διαλέξεις, ο σιδερένιος κανόνας είναι: δες πρώτα το πραγματικό JSON που επιστρέφεται, μετά ορίσε τα πεδία. Πολλά bugs «αποτυχίας ανάλυσης» οφείλονται σε λάθος όνομα πεδίου ή λάθος μαντεμένο επίπεδο εμφωλής — τύπωσε το αρχικό JSON και σύγκρινε, και θα το εντοπίσεις σε δέκα δευτερόλεπτα.

#### 6. Coroutines: η «κοινή γλώσσα» του ταυτοχρονισμού στο Android

Τα suspend και launch που εμφανίζονται ξανά και ξανά παραπάνω προέρχονται από τα coroutines της Kotlin — την επίσημη λύση ταυτοχρονισμού του Android. Ας το πούμε χοντρικά: κάνουν τις λειτουργίες που «θέλουν λίγη αναμονή» (δίκτυο, βάση δεδομένων) να μην μπλοκάρουν τη διεπαφή.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Πρώτες γεύσεις από coroutine</span><span class="dots">···</span>
:::

```
// Εκκίνηση coroutine μέσα στο ViewModel
viewModelScope.launch {
    val records = dao.getAll().first()  // suspend: περιμένει αυτόματα χωρίς μπλοκάρισμα
    // Ενημέρωση της κατάστασης οθόνης……
}

// Συντομνύσεις λέξεων-κλειδιών:
// suspend   —— "πρέπει να περιμένω, μην με εμποδίζεις"
// launch    —— "Ξεκίνα τη δουλειά!"
// viewModelScope —— το "εργαστήριο" που ακολουθεί τη σελίδα, κλείνει μόνο του όταν η σελίδα καταστρέφεται
```
:::

Αν ξεκινάς από το μηδέν, αρκεί να θυμάσαι τη χρήση· την αρχή του «suspend και resume» που κρύβεται πίσω μπορείς να τη μελετήσεις αργότερα. Στην καθημερινή ανάπτυξη, το 90% όσων γράφεις είναι αυτό το πρότυπο.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Πρακτική άσκηση: φτιάξε μια μικρή εφαρμογή «φράση της ημέρας»

{class="mt-1"}
Βρες ένα δωρεάν API με αποφθέγματα (π.χ. κάτι σαν το hitokoto), τράβηξε με το Retrofit τη «φράση της ημέρας», δείξ’ τη στο κέντρο της οθόνης και πρόσθεσε κουμπί «άλλη μία» (νέο αίτημα μέσα σε coroutine). Μετά αποθήκευσε τις αγαπημένες φράσεις σε «αγαπημένα» με το Room. Η άσκηση αυτή χρησιμοποιεί ένα-ένα τα DataStore/Room/Retrofit/coroutines — μόλις την τελειώσεις, τα κεφάλαια 7 και 8 θα σου φανούν παιχνίδι.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Σύνοψη κεφαλαίου

- Ο στίχος: μικρές ρυθμίσεις στο DataStore, δεδομένα σε όγκο στο Room, εξωτερικά δεδομένα μέσω Retrofit
- Το DataStore επιστρέφει Flow: όταν αλλάζει η τιμή, οι παρατηρητές τη λαμβάνουν αυτόματα
- Το τρίο του Room: @Entity (πίνακας) + @Dao (λειτουργίες) + @Database (συνολική συναρμολόγηση) — πρότυπο άμεσα επαναχρησιμοποιήσιμο
- Τρία βήματα Retrofit: ορίζεις το interface → δημιουργείς instance → καλείς μέσα σε coroutine
- Δύο σιδερένιοι κανόνες: το δίκτυο δεν μπαίνει στο κύριο νήμα· το τελικό προϊόν απαιτεί HTTPS
- Coroutine = αναμονή που δεν μπλοκάρει τη διεπαφή· το viewModelScope είναι το προσωπικό εργαστήριο κάθε οθόνης
:::
