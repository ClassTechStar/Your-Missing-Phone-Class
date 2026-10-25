---
id: di-er-shi-zhang-jinjie
num: 20
part: jin-jie-pian
nav: Κεφάλαιο 20: Λειτουργία προγραμματιστή και προχωρημένα δι και ώματα
toc: default
kind: supplement
---

### Κεφάλαιο 20: Λειτουργία προγραμματιστή και προχωρημένα δι και ώματα

{class="chapter-intro mb-4"}
Αυτό το κεφάλαιο είναι για όσους θέλουν να εμβαθύνουν σε "κρυφές λειτουργίες". Λειτουργία προγραμματιστή, Root, BL — ακούγονται geek αλλά δεν είναι μακριά.

#### I. Λειτουργία προγραμματιστή: ξεκλειδώστε κρυφές ρυθμίσεις

Η λειτουργία προγραμματιστή είναι ένα κρυφό μενού ενσωματωμένο στο σύστημα του κινητού, που περιέχει πολλές λειτουργίες που οι απλοί χρήστες δεν χρειάζονται αλλά οι προγραμματιστές χρειάζονται.

##### Πώς να ενεργοποιήσετε:

- <strong>Android</strong>: μπείτε στις Ρυθμίσεις &gt; Σχετικά με το τηλέφωνο &gt; πατήστε συνεχόμενα τον "Αριθμό έκδοσης " 7 φορές, μέχρι να εμφανιστεί "Έχετε ενεργοποιήσει τη λειτουργία προγραμματιστή".
- <strong>HarmonyOS</strong>: Ρυθμίσεις &gt; Σχετικά με το τηλέφωνο &gt; πατήστε 7 φορές συνεχόμενα "Έκδοση HarmonyOS".
- <strong>iOS</strong>. Απλοί χρήστες δεν μπορούν, θέλει Apple Developer επί πληρωμή.

##### Συχνές λειτουργίες:

- <strong>Εντοπισμός σφαλμάτων USB</strong>:σύνδεση προηγμένος(Flash, Δεδομένα επαναφορά, ADB Εντολή),κεφάλαιο "ADB Εντολή".
- <strong>Εμφάνιση λειτουργίας αφής</strong>:Οθόνηεμφάνιση().

##### Απόδοση και ομαλότητα:

- <strong>(κλιμάκωση / κλιμάκωση / κλιμάκωση)</strong>:άνοιγμα App. προεπιλογή 1x,0.5x"" (,),απενεργοποίηση.0.5x, απενεργοποίηση, "".
- <strong>Εξαναγκασμένη απόδοση GPU (Force GPU Rendering)</strong>:2DGPUCPU.App βελτιστοποίηση, GPU Κατανάλωση ενέργειας.προεπιλογή GPU, υψηλό, Χρήστης προεπιλογή.
- <strong>εμφάνιση GPU(Profile GPU Rendering)</strong>:Οθόνη πραγματικού χρόνουεμφάνιση,16.6ms(60fps)..Προγραμματιστής App, Χρήστης App βελτιστοποίηση——App.

##### Παρασκήνιο και αυτονομία:

- <strong>Περιορισμός διεργασιών παρασκηνίου</strong>:Ρυθμίσεις "περιορισμός""1 Διεργασία ""2 Διεργασία".περιορισμός Παρασκήνιο Διεργασία Εξοικονόμηση ενέργειας, Android Παρασκήνιο, περιορισμός App φόρτωση(Κατανάλωση ενέργειας,).Debug, Συμβουλές Χρήστης ενεργοποίηση,"περιορισμός".
- <strong>Μη διατήρηση δραστηριοτήτων</strong>:. App, φόρτωση, έλεγχος App επαναφορά.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Σημειώσεις

{class="mt-1"}
Οι ρυθμίσεις της λειτουργίας προγραμματιστή μπορεί να επηρεάσουν τη σταθερότητα του συστήματος, μην αλλάζετε ό, τι δεν καταλαβαίνετε. Αφού ενεργοποιήσετε USB debugging, προσέξτε όταν συνδέεστε με υπολογιστή, μην συνδέεστε σε μη αξιόπιστους υπολογιστές.
:::

#### Δεύτερο: OEM Unlocking — ο «διακόπτης flash» στις επιλογές προγραμματιστή

Προγραμματιστής——"OEM Ξεκλείδωμα " (Μάρκα"OEM Ξεκλείδωμα επιτρέπεται ""Συσκευή Ξεκλείδωμα ").Ξεκλείδωμα BL,"":άνοιγμα, επιτρέπεται fastboot Εντολή Μάρκα Ξεκλείδωμα BL.

- <strong>Ρόλος του διακόπτη</strong>:", επιτρέπεται Ξεκλείδωμα BL".απενεργοποίηση, Ξεκλείδωμα BL Εντολήαπόρριψη.
- <strong>Σχέση με το BL lock</strong>:OEM Ξεκλείδωμα "",BL Ξεκλείδωμα "".Ρυθμίσεις, Ξεκλείδωμα, fastboot Εντολή( <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">fastboot flashing unlock</code>), και τα δύο απαραίτητα.
- <strong>Επαναφορά εργοστασιακών τιμών;</strong>:."OEM Ξεκλείδωμα"επαναφορά απενεργοποίηση, BL Ξεκλείδωμα φυσικό, επαναφορά——χειροκίνητο <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">fastboot flashing lock</code> για ξανακλείδωμα.
- <strong>Πότε πρέπει να ανοίξει</strong>:Επιβεβαίωση FlashRoot, απενεργοποίηση."USBDebug",Flash άνοιγμα.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Γνώση: Γιατί οι κατασκευαστές βάζουν αυτόν τον διακόπτη

{class="mt-1"}
,Δικαίωμα Σύστημα.Google Προγραμματιστής "OEM Ξεκλείδωμα","Χρήστης"επιβεβαίωση.BL, OEM Ξεκλείδωμα απενεργοποίηση, Flash.
:::

#### Τρίτο: BL Lock (Bootloader Lock) — η πρώτη πόρτα του flash

Το Bootloader φορτώνει το λειτουργικό κατά την εκκίνηση. Το κλείδωμα BL είναι κλείδωμα ασφαλείας των κατασκευαστών, για να αποτρέψουν την εγκατάσταση μη επίσημων συστημάτων.

##### Ο ρόλος του κλειδώματος BL:

- <strong>Προστασία ασφαλείας</strong>. Αποτρέπει κακόβουλο flash.
- <strong>Αντικλοπή</strong>: Ακόμα και μετά flash, χωρίς αρχικό κωδικό δεν λειτουργεί.
- <strong>Περιορισμός εγγύησης</strong>. Ξεκλείδωμα BL = απώλεια εγγύησης.

##### Πολιτικές κλειδώματος Bootloader ανά επωνυμία:

- <strong>Xiaomi</strong>: Ξεκλειδώνει, απαιτεί λογαριασμό και αναμονή (7-30 μέρες).
- <strong>Huawei</strong>: από το 2018 σταμάτησε τους κωδικούς, σχεδόν αδύνατο ξεκλείδωμα.
- <strong>OnePlus</strong>: Ξεκλειδώνει, πιο χαλαρά.
- <strong>OPPO/vivo</strong>. Κάποια μοντέλα με αίτημα.
- <strong>Samsung</strong>: Ξεκλειδώνει, αλλά Knox fuse, χάνετε Samsung Pay.
- <strong>Apple</strong>: iOS χωρίς παραδοσιακό BL αλλά παρόμοιο ασφάλειας.

#### Τέταρτο: Πρακτικές εντολές ADB — έλεγχος κινητού μέσω υπολογιστή

ADB Android Debug Bridge(Debug), Google επίσημο Εντολή, USB Wi-Fi . Root,"USBDebug".""——Flash, App, Αρχείο, .

##### Πώς να συνδέσετε μέσω USB:

1. Στο κινητό: Επιλογές προγραμματιστή → Ενεργοποίηση «USB Debugging».
2. : Google επίσημο Λήψη Platform Tools( <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb</code> και <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">fastboot</code> δύο εκτελέσιμα), αποσυμπιέστε σε οποιονδήποτε φάκελο.
3. Καλώδιο δεδομένων σύνδεση,"επιτρέπεται USBDebug","επιτρέπεται"Επιβεβαίωση.
4. Εντολή(Windows PowerShell cmd) <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb devices</code>, αν η έξοδος μοιάζει <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">List of devices attached / xxxxxxxx device</code>, έχει συνδεθεί.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Μην αγνοείτε drivers και popup εξουσιοδότησης

{class="mt-1"}
Χρήστες Windows αν <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb devices</code> εμφάνιση "unauthorized" Συσκευή, Driver"επιτρέπεται "./Μάρκα"USBDriver"""Driver; Mac Linux . Καλώδιο δεδομένων.
:::

##### Συχνές εντολές ADB:

- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb install app.apk</code>: Εγκατάσταση APK από υπολογιστή (<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-r</code> σημαίνει επανεγκατάσταση με διατήρηση δεδομένων·<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-s</code> εγκατάσταση σε SD card).
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb uninstall com.xxx.xxx</code>: Απεγκατάσταση εφαρμογής με όνομα πακέτου.
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb push διαδρομή_υπολογιστή /sdcard/προορισμός</code>: Αποστολή αρχείου σε κινητό.
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb pull /sdcard/αρχείο διαδρομή_υπολογιστή</code>: Λήψη αρχείου σε υπολογιστή (πολύ πιο γρήγορο από WeChat).
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell</code>: Είσοδος στο Linux shell του κινητού, απευθείας εκτέλεση <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">ls</code>,<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pm</code>,<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">am</code> εντολών.
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb reboot bootloader</code>: Επανεκκίνηση σε Fastboot (είσοδος flash).
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb reboot recovery</code>: Επανεκκίνηση σε Recovery.
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm list packages</code>: Λίστα όλων των εγκατεστημένων πακέτων. Προσθέστε <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-s</code> για εφαρμογές συστήματος, <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-3</code> για εφαρμογές τρίτων.
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm uninstall --user 0 όνομα_πακέτου</code>: Απεγκατάσταση προεγκατεστημένης εφαρμογής για τρέχοντα χρήστη, χωρίς Root.

##### Πρακτική: Απεγκατάσταση προεγκατεστημένων χωρίς Root:

Αυτή είναι μια από τις πιο πρακτικές χρήσεις του ADB: με <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pm uninstall --user 0</code> Εντολή "Χρήστης"απεγκατάσταση App, Root, Σύστημα.απεγκατάσταση App Σύστημα "",Σύστημα, Επαναφορά εργοστασιακών ρυθμίσεων.

1. Πρώτα με <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm list packages -s</code> εμφανίστε όλες τις εφαρμογές συστήματος και βρείτε το όνομα πακέτου. π.χ. του browser Xiaomi είναι <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.browser</code>, του Huawei AppGallery είναι <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.vmall.client</code>.
2. Δεν είστε σίγουροι ποια εφαρμογή αντιστοιχεί σε ποιο πακέτο; Στον υπολογιστή χρησιμοποιήστε <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm list packages | findstr λέξη-κλειδί</code> αναζήτηση, τρίτου App "Package Viewer"Προβολή App .
3. Εκτέλεση απεγκατάστασης:<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm uninstall --user 0 όνομα_πακέτου</code>, π.χ. <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm uninstall --user 0 com.android.browser</code>. Επιστρέφει <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">Success</code> — επιτυχία.
4. επαναφορά?:① Επαναφορά εργοστασιακών ρυθμίσεων();② εγκατάσταση:<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell cmd package install-existing όνομα_πακέτου</code>.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-skull-crossbones mr-2"></i>Ποτέ μην διαγράφετε κρίσιμα πακέτα συστήματος

{class="mt-1"}
"pm uninstall --user 0" Root Ασφάλεια, Σύστημα Εφαρμογή( <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.systemui</code> Γραμμή κατάστασης,<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.phone</code> Τηλέφωνο,<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.settings</code> Ρυθμίσεις)Σύστημα, . Google "". Συμβουλές, επιβεβαίωση.
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Γνώση: Τι σημαίνει --user 0

{class="mt-1"}
4.2 Χρήστης, Χρήστης ID( 0, Χρήστης 10 ).<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">--user 0</code> "απεγκατάσταση ",Σύστημα APK Αρχείο, εμφάνιση. Root——Σύστημα Αρχείο,"Χρήστηςρύθμιση". Root απεγκατάσταση: Root απεγκατάσταση Σύστημα, Όλοι οι χρήστες; ADB απεγκατάσταση "Χρήστης απόκρυψη".
:::

#### Πέμπτο: Root — ο «υπερ διαχειριστής» του Android

Root Δικαίωμα Linux Χρήστης(/Πίνακας περιεχομένων, Αρχείο),Σύστημα Δικαίωμα.WindowsAdministrator:Windows Ασφάλεια Διαχειριστής περιορισμός(Δικαίωμα TrustedInstaller), Administrator Linux root <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">sudo rm -rf /*</code>.Root Δικαίωμα, Τροποποίηση Σύστημα Αρχείο, απεγκατάσταση Εφαρμογή, Root προηγμένος App.

##### Πλεονεκτήματα του Root:

- Απεγκατάσταση προεγκατεστημένων εφαρμογών που δεν απεγκαθίστανται.
- Χρήση App προχωρημένων λειτουργιών (π.χ. Titanium Backup, Greenify).
- Τροποποίηση διεπαφής και λειτουργιών συστήματος.
- εγκατάσταση τρίτου Recovery και προσαρμοσμένης ROM.

##### Κίνδυνοι του Root:

- <strong>Απώλεια εγγύησης</strong>: Οι περισσότεροι δεν καλύπτουν Root.
- <strong>Κίνδυνος ασφαλείας</strong>: Κακόβουλες App με Root, σοβαρές συνέπειες.
- <strong>Αστάθεια συστήματος</strong>. Λάθος = crash.
- <strong>Οι τραπεζικές App δεν λειτουργούν</strong>: Πολλές τραπεζικές App δεν τρέχουν με Root.
- <strong>Αποτυχία ενημέρωσης OTA</strong>: Ίσως δεν δέχεται επίσημα updates.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-skull-crossbones mr-2"></i>Σοβαρή προειδοποίηση

{class="mt-1"}
Η διαδικασία Root έχει ρίσκο, μπορεί να κάνει το κινητό "τούβλο". Αν είστε αρχάριος, ενημερωθείτε επαρκώς και έχετε πλήρες αντίγραφο. Διαβάστε προσεκτικά τον οδηγό και επιβεβαιώστε το μοντέλο και την έκδοση συστήματος.
:::

#### 6. Πιστοποίηση SafetyNet και Play Integrity: Γιατί οι τραπεζικές εφαρμογές δεν λειτουργούν μετά το Root

Root Χρήστης:RootModule, άνοιγμα App——"Συσκευή Ασφάλεια,",Google Pay, Netflix απόρριψη Αναπαραγωγή.Google Συσκευή: SafetyNet Play Integrity API.

##### Τι είναι το SafetyNet / Play Integrity:

- <strong>SafetyNet Attestation (παλαιά έκδοση, από το 2017)</strong>:Google Συσκευή API, Εφαρμογή Google Διακομιστής "Συσκευή CTS έλεγχος, Τροποποίηση επίσημο".Επιστροφή Basic Attestation(βασικό) Strong Attestation(,).Google SafetyNet 2024 .
- <strong>Play Integrity API (νέα έκδοση, από 2022)</strong>:Google Λύση, SafetyNet .Συσκευή,"Εφαρμογή " (App )"/Εξουσιοδότηση" (Χρήστης Google ). App μεταφορά Play Integrity.
- <strong>Ποιος το χρησιμοποιεί</strong>:, App( Google Pay, /Σενάριο),(Netflix ),(/),επιχείρηση App(MDM Συσκευή).

##### Τρία επίπεδα αποτελεσμάτων Play Integrity:

- <strong>MEETS_DEVICE_INTEGRITY(Συσκευή)</strong>:Συσκευή Android Σύστημα, Bootloader Ξεκλείδωμα, Root, CTS έλεγχος., App.
- <strong>MEETS_BASIC_INTEGRITY (βασική ακεραιότητα)</strong>:Συσκευή. App υποβάθμιση( Netflix Αναπαραγωγή περιορισμός), App απόρριψη.
- <strong>MEETS_STRONG_INTEGRITY (ισχυρή ακεραιότητα)</strong>:προηγμένος,( Google Pixel Titan M ),τρίτου Μάρκα Root .
- <strong>Καμία ετικέτα (NO_INTEGRITY)</strong>:Συσκευή Root, Ξεκλείδωμα BL, τρίτου ROM αναλογικό,/ App απόρριψη.

##### Γιατί μετά από Root αυτές οι εφαρμογές δεν δουλεύουν:

Εφαρμογή Play Integrity API Google Διακομιστής, Google Συσκευή——Bootloader Κλείδωμα, Σύστημα Τροποποίηση, su Αρχείο, SELinux .Επιστροφή, App "Συσκευή Ασφάλεια",απόρριψη.

##### απόκρυψη Λύση: Magisk Hide / Shamiko / Zygisk:

Root App,"απόκρυψη Root "Λύση.Κεντρική ιδέα: Τροποποίηση Σύστημα,""Συσκευή.

- <strong>Magisk</strong>:κύριο Systemless Root Λύση——Τροποποίηση Σύστημα, Root. OTA ενημέρωση, απεγκατάσταση, απόκρυψη Λύσηβασικό. Magisk Ξεκλείδωμα BL .
- <strong>Magisk Hide (έχει διακοπεί)</strong>:Magisk απόκρυψη Module, App απόκρυψη Root. 2021 Magisk επίσημο, Google αναβάθμιση,"".
- <strong>Zygisk</strong>:Magisk 24.0+ , Riru, Zygote Διεργασία Module φόρτωση, Τροποποίηση Σύστημα.ενεργοποίηση Zygisk απόκρυψη Λύση.
- <strong>Shamiko</strong>:κύριοαπόκρυψη Module, Zygisk , App("")απόκρυψη Root, απόκρυψη Magisk , Bootloader Κλείδωμα.Shamiko LSPosed GitHub .
- <strong>Play Integrity Fix(osm0sis)</strong>: Google Play Integrity Magisk Module, Τροποποίηση Συσκευή(fingerprint) Google Συσκευή Root επίσημο.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Το παιχνίδι γάτας-ποντικιού δεν τελειώνει ποτέ

{class="mt-1"}
Google ενημέρωση, App αναβάθμιση Play Integrity .απόκρυψη Λύση. / App(καθημερινό,),: Root, BL .απόκρυψη Λύση " Root + Root"ρύθμιση.
:::

#### Έβδομο: Συμβουλές για απλούς χρήστες

- <strong>Λειτουργία προγραμματιστή</strong>:ενεργοποίηση, Επιτάχυνση, GPU Λειτουργία.
- <strong>OEM Unlocking και BL Lock</strong>:Flash Root, προεπιλογή(απενεργοποίηση)Ασφάλεια.
- <strong>ADB</strong>: Ισχυρό εργαλείο χωρίς Root, χρήσιμο και για απλούς χρήστες — π.χ. με <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pm uninstall --user 0</code> απεγκατάσταση προεγκατεστημένων. Πριν διαγράψετε, ελέγξτε αν μπορεί να διαγραφεί.
- <strong>Root</strong>:Χρήστης Συμβουλές Root. Λειτουργία, Root Λύση( ADB απεγκατάσταση, Shizuku Root Λειτουργία).

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Δοκιμή: ενεργοποιήστε λειτουργία προγραμματιστή και ρυθμίστε ταχύτητα κινουμένων σχεδίων

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Μεταβείτε στα Ρυθμίσεις &gt; Σχετικά με το τηλέφωνο.
2. Πατήστε "Αριθμός έκδοσης" 7 φορές, μέχρι να ανοίξει.
3. Επιστρέψτε στις ρυθμίσεις, βρείτε "Επιλογές προγραμματιστή " (συνήθως κάτω ή στο "Σύστημα").
4. Βρείτε "Κλίμακα κίνησης παραθύρου ", "Κλίμακα κίνησης μετάβασης ", "Κλίμακα διάρκειας κινούμενου προγράμματος", ρυθμίστε τα όλα σε 0.5x ή απενεργοποιήστε.
5. Νιώστε αν το κινητό έγινε πιο γρήγορο.
:::
