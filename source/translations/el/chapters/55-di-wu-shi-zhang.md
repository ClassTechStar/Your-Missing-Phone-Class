---
id: di-wu-shi-zhang
num: 50
part: an-zhuo-kai-fa-pian
nav: Κεφάλαιο 50: Kotlin σε γρήγορους ρυθμούς — η πρώτη γλώσσα για ανάπτυξη σε Android
toc: default
kind: chapter
---

### Κεφάλαιο 50: Kotlin με γρήγορο ρυθμό — η πρώτη γλώσσα της ανάπτυξης Android

{class="chapter-intro mb-4"}
Σε αυτό το κεφάλαιο μαθαίνουμε επίσημα τη γλώσσα. Μην αγχώνεσαι — το Kotlin είναι φημισμένο «φιλικό προς τους αρχάριους», και δεν χρειάζεται να απομνημονεύσεις βιβλίο σύνταξης: με το 20% της σύνταξης, μπορείς να διαβάσεις και να γράψεις το 80% της καθημερινής δουλειάς. Την υπόλοιπη θα τη ψάχνεις παράλληλα με τα projects. Κράτα την αρχή μάθησής μας: να καταλαβαίνεις > να απομνημονεύεις, να ξέρεις να το χρησιμοποιείς > να το έχεις τελειοποιήσει.

#### 1. Μεταβλητές και τύποι: δίνεις όνομα στα δεδομένα

Ένα πρόγραμμα είναι «δεδομένα + λογική». Η μεταβλητή είναι το όνομα με το οποίο αποθηκεύεις τα δεδομένα. Στο Kotlin υπάρχουν δύο τρόποι δήλωσης:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Μεταβλητές</span><span class="dots">···</span>
:::

```
val name = "Γιώργος"        // val: μεταβλητή μόνο για ανάγνωση (προτείνεται ως προεπιλογή)
var age = 18             // var: μεταβλητή που αλλάζει (μπορεί να ξαναγραφτεί)

age = 19                 // <i class="fas fa-check-circle mr-1"></i> var αλλάζει
// name = "Νίκος"         // <i class="fas fa-times-circle mr-1"></i> val δεν αλλάζει, σφάλμα μεταγλώττισης

val score: Int = 100     // μπορείς και να γράψεις τον τύπο ρητά
val pi = 3.14            // και χωρίς αυτόν γίνεται αυτόματη εξαγωγή
```
:::

Οι συνηθισμένοι τύποι είναι λίγοι — τους θυμάσαι με έναν πίνακα:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Τύπος</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Τι αποθηκεύει</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Παράδειγμα</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Int</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ακέραιος</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">42</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Double</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Δεκαδικός</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3.14</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">String</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Κείμενο</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"Γεια σου"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Boolean</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Αλήθεια/ψέμα</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">true / false</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">List&lt; T&gt;</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Μια συλλογή δεδομένων</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">listOf(1, 2, 3)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Συνηθισμένοι βασικοί τύποι του Kotlin

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Συμβουλή: η αρχή του «val πρώτα»

{class="mt-1"}
Ο σιδερένιος κανόνας της κοινότητας Kotlin: προεπιλογή val, var μόνο όταν πραγματικά χρειάζεται. Αν χρησιμοποιήσεις var όπου θα έπρεπε val, το IDE θα σε προειδοποιήσει με κίτρινη επισήμανση. Αυτή η συνήθεια σε γλιτώνει από μια ολόκληρη κατηγορία bugs του τύπου «η μεταβλητή άλλαξε κατά λάθος» — όσο λιγότερο μεταβάλλεται ο κώδικας, τόσο πιο εύκολα τον σκέφτεσαι λογικά.
:::

#### 2. Συναρτήσεις: πακετάρεις τη λογική σε «κουμπί»

Η συνάρτηση είναι ένα κομμάτι λογικής με όνομα, σαν κουμπί στο τηλεχειριστήριο — το πατάς (την καλείς) και εκτελεί μια σειρά ενεργειών. Στο Kotlin δηλώνεται με fun:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Συναρτήσεις</span><span class="dots">···</span>
:::

```
fun greet(name: String): String {
    return "Γεια σου, $name!"     // το σύμβολο $ εισάγει τη μεταβλητή στο αλφαριθμητικό
}

println(greet("Γιώργος"))        // Έξοδος: Γεια σου, Γιώργο!

// Μονογραμμικές συναρτήσεις γράφονται ως εκφράσεις
fun add(a: Int, b: Int) = a + b

println(add(3, 5))            // Έξοδος: 8
```
:::

Μερικά κλειδιά: οι παράμετροι γράφονται μέσα σε παρένθεση (πρώτα το όνομα, μετά ο τύπος, χωρισμένα με άνω-κάτω τελεία)· ο τύπος επιστροφής γράφεται μετά την παρένθεση· και το string template $όνομα Μεταβλητής είναι η εμβληματική ευκολία του Kotlin — δεν χρειάζεται να «κολλάς» string και μεταβλητές με + όπως στη Java.

#### 3. Συνθήκες και βρόχοι: το πρόγραμμα «σκέφτεται»

Η «ευφυΐα» του προγράμματος προέρχεται από δύο πράγματα: να κρίνει (if/when) και να επαναλαμβάνει (for/while).

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Συνθήκες και βρόχοι</span><span class="dots">···</span>
:::

```
// Έλεγχος: if / else
val age = 17
if (age >= 18) {
    println("Ενήλικας")
} else {
    println("Ανήλικος")
}

// Πολλαπλοί κλάδοι: when (εκατοντάδες φορές πιο βολικό από το switch)
val score = 85
val level = when {
    score >= 90 -> "Άριστα"
    score >= 60 -> "Βάση"
    else -> "Συνέχεια, μπροστά!"
}

// Επανάληψη: βρόχος for
val fruits = listOf("μήλο", "μπανάνα", "πορτοκάλι")
for (fruit in fruits) {
    println("Μου αρέσει να τρώω$fruit")
}
```
:::

Το when είναι ο πιο συνηθισμένος τρόπος πολλαπλής διακλάδωσης στο Kotlin — στην ανάπτυξη Android θα το χρησιμοποιείς καθημερινά (π.χ. να εμφανίζεις διαφορετική οθόνη ανάλογα με την κατάσταση).

#### 4. Null safety: το «χαρτί ζωής» του Kotlin

Το πιο διάσημο bug της εποχής Java λέγεται NullPointerException («εξαίρεση κενού δείκτη») — το πρόγραμμα προσπελάζει κάτι που «δεν υπάρχει» και καταρρέει αμέσως. Σύμφωνα με τα στατιστικά, είναι χρόνια πρώτο στη λίστα των crashes του Android. Το Kotlin το λύνει σε επίπεδο γλώσσας: προεπιλεγμένα δεν επιτρέπει null τιμές.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Null Safety</span><span class="dots">···</span>
:::

```
var name: String = "Γιώργος"   // Συνηθισμένος τύπος: ποτέ null
// name = null                // <i class="fas fa-times-circle mr-1"></i> Σε σταματάει κατευθείαν ο compiler

var nickname: String? = null // με ερωτηματικό: επιτρέπεται null
nickname = "Μπαμπής"

// Με nullable type, η διαχείριση πρέπει να είναι ασφαλής:
println(nickname?.length)    // safe call: null επιστρέφει null, χωρίς κρασ
val len = nickname?.length ?: 0   // Elvis operator: σε null δίνει προεπιλογή
println(len)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Προσοχή: μην μπερδέψεις το ? με το ?:

{class="mt-1"}
Το String? σημαίνει «επιτρέπεται null», ενώ το a ?: b σημαίνει «αν το a είναι null, χρησιμοποίησε το b» (μοιάζει με τα μαλλιά του Elvis, γι' αυτό λέγεται τελεστής Elvis). Όταν ξεκινάς και βλέπεις από τον compiler σφάλμα που αφορά null, κατά τα δύο τρίτα έχεις ξεχάσει να χειριστείς nullable τύπο — και αυτό ακριβώς είναι η γλώσσα που σε προστατεύει.
:::

#### 5. Κλάσεις και αντικείμενα: το «καλούπι» που φτιάχνει «τεμάχια»

Η κλάση είναι το «καλούπι» και το αντικείμενο το «προϊόν» που βγαίνει από αυτό. Στο Android όλα — σελίδες, κουμπιά, δεδομένα — είναι αντικείμενα. Στο Kotlin υπάρχει ένα εργαλείο-θαύμα, το data class (κλάση δεδομένων), ειδικό για «να κουβαλάει δεδομένα»: μια γραμμή αναπληρώνει δεκάδες στη Java:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Κλάσεις και data classes</span><span class="dots">···</span>
:::

```
// Συνηθισμένη κλάση: καλούπι
class Dog(val name: String) {
    fun bark() = println("$name γαβ γαβ!")
}

val dog = Dog("Λάκης")      // Δημιουργία αντικειμένου
dog.bark()                 // Λάκης γαβ γαβ!

// data class: κουτί με δεδομένα (έτοιμα equals/copy κ.λπ.)
data class User(val id: Int, val name: String, val email: String)

val me = User(1, "Γιώργος", "zhangsan@example.com")
val twin = me.copy(name = "Γιώργος Παπαδόπουλος")   // Αντιγραφή με αλλαγή ενός πεδίου
```
:::

Αργότερα, όταν φτιάξεις λογιστήριο εξόδων, κάθε εγγραφή θα είναι ένα data class: data class Record(val amount: Double, val category: String, val date: String). Βλέπεις; Μπορείς ήδη να γράψεις τη δομή κώδικα ενός πραγματικού project.

#### 6. Lambda και συναρτήσεις υψηλότερης τάξης: τα «συντακτικά γλυκά» του Kotlin

Στον κώδικα Android θα βλέπεις συνέχεια { ... } — «συναρτήσεις χωρίς όνομα», που λέγονται lambda (ανώνυμες συναρτήσεις). Το onClick = { count++ } του Button είναι μια lambda — «πακετάρει» το «τι θα γίνει μετά το κλικ» και το παραδίδει στο κουμπί.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Πρώτες γεύσεις από lambda</span><span class="dots">···</span>
:::

```
// Συνηθισμένος τρόπος: ορίζουμε επώνυμη συνάρτηση και μετά την περνάμε
fun double(x: Int) = x * 2
val result = listOf(1, 2, 3).map(::double)

// Με lambda: ορισμός επί τόπου, κομψά και άμεσα
val result2 = listOf(1, 2, 3).map { it * 2 }   // it = τρέχον στοιχείο

// Φίλτρο + μετασχηματισμός σε σύνδεση (πολύ συνηθισμένο σε πραγματικά έργα)
val bills = listOf(12.5, 88.0, 5.0, 200.0)
val bigBills = bills.filter { it > 50 }.sorted()
// [88.0, 200.0]—"τα τιμολόγια άνω των 50, ταξινομημένα"
```
:::

Κράτα μερικές συχνές «συνδυαστικές κινήσεις» για συλλογές: filter (φιλτράρισμα), map (μετασχηματισμός), sorted (ταξινόμηση), sum (άθροισμα). Το 90% της επεξεργασίας λιστών που θα κάνεις στο μέλλον είναι συνδυασμός αυτών των τεσσάρων. Η φιλοσοφία του Kotlin είναι: ό, τι λέγεται με μία φράση, μην το γράφεις με πέντε.

#### 7. Κάρτα σύνταξης γραμμένη για αρχάριους

Μην προσπαθείς να απομνημονεύσεις όλη τη σύνταξη σε μια μέρα. Κράτα την κάρτα και συμβουλεύεσαι την όσο γράφεις κώδικα — σε δύο εβδομάδες θα σου είναι φυσική:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Τι θες να κάνεις</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Πώς γράφεται</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Δήλωση μεταβλητής μόνο για ανάγνωση</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">val x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Δήλωση μεταβλητής που αλλάζει</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">var x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Δήλωση συνάρτησης</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">fun όνομα(παράμετροι): τύπος Επιστροφής { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Συνθήκη</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if (συνθήκη) {...} else {...}</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Πολλαπλή διακλάδωση</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">when { συνθήκη -> αποτέλεσμα }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Επανάληψη</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">for (x in λίστα) { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ένωση string</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"Γεια σου, $name"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Χειρισμός nullable τιμών</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">x?.length ?: 0</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Δήλωση data class</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">data class X(val a: Int, val b: String)</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Κάρτα γρήγορης αναφοράς σύνταξης Kotlin (για αρχάριους)

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Σειρά σου: παίξε 10 λεπτά Kotlin χωρίς να εγκαταστήσεις τίποτα

{class="mt-1"}
Άνοιξε το play.kotlinlang.org στον browser (το επίσημο online playground του Kotlin), επικόλλησε και τρέξε κάθε κομμάτι κώδικα του κεφαλαίου, άλλαξε νούμερα και κείμενα και δες πώς αλλάζει η έξοδος. Αυτά τα 10 λεπτά «πρώτα παίξε, μετά μάθε» θα σου κάνουν την εκκίνηση στο κεφάλαιο 51 πολύ πιο εύκολη.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Σύνοψη κεφαλαίου

- val πρώτα, var με φειδώ· οι τύποι μπορούν να συνάγονται αυτόματα, αλλά μπορείς και να τους δηλώσεις ρητά μετά το άνω-κάτω τελεία
- Συνάρτηση = πακεταρισμένη λογική· το string template $ είναι η εμβληματική ευκολία
- if/when για κρίσεις, for για βρόχους· το when είναι ο «πανκαλωτήρας» της ανάπτυξης Android
- Το null safety είναι το «χαρτί ζωής» του Kotlin: ο κανονικός τύπος δεν δέχεται null, ο nullable τύπος χρειάζεται υποχρεωτικά ? / ?:
- Το data class είναι το κουτί για τα δεδομένα: ένα πεδίο ανά γραμμή, καθημερινό εργαλείο σε πραγματικά projects
- 20% σύνταξη κάνει το 80% της δουλειάς: πρώτα να ξέρεις να το χρησιμοποιείς, μετά να το εξειδικεύεις
:::
