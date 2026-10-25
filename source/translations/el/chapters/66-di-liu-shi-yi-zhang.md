---
id: di-liu-shi-yi-zhang
num: 61
part: ios-kai-fa-pian
nav: Κεφάλαιο 61: Swift σε γρήγορους ρυθμούς — η πρώτη γλώσσα για ανάπτυξη στην Apple
toc: default
kind: chapter
---

### Κεφάλαιο 61: Γρήγορη εκμάθηση Swift — η πρώτη γλώσσα της Apple

{class="chapter-intro mb-4"}
Σε αυτό το κεφάλαιο μαθαίνουμε επίσημα τη γλώσσα. Μην αγχώνεσαι — η Swift είναι διάσημη για το ότι είναι «φιλική στους αρχάριους», και δεν χρειάζεται να αποστηθίσεις βιβλία σύνταξης: μαθαίνοντας το 20% της σύνταξης, διαβάζεις και γράφεις το 80% του καθημερινού κώδικα. Τα υπόλοιπα τα ψάχνεις όσο χτίζεις project. Θυμήσου την αρχή μάθησής μας: να καταλαβαίνεις > να αποστηθίζεις, να ξέρεις να το χρησιμοποιείς > να το κατέχεις σε βάθος.

#### Α. Μεταβλητές και τύποι: δίνουμε ονόματα στα δεδομένα

Ένα πρόγραμμα είναι «δεδομένα + λογική». Η μεταβλητή είναι να δώσεις στα δεδομένα ένα όνομα και να τα αποθηκεύσεις. Στη Swift δηλώνεις με let και var:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Μεταβλητές</span><span class="dots">···</span>
:::

```
let name = "Γιώργος"        // let: σταθερά (προτείνεται ως προεπιλογή)
var age = 18             // var: μεταβλητή (μπορεί να αλλάξει μετά)

age = 19                 // <i class="fas fa-check-circle mr-1"></i> var αλλάζει
// name = "Νίκος"         // <i class="fas fa-times-circle mr-1"></i> let δεν αλλάζει, σφάλμα μεταγλώττισης

let score: Int = 100     // μπορείς και να γράψεις τον τύπο ρητά
let pi = 3.14            // και χωρίς αυτόν γίνεται αυτόματη εξαγωγή

print("Γεια σου, \(name)")   // ενσωμάτωση αλφαριθμητικού: ανάστροφη κάθετος + παρένθεση
```
:::

Οι συχνά χρησιμοποιούμενοι τύποι, σε έναν πίνακα:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Τύπος</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Τι αποθηκεύει</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Παράδειγμα</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Int</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ακέραιος</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">42</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Double</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Δεκαδικός</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3.14</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">String</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Κείμενο</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">«Γεια σου»</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bool</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Αληθές/Ψευδές</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">true / false</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">[Int] (πίνακας)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Μια συλλογή δεδομένων</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">[1, 2, 3]</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Οι βασικοί συχνοί τύποι της Swift

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Συμβουλή: ο κανόνας «πρώτα let»

{class="mt-1"}
Σιδερένιος κανόνας της κοινότητας της Swift: με let ως προεπιλογή, και var μόνο όταν πραγματικά χρειάζεται. Αν γράψεις var όπου θα μπορούσε let, το Xcode θα σε προειδοποιήσει με κίτρινο γράμμα. Η συνήθεια αυτή σε γλιτώνει από μια ολόκληρη κατηγορία bugs «τυχαίας αλλαγής μεταβλητής» — όσο λιγότερο αλλάζει ο κώδικας, τόσο πιο εύκολο είναι να τον συλλογιστείς.
:::

#### Β. Προαιρετικές τιμές (Optional): το «φυλαχτό κατά των crashes» της Swift

Αυτή είναι η πιο σημαντική έννοια της Swift, χωρίς δεύτερη. Με μια φράση: όταν μια τιμή μπορεί «να μην υπάρχει», η Swift σε αναγκάζει να τη διαχειριστείς — εξαλείφοντας από τη γλώσσα τον επαγγελματικό εφιάλτη του «crash λόγω κενού δείκτη».

::: div .code-block
:::inline div .code-head
<span>SWIFT · Optionals</span><span class="dots">···</span>
:::

```
var name: String = "Γιώργος"   // Συνηθισμένος τύπος: ποτέ nil
// name = nil                // <i class="fas fa-times-circle mr-1"></i> Σε σταματάει κατευθείαν ο compiler

var nickname: String? = nil  // με ερωτηματικό: επιτρέπεται nil (optional)
nickname = "Μπαμπής"

// Με optional, πρέπει να "ξετυλίξεις" πρώτα:
if let n = nickname {        // if let: ασφαλές ξετύλιγμα
    print("Γεια σου, \(n)")
} else {
    print("Δεν έχει ακόμα παρατσούκλι")
}

let len = nickname?.count ?? 0   // ?? δίνει προεπιλογή (nil coalescing)
print(len)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Προσοχή: το ! είναι «επικίνδυνη κίνηση»

{class="mt-1"}
Όταν γράφεις nickname! (βίαιη αποσυμπίεση), είναι σαν να φωνάζεις στον compiler «εγγυώμαι ότι δεν είναι nil» — αν πέσεις έξω, η εφαρμογή κρασάρει επί τόπου. Κανόνας για αρχάριους: χρησιμοποίησε όσο γίνεται if let / ?? και όχι !. Όταν το Xcode συμπληρώνει κώδικα, κάπου-κάπου σου πετάει ένα ! — θυμήσου να το αλλάζεις.
:::

#### Γ. Συναρτήσεις και closures: πακετάρουμε τη λογική σε «κουμπιά»

Η συνάρτηση είναι ένα τμήμα λογικής με όνομα, σαν ένα κουμπί στο τηλεχειριστήριο. Το closure είναι «συνάρτηση χωρίς όνομα», που μπορείς να περάσεις όποιον θέλεις:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Συναρτήσεις και closures</span><span class="dots">···</span>
:::

```
// Συνάρτηση: το όνομα μπροστά, παράμετροι και τύπος επιστροφής πίσω
func greet(name: String) -> String {
    return "Γεια σου, \(name)!"
}
print(greet(name: "Γιώργος"))     // Στην κλήση πρέπει να αναφέρεται το όνομα της παραμέτρου

// Closure: ορισμός επί τόπου, κομψά και άμεσα
let numbers = [1, 2, 3, 4]
let doubled = numbers.map { $0 * 2 }   // $0 = τρέχον στοιχείο
// [2, 4, 6, 8]

let big = numbers.filter { $0 > 2 }    // Φιλτράρισμα
// [3, 4]
```
:::

Στο SwiftUI τα closures είναι παντού: τα άγκιστρα { ... } που ακολουθούν το Button("Πάτα με") είναι ένα closure. Τα map, filter, sorted — τα «συνδυαστικά χτυπήματα» των συλλογών — κράτα τα καλά: το 90% της μελλοντικής επεξεργασίας λιστών θα είναι συνδυασμός τους.

#### Δ. Structs και protocols: το σύστημα «LEGO» της Swift

Η επίσημη προτίμηση της Swift είναι ξεκάθαρη: προτίμησε struct, και class μόνο όταν χρειάζεται κληρονομικότητα. Τα struct είναι «τύποι τιμής» — στην αντιγραφή, το καθένα ζει τη ζωή του, και έτσι λείπει από μόνο του μια κατηγορία bugs:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Structs και protocols</span><span class="dots">···</span>
:::

```
// Struct: κουτί με δεδομένα
struct Record {
    var id = UUID()
    var amount: Double
    var category: String
    var date: Date

    // Το struct έχει έτοιμο "memberwise initializer": δημιουργείται κατευθείαν
}
let r = Record(amount: 25.5, category: "Φαγητό", date: Date())

// Protocol: συμφωνία για "ποιες ικανότητες πρέπει να έχει"
protocol Identifiable {
    var id: UUID { get }
}
struct Record: Identifiable { ... }   // Συμμόρφωση με protocol = υπόσχεση υλοποίησης των απαιτήσεων
```
:::

Στο SwiftUI σχεδόν τα πάντα είναι struct (το View είναι protocol). Αν δεν το καταλαβαίνεις τώρα, δεν πειράζει — από το Κεφάλαιο 62 θα τα συναντάς καθημερινά. Στον κόσμο της Swift, αγκαλιάσε πρώτα το struct.

#### Ε. Κάρτα ταχείας αναφοράς σύνταξης για απόλυτους αρχάριους

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Τι θέλεις να κάνεις</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Πώς γράφεται</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ορισμός σταθεράς/μεταβλητής</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">let x = 1</code> / <code class="inline">var x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Εμβολή συμβολοσειρών (string interpolation)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"Γεια σου, \(name)"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ορισμός συνάρτησης</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">func ονομα(παράμετρος: τύπος) -> τύπος Επιστροφής { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Έλεγχος συνθήκης</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if συνθήκη { ... } else { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Επανάληψη</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">for x in πίνακας { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ασφαλής αποσυμπίεση</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if let x = προαιρετική Τιμή { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Προεπιλεγμένη τιμή</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">x ?? προεπιλεγμένη Τιμή</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ορισμός struct</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">struct X { var a: Int; var b: String }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Closure</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">{ $0 * 2 }</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Κάρτα ταχείας αναφοράς σύνταξης Swift (για αρχάριους)

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Ας το δοκιμάσουμε: παίξε 15 λεπτά Swift στο Playgrounds

{class="mt-1"}
Αν έχεις Mac, άνοιξε Xcode > Playground· αν όχι, χρησιμοποίησε το Swift Playgrounds στο iPad ή το web-based περιβάλλον εξάσκησης. Τρέξε κάθε κομμάτι κώδικα του κεφαλαίου, άλλαξε αριθμούς και κείμενα, και φτιάξε σκόπιμα μερικά λάθη για να δεις πώς σου δείχνει το Xcode. Αυτά τα 15 λεπτά «πρώτα παίζεις, μετά μαθαίνεις» θα σου κάνουν την είσοδο στο Κεφάλαιο 62 διπλά πιο εύκολη.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Σύνοψη κεφαλαίου

- Πρώτα let, var με προσοχή· οι τύποι εξάγονται αυτόματα, αλλά μπορείς να τους δηλώσεις ρητά μετά την άνω-κάτω τελεία
- Τα Optional είναι η ψυχή της Swift: ό, τι μπορεί να είναι κενό πρέπει να διαχειριστείς· το if let / ?? είναι το φυλαχτό, το ! επικίνδυνη κίνηση
- Στην κλήση συνάρτησης γράφεις τα ονόματα των παραμέτρων· το closure = συνάρτηση χωρίς όνομα, και είναι παντού στο SwiftUI
- Πρώτα struct, και τήρηση των protocols (Protocol)· στο SwiftUI σχεδόν τα πάντα είναι struct
- Με το 20% της σύνταξης κάνεις το 80% της δουλειάς: πρώτα να ξέρεις να το χρησιμοποιείς, μετά να το κατέχεις σε βάθος
:::
