---
id: di-san-shi-jiu-zhang
num: 39
part: ai-biancheng-pian
nav: Κεφάλαιο 39: Μηχανική συμφραζομένων — κάνε την AI να καταλαβαίνει τι θέλεις
toc: default
kind: chapter
---

### Κεφάλαιο 39: Μηχανική συμφραζομένων — να καταλαβαίνει η AI τι εννοείς

{class="chapter-intro mb-4"}
Έχεις ποτέ ζήσει αυτό: ανοίγεις ένα νέο παράθυρο συνομιλίας και η AI, σαν να έχασε τη μνήμη της, έχει ξεχάσει όλα τα βασικά για το project σου; Δεν το κάνει επίτηδες για να σε εκνευρίσει — απλώς είναι «ξεχασιάρα» εκ φύσεως. Σε αυτό το κεφάλαιο θα μάθεις να εφοδιάζεις την AI με ένα «σύστημα μακροχρόνιας μνήμης» και, παράλληλα, θα γνωρίσεις ένα από τα πιο δημοφιλή παραδείγματα ανάπτυξης του 2026 — την ανάπτυξη με βάση προδιαγραφές (spec-driven development).

#### 1. Το αρχείο μνήμης project: η «μακροχρόνια μνήμη» της AI

Τα μοντέλα AI έχουν έναν θεμελιώδη περιορισμό: η μνήμη τους είναι «βραχυχρόνια». Κάθε φορά που ξεκινά συνομιλία, η AI ξέρει μηδέν για το project σου. Χρειάζεται να της λες ξανά και ξανά μέσα στη συνομιλία «χρησιμοποιούμε React», «το backend είναι Node.js», «η βάση δεδομένων είναι PostgreSQL», «στο στυλ κώδικα βάζουμε διπλά εισαγωγικά». Αυτό όχι μόνο είναι αναποτελεσματικό, αλλά εύκολα ξεχνάς κάτι — σαν να κάνεις κάθε μέρα από την αρχή onboarding σε έναν νέο συνάδελφο.

Η λύση είναι το «αρχείο μνήμης project» — ένα απλό αρχείο κειμένου στη ριζική βιβλιοθήκη του project, που τα εργαλεία AI διαβάζουν αυτόματα σε κάθε έναρξη συνομιλίας. Κάθε εργαλείο έχει τη δική του σύμβαση ονομασίας:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Εργαλείο</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Όνομα αρχείου</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cursor</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.cursorrules</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Code</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">CLAUDE.md</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GitHub Copilot</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">copilot-instructions.md</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Γενική λύση</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">AGENTS.md</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Συμβάσεις ονομασίας αρχείων μνήμης project ανά εργαλείο

Αν και τα ονόματα διαφέρουν, η αρχή είναι η ίδια: γράφεις σε αυτό το αρχείο ό, τι θέλεις η AI να «θυμάται πάντα». Ένα καλό αρχείο μνήμης project πρέπει να περιλαμβάνει: σύνοψη του project (τι είναι αυτό το project), τεχνολογικό stack (ποια τεχνολογία χρησιμοποιείται), κανόνες κώδικα (ονοματοδοσία, εσοχές, στυλ σχολίων), δομή φακέλων (πώς οργανώνεται ο κώδικας), συμφωνίες ανάπτυξης (στρατηγική branches, κανόνες commits, απαιτήσεις tests). Το CLAUDE.md του Karpathy είναι μόλις 70 γραμμές, αλλά καλύπτει όλες τις κρίσιμες πληροφορίες — σύντομο και συνολικό.

::: div .code-block
:::inline div .code-head
<span>CLAUDE.md</span><span class="dots">···</span>
:::

```
# Έργο: εφαρμογή προσωπικού λογιστηρίου
## Επισκόπηση
Μια full-stack εφαρμογή προσωπικού λογιστηρίου που βοηθά την καταγραφή καθημερινών εσόδων-εξόδων.
## Τεχνολογίες
- Frontend: React + TypeScript + Tailwind CSS
- Backend: Node.js + Express + TypeScript
- Βάση δεδομένων: SQLite (ανάπτυξη) / PostgreSQL (παραγωγή)
- Τεστ: Vitest
## Κανόνες κώδικα
- Διπλά εισαγωγικά
- Εσοχή 2 κενών
- Ονόματα συναρτήσεων σε camelCase
- Ορισμοί τύπων σε PascalCase
- Κάθε συνάρτηση με σχόλιο JSDoc
## Δομή φακέλων
/src
  /frontend  - κώδικας frontend
  /backend   - κώδικας backend
  /shared    - κοινοί τύποι
  /tests     - αρχεία τεστ
## Συμφωνίες ανάπτυξης
- Μηνύματα commit στα κινεζικά
- Νέα λειτουργία με τεστ πριν την υλοποίηση
- Το API απαντά πάντα με μορφή { success, data, error }
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Προσοχή: μην το γράψεις σαν «δεύτερο έγγραφο απαιτήσεων»

{class="mt-1"}
Πρόσεξε το μέγεθος του αρχείου — μην το γράψεις σαν έγγραφο απαιτήσεων δεκάδων σελίδων. Ο σκοπός του αρχείου μνήμης project είναι να «χτίζει γρήγορα την επίγνωση πλαισίου» στην AI, όχι να «περιγράφει αναλυτικά κάθε λειτουργία». Κράτα το σύντομο, δομημένο, και γράψε μόνο «ό, τι χρειάζεται να ξέρει η AI».
:::

#### 2. Ανάπτυξη με βάση προδιαγραφές (SDD)

Το Spec-Driven Development (SDD, ανάπτυξη με βάση προδιαγραφές) είναι ένα παράδειγμα ανάπτυξης που ωρίμασε σταδιακά το 2026. Η βασική ιδέα σε μία πρόταση: πρώτα γράφεις τις προδιαγραφές, μετά τον κώδικα. Σε αντίθεση με το παραδοσιακό TDD (ανάπτυξη με βάση tests), οι «προδιαγραφές» του SDD δεν είναι μόνο test cases, αλλά περιλαμβάνουν περιγραφή απαιτήσεων, ορισμούς διεπαφών (interfaces), μοντέλα δεδομένων κ.ά. Η AI παράγει κώδικα με βάση αυτές τις προδιαγραφές, και ο ρόλος του ανθρώπου είναι να τις γράφει και να τις συντηρεί.

Η ροή εργασίας του SDD έχει πέντε βήματα:

1. Περιγράφεις τις προδιαγραφές των απαιτήσεων σε φυσική γλώσσα (σε ένα αρχείο .md)·
2. Ορίζεις τις διεπαφές και τις δομές δεδομένων (μέσα στο αρχείο προδιαγραφών)·
3. Ζητάς από την AI να παράγει την υλοποίηση με βάση τις προδιαγραφές·
4. Τρέχεις tests για να ελέγξεις αν το αποτέλεσμα συμμορφώνεται με τις προδιαγραφές·
5. Αν δεν συμμορφώνεται, διορθώνεις τις προδιαγραφές ή ζητάς από την AI να διορθώσει τον κώδικα.

Σε αυτή τη ροή, το αρχείο προδιαγραφών είναι η «μοναδική πηγή αλήθειας» — τον κώδικα μπορείς να τον ξαναπαράγεις, αλλά οι προδιαγραφές πρέπει πρώτα να είναι σωστές.

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> Σύνταξη αρχείου προδιαγραφών</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> Είναι πλήρεις οι προδιαγραφές;</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> Πλήρες</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-robot mr-1"></i> Το AI γράφει κώδικα από προδιαγραφές</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> Εκτέλεση τεστ για επαλήθευση αποτελέσματος</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-times-circle mr-1"></i> Ατελές / αποτυχία τεστ</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-tools mr-1"></i> Πρόβλημα κώδικα → φτιάξε κώδικα· πρόβλημα προδιαγραφών → φτιάξε προδιαγραφές</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> Πίσω στον έλεγχο</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> Όλα πέρασαν → παράδοση</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Σχήμα 3: Ροή εργασίας της ανάπτυξης με βάση προδιαγραφές (SDD)
:::

Το πλεονέκτημα του SDD είναι ότι το αρχείο προδιαγραφών είναι πιο σταθερό από τον κώδικα. Όταν αλλάξει το υποκείμενο μοντέλο ή εργαλείο, οι προδιαγραφές σου παραμένουν έγκυρες — αρκεί να ζητήσεις από το νέο εργαλείο AI να ξαναπαράγει τον κώδικα. Εδώ ακριβώς βρίσκεται και η έμφαση του βιβλίου ότι «η μεθοδολογία μετράει περισσότερο από τα εργαλεία» — το αρχείο προδιαγραφών είναι ο χειροπιαστός φορέας της μεθοδολογίας σου.

#### 3. Διαχείριση του παραθύρου συμφραζομένων

Ακόμα κι αν έχεις αρχείο μνήμης project, στη συνομιλία θα συνεχίσεις να συναντάς το πρόβλημα του «δεν φτάνουν τα συμφραζόμενα». Το παράθυρο συμφραζομένων ενός μοντέλου AI (η ποσότητα πληροφορίας που επεξεργάζεται ταυτόχρονα) είναι πεπερασμένο. Όταν η συνομιλία μακραίνει πολύ ή παραπέμπεις σε πολλά αρχεία, η AI «ξεχνά» τις πρώτες πληροφορίες και η ποιότητα της παραγωγής πέφτει — σαν να συνομιλείς έξι ώρες με έναν φίλο, που έχει προ πολλού ξεχάσει τι σου είπες πρώτο-πρώτο στην αρχή.

Η βασική στρατηγική διαχείρισης του παραθύρου συμφραζομένων είναι η «στρωματωμένη παραπομπή»:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Στρώμα συμφραζομένων</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Περιεχόμενο</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Τρόπος διαχείρισης</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Πρώτο στρώμα: μνήμη project</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Τεχνολογικό stack, κανόνες, δομή φακέλων</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Γράφεται σε αρχεία όπως το CLAUDE.md, φορτώνεται αυτόματα, χωρίς επαναλήψεις</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Δεύτερο στρώμα: παραπομπές σε αρχεία</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Τα αρχεία κώδικα που αφορούν την τρέχουσα εργασία</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ακριβείς παραπομπές με το σύμβολο @, χωρίς να επικολλάς ολόκληρα κείμενα στη συνομιλία</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Τρίτο στρώμα: συμφραζόμενα συνομιλίας</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Το ιστορικό συνομιλίας της τρέχουσας εργασίας</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ανοίγεις νέα συνομιλία μετά από κάθε εργασία, για να μην φουσκώνουν τα συμφραζόμενα</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Τέταρτο στρώμα: άμεσες οδηγίες</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Οι συγκεκριμένες απαιτήσεις αυτού του βήματος</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Καθαρές, σύντομες, στοχευμένες — χωρίς μακροσκελείς περιγραφές</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Στρωματωμένη στρατηγική διαχείρισης του παραθύρου συμφραζομένων

#### 4. Πρακτικά σημεία της μηχανικής συμφραζομένων

Η μηχανική συμφραζομένων δεν είναι μια εφάπαξ ρύθμιση, αλλά μια συνεχής διαδικασία βελτίωσης. Ιδού μερικά σημεία που έχουν επανειλημμένα αποδειχθεί στην πράξη:

1. Ενημερώνεις το αρχείο μνήμης συγχρόνως με την εξέλιξη του project. Όταν υιοθετείς νέα τεχνολογία ή αλλάζεις αρχιτεκτονική, ενημερώνεις πρώτο-πρώτο το αρχείο μνήμης, αντί να το εξηγείς πρόχειρα μέσα στη συνομιλία.
2. Χρησιμοποιείς έξυπνα παραπομπές @ αντί για επικόλληση ολόκληρων κειμένων. Τα περισσότερα εργαλεία προγραμματισμού με AI υποστηρίζουν σύνταξη @file ή @folder: εισάγουν το περιεχόμενο του αρχείου στα συμφραζόμενα της AI στο παρασκήνιο — πιο αποδοτικά από το χειροκίνητο paste και χωρίς να «λερώνουν» τη συνομιλία.
3. Οι συνομιλίες θέλουν «κοντές και πυκνές». Μια συνομιλία αναλαμβάνει μόνο μία εργασία ή ένα σημείο-λειτουργία. Όταν τελειώσεις, ανοίγεις νέα συνομιλία για την επόμενη. Οι μεγάλες συνομιλίες όχι μόνο καταναλώνουν το παράθυρο συμφραζομένων, αλλά αποσπούν και την προσοχή της AI.
4. «Δείχνεις» στην AI το αποτέλεσμα αντί να το «περιγράφεις». Όταν πέσεις πάνω σε bug, παραπέμπεις με @ απευθείας το log του σφάλματος στην AI, αντί να το περιγράφεις με δικά σου λόγια («κάποιο λάθος βγάζει περίπου»). Για την AI, το να δει την αρχική πληροφορία είναι πολύ πιο αποδοτικό από το να δει τη δική σου διατύπωση.
5. Τακτικός καθαρισμός και αρχειοθέτηση. Οι ολοκληρωμένες συνομιλίες και τα προσωρινά αρχεία καταλαμβάνουν χώρο εργασίας. Καθαρίζεις τακτικά ό, τι δεν χρειάζεται και κρατάς τον φάκελο του project τακτοποιημένο — έτσι και η AI κατανοεί πιο αποδοτικά τη δομή του project.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Πάμε στα πρακτικά: γράψε ένα αρχείο μνήμης 70 γραμμών για το project σου

{class="mt-1"}
Διάλεξε ένα project που κάνεις τώρα (ή σκοπεύεις να ξεκινήσεις) και γράψε ένα CLAUDE.md: σύνοψη project (2-3 προτάσεις), τεχνολογικό stack (φτιάξε λίστα), κανόνες κώδικα (3-5 σημεία), δομή φακέλων (σχέδιο δέντρου), συμφωνίες ανάπτυξης (2-3 σημεία). Μείνε κάτω από 70 γραμμές — μόλις το γράψεις, θα διαπιστώσεις ότι και η δική σου κατανόηση του project έγινε πολύ πιο καθαρή.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Σύνοψη κεφαλαίου

- Η μνήμη της AI είναι «βραχυχρόνια»: σε κάθε νέα συνομιλία ξέρει μηδέν για το project
- Το αρχείο μνήμης project (CLAUDE.md κ.ά.) είναι η «μακροχρόνια μνήμη» της AI και φορτώνεται αυτόματα σε κάθε συνομιλία
- Καλό αρχείο μνήμης = σύνοψη + τεχνολογικό stack + κανόνες + δομή φακέλων + συμφωνίες· αρκούν 70 γραμμές
- SDD — ανάπτυξη με προδιαγραφές: πρώτα προδιαγραφές, μετά κώδικας· οι προδιαγραφές είναι η «μοναδική πηγή αλήθειας» και πιο σταθερές από τον κώδικα
- Τα συμφραζόμενα διαχειρίζονται σε τέσσερα στρώματα: μνήμη project → @αρχεία → ιστορικό συνομιλίας → άμεσες οδηγίες
- Πέντε πρακτικά σημεία: συγχρονισμένη ενημέρωση, παραπομπές @, σύντομες συνομιλίες, αρχική πληροφορία αντί για περιγραφή, τακτικός καθαρισμός
:::
