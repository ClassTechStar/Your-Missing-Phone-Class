---
id: di-liu-shi-er-zhang
num: 62
part: ios-kai-fa-pian
nav: Κεφάλαιο 62: Ανάπτυξη διεπαφών — πρώτα βήματα με SwiftUI
toc: default
kind: chapter
---

### Κεφάλαιο 62: Ανάπτυξη διεπαφής — εισαγωγή στο SwiftUI

{class="chapter-intro mb-4"}
Η διεπαφή είναι ό, τι βλέπει ο χρήστης. Το SwiftUI είναι το δηλωτικό framework διεπαφής που παρουσίασε η Apple το 2019 — αρκεί να «δηλώσεις» πώς μοιάζει η διεπαφή, και το σύστημα αναλαμβάνει αυτόματα την απεικόνιση, την προσαρμογή στο σκούρο θέμα και την προσαρμογή σε κάθε οθόνη. Το 2026 το SwiftUI είναι ήδη η απόλυτα mainstream επιλογή για νέα project. Σε αυτό το κεφάλαιο μαθαίνουμε να «ζωγραφίζουμε».

#### Α. Η ιδέα του SwiftUI: δηλωτικό, όχι προστακτικό

Η παλιά ανάπτυξη διεπαφών είναι «προστακτική»: λες στο σύστημα «φτιάξε κουμπί > βάλε το στο (20,30) > όρισε χρώμα» και το καθοδηγείς βήμα-βήμα. Το SwiftUI είναι «δηλωτικό»: περιγράφεις απευθείας «στη διεπαφή υπάρχει ένα κόκκινο κουμπί που γράφει 'Πάτα με'», και το πώς θα ζωγραφιστεί και πότε θα ξαναζωγραφιστεί το φροντίζει το ίδιο το σύστημα.

::: div .code-block
:::inline div .code-head
<span>SWIFT · Η πρώτη σου view SwiftUI</span><span class="dots">···</span>
:::

```
import SwiftUI

struct ContentView: View {
    var body: some View {      // body: περιγράφει "πώς μοιάζει η οθόνη"
        VStack {               // κατακόρυφη διάταξη
            Text("Γεια σου κόσμε!")
                .font(.largeTitle)      // modifier: μεγάλος τίτλος
            Button("Πάτα με") {
                print("Πατήθηκε")
            }
            .buttonStyle(.borderedProminent)  // μπλε συμπαγές κουμπί
        }
        .padding()
    }
}
```
:::

Το κλειδί: προβολή = struct που ακολουθεί το protocol View, η ιδιότητα body περιγράφει τη διεπαφή, και οι .τροποποιητές() «μακιγιάρουν» σε αλυσίδα. Αυτά είναι όλο το θεμέλιο του SwiftUI.

#### Β. Βασικές προβολές: κείμενο, κουμπί, πεδίο εισαγωγής, εικόνα

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Προβολή</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Τι κάνει</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Παράδειγμα</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Εμφάνιση κειμένου</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text("Γεια σου")</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Κουμπί</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button("Πάτα με") { ενέργεια }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Πεδίο εισαγωγής</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField("Υπόδειξη", text: $κείμενο)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Image</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Εμφάνιση εικόνας</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Image(systemName: "star.fill")</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Οι τέσσερις βασικές προβολές του SwiftUI

Πρόσεξε το Image(systemName:) — η Apple διαθέτει ενσωματωμένη τη βιβλιοθήκη εικονιδίων SF Symbols (χιλιάδες δωρεάν εικονίδια), και με ένα όνομα όπως «star.fill» εμφανίζεται αμέσως ένα γεμάτο αστέρι. Αυτό είναι ένα κρυφό δώρο της ανάπτυξης iOS: στη δημιουργία διεπαφών σχεδόν δεν χρειάζεται να ψάχνεις υλικό εικονιδίων.

#### Γ. Τα τρία εργαλεία διάταξης: VStack, HStack, ZStack

- VStack: στοίχιση σε στήλες (σαν ουρά για φαγητό)·
- HStack: στοίχιση σε γραμμή (σαν να κάθεστε δίπλα-δίπλα)·
- ZStack: τοποθέτηση το ένα πάνω στο άλλο (σαν τραπουλόχαρτα φορτωμένα, κατάλληλο για badges, καλύμματα).

::: div .code-block
:::inline div .code-head
<span>SWIFT · Τριάδα layout + συνηθισμένα modifiers</span><span class="dots">···</span>
:::

```
VStack(alignment: .leading, spacing: 12) {
    HStack {
        Text("Λογαριασμός")
        Spacer()                 // Ελαστικός χώρος: σπρώχνει τα δεξιά ως άκρο
        Text("-25.5 γιουάν").foregroundColor(.red)
    }
    Divider()                    // Διαχωριστική γραμμή
    Text("Σημείωση: μεσημεριανό")
}
.padding(16)                     // περιθώριο γύρω-γύρω
.background(Color(.systemGray6)) // ανοιχτό γκρι φόντο
.cornerRadius(12)                // στρογγυλεμένες γωνίες

// Η σειρά των modifiers μετράει: πρώτα padding μετά background, το φόντο δεν περιλαμβάνει τα περιθώρια
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Προσοχή: η σειρά των τροποποιητών έχει σημασία

{class="mt-1"}
Το padding(16).background(γκρι) και το background(γκρι).padding(16) έχουν διαφορετικό αποτέλεσμα — το πρώτο «πρώτα περιθώριο, μετά χρώμα» (το φόντο δεν περιλαμβάνει το περιθώριο), το δεύτερο «πρώτα χρώμα, μετά περιθώριο» (το φόντο περιλαμβάνει το περιθώριο). Οι πιο συχνές «περίεργες λευκές άκρες» του αρχάριου πηγάζουν από εδώ. Όταν διστάζεις, άλλαξε τη σειρά και η προεπισκόπηση θα σου δώσει αμέσως την απάντηση.
:::

#### Δ. Κατάσταση και δέσμευση: κάνε τη διεπαφή να «ζωντανεύει»

Η στατική διεπαφή δεν έχει γοητεία. Ο κανόνας του SwiftUI: η διεπαφή αντικατοπτρίζει πάντα πιστά την κατάσταση· όταν η κατάσταση αλλάζει, η διεπαφή ξαναζωγραφίζεται αυτόματα.

::: div .code-block
:::inline div .code-head
<span>SWIFT · Μετρητής με @State</span><span class="dots">···</span>
:::

```
struct CounterView: View {
    @State private var count = 0   // @State: όταν αλλάζει αυτή η τιμή, ξαναζωγραφίζει

    var body: some View {
        VStack {
            Text("Έχεις πατήσει \(count) φορές")
            Button("Πάτα με +1") {
                count += 1          // αλλαγή κατάστασης, η οθόνη ανανεώνεται μόνη της
            }
        }
    }
}
```
:::

Το πεδίο εισαγωγής θέλει «αμφίδρομη δέσμευση» — το σύμβολο $ περνάει ταυτόχρονα την «τιμή και το δικαίωμα αλλαγής»:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Αμφίδρομη σύνδεση με @Binding</span><span class="dots">···</span>
:::

```
struct InputView: View {
    @State private var text = ""

    var body: some View {
        TextField("Γράψε κάτι", text: $text)  // αμφίδρομη σύνδεση με $
            .textFieldStyle(.roundedBorder)
        Text("Έγραψες: \(text)")   // ενημερώνεται ζωντανά όσο γράφεις
    }
}
```
:::

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hand-pointer mr-1"></i> Ενέργεια χρήστη</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> Η κατάσταση αλλάζει (count += 1)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> Το SwiftUI αντιλαμβάνεται την αλλαγή</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> Αυτόματο ξαναζωγράφισμα οθόνης (επανυπολογισμός του body)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Εικόνα 3: Η μονής κατεύθυνσης ροή δεδομένων «κατάσταση > διεπαφή» του SwiftUI
:::

#### Ε. Προεπισκόπηση, θέμα και κίνηση: τα «πρόσθετα» του SwiftUI

- Η μακροεντολή #Preview: πρόσθεσε στο τέλος του αρχείου #Preview { ContentView() } και το canvas στα δεξιά αποδίδει σε πραγματικό χρόνο — αλλάζεις κώδικα και βλέπεις αμέσως·
- Σκούρο θέμα δωρεάν: χρησιμοποίησε τα χρώματα συστήματος (Color(.systemGray6), .primary) αντί για σταθερά χρώματα, και το σκούρο θέμα προσαρμόζεται αυτόματα, χωρίς ούτε μία επιπλέον γραμμή·
- Κίνηση με μια γραμμή: withAnimation { count += 1 } ή πρόσθεσε .animation(.default, value: count) στην προβολή — οι μεταβάσεις γίνονται βελούδινες.

::: div .code-block
:::inline div .code-head
<span>SWIFT · Animation που μαθαίνεις σε 10 λεπτά</span><span class="dots">···</span>
:::

```
struct AnimatedHeartView: View {
    @State private var liked = false

    var body: some View {
        Button {
            withAnimation(.spring(duration: 0.4)) {
                liked.toggle()
            }
        } label: {
            Image(systemName: liked ? "heart.fill" : "heart")
                .font(.system(size: 48))
                .foregroundColor(liked ? .red : .gray)
                .scaleEffect(liked ? 1.3 : 1.0)
        }
    }
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Συμβουλή: πρώτα λειτουργία, μετά κίνηση

{class="mt-1"}
Το συχνό λάθος του αρχάριου: «η διεπαφή δεν έχει γίνει ακόμα σωστά, και ήδη σπάει το κεφάλι για κινήσεις». Πρώτα βεβαιώσου ότι η λειτουργία τρέχει, και στο τέλος πρόσθεσε τις κινήσεις μαζί — η κίνηση είναι το κερασάκι στην τούρτα, η λειτουργία είναι η σωτηρία στη θύελλα. Αυτή είναι και η σταθερή μας αρχή «η απλότητα πάνω απ' όλα».
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Ας το δοκιμάσουμε: φτιάξε ένα «κουμπί διάθεσης»

#### ΣΤ. Ταχεία αναφορά συχνών τροποποιητών: με μια σελίδα στο χέρι, δεν αγχώνεσαι με τη διεπαφή

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Τι θέλεις να κάνεις</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Τροποποιητής</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Περιθώριο</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.padding(16)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Στρογγυλεμένες γωνίες</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.cornerRadius(12)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Χρώμα φόντου</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.background(Color(.systemGray6))</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Γραμματοσειρά και μέγεθος</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.font(.title.bold())</code> / <code class="inline">.font(.system(size: 20))</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Χρώμα προσκηνίου (κείμενο/εικονίδιο)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.foregroundColor(.red)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Γέμισμα του πλάτους</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.frame(maxWidth: .infinity)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Σταθερό μέγεθος</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.frame(width:100, height: 44)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Στοίχιση</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">VStack(alignment: .leading)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Διαφάνεια</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.opacity(0.6)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Σκιά</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.shadow(radius: 5)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Χειρονομία πάτησης</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.onTapGesture { ... }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Τύπος πληκτρολογίου</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.keyboardType(.decimalPad)</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Ταχεία αναφορά συχνών τροποποιητών SwiftUI

Δεν πειράζει αν δεν τα θυμάσαι — αυτή η σελίδα είναι για αναζήτηση. Τα πιο συχνά χρησιμοποιούμενα είναι τελικά τα τέσσερα πρώτα: padding, στρογγυλεμένες γωνίες, φόντο, γραμματοσειρά.

{class="mt-1"}
Άλλαξε το template project σε έναν εναλλάκτη διάθεσης: ένα κουμπί που, όταν το πατάς, κυκλικά εναλλάσσεται ανάμεσα σε 😀 χαρά > 😢 λύπη > 😡 θυμός, με το κείμενο και το χρώμα φόντου να αλλάζουν μαζί. Συμβουλή: κράτα σε πίνακα τρία ζευγάρια (κείμενο+χρώμα), την ένδειξη σε @State, και όταν πατάς (index + 1) % 3. Όταν το τελειώσεις, στείλε το σε φίλους να παίξουν και μαζέψε το πρώτο κύμα «ουάου, ξέρεις να φτιάχνεις εφαρμογές».
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Σύνοψη κεφαλαίου

- Το SwiftUI είναι δηλωτικό: περιγράφεις «πώς μοιάζει», και το σύστημα αναλαμβάνει τη ζωγραφική και το ξαναζωγράφισμα
- Προβολή = struct που ακολουθεί το protocol View· το body περιγράφει τη διεπαφή· οι τροποποιητές «μακιγιάρουν» σε αλυσίδα
- Οι τέσσερις βασικές προβολές: Text / Button / TextField / Image· η βιβλιοθήκη εικονιδίων SF Symbols είναι δωρεάν και άφθονη
- Τα τρία εργαλεία διάταξης: VStack κάθετα, HStack οριζόντια, ZStack σε στοίβα· το Spacer είναι ο ελαστικός χώρος
- Το @State κάνει τη διεπαφή να ζωντανεύει· το $ δίνει αμφίδρομη δέσμευση στο πεδίο εισαγωγής
- #Preview: ό, τι βλέπεις το παίρνεις· τα χρώματα συστήματος προσαρμόζονται αυτόματα στο σκούρο θέμα· το withAnimation δίνει κίνηση σε μια γραμμή
:::
