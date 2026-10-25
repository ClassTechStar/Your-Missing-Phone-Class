---
id: di-liu-shi-qi-zhang
num: 67
part: ios-kai-fa-pian
nav: Chapitre 67 : Peaufiner et publier — mise en ligne sur l'App Store
toc: default
kind: chapter
---

### Chapitre 67 : Polissage et publication — tests, débogage et mise en ligne sur l'App Store

{class="chapter-intro mb-4"}
L'App est faite, et ensuite ? Ce chapitre répond aux trois étapes du passage de « ça tourne » à « ça se livre » : comment déboguer avec efficacité pour traquer les bugs, comment écrire des tests pour prévenir les régressions, comment porter l'App sur l'App Store pour que le monde entier la télécharge. La mise en ligne n'est pas qu'une cérémonie — c'est la ligne de partage qui change une réalisation en produit.

#### 1. Les trois armes du débogage : print, points d'arrêt, aperçu

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Outil</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">À quoi ça sert</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Comment s'en servir</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">print + console</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lire les journaux d'exécution</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Dans le code, print("valeur=\(x)") ; la sortie se lit dans la console en bas de Xcode</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Débogage par points d'arrêt</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Arrêter le programme sur une ligne pour voir les valeurs des variables</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Un clic près du numéro de ligne fait naître un marqueur bleu ; l'exécution s'y suspend, et tu avances pas à pas</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Aperçu SwiftUI + débogueur</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Voir en direct l'interface et la hiérarchie des vues</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Canevas #Preview + inspecteur View Hierarchy en cours d'exécution</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Les trois armes du débogage

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Astuce : comment lire un plantage ?

{class="mt-1"}
Quand Swift plante, la console imprime "Fatal error" accompagné de la cause, et Xcode s'arrête à la ligne fautive en la surlignant. L'historique des plantages sur appareil réel se consulte dans Xcode → Window → Organizer → Crashes (compte payant exigé). Cherche d'abord avec les mots-clés « première phrase de la cause de l'erreur + swiftui » — une question précise vaut une réponse précise.
:::

#### 2. Les tests : une assurance-vie pour le code

Le test à la main est traître — tu modifies une fonctionnalité, une autre casse en silence. Les tests valent à la fois « pilule du remords » et « gilet pare-balles ». Sur iOS, le framework XCTest se décline en deux :

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Niveau</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ce qui est testé</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Target</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Vitesse</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tests unitaires</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Logique pure (calculs, validations)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstAppTests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">En secondes</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tests UI</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Comportement réel de l'interface</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstAppUITests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">En minutes</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Test manuel</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ressenti et expérience d'un humain</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">——</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Toujours nécessaire</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Les niveaux de test iOS (le projet modèle embarque déjà deux Test Target)

::: div .code-block
:::inline div .code-head
<span>SWIFT · Exemple de test unitaire</span><span class="dots">···</span>
:::

```
import XCTest

// extraire en fonction pure la logique de "convertir le texte du montant en nombre"
func parseAmount(_ input: String) -> Double? {
    guard let v = Double(input.trimmingCharacters(in: .whitespaces)),
          v > 0 else { return nil }
    return v
}

final class AmountTests: XCTestCase {
    func testEmptyInputReturnsNil() {
        XCTAssertNil(parseAmount(""))
    }
    func testNegativeReturnsNil() {
        XCTAssertNil(parseAmount("-5"))
    }
    func testNormalValueParses() {
        XCTAssertEqual(parseAmount("12.5"), 12.5)
    }
}
```
:::

Lancer les tests : ⌘U. Quand tout est au vert, on modifie le code l'esprit tranquille. La validation des montants et les calculs de synthèse du carnet de comptes méritent tous d'être couverts par des tests unitaires.

#### 3. Signature et packaging : apposer le « sceau » sur l'App

Chaque App iOS doit être signée pour pouvoir s'installer — la preuve que « ce paquet sort bien de toi et n'a pas été altéré ». La hiérarchie :

- Phase d'apprentissage : Apple ID gratuit + signature automatique de Xcode (Personal Team) ; ça tourne sur appareil réel, à renouveler tous les 7 jours ;
- Phase de distribution : un compte développeur payant (99 dollars/an) délivre certificats et profils, condition de la mise en boutique et de l'installation durable.

Packaging : menu Xcode Product → Archive ; construction achevée, dans Organizer, Distribute App → choisir App Store Connect → envoyer. L'archivage doit viser Generic iOS Device comme cible (pas le simulateur) — l'étape que les débutants oublient le plus.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Piège à éviter : certificat perdu = mises à jour coupées

{class="mt-1"}
Une fois le certificat de signature et la clé privée perdus, il te devient impossible d'envoyer des mises à jour à l'ancienne App — les utilisateurs ne peuvent qu'installer une application « toute neuve ». Sauvegarde soigneusement les certificats (export .p12 du trousseau) et garde le mot de passe en sûreté. Bonne nouvelle : Apple offre la « signature automatique » et la gestion des certificats dans le cloud (case Automatically manage signing dans Xcode), qui épargnent l'essentiel des pièges manuels.
:::

#### 4. Le parcours complet de mise en boutique sur l'App Store

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> Créer le compte de développeur</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-invoice mr-1"></i> Préparer les éléments de la boutique</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-box mr-1"></i> Téléverser le build</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-clipboard-list mr-1"></i> Remplir les infos de confidentialité et de validation</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> Validation Apple (1 à 7 jours)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-party-horn mr-1"></i> Publier</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figure 5 : les six pas de la mise en ligne sur l'App Store
:::

- Inscription : developer.apple.com, compte individuel 99 dollars/an ;
- Éléments : icône (1024×1024, sans coins arrondis — Apple découpe lui-même), captures d'écran (toutes les tailles d'iPhone), description, lien vers la politique de confidentialité ;
- Questionnaire de confidentialité : déclare en toute honnêteté quelles données sont recueillies — un carnet de comptes hors ligne peut cocher « ne collecte aucune donnée » ;
- Revue : la première soumission attend souvent 1 à 7 jours ; en cas de refus, corrige point par point d'après les « remarques de revue » — les motifs de refus d'Apple sont d'ordinaire très précis, il suffit de les suivre ;
- TestFlight : avant la mise en boutique, distribue la version de test à tes amis en bêta interne (jusqu'à 10 000 personnes), récolte un tour de retours puis soumets officiellement — l'allure du vrai professionnel.

#### 5. Fabriquer les éléments de boutique : la première impression, c'est le volume de téléchargements

La fiche boutique est la vitrine que l'utilisateur voit en « flânant » devant le magasin. Trois éléments décident de la première impression :

- Icône : 1024×1024, ne te débrouille pas avec une capture d'écran. Sans âme de designer, fais générer un graphique épuré par un outil d'IA ; elle n'est recevable que si, rapetissée sur l'écran d'accueil, on la reconnaît d'un coup d'œil ;
- Captures : au moins 2 jeux (aux tailles iPhone dominantes), montrant les scènes fonctionnelles les plus centrales ; chaque capture porte une légende en langue de tous les jours (« une écriture en une seconde » vaut dix fois « une solution de comptabilité performante ») ;
- Description : la première phrase établit « ce que c'est + pour qui », sans empiler « le plus pro, le plus fort » — la sincérité rapporte plus que l'enflure.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
À toi de jouer : « livre » une fois le carnet de comptes

#### 6. Remontée des plantages et petite liste d'optimisation des performances

Avant la mise en boutique, ces deux chantiers méritent chacun une demi-heure :

##### 1. La surveillance des plantages

Ce qui n'a pas planté pendant tes tests peut planter sur le téléphone des utilisateurs. Apple livre des rapports de plantage gratuits dans Xcode Organizer (les journaux d'appareils réels supposent un compte payant) ; le choix plus paisible consiste à intégrer un SDK tiers (du genre Firebase Crashlytics). Publier sans surveillance des plantages, c'est rouler les yeux fermés.

##### 2. Quatre points d'autocontrôle des performances

1. Les listes avec LazyVStack / List : ne force pas une longue liste dans un simple VStack — le chargement paresseux est la première leçon de performances ;
2. Les images sans y fourrer les originaux : passe par AsyncImage (image distante) et le cache système ; un original de 5 Mo suffit à étrangler un vieil appareil ;
3. Pas de gros travaux sur le thread principal : réseau et gros fichiers passent tous par async/await ;
4. Mesure avec Instruments : l'analyseur de performances embarqué dans Xcode (Time Profiler, détection de fuites mémoire) — mesure d'abord, optimise ensuite, ne te fie pas à ton flair.

{class="mt-1"}
① Complète les logiques comme parseAmount de 3 tests unitaires (⌘U au vert) ; ② attrape de tes propres mains, au point d'arrêt, un plantage que tu auras fabriqué, et répare-le ; ③ produis un paquet via Product → Archive, puis passe par TestFlight pour inviter des amis en bêta ; ④ si tu as du carburant, inscris-toi au compte développeur et soumets réellement le carnet de comptes en boutique. Les trois premières étapes se bouclent ce soir.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Résumé du chapitre

- Trois armes du débogage : journaux print, points d'arrêt, aperçu SwiftUI et inspecteur de vues
- XCTest : tests unitaires (⌘U) + tests UI + tests manuels, déjà prévus dans le modèle
- Signature : automatique avec un compte gratuit (renouvellement tous les 7 jours) ; seule la distribution exige un compte payant
- Packaging : Generic iOS Device + Archive + Distribute ; sauvegarde impérative des certificats
- Six pas vers la boutique : inscription → éléments → envoi → questionnaire de confidentialité → revue → publication ; TestFlight pour la bêta d'abord
:::
