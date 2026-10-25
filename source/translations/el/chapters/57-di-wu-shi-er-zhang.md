---
id: di-wu-shi-er-zhang
num: 52
part: an-zhuo-kai-fa-pian
nav: Κεφάλαιο 52: Τα τέσσερα βασικά στοιχεία και ο κύκλος ζωής του Activity
toc: default
kind: chapter
---

### Κεφάλαιο 52: Τα τέσσερα βασικά συστατικά και ο κύκλος ζωής του Activity

{class="chapter-intro mb-4"}
Αν το Compose είναι το «πρόσωπο» της εφαρμογής, αυτό το κεφάλαιο μιλάει για τον «σκελετό» της. Το Android έχει τέσσερα βασικά συστατικά και όλες οι εφαρμογές φτιάχνονται από αυτά· το σημαντικότερο από αυτά, το Activity, έχει έναν «χάρτη κύκλου ζωής» που κάθε προγραμματιστής Android πρέπει να έχει χαραγμένο στο μυαλό του. Μόλις τελειώσεις το κεφάλαιο, θα καταλαβαίνεις μυστηριώδη ερωτήματα τύπου «γιατί, μόλις πήγα στο παρασκήνιο και γύρισα, χάθηκε η κατάσταση της εφαρμογής μου».

#### 1. Τα τέσσερα συστατικά: οι «κολόνες και δοκοί» του Android

Το Android ορίζει επίσημα τέσσερα βασικά συστατικά, με το καθένα υπεύθυνο για ένα είδος δουλειάς:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Συστατικό</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Καθήκον</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Παρομοίωση</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Activity</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Μια ορατή διεπαφή (οθόνη)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Η βιτρίνα του μαγαζιού — ο χρήστης τη βλέπει και αλληλεπιδρά</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Service</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ο «αόρατος» που δουλεύει στο παρασκήνιο</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ο αποθηκάριος — παίζει μουσική, κατεβάζει αρχεία, χωρίς διεπαφή</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">BroadcastReceiver</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Λαμβάνει μεταδόσεις (broadcast) του συστήματος</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Το γραφείο κοινοποιήσεων — το «μεγάφωνο» για το «τελείωσε η μπαταρία», «κόπηκε το δίκτυο»</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ContentProvider</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Μοιράζεται δεδομένα ανάμεσα σε εφαρμογές</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ο δημόσιος φάκελος αρχείων — π.χ. μοιράζεται τις επαφές σε άλλες εφαρμογές</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Τα τέσσερα συστατικά του Android με μια ματιά

Στο στάδιο του αρχάριου θα περνάς το 95% του χρόνου σου με το Activity· το Service και το BroadcastReceiver θα τα χρειαστείς για αναπαραγωγή μουσικής και ειδοποιήσεις push· το ContentProvider χρησιμοποιείται πιο σπάνια (το σύστημα έχει ήδη «πακετάρει» τα συνηθισμένα δεδομένα). Και πρόσεξε: και τα τέσσερα συστατικά πρέπει να δηλωθούν στο AndroidManifest.xml — χωρίς δήλωση, το σύστημα δεν τα βρίσκει.

#### 2. Ο κύκλος ζωής του Activity: ο πρώτος «χάρτης θησαυρού» του προγραμματισμού Android

Μια εφαρμογή στο κινητό μπορεί να διακοπεί ανά πάσα στιγμή: έρχεται τηλεφώνημα, ο χρήστης πάει να απαντήσει στο WeChat, το σύστημα δεν έχει μνήμη και τη «σκοτώνει»… Η ζωή ενός Activity είναι ένα ατελείωτο ταξίδι σε κύκλους πάνω σε αυτόν τον χάρτη:

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onCreate (γέννηση: αρχικοποίηση)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onStart (ορατό)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onResume (σε πρώτο πλάνο, ενεργό)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center">onPause (μερικώς καλυμμένο)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center">onStop (αόρατο εντελώς)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center">onDestroy (καταστροφή)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center">🔁 onRestart / onStart / onResume: επιστροφή σε πρώτο πλάνο από τον ίδιο δρόμο</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Εικόνα 4: Κύκλος ζωής του Activity (προς τα εμπρός: η πάνω σειρά «γέννηση» → η κάτω σειρά «αποχώρηση»· στην επιστροφή, ο ίδιος δρόμος ανάποδα)
:::

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Callback</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Πότε ενεργοποιείται</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Τυπική χρήση</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onCreate</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Όταν δημιουργείται το Activity (μία φορά)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Φόρτωση διεπαφής, αρχικοποίηση δεδομένων</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onStart</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Η διεπαφή γίνεται ορατή</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ξεκινάς κάποια ελαφριά λογική</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onResume</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Παίρνει εστία και γίνεται αλληλεπιδραστικό</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ξεκινάς κινήσεις (animations), συνεχίζεις αναπαραγωγή</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onPause</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Όταν καλύπτεται μερικώς / τη στιγμή της μετάβασης</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Παύεις κινήσεις, σώζεις πρόχειρο</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onStop</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Γίνεται εντελώς αόρατο</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Απελευθερώνεις βαριούς πόρους, σταματάς λήψεις</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onDestroy</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Πριν την καταστροφή</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ο τελικός καθαρισμός</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Οι τυπικές χρήσεις των έξι callbacks του κύκλου ζωής

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Προσοχή στην παγίδα: η περιστροφή της οθόνης «σκοτώνει» το Activity

{class="mt-1"}
Η πιο κλασική παγίδα του αρχάριου: η εφαρμογή γυρίζει την οθόνη και τα κείμενα στα πεδία εισαγωγής εξαφανίζονται. Αιτία: με την περιστροφή της οθόνης, από προεπιλογή το Activity καταστρέφεται και ξαναδημιουργείται (περνά μια φορά από onDestroy → onCreate). Λύση: αποθήκευσε την κατάσταση με rememberSaveable (ο αντικαταστάτης του remember στο Compose) — ξαναφέρνει αυτόματα τις τιμές μετά την αναδημιουργία. Θα το χρειάζεσαι ξανά και ξανά στα κεφάλαια 6 και 7.
:::

#### 3. Intent: το «εισιτήριο» για μετακινήσεις μέσα κι έξω από την εφαρμογή

Το Intent («πρόθεση») είναι το «εισιτήριο» επικοινωνίας ανάμεσα στα συστατικά. Θέλεις να πηδήξεις από μια οθόνη σε άλλη, να ανοίξεις τον browser ή να ξεκινήσεις την κάμερα; Πρέπει να «αγοράσεις εισιτήριο και να ανέβεις στο τρένο»:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Μετάβαση με Intent</span><span class="dots">···</span>
:::

```
// Τρόπος 1: ρητό Intent—ορίζεις καθαρά τη σελίδα προορισμού
val intent = Intent(this, DetailActivity::class.java)
intent.putExtra("name", "Γιώργος ") // Σαν "αποσκευή" πάνω στο όχημα (δεδομένα)
startActivity(intent)

// Τρόπος 2: σιωητό Intent—λες μόνο τι θες, το σύστημα βρίσκει ποιος θα το κάνει
val web = Intent(Intent.ACTION_VIEW, Uri.parse("https://developer.android.com"))
startActivity(web) // Το σύστημα θα ανοίξει browser/ή θα σε αφήσει να επιλέξεις
```
:::

Κάθε τρόπος έχει τη χρήση του: ο ρητός (explicit) για μεταβάσεις ανάμεσα στις οθόνες της δικής σου εφαρμογής· ο σιωπηρός (implicit) για να καλείς δυνατότητες του συστήματος ή άλλων εφαρμογών (άνοιγμα ιστοσελίδας, τηλεφώνημα, κοινοποίηση). Σε έργα Compose, μέσα σε ένα Composable παίρνεις το Context με το LocalContext.current και μπορείς να καλέσεις το startActivity.

#### 4. Πολλαπλές οθόνες και πλοήγηση

Οι πραγματικές εφαρμογές έχουν πολλές οθόνες. Η επίσημη προτεινόμενη λύση του Compose είναι το Navigation Compose (βιβλιοθήκη androidx.navigation):

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Σκελετός Navigation Compose</span><span class="dots">···</span>
:::

```
val navController = rememberNavController()

NavHost(navController, startDestination = "home") {
    composable("home") { HomeScreen(navController) }
    composable("detail/{name}") { entry ->
        val name = entry.arguments?.getString("name")
        DetailScreen(name ?: "Άγνωστο")
    }
}

// Πλοήγηση μέσα στη σελίδα:
navController.navigate("detail/Γιώργος")     // με παράμετρο
navController.popBackStack()              // πίσω στην προηγούμενη
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Συμβουλή: τι κάνεις όταν πολλαπλασιάζονται οι οθόνες;

{class="mt-1"}
Όταν το έργο μεγαλώσει, γράψε όλες τις διαδρομές των οθονών συγκεντρωμένες σε ένα αρχείο (π.χ. AppNavGraph.kt) για ενιαία διαχείριση — μην αφήνεις τη λογική «πού πάω τώρα» σκορπισμένη στις οθόνες. Είναι το πρώτο βήμα από το «τρέχει» στο «συντηρήσιμο».
:::

#### 5. Παρεμπιπτόντως: τι είναι το Fragment (και γιατί δεν το διδάσκει αυτό το βιβλίο)

Ψάχνοντας σε παλιούς οδηγούς θα πέσεις σίγουρα πάνω στο Fragment — είναι ένα «επαναχρησιμοποιήσιμο τμήμα διεπαφής» μέσα σε ένα Activity και πρωταγωνιστούσε στην παλιά αρχιτεκτονική πολλών οθονών. Στην εποχή του Compose, όμως, οι οθόνες φτιάχνονται απλώς με συναρτήσεις Composable + δρομολόγηση Navigation, και η ίδια η επίσημη τεκμηρίωση έχει μειώσει τον ρόλο του Fragment. Γι’ αυτό το βιβλίο δεν το βάζει στο βασικό δρόμο.

Η συμβουλή μου: σε νέο έργο μην χρησιμοποιείς Fragment με τη θέλησή σου· αλλά όταν διαβάζεις παλιό κώδικα ή σου κάνουν την ερώτηση σε συνέντευξη, αρκεί να ξέρεις ότι είναι «ένα τμήμα διεπαφής ενσωματωμένο σε ένα Activity». Στους πόρους εκμάθησης προτίμα πάντα ό, τι είναι από το 2023 και μετά — το «αλμανάκ» της τεχνολογίας Android ανανεώνεται πιο γρήγορα απ’ όσο φαντάζεσαι.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Πρακτική άσκηση: δώσε στον μετρητή «μνήμη»

{class="mt-1"}
Τροποποίησε τον μετρητή του κεφαλαίου 51: ① αντικατάστησε το remember με rememberSaveable και γύρισε την οθόνη για να επιβεβαιώσεις ότι ο αριθμός μένει· ② πρόσθεσε ένα κουμπί «Σχετικά» που με το Navigation πηγαίνει σε δεύτερη οθόνη και δείχνει τον αριθμό έκδοσης· ③ τύπωσε logs (Log.d) στα onCreate/onPause των δύο οθονών και παρακολούθησε στο Logcat τη σειρά κλήσεων του κύκλου ζωής. Αφού κάνεις αυτά τα τρία βήματα, ο κύκλος ζωής δεν θα είναι πια θεωρία.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Σύνοψη κεφαλαίου

- Τα τέσσερα συστατικά: Activity (βιτρίνα), Service (παρασκήνιο), BroadcastReceiver (μεγάφωνο), ContentProvider (φάκελος αρχείων)
- Τα έξι callbacks του κύκλου ζωής: onCreate → onStart → onResume → onPause → onStop → onDestroy
- Η περιστροφή της οθόνης καταστρέφει και ξαναφτιάχνει το Activity: κράτα την κατάσταση με rememberSaveable
- Το Intent είναι το «εισιτήριο»: ρητό για τις δικές σου οθόνες, σιωπηρό για δυνατότητες του συστήματος
- Πολλές οθόνες με Navigation Compose: NavHost + δρομολόγηση με composable
:::
