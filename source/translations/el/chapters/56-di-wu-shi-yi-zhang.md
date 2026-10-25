---
id: di-wu-shi-yi-zhang
num: 51
part: an-zhuo-kai-fa-pian
nav: Κεφάλαιο 51: Ανάπτυξη διεπαφών — πρώτα βήματα με Jetpack Compose
toc: default
kind: chapter
---

### Κεφάλαιο 51: Ανάπτυξη διεπαφής — πρώτα βήματα με το Jetpack Compose

{class="chapter-intro mb-4"}
Η διεπαφή είναι ό, τι βλέπει ο χρήστης. Πριν εμφανιστεί το Compose, οι διεπαφές του Android γράφονταν σε XML — κουραστικές, σαν ασκήσεις συμπλήρωσης κενών. Το 2021 η Google κυκλοφόρησε το Jetpack Compose: σχεδιάζεις τη διεπαφή απευθείας με κώδικα Kotlin, βλέπεις αυτό που παίρνεις, και με κάθε αλλαγή γραμμής η προεπισκόπηση ανανεώνεται αμέσως. Το 2026 το Compose είναι ήδη η απόλυτη mainstream επιλογή για νέα projects. Σε αυτό το κεφάλαιο μαθαίνουμε να «ζωγραφίζουμε».

#### 1. Η ιδέα του Compose: η διεπαφή είναι συνάρτηση

Η βασική ιδέα του Compose σε μία φράση: διεπαφή = συνάρτηση. Ό, τι εμφανίζεται στην οθόνη (κείμενο, κουμπί, εικόνα) είναι μια «συνάρτηση σύνθεσης» (Composable), σημειωμένη με @Composable. Τις ενθέτεις η μία μέσα στην άλλη σαν τουβλάκια — αυτό είναι η διεπαφή.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Η πρώτη σου οθόνη Compose</span><span class="dots">···</span>
:::

```
@Composable
fun Greeting(name: String) {
    Text(text = "Γεια σου, $name!")     // Ενα "κομμάτι κειμένου"
}

// Φωλιάσμα: μεγάλα κομμάτια περιέχουν μικρά
@Composable
fun HomeScreen() {
    Column {                          // Κατακόρυφη διάταξη
        Greeting(name = "Γιώργος")
        Greeting(name = "Νίκος")
        Button(onClick = { /* τι γίνεται στο πάτημα */ }) {
            Text("Πάτα με")
        }
    }
}
```
:::

Πρόσεξε το «καπέλο» @Composable — λέει στον compiler «αυτό είναι ένα τουβλάκι διεπαφής». Τα τουβλάκια μπορούν να ενθέτονται απεριόριστα — αυτό είναι όλο το μυστικό του Compose.

#### 2. Βασικά components: κείμενο, κουμπί, πεδίο εισαγωγής, εικόνα

Τα components του Compose είναι «τουβλάκια»· τα πιο συνηθισμένα είναι τέσσερα:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Component</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Τι κάνει</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Απαραίτητες παράμετροι</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Εμφανίζει κείμενο</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">text (το κείμενο που εμφανίζεται)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Κουμπί</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onClick (callback στο πάτημα)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Πεδίο εισαγωγής</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">value, onValueChange (callback για αλλαγή της εισόδου)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Image</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Εμφανίζει εικόνα</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">painter (πόρος εικόνας)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Τα τέσσερα βασικά components του Compose

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Παράδειγμα βασικών στοιχείων</span><span class="dots">···</span>
:::

```
@Composable
fun BasicWidgets() {
    Column {
        Text(text = "Κείμενο εδώ")
        Button(onClick = { println("Πατήθηκε") }) {
            Text("Κουμπί")
        }
        var input by remember { mutableStateOf("") }
        TextField(
            value = input,
            onValueChange = { input = it },
            label = { Text("Γράψε κάτι") }
        )
    }
}
```
:::

Στις δύο γραμμές του πεδίου εισαγωγής εμφανίζεται το remember { mutableStateOf("") } — αυτή είναι η «μαγεία της κατάστασης» (state) του Compose, θα τη δούμε αναλυτικά στην 5 η ενότητα του κεφαλαίου. Για την ώρα, απλώς να τη γνωρίσεις.

#### 3. Το τρίπτυχο των layouts: Column, Row, Box

Τώρα που έχεις components, πώς τα τοποθετείς; Θυμήσου τρία «κουτιά»:

- Column: τοποθετεί κάθετα (σαν ουρά για φαγητό)·
- Row: τοποθετεί οριζόντια (σαν να κάθεστε πλάι-πλάι)·
- Box: τα βάζει το ένα πάνω στο άλλο (σαν στοιβαγμένα τραπουλόχαρτα· ταιριάζει για badge και επικάλυψεις).

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Τριάδα layout</span><span class="dots">···</span>
:::

```
Column {
    Text("Πρώτη γραμμή")
    Row {
        Text("Αριστερά")
        Text("Δεξιά")
    }
    Box {
        Text("Κάτω στρώμα")
        Text("Ετικέτα σε επικάλυψη πάνω")
    }
}
```
:::

Θέλεις πιο όμορφη διάταξη; Πρόσθεσε στα components ένα Modifier (τροποποιητή) — είναι σαν να «βάφεις» τα τουβλάκια:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Χρήσιμα κόλπα Modifier</span><span class="dots">···</span>
:::

```
Text(
    text = "Όμορφο κείμενο",
    modifier = Modifier
        .padding(16.dp)          // περιθώριο γύρω-γύρω
        .fillMaxWidth()          // γεμίζει το πλάτος
        .background(Color.Blue)  // χρώμα φόντου
        .clickable { /* πάτημα */ }// με κλικ
)
// Αλυσιδωτά: το ένα μετά το άλλο, η σειρά μετράει (πρώτα padding μετά φόντο, το φόντο δεν περιλαμβάνει τα περιθώρια)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Προσοχή: η σειρά του Modifier έχει σημασία

{class="mt-1"}
Το padding(16.dp).background(Blue) και το background(Blue).padding(16.dp) δεν δίνουν το ίδιο αποτέλεσμα — το πρώτο είναι «πρώτα κενό, μετά χρώμα» (το background δεν περιλαμβάνει το padding), το δεύτερο «πρώτα χρώμα, μετά κενό» (το background περιλαμβάνει το padding). Εδώ οι αρχάριοι ζωγραφίζουν συχνά «περίεργα λευκά περιθώρια». Όταν δεν είσαι σίγουρος/η, άλλαξε τη σειρά και δοκίμασε — η προεπισκόπηση θα σου δώσει αμέσως την απάντηση.
:::

#### 4. State: η διεπαφή «ζωντανεύει»

Η στατική διεπαφή δεν έχει ενδιαφέρον. Αν θες το νούμερο να ανεβαίνει +1 όταν πατάς το κουμπί και το πεδίο εισαγωγής να δέχεται πληκτρολόγηση, χρειάζεσαι state (κατάσταση). Ο κανόνας του Compose: η διεπαφή αντανακλά πάντα πιστά το state· όταν αλλάζει το state, η διεπαφή ξαναζωγραφίζεται αυτόματα.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Κατάσταση: μετρητής πατημάτων</span><span class="dots">···</span>
:::

```
@Composable
fun Counter() {
    // remember + mutableStateOf: θυμάται αυτή την τιμή που αλλάζει
    var count by remember { mutableStateOf(0) }

    Column {
        Text(text = "Έχεις πατήσει $count φορές")
        Button(onClick = { count++ }) {   // αλλαγή κατάστασης
            Text("Πάτα με +1")                // η οθόνη ανανεώνεται μόνη της
        }
    }
}
```
:::

Τρεις γραμμές κώδικα, ένας ζωντανός μετρητής. Εδώ είναι το «γλυκό» του Compose σε σχέση με την παλιά γραφή: δεν χρειάζεται να «ανανεώνεις τη διεπαφή» με το χέρι — αρκεί να αλλάζεις τα δεδομένα. Κράτα δύο βασικές συναρτήσεις: remember (κρατά την τιμή όταν η διεπαφή ανασυντίθεται) και mutableStateOf (λέει στο Compose «αυτή η τιμή άλλαξε, ξαναζωγράφισε»).

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hand-pointer mr-1"></i> Ο χρήστης πατάει</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> Η κατάσταση αλλάζει (count++)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> Το Compose αντιλαμβάνεται την αλλαγή</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> Αυτόματο ξαναζωγράφισμα οθόνης (recomposition)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Σχήμα 3: Η μονής κατεύθυνσης ροή δεδομένων «state → διεπαφή» του Compose
:::

#### 5. Θέμα και σκούρο θέμα: μία ρύθμιση, ισχύ παντού

Στο template project, το MyFirstAppTheme { ... } είναι το θέμα. Βασίζεται στις προδιαγραφές σχεδίασης Material 3 και σε βοηθά να διαχειρίζεσαι ενιαία χρώματα, γραμματοσειρές και σχήματα. Η υποστήριξη σκούρου θέματος θέλει τρία βήματα:

1. Ορίζεις στο θέμα δύο παλέτες χρωμάτων, ανοιχτή/σκούρα (το template έχει ήδη δημιουργήσει το ColorScheme)·
2. Όταν το σύστημα περνά σε σκούρο θέμα, το isSystemInDarkTheme() το κρίνει αυτόματα·
3. Χρησιμοποιείς τα χρώματα που προσφέρει το θέμα (π.χ. MaterialTheme.colorScheme.primary) αντί να γράφεις σταθερές τιμές χρωμάτων.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Συμβουλή: δυναμικά χρώματα του Material 3

{class="mt-1"}
Από το Android 12 και μετά, το «Material You» επιτρέπει στην εφαρμογή να αντλεί χρώματα από το wallpaper σου. Το Compose template το υποστηρίζει προεπιλεγμένα (dynamicColor). Η εφαρμογή σου θα «αλλάζει ρούχα» αυτόματα στο τηλέφωνο κάθε χρήστη — αυτή είναι η ρομαντική πλευρά του σύγχρονου Android.
:::

#### 6. Preview, animations και Live Edit: τα «superpowers» του Compose

Τρία «superpowers» του Compose στην εμπειρία ανάπτυξης — μόλις τα αποκτήσεις, δεν γυρνάς πίσω:

- @Preview: προσθέτεις την ένδειξη @Preview σε ένα Composable και το Android Studio αμέσως σχεδιάζει τη διεπαφή στα δεξιά — βλέπεις ό, τι γράφεις, χωρίς κάθε φορά να το εγκαθιστάς στο τηλέφωνο·
- Live Edit: το Android Studio του 2026 υποστηρίζει «hot update» ορισμένων αλλαγών στον emulator/πραγματική συσκευή· μικρές αλλαγές, όπως το χρώμα κειμένου, εμφανίζονται αμέσως στη συσκευή·
- Animations API: με λίγες γραμμές όπως animateFloatAsState, AnimatedVisibility, τα στοιχεία μεταβαίνουν ομαλά — η «αίσθηση premium» συχνά απλώς απέχει τόσο λίγες γραμμές.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Animation που μαθαίνεις σε 10 λεπτά</span><span class="dots">···</span>
:::

```
@Composable
fun AnimatedBox() {
    var big by remember { mutableStateOf(false) }
    // Όταν αλλάζει η τιμή, ομαλή μετάβαση στον στόχο
    val size by animateDpAsState(if (big) 120.dp else 60.dp)

    Box(Modifier
        .size(size)
        .background(MaterialTheme.colorScheme.primary)
        .clickable { big = !big }
    )
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Συμβουλή: πρώτα η λειτουργία, μετά τα animations

{class="mt-1"}
Συχνό λάθος των αρχάριων: «δεν έκανα ακόμα σωστά τη διεπαφή, αλλά αρχίζω να αγχώνομαι για animations». Πρώτα κάνε τη λειτουργία να τρέχει, και στο τέλος πρόσθεσε μαζί όλα τα animations — κι αυτό είναι η αρχή «πρώτα η απλότητα»: τα animations είναι το κεράκι στην τούρτα, η λειτουργία είναι το ψωμί της επιβίωσης.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Σειρά σου: φτιάξε ένα «κουμπί διάθεσης»

{class="mt-1"}
Άλλαξε το template project σε εναλλάκτη διάθεσης: ένα κουμπί που, σε κάθε πάτημα, κάνει κύκλο ανάμεσα σε 😀χαρά → 😢λύπη → 😡θυμός, με το κείμενο και το χρώμα φόντου να αλλάζουν μαζί. Υπόδειξη: χρησιμοποίησε when για να διαλέγεις κείμενο και χρώμα ανάλογα με το state. Όταν το τελειώσεις, στείλε το σε φίλους για πείραγμα και μάζεψε τα πρώτα «τι; εσύ φτιάχνεις εφαρμογές;».
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Σύνοψη κεφαλαίου

- Η ιδέα του Compose: διεπαφή = συναρτήσεις @Composable, ενθεμένες σαν τουβλάκια
- Τα τέσσερα βασικά components: Text / Button / TextField / Image
- Το τρίπτυχο των layouts: Column κάθετα, Row οριζόντια, Box στοιβαγμένα
- Modifier σε «αλυσίδα στυλ»: padding, fillMaxWidth, background, clickable — η σειρά έχει σημασία
- Η κατάσταση είναι η ψυχή: remember + mutableStateOf — αλλάζεις τα δεδομένα και η οθόνη ζωγραφίζει ξανά μόνη της
- Θέμα με Material 3 + δυναμικά χρώματα: ρύθμισε το σκοτεινό θέμα μία φορά και ισχύει παντού
:::
