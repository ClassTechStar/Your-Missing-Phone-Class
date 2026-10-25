---
id: di-wu-shi-si-zhang
num: 54
part: an-zhuo-kai-fa-pian
nav: Chapitre 54 : Projet 1 — Mon carnet de comptes (version locale)
toc: default
kind: chapter
---

### Chapitre 54 : Projet 1 — Mon carnet de comptes (version locale)

{class="chapter-intro mb-4"}
Bienvenue dans ton premier « vrai projet ». Ce carnet de comptes ne se connecte pas au réseau, mais il a tout d'une grande : enregistrer une écriture, consulter l'historique, faire des statistiques mensuelles, supprimer et modifier. Une fois terminé, tu auras parcouru de bout en bout le flux complet « données → logique → interface ». Ne te précipite pas pour recopier le code — réfléchis d'abord, agis ensuite : c'est notre principe de toujours.

#### 1. Réfléchir au besoin : pose d'abord cinq questions

Avant de te lancer, clarifie ton idée avec les « cinq éléments du besoin » :

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Élément</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Réponse</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who (pour qui)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pour soi, et pour la famille ou les amis aussi</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What (faire quoi)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Enregistrer revenus et dépenses, consulter l'historique, résumer par mois, statistiques par catégorie</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why (pourquoi)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">S'entraîner + comprendre où part l'argent</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How (comment)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin + Compose + Room + MVVM, 100 % local, sans back-end</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint (contraintes)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Terminer en une semaine ; Android 8 minimum ; même sans publication, coder selon les critères de publication</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Les cinq éléments du besoin du carnet de comptes

Décompose ensuite en petites étapes « utilisables dès leur achèvement » : ① la couche données Room (stocker une écriture) ; ② l'écran liste (voir l'historique) ; ③ l'écran de saisie (ajouter une écriture) ; ④ suppression et édition ; ⑤ la carte de synthèse mensuelle. À chaque étape finie, l'app est déjà « quelque chose d'utilisable ».

#### 2. La couche données : donner un « foyer » aux écritures

Définis d'abord à quoi ressemble une écriture — des champs suffisants, sans gourmandise :

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Record.kt (entité)</span><span class="dots">···</span>
:::

```
@Entity(tableName = "records")
data class Record(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val type: String,        // "income" revenu | "expense" dépense
    val amount: Double,      // montant (yuan)
    val category: String,    // catégorie : repas, transport, salaire…
    val note: String = "",   // note (facultatif)
    val date: String         // "2026-08-15"
)
```
:::

Ajoute dans le Dao deux requêtes « pour les statistiques » — c'est l'âme du carnet de comptes :

::: div .code-block
:::inline div .code-head
<span>KOTLIN · RecordDao.kt (requêtes statistiques)</span><span class="dots">···</span>
:::

```
@Dao
interface RecordDao {
    @Query("SELECT * FROM records ORDER BY date DESC, id DESC")
    fun getAll(): Flow&lt;List&lt;Record&gt;&gt;

    @Insert
    suspend fun insert(record: Record)

    @Delete
    suspend fun delete(record: Record)

    @Query("SELECT COALESCE(SUM(amount),0) FROM records WHERE type='income' AND date LIKE :month || '%'")
    suspend fun monthIncome(month: String): Double   // month est au format "2026-08"

    @Query("SELECT COALESCE(SUM(amount),0) FROM records WHERE type='expense' AND date LIKE :month || '%'")
    suspend fun monthExpense(month: String): Double
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Petit conseil : pourquoi Double pour les montants ?

{class="mt-1"}
Les apps financières rigoureuses utilisent BigDecimal ou un « Int en centimes » pour éviter les erreurs de virgule flottante (le vieux problème 0,1+0,2≠0,3). Pour un projet d'entraînement, Double suffit ; le jour où tu feras un vrai produit financier, pense à passer aux centimes comme unité — c'est un piège que d'innombrables aînés ont foulé avant toi.
:::

#### 3. MVVM : quand interface et logique « quittent la maison commune »

Laisser l'interface toucher directement à la base de données ? Ça tourne, mais le code de l'interface devient long et pénible. L'architecture MVVM donne à chacun son rôle : la View (l'interface) ne fait que dessiner, le ViewModel (le pivot logique) gère les données, le Model (Room) gère le stockage.

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> Vue (interface Compose)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> ViewModel (état et logique)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-database mr-1"></i> Model (couche de données Room)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figure 5 : la structure MVVM en trois couches — les données circulent dans un seul sens, chaque couche reste à sa place
:::

::: div .code-block
:::inline div .code-head
<span>KOTLIN · RecordViewModel.kt (squelette)</span><span class="dots">···</span>
:::

```
class RecordViewModel(private val dao: RecordDao) : ViewModel() {

    // convertit le Flow en état observable par l'interface
    val records = dao.getAll()
        .stateIn(viewModelScope, SharingStarted.WhileSubscribed(), emptyList())

    // actions utilisateur : appeler des fonctions suspend
    fun addRecord(type: String, amount: Double, category: String, note: String, date: String) {
        viewModelScope.launch {
            dao.insert(Record(type = type, amount = amount,
                category = category, note = note, date = date))
        }
    }

    fun deleteRecord(record: Record) {
        viewModelScope.launch { dao.delete(record) }
    }
}
```
:::

Dans l'interface (Compose), écris : val vm: RecordViewModel = viewModel(), puis val list by vm.records.collectAsState() — dès que les données changent, la liste se rafraîchit toute seule, sans que tu aies rien à faire. C'est la puissance des trois mousquetaires MVVM + Flow + Compose réunis.

#### 4. L'interface : l'écran liste + l'écran de saisie

Pour l'écran liste, utilise LazyColumn (liste à chargement paresseux) — jamais de ralentissement, même avec beaucoup de données :

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Écran de liste des dépenses (extrait clé)</span><span class="dots">···</span>
:::

```
@Composable
fun RecordListScreen(vm: RecordViewModel) {
    val records by vm.records.collectAsState()

    Column {
        // carte de synthèse en haut (revenus - dépenses = solde)
        SummaryCard(records)

        // liste des opérations
        LazyColumn {
            items(records, key = { it.id }) { record -&gt;
                RecordRow(record) { vm.deleteRecord(record) }
            }
        }

        // bouton flottant "ajouter une dépense" → ouvre le formulaire
        FloatingActionButton(onClick = { showAddDialog = true }) {
            Text("+")
        }
    }
}

@Composable
fun RecordRow(record: Record, onDelete: () -&gt; Unit) {
    Row(Modifier.fillMaxWidth().padding(12.dp)) {
        Text(record.category, fontWeight = FontWeight.Bold)
        Spacer(Modifier.weight(1f))
        Text(if (record.type == "income") "+${record.amount}" else "-${record.amount}",
             color = if (record.type == "income") Color(0xFF27AE60) else Color(0xFFC0392B))
    }
}
```
:::

Pour la saisie, un AlertDialog (boîte de dialogue) est le plus simple : quelques champs + un basculement dépense/revenu + un menu déroulant de catégories, et au clic sur OK on appelle vm.addRecord(...).

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Attention : ne fais pas l'économe sur la validation des saisies

{class="mt-1"}
Le champ du montant doit absolument être validé : valeurs vides, négatives, saisies illégales comme « abc », tout doit être intercepté (avec toDoubleOrNull()). L'une des causes les plus courantes de plantage d'une app, c'est de « considérer la saisie de l'utilisateur comme un enfant sage ». Retiens : tout ce que tape l'utilisateur doit être inspecté comme un ennemi.
:::

#### 5. Éditer et supprimer : permettre aux données « d'entrer et de sortir »

Un carnet qui sait ajouter mais pas supprimer est bon à jeter au bout de trois jours. Ajoute deux opérations :

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Supprimer et modifier</span><span class="dots">···</span>
:::

```
// ajoute deux méthodes au Dao :
@Query("UPDATE records SET amount=:amount, category=:category, note=:note WHERE id=:id")
suspend fun update(id: Long, amount: Double, category: String, note: String)

@Query("DELETE FROM records WHERE id=:id")
suspend fun deleteById(id: Long)

// à l'écran : appui long sur un élément ouvre le menu "modifier/supprimer" (avec Compose : DropdownMenu ou AlertDialog)
// avant de supprimer, mieux vaut une confirmation : la "suppression accidentelle" est ce que les utilisateurs d'apps de dépenses détestent le plus
```
:::

Deux leçons de détail sur l'interaction : la suppression exige une double confirmation (contre les doigts qui glissent), et l'édition pré-remplit autant que possible les valeurs d'origine (corriger un mot est plus simple que tout retaper). Ne sous-estime pas ces deux détails — le « côté produit » se bâtit sur ce genre de détails.

#### 6. Réception : trois niveaux de vérification + deux défis avancés

Projet terminé, fais la réception selon trois niveaux « fonctionnalités → cas limites → architecture » : sait-on enregistrer, sait-on supprimer, les données sont-elles encore là à la réouverture de l'app (fonctionnalités) ; l'app plante-t-elle avec un montant à 0 ou négatif, les données se perdent-elles à la rotation de l'écran (cas limites) ; interface et données sont-elles mélangées, des champs sont-ils codés en dur (architecture).

Une fois la version de base réceptionnée, offre-toi deux « plats avancés » :

1. Filtre mensuel : ajoute en haut un sélecteur de mois (par exemple 2026-08 ▾), la liste n'affichant que les écritures du mois ;
2. Camembert par catégorie : avec le Canvas de Compose ou une petite bibliothèque de graphiques, dessine « où part l'argent » en camembert — une fois fait, le carnet de comptes prend un petit « air de produit ».

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
À toi de jouer : termine-le cette semaine

{class="mt-1"}
Avance dans l'ordre « couche données → ViewModel → écran liste → écran de saisie → carte de synthèse », une étape par jour. En cas de blocage, balance le message d'erreur tel quel à un moteur de recherche ou à une IA (tu te souviens de la partie 7, « L'IA au service du code » ? Décris le problème en précisant « comportement attendu, comportement observé, étapes de reproduction »). Une fois l'app finie, note tes comptes pendant une semaine — utiliser une app de ta propre fabrication donne une fierté qui te poussera à continuer.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Résumé du chapitre

- Cinq éléments du besoin → décomposition en petites étapes « utilisables à chaque pas », puis on se lance
- Couche données : entité Record + Dao (avec le SQL de statistiques mensuelles) + Database
- Répartition MVVM : la View ne fait que dessiner, le ViewModel gère la logique, le Model gère le stockage
- Flow + stateIn + collectAsState : dès que les données changent, l'interface se rafraîchit automatiquement
- LazyColumn pour la liste à chargement paresseux ; AlertDialog pour la saisie
- Réception en trois niveaux (fonctionnalités/cas limites/architecture) + défis avancés (filtre mensuel, camembert par catégorie)
:::
