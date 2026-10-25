---
id: di-liu-shi-qi-zhang
num: 67
part: ios-kai-fa-pian
nav: Κεφάλαιο 67: Φινίρισμα και δημοσίευση — ανέβασε την εφαρμογή στο App Store
toc: default
kind: chapter
---

### Κεφάλαιο 67: Γυάλισμα και κυκλοφορία — δοκιμές, debugging και ανέβασμα στο App Store

{class="chapter-intro mb-4"}
Έφτιαξες την εφαρμογή — και μετά; Σε αυτό το κεφάλαιο απαντιούνται τα τρία ζητήματα της πορείας «από το να τρέχει» στο «να το παραδίδεις»: πώς κάνεις αποδοτικό debugging για να βρίσκεις bugs, πώς γράφεις δοκιμές για να μην επιστρέφουν παλιές βλάβες, και πώς ανεβάζεις την εφαρμογή στο App Store για να τη κατεβάζει όλος ο κόσμος. Το ανέβασμα δεν είναι απλώς τελετουργικό — είναι το ορόσημο που μετατρέπει ένα έργο σε προϊόν.

#### 1. Τα τρία βασικά εργαλεία debugging: print, breakpoints, preview

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Εργαλείο</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Τι κάνει</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Πώς το χρησιμοποιείς</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">print + κονσόλα</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Εμφάνιση logs εκτέλεσης</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Στον κώδικα γράφεις print("τιμή=\(x)") και βλέπεις το αποτέλεσμα στην κονσόλα κάτω στο Xcode</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Debugging με breakpoints</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Σταματάς το πρόγραμμα σε μια γραμμή και βλέπεις τις τιμές των μεταβλητών</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ένα κλικ δίπλα στον αριθμό γραμμής βάζει μπλε σημάδι· η εκτέλεση σταματά εκεί όταν φτάσει, και προχωράς βήμα-βήμα</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Προεπισκόπηση SwiftUI + debugger</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Βλέπεις τη διεπαφή και την ιεραρχία των views σε πραγματικό χρόνο</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Καμβάς #Preview + επιθεωρητής View Hierarchy κατά την εκτέλεση</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Τα τρία βασικά εργαλεία debugging

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Μικρή συμβουλή: Πώς διαβάζεις ένα crash;

{class="mt-1"}
Όταν ένα πρόγραμμα Swift κρασάρει, η κονσόλα τυπώνει «Fatal error» μαζί με την αιτία, και το Xcode σταματά στη γραμμή του σφάλματος και τη τονίζει. Τα ιστορικά crashes σε πραγματική συσκευή μπορείς να τα δεις στο Xcode → Window → Organizer → Crashes (θέλει πληρωμένο λογαριασμό). Στην αναζήτηση βάλε προτεραιότητα στο «πρώτη φράση της αιτίας του σφάλματος + swiftui» — μόνο ακριβής ερώτηση δίνει ακριβή απάντηση.
:::

#### 2. Δοκιμές: ασφάλεια για τον κώδικά σου

Οι χειροκίνητες δοκιμές δεν αξίζουν πολλή εμπιστοσύνη — αλλάζεις αυτή τη λειτουργία και μια άλλη χαλάει διακριτικά. Οι δοκιμές είναι «φάρμακο της μεταμέλειας» και ταυτόχρονα «αλεξίσφαιρο γιλέκο». Το iOS χρησιμοποιεί το framework XCTest, με τα εξής είδη:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Επίπεδο</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Τι δοκιμάζει</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Target</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ταχύτητα</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Δοκιμή μονάδας (unit test)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Καθαρή λογική (υπολογισμοί, έλεγχοι)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstAppTests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Δευτερόλεπτα</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Δοκιμή UI (UI test)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Πραγματική συμπεριφορά της διεπαφής</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstAppUITests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Λεπτά</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Χειροκίνητη δοκιμή</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Αίσθηση και εμπειρία από πραγματικό άνθρωπο</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">——</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Χρειάζεται πάντα</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Επίπεδα δοκιμών στο iOS (το template του έργου περιλαμβάνει ήδη δύο Test Target)

::: div .code-block
:::inline div .code-head
<span>SWIFT · Παράδειγμα unit test</span><span class="dots">···</span>
:::

```
import XCTest

// Διαχωρίζουμε τη λογική "μετατροπή κειμένου ποσού σε αριθμό" σε καθαρή συνάρτηση
func parseAmount(_ input: String) -> Double? {
    guard let v = Double(input.trimmingCharacters(in: .whitespaces)),
          v > 0 else { return nil }
    return v
}

final class AmountTests: XCTestCase {
    func testEmptyInputReturnsNil() {
        XCTAssertNil(parseAmount(""))
    }
    func testNegativeReturnsNil() {
        XCTAssertNil(parseAmount("-5"))
    }
    func testNormalValueParses() {
        XCTAssertEqual(parseAmount("12.5"), 12.5)
    }
}
```
:::

Τρέξιμο δοκιμών: ⌘U. Όταν όλα είναι πράσινα, αλλάζεις κώδικα με ησυχία. Οι έλεγχοι ποσών και οι υπολογισμοί συνόλων στο βιβλίο εξόδων πρέπει όλοι να καλύπτονται από unit tests.

#### 3. Υπογραφή και πακετάρισμα: βάλε τη «σφραγίδα» στην εφαρμογή

Κάθε εφαρμογή iOS πρέπει να είναι υπογεγραμμένη για να εγκαθίσταται — αποδεικνύει ότι «το πακέτο προέρχεται από σένα και δεν έχει παραποιηθεί». Η ιεραρχική σχέση:

- Στάδιο μάθησης: δωρεάν Apple ID + αυτόματη υπογραφή στο Xcode (Personal Team), τρέχει σε πραγματική συσκευή, με ανανέωση κάθε 7 ημέρες·
- Στάδιο διανομής: πληρωμένος λογαριασμός προγραμματιστή (99 δολάρια/έτος) που εκδίδει πιστοποιητικά και provisioning profiles, για να μπορείς να ανεβάσεις στο κατάστημα και να εγκαθιστάς μακροπρόθεσμα.

Πακετάρισμα: στο μενού του Xcode, Product → Archive (αρχειοθέτηση)· μετά την ολοκλήρωση του build, στο Organizer διάλεξε Distribute App → App Store Connect → ανέβασμα. Η αρχειοθέτηση πρέπει να γίνει με στόχο το Generic iOS Device (όχι τον εξομοιωτή) — βήμα που οι αρχάριοι ξεχνάνε συχνά.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Προσοχή στην παγίδα: Χάθηκε το πιστοποιητικό = σταματάνε οι ενημερώσεις

{class="mt-1"}
Αν χάσεις το πιστοποιητικό υπογραφής και το ιδιωτικό κλειδί, δεν μπορείς πια να στείλεις ενημερώσεις στην παλιά εφαρμογή — οι χρήστες μπορούν να εγκαταστήσουν μόνο «ολοκαίνουργια» εφαρμογή. Κράτα προσεκτικά backup του πιστοποιητικού (εξαγωγή .p12 από το Keychain) και σημείωσε καλά τον κωδικό. Τυχερά, η Apple προσφέρει «αυτόματη υπογραφή» και διαχείριση πιστοποιητικών στο cloud (τσέκαρε στο Xcode το Automatically manage signing), που σου γλιτώνει τις περισσότερες χειροκίνητες παγίδες.
:::

#### 4. Η πλήρης διαδικασία ανεβάσματος στο App Store

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> Εγγραφή λογαριασμού developer</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-invoice mr-1"></i> Προετοιμασία υλικών για το κατάστημα</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-box mr-1"></i> Ανέβασμα πακέτου build</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-clipboard-list mr-1"></i> Συμπλήρωσε στοιχεία ιδιωτικότητας και ελέγχου</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> Έλεγχος Apple (1-7 μέρες)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-party-horn mr-1"></i> Κυκλοφορία</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Εικόνα 5: Έξι βήματα για το App Store
:::

- Εγγραφή: developer.apple.com, προσωπικός λογαριασμός 99 δολάρια/έτος·
- Υλικό: εικονίδιο (1024×1024, χωρίς στρογγυλεμένες γωνίες — η Apple κόβει μόνη της), στιγμιότυπα (για όλα τα μεγέθη iPhone), περιγραφή, σύνδεσμος πολιτικής απορρήτου·
- Ερωτηματολόγιο απορρήτου: δήλωσε ειλικρινά ποια δεδομένα συλλέγεις — η εφαρμογή εξόδων χωρίς σύνδεση internet μπορεί να δηλώσει «δεν συλλέγω κανένα δεδομένο»·
- Έλεγχος (review): η πρώτη υποβολή συχνά περιμένει 1-7 ημέρες· αν απορριφθεί, διόρθωσε σημείο-σημείο σύμφωνα με τις «σημειώσεις του ελέγχου» — οι λόγοι απόρριψης της Apple συνήθως είναι γραμμένοι πολύ συγκεκριμένα, απλώς ακολούθησέ τους·
- TestFlight: πριν την κυκλοφορία, στείλε τη δοκιμαστική έκδοση σε φίλους για εσωτερική δοκιμή (έως 10.000 άτομα), μάζεψε έναν γύρο σχόλια και μετά κάνε την επίσημη υποβολή — απόλυτα επαγγελματική εικόνα.

#### 5. Πώς φτιάχνεις το υλικό του καταστήματος: η πρώτη εντύπωση είναι οι λήψεις

Η σελίδα του καταστήματος είναι η βιτρίνα που βλέπει ο χρήστης «όταν κάνει βόλτα στο κατάστημα». Τρία στοιχεία καθορίζουν την πρώτη εντύπωση:

- Εικονίδιο: 1024×1024, μην «συμβιβαστείς» με ένα στιγμιότυπο. Αν δεν έχεις σχεδιαστικές δεξιότητες, φτιάξε με εργαλείο AI ένα απλό, καθαρό σχήμα — είναι αποδεκτό μόνο αν το αναγνωρίζεις με μια ματιά ακόμα και συρρικνωμένο στην αρχική οθόνη·
- Στιγμιότυπα: τουλάχιστον 2 σετ (στις βασικές αναλύσεις iPhone), που δείχνουν τις πιο βασικές λειτουργίες· σε κάθε ένα πρόσθεσε μια φράση απλή, ανθρώπινη («Καταγραφή εξόδου σε ένα δευτερόλεπτο» είναι δέκα φορές καλύτερη από «Αποδοτική λύση λογιστικής»)·
- Περιγραφή: η πρώτη φράση να λέει καθαρά «τι είναι + σε ποιον απευθύνεται»· μην στοιβάζεις «το πιο επαγγελματικό, το πιο δυνατό» — η ειλικρίνεια αποδίδει περισσότερο από το μεγαλόπνοο.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Φτιάξε το μόνο σου: «παράδωσε» την εφαρμογή εξόδων μια φορά

#### 6. Αναφορές crash και μικρή λίστα βελτιστοποίησης απόδοσης

Πριν ανέβει η εφαρμογή στο κατάστημα, αξίζει μισή ώρα για καθένα από τα δύο αυτά:

##### 1. Παρακολούθηση crashes

Το ότι δεν κρασάρει στις δικές σου δοκιμές δεν σημαίνει ότι δεν θα κρασάρει στο κινητό του χρήστη. Η Apple παρέχει δωρεάν αναφορές crash στο Xcode Organizer (με πληρωμένο λογαριασμό βλέπεις και τα crash logs από πραγματικές συσκευές)· πιο ανώδυνη λύση είναι να ενσωματώσεις SDK τρίτου (π.χ. Firebase Crashlytics). Κυκλοφορία χωρίς παρακολούθηση crashes ισούται με οδήγηση με κλειστά μάτια.

##### 2. Τέσσερα σημεία αυτοελέγχου απόδοσης

1. Λίστες με LazyVStack / List: μακριές λίστες μην τις στήνεις με απλό VStack — το lazy loading είναι το πρώτο μάθημα απόδοσης·
2. Μην πετάς μέσα πρωτότυπες εικόνες: χρησιμοποίησε AsyncImage (για εικόνες από το internet) και την cache του συστήματος — μια πρωτότυπη εικόνα 5MB αρκεί για να «πνίξει» παλιές συσκευές·
3. Μην κάνεις βαριές δουλειές στο κύριο νήμα (main thread): δίκτυο και μεγάλα αρχεία πάνε όλα με async/await·
4. Μέτρησε με το Instruments: ο αναλυτής απόδοσης που έρχεται με το Xcode (Time Profiler, έλεγχος διαρροών μνήμης) — πρώτα μέτρησε, μετά βελτιστοποίησε, μην δουλεύεις με το ένστικτο.

{class="mt-1"}
① Πρόσθεσε 3 unit tests σε λογική όπως η parseAmount (να τρέχουν πράσινα με ⌘U)· ② με breakpoints πιάσε μόνος σου ένα crash που έφτιαξες εσύ και διόρθωσέ το· ③ με Product → Archive φτιάξε ένα πακέτο και μέσω TestFlight κάλεσε φίλους για εσωτερική δοκιμή· ④ αν έχεις περιθώριο, εγγράψου στο πρόγραμμα προγραμματιστών και ανέβασε πραγματικά το βιβλίο εξόδων στο κατάστημα. Τα τρία πρώτα βήματα μπορούν να τελειώσουν απόψε.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Σύνοψη κεφαλαίου

- Τρία εργαλεία debugging: logs με print, breakpoints, προεπισκόπηση SwiftUI και επιθεωρητής views
- XCTest: unit tests (⌘U) + UI tests + χειροκίνητες δοκιμές — το template τα έχει ήδη έτοιμα
- Υπογραφή: δωρεάν λογαριασμός με αυτόματη υπογραφή (ανανέωση κάθε 7 ημέρες)· μόνο πληρωμένος λογαριασμός μπορεί να διανείμει
- Πακετάρισμα: Generic iOS Device + Archive + Distribute· οπωσδήποτε κράτα backup των πιστοποιητικών
- Έξι βήματα κυκλοφορίας: εγγραφή → υλικό → ανέβασμα → ερωτηματολόγιο απορρήτου → έλεγχος → στο ράφι· πρώτα εσωτερική δοκιμή με TestFlight
:::
