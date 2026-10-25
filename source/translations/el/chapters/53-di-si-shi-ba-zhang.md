---
id: di-si-shi-ba-zhang
num: 48
part: an-zhuo-kai-fa-pian
nav: Κεφάλαιο 48: Γνώρισε το Android — από το λειτουργικό σύστημα στο οικοσύστημα ανάπτυξης
toc: default
kind: chapter
---

### Κεφάλαιο 48: Γνωριμία με το Android — από το λειτουργικό σύστημα στο οικοσύστημα ανάπτυξης

{class="chapter-intro mb-4"}
Συγχαρητήρια για την απόφαση — από «κάποιος που παίζει με το τηλέφωνο» σε «κάποιος που φτιάχνει εφαρμογές τηλεφώνου». Πριν πιάσουμε δουλειά, ας απλώσουμε τον χάρτη: από πού προήλθε το Android; Γιατί οι developers σε όλο τον κόσμο γράφουν εφαρμογές για αυτό; Τι συμβαίνει από τη στιγμή που χτυπάς τα πλήκτρα μέχρι η εφαρμογή να φτάσει στο τηλέφωνο του χρήστη;

#### 1. Οι ρίζες του Android: από το «μικρό ρομποτάκι» στο «μεγαλύτερο σύστημα του κόσμου»

Η ιστορία του Android αρχίζει το 2003 — ο μηχανικός Andy Rubin ίδρυσε την εταιρεία Android με έναν ταπεινό στόχο: ένα έξυπνο λειτουργικό σύστημα που να «καταλαβαίνει την κάμερα» καλύτερα. Το 2005 η Google το αγόρασε, το 2007 μαζί με δεκάδες κατασκευαστές σχημάτισαν την Open Handset Alliance (OHA), και τον Σεπτέμβριο 2008 κυκλοφόρησε επίσημα το πρώτο τηλέφωνο Android, το HTC Dream (G1).

Την υπόλοιπη ιστορία τη ξέρουμε όλοι: μέχρι το 2026 το Android είναι το λειτουργικό σύστημα κινητών με τη μεγαλύτερη μερίδα αγοράς παγκοσμίως, με δισεκατομμύρια ενεργές συσκευές. Το τηλέφωνό σου, το TV box σου, η μεγάλη οθόνη του αυτοκινήτου, το έξυπνο ρολόι σου — πολύ πιθανόν όλα τρέχουν Android. Τι σημαίνει αυτό; Ότι κάθε γραμμή κώδικα που γράφεις έχει την ευ και ρία να τη χρησιμοποιήσουν οι περισσότεροι άνθρωποι του πλανήτη.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Συμβουλή: το DNA ανοιχτού κώδικα του Android

{class="mt-1"}
Ο πυρήνας του Android (AOSP, Android Open Source Project) είναι ανοιχτού κώδικα — κάθε κατασκευαστής μπορεί να τον πάρει, να τον τροποποιήσει και να τον προσαρμόσει. Γι' αυτό η Xiaomi έχει το MIUI (τώρα HyperOS), η Huawei το συμβατό στρώμα HarmonyOS, η Samsung το One UI. Για τον developer αυτό είναι καλό: μαθαίνεις «ανάπτυξη Android», όχι «ανάπτυξη για ένα brand» — μια δουλειά που δουλεύει παντού.
:::

Και η εξέλιξη των εκδόσεων έχει ενδιαφέρον: από το 1.5 με το Cupcake, κάθε μεγάλη έκδοση έπαιρνε όνομα γλυκού — Donut, Eclair, Frozen Yogurt, Gingerbread… και μόνο με το Android 10, το 2019, πέρασε σε σκέτα νούμερα. Μέχρι τον Αύγουστο 2026, η νεότερη επίσημη έκδοση είναι το Android 17· σε επίπεδο ανάπτυξης, το «ελάχιστο υποστηριζόμενο» που πραγματικά σε αφορά, στις mainstream εφαρμογές ορίζεται συνήθως ανάμεσα στο Android 8 (API 26) και στο Android 10 (API 29) — όσο υποστηρίζεις συσκευές λίγων ετών, τόσο μεγαλύτερο είναι το κοινό σου.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Έκδοση</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Κωδικό όνομα / Έτος</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Τα σημαντικά για τον developer</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 8 (API 26)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Oreo · 2017</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Κανάλια ειδοποιήσεων, περιορισμοί στο background — το ελάχιστο όριο για πολλές παλιές συσκευές</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 10 (API 29)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2019</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Έρχεται το scoped storage· οι κανόνες πρόσβασης σε αρχεία αλλάζουν ριζικά</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 12 (API 31)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2021</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Material You με δυναμικά χρώματα· μεγάλη αναβάθμιση στην όψη του UI</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 13 (API 33)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2022</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Άδεια ειδοποιήσεων κατά την εκτέλεση· παράθυρο που ρωτά «επιτρέπεις τις ειδοποιήσεις;»</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 14-15 (API 34-35)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2023-2024</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Προβλεπτικό back, σελίδες 16KB, περαιτέρω σύσφιξη ιδιωτικότητας</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 16-17 (API 36-37)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2025-2026</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Πιο γρήγορος ρυθμός μικρών εκδόσεων, ενσωμάτωση AI (π.χ. επεκτάσεις Gemini)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Σύντομη ιστορία εκδόσεων του Android (κατά τον Αύγουστο 2026, τα σημεία-κλειδιά για ανάπτυξη)

#### 2. Σε ποια γλώσσα γράφεις: Java ή Kotlin;

Στην ιστορία του Android εμφανίστηκαν δύο κύριες γλώσσες. Η Java είναι ο «παλιός στρατιώτης της πρώτης ώρας» — την είχε το Android από τη γέννησή του· το Kotlin ανακηρύχθηκε το 2017 από τη Google «γλώσσα πρώτης κατηγορίας» και από το 2019 η επίσημη γραμμή είναι σαφές «Kotlin-first». Το 2026, σχεδόν όλα τα νέα projects είναι σε Kotlin και τα παλιά projects μεταφέρονται σταδιακά.

Πάμε στα ίσια: αν είσαι εντελώς αρχάριος, μάθε ευθεία Kotlin και μη γυρίζεις πίσω στη Java. Τρεις λόγοι: πρώτον, ο κώδικας Kotlin είναι 30%-40% μικρότερος από τη Java (ίδια λειτουργία, πιο σύντομος και καθαρός)· δεύτερον, προστατεύει εκ φύσεως από το «null pointer», τον εφιάλτη των αρχάριων· τρίτον, όλα τα σύγχρονα μαθήματα, τα επίσημα έγγραφα και τα εργαλεία προγραμματισμού με AI (θυμάσαι το βιβλίο μας για τον προγραμματισμό με AI;) βασίζονται στο Kotlin. Java θα συναντήσεις μόνο όταν συντηρείς παλιά projects ή διαβάζεις παλιό κώδικα.

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
Στυλ Java (μακροσκελές)

{class="font-mono text-xs leading-relaxed"}
public class MainActivity extends Activity {<br>&nbsp;&nbsp;@Override<br>&nbsp;&nbsp;protected void onCreate(Bundle b) {<br>&nbsp;&nbsp;&nbsp;&nbsp; super.onCreate(b);<br>&nbsp;&nbsp;&nbsp;&nbsp; setContentView(R.layout.activity);<br>&nbsp;&nbsp;}<br>}
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
Στυλ Kotlin (καθαρό)

{class="font-mono text-xs leading-relaxed"}
class MainActivity : ComponentActivity() {<br>&nbsp;&nbsp;override fun onCreate(b: Bundle?) {<br>&nbsp;&nbsp;&nbsp;&nbsp; super.onCreate(b)<br>&nbsp;&nbsp;&nbsp;&nbsp;setContent { App() }<br>&nbsp;&nbsp;}<br>}
:::
:::

Για το ίδιο πράγμα, το Kotlin γλιτώνει σωρό άγκιστρα και boilerplate. Στο κεφάλαιο 50 θα το μάθουμε σωστά· για την ώρα κράτα ένα: η «κοινή γλώσσα» της ανάπτυξης Android λέγεται Kotlin.

#### 3. Πώς γεννιέται μια εφαρμογή;

Πολλοί νομίζουν ότι «η ανάπτυξη εφαρμογής» σημαίνει ότι ανοίγεις τον υπολογιστή και γράφεις αδιάκοπα κώδικα. Στην πραγματικότητα, από την ιδέα μέχρι το τηλέφωνο του χρήστη, μια εφαρμογή περνά περίπου από αυτή τη γραμμή παραγωγής:

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-lightbulb mr-1"></i> Ιδέα</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center">📐 Σχεδίαση (οθόνη+λειτουργίες)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-keyboard mr-1"></i> Γράφει κώδικα</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hammer mr-1"></i> Μεταγλώττιση και πακετάρισμα (APK/AAB)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> Τεστ (emulator+πραγματική συσκευή)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-rocket mr-1"></i> Δημοσίευση (κατάστημα/πακέτο εγκατάστασης)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Σχήμα 1: Ολόκληρη η ροή μιας Android εφαρμογής, από την ιδέα μέχρι το κατάστημα
:::

Στη ροή υπάρχουν δύο έννοιες που πρέπει να γνωρίζεις από τώρα:

- APK: η μορφή του πακέτου εγκατάστασης Android εφαρμογών (.apk)· με διπλό κλικ εγκαθίσταται στο τηλέφωνο, όπως το .exe στα Windows. Για τις προσωπικές σου δοκιμές και για να το μοιράζεσαι σε φίλους για πείραγμα, αυτό χρησιμοποιείς.
- AAB: Android App Bundle (.aab), η «προηγμένη μορφή πακεταρίσματος» που απαιτείται για το Google Play. Το κατάστημα το «κόβει» δυναμικά ανάλογα με το μοντέλο του τηλεφώνου του χρήστη, ώστε το πακέτο που κατεβαίνει να είναι μικρότερο. Μόνος σου δεν το εγκαθιστάς — πηγαίνει μόνο στο κατάστημα.

Ακόμα ένας όρος που θα ακούς συνέχεια: SDK (Software Development Kit, κιτ ανάπτυξης λογισμικού). Είναι ολόκληρος ο «εξοπλισμός» που προσφέρει επίσημα το Android — τις βιβλιοθήκες API κάθε έκδοσης, τα εργαλεία debugging, τις εικόνες του emulator κ.ά. Κλάσεις όπως το Activity και το Button που καλείς στον κώδικα προέρχονται από το SDK.

#### 4. Το τεχνολογικό τοπίο του Android σε μια ματιά: η «λίστα οπλισμού» σου

Πριν ξεκινήσεις σοβαρά, γνώρισε την τυπική διαμόρφωση των mainstream Android projects του 2026 — αν δεν την καταλαβαίνεις τώρα, δεν πειράζει· στο τέλος του βιβλίου θα τη ξαναδείς και όλα θα σου φαίνονται καθαρά:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Επίπεδο</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Σύγχρονη επιλογή (2026)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Σε τι χρησιμεύει</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Γλώσσα</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin 2.x</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Η γλώσσα για τη λογική</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Διεπαφή</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Jetpack Compose + Material 3</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Σχεδιάζεις τη διεπαφή με κώδικα (η κύρια γραμμή του βιβλίου)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Αρχιτεκτονική</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MVVM + ViewModel</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ξεχωρίζεις διεπαφή και λογική, ώστε ο κώδικας να μην μπερδεύεται</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Αποθήκευση δεδομένων</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room (βάση δεδομένων) + DataStore (ρυθμίσεις)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Αποθηκεύεις δεδομένα στο τηλέφωνο</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Δίκτυο</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit + OkHttp + Kotlin Coroutines</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Μιλάς με τον server</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Εργαλείο build</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gradle + Kotlin DSL</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Μετατρέπεις τον κώδικα σε πακέτο εγκατάστασης</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Περιβάλλον ανάπτυξης</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android Studio</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Το «όλα-σε-ένα» IDE της Google</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Ο mainstream tech stack του Android το 2026, σε μια ματιά

Μη τρομάζεις με τον σωρό των αγγλικών όρων. Είναι όπως τα σκεύη της κουζίνας — για την ώρα αρκεί να ξέρεις ότι «για να μαγειρέψεις, μπαίνεις στην κουζίνα»· πώς χρησιμοποιείται το κάθε εργαλείο, θα σου το ξετυλίγουμε ένα-ένα στα επόμενα κεφάλαια. Και το καλό νέο: όταν το Android Studio δημιουργεί νέο project, σετάρει όλο αυτό το σετ αυτόματα — εσύ απλώς μαγειρεύεις.

#### 5. Android vs iOS: το πρώτο μάθημα «επιλογής πλευράς» για τον developer

Ίσως να έχεις στα χέρια σου ταυτόχρονα συσκευή Android και συσκευή Apple. Ως developer, αξίζει να γνωρίζεις από τώρα τις διαφορές των δύο πλευρών — δεν πρόκειται για το «ποιο είναι καλύτερο», αλλά για τον ρεαλιστικό υπολογισμό «από ποια πλευρά σου αξίζει να ξεκινήσεις»:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Κριτήριο</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ανάπτυξη Android</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ανάπτυξη iOS</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Υπολογιστής ανάπτυξης</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Windows / Mac / Linux — όλα ισχύουν</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Μόνο Mac (αποκλειστικό Xcode)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Εργαλεία ανάπτυξης</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android Studio (δωρεάν)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode (δωρεάν) + ετήσιο 99$ για δημοσίευση</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Έλεγχος δημοσίευσης</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Χαλαρός, από λίγες ώρες έως λίγες μέρες</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Αυστηρός, 1-7 ημέρες είναι ο κανόνας</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Εγκατάσταση και δοκιμή</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">APK: το μοιράζεσαι και το εγκαθιστάς ελεύθερα</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Περιορισμένη διανομή· για τεστ χρειάζεται υπογραφή/TestFlight</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Περιβάλλον εσόδων</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Κυρίως διαφημίσεις / τοπικά κανάλια</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Καλύτερες συνήθειες πληρωμών εντός εφαρμογής στο App Store</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Κόστος εκμάθησης</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Πολλές έννοιες (τα τέσσερα βασικά components κ.ά.)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Κλειστό οικοσύστημα αλλά ενιαίο, με άριστη τεκμηρίωση</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Σύγκριση των διαδρομών ανάπτυξης Android και iOS (Αύγουστος 2026)

Πάμε στα ίσια: αν ο υπολογιστής σου δεν είναι Mac, το ερώτημα δεν χρειάζεται καν σκέψη — το Android είναι η μοναδική επιλογή. Αν έχεις Mac, τα μέρη 8 και 9 του βιβλίου μπορούν να διαβαστούν παράλληλα· η λογική του προγραμματισμού είναι κοινή, και ό, τι μάθεις στη μία πλευρά θα σε βοηθήσει να μάθεις την άλλη πολύ πιο γρήγορα.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Σειρά σου: δες το «Android» μέσα στο τηλέφωνό σου

{class="mt-1"}
Άνοιξε στο τηλέφωνο [Ρυθμίσεις] → [Σχετικά με το τηλέφωνο] (ή «Σχετικά με τη συσκευή»), βρες τη γραμμή «Έκδοση Android» — αν την πατήσεις αρκετές φορές συνεχόμενα, θα ενεργοποιηθεί και το μίνι παιχνίδι-έκπληξη του συστήματος. Σημείωσε τον αριθμό της έκδοσής σου και σύγκρινε τον με τον παραπάνω πίνακα για να δεις σε ποια γενιά ανήκει. Το τηλέφωνό σου είναι η πρώτη σου «συσκευή δοκιμών».
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Σύνοψη κεφαλαίου

- Το Android γεννήθηκε το 2008· το 2026 είναι το λειτουργικό κινητών με τη μεγαλύτερη μερίδα αγοράς, με δισεκατομμύρια ενεργές συσκευές
- Νεότερη επίσημη έκδοση: Android 17· οι mainstream εφαρμογές στηρίζουν τουλάχιστον Android 8-10, για να είναι μεγάλο το κοινό
- Για νέα projects: πάντα Kotlin — 30%+ λιγότερος κώδικας, προστασία από null, επίσημη προτίμηση της Google
- APK για προσωπική εγκατάσταση, AAB για το κατάστημα· το SDK είναι το επίσημο «κιτ εξοπλισμού» ανάπτυξης
- Τυπικό tech stack του 2026: Kotlin + Compose + MVVM + Room + Retrofit + Gradle + Android Studio
:::
