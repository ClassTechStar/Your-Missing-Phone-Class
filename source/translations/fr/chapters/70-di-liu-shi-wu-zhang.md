---
id: di-liu-shi-wu-zhang
num: 65
part: ios-kai-fa-pian
nav: Chapitre 65 : Projet 1 — Mon carnet de comptes (version locale)
toc: default
kind: chapter
---

### Chapitre 65 : Projet 1 — mon carnet de comptes (version locale)

{class="chapter-intro mb-4"}
Bienvenue dans ton premier « vrai projet ». Ce carnet de comptes ne va pas sur Internet, mais il a tout d'un grand : enregistrer une écriture, consulter le relevé, faire les statistiques par mois, supprimer et corriger. En l'achevant, tu auras parcouru d'un bout à l'autre le cycle complet « données → logique → interface ». Ne te hâte pas pour copier le code — réfléchis d'abord, agis ensuite : c'est notre principe de toujours.

#### 1. Réfléchir aux besoins : commencer par cinq questions

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Élément</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Réponse</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who (pour qui ?)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pour soi ; famille et amis conviennent aussi</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What (quoi faire ?)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Saisir dépenses et revenus, consulter le relevé, résumés mensuels, statistiques par catégorie</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why (pourquoi ?)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">S'entraîner + comprendre où passe l'argent</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How (comment ?)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift + SwiftUI + SwiftData + MVVM, 100 % local, sans backend</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint (contraintes)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Terminer en une semaine ; iOS 17 au minimum (le seuil de SwiftData)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Les cinq éléments du cahier des charges du carnet de comptes

Découpe ensuite en petites étapes « utilisables à chaque pas » : ① bâtir la couche données SwiftData (savoir stocker une écriture) ; ② la page liste (voir le relevé) ; ③ la fenêtre de saisie (ajouter une écriture) ; ④ suppression et édition ; ⑤ la carte de synthèse mensuelle. À chaque étape bouclée, l'App reste « quelque chose d'utilisable ».

#### 2. La couche données : un toit pour les « écritures »

Définis d'abord à quoi ressemble une écriture — assez de champs, mais sans gloutonnerie :

::: div .code-block
:::inline div .code-head
<span>SWIFT · Record.swift (modèle)</span><span class="dots">···</span>
:::

```
import SwiftData

@Model
class Record {
    var type: String      // "income" revenu | "expense" dépense
    var amount: Double    // montant (yuan)
    var category: String  // catégorie : repas, transport, salaire…
    var note: String      // note (facultatif)
    var date: Date        // date de l'opération

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
Astuce : pourquoi un Double pour les montants ?

{class="mt-1"}
Une App financière rigoureuse emploie Decimal (décimal exact) pour esquiver les erreurs de virgule flottante (le vieux problème 0,1+0,2≠0,3). Pour un projet d'entraînement, Double suffit ; si un jour tu bâtis un vrai produit financier, pense à passer à Decimal ou à un « Int exprimé en centimes » — c'est un piège où d'innombrables aînés sont tombés.
:::

#### 3. MVVM : l'interface et la logique « font ménage à part »

Laisser l'interface manipuler directement la base ? Ça tourne, mais le code de l'interface devient long et pénible. L'architecture MVVM fait régner chacun à son poste : la View (interface) ne fait que dessiner, le ViewModel (centre logique) gère les données, le Model (SwiftData) gère le stockage.

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> Vue (interface SwiftUI)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> ViewModel (centre logique @Observable)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-database mr-1"></i> Model (couche de données SwiftData)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figure 4 : la structure à trois étages de MVVM — les données coulent dans un seul sens, aucune couche ne dépasse chez les autres
:::

::: div .code-block
:::inline div .code-head
<span>SWIFT · RecordViewModel.swift (squelette)</span><span class="dots">···</span>
:::

```
import Observation

@Observable
class RecordViewModel {
    var records: [Record] = []
    private let context: ModelContext

    init(context: ModelContext) { self.context = context }

    func load() {
        // filtre avec #Predicate de SwiftData + tri
        let descriptor = FetchDescriptor<Record>(
            sortBy: [SortDescriptor(\.date, order: .reverse)]
        )
        records = (try? context.fetch(descriptor)) ?? []
    }

    func add(type: String, amount: Double, category: String, note: String) {
        let r = Record(type: type, amount: amount, category: category, note: note)
        context.insert(r)
        try? context.save()
        load()                       // recharge ; l'interface se rafraîchit
    }

    func delete(_ record: Record) {
        context.delete(record)
        try? context.save()
        load()
    }
}
```
:::

Dans l'interface, écris @State private var vm = RecordViewModel(...), puis rends la liste directement avec vm.records — dès que les données bougent, l'interface se rafraîchit toute seule.

#### 4. L'interface : page liste + fenêtre de saisie

::: div .code-block
:::inline div .code-head
<span>SWIFT · Écran de liste des dépenses (extrait clé)</span><span class="dots">···</span>
:::

```
struct RecordListView: View {
    @State private var vm: RecordViewModel
    @State private var showAdd = false

    var body: some View {
        NavigationStack {
            List {
                Section("Solde du mois") {          // carte de synthèse
                    SummaryRow(records: vm.records)
                }
                Section("Transactions") {
                    ForEach(vm.records) { r in
                        RecordRow(record: r)
                    }
                    .onDelete { idx in
                        idx.forEach { vm.delete(vm.records[$0]) }
                    }
                }
            }
            .navigationTitle("Mon registre de dépenses")
            .toolbar {
                Button { showAdd = true } label: {
                    Image(systemName: "plus")
                }
            }
            .sheet(isPresented: $showAdd) {
                AddRecordView(vm: vm)          // formulaire d'ajout
            }
        }
    }
}
```
:::

Points clés de la fenêtre de saisie : pour le champ du montant, clavier .keyboardType(.decimalPad) (clavier numérique) ; dépense/revenu via un contrôle segmenté (Picker) ; catégorie choisie dans un menu ; au tap sur « Enregistrer », appelle vm.add(...) puis dismiss() pour refermer la fenêtre.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Attention : ne fais pas l'économie de la validation des saisies

{class="mt-1"}
Le champ du montant doit impérativement être validé : valeurs vides, négatives, saisies illégales du genre "abc" doivent être barrées (teste avec Double(text), qui renvoie nil en cas d'échec). Une des causes les plus banales de plantage d'une App, c'est de « croire que ce que l'utilisateur tape est un enfant sage ». Retiens : tout ce que l'utilisateur saisit doit être inspecté comme un ennemi.
:::

#### 5. Éditer, supprimer et résumer

- Suppression : .onDelete de List pour glisser vers la gauche et effacer + fenêtre de confirmation (la suppression par mégarde est ce que les utilisateurs d'Apps de comptes détestent le plus au monde) ;
- Édition : taper une ligne ouvre la fenêtre d'édition préremplie avec les valeurs d'origine (corriger un mot épargne la ressaisie complète) ;
- Synthèse : calcule « revenus / dépenses / solde du mois » avec filter + reduce et présente-les dans une carte en haut :

::: div .code-block
:::inline div .code-head
<span>SWIFT · Calcul du résumé mensuel</span><span class="dots">···</span>
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

#### 6. La recette : trois niveaux de contrôle + deux défis pour aller plus loin

Projet fini ? Passe la recette sur trois niveaux « fonctionnel → limites → architecture » : peut-on enregistrer, supprimer, les données survivent-elles au redémarrage de l'App (fonctionnel) ; l'App plante-t-elle si on saisit 0 ou un montant négatif (limites) ; l'interface et les données sont-elles bien séparées, les champs sont-ils codés en dur (architecture).

Une fois la recette de la version de base franchie, offre-toi deux « plats plus relevés » :

1. Statistiques par catégorie : ajoute un onglet « Stats » et dessine les dépenses par catégorie en camembert / histogramme avec Swift Charts — la bibliothèque de graphiques officielle d'Apple produit un graphique en quelques lignes ;
2. Synchronisation iCloud : activer la synchro iCloud de SwiftData demande à peine quelques réglages — le carnet se synchronise tout seul entre iPhone/iPad, et prend d'un coup des « allures haut de gamme ».

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
À toi de jouer : achève-le cette semaine

{class="mt-1"}
Avance dans l'ordre « couche données → ViewModel → page liste → fenêtre de saisie → carte de synthèse », une étape par jour. Si tu restes bloqué, donne l'erreur telle quelle à un moteur de recherche ou à une IA (tu te souviens de la septième partie, « Pratique de la programmation avec l'IA » ? En décrivant un problème, précise « comportement attendu, comportement observé, étapes pour reproduire »). Une fois terminé, tiens tes comptes avec pendant une semaine — se servir d'une App faite de ses mains procure un élan de fierté qui te poussera à continuer.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Résumé du chapitre

- Cinq éléments de besoin → découpés en petites étapes « utilisables à chaque pas », puis on se lance
- Couche données : modèle @Model + conteneur modelContainer + requêtes FetchDescriptor
- Répartition MVVM : la View dessine, le ViewModel @Observable tient la logique, SwiftData tient le stockage
- Interface : List + Section + toolbar + fenêtre de saisie en sheet
- Recette en trois niveaux (fonctionnel/limites/architecture) + défis avancés (Swift Charts, synchro iCloud)
:::
