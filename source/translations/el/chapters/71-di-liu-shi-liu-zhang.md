---
id: di-liu-shi-liu-zhang
num: 66
part: ios-kai-fa-pian
nav: Κεφάλαιο 66: Έργο 2 — Εφαρμογή αναζήτησης καιρού (δικτυακή έκδοση)
toc: default
kind: chapter
---

### Κεφάλαιο 66: Έργο 2 — Εφαρμογή αναζήτησης καιρού (δικτυακή έκδοση)

{class="chapter-intro mb-4"}
Αν το βιβλίο εξόδων ήταν εξάσκηση «μέσα», η εφαρμογή καιρού είναι η πρώτη σου επαφή με τον «έξω κόσμο» — πρέπει να συνεργάζεται με το internet. Σε αυτό το έργο θα μάθεις: πώς να αποκτάς δωρεάν API, πώς να αναλύεις JSON, πώς να διαχειρίζεσαι τις τρεις καταστάσεις της οθόνης («φόρτωση/επιτυχία/αποτυχία») και πώς να κρύβεις καλά το κλειδί του API. Όταν το ολοκληρώσεις, θα έχεις αποκτήσει τη δύναμη να φτιάχνεις οποιαδήποτε «συνδεδεμένη εφαρμογή» — ειδήσεις, συναλλαγματικές ισοτιμίες, μετάφραση: η λογική είναι ακριβώς η ίδια.

#### 1. Απόκτηση δωρεάν API καιρού

Για προσωπική εξάσκηση προτείνονται το OpenWeatherMap ή η QWeather (He Feng Tianqi, δημοφιλής στην Κίνα) — και τα δύο έχουν δωρεάν ποσόστωση και είσαι έτοιμος μόλις εγγραφείς. Πάμε με παράδειγμα το OpenWeatherMap:

1. Δημιουργία λογαριασμού → στη σελίδα API keys φτιάξε ένα κλειδί (apikey)·
2. Η δωρεάν έκδοση μπορεί να καλέσει το endpoint Current Weather: api.openweathermap.org/data/2.5/weather? q=beijing&appid=ΤΟ_ΚΛΕΙΔΙ_ΣΟΥ&units=metric·
3. Δοκίμασέ το πρώτα μία φορά στον browser για να δεις πώς μοιάζει το JSON που επιστρέφει — αυτό είναι το υποχρεωτικό «προκαταρκτικό μάθημα» πριν συνδέσεις οποιοδήποτε API.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Προσοχή στην παγίδα: Το κλειδί δεν πρέπει ποτέ να μπαίνει σκληρά στον κώδικα

{class="mt-1"}
Το API Key είναι σαν ο «κωδικός του πορτοφολιού σου»: αν γραφτεί στον κώδικα και ανέβει στο GitHub, μέσα σε λίγες ώρες θα το αρπάξουν crawlers και θα το ξοδέψουν χωρίς εσένα. Ο σωστός τρόπος στο iOS: βάλε το στο Config.xcconfig (αρχείο ρυθμίσεων που το gitignore αγνοεί ήδη) και διάβαζέ το στον κώδικα μέσω του Info.plist. Ψάξε «iOS xcconfig API key» και κάνε τις αλλαγές ακολουθώντας τις οδηγίες.
:::

#### 2. Δικτυακό στρώμα: URLSession + Codable

Πρώτα όρισε τα μοντέλα με βάση το JSON που επιστρέφει το API, και μετά γράψε το service:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Μοντέλο δεδομένων + υπηρεσία</span><span class="dots">···</span>
:::

```
// JSON: {"weather":[{"description":"Αίθριο"}],"main":{"temp":26.5,"humidity":40},"name":"Πεκίνο"}
struct WeatherResponse: Codable {
    let weather: [Weather]
    let main: Main
    let name: String
}
struct Weather: Codable { let description: String }
struct Main: Codable { let temp: Double; let humidity: Int }

struct WeatherService {
    let key: String   // Διαβάζεται από xcconfig

    func fetchWeather(city: String) async throws -> WeatherResponse {
        var comps = URLComponents(string: "https://api.openweathermap.org/data/2.5/weather")!
        comps.queryItems = [
            URLQueryItem(name: "q", value: city),
            URLQueryItem(name: "appid", value: key),
            URLQueryItem(name: "units", value: "metric"),
            URLQueryItem(name: "lang", value: "zh_cn")
        ]
        let (data, _) = try await URLSession.shared.data(from: comps.url!)
        return try JSONDecoder().decode(WeatherResponse.self, from: data)
    }
}
```
:::

#### 3. Τρεις καταστάσεις διεπαφής: φόρτωση / επιτυχία / αποτυχία

Η ψυχή μιας συνδεδεμένης εφαρμογής βρίσκεται στη «διαχείριση καταστάσεων». Αργό δίκτυο, κομμένη σύνδεση, λάθος όνομα πόλης… για κάθε περίπτωση η οθόνη πρέπει να δίνει απάντηση στον χρήστη. Εκφράσέ τες κομψά με enum + switch:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Κατάσταση οθόνης</span><span class="dots">···</span>
:::

```
enum LoadState {
    case loading                  // περιστρέφεται
    case success(WeatherResponse) // επιτυχία
    case error(String)            // αποτυχία
}

@Observable
class WeatherViewModel {
    var state: LoadState = .loading
    private let service = WeatherService(key: Config.apiKey)

    func search(city: String) async {
        state = .loading
        do {
            let data = try await service.fetchWeather(city: city)
            state = .success(data)
        } catch {
            state = .error("Δεν βρήκα αυτή την πόλη, δοκίμασε άλλο όνομα;")
        }
    }
}

// Στην οθόνη:
switch vm.state {
case .loading: ProgressView("Φόρτωση…")
case .success(let d): WeatherContent(data: d)
case .error(let msg): Text(msg).foregroundColor(.secondary)
}
```
:::

Το τριμερές σχήμα loading/success/error είναι το «καθολικό πρότυπο» των συνδεδεμένων διεπαφών — μάθε το αρχικά απ' έξω, και μετά σε κάθε συνδεδεμένη εφαρμογή ακολούθησε το ίδιο σχήμα.

#### 4. Πρακτικός κώδικας διεπαφής: απεικόνισε τον καιρό

::: div .code-block
:::inline div .code-head
<span>SWIFT · Οθόνη καιρού (κομμάτι-κλειδί)</span><span class="dots">···</span>
:::

```
struct WeatherContent: View {
    let data: WeatherResponse

    var body: some View {
        VStack(spacing: 12) {
            Text(data.name)
                .font(.title.bold())
            Text("\(Int(data.main.temp))°C")
                .font(.system(size: 76, weight: .thin))
            Text(data.weather.first?.description ?? "Άγνωστο")
                .font(.title3)
                .foregroundColor(.secondary)
            HStack(spacing: 24) {
                Label("Υγρασία \(data.main.humidity)%", systemImage: "humidity")
                Label("Αίσθηση \(Int(data.main.temp))°C", systemImage: "thermometer")
            }
        }
        .padding()
    }
}
```
:::

Μερικές λεπτομέρειες που αξίζει να προσέξεις: το first? παίρνει με ασφάλεια το πρώτο στοιχείο (η λίστα μπορεί να είναι άδεια), το ?? «Άγνωστο» δίνει εφεδρικό κείμενο· οι αριθμοί της θερμοκρασίας σε λεπτό βάρος γραμματοσειράς (76) είναι η κλασική συνταγή των εφαρμογών καιρού· το Label είναι το επίσημο στοιχείο «εικονίδιο+κείμενο», πιο σωστό από ένα χειροποίητο HStack.

#### 5. Λεπτομέρειες αλληλεπίδρασης και αγαπημένες πόλεις

- Πεδίο αναζήτησης: ο τροποποιητής .searchable στην κορυφή δίνει την ενσωματωμένη αναζήτηση του συστήματος, και στην υποβολή καλεί το vm.search·
- Αγαπημένες πόλεις: αποθήκευσε τις πόλεις που κοιτάς συχνά στο UserDefaults, και την επόμενη φορά η αναζήτηση γίνεται αυτόματα·
- Ανανέωση με τράβηγμα προς τα κάτω: η μία γραμμή .refreshable { await vm.search(...) } τα κάνει όλα·
- Εικονίδια καιρού: με το Image(systemName:) κάνεις αντιστοίχιση ανά περιγραφή (sun.max / cloud.rain / snowflake) και η οθόνη ζωντανεύει αμέσως.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Μικρή συμβουλή: η «παγίδα» με τα κινέζικα ονόματα πόλεων

{class="mt-1"}
Το OpenWeatherMap δεν τα πηγαίνει και τόσο καλά με τα κινέζικα ονόματα πόλεων: η αναζήτηση με το κινέζικο όνομα της πόλης («Μπεϊτζίνγκ») μπορεί να μη δώσει αποτέλεσμα, ενώ το «beijing» δουλεύει κανονικά. Η «επαγγελματική» λύση είναι ένας ενσωματωμένος πίνακας αντιστοίχισης «όνομα πόλης → αγγλικά/συντεταγμένες» ή σύνδεση με κινέζικη υπηρεσία καιρού. Στο στάδιο της εξάσκησης αρκεί να υποστηρίζεις ονόματα πόλεων σε pinyin/αγγλικά — μην το παλέψεις.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Φτιάξε το μόνο σου: λίστα ελέγχου αποδοχής της εφαρμογής καιρού

#### 6. Πώς κάνεις debugging στα αιτήματα δικτύου: εκτύπωση, καταγραφή κίνησης και προσομοίωση αργού δικτύου

Όταν μια συνδεδεμένη εφαρμογή χαλάει, 9 φορές στους 10 φταίει ότι «το αίτημα δεν στάλθηκε σωστά» ή «η απόκριση δεν αναλύθηκε σωστά». Τρία εργαλεία debugging:

1. Εκτύπωσε τα ακατέργαστα δεδομένα: τύπωσε το String(data: data, encoding: .utf8) για να δεις το ωμό JSON — ονόματα πεδίων και τύποι φαίνονται με μια ματιά, δέκα φορές πιο γρήγορα από το να μαντεύεις·
2. Εργαλεία καταγραφής κίνησης: στο Mac, το δωρεάν Proxyman / το open source Charles μπορεί να υποκλέψει όλα τα αιτήματα και τις αποκρίσεις της εφαρμογής, και σου δείχνει το δικτυακό στρώμα σαν ακτινογραφία·
3. Προσομοίωση αργού δικτύου: από το μενού του εξομοιωτή, Features → Network Link Conditioner (το εργαλείο κατεβαίνει από τον ιστότοπο των προγραμματιστών), μπορείς να προσομοιώσεις 3G και μεγάλη καθυστέρηση — και να φέρεις στην επιφάνεια προβλήματα εμπειρίας τύπου «γυρίζει ο τροχός μια αιωνιότητα».

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Μικρή συμβουλή: Το αίτημα δεν πέρασε από το ATS;

{class="mt-1"}
Αν το αίτημα πετάει «App Transport Security» σφάλμα μόλις σταλεί, κατά τις 8 στις 10 χρησιμοποιείς http:// μη κρυπτογραφημένη διεύθυνση. Τα επίσημα endpoints πρέπει να είναι HTTPS· για τοπικό debugging άνοιξε προσωρινά εξαίρεση (πρόσθεσε NSAllowsLocalNetworking στο Info.plist), και θυμήσου να την αφήσεις καθαρή πριν την κυκλοφορία.
:::

{class="mt-1"}
① Η αναζήτηση εμφανίζει κανονικά τον καιρό· ② κόψε το δίκτυο — η εφαρμογή δίνει κομψό μήνυμα σφάλματος χωρίς να κρασάρει (δοκίμασέ το κλείνοντας το δίκτυο του Mac με ενεργό τον εξομοιωτή!)· ③ γράψε μια ανύπαρκτη πόλη και δες αν το μήνυμα είναι φιλικό· ④ αποθήκευσε δύο αγαπημένες πόλεις και έλεγξε ότι υπάρχουν και μετά την επανεκκίνηση· ⑤ στη σκοτεινή λειτουργία η οθόνη να μην τσούζει τα μάτια. Αν περάσουν και οι πέντε, το έργο «αποφοιτά».
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Σύνοψη κεφαλαίου

- Πρώτα δοκίμασε το API στον browser και κατάλαβε το JSON, μετά γράψε κώδικα — η «προετοιμασία» δεν χάνει ποτέ
- Το API Key κρύβεται στο xcconfig, δεν μπαίνει ποτέ στο repository
- Μοντέλο Codable + URLSession με async/await: όταν τα πεδία ταιριάζουν, το JSON αναλύεται αυτόματα
- Οι τρεις καταστάσεις loading/success/error είναι το καθολικό εργαλείο των συνδεδεμένων διεπαφών
- Κομμένο δίκτυο, κενή είσοδος, ανύπαρκτη πόλη — ο χειρισμός σφαλμάτων είναι η βάση για να θεωρείται περασμένη μια συνδεδεμένη εφαρμογή
:::
