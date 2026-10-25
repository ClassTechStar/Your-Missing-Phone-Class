---
id: di-wu-shi-liu-zhang
num: 56
part: an-zhuo-kai-fa-pian
nav: Κεφάλαιο 56: Φινίρισμα και δημοσίευση — ανέβασε την εφαρμογή στο Google Play
toc: default
kind: chapter
---

### Κεφάλαιο 56: Γυάλισμα και δημοσίευση — δοκιμές, αποσφαλμάτωση και ανάρτηση στο Google Play

{class="chapter-intro mb-4"}
Έφτιαξες την εφαρμογή — και μετά; Αυτό το κεφάλαιο απαντά σε τρία θέματα του δρόμου από το «τρέχει» στο «παραδίδεται»: πώς αποσφαλματώνεις αποτελεσματικά για να βρίσκεις bugs, πώς γράφεις δοκιμές για να μην ξαναγυρίζουν τα λάθη, και πώς στέλνεις την εφαρμογή στο Google Play για να την κατεβάζει όλος ο κόσμος. Η ανάρτηση δεν είναι μόνο τελετουργία — είναι το ορόσημο που μετατρέπει ένα έργο σε προϊόν.

#### 1. Τα τρία όπλα της αποσφαλμάτωσης: Logcat, breakpoints, επιθεωρητής UI

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Εργαλείο</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Σε τι χρησιμεύει</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Πώς το χρησιμοποιείς</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Logcat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Βλέπεις τα logs του συστήματος ή τα δικά σου</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Στον κώδικα Log.d("TAG","τιμή=$x"), και στο πάνελ ψάχνεις το TAG για φίλτρο</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Αποσφαλμάτωση με breakpoints</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Σταματάς το πρόγραμμα σε μια γραμμή και βλέπεις τις τιμές μεταβλητών</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Κλίκ δίπλα στον αριθμό γραμμής βγάζει κόκκινη κουκκίδα, τρέχεις σε Debug mode και πας βήμα-βήμα</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Layout Inspector</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Βλέπεις τη δομή της διεπαφής όσο τρέχει</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Μενού Tools → Layout Inspector, βλέπεις το δέντρο στοιχείων σε πραγματικό χρόνο</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Τα τρία όπλα της αποσφαλμάτωσης

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Συμβουλή: πώς διαβάζεις ένα σφάλμα;

{class="mt-1"}
Μετά από κατάρρευση, στο Logcat θα δεις κόκκινη στοίβα (Stacktrace): ψάξε από κάτω προς τα πάνω την πρώτη γραμμή που αρχίζει από το δικό σου package (π.χ. com.example.yourapp) — αυτή είναι συνήθως ο «τόπος του εγκλήματος». Δες πρώτα τον «τύπο της Exception» (null pointer; μετατροπή τύπου;), μετά το «at ... Το Αρχείο Σου: γραμμή». Με αυτό το κόλπο λύνεις το 80% των καταρρεύσεων.
:::

#### 2. Δοκιμές: ασφάλιση του κώδικα

Οι χειρωνακτικές δοκιμές δεν είναι αξιόπιστες — άλλαξες μια λειτουργία και μια άλλη χάλασε στα κρυφά. Οι δοκιμές είναι «αντίδοτο για τις μεταμέλειες» και «αλεξίσφαιρο γιλέκο». Οι δοκιμές στο Android χωρίζονται σε τρία επίπεδα· ως αρχάριος, κατάκτησε πρώτα το πρώτο:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Επίπεδο</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Τι δοκιμάζει</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Πού μπαίνει</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ταχύτητα</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Μοναδιαίες δοκιμές (unit tests)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Καθαρή λογική (υπολογισμοί, επικύρωση)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">app/src/test/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Δευτερόλεπτα</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Δοκιμές οργάνων (instrumented tests)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Συμπεριφορά διεπαφής σε πραγματική συσκευή</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">app/src/androidTest/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Λεπτά</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Χειρωνακτικές δοκιμές</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Αίσθηση και εμπειρία πραγματικού ανθρώπου</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">——</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Πάντα απαραίτητες</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Τα τρία επίπεδα δοκιμών

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Παράδειγμα unit test</span><span class="dots">···</span>
:::

```
// Διαχωρίζουμε τη λογική "μετατροπή κειμένου ποσού σε αριθμό" σε καθαρή συνάρτηση
fun parseAmount(input: String): Double? {
    val v = input.trim().toDoubleOrNull()
    return if (v != null && v > 0) v else null
}

// Τεστάρισμα (JUnit4)
@Test
fun emptyInputReturnsNull() {
    assertEquals(null, parseAmount(""))
}
@Test
fun negativeReturnsNull() {
    assertEquals(null, parseAmount("-5"))
}
@Test
fun normalValueParses() {
    assertEquals(12.5, parseAmount("12.5"))
}
```
:::

Η επικύρωση ποσών και οι στατιστικοί υπολογισμοί στο βιβλίο εξόδων πρέπει να έχουν πάνω τους unit tests. Εκτέλεση δοκιμών: δεξί κλικ στον κατάλογο test → Run. Αν όλα βγουν πράσινα, άλλαζε κώδικα με σιγουριά.

#### 3. Υπογραφή και πακετάρισμα: να «σφραγίσεις» την εφαρμογή

Το Android απαιτεί όλα τα πακέτα εγκατάστασης να είναι υπογεγραμμένα — σαν στρογγυλή σφραγίδα που πιστοποιεί «αυτό το πακέτο το βγάλω εγώ και δεν έχει παραποιηθεί». Στην αποσφαλμάτωση το Android Studio χρησιμοποιεί αυτόματα υπογραφή debug· για δημοσίευση θέλεις τη δική σου υπογραφή release. Η διαδικασία:

1. Μενού Build → Generate Signed Bundle / APK·
2. Δημιουργία αρχείου keystore (θησαυροφυλάκιο κλειδιών) — ορίζεις κωδικό και τον φυλάς με προσοχή·
3. Επιλέγεις release + μορφή AAB και η δόμηση ολοκληρώνεται.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Προσοχή στην παγίδα: keystore χαμένο = εφαρμογή χαμένη

{class="mt-1"}
Μετά την ανάρτηση, κάθε ενημέρωση της εφαρμογής πρέπει να γίνεται με την ίδια υπογραφή, αλλιώς το κατάστημα απορρίπτει την ενημέρωση. Αν χαθεί το αρχείο keystore και ο κωδικός, μπορείς μόνο να ξαναδημοσιεύσεις ως νέα εφαρμογή — οι παλιοί χρήστες χάνονται όλοι. Φρόντισε να κρατάς backup του keystore και του κωδικού σε ασφαλές μέρος (κρυπτογραφημένο cloud + σημειωματάριο) — ένα από τα πιο ακριβά μαθήματα των προγραμματιστών Android.
:::

#### 4. Η πλήρης διαδικασία ανάρτησης στο Google Play

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> Εγγραφή λογαριασμού developer</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-invoice mr-1"></i> Προετοιμασία υλικών για το κατάστημα</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-box mr-1"></i> Ανέβασμα AAB</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-clipboard-list mr-1"></i> Συμπλήρωσε τον πίνακα ασφάλειας δεδομένων</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> Έλεγχος (ώρες~μέρες)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-party-horn mr-1"></i> Κυκλοφορία</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Εικόνα 6: Έξι βήματα για την ανάρτηση στο Google Play
:::

- Εγγραφή: εφάπαξ τέλος 25 δολαρίων, με λειτουργικό λογαριασμό Google·
- Υλικό: εικονίδιο εφαρμογής (512×512), screenshots (τουλάχιστον 2), περιγραφή λειτουργιών, σύνδεσμος πολιτικής απορρήτου (υποχρεωτικό αν συλλέγονται δεδομένα)·
- Φόρμα ασφάλειας δεδομένων: δηλώνεις ειλικρινά ποια δεδομένα συλλέγεις — ένα βιβλίο εξόδων χωρίς internet μπορεί να δηλώσει «μηδενική συλλογή»·
- Έλεγχος: οι νέοι λογαριασμοί στην πρώτη ανάρτηση περνούν συχνά από ανθρώπινο έλεγχο, από μερικές ώρες έως μέρες· αν απορριφθείς, διορθώνεις βάσει των σχολίων.

Σημείωση για χρήστες στην Κίνα: το Google Play απαιτεί ειδικές συνθήκες δικτύου, και στην ηπειρωτική Κίνα η διανομή γίνεται συνήθως μέσω εγχώριων καταστημάτων (Huawei, Xiaomi, YingYongBao κ.ά.). Η διαδικασία ανάρτησης εκεί μοιάζει, αλλά κάθε κατάστημα έχει τις δικές του γεύσεις στον έλεγχο — το ίδιο AAB/APK μπορεί να διανεμηθεί σε πολλά καταστήματα. Για εξάσκηση, αρκεί να πετύχεις πρώτα σε ένα — αυτό είναι νίκη.

#### 5. Πώς φτιάχνεις το υλικό καταστήματος: η πρώτη εντύπωση είναι οι λήψεις

Η σελίδα στο κατάστημα είναι η βιτρίνα που βλέπει ο χρήστης «όταν περιφέρεται». Τρία στοιχεία καθορίζουν την πρώτη εντύπωση:

- Εικονίδιο: 512×512, όχι κάποιο screenshot της τελευταίας στιγμής. Αν δεν έχεις σχεδιαστικές ικανότητες, φτιάξε με εργαλείο AI ένα απλό γεωμετρικό σχήμα — μόνο αν αναγνωρίζεται με μια ματιά ακόμα και συρρικνωμένο στην αρχική οθόνη του κινητού είναι αποδεκτό·
- Screenshots: τουλάχιστον 2, καλύτερα 4-6, που δείχνουν τα πιο βασικά σενάρια χρήσης· κάθε ένα με μια απλή, ανθρώπινη φράση («Καταγραφή σε ένα δευτερόλεπτο» είναι δέκα φορές καλύτερο από «Αποδοτική λύση λογιστικής»)·
- Περιγραφή: η πρώτη πρόταση να λέει καθαρά «τι είναι + για ποιον», χωρίς σωρούς από «το πιο επαγγελματικό, το πιο δυνατό» — η κατάταξη στην αναζήτηση του καταστήματος κοιτάζει κυρίως λέξεις-κλειδιά και μετατροπή σε λήψεις· η ειλικρίνεια αποδίδει περισσότερο από την υπερβολή.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Συμβουλή: κάνε σύγκριση με τους συναγωνιστές

{class="mt-1"}
Πριν την ανάρτηση, κύκλωσε τις πρώτες δέκα παρόμοιες εφαρμογές στο κατάστημα και τράβα screenshots για σύγκριση: τι στυλ έχουν τα εικονίδια τους; τι πλεονεκτήματα προβάλουν στα screenshots; πώς γράφουν τους τίτλους; Η μίμηση δεν είναι λογοκλοπή — μαθαίνεις το σχήμα και βάζεις δικό σου περιεχόμενο· αυτό είναι το γρηγορότερο μάθημα ψυχρής εκκίνησης για κάθε προϊόν.
:::

#### 6. Μικρή λίστα: βελτιστοποίηση απόδοσης και αναφορά καταρρεύσεων

Πριν από την ανάρτηση, αξίζουν μισή ώρα η καθεμιά από αυτές τις δύο υποθέσεις:

##### 1. Τέσσερα σημεία αυτοελέγχου απόδοσης

1. Λίστες με LazyColumn: τις μακριές λίστες μην τις τοποθετείς ποτέ σκληρά σε Column — η lazy φόρτωση είναι το πρώτο μάθημα απόδοσης στο Android·
2. Μην ρίχνεις κατευθείαν τις αρχικές εικόνες: με τη βιβλιοθήκη Coil γίνεται αυτόματη κλιμάκωση και caching — μια αρχική εικόνα 5MB αρκεί να «στραγγάλει» ένα φτηνό κινητό·
3. Απόφυγε τις βαριές δουλειές στο κύριο νήμα: βάσεις δεδομένων, δίκτυο, μεγάλα αρχεία — όλα μέσα σε coroutines·
4. Μέτρησε με τον Profiler: ο αναλυτής απόδοσης του Android Studio δείχνει μνήμη, CPU και κατανάλωση — πρώτα μέτρηση, μετά βελτιστοποίηση, όχι με την αίσθηση.

##### 2. Αναφορά καταρρεύσεων

Το ότι δεν κατέρρευσε στις δικές σου δοκιμές δεν σημαίνει ότι δεν θα καταρρεύσει στο κινητό κάποιου χρήστη. Πριν την ανάρτηση, ενσωμάτωσε το Firebase Crashlytics (επίσημο της Google, δωρεάν): με λίγες γραμμές ρύθμισης, όταν η εφαρμογή καταρρεύσει, η στοίβα αναφέρεται αυτόματα και στο backend βλέπεις «ποιο μοντέλο, ποια έκδοση, σε ποια γραμμή». Ανάρτηση χωρίς παρακολούθηση καταρρεύσεων είναι σαν οδήγηση με κλειστά μάτια.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Πρακτική άσκηση: «παράδοσε» το βιβλίο εξόδων μία φορά

{class="mt-1"}
① Πρόσθεσε 3 unit tests στη λογική του parseAmount κ.λπ.· ② με το Logcat, πίασε με τα χέρια σου μια κατάρρευση που δημιούργησες μόνος σου και δώσε της λύση· ③ παράγαγε ένα APK με υπογραφή release και στείλ’ το σε φίλο να το εγκαταστήσει (αυτό είναι η «τελετουργία» του έργου)· ④ αν έχεις περιθώριο, κάνε εγγραφή στον λογαριασμό προγραμματιστών και υποβάλλε πραγματικά το βιβλίο εξόδων για ανάρτηση. Τα τρία πρώτα μπορείς να τα τελειώσεις απόψε.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Σύνοψη κεφαλαίου

- Τα τρία όπλα αποσφαλμάτωσης: Logcat για logs, breakpoints για μεταβλητές, Layout Inspector για τη διεπαφή
- Διάβασε μια κατάρρευση: από κάτω προς τα πάνω στην στοίβα, βρες την πρώτη γραμμή με το δικό σου package
- Τρία επίπεδα δοκιμών: μοναδιαίες (δευτερόλεπτα — μάθε πρώτα αυτές) / instrumented / χειρωνακτικές
- Η δημοσίευση θέλει υπογραφή: κράτα backup keystore και κωδικού — αν χαθούν, η εφαρμογή «αλλάζει πρόσωπο»
- Έξι βήματα ανάρτησης: εγγραφή → υλικό → ανέβασμα AAB → φόρμα ασφάλειας δεδομένων → έλεγχος → δημοσίευση
:::
