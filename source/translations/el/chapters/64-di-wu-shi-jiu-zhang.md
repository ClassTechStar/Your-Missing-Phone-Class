---
id: di-wu-shi-jiu-zhang
num: 59
part: ios-kai-fa-pian
nav: Κεφάλαιο 59: Γνώρισε το iOS — το οικοσύστημα της Apple και το οικοσύστημα ανάπτυξης
toc: default
kind: chapter
---

### Κεφάλαιο 59: Γνωριμία με iOS — το οικοσύστημα Apple και το οικοσύστημα ανάπτυξης

{class="chapter-intro mb-4"}
Συγχαρητήρια για την απόφαση — από «άνθρωπος που χρησιμοποιεί iPhone» γίνεσαι «άνθρωπος που γράφει εφαρμογές για iPhone». Πριν πιάσεις δουλειά, ας απλώσουμε τον χάρτη: από πού ήρθε το iOS; τι σημαίνει για τον προγραμματιστή ο «κλειστός κήπος» της Apple; και τι συμβαίνει στον δρόμο από τα δάχτυλά σου στο πληκτρολόγιο έως το κινητό του χρήστη;

#### 1. Η ιστορία του iOS: ένα κινητό άλλαξε μια ολόκληρη βιομηχανία

Τον Ιανουάριο του 2007, ο Jobs στην παρουσίαση τράβηξε από την τσέπη το πρώτο iPhone. Τότε δεν υποστήριζε καν εφαρμογές τρίτων — μέχρι που το 2008 η Apple έβγαλε το App Store και το iPhone SDK, επιτρέποντας σε προγραμματιστές απ’ όλο τον κόσμο να γράφουν λογισμικό για iPhone. Σε εκείνη τη στιγμή γεννήθηκε η «οικονομία των εφαρμογών»: σήμερα στο App Store υπάρχουν εκατομμύρια εφαρμογές, και οι συνολικές αποζημιώσεις στους προγραμματιστές έχουν ξεπεράσει τις εκατοντάδες δισεκατομμύρια δολάρια.

Και το ίδιο το σύστημα εξελίσσεται: αρχικά λεγόταν iPhone OS, το 2010 μετονομάστηκε σε iOS· οι εκδόσεις έφτασαν μέχρι το iOS 17 (2023), και το 2025 η Apple άλλαξε την ονομασία ώστε να ακολουθεί το έτος — το iOS 26 κυκλοφόρησε το 2025, και τον Αύγουστο 2026 η τρέχουσα έκδοση είναι το iOS 27. Οι ονομασίες αλλάζουν, αλλά ένα δεν άλλαξε ποτέ: οι συνήθειες πληρωμής των χρηστών iOS και η φήμη της ποιότητας λογισμικού θεωρούνται οι καλύτερες της κινητής οικοσύστημα — η ίδια εφαρμογή συχνά βγάζει στο iOS αισθητά μεγαλύτερα έσοδα απ’ ό, τι στο Android.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ορόσημο</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Έτος</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Σημαντικό για τους προγραμματιστές</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Κυκλοφορία του App Store</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2008</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Άνοιγμα του οικοσυστήματος ανάπτυξης τρίτων</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Κυκλοφορία της Swift</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2014</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Η σύγχρονη γλώσσα ανάπτυξης iOS κάνει την εμφάνισή της</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Κυκλοφορία του SwiftUI</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2019</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Δηλωτικό framework διεπαφής, ο κεντρικός άξονας του βιβλίου</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">iOS 26 (το έτος της μετονομασίας)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2025</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Η ονομασία ακολουθεί το έτος· πλήρης ενσωμάτωση της Apple Intelligence</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">iOS 27</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2026</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Η πιο πρόσφατη έκδοση (η βάση του βιβλίου)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Ορόσημα της ανάπτυξης iOS (έως τον Αύγουστο 2026)

#### Β. Ο «κλειστός κήπος»: οι «κανόνες» και τα «κέρδη» του οικοσυστήματος της Apple

Το οικοσύστημα της Apple συχνά περιγράφεται ως «κλειστός κήπος» (Walled Garden) — πολλοί κανόνες και αυστηρός έλεγχος: οι εφαρμογές πρέπει να περάσουν από έγκριση για να ανέβουν στο κατάστημα, η ανάπτυξη γίνεται μόνο με Mac και Xcode, και η διανομή περνάει κυρίως από το App Store. Σου φαίνεται στριμωγμένο; Όμως για τον προγραμματιστή, αυτοί οι κανόνες φέρνουν αληθινά, χοντρά κέρδη:

- Ελάχιστος κατακερματισμός συσκευών: τα μοντέλα iPhone μετριούνται στα δάχτυλα, με εξαιρετικά ομοιόμορφα μεγέθη οθόνης και εκδόσεις συστήματος — προσαρμόζεις 5 μοντέλα και καλύπτεις το 95% των χρηστών (στο Android ίσως χρειαστούν δεκάδες)·
- Πολύ υψηλό ποσοστό αναβαθμίσεων: μέσα σε λίγες εβδομάδες από την κυκλοφορία του νέου συστήματος το 70-80% των χρηστών το έχει αναβαθμίσει, οπότε χρησιμοποιείς άφοβα τα νέα API χωρίς να λογαριάζεις «παλιό σύστημα πέντε ετών»·
- Οι χρήστες έχουν καλή συνήθεια πληρωμής: οι χρήστες του App Store ξοδεύουν πιο πρόθυμα για εφαρμογές και αγορές εντός εφαρμογής·
- Η έγκριση είναι αυστηρή, αλλά το κατάστημα μένει καθαρό: λίγες απομιμήσεις και κακόβουλες εφαρμογές, και τα καλά προϊόντα βλέπουν πιο εύκολα το φως.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Προσοχή: πρώτα να ξεκαθαρίσουμε το κόστος

{class="mt-1"}
Η ανάπτυξη iOS έχει σκληρά εμπόδια: χρειάζεσαι οπωσδήποτε ένα Mac (το Xcode τρέχει μόνο σε macOS), και για δημοσίευση θέλει λογαριασμό προγραμματιστή 99 δολαρίων/έτος (ο δωρεάν λογαριασμός ατομικού προγραμματιστή επιτρέπει δοκιμές σε πραγματική συσκευή τοπικά, αλλά όχι δημοσίευση). Ζύγισε καλά αυτή την επένδυση πριν ξεκινήσεις — τα καλά νέα είναι ότι στη φάση της μάθησης ο δωρεάν λογαριασμός φτάνει απόλυτα, όπως θα δούμε στο Κεφάλαιο 60.
:::

#### Γ. Σε ποια γλώσσα γράφεις: Objective-C ή Swift;

Και στην ιστορία της ανάπτυξης iOS υπήρξαν δύο «πρωταγωνιστές». Η Objective-C είναι η παλαιά φρουρά — χρησιμοποιήθηκε από το 2008 έως το 2014· η Swift είναι η νέα γλώσσα που κυκλοφόρησε η Apple το 2014 και έχει εξελιχθεί έως τη Swift 6 (κυκλοφόρησε το 2024 με αυστηρούς ελέγχους concurrency). Το 2026, σχεδόν όλα τα νέα projects γράφονται σε Swift.

Μια ειλικρινής κουβέντα για σένα που ξεκινάς από το μηδέν: μάθε κατευθείαν Swift, και την Objective-C μην την κοιτάξεις καν — εκτός αν μετά την πρόσληψή σου χρειαστεί να συντηρείς legacy κώδικα δέκα ετών. Τα πλεονεκτήματα της Swift: καθαρή σύνταξη (χωρίς τα ";" στο τέλος των γραμμών και τα header files της εποχής της C), ο μηχανισμός των προαιρετικών τιμών (Optional) που εξαλείφει από τη γλώσσα τα «crash λόγω κενού δείκτη», η άψογη συνεργασία με το SwiftUI, και το Swift Playgrounds στο iPad για να μαθαίνεις παίζοντας.

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
Στυλ Objective-C (απολίθωμα από άλλη εποχή)

{class="font-mono text-xs leading-relaxed"}
NSString *name = @"Γιώργος"; [name stringByAppendingString:@"Γεια σου"]; // Το τρίο: αγκύλες + δείκτες + ";"
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
Στυλ Swift (μοντέρνο και καθαρό)

{class="font-mono text-xs leading-relaxed"}
var name = "Γιώργος" name += "Γεια σου" // Ευθύ σαν φυσική γλώσσα
:::
:::

#### Δ. Πώς γεννιέται μια εφαρμογή;

Όπως σε κάθε πλατφόρμα, έτσι και η γέννηση μιας εφαρμογής iOS ακολουθεί τη δική της γραμμή παραγωγής. Η εκδοχή της Apple όμως έχει δύο επιπλέον σταθμούς ελέγχου:

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-lightbulb mr-1"></i> Ιδέα</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center">📐 Σχεδίαση (οθόνη+λειτουργίες)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-keyboard mr-1"></i> Γράφει κώδικα (Swift + SwiftUI)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hammer mr-1"></i> Μεταγλώττιση και υπογραφή</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> Τεστ (emulator+πραγματική συσκευή)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-stamp mr-1"></i> Έλεγχος Apple</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-party-horn mr-1"></i> Κυκλοφορία στο App Store</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Εικόνα 1: Η πλήρης διαδρομή μιας εφαρμογής iOS από την ιδέα ως το κατάστημα (πρόσεξε το επιπλέον στάδιο της «έγκρισης»)
:::

Βασικές έννοιες της διαδικασίας:

- Υπογραφή (Signing): Κάθε εφαρμογή iOS πρέπει να είναι «υπογεγραμμένη» για να εγκατασταθεί — αποδεικνύει ότι «το πακέτο προέρχεται από σένα και δεν έχει παραποιηθεί». Στη φάση της μάθησης το Xcode υπογράφει αυτόματα με το Apple ID σου· για δημοσίευση χρησιμοποιείται πιστοποιητικό προγραμματιστή. Θα το πούμε αναλυτικά στο Κεφάλαιο 67.
- Προσομοιωτής (Simulator): Ένα εικονικό iPhone μέσα στο Mac, το κύριο πεδίο δράσης της ανάπτυξης και του εντοπισμού σφαλμάτων. Τρέχει στον επεξεργαστή του Mac, γι' αυτό είναι ιδιαίτερα ευέλικτο — η εμπειρία είναι μια τάξη καλύτερη από τον προσομοιωτή Android.
- TestFlight: Το επίσημο εργαλείο της Apple για «δοκιμαστική διανομή» — πριν τη δημοσίευση στέλνεις τη δοκιμαστική έκδοση σε έως 10.000 δοκιμαστές, που την εγκαθιστούν και τη δοκιμάζουν μέσα από την εφαρμογή TestFlight. Μια κομψότητα που έχει μόνο το οικοσύστημα iOS.

#### Ε. Η τεχνολογική στοίβα του iOS με τη μια ματιά: η «λίστα εξοπλισμού» σου

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Επίπεδο</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Κυρίαρχη επιλογή (2026)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Σε τι χρησιμεύει</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Γλώσσα</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift 6</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Η γλώσσα για τη λογική</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Διεπαφή</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI + οδηγός σχεδιασμού της Apple (HIG)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ζωγραφίζεις τη διεπαφή με κώδικα</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Αρχιτεκτονική</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MVVM + @Observable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Χωρίζει τη διεπαφή από τη λογική</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Αποθήκευση δεδομένων</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftData (βάση δεδομένων) + UserDefaults (ρυθμίσεις)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Αποθηκεύει τα δεδομένα στο κινητό</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Δίκτυο</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">URLSession + async/await + Codable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Επικοινωνία με τον διακομιστή</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Εργαλεία build</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode Build System / xcodebuild</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Μετατρέπει τον κώδικα σε πακέτο εγκατάστασης</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Περιβάλλον ανάπτυξης</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode (μόνο για macOS)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Το επίσημο IDE της Apple</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Η κυρίαρχη τεχνολογική στοίβα του iOS το 2026 με μια ματιά

Το πρόσεξες; Η λίστα είναι πιο κοντή από του Android — γιατί η Apple έχει «αναλάβει» πολλά εξ αρχής. Το τίμημα του κλειστού οικοσυστήματος είναι η ελευθερία· το κέρδος είναι η ανέση: δεν σπάς το κεφάλι σου για ποια βιβλιοθήκη δικτύου ή ποια βάση δεδομένων θα διαλέξεις — ό, τι δίνει η επίσημη πλευρά είναι συνήθως η καλύτερη λύση.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Ας το δοκιμάσουμε: δες το «μητρώο Apple» του τηλεφώνου σου

{class="mt-1"}
Άνοιξε στο iPhone: [Ρυθμίσεις] > [Γενικά] > [Πληροφορίες], και σημείωσε τρία πράγματα: την έκδοση iOS, το όνομα της συσκευής και τον διαθέσιμο χώρο. Ύστερα κάνε μια βόλτα στη σελίδα «Σήμερα» του App Store και κοίτα τα στιγμιότυπα και τα κείμενα των κορυφαίων εφαρμογών — από σήμερα η ματιά σου στο κατάστημα περνάει από «χρήστης» σε «προγραμματιστής».
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Σύνοψη κεφαλαίου

- Το 2008 κυκλοφόρησε το App Store και γεννήθηκε η «οικονομία των εφαρμογών»· το 2026 η τρέχουσα έκδοση είναι το iOS 27
- Ο απολογισμός του «κλειστού κήπου»: πολλοί κανόνες, αλλά λίγες συσκευές, φρέσκες εκδόσεις, χρήστες που πληρώνουν πρόθυμα και καθαρό κατάστημα
- Σκληρά εμπόδια: απαραίτητο το Mac· για δημοσίευση λογαριασμός προγραμματιστή 99 δολάρια/έτος· στη φάση μάθησης φτάνει ο δωρεάν λογαριασμός
- Γλώσσα: ξεκίνα κατευθείαν με Swift· η Objective-C ανήκει μόνο στον legacy κώδικα
- Η γραμμή παραγωγής έχει ένα στάδιο παραπάνω από του Android: την έγκριση της Apple· το TestFlight είναι το υπέρτατο όπλο της δοκιμαστικής διανομής
- Η βασική στοίβα του 2026: Swift 6 + SwiftUI + MVVM + SwiftData + URLSession + Xcode
:::
