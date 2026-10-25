---
id: di-er-shi-zhang-termux
part: jin-jie-pian
nav: Κεφάλαιο 20
toc: sub
kind: supplement
---

### Κεφάλαιο 20 Παράρτημα: Termux — φορητό περιβάλλον τερματικού Linux σε Android

{class="chapter-intro mb-4"}
Αν νιώθετε ότι η λειτουργία προγραμματιστή δεν είναι αρκετά «hardcore» και θέλετε μια ολοκληρωμένη εμπειρία Linux command line στο κινητό, το Termux είναι για εσάς. Χωρίς root, μετατρέπει ένα απλό Android κινητό σε φορητό Linux σταθμό εργασίας — ιδανικό για προχωρημένους χρήστες που εξερευνούν την ανάπτυξη και τη λειτουργία σε κινητά.

#### I. Τι είναι το Termux

Το Termux είναι εφαρμογή ανοιχτού κώδικα για Android, παρέχει πλήρη εμπειρία Linux shell χωρίς root. Ως ελαφριά εφαρμογή (~30MB), μέσω APT υποστηρίζει πλούσιο οικοσύστημα, επιτρέποντας Python, Node.js, Git, SSH, ακόμα και στήσιμο διακομιστή ή penetration testing.

Το βασικό πλεονέκτημα του Termux είναι η ελαφριά αρχιτεκτονική και η υψηλή επεκτασιμότητα, κατάλληλο για ανάπτυξη, μάθηση και διαχείριση συστημάτων. Συνδυάζει τυποποιημένα πακέτα με ακριβή προσομοίωση τερματικού σε λύση ανοιχτού κώδικα.

#### II. Βασικές λειτουργίες και χαρακτηριστικά

##### 🖥️ Πλήρες περιβάλλον Linux

Termux <strong>Μόνο ενσωματωμένο Bash</strong> Shell.ZshfishShell, χειροκίνητο εγκατάσταση,:<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install zsh</code>ή<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install fish</code>.TermuxVim, Nano, Emacs Επεξεργασία, εγγενές Εντολή.Χρήστης "pkg install"εγκατάσταση 2000+,GCC, OpenSSH, SQLMap Ασφάλεια.

##### 📦 Ισχυρός package manager

Χρήση APT (όπως Debian, Ubuntu), εγκαθιστά χιλιάδες πακέτα Linux, εργαλεία ανάπτυξης και δικτύου. Υποστηρίζει Python, Ruby, Node.js, Go, Rust, Swift.

##### 🔒 Ασφάλεια και δίκτυο

- <strong>SSH απομακρυσμένη σύνδεση</strong>. SSH client και server.
- <strong>Εργαλείο κρυπτογράφησης</strong>. OpenSSL κ.λπ., κρυπτογράφηση και ασφαλής επικοινωνία.
- <strong>Στήσιμο διακομιστή</strong>: Nginx ή Apache για static server.

##### 🔧 Ενσωμάτωση και επέκταση

- Πρόσβαση αποθήκευσης για τοπική διαχείριση αρχείων.
- Καλέστε αισθητήρες και κάμερα Android μέσω Termux:API.
- Υποστηρίζει μπλουτούθ πληκτρολόγιο και εξωτερική οθόνη, με πλήρη υποστήριξη ποντικιού.

#### III. Οικοσύστημα πρόσθετων

Η κεντρική εφαρμογή Termux επεκτείνεται με προαιρετικά πρόσθετα, παρέχοντας επιπλέον λειτουργίες:

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                        <thead>
                            <tr class="bg-light dark:bg-gray-700">
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Όνομα πρόσθετου</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Περιγραφή λειτουργίας</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:API</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Έκθεση λειτουργιών Android API σε προγράμματα γραμμής εντολών</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Boot</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Επιτρέπει εκτέλεση σεναρίων κατά την εκκίνηση</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Float</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Παρέχει παράθυρο πλωτού τερματικού</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Styling</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ενεργοποίηση σχημάτων χρωμάτων και προσαρμογής γραμματοσειρών</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Tasker</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ενσωμάτωση σεναρίων Termux με την εφαρμογή αυτοματισμού Tasker</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Widget</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Επιτρέπει εκτέλεση σεναρίων από widget αρχικής</td>
                            </tr>
                        </tbody>
                    </table>
```

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Σημαντική υπόδειξη

{class="mt-1"}
Το Termux και τα πρόσθετά του πρέπει να εγκαθίστανται από την ίδια πηγή, διότι μοιράζονται το ίδιο sharedUserId. Ανάμειξη πηγών (π.χ. F-Droid και GitHub) προκαλεί σφάλμα εγκατάστασης.
:::

#### IV. Οδηγός εγκατάστασης και ρύθμισης

##### 📥 Βήματα εγκατάστασης

1. <strong>Λήψη εφαρμογής</strong>: Από F-Droid ή GitHub, χωρίς root.
2. <strong>Αρχικοποίηση συστήματος</strong>. Περιμένετε "Installing bootstrap packages".
3. <strong>Λήψη δι και ωμάτων αποθήκευσης</strong>: εκτέλεση<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">termux-setup-storage</code>Λήψη δι και ωμάτων συστήματος αρχείων.
4. <strong>Ενημέρωση πηγής λογισμικού</strong>: εκτέλεση<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg update &amp;&amp; pkg upgrade</code>Ενημέρωση λίστας πακέτων.

##### ⚙️ Βασική βελτιστοποίηση

- <strong>Αλλαγή mirror</strong>: Χρήση<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">termux-change-repo</code>Εντολή αλλαγής mirror μέσω γραφικού περιβάλλοντος (συνιστάται mirror του Πανεπιστημίου Tsinghua).
- <strong>Ρυθμίσεις συντομεύσεων πληκτρολογίου</strong>. Τόνος- = Ctrl, τόνος+ = Esc, ταχύτητα.
- <strong>Ομορφοποίηση διεπαφής</strong>: Zsh + Oh My Zsh, theme και plugins.

#### V. Τυπικά σενάρια χρήσης

##### 💻 Mobile dev testing

Στήστε ένα πλήρες περιβάλλον ανάπτυξης στο κινητό: γράψτε και τρέξτε Python scripts, μεταγλωττίστε C προγράμματα με GCC, διαχειριστείτε αποθετήρια με Git, συγχρονιστείτε με απομακρυσμένους servers μέσω SSH.

##### 🖥️ Διαχείριση διακομιστή

Διαχειριστείτε διακομιστές μέσω SSH, συντήρηση και ανάλυση log, από παντού.

##### 📚 Εκμάθηση Linux

Linux, Εντολή Σύστημα Πλατφόρμα, ShellScript, Linux Αρχείο Δικαίωμα( <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">chmod 755</code> Ορισμός δι και ωμάτων rwxr-xr-x,<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">chown user:group</code> Αλλαγή ιδιοκτησίας αρχείου,<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">ls -l</code> Προβολή owner/group/other Δικαίωμα)βασικό Εντολή.Unix/Linux""Δικαίωμα(owner / group / other × / / ),Windows NTFSACL.

##### 🔐 Network security testing

Εγκατάσταση εργαλείων ασφαλείας όπως Nmap, SQLMap, Hydra, Metasploit για σάρωση δικτύου και δοκιμές διείσδυσης.

#### VI. Εκδόσεις και συμβατότητα

Η τελευταία σταθερή έκδοση του Termux είναι η v0.118.2, για Android ≥ 7. Στο Android 12+ ενδέχεται να υπάρχουν αστάθειες· παρακολουθήστε το επίσημο changelog.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Συμπέρασμα

{class="mt-1"}
Το Termux φέρνει την ισχυρή εμπειρία τερματικού Linux σε Android, κάνοντας το κινητό φορητό εργαλείο ανάπτυξης και μάθησης. Developers, διαχειριστές συστημάτων και λάτρεις της τεχνολογίας απολαμβάνουν πλήρη εμπειρία γραμμής εντολών, υλοποιώντας την ιδέα "Linux στην τσέπη".
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Δοκιμή: τρέξτε την πρώτη εντολή Linux στο κινητό

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Κατεβάστε και εγκαταστήστε το Termux από F-Droid, περιμένετε την αρχικοποίηση.
2. Εκτέλεση<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg update &amp;&amp; pkg upgrade</code>Ενημέρωση πακέτων λογισμικού.
3. Εγκατάσταση Python:<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install python</code>.
4. Εισαγωγή<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">python3 -c "print('Hello from Termux!')"</code>, νιώστε τη χαρά του κώδικα στο κινητό.
:::
