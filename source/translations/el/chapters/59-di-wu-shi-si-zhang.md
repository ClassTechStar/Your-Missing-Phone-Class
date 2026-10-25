---
id: di-wu-shi-si-zhang
num: 54
part: an-zhuo-kai-fa-pian
nav: Κεφάλαιο 54: Έργο 1 — Το βιβλίο εξόδων μου (τοπική έκδοση)
toc: default
kind: chapter
---

### Κεφάλαιο 54: Έργο 1 — Το βιβλίο εξόδων μου (τοπική έκδοση)

{class="chapter-intro mb-4"}
Καλώς ήρθες στο πρώτο σου «κανονικό» έργο. Αυτό το βιβλίο εξόδων, παρότι δεν συνδέεται στο διαδίκτυο, είναι πλήρες σε όλα: καταγράφει συναλλαγή, δείχνει την κίνηση, κάνει μηνιαία στατιστικά, επιτρέπει διαγραφή και αλλαγή. Όταν το τελειώσεις, θα έχεις περπατήσει ολόκληρη τη διαδρομή «δεδομένα → λογική → διεπαφή». Μη βιάζεσαι να αντιγράψεις κώδικα — πρώτα σκέψου καθαρά, μετά δράσε· αυτός είναι ο μόνιμος κανόνας μας.

#### 1. Σκέψη απαιτήσεων: ρώτα πρώτα πέντε ερωτήσεις

Πριν πας στη δράση, ξεκαθάρισε την ιδέα με τα «πέντε στοιχεία απαιτήσεων»:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Στοιχείο</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Απάντηση</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who (για ποιον)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Για μένα — και για οικογένεια και φίλους</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What (τι κάνει)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Καταγραφή εσόδων-εξόδων, προβολή κίνησης, μηνιαία σύνοψη, στατιστικά ανά κατηγορία</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why (γιατί)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Εξάσκηση + να καταλάβω πού πάνε τα λεφτά μου</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How (πώς)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin + Compose + Room + MVVM, αμιγώς τοπικό χωρίς backend</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint (περιορισμοί)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ολοκλήρωση μέσα σε μία εβδομάδα· ελάχιστη υποστήριξη Android 8· έστω χωρίς δημοσίευση, να γράφεται με πρότυπα δημοσίευσης</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Τα πέντε στοιχεία απαιτήσεων του βιβλίου εξόδων

Μετά σπά’ το σε μικρά βήματα «κάθε ένα χρήσιμο από μόνο του»: ① φτιάξε το στρώμα δεδομένων Room (να αποθηκεύει μια εγγραφή)· ② σελίδα λίστας (να βλέπεις την κίνηση)· ③ σελίδα καταχώρησης (να προσθέτεις εγγραφές)· ④ διαγραφή και επεξεργασία· ⑤ κάρτα μηνιαίας σύνοψης. Σε κάθε βήμα που ολοκληρώνεις, η εφαρμογή είναι ήδη κάτι «χρήσιμο».

#### 2. Στρώμα δεδομένων: να πάρουν οι «εγγραφές» σπίτι

Ορίσε πρώτα πώς μοιάζει μια εγγραφή — τα πεδία ας φτάνουν για τις ανάγκες, χωρίς απληστία:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Record.kt (οντότητα)</span><span class="dots">···</span>
:::

```
@Entity(tableName = "records")
data class Record(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val type: String,        // "income" έσοδο | "expense" έξοδο
    val amount: Double,      // Ποσό (γιουάν)
    val category: String,    // Κατηγορία: φαγητό, μετακινήσεις, μισθός……
    val note: String = "",   // Σημείωση (προαιρετικό)
    val date: String         // "2026-08-15"
)
```
:::

Στο Dao πρόσθεσε δύο ερωτήματα «για στατιστικά» — αυτή είναι η ψυχή του βιβλίου εξόδων:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · RecordDao.kt (ερωτήματα στατιστικών)</span><span class="dots">···</span>
:::

```
@Dao
interface RecordDao {
    @Query("SELECT * FROM records ORDER BY date DESC, id DESC")
    fun getAll(): Flow&lt;List&lt;Record&gt;&gt;

    @Insert
    suspend fun insert(record: Record)

    @Delete
    suspend fun delete(record: Record)

    @Query("SELECT COALESCE(SUM(amount),0) FROM records WHERE type='income' AND date LIKE :month || '%'")
    suspend fun monthIncome(month: String): Double   // month σε μορφή "2026-08"

    @Query("SELECT COALESCE(SUM(amount),0) FROM records WHERE type='expense' AND date LIKE :month || '%'")
    suspend fun monthExpense(month: String): Double
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Συμβουλή: γιατί το ποσό είναι Double;

{class="mt-1"}
Τα αυστηρά χρηματοοικονομικά προϊόντα χρησιμοποιούν BigDecimal ή «Int σε μονάδες λεπτών (cents)» για να αποφύγουν σφάλματα κινητής υποδιαστολής (το παλιό πρόβλημα 0.1+0.2≠0.3). Για έργο εξάσκησης το Double αρκεί· αν κάποτε φτιάξεις πραγματικό χρηματοοικονομικό προϊόν, θυμήσου να αλλάξεις σε μονάδα «λεπτά» — είναι παγίδα στην οποία έχουν πέσει αμέτρητοι προηγούμενοι.
:::

#### 3. MVVM: διεπαφή και λογική «χωρίζουν σπίτια»

Να αφήσεις τη διεπαφή να μιλάει απευθείας με τη βάση; Θα τρέχει, αλλά ο κώδικας της διεπαφής γίνεται ατελείωτος και ακομψός. Η αρχιτεκτονική MVVM μοιράζει καθήκοντα: η View (διεπαφή) μόνο ζωγραφίζει, το ViewModel (κέντρο λογικής) διαχειρίζεται τα δεδομένα, το Model (Room) την αποθήκευση.

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> View (οθόνη Compose)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> ViewModel (κατάσταση και λογική)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-database mr-1"></i> Model (στρώμα δεδομένων Room)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Εικόνα 5: Η τριών επιπέδων δομή του MVVM — τα δεδομένα ρέουν προς μία κατεύθυνση και κάθε επίπεδο μένει στα σύνορά του
:::

::: div .code-block
:::inline div .code-head
<span>KOTLIN · RecordViewModel.kt (σκελετός)</span><span class="dots">···</span>
:::

```
class RecordViewModel(private val dao: RecordDao) : ViewModel() {

    // Μετατροπή Flow σε κατάσταση παρατηρήσιμη από την οθόνη
    val records = dao.getAll()
        .stateIn(viewModelScope, SharingStarted.WhileSubscribed(), emptyList())

    // Ενέργεια χρήστη: κλήση συνάρτησης suspend
    fun addRecord(type: String, amount: Double, category: String, note: String, date: String) {
        viewModelScope.launch {
            dao.insert(Record(type = type, amount = amount,
                category = category, note = note, date = date))
        }
    }

    fun deleteRecord(record: Record) {
        viewModelScope.launch { dao.delete(record) }
    }
}
```
:::

Στη διεπαφή (Compose) το χρησιμοποιείς έτσι: val vm: RecordViewModel = viewModel(), και μετά val list by vm.records.collectAsState() — μόλις αλλάξουν τα δεδομένα, η λίστα ανανεώνεται μόνη της και εσύ δεν χρειάζεται να κάνεις τίποτα. Αυτή είναι η δύναμη της συνεργασίας MVVM + Flow + Compose.

#### 4. Διεπαφή: σελίδα λίστας + σελίδα καταχώρησης

Για τη λίστα χρησιμοποίησε LazyColumn (τεμπέλικη λίστα) — όσα κι αν είναι τα δεδομένα, δεν κολλάει:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Σελίδα λίστας λογιστηρίου (κομμάτι-κλειδί)</span><span class="dots">···</span>
:::

```
@Composable
fun RecordListScreen(vm: RecordViewModel) {
    val records by vm.records.collectAsState()

    Column {
        // Κάρτα σύνοψης πάνω (έσοδα-έξοδα=υπόλοιπο)
        SummaryCard(records)

        // Λίστα κινήσεων
        LazyColumn {
            items(records, key = { it.id }) { record -&gt;
                RecordRow(record) { vm.deleteRecord(record) }
            }
        }

        // Πλωτό κουμπί "Καταγραφή" → διάλογος εισαγωγής
        FloatingActionButton(onClick = { showAddDialog = true }) {
            Text("+")
        }
    }
}

@Composable
fun RecordRow(record: Record, onDelete: () -&gt; Unit) {
    Row(Modifier.fillMaxWidth().padding(12.dp)) {
        Text(record.category, fontWeight = FontWeight.Bold)
        Spacer(Modifier.weight(1f))
        Text(if (record.type == "income") "+${record.amount}" else "-${record.amount}",
             color = if (record.type == "income") Color(0xFF27AE60) else Color(0xFFC0392B))
    }
}
```
:::

Για την καταχώρηση, το AlertDialog (διάλογος) είναι το πιο βολικό: μερικά πεδία εισαγωγής + εναλλαγή έσοδο/έξοδο + λίστα κατηγοριών, και με «ΟΚ» καλείς το vm.addRecord(...).

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Προσοχή: μην τεμπελιάζεις με την επικύρωση εισόδου

{class="mt-1"}
Το πεδίο ποσού πρέπει οπωσδήποτε να επικυρώνεται: κενή τιμή, αρνητικός αριθμός και μη έγκυρες είσοδοι όπως «abc» πρέπει να μπλοκάρονται (έλεγξε με toDoubleOrNull()). Από τις πιο συχνές αιτίες κατάρρευσης εφαρμογών είναι το «να θεωρήσουμε την εισαγωγή του χρήστη καλό παιδί». Θυμήσου: ό, τι πληκτρολογεί ο χρήστης, έλεγχέ το σαν εχθρό.
:::

#### 5. Επεξεργασία και διαγραφή: τα δεδομένα να «μπαίνουν και να βγαίνουν»

Ένα βιβλίο εξόδων που μόνο προσθέτει και δεν διαγράφει, σε τρεις μέρες γίνεται άχρηστο. Πρόσθεσε δύο λειτουργίες:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Διαγραφή και επεξεργασία</span><span class="dots">···</span>
:::

```
// Δύο ακόμα συναρτήσεις στο Dao:
@Query("UPDATE records SET amount=:amount, category=:category, note=:note WHERE id=:id")
suspend fun update(id: Long, amount: Double, category: String, note: String)

@Query("DELETE FROM records WHERE id=:id")
suspend fun deleteById(id: Long)

// Στην οθόνη: παρατεταμένο πάτημα στοιχείου για μενού "επεξεργασία/διαγραφή" (Compose με DropdownMenu ή AlertDialog)
// Πριν τη διαγραφή, καλύτερα διάλογος επιβεβαίωσης—η "κατά λάθος διαγραφή" είναι ό, τι πιο μισημένο για χρήστες λογιστηρίου
```
:::

Δύο εμπειρίες για τις λεπτομέρειες αλληλεπίδρασης: η διαγραφή θέλει δεύτερη επιβεβαίωση (για να μην πατήσεις κατά λάθος), και η επεξεργασία να προ-συμπληρώνει τις αρχικές τιμές όσο γίνεται (η αλλαγή ενός γράμματος είναι πιο εύκολη από την επανεισαγωγή). Μην υποτιμάς αυτές τις λεπτομέρειες — η «αίσθηση προϊόντος» χτίζεται από τέτοιες λεπτομέρειες.

#### 6. Αποδοχή: έλεγχος σε τρία επίπεδα + δύο προχωρημένες προκλήσεις

Μόλις τελειώσει το έργο, κάνε αποδοχή σε τρία επίπεδα «λειτουργικότητα → όρια → αρχιτεκτονική»: μπορείς να καταγράφεις, να διαγράφεις, και τα δεδομένα μένουν μετά από επανεκκίνηση της εφαρμογής (λειτουργικότητα)· με ποσό 0 ή αρνητικό καταρρέει; με περιστροφή οθόνης χάνονται δεδομένα; (όρια)· διεπαφή και δεδομένα είναι ανακατεμένα; υπάρχουν πεδία σκληρά κωδικοποιημένα; (αρχιτεκτονική).

Αφού περάσει η αποδοχή της βασικής έκδοσης, βάλ’ στον εαυτό σου δύο «πιάτα για προχωρημένους»:

1. Μηνιαίο φίλτρο: εναλλαγή μήνα στην κορυφή (π.χ. 2026-08 ▾) και η λίστα να δείχνει μόνο την κίνηση του τρέχοντος μήνα·
2. Πίτα κατηγοριών: με το Canvas του Compose ή με μια ελαφριά βιβλιοθήκη γραφημάτων, ζωγράφισε το «πού πάνε τα λεφτά» σε διάγραμμα πίτας — μόλις το κάνεις, το βιβλίο εξόδων αρχίζει να «μοιάζει προϊόν».

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Πρακτική άσκηση: ολοκλήρωσέ το αυτή την εβδομάδα

{class="mt-1"}
Δούλεψε με τη σειρά «στρώμα δεδομένων → ViewModel → σελίδα λίστας → σελίδα καταχώρησης → κάρτα σύνοψης», ένα βήμα τη μέρα. Αν κολλήσεις, ρίξε το μήνυμα σφάλματος αυτούσιο σε μηχανή αναζήτησης ή AI (θυμάσαι το Μέρος 7 «Πρακτικός Προγραμματισμός με AI»; όταν περιγράφεις ένα πρόβλημα, ανέφερε καθαρά «αναμενόμενη συμπεριφορά, πραγματική συμπεριφορά, βήματα αναπαραγωγής»). Μόλις τελειώσεις, χρησιμοποίησέ το για μια εβδομάδα καταγραφές — όταν χρησιμοποιείς εφαρμογή που έφτιαξες μόνος σου, η ικανοποίηση σε σπρώχνει να συνεχίσεις.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Σύνοψη κεφαλαίου

- Πέντε στοιχεία απαιτήσεων → σπάσιμο σε μικρά βήματα «κάθε βήμα χρήσιμο», και μετά δράση
- Στρώμα δεδομένων: οντότητα Record + Dao (με SQL στατιστικών ανά μήνα) + Database
- Καταμερισμός MVVM: η View μόνο ζωγραφίζει, το ViewModel τη λογική, το Model την αποθήκευση
- Flow + stateIn + collectAsState: μόλις αλλάξουν τα δεδομένα, η διεπαφή ανανεώνεται αυτόματα
- LazyColumn για τη λίστα· AlertDialog για την καταχώρηση
- Αποδοχή σε τρία επίπεδα (λειτουργικότητα/όρια/αρχιτεκτονική) + προχωρημένες προκλήσεις (μηνιαίο φίλτρο, πίτα κατηγοριών)
:::
