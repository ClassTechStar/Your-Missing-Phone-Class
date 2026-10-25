---
id: di-liu-shi-wu-zhang
num: 65
part: ios-kai-fa-pian
nav: Κεφάλαιο 65: Έργο 1 — Το βιβλίο εξόδων μου (τοπική έκδοση)
toc: default
kind: chapter
---

### Κεφάλαιο 65: Project 1 — Το βιβλίο εξόδων μου (τοπική έκδοση)

{class="chapter-intro mb-4"}
Καλωσόρισες στο πρώτο σου «αληθινό project». Αν και δεν συνδέεται στο internet, αυτό το βιβλίο εξόδων έχει τα πάντα: καταγράφει μια συναλλαγή, δείχνει την κίνηση, κάνει μηνιαία στατιστικά, και διαγράφει/αλλάζει. Αφού το τελειώσεις, θα έχεις περάσει ολόκληρη τη ροή «δεδομένα > λογική > διεπαφή». Μην βιάζεσαι να αντιγράψεις κώδικα — σκέψου πρώτα καθαρά και μετά δρα, αυτή είναι η σταθερή μας αρχή.

#### Α. Σκέψη απαιτήσεων: ρώτα πρώτα πέντε ερωτήσεις

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Στοιχείο</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Απάντηση</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who (σε ποιον)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Για εσένα· κανό και για οικογένεια/φίλους</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What (τι κάνει)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Καταγραφή εσόδων-εξόδων, εμφάνιση κίνησης, μηνιαίες συνοψίσεις, στατιστικά ανά κατηγορία</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why (γιατί)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Εξάσκηση + να βγάλεις άκρη πού πάνε τα λεφτά σου</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How (πώς)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift + SwiftUI + SwiftData + MVVM, καθαρά τοπικά, χωρίς backend</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint (περιορισμοί)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ολοκλήρωση μέσα σε μια εβδομάδα· ελάχιστη υποστήριξη iOS 17 (το εμπόδιο του SwiftData)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Τα πέντε στοιχεία απαιτήσεων του βιβλίου εξόδων

Κατόπιν χώρισέ το σε μικρά βήματα «κάθε βήμα χρήσιμο»: ① στήσιμο της στρώσης δεδομένων SwiftData (να αποθηκεύει μια συναλλαγή)· ② σελίδα λίστας (να βλέπεις την κίνηση)· ③ αναδυόμενο παράθυρο καταχώρισης (να προσθέτεις συναλλαγή)· ④ διαγραφή και επεξεργασία· ⑤ κάρτα μηνιαίας σύνοψης. Με κάθε ολοκληρωμένο βήμα, η εφαρμογή είναι ένα «χρήσιμο πράγμα».

#### Β. Στρώση δεδομένων: δώσε στη «συναλλαγή» ένα σπίτι

Πρώτα όρισε πώς μοιάζει μια συναλλαγή — τα πεδία να φτάνουν, χωρίς υπερβολές:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Record.swift (μοντέλο)</span><span class="dots">···</span>
:::

```
import SwiftData

@Model
class Record {
    var type: String      // "income" έσοδο | "expense" έξοδο
    var amount: Double    // Ποσό (γιουάν)
    var category: String  // Κατηγορία: φαγητό, μετακινήσεις, μισθός……
    var note: String      // Σημείωση (προαιρετικό)
    var date: Date        // Ημερομηνία καταχώρισης

    init(type: String, amount: Double, category: String, note: String = "", date: Date = Date()) {
        self.type = type
        self.amount = amount
        self.category = category
        self.note = note
        self.date = date
    }
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Συμβουλή: γιατί το ποσό σε Double;

{class="mt-1"}
Οι αυστηρές οικονομικές εφαρμογές χρησιμοποιούν Decimal (ακριβής δεκαδική αρίθμηση) για να αποφύγουν σφάλματα κινητής υποδιαστολής (το παλιό πρόβλημα 0.1+0.2≠0.3). Για project εξάσκησης, το Double αρκεί· αν κάποτε φτιάξεις αληθινό οικονομικό προϊόν, θυμήσου να το αλλάξεις σε Decimal ή «Int σε cents» — αυτή είναι η παγίδα που πατούσαν αμέτρητοι προκάτοχοι.
:::

#### Γ. MVVM: η διεπαφή και η λογική «χωρίζουν δρόμο»

Να αφήνεις τη διεπαφή να χειρίζεται απευθείας τη βάση; Θα τρέχει, αλλά ο κώδικας διεπαφής θα γίνεται δύσχρηστος και μακροσκελής. Η αρχιτεκτονική MVVM μοιράζει καθήκοντα: το View (διεπαφή) μόνο ζωγραφίζει, το ViewModel (κέντρο λογικής) διαχειρίζεται δεδομένα, και το Model (SwiftData) αναλαμβάνει την αποθήκευση.

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> View (οθόνη SwiftUI)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> ViewModel (κέντρο λογικής @Observable)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-database mr-1"></i> Model (στρώμα δεδομένων SwiftData)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Εικόνα 4: Τα τρία επίπεδα του MVVM — τα δεδομένα ρέουν προς μία κατεύθυνση, και τα επίπεδα δεν παραβιάζουν τα όριά τους
:::

::: div .code-block
:::inline div .code-head
<span>SWIFT · RecordViewModel.swift (σκελετός)</span><span class="dots">···</span>
:::

```
import Observation

@Observable
class RecordViewModel {
    var records: [Record] = []
    private let context: ModelContext

    init(context: ModelContext) { self.context = context }

    func load() {
        // Φιλτράρισμα + ταξινόμηση με #Predicate του SwiftData
        let descriptor = FetchDescriptor<Record>(
            sortBy: [SortDescriptor(\.date, order: .reverse)]
        )
        records = (try? context.fetch(descriptor)) ?? []
    }

    func add(type: String, amount: Double, category: String, note: String) {
        let r = Record(type: type, amount: amount, category: category, note: note)
        context.insert(r)
        try? context.save()
        load()                       // Επαναφόρτωση, η οθόνη ανανεώνεται
    }

    func delete(_ record: Record) {
        context.delete(record)
        try? context.save()
        load()
    }
}
```
:::

Στη διεπαφή γράφεις @State private var vm = RecordViewModel(...), και ύστερα απεικονίζεις τη λίστα απευθείας με vm.records — μόλις αλλάξουν τα δεδομένα, η διεπαφή ανανεώνεται από μόνη της.

#### Δ. Διεπαφή: σελίδα λίστας + παράθυρο καταχώρισης

::: div .code-block
:::inline div .code-head
<span>SWIFT · Σελίδα λίστας λογιστηρίου (κομμάτι-κλειδί)</span><span class="dots">···</span>
:::

```
struct RecordListView: View {
    @State private var vm: RecordViewModel
    @State private var showAdd = false

    var body: some View {
        NavigationStack {
            List {
                Section("Υπόλοιπο μήνα") {          // κάρτα σύνοψης
                    SummaryRow(records: vm.records)
                }
                Section("Κινήσεις") {
                    ForEach(vm.records) { r in
                        RecordRow(record: r)
                    }
                    .onDelete { idx in
                        idx.forEach { vm.delete(vm.records[$0]) }
                    }
                }
            }
            .navigationTitle("Το λογιστηρίο μου")
            .toolbar {
                Button { showAdd = true } label: {
                    Image(systemName: "plus")
                }
            }
            .sheet(isPresented: $showAdd) {
                AddRecordView(vm: vm)          // διάλογος εισαγωγής
            }
        }
    }
}
```
:::

Βασικά σημεία του παραθύρου καταχώρισης: το πληκτρολόγιο του πεδίου ποσού με .keyboardType(.decimalPad) (αριθμητικό πληκτρολόγιο), έσοδα/έξοδα με τμηματικό έλεγχο (Picker), κατηγορία με επιλογή μενού, και στο πάτημα του «Αποθήκευση» καλείς vm.add(...) και dismiss() για να κλείσει το παράθυρο.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Προσοχή: μην τεμπελιάζεις με τον έλεγχο εισαγωγής

{class="mt-1"}
Το πεδίο ποσού πρέπει οπωσδήποτε να ελέγχεται: κενές τιμές, αρνητικοί αριθμοί, παράνομες εισαγωγές σαν «abc» — όλα να μπλοκάρονται (έλεγξε με Double(text), που επιστρέφει nil σε αποτυχία). Μια από τις πιο συχνές αιτίες crash των εφαρμογών είναι το «να μεταχειρίζεσαι την εισαγωγή του χρήστη σαν φρόνιμο παιδί». Θυμήσου: ό, τι πληκτρολογεί ο χρήστης, έλεγξέ το σαν εχθρό.
:::

#### Ε. Επεξεργασία, διαγραφή και σύνοψη

- Διαγραφή: το .onDelete της List με ολίσθηση αριστερά + παράθυρο επιβεβαίωσης (η κατά λάθος διαγραφή είναι ό, τι πιο μισημένο για τους χρήστες εφαρμογών εξόδων)·
- Επεξεργασία: πάτα στη γραμμή για να ανοίξεις παράθυρο επεξεργασίας, με προσυμπληρωμένες τις αρχικές τιμές (να αλλάξεις ένα γράμμα είναι πιο εύκολο από το να ξαναγράψεις όλα)·
- Σύνοψη: υπολόγισε «έσοδα / έξοδα / υπόλοιπο του μήνα» με filter + reduce, και εμφάνισέ το σε κάρτα στην κορυφή:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Υπολογισμός μηνιαίας σύνοψης</span><span class="dots">···</span>
:::

```
func monthSummary(_ records: [Record]) -> (income: Double, expense: Double) {
    let cal = Calendar.current
    let monthRecords = records.filter {
        cal.isDate($0.date, equalTo: Date(), toGranularity: .month)
    }
    let income = monthRecords
        .filter { $0.type == "income" }
        .reduce(0) { $0 + $1.amount }
    let expense = monthRecords
        .filter { $0.type == "expense" }
        .reduce(0) { $0 + $1.amount }
    return (income, expense)
}
```
:::

#### ΣΤ. Παραλαβή: έλεγχος σε τρία επίπεδα + δύο προχωρημένες προκλήσεις

Μετά την ολοκλήρωση του project, έλεγξε σε τρία επίπεδα «λειτουργία > όρια > αρχιτεκτονική»: καταγράφει; διαγράφει; τα δεδομένα μένουν μετά την επανεκκίνηση (λειτουργία)· με ποσό 0 ή αρνητικό κρασάρει; (όρια)· διεπαφή και δεδομένα ανακατεμένα; πεδία σκληρά κωδικοποιημένα; (αρχιτεκτονική).

Αφού περάσει η παραλαβή της βασικής έκδοσης, δώσε στον εαυτό σου δύο «προχωρημένα πιάτα»:

1. Στατιστικά ανά κατηγορία: πρόσθεσε καρτέλα «Στατιστικά», και με το Swift Charts ζωγράφισε τις δαπάνες ανά κατηγορία σε πίτα/ράβδους — η επίσημη βιβλιοθήκη γραφημάτων της Apple, με λίγες γραμμές κώδικα βγαίνει διάγραμμα·
2. Συγχρονισμός iCloud: Στο SwiftData, η ενεργοποίηση του iCloud sync θέλει μόνο λίγες ρυθμίσεις — η εφαρμογή εξόδων συγχρονίζεται αυτόματα ανάμεσα σε iPhone/iPad, και ξαφνικά όλα αποκτούν «επαγγελματική» αίσθηση.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Φτιάξε το μόνο σου: ολοκλήρωσέ το αυτή την εβδομάδα

{class="mt-1"}
Δούλεψε με αυτή τη σειρά: «στρώμα δεδομένων → ViewModel → σελίδα λίστας → παράθυρο καταχώρησης → κάρτα σύνοψης», ένα βήμα την ημέρα. Αν κολλήσεις, ρίξε το μήνυμα σφάλματος αυτούσιο σε μηχανή αναζήτησης ή σε AI (θυμάσαι το έβδομο μέρος, «Πρακτικός Προγραμματισμός με AI»; Όταν περιγράφεις ένα πρόβλημα, ξεκαθάρισε «τι περίμενες να γίνει, τι έγινε στην πραγματικότητα και τα βήματα αναπαραγωγής»). Όταν τελειώσεις, χρησιμοποίησέ το για μια εβδομάδα καταγράφοντας τα έξοδά σου — όταν χρησιμοποιείς μια εφαρμογή που έφτιαξες ο ίδιος, η ικανοποίηση σε σπρώχνει να συνεχίσεις.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Σύνοψη κεφαλαίου

- Τα πέντε στοιχεία των απαιτήσεων → διάσπαση σε μικρά βήματα «κάθε βήμα να δουλεύει» και μετά πιάσε δουλειά
- Στρώμα δεδομένων: μοντέλο @Model + κοντέινερ modelContainer + ερώτημα FetchDescriptor
- Κατανομή ρόλων MVVM: το View μόνο σχεδιάζει, το ViewModel με @Observable κρατά τη λογική, το SwiftData κρατά την αποθήκευση
- Διεπαφή: List + Section + toolbar + sheet ως παράθυρο καταχώρησης
- Έλεγχος σε τρία επίπεδα (λειτουργικότητα/οριακές περιπτώσεις/αρχιτεκτονική) + προχωρημένες προκλήσεις (Swift Charts, συγχρονισμός iCloud)
:::
