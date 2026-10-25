---
id: di-er-shi-si-zhang
num: 24
part: chao-yue-pian
nav: Κεφάλαιο 24: Δικαιώματα Root και BL lock σε βάθος
toc: default
kind: chapter
---

### Κεφάλαιο 24: Βαθιά ανάλυση δι και ωμάτων Root και κλειδώματος Bootloader

{class="chapter-intro mb-4"}
Επέκταση κεφ. 20. Κίνδυνοι.

#### 1. Bootloader

Bootloader = φύλακας.

##### Πώς δουλεύει BL:

- <strong>Verify signature</strong>: Digital signature.
- <strong>Anti-downgrade</strong>: No old versions.
- <strong>Data protection</strong>: No access without account.

##### 🔐 Αποθήκευση και επαλήθευση σε επίπεδο υλισμικού

BL Κλείδωμα(Locked/Unlocked),Αποθήκευση( devinfo ,eFuse RPMB ). Bootloader Ασφάλεια ανάγνωση, Υπογραφή επαλήθευση.

##### 🔏 Επαλήθευση ψηφιακής υπογραφής

Δημοσίευση Σύστημα ενημέρωση Image, Υπογραφή.Συσκευή, Bootloader Σύστημα Image( boot.img, recovery.img)επαλήθευση.:

1. Επανυπολογισμός hash του συστημικού image.
2. Αποκρυπτογράφηση της υπογραφής του image με το δημόσιο κλειδί, παραγωγή hash.
3. Hash, επαλήθευση.Σύστημα Image τρίτου.

##### 🔗 Αλυσίδα ασφαλούς εκκίνησης

BL Ασφάλεια.επαλήθευση, φόρτωση(),Σύστημα.

##### 📊 Κλειδωμένο vs ξεκλείδωτο: Διπλή επίπτωση του BL Lock

BL , 5 κεντρικό Διάσταση:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 dark:border-gray-600 text-sm">
                            <thead>
                                <tr class="bg-gray-100 dark:bg-gray-800">
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Κεντρικός ρόλος</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Κλειδωμένο (προεπιλογή)</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ξεκλείδωτο</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Ασφάλεια συστήματος</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Αποτρέπει εγγραφή μη υπογεγραμμένων συστημάτων, προστατεύει ακεραιότητα<br><span class="text-emerald-600 dark:text-emerald-400">✅ Υψηλή ασφάλεια: φορτώνει μόνο επίσημα υπογεγραμμένα images</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ Ασφάλεια: επιτρέπεται τρίτου ROM, Σύστημα, Root Δικαίωμα Σύστημα</span></td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Σταθερότητα συστήματος</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Εξασφαλίζει δοκιμασμένο και βελτιστοποιημένο επίσημο σύστημα<br><span class="text-emerald-600 dark:text-emerald-400">✅ Σταθερό: επίσημο firmware, πλήρεις λειτουργίες, αξιόπιστο OTA</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ :τρίτου ROM ,Σύστημα, Λειτουργία(,),OTA ενημέρωση</span></td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Εγγύηση</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ο κατασκευαστής κλειδώνει το BL για να παρέχει σταθερό σύστημα και εγγύηση<br><span class="text-emerald-600 dark:text-emerald-400">✅ Εγγύηση ενεργή: δωρεάν επίσημη εξυπηρέτηση (μη ανθρώπινη ζημιά)</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ :Ξεκλείδωμα BL , Ξεκλείδωμα καταγραφή</span></td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Ασφάλεια δεδομένων</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Το ξεκλείδωμα συνήθως διαγράφει δεδομένα, αποτρόπαια κακή χρήση<br><span class="text-emerald-600 dark:text-emerald-400">✅ Δεδομένα Ασφάλεια: καθημερινό, BL περιορισμός Σύστημα Τροποποίηση</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ Δεδομένα: Ξεκλείδωμα Εκκαθάριση Όλοι οι χρήστες Δεδομένα; Ξεκλείδωμα Κρυπτογράφηση, Δεδομένα Αποθήκευση Ασφάλεια; Flash Δεδομένα</span></td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Περιορισμοί λειτουργιών</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Εξασφαλίζει λειτουργίες που εξαρτώνται από ασφαλές περιβάλλον (πληρωμές, τράπεζα)<br><span class="text-emerald-600 dark:text-emerald-400">✅ Πλήρεις λειτουργίες: όλες οι επίσημες λειτουργίες διαθέσιμες</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ Λειτουργία: Ασφάλεια Εφαρμογή( Google Pay, App) BL Ξεκλείδωμα απόρριψη; DRM υποβάθμιση, Βίντεο Αναπαραγωγή</span></td>
                                </tr>
                            </tbody>
                        </table>
```
:::

#### 2. unlockBL Λεπτομερής διαδικασία ξεκλειδώματος((παράδειγμα: Xiaomi))

1. <strong>Αίτημα δι και ωμάτων ξεκλειδώματος</strong>:στο Xiaomiunlock εφαρμογή μέσω ιστοσελίδας εργαλείου unlock.
2. <strong>Σύνδεση λογαριασμού</strong>:στο κινητό settings σύνδεσε Xiaomi account.
3. <strong>Περίοδος αναμονής</strong>:Βάσει επιπέδου λογαριασμού, Απαιτείται αναμονή 7-30 ημέρες.
4. <strong>Λειτουργία ξεκλειδώματος</strong>:χρησιμοποίησε Xiaomiunlock εργαλείο σύνδεσης με υπολογιστή unlock.

#### 3. Root Πολλαπλές λύσεις

- <strong>Magisk</strong>:modernRootsolution, Systemlessdesign, Μπορεί να κρυφτεί Rootstatus.
- <strong>Kernelsu</strong>:Βασισμένο σε kernelRootsolution, Πιο βαθύ, Καλύτερη απόκρυψη.
- <strong>SuperSU</strong>:establishedRootsolution, Έχει σταματήσει η ενημέρωση.

#### 4. Εισαγωγή στο flashing

Το flashing σημαίνει εγκατάσταση νέου λειτουργικού συστήματος στο κινητό.Συνηθισμένοι τύποι flashing:

- <strong>Flash επίσημου ROM</strong>:Εγκατάσταση επίσημου συστήματος, Γιά διάσωση από brick ή υποβάθμιση.
- <strong>Flash τρίτου κατασκευαστή Recovery</strong>:όπως TWRP, Γιά αντίγραφο ασφαλείας και επαναφορά, Flash τρίτου κατασκευαστή ROM.
- <strong>Flash τρίτου κατασκευαστή ROM</strong>:όπως LineageOS, Pixel Experience κ.λπ.,Δοκιμή διαφορετικών συστημάτων.

#### Πέμπτο: Samsung Knox — μη αναστρέψιμο κόστος BL Unlock

,BL Ξεκλείδωμα "":<strong>,Ξεκλείδωμα Knox, Ασφάλεια Λειτουργία(Samsung Pay);Εκκαθάριση Δεδομένα;</strong>. Συγκεκριμένα:

- <strong>Το eFuse καίγεται μία φορά</strong>: eFuse , BL Ξεκλείδωμα, επαναφορά.
- <strong>Επηρεαζόμενες λειτουργίες</strong>:Samsung Pay(/),Knox Ασφάλεια Αρχείο, επιχείρηση MDM ,Υγεία App .
- <strong>Εξαναγκαστική διαγραφή δεδομένων</strong>:Επαναφορά εργοστασιακών ρυθμίσεων, τοπικό Δεδομένα(cloud Δεδομένα).
- <strong>Επίπτωση στην εγγύηση</strong>: Επίσημα, μετά το κάψιμο του Knox δεν υπάρχει εγγύηση.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Σκεφτείτε το καλά

{class="mt-1"}
Το κάψιμο Knox της Samsung είναι <strong>μη αναστρέψιμο</strong>. Root Λειτουργία, Συμβουλές Root Λύση.
:::

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-skull-crossbones mr-2"></i>Σημαντική προειδοποίηση

{class="mt-1"}
Το flashing έχει ρίσκο, Προσοχή στις λειτουργίες.Μπορεί να προκαλέσει:

{class="list-disc pl-6 mt-1 space-y-1"}
- Το κινητό έγινε brick(Δεν ανοίγει)
- Απώλεια εγγύησης
- Απώλεια δεδομένων
- Δυσλειτουργία πληρωμών

{class="mt-1"}
Πριν το flashing κάνε οπωσδήποτε πλήρες αντίγραφο ασφαλείας, Διάβασε προσεκτικά το tutorial, Επιβεβαίωση αντιστοιχίας μοντέλου και έκδοσης.
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Προτεινόμενες πηγές

{class="list-disc pl-6 mt-1 space-y-1"}
- <strong>XDA Developers</strong>:η μεγαλύτερη κοινότητα προγραμματιστών Android παγκοσμίως, Υπάρχουν πλούσια tutorials flashing και ROMresources.
- <strong>Coolapk</strong>:Γνωστή εγχώρια ψηφιακή κοινότητα, Υπάρχουν πολλά κινεζικά tutorials και συζητήσεις.
- <strong>Φόρουμ κάθε μοντέλου</strong>:όπως κοινότητα Xiaomi, κοινότητα OnePlus κ.λπ.,Υπάρχουν επίσημα και ανεπίσημα tutorials.
:::

#### Έκτο: Συχνές ερωτήσεις (Q&amp; A)

::: div .qa-item .mt-3
{class="font-semibold mb-1"}
<i class="fas fa-question-circle text-primary mr-1"></i>Q1: Μπορεί να αναιρεθεί το BL Unlock;

{class="mb-2 pl-6"}
<strong>A:</strong>.επίσημο, FlashScript( <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">flash_all_lock.bat</code>). Ξεκλείδωμα Ασφάλεια(Knox).
:::

::: div .qa-item .mt-3
{class="font-semibold mb-1"}
<i class="fas fa-question-circle text-primary mr-1"></i>Q2: Πώς γίνεται Root μετά το Unlock;

{class="mb-2 pl-6"}
<strong>A:</strong> Το BL Unlock είναι μόνο το πρώτο βήμα. Το Root συνήθως απαιτεί:

{class="list-decimal pl-12 mb-2 space-y-1"}
1. FlashRecovery (π.χ. TWRP).
2. RecoveryMagiskRootbootImage, Root Δικαίωμα.
:::
