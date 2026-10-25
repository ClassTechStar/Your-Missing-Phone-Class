---
id: di-si-shi-jiu-zhang
num: 49
part: an-zhuo-kai-fa-pian
nav: Κεφάλαιο 49: Στήσε το περιβάλλον ανάπτυξης — Android Studio και το πρώτο σου έργο
toc: default
kind: chapter
---

### Κεφάλαιο 49: Στήσιμο του περιβάλλοντος ανάπτυξης — Android Studio και το πρώτο project

{class="chapter-intro mb-4"}
Για καλή δουλειά, πρώτα φτιάξε τα εργαλεία. Σε αυτό το κεφάλαιο στήνουμε την «κουζίνα»: εγκαθιστούμε το Android Studio, βάζουμε τον emulator σε λειτουργία, δημιουργούμε το πρώτο Android project της ζωής σου και μετά αποσυναρμολογούμε τη δομή του project για να τη δούμε καθαρά. Μόλις στηθεί το περιβάλλον, θα δεις για πρώτη φορά τον κώδικά σου να γίνεται ένα κουμπί που μπορείς να πατήσεις — αυτή η στιγμή, για πολλούς, μένει για μια ζωή.

#### 1. Εγκατάσταση του Android Studio

Το Android Studio είναι το επίσημο ολοκληρωμένο περιβάλλον ανάπτυξης (IDE) της Google· δωρεάν, με όλα μέσα: γράφεις κώδικα, βλέπεις προεπισκόπηση της διεπαφής, κάνεις debugging, πακετάρεις. Εγκατάσταση σε τέσσερα βήματα:

1. Άνοιξε την επίσημη σελίδα developer.android.com/studio και κατέβασε τη νεότερη σταθερή έκδοση (τον Αύγουστο 2026 είναι η έκδοση μετά το Narwhal· υπάρχει για Windows/Mac/Linux)·
2. Τρέξε το πακέτο εγκατάστασης και πάτα «Επόμενο» διαρκώς — ο οδηγός εγκατάστασης φέρνει αυτόματα το Android SDK και τα στοιχεία του emulator·
3. Στην πρώτη εκκίνηση κατέβασε τα στοιχεία SDK που ζητά (η προεπιλογή είναι εντάξει· θα χρειαστούν μερικά λεπτά και μερικά GB χώρου)·
4. Στο τέλος θα δεις τη σελίδα καλωσορίσματος — συγχαρητήρια, η «κουζίνα» είναι έτοιμη.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Προσοχή: γνώρισε τις απαιτήσεις σε υλικό

{class="mt-1"}
Το Android Studio είναι φανερά «φαγωμένο» στη μνήμη: προτείνεται τουλάχιστον 16GB RAM (με 8GB τρέχει, αλλά ο emulator σε ταλαιπωρεί), 20GB+ ελεύθερου δίσκου και CPU με υποστήριξη virtualization (ενεργοποίησε το VT-x/AMD-V μέσα στο BIOS). Αν ο υπολογιστής σου είναι πράγματι παλιός, μπορείς να αντικαταστήσεις τον emulator με «debugging σε πραγματική συσκευή» (θα το δούμε στην 4 η ενότητα του κεφαλαίου) — η εμπειρία είναι μάλιστα πιο ομαλή.
:::

#### 2. Δημιουργία του πρώτου σου project

Στη σελίδα καλωσορίσματος πάτα New Project, διάλεξε το template Empty Activity (το πιο καθαρό για αρχάριους) και συμπλήρωσε τρία πράγματα:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ρύθμιση</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Τι συμπληρώνεις</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Επεξήγηση</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">My First App</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Το όνομα της εφαρμογής, εμφανίζεται στην αρχική οθόνη του τηλεφώνου</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Package name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">com.example.myfirstapp</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Παγκοσμίως μοναδικό αναγνωριστικό· κατά συνήθεια «ανάποδο domain name»· προς το παρόν άφησε το προεπιλεγμένο</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Minimum SDK</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">API 26(Android 8.0)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ελάχιστη υποστηριζόμενη έκδοση· καλύπτει 95%+ των συσκευών</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Τα τρία πράγματα που συμπληρώνεις στη δημιουργία project

Με το Finish, το Android Studio θα κατεβάσει τις εξαρτήσεις και θα χτίσει το project μέσω Gradle (την πρώτη φορά θα περιμένεις μερικά λεπτά, μετά θα πηγαίνει πολύ πιο γρήγορα). Όταν ολοκληρωθεί το build, έχεις μια εφαρμογή που τρέχει — που προς το παρόν εμφανίζει μόνο μια γραμμή «Hello Android!».

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Συμβουλή: τα μυστικά του package name

{class="mt-1"}
Το package name είναι σαν ο «αριθμός ταυτότητας» της εφαρμογής: δεν επαναλαμβάνεται παγκοσμίως και δεν αλλάζει μετά τη δημοσίευση. Για προσωπικές εξασκήσεις αρκεί το com.example.xxx· σε πραγματικό προϊόν βάλε το ανάποδο δικό σου domain name (π.χ. com.yourname.appname). Μην δημοσιεύσεις με com.example — το κατάστημα θα το απορρίψει.
:::

#### 3. Τρέξ' το: emulator και πραγματική συσκευή

Ο κώδικας έτοιμος — τώρα χρειάζεσαι ένα «τηλέφωνο» για να τον τρέξεις. Έχεις δύο επιλογές:

##### 1. Ο Emulator

Ο emulator δημιουργεί μια εικονική Android συσκευή μέσα στον υπολογιστή. Στο Android Studio άνοιξε Device Manager → Create Device, διάλεξε μια συσκευή (προτείνεται η σειρά Pixel) → διάλεξε ένα system image (με Google APIs) → κατέβασέ το → εκκίνησέ το. Μετά πάτα το πράσινο τρίγωνο Run στην μπάρα εργαλείων και, σε λίγα δευτερόλεπτα, η οθόνη του «τηλεφώνου» θα δείξει την εφαρμογή σου.

##### 2. Debugging σε πραγματική συσκευή (προτιμότερο)

Το πραγματικό τηλέφωνο είναι πάντα το πιο αληθινό περιβάλλον δοκιμής — η αίσθηση της ολίσθησης, το αληθινό δίκτυο, οι αληθινοί αισθητήρες: τίποτα από αυτά δεν φτάνει ο emulator. Το debugging σε πραγματική Android συσκευή είναι απλό:

1. Στο τηλέφωνο άνοιξε [Ρυθμίσεις] → [Σχετικά με το τηλέφωνο] και πάτα 7 φορές συνέχεια στο «Αριθμός έκδοσης», για να ανοίξουν οι «Επιλογές προγραμματιστή»·
2. Στις [Επιλογές προγραμματιστή] ενεργοποίησε τον εντοπισμό σφαλμάτων USB (USB debugging)·
3. Σύνδεσε το τηλέφωνο στον υπολογιστή με καλώδιο δεδομένων· στο παράθυρο του τηλεφώνου διάλεξε «Να επιτρέπεται ο εντοπισμός σφαλμάτων USB»·
4. Πίσω στο Android Studio, το τηλέφωνό σου θα εμφανιστεί στη λίστα συσκευών της μπάρας εργαλείων· πάτα Run.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Προσοχή-αποφυγή παγίδων: μη κρατάς ανοιχτό το USB debugging

{class="mt-1"}
Το USB debugging είναι σαν να ανοίγεις ένα «παραθυράκι» στον υπολογιστή. Όταν φορτίζεις σε δημόσιους χώρους ή συνδέεσαι σε υπολογιστή που δεν εμπιστεύεσαι, φρόντισε να κλείνεις το USB debugging, για να μη διαβάσει κάποιος τα δεδομένα σου μέσα από αυτό. Κλείσ' το κάθε φορά που τελειώνεις την ανάπτυξη — κάν' το συνήθεια.
:::

#### 4. Αποσυναρμολόγηση της δομής του project: τι κάνει κάθε αρχείο

Την πρώτη φορά που ανοίγεις project, το δέντρο αρχείων αριστερά μπορεί να σε ζαλίσει. Ησύχα· στην καθημερινή ανάπτυξη το 90% του χρόνου έχεις να κάνεις μόνο με τα παρακάτω:

::: div .figure
```html
<svg style="max-width:100%;height:auto" width="600" height="300" viewBox="0 0 600 300" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="600" height="300" fill="#fafafa" rx="8"/>
      <text x="20" y="30" font-size="13" font-weight="bold" fill="#111827">MyFirstApp/ βασικός φάκελος έργου</text>
      <rect x="30" y="45" width="540" height="230" fill="#ffffff" stroke="#d1d5db" rx="6"/>
      <text x="45" y="70" font-size="11" fill="#4f46e5" font-weight="bold">app/ ← εκεί γράφεις κώδικα</text>
      <rect x="60" y="82" width="240" height="178" fill="#eef2ff" rx="5"/>
      <text x="70" y="102" font-size="10" fill="#1e1b4b" font-weight="bold">src/main/</text>
      <text x="80" y="120" font-size="10" fill="#374151">├ java/…/MainActivity.kt  ← κώδικας λογικής</text>
      <text x="80" y="138" font-size="10" fill="#374151">├ res/  ← πόροι (εικόνες, κείμενα, χρώματα)</text>
      <text x="80" y="156" font-size="10" fill="#374151">└ AndroidManifest.xml  ← η "ταυτότητα" της εφαρμογής</text>
      <text x="70" y="180" font-size="10" fill="#1e1b4b" font-weight="bold">build.gradle.kts</text>
      <text x="80" y="198" font-size="10" fill="#6b7280">Δήλωση των βιβλιοθηκών (έκδοση SDK, Compose κ.λπ.)</text>
      <text x="70" y="222" font-size="10" fill="#1e1b4b" font-weight="bold">src/androidTest/ και test/</text>
      <text x="80" y="240" font-size="10" fill="#6b7280">Κώδικας αυτοματοποιημένων τεστ (χρήση στο κεφάλαιο 56)</text>
      <rect x="320" y="82" width="230" height="178" fill="#f0fdf4" rx="5"/>
      <text x="330" y="102" font-size="10" fill="#065f46" font-weight="bold">Άλλα αρχεία στον βασικό φάκελο</text>
      <text x="340" y="122" font-size="10" fill="#374151">gradle/ + gradlew.bat  ← scripts build</text>
      <text x="340" y="142" font-size="10" fill="#374151">settings.gradle.kts  ← ρυθμίσεις έργου</text>
      <text x="340" y="162" font-size="10" fill="#6b7280">(ο κανόνας του αρχάριου: ακούμπα μόνο στον φάκελο app/ </text>
      <text x="340" y="180" font-size="10" fill="#6b7280">τα υπόλοιπα βλέπε προς το παρόν ως "μαύρο κουτί", μην τα πειράξεις)</text>
      <text x="340" y="208" font-size="10" fill="#9ca3af">.gitignore  ← λίστα αγνόησης ελέγχου εκδόσεων</text>
    </svg>
```

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Σχήμα 2: Η δομή του project που πρέπει να ξέρει κάθε αρχάριος (κανόνας: πείραξε μόνο τον φάκελο app/)
:::

- MainActivity.kt: η «κύρια πόρτα» της εφαρμογής. Όταν ο χρήστης πατάει το εικονίδιο, αυτό είναι το πρώτο που «ξυπνά». Στο σημερινό template είναι υπεύθυνο για την εμφάνιση του «Hello Android!».
- AndroidManifest.xml: το «μητρώο» της εφαρμογής — δηλώνει πώς λέγεται η εφαρμογή, ποιο είναι το εικονίδιο της, ποιες σελίδες έχει και ποιες άδειες χρειάζεται (κάμερα, τοποθεσία κ.ά.).
- Ο φάκελος res/: η αποθήκη πόρων· εκεί αποθηκεύονται εικόνες, εικονίδια, κείμενα, χρώματα. Το να βάζεις τα κείμενα σε αρχεία πόρων αντί να τα γράφεις «δεμένα» στον κώδικα είναι καλή πρακτική στο Android (βοηθά τόσο στην αλλαγή γλώσσας όσο και στο θέμα).
- build.gradle.kts: η «συνταγή» του build — δηλώνει την ελάχιστη υποστηριζόμενη έκδοση και ποιες βιβλιοθήκες χρειάζεσαι (π.χ. Compose).

#### 5. Πρώτη δοκιμή: άλλαξε το «Hello» με το όνομά σου

Άνοιξε το MainActivity.kt και θα δεις τον κώδικα που δημιούργησε το Compose template. Βρες τη γραμμή Text("Hello Android!") και άλλαξε το κείμενο μέσα στα εισαγωγικά με το όνομά σου, π.χ. Text("Γεια σου, Γιώργο! Αυτή είναι η πρώτη μου εφαρμογή"), και μετά πάτα Ctrl+R (Cmd+R σε Mac) για να ξανατρέξεις. Σε λίγα δευτερόλεπτα, ο emulator θα δείξει το όνομά σου.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · MainActivity.kt (άλλαξε αυτή τη γραμμή)</span><span class="dots">···</span>
:::

```
setContent {
    MyFirstAppTheme {
        Surface(modifier = Modifier.fillMaxSize()) {
            // ▼ Άλλαξε εδώ το κείμενο με δικό σου
            Text("Γεια σου Γιώργο! Αυτή είναι η πρώτη μου εφαρμογή")
        }
    }
}
```
:::

Συγχαρητήρια — μόλις ολοκλήρωσες έναν πλήρη κύκλο «αλλαγή κώδικα → build → εγκατάσταση → εκτέλεση». Αυτός ο κύκλος είναι η καθημερινότητα της ανάπτυξης από δω και μπρος. Εκμεταλλεύσου την ορμή και δοκίμασε να αλλάξεις κάτι ακόμα: μεγάλωσε τη γραμματοσειρά, άλλαξε χρώμα — στο επόμενο κεφάλαιο θα δούμε από πού προέρχονται αυτά τα «μαγικά».

#### 6. Πρώτες βοήθειες σε συχνά σφάλματα: το «τμήμα επειγόντων» των δύο πρώτων εβδομάδων

Στο στήσιμο του περιβάλλοντος και στο πρώτο build, πολύ πιθανόν να συναντήσεις τα τρία παρακάτω σφάλματα. Ήσυχα — όλα έχουν αντίδοτο:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Σφάλμα</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Συνηθισμένη αιτία</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Αντίδοτο</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gradle sync failed / αργή λήψη εξαρτήσεων</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Η πρόσβαση στα repositories δεν πάει καλά από το δίκτυο</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ρύθμισε στο Gradle τοπικά mirror repositories (maven mirrors, π.χ. της Alibaba Cloud/Tencent Cloud)· ψάξε στο internet «gradle mirror» και άλλαξε όπως δείχνουν οι οδηγίες</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Λείπουν στοιχεία SDK</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Παράλειψες τη λήψη του SDK κατά την εγκατάσταση</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Settings → SDK Manager: πρόσθεσε τις πλατφόρμες και τα εργαλεία που λείπουν</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ο emulator δεν ξεκινά / μαύρη οθόνη</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Δεν είναι ενεργή η virtualization· το image έχει καταστραφεί</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ενεργοποίησε το VT-x/AMD-V στο BIOS· διέγραψε τον emulator και ξαναφτιάξ' τον· ή πήγαινε απευθείας σε debugging με πραγματική συσκευή</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Πίνακας πρώτων βοηθειών για σφάλματα περιβάλλοντος αρχάριου

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Συμβουλή: η μεθοδολογία της αναζήτησης σφαλμάτων

{class="mt-1"}
Η πρώτη γραμμή του μηνύματος σφάλματος είναι η πιο πολύτιμη — αντιγράψ' την όπως ακριβώς είναι σε μια μηχανή αναζήτησης και πρόσθεσε τη λέξη-κλειδί «android studio». Μη ψάχνεις γενικότητες όπως «δεν μπορώ να στήσω το περιβάλλον, τι κάνω;», αλλά συγκεκριμένα σφάλματα όπως «Gradle sync failed: Could not resolve com.android.tools.build». Μόνο σε ακριβείς ερωτήσεις έρχονται ακριβείς απαντήσεις.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Σειρά σου: ολοκλήρωσε τη «λίστα τελετουργίας» της ανάπτυξης

{class="mt-1"}
① Εγκατέστησε το Android Studio και έβαλε τον emulator σε λειτουργία· ② Τρέξε την εφαρμογή σου μια φορά σε πραγματική συσκευή και κράτα screenshot ως αναμνηστικό· ③ Άλλαξε το κείμενο Hello με το όνομά σου· ④ Συμπίεσε το project και κράτα αντίγραφο ασφαλείας. Αφού τελειώσεις και τα τέσσερα, μπορείς να ανακοινώσεις στους φίλους σου: «κι εγώ είμαι πια Android developer» (με screenshot ως απόδειξη).
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Σύνοψη κεφαλαίου

- Android Studio = το επίσημο δωρεάν IDE· προτείνονται 16GB RAM + 20GB δίσκος + ενεργοποιημένη virtualization
- Τρία βασικά στη δημιουργία project: όνομα, package name (παγκοσμίως μοναδικό, όχι com.example για δημοσίευση), ελάχιστο SDK (από API 26)
- Δύο τρόποι εκτέλεσης: emulator (εικονικό τηλέφωνο μέσα στον υπολογιστή) και πραγματική συσκευή (άνοιξε USB debugging, και θυμήσου να το κλείνεις)
- Ο κανόνας του project: πείραξε μόνο τον φάκελο app/ — το MainActivity.kt είναι η πόρτα, το Manifest το μητρώο, το res/ η αποθήκη πόρων
- Καθημερινή ανάπτυξη = αλλαγή κώδικα → Run → βλέπεις το αποτέλεσμα, και πάλι από την αρχή
:::
