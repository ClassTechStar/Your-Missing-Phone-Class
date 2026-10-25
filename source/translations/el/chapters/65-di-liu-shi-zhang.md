---
id: di-liu-shi-zhang
num: 60
part: ios-kai-fa-pian
nav: Κεφάλαιο 60: Στήσε το περιβάλλον ανάπτυξης — Xcode και το πρώτο σου έργο
toc: default
kind: chapter
---

### Κεφάλαιο 60: Στήσιμο περιβάλλοντος ανάπτυξης — Xcode και το πρώτο project

{class="chapter-intro mb-4"}
Για να κάνεις καλή δουλειά, πρέπει πρώτα να ακονίσεις τα εργαλεία σου. Σε αυτό το κεφάλαιο στήνουμε την «κουζίνα»: εγκαθιστούμε το Xcode, βάζουμε τον προσομοιωτή να τρέξει, δημιουργούμε το πρώτο σου iOS project και ύστερα ξεδιπλώνουμε τη δομή του project για να τη δεις καθαρά. Όταν το περιβάλλον είναι έτοιμο, θα δεις για πρώτη φορά τον κώδικά σου να γίνεται ένα κουμπί που πατάς — τη στιγμή αυτή πολλοί τη θυμούνται μια ζωή.

#### Α. Απόκτησε ένα Mac

Ας πούμε πρώτα το εμπόδιο: η ανάπτυξη iOS γίνεται μόνο σε macOS. Αν δεν έχεις Mac, έχεις τρεις επιλογές: να αγοράσεις ένα (αρκεί ακόμα κι ένα μεταχειρισμένο Mac mini ή MacBook Air), να νοικιάσεις ένα cloud Mac για λίγο καιρό, ή να διαβάσεις πρώτα το όγδοο μέρος, «Πρακτική ανάπτυξη Android» (δουλεύει και με Windows).

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Στοιχείο</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ελάχιστες απαιτήσεις</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Άνετο επίπεδο (προτεινόμενο)</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Τσιπ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple Silicon (από M1)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">M2 ή νεότερο</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Μνήμη</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">8GB</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">16GB</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Δίσκος</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Κράτα 40GB+ (το ίδιο το Xcode είναι πολύ βαρύ)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">256GB και πάνω</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Λειτουργικό</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Το πιο πρόσφατο macOS</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Κράτα το σε αυτόματη ενημέρωση</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Οδηγός ρυθμίσεων Mac για ανάπτυξη (Αύγουστος 2026)

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Συμβουλή: μπορείς να μάθεις τη γλώσσα ακόμα και χωρίς Mac

{class="mt-1"}
Το δωρεάν Swift Playgrounds στο iPad διδάσκει τα βασικά της γλώσσας Swift (χωρίς Mac)· μπορείς μάλιστα να το εγκαταστήσεις και σε iPhone. Εξασκήσου καλά στο Playgrounds στα θέματα γλώσσας του Κεφαλαίου 61, και όταν αποκτήσεις Mac θα πετάξεις αμέσως. Το «ακόνισμα δεν αργεί το κόψιμο» — ακριβώς γι' αυτό μιλάμε.
:::

#### Β. Εγκατάσταση Xcode

Το Xcode είναι το επίσημο ολοκληρωμένο περιβάλλον ανάπτυξης της Apple και είναι δωρεάν. Εγκαθίσταται σε τρία βήματα:

1. Στο Mac άνοιξε το App Store, ψάξε «Xcode» και πάτα Εγκατάσταση — πρόσεξε ότι είναι αρκετά GB, διάλεξε μια ώρα με καλύτερη ταχύτητα internet·
2. Μετά την εγκατάσταση, στην πρώτη εκκίνηση αποδέξου τη συμφωνία χρήσης και άσε τα components να εγκατασταθούν (γίνεται αυτόματα)·
3. Στο μενού Xcode > Settings > Locations βεβαιώσου ότι έχουν επιλεγεί τα Command Line Tools — τα εργαλεία γραμμής εντολών είναι προϋπόθεση για πολλά scripts και εργαλεία τρίτων.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Προσοχή: το «παιχνίδι αντιστοίχισης» έκδοσης και λειτουργικού

{class="mt-1"}
Το νέο Xcode συχνά απαιτεί το πιο πρόσφατο macOS, ενώ τα παλιά Mac μπορεί να κολλήσουν σε παλιά έκδοση. Για δημοσίευση στο App Store, η Apple ζητά build με πιο πρόσφατο Xcode (συνήθως δίνει μια περίοδο χάρης). Γι' αυτό μην αργείς πολύ με τις ενημερώσεις — οι προγραμματιστές iOS είναι από τους πιο επιμελείς στο να «τρέχουν τα τελευταία».
:::

#### Γ. Δημιούργησε το πρώτο σου project

Άνοιξε Xcode > Create New Project > επίλεξε iOS > template App, και συμπλήρωσε:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Στοιχείο</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Τι συμπληρώνεις</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Εξήγηση</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Product Name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstApp</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Όνομα εφαρμογής</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Team</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Το Apple ID σου (δωρεάν)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Για την υπογραφή· αρκεί ο ατομικός λογαριασμός</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Organization Identifier</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">com.example</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Σχηματίζει το bundle identifier μαζί με το Product Name</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Interface</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Το framework κεντρικού άξονα του βιβλίου</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Language</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Αυτονόητο</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Τα πέντε πράγματα που συμπληρώνεις στη δημιουργία project

Αφού πατήσεις Create, το Xcode δημιουργεί ένα project που τρέχει αμέσως. Επίλεξε έναν προσομοιωτή πάνω αριστερά (π.χ. iPhone 17) και πάτα ▶ για εκτέλεση — μετά από λίγα δευτερόλεπτα θα εμφανιστεί στην οθόνη του προσομοιωτή ένα παράθυρο που γράφει «Hello, world!». Η πρώτη σου εφαρμογή iOS μόλις γεννήθηκε.

#### Δ. Η δομή του project αναλυμένη: τι κάνει κάθε αρχείο

Αριστερά βρίσκεται ο project navigator· ως αρχάριος αρκεί να γνωρίζεις τα εξής:

::: div .figure
```html
<svg style="max-width:100%;height:auto" width="600" height="290" viewBox="0 0 600 290" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="600" height="290" fill="#fafafa" rx="8"/>
      <text x="20" y="28" font-size="13" font-weight="bold" fill="#111827">MyFirstApp/ βασικός φάκελος έργου</text>
      <rect x="30" y="42" width="540" height="225" fill="#ffffff" stroke="#d1d5db" rx="6"/>
      <rect x="45" y="56" width="250" height="196" fill="#eef2ff" rx="5"/>
      <text x="56" y="78" font-size="11" fill="#1e1b4b" font-weight="bold">MyFirstApp/ (φάκελος κώδικα)</text>
      <text x="66" y="100" font-size="10" fill="#374151">├ MyFirstAppApp.swift  ← είσοδος προγράμματος</text>
      <text x="66" y="120" font-size="10" fill="#374151">├ ContentView.swift  ← κύρια οθόνη</text>
      <text x="66" y="140" font-size="10" fill="#374151">└ Assets.xcassets  ← εικονίδια, εικόνες, χρώματα</text>
      <text x="56" y="166" font-size="10" fill="#6b7280">(όλα τα νέα αρχεία μπαίνουν σε αυτόν τον φάκελο)</text>
      <text x="56" y="196" font-size="10" fill="#1e1b4b" font-weight="bold">Καρτέλα Info / Info.plist</text>
      <text x="66" y="216" font-size="10" fill="#6b7280">Δήλωση εφαρμογής: όνομα, δι και ώματα, ρυθμίσεις</text>
      <rect x="310" y="56" width="245" height="196" fill="#f0fdf4" rx="5"/>
      <text x="321" y="78" font-size="11" fill="#065f46" font-weight="bold">Άλλες σημαντικές θέσεις</text>
      <text x="331" y="100" font-size="10" fill="#374151">📁 Preview Content/  ← υλικό προεπισκόπησης</text>
      <text x="331" y="122" font-size="10" fill="#374151"><i class="fas fa-bullseye mr-1"></i> Ρυθμίσεις Target (μπλε εικονίδιο έργου)</text>
      <text x="331" y="142" font-size="10" fill="#6b7280">— εδώ είναι η έκδοση, το ελάχιστο σύστημα και η υπογραφή</text>
      <text x="331" y="168" font-size="10" fill="#374151"><i class="fas fa-flask mr-1"></i> MyFirstAppTests/  ← unit tests</text>
      <text x="331" y="188" font-size="10" fill="#374151">📱 MyFirstAppUITests/ ← τεστ οθόνης</text>
      <text x="331" y="216" font-size="10" fill="#9ca3af">(το πρότυπο τεστ έχει δημιουργηθεί, χρήση στο κεφάλαιο 67)</text>
    </svg>
```

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Εικόνα 2: Η δομή project του Xcode που πρέπει οπωσδήποτε να ξέρεις
:::

- MyFirstAppApp.swift: Το σημείο εκκίνησης του προγράμματος· στο SwiftUI είναι λίγες μόνο γραμμές — «ξεκίνα και δείξε την κύρια οθόνη»·
- ContentView.swift: Η κύρια προβολή· ό, τι βλέπεις τώρα βρίσκεται εδώ·
- Assets.xcassets: Η αποθήκη πόρων — εδώ μπαίνουν εικονίδια, εικόνες και χρώματα·
- Ρυθμίσεις Target: πάτα στο μπλε εικονίδιο του project αριστερά για να μπεις· μέσα είναι ο αριθμός έκδοσης, η ελάχιστη έκδοση iOS και η υπογραφή. Εδώ ρυθμίζεται και το εμφανιζόμενο όνομα και το εικονίδιο της εφαρμογής.

#### Ε. Τεχνικές ταχύτητας στο Xcode: τα πέντε «πρόσθετα» συντομεύσεων για αρχάριους

Όταν τα εξασκηθείς, θα φαίνεσαι «πολύ επαγγελματίας»:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ενέργεια</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Συντόμευση</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Χρησιμότητα</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Εκτέλεση</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘R</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Build και εκτέλεση</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Άνοιγμα/εναλλαγή προεπισκόπησης στο canvas</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌥⌘↩</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ο διακόπτης του «ό, τι βλέπεις το παίρνεις»</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Μορφοποίηση εσοχών</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌃I</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Τακτοποιεί αυτόματα τις εσοχές του επιλεγμένου κώδικα</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Γρήγορο άνοιγμα αρχείου</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘O</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Γράφεις το όνομα του αρχείου και ανοίγει αμέσως (το πιο συχνό!)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Σχολιασμός/αίρεση σχολίου</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ενεργοποιεί/απενεργοποιεί κώδικα όποτε θες κατά το debugging</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Οι πιο συχνές συντομεύσεις του Xcode (το πεντασύνολο για αρχάριους)

Δύο ακόμα κρυφά δώρα: πολλαπλοί προσομοιωτές (τρέχεις ταυτόχρονα iPhone και iPad για να συγκρίνεις στοιχήσεις) και η βιβλιοθήκη snippets (σύρε τις γραμμές κώδικα που χρησιμοποιείς συχνά στο Snippets panel δεξιά, και την επόμενη φορά τις εισάγεις με ένα πάτημα) — άρχισε να χρησιμοποιείς τα εργαλεία ταχύτητας, και το «χέρι» θα έρθει από μόνο του.

#### ΣΤ. Δοκιμή σε πραγματική συσκευή: βάλε την εφαρμογή στο iPhone σου

Ο προσομοιωτής είναι καλός, αλλά ο προορισμός είναι η πραγματική συσκευή. Με δωρεάν Apple ID μπορείς να κάνεις δοκιμές σε πραγματική συσκευή:

1. Σύνδεσε το iPhone με καλώδιο δεδομένων (ή κάνε ασύρματο debugging στο ίδιο Wi-Fi)·
2. Στη λίστα συσκευών στο πάνω μέρος του Xcode επίλεξε το κινητό σου· την πρώτη φορά θα σου ζητήσει σύνδεση Apple ID και θα ρυθμίσει αυτόματα την υπογραφή·
3. Στο iPhone: [Ρυθμίσεις] > [Γενικά] > [Διαχείριση VPN & Συσκευών] και εμπιστεύσου το πιστοποιητικό προγραμματιστή σου·
4. Πάτα ▶ και η εφαρμογή εγκαθίσταται στη πραγματική συσκευή.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Προσοχή: ο «περιορισμός των επτά ημερών» του δωρεάν λογαριασμού

{class="mt-1"}
Οι εφαρμογές που υπογράφονται με δωρεάν Apple ID λήγουν μετά από 7 ημέρες (μια επανεκτέλεση τις ανανεώνει). Είναι ο μηχανισμός της Apple κατά της κατάχρησης, και για τη φάση της μάθησης αρκεί πλήρως· ο επί πληρωμή λογαριασμός προγραμματιστή (99 δολάρια/έτος) δεν έχει αυτόν τον περιορισμό — θα το πούμε αναλυτικά στο Κεφάλαιο 67.
:::

#### Ζ. Πρώτες δοκιμές + πρώτες βοήθειες για συχνά σφάλματα

Άνοιξε το ContentView.swift, άλλαξε το κείμενο μέσα στο Text("Hello, world!") με το όνομά σου και πάτα ⌘R για επανεκτέλεση — σε λίγα δευτερόλεπτα το όνομά σου εμφανίζεται στον προσομοιωτή. Συγχαρητήρια — ολοκλήρωσες τον πρώτο σου πλήρη κύκλο «αλλαγή κώδικα > build > εγκατάσταση > εκτέλεση».

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Σύμπτωμα σφάλματος</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Συχνή αιτία</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Αντίδοτο</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Σφάλμα υπογραφής (Signing)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Δεν έχει επιλεγεί Team ή το πιστοποιητικό έχει λήξει</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Στα Target > Signing τσέκαρε τον λογαριασμό σου· με δωρεάν λογαριασμό, τρέξε ξανά μία φορά</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ο προσομοιωτής δείχνει μαύρη οθόνη / δεν ανοίγει</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Κατεστραμμένο image</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Μενού Device > Erase All Content· ή διέγραψε τον προσομοιωτή και πρόσθεσέ τον ξανά</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Το Xcode κατεβαίνει αργά / δεν εγκαθίσταται</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Διακυμάνσεις δικτύου στο App Store</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Δοκίμασε άλλη ώρα· ή κατέβασε το offline πακέτο .xip από την ιστοσελίδα προγραμματιστών της Apple</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Πίνακας πρώτων βοηθειών για σφάλματα περιβάλλοντος (για αρχάριους)

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Ας το δοκιμάσουμε: ολοκλήρωσε τη λίστα του «τελετουργικού ανάπτυξης»

{class="mt-1"}
① Εγκατάστησε το Xcode και βεβαιώσου ότι ο προσομοιωτής τρέχει· ② τρέξε την εφαρμογή σου σε πραγματική συσκευή και κράτα ένα screenshot για ανάμνηση· ③ άλλαξε το κείμενο Hello με το όνομά σου· ④ στις ρυθμίσεις Target άλλαξε το εμφανιζόμενο όνομα της εφαρμογής σε «Η πρώτη μου εφαρμογή». Αφού κάνεις αυτά τα τέσσερα βήματα, γίνεσαι άνθρωπος με έργα.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Σύνοψη κεφαλαίου

- Σκληρά εμπόδια: Mac + Xcode· χωρίς Mac, μάθε πρώτα τη γλώσσα στο Swift Playgrounds του iPad
- Το Xcode εγκαθίσταται από το App Store· οι νέες εκδόσεις θέλουν νέο λειτουργικό, μην καθυστερείς τις ενημερώσεις
- Τα πέντε στοιχεία για νέο project: όνομα, Team, αναγνωριστικό οργανισμού, SwiftUI, Swift
- Μνημόνιο του project: όλος ο κώδικας στον φάκελο MyFirstApp/· οι ρυθμίσεις Target διαχειρίζονται έκδοση και υπογραφή
- Η δοκιμή σε πραγματική συσκευή με δωρεάν Apple ID έχει περιορισμό υπογραφής 7 ημερών· ο επί πληρωμή λογαριασμός δεν τον έχει
- Η καθημερινότητα ανάπτυξης = αλλαγή κώδικα > ⌘R > δες το αποτέλεσμα, ξανά και ξανά
:::
