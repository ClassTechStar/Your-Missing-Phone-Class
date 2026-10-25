---
id: di-liu-shi-san-zhang
num: 63
part: ios-kai-fa-pian
nav: Κεφάλαιο 63: Προβολές, κατάσταση και πλοήγηση
toc: default
kind: chapter
---

### Κεφάλαιο 63: Προβολές, κατάσταση και πλοήγηση

{class="chapter-intro mb-4"}
Τα μονοσέλιδα παιχνίδια τα ξέρεις ήδη. Αυτό το κεφάλαιο λύνει δύο «προβλήματα μεγαλώματος»: πώς πηδάς από σελίδα σε σελίδα (πλοήγηση) και πώς ρέουν τα δεδομένα ανάμεσα στις σελίδες (διαχείριση κατάστασης). Με την ολοκλήρωσή του, θα μπορείς να στήσεις τον κλασικό σκελετό πολλαπλών σελίδων «λίστα > λεπτομέρειες > επεξεργασία».

#### Α. Η πλήρης εικόνα της ροής δεδομένων στη διαχείριση κατάστασης

Τα εργαλεία κατάστασης του SwiftUI δεν είναι μόνο το @State. Ρίξε πρώτα μια ματιά σε αυτή την πλήρη εικόνα, για να καταλάβεις «πότε χρησιμοποιείς ποιο»:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Εργαλείο</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Τι διαχειρίζεται</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ποιος το χρησιμοποιεί</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Τυπικές περιπτώσεις</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@State</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Προσωρινή κατάσταση ιδιωτική για τη σελίδα</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Τρέχουσα προβολή</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Μετρητής, κείμενο πεδίου εισαγωγής</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Binding</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Δανείζεσαι την κατάσταση κάποιου άλλου</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Η υποπροβολή αλλάζει τη γονική</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Προσαρμοσμένα components</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@StateObject / @Observable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Λογική κοινή σε πολλές σελίδες</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Μοντέλο προβολής (ViewModel)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Φόρτωση δεδομένων, επιχειρησιακή λογική</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@EnvironmentObject / .environment</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Κατάσταση κοινή σε όλη την εφαρμογή</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ολόκληρη η εφαρμογή</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Κατάσταση σύνδεσης χρήστη, ρυθμίσεις θέματος</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Πλήρης εικόνα των εργαλείων κατάστασης του SwiftUI (2026· το @Observable είναι πλέον mainstream)

::: div .code-block
:::inline div .code-head
<span>SWIFT · Κύριο ρεύμα 2026: view model με @Observable</span><span class="dots">···</span>
:::

```
// Ο μοντέρνος τρόπος σε iOS 17+: μακροεντολή @Observable (προτεινόμενη για νέα έργα)
import Observation

@Observable
class CounterModel {                 // View model
    var count = 0
    func increment() { count += 1 }
}

struct CounterView: View {
    @State private var model = CounterModel()   // Κρατά το μοντέλο

    var body: some View {
        VStack {
            Text("Έχεις πατήσει \(model.count) φορές")
            Button("Πάτα με") { model.increment() }
        }
    }
}
```
:::

Άγρια συμβουλή για αρχάριους: ό, τι αφορά μόνο τη σελίδα με @State, και ό, τι διασελίδας/έχει λογική με κλάσεις @Observable. Τα @StateObject/@ObservableObject των παλιών οδηγών είναι η προηγούμενη γενιά — αρκεί να τα διαβάζεις, και στον νέο κώδικα ακολούθα τα παραπάνω.

#### Β. NavigationStack: η «στοίβα» της πλοήγησης

Από το iOS 16 και μετά, η πλοήγηση σε πολλές σελίδες γίνεται με το NavigationStack — σαν μια στοίβα πιάτων: ωθείς ένα-ένα μέσα, και στην επιστροφή βγαίνουν ένα-ένα:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Πλοήγηση NavigationStack</span><span class="dots">···</span>
:::

```
struct HomeView: View {
    var body: some View {
        NavigationStack {
            List {
                NavigationLink("Το λογιστήριο του Γιώργου") {
                    DetailView(name: "Το λογιστήριο του Γιώργου")   // σελίδα προορισμού
                }
                NavigationLink("Το λογιστήριο του Νίκου") {
                    DetailView(name: "Το λογιστήριο του Νίκου")
                }
            }
            .navigationTitle("Λίστα λογιστηρίων")   // μεγάλος τίτλος πάνω
        }
    }
}

struct DetailView: View {
    let name: String
    var body: some View {
        Text("Σελίδα λεπτομερειών \(name)")
            .navigationTitle(name)
            .navigationBarTitleDisplayMode(.inline)
    }
}
```
:::

Το NavigationLink είναι «ο σύνδεσμος που πατάς για μετάβαση»· το navigationTitle δημιουργεί αυτόματα τον τίτλο της μπάρας πλοήγησης και το κουμπί επιστροφής. Για προγραμματισμένη μετάβαση (π.χ. μετά το «Αποθήκευση» να γυρίζεις αυτόματα), χρησιμοποίησε το @Environment(\.dismiss) για να κλείνεις την τρέχουσα σελίδα — με αυτά τα δύο, καλύπτεται το 90% των αναγκών πλοήγησης.

#### Γ. Αναδυόμενα παράθυρα και κάτω καρτέλες: sheet και TabView

Εκτός από το «ωθείς σελίδες», υπάρχουν δύο ακόμα κλασικές αλληλεπιδράσεις:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Pop-up sheet + καρτέλες TabView</span><span class="dots">···</span>
:::

```
// 1. Pop μισής/ολοκλήρωσης οθόνης από κάτω (αγαπημένο για φόρμες)
struct HomeView: View {
    @State private var showAdd = false
    var body: some View {
        Button("Καταγραφή") { showAdd = true }
            .sheet(isPresented: $showAdd) {
                AddRecordView()     // Η σελίδα εισαγωγής που εμφανίζεται
            }
    }
}

// 2. Μπάρα καρτελών κάτω (ο "σκελετός" της εφαρμογής)
struct MainTabView: View {
    var body: some View {
        TabView {
            RecordListView()
                .tabItem { Label("Λογιστήριο", systemImage: "book") }
            StatsView()
                .tabItem { Label("Στατιστικά", systemImage: "chart.pie") }
            SettingsView()
                .tabItem { Label("Ρυθμίσεις", systemImage: "gear") }
        }
    }
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Συμβουλή: πότε χρησιμοποιείς ποιο;

{class="mt-1"}
Κανόνας εμπειρίας: για την κύρια ροή ωθείς σελίδες με NavigationStack (λίστα > λεπτομέρειες), για προσωρινές ενέργειες ανοίγεις sheet (προσθήκη, επεξεργασία, επιβεβαίωση), και για παράλληλα μεγάλα τμήματα χρησιμοποιείς TabView (κάτω καρτέλες). Ο συνδυασμός των τριών είναι ο σκελετός της συντριπτικής πλειονότητας των εφαρμογών.
:::

#### Δ. List: η «εθνική λίστα» του iOS

Το πιο συχνά χρησιμοποιούμενο και πιο «Apple» component στο iOS είναι το List — έχει εκ γενετής γραμμές διαχωρισμού, διαγραφή με ολίσθηση και επισήμανση στο πάτημα:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Λίστα List + σβούρισμα για διαγραφή</span><span class="dots">···</span>
:::

```
struct RecordListView: View {
    @State private var records = ["Μεσημεριανό 25.5", "Μετρό 6.0", "Μισθός +8000"]

    var body: some View {
        List {
            ForEach(records, id: \.self) { r in
                Text(r)
            }
            .onDelete { indexSet in          // σβούρισμα αριστερά για διαγραφή
                records.remove(atOffsets: indexSet)
            }
        }
    }
}
```
:::

Λίστα + NavigationLink + sheet + TabView — συνδυάζοντας αυτά τα τέσσερα, μπορείς ήδη να στήσεις τον πλήρη σκελετό εφαρμογής «λίστα βιβλίου εξόδων > άνοιγμα λεπτομερειών > πάτημα στο + ανοίγει φόρμα καταχώρισης». Έτσι θα στηθεί και το project βιβλίου εξόδων του επόμενου κεφαλαίου.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Ας το δοκιμάσουμε: στήσε έναν «σκελετό τριών σελίδων»

#### Ε. Κύκλος ζωής προγράμματος: προσκήνιο και παρασκήνιο

Όπως ο κύκλος ζωής του Activity στο Android, έτσι και οι εφαρμογές iOS έχουν αλλαγές κατάστασης «γέννηση, προσκήνιο, παρασκήνιο, θάνατος». Στο SwiftUI τις παρατηρείς με την τιμή περιβάλλοντος scenePhase:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Παρατήρηση εναλλαγής προσκηνίου/παρασκηνίου</span><span class="dots">···</span>
:::

```
@main
struct MyApp: App {
    @Environment(\.scenePhase) private var phase

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .onChange(of: phase) { _, newPhase in
            switch newPhase {
            case .active:    print("Πίσω σε πρώτο πλάνο, συνέχεια ανανέωσης")
            case .inactive:  print("Σε μετάβαση (κλήση/στιγμή ταμπλέτας)")
            case .background: print("Σε φόντο, αποθήκευση προσχέδιου")
            @unknown default: break
            }
        }
    }
}
```
:::

Τυπικές χρήσεις: όταν γυρνάς σε προσκήνιο ανανεώνεις τα δεδομένα, και όταν πηγαίνεις σε παρασκήνιο αποθηκεύεις το προσχέδιο. Το iOS ελέγχει αυστηρά την εκτέλεση στο παρασκήνιο — οι συνηθισμένες εφαρμογές σύντομα αναστέλλονται (παγώνονται) μόλις πάνε στο παρασκήνιο, οπότε μην περιμένεις να κάνεις κρυφά βαριές δουλειές στο παρασκήνιο· για προγραμματισμένες εργασίες, χρησιμοποίησε τις τοπικές ειδοποιήσεις του Κεφαλαίου 68, όχι «μόνιμη παραμονή στο παρασκήνιο».

{class="mt-1"}
Φτιάξε τον σκελετό του βιβλίου εξόδων σε έκδοση με εικονικά δεδομένα: TabView με τρεις καρτέλες (Βιβλίο εξόδων/Στατιστικά/Ρυθμίσεις) > στη σελίδα Βιβλίο εξόδων εμφάνισε εικονικά δεδομένα με List, πάτα σε γραμμή και πήγαινε στις λεπτομέρειες (NavigationStack) > το κουμπί «+» πάνω δεξιά ανοίγει sheet καταχώρισης. Χωρίς αποθήκευση δεδομένων, χωρίς internet — καθαρή εξάσκηση στον σκελετό. Όταν αυτός ο σκελετός γίνει καλά, στο Κεφάλαιο 65 το γέμισμα με πραγματικά δεδομένα θα έρθει φυσικά.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Σύνοψη κεφαλαίου

- Τα τέσσερα εργαλεία κατάστασης: @State (ιδιωτικό σελίδας), @Binding (δανεισμός), @Observable (λογική), .environment (καθολικό)
- Στα νέα project γράφε τα view models με τη μακροεντολή @Observable· τα @ObservableObject των παλιών οδηγών, αρκεί να τα διαβάζεις
- Το NavigationStack ωθεί σελίδες· το @Environment(\.dismiss) δίνει προγραμματισμένη επιστροφή
- Κύρια ροή: ωθείς σελίδες· προσωρινές ενέργειες: sheet· παράλληλα μεγάλα τμήματα: TabView
- Το List είναι η «εθνική λίστα»: γραμμές διαχωρισμού και διαγραφή με ολίσθηση, έτοιμα εκ κατασκευής
:::
