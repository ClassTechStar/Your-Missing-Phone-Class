---
id: di-liu-shi-si-zhang
num: 64
part: ios-kai-fa-pian
nav: Κεφάλαιο 64: Αποθήκευση δεδομένων και αιτήματα δικτύου
toc: default
kind: chapter
---

### Κεφάλαιο 64: Αποθήκευση δεδομένων και κλήσεις δικτύου

{class="chapter-intro mb-4"}
Μια εφαρμογή που μόνο «κοιτάζει» είναι νεκρή· εφαρμογή που αποθηκεύει δεδομένα και συνδέεται στο internet είναι ζωντανή. Σε αυτό το κεφάλαιο γνωρίζεις το «τρίο» της στρώσης δεδομένων iOS: UserDefaults (μικρές ρυθμίσεις), SwiftData (δομημένα δεδομένα), URLSession (επικοινωνία με τον διακομιστή), μαζί με το Codable για ανάλυση JSON και το μοντέρνο async/await. Μετά το κεφάλαιο αυτό, θα μπορείς να γράφεις πραγματικές εφαρμογές που θυμούνται τις συνήθειες του χρήστη και ανανεώνουν περιεχόμενο σε πραγματικό χρόνο.

#### Α. Πώς διαλέγεις λύση αποθήκευσης: δες πρώτα τον πίνακα

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Λύση</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Τι αποθηκεύει καλύτερα</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Χαρακτηριστικά</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Πού χρησιμοποιείται στο βιβλίο</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UserDefaults</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Σκόρπιες μικρο-ρυθμίσεις (διακόπτες, προτιμήσεις)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ζεύγη κλειδί-τιμής, απλό και ευθύ</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Οι ρυθμίσεις στο Κεφ. 65, οι αγαπημένες πόλεις στο Κεφ. 66</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftData</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Δομημένα δεδομένα (συναλλαγές, καταγραφές)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Επίσημο wrapper βάσης δεδομένων· δήλωση με μία γραμμή @Model</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Οι καταγραφές συναλλαγών στο Κεφ. 65</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">URLSession</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">(δεν αποθηκεύει, τα παίρνεις online) Δεδομένα διακομιστή</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ενσωματωμένο στο σύστημα framework δικτύου, χωρίς εξαρτήσεις από τρίτους</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Τα δεδομένα καιρού στο Κεφ. 66</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Ο ρόλος του τρίο των δεδομένων

Κράτα ένα μνημόνιο: «μικρές ρυθμίσεις στο UserDefaults, μαζικά δεδομένα στο SwiftData, τα δεδομένα απ' έξω περνούν από το URLSession». Το Core Data των παλιών οδηγών εξακολουθεί να δουλεύει (το SwiftData είναι η μοντέρνα εκδοχή του), ενώ το χειρόγραφο SQLite σχεδόν δεν το αγγίζεις — μάθε απευθείας το νέο, μην πας παλιό δρόμο.

#### Β. UserDefaults: αποθηκεύεις μικρές ρυθμίσεις

::: div .code-block
:::inline div .code-head
<span>SWIFT · Παράδειγμα UserDefaults</span><span class="dots">···</span>
:::

```
// Γράψιμο: αποθήκευση τιμής
UserDefaults.standard.set(true, forKey: "isDarkMode")
UserDefaults.standard.set("Πεκίνο ", forKey: "favoriteCity")

// Διάβασμα: ανάκτηση (χωρίς τιμή, επιστρέφεται η προεπιλογή)
let isDark = UserDefaults.standard.bool(forKey: "isDarkMode")
let city = UserDefaults.standard.string(forKey: "favoriteCity") ?? "Πεκίνο"

// Διαγραφή: αφαίρεση κλειδιού
UserDefaults.standard.removeObject(forKey: "isDarkMode")
```
:::

Πρόσεξε ότι ταιριάζει μόνο για σκόρπιες μικρο-ρυθμίσεις — για δεκάδες ή εκατοντάδες εγγραφές άσε το στο SwiftData, και μην χρησιμοποιείς το UserDefaults σαν βάση δεδομένων (καθυστερεί την εκκίνηση και δεν ευννοεί αναζητήσεις).

#### Γ. SwiftData: δώσε στα δεδομένα «σπίτι αληθινό»

Το SwiftData είναι η επίσημη λύση βάσης δεδομένων από το iOS 17, και έχει απλοποιήσει στο έπακρο τη «δημιουργία πινάκων και τις προσθήκες/διαγραφές/αλλαγές/αναζητήσεις» — με ένα annotation @Model, η κλάση δεδομένων γίνεται πίνακας βάσης:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Παράδειγμα SwiftData</span><span class="dots">···</span>
:::

```
import SwiftData

// 1. @Model: η κλάση γίνεται αυτόματα "πίνακας"
@Model
class Record {
    var amount: Double
    var category: String
    var note: String
    var date: Date

    init(amount: Double, category: String, note: String, date: Date) {
        self.amount = amount
        self.category = category
        self.note = note
        self.date = date
    }
}

// 2. Σύνδεση container στην είσοδο της εφαρμογής
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .modelContainer(for: Record.self)   // η βάση είναι έτοιμη
    }
}

// 3. Στο view ανάγνωση με @Query, εγγραφή με @Environment
struct RecordListView: View {
    @Query(sort: \Record.date, order: .reverse) var records: [Record]
    @Environment(\.modelContext) private var context

    var body: some View {
        List(records) { r in
            Text("\(r.category) \(r.amount) γιουάν")
        }
    }

    func add(amount: Double, category: String) {
        let r = Record(amount: amount, category: category, note: "", date: Date())
        context.insert(r)     // αποθήκευση
        try? context.save()   // εγγραφή στον δίσκο
    }
}
```
:::

Αυτό το template «@Model + modelContainer + @Query» μπορείς να το μεταφέρεις αυτούσιο σε όποιο project θέλεις — απλά άλλαξε τα ονόματα των πεδίων. Μόλις αλλάξουν τα δεδομένα, το @Query ανανεώνει αυτόματα τη διεπαφή — μαγικό.

#### Δ. Codable: «μεταφράζεις» το JSON

Τα δεδομένα του διακομιστή είναι ως επί το πλείστον κείμενο JSON. Το protocol Codable της Swift κάνει τη μετατροπή «JSON ⇄ struct» να γίνεται αυτόματα — αν τα ονόματα των πεδίων ταιριάζουν, η μαγεία δουλεύει:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Ανάλυση JSON με Codable</span><span class="dots">···</span>
:::

```
// JSON: {"name":"Πεκίνο","main":{"temp":26.5},"weather":[{"description":"Αίθριο"}]}
struct WeatherResponse: Codable {
    let name: String
    let main: Main
    let weather: [Weather]
}
struct Main: Codable { let temp: Double }
struct Weather: Codable { let description: String }

// Αλφαριθμητικό JSON → struct
let decoder = JSONDecoder()
let data = jsonString.data(using: .utf8)!
let result = try decoder.decode(WeatherResponse.self, from: data)
print(result.weather[0].description)   // "Αίθριο"
```
:::

Σιδερένιος κανόνας: πρώτα κοιτά το πραγματικό JSON που επιστρέφεται, μετά όρισε τα πεδία. Πολλά bugs «αποτυχίας ανάλυσης» οφείλονται σε λάθος όνομα πεδίου ή λάθος τύπο (ο διακομιστής στέλνει «26.5» σαν συμβολοσειρά, εσύ το δήλωσες Double) — τύπωσε το αρχικό JSON και σύγκρινε, και θα το εντοπίσεις σε δέκα δευτερόλεπτα.

#### Ε. URLSession + async/await: μιλάς με τον διακομιστή

Στο iOS η σύνδεση στο internet γίνεται με το ενσωματωμένο URLSession, σε συνδυασμό με το async/await (ασύγχρονες συναρτήσεις) της Swift — το «περιμένεις το internet» είναι τόσο φυσικό όσο το «περιμένεις το courier»:

::: div .code-block
:::inline div .code-head
<span>SWIFT · URLSession + async/await</span><span class="dots">···</span>
:::

```
struct WeatherService {
    // Ασύγχρονη συνάρτηση: async σημαίνει "πρέπει να περιμένω λίγο", throws σημαίνει "μπορεί να αποτύχει"
    func fetchWeather(city: String) async throws -> WeatherResponse {
        let url = URL(string:
            "https://api.example.com/weather?city=\(city)")!
        let (data, _) = try await URLSession.shared.data(from: url)
        return try JSONDecoder().decode(WeatherResponse.self, from: data)
    }
}

// Σημείο κλήσης (μέσα σε .task):
.task {
    do {
        let weather = try await service.fetchWeather(city: "Πεκίνο")
        // Ενημέρωση οθόνης……
    } catch {
        print("Σφάλμα: \(error)")
    }
}
```
:::

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Υπενθύμιση αποφυγής παγίδων: δύο σιδερένιοι κανόνες δικτύου

{class="mt-1"}
① Οι κλήσεις δικτύου γίνονται πάντα με async/await, ποτέ δεν μπλοκάρεις το κύριο νήμα — η κλειδωμένη διεπαφή είναι εμπειρία επιπέδου crash. Η δομημένη ταυτόχρονη εκτέλεση της Swift το κάνει φυσικό, αλλά μην ξεχνάς το try await και το do/catch. ② Το ATS απαγορεύει από προεπιλογή το HTTP σε καθαρό κείμενο: το iOS θέλει HTTPS. Για δοκιμή τοπικού http:// service χρειάζεται προσωρινή εξαίρεση στο Info.plist (NSAppTransportSecurity), αλλά το τελικό προϊόν πρέπει να περνάει εξ ολοκλήρου από HTTPS — και η έγκριση το προσέχει.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Ας το δοκιμάσουμε: φτιάξε μια μικρή εφαρμογή «φράση της ημέρας»

#### ΣΤ. Τα σφάλματα δικτύου θέλουν «βαθμίδες»: μην πετάς όλα τα λάθη στον χρήστη

Χωρίς internet, λήξη χρόνου, 404, 500 διακομιστή... σε διαφορετικό λάθος, ο χρήστης πρέπει να δει διαφορετικό μήνυμα:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Διαχείριση σφαλμάτων σε επίπεδα</span><span class="dots">···</span>
:::

```
func friendlyMessage(_ error: Error) -> String {
    if let urlError = error as? URLError {
        switch urlError.code {
        case .notConnectedToInternet: return "Έπεσε η σύνδεση, να τη ελέγξεις;"
        case .timedOut:               return "Το αίτημα έληξε, δοκιμή αργότερα;"
        case .cannotFindHost:         return "Ο server δεν βρέθηκε"
        default:                      return "Πρόβλημα δικτύου: \(urlError.code)"
        }
    }
    if let d = error as? DecodingError {
        return "Λάθος μορφή δεδομένων (ίσως άλλαξε το API)"
    }
    return "Σφάλμα: \(error.localizedDescription)"
}
```
:::

Δείξε στον χρήστη «ανθρώπινη γλώσσα», και στο log άσε το «πρωτότυπο κείμενο» (print το πλήρες error). Μην πετάς στον χρήστη το αγγλικό μυστήριο του error.localizedDescription — η αίσθηση του προϊόντος κρύβεται σε αυτές τις λεπτομέρειες.

{class="mt-1"}
Βρες ένα δωρεάν API φράσεων (π.χ. hitokoto ή παρόμοιο), και με URLSession + async/await φέρνε τη «φράση της ημέρας» και εμφάνισέ τη στο κέντρο της οθόνης, προσθέτοντας ένα κουμπί «Άλλαξε φράση». Κατόπιν αποθήκευσε τις αγαπημένες φράσεις σε «Αγαπημένα» με SwiftData. Αυτή η άσκηση χρησιμοποιεί όλα τα UserDefaults/SwiftData/Codable/URLSession — αφού την τελειώσεις, τα Κεφάλαια 7 και 8 θα σου φανούν παιχνίδι.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Σύνοψη κεφαλαίου

- Μνημόνιο: μικρές ρυθμίσεις στο UserDefaults, μαζικά δεδομένα στο SwiftData, τα εξωτερικά δεδομένα περνούν από το URLSession
- Τα τρία «χτυπήματα» του SwiftData: @Model δηλώνει τον πίνακα, modelContainer κρεμά το container, @Query διαβάζει + context.insert γράφει
- Το Codable «μεταφράζει» αυτόματα το JSON: αν τα πεδία ταιριάζουν, η μαγεία δουλεύει
- URLSession + async/await: το internet σαν να περιμένεις courier· το do/catch διαχειρίζεται τις αποτυχίες
- Δύο σιδερένιοι κανόνες: μην μπλοκάρεις το κύριο νήμα· το τελικό προϊόν πρέπει να είναι HTTPS (ATS)
:::
