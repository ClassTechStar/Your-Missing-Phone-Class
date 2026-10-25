---
id: di-wu-shi-wu-zhang
num: 55
part: an-zhuo-kai-fa-pian
nav: Κεφάλαιο 55: Έργο 2 — Εφαρμογή αναζήτησης καιρού (δικτυακή έκδοση)
toc: default
kind: chapter
---

### Κεφάλαιο 55: Έργο 2 — Εφαρμογή αναζήτησης καιρού (δίκτυο)

{class="chapter-intro mb-4"}
Το βιβλίο εξόδων ήταν «εσωτερική εξάσκηση»· η εφαρμογή καιρού είναι «έξοδος στον κόσμο» — έχει να κάνει με το διαδίκτυο. Σε αυτό το έργο θα μάθεις: να κάνεις αίτηση για δωρεάν API, να αναλύεις JSON, να διαχειρίζεσαι τις τρεις καταστάσεις διεπαφής «φόρτωση/επιτυχία/αποτυχία», και πώς να κρύβεις καλά το κλειδί API. Όταν το τελειώσεις, θα έχεις την ικανότητα να φτιάχνεις οποιαδήποτε «συνδεδεμένη εφαρμογή» — ειδήσεις, ισοτιμίες, μετάφραση: ίδια συνταγή.

#### 1. Αίτηση για δωρεάν API καιρού

Για προσωπική εξάσκηση προτείνονται το OpenWeatherMap ή το QWeather (δημοφιλές στην Κίνα) — και τα δύο έχουν δωρεάν όριο, αρκεί να γραφτείς. Με παράδειγμα το OpenWeatherMap:

1. Δημιουργία λογαριασμού → στη σελίδα API keys δημιουργείς ένα κλειδί (apikey)·
2. Η δωρεάν έκδοση μπορεί να καλέσει το Current Weather (τρέχουσα πρόγνωση): api.openweathermap.org/data/2.5/weather? q=beijing&appid=ΤΟ_ΚΛΕΙΔΙ_ΣΟΥ&units=metric·
3. Δοκίμασέ το μια φορά στον browser και δες πώς μοιάζει το JSON που επιστρέφεται — αυτό είναι το υποχρεωτικό «διάβασμα» πριν συνδεθείς με οποιοδήποτε API.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Προσοχή στην παγίδα: το κλειδί δεν πρέπει ποτέ να γραφτεί σκληρά στον κώδικα

{class="mt-1"}
Το API Key είναι σαν τον «κωδικό του πορτοφολιού σου» — μόλις μπει σε κώδικα και γίνει commit στο GitHub, μέσα σε λίγες ώρες θα το αρπάξουν crawlers για κατάχρηση. Η σωστή μέθοδος: βάλ’ το στο local.properties (αρχείο που το gitignore αγνοεί ήδη) και διάβασέ το στον κώδικα μέσω του buildConfig του Gradle. Ψάξε «best practices για την απόκρυψη του API Key σε Android» και ακολούθησέ το.
:::

#### 2. Στρώμα δικτύου: Retrofit + ανάλυση JSON

Ορίσε πρώτα το «μοντέλο δεδομένων» σύμφωνα με το JSON που επιστρέφει το API· όσα πεδία δεν ταιριάζουν, αγνόησέ τα:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Μοντέλο δεδομένων + διεπαφή</span><span class="dots">···</span>
:::

```
// JSON: {"weather":[{"description":"Αίθριο"}],"main":{"temp":26.5,"humidity":40},"name":"Πεκίνο"}
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

Το Gson θα στρώσει αυτόματα το JSON σε αυτά τα data class — αρκεί τα ονόματα των πεδίων να ταιριάζουν και η μαγεία γίνεται μόνη της.

#### 3. Τρεις καταστάσεις διεπαφής: φόρτωση / επιτυχία / αποτυχία

Η ψυχή μιας συνδεδεμένης εφαρμογής είναι η «διαχείριση καταστάσεων». Αργό δίκτυο, αποσύνδεση, λάθος όνομα πόλης… για κάθε περίπτωση η διεπαφή πρέπει να δίνει απάντηση στον χρήστη. Εκφράσ’ το κομψά με ένα sealed class (σφραγισμένη κλάση):

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Κατάσταση οθόνης</span><span class="dots">···</span>
:::

```
sealed class UiState {
    object Loading : UiState()                    // περιστρέφεται
    data class Success(val data: WeatherResponse) : UiState()  // επιτυχία
    data class Error(val message: String) : UiState()          // αποτυχία
}

// Στο ViewModel:
fun search(city: String) {
    viewModelScope.launch {
        _state.value = UiState.Loading
        _state.value = try {
            UiState.Success(api.getWeather(city))
        } catch (e: Exception) {
            UiState.Error("Δεν βρήκα αυτή την πόλη, δοκίμασε άλλο όνομα;")
        }
    }
}

// Στην οθόνη:
when (val s = state) {
    is UiState.Loading -&gt; CircularProgressIndicator()   // περιστροφή
    is UiState.Success -&gt; WeatherContent(s.data)        // εμφάνιση
    is UiState.Error -&gt; Text(s.message)                 // εμφάνιση σφάλματος
}
```
:::

Το τριμερές Loading/Success/Error είναι το «πανάκεια πρότυπο» των συνδεδεμένων διεπαφών — μάθε το απ’ έξω και μετά, σε όλες τις συνδεδεμένες εφαρμογές, ακολούθησε το ίδιο σχήμα.

#### 4. Κώδικας διεπαφής στην πράξη: να ζωγραφίσεις τον καιρό

Με τις καταστάσεις έτοιμες, η διεπαφή μοιάζει έτσι (κρίσιμα αποσπάσματα):

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Οθόνη καιρού (κομμάτι-κλειδί)</span><span class="dots">···</span>
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
            data.weather.firstOrNull()?.description ?: "Άγνωστο",
            fontSize = 20.sp,
            color = Color.Gray
        )
        Spacer(Modifier.height(16.dp))
        Row {
            Text("💧 Υγρασία ${data.main.humidity}%")
            Spacer(Modifier.width(24.dp))
            Text("🌡️ Αίσθηση ${data.main.temp}°C")
        }
    }
}
```
:::

Μερικές λεπτομέρειες αξίζουν προσοχή: το firstOrNull() παίρνει με ασφάλεια το πρώτο στοιχείο (η λίστα μπορεί να είναι κενή), και το ?: "Άγνωστο" δίνει κείμενο εφεδρείας — η αρχή null-safety ισχύει και στη διεπαφή. Η θερμοκρασία με μεγάλο μέγεθος γραμματοσειράς 72.sp για εντύπωση και το ελαφρύ βάρος (Light) κάνουν τους αριθμούς κομψούς — κλασική συνταγή εφαρμογών καιρού.

#### 5. Λεπτομέρειες διεπαφής και αλληλεπίδρασης

- Πεδίο αναζήτησης: TextField στην κορυφή, γράφεις όνομα πόλης και πατάς αναζήτηση (με ενέργεια «αναζήτηση» στο πληκτρολόγιο — Enter και ψάχνει)·
- Κάρτα καιρού: θερμοκρασία σε μεγάλα γράμματα (26.5°), περιγραφή καιρού (ηλιοφάνεια), υγρασία, όνομα πόλης·
- Αγαπημένες πόλεις: αποθήκευσε τις πόλεις που κοιτάς συχνά στο DataStore, ώστε να αναζητούνται αυτόματα στο επόμενο άνοιγμα — και μια επανάληψη του κεφαλαίου 6 κάτω από το χέρι·
- Τράβηγμα για ανανέωση: στο Compose με το PullToRefreshBox (το δίνει το Material 3), και η αίσθηση γίνεται αμέσως «επαγγελματική».

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Συμβουλή: οι εικόνες ζωντανεύουν τη διεπαφή

{class="mt-1"}
Για κάθε είδος καιρού βάλε ένα emoji ή εικονίδιο (☀️🌧️❄️), με αντιστοίχιση when(description) — τρεις γραμμές κώδικα και η «θερμοκρασία» της διεπαφής διπλασιάζεται. Μπορείς και να φορτώσεις βιβλιοθήκη εικονιδίων καιρού τρίτων, αλλά στο στάδιο της εξάσκησης τα emoji αρκούν.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Πρακτική άσκηση: λίστα ελέγχου της εφαρμογής καιρού

{class="mt-1"}
① Η αναζήτηση καιρού δουλεύει κανονικά· ② με αποσύνδεση δικτύου, η εφαρμογή εμφανίζει κομψό σφάλμα χωρίς κατάρρευση (δοκίμασέ το σε λειτουργία πτήσης!)· ③ με ανύπαρκτη πόλη, φιλικό μήνυμα· ④ με δύο αγαπημένες πόλεις, να μένουν μετά από επανεκκίνηση της εφαρμογής· ⑤ με περιστροφή οθόνης να μη χάνεται η κατάσταση. Αν περάσουν και οι πέντε, το έργο «αποφοιτά».
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Σύνοψη κεφαλαίου

- Πρώτα δοκιμή του API στον browser και κατανόηση του JSON, μετά κώδικας — το «προπαρασκευαστικό διάβασμα» δεν χάνει ποτέ
- Το API Key κρύβεται στο local.properties, ποτέ μέσα στη βάση κώδικα
- Interface Retrofit + data class: με τα σωστά πεδία, το JSON αναλύεται αυτόματα
- Η τριμερής κατάσταση Loading/Success/Error είναι το πανάκεια των συνδεδεμένων διεπαφών
- Αποσύνδεση, κενή είσοδος, ανύπαρκτη πόλη — η διαχείριση σφαλμάτων είναι η βάση επιτυχίας κάθε συνδεδεμένης εφαρμογής
:::
