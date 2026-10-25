---
id: di-liu-shi-jiu-zhang
num: 69
part: ios-kai-fa-pian
nav: Chapitre 69 : Aide-mémoire et ressources
toc: default
kind: chapter
---

### Chapitre 69 : Mémo et ressources

{class="chapter-intro mb-4"}
Ce chapitre est un mémo qui se suffit à lui-même. Quand tu ne te rappelles plus d'une écriture ou qu'il te faut décider vite, ouvre-le directement. Traite-le comme des « cartes de poche » : mémo du code courant, questions fréquentes, ressources d'apprentissage — sans en sauter la moindre page.

#### 1. La fiche mémo du code courant

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ce que tu veux faire</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Code clé</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">État privé de la page</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@State private var x = valeurInitiale</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Logique entre les pages</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">@Observable class VM { var x = 0 }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Disposition verticale / horizontale</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">VStack { }</code> / <code class="inline">HStack { }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Espace élastique</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Spacer()</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Liste</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">List { ForEach(tableau) { ... } }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Saut d'une page à l'autre</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">NavigationStack + NavigationLink</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Fenêtre en bas d'écran</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">.sheet(isPresented: $show) { contenu }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Fermer la page courante</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">@Environment(\.dismiss) var dismiss</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Récupérer des données en ligne</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">try await URLSession.shared.data(from: url)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Analyse JSON</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">struct X: Codable</code> + <code class="inline">JSONDecoder().decode</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Stocker une petite configuration</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UserDefaults.standard.set(valeur, forKey: "cle")</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Stocker des données structurées</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">@Model</code> + <code class="inline">modelContainer</code> + <code class="inline">@Query</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Adaptation au mode sombre</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Utiliser les couleurs système (.primary / Color(.systemGray6)), ne rien coder en dur</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lancer les tests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><kbd>⌘U</kbd></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Aide-mémoire du développement iOS (édition d'août 2026)

#### II. Questions fréquentes (FAQ)

Q1 : Je n'ai pas de Mac, puis-je apprendre le développement iOS ?

Tu peux apprendre le langage, mais pas faire un développement complet. Swift Playgrounds sur iPad/iPhone permet de couvrir tout le contenu du chapitre 61 ; mais Xcode est exclusif à macOS et il te faudra au final un Mac. Avec un budget limité, tu peux d'abord louer un Mac dans le cloud ou acheter un Mac mini d'occasion pour dépanner, puis décider de ton investissement une fois le langage maîtrisé.

Q2 : Combien coûte l'apprentissage du développement iOS ?

Phase d'apprentissage : 0 yuan (Xcode gratuit + tests sur appareil réel avec un identifiant Apple gratuit). Phase de publication : compte développeur à 99 $ par an (environ 700 yuans). Ajoute l'investissement matériel d'un Mac, et c'est tout le coût. Au regard du retour — même un petit utilitaire sur l'App Store trouve des utilisateurs payants — le calcul est rentable.

Q3 : SwiftUI ou UIKit, lequel apprendre en premier ?

SwiftUI. En 2026, les nouveaux projets, tutoriels et postes sont dominés par SwiftUI, et ce livre l'utilise du début à la fin. UIKit est le framework de la génération précédente, encore très utilisé dans d'anciens projets — une fois SwiftUI bien maîtrisé, complète avec UIKit selon tes besoins (Apple propose des tutoriels d'interopérabilité), tu t'y mettras très vite. N'inverse pas l'ordre.

Q4 : Est-ce facile de trouver du travail en développement iOS ?

L'état du marché en 2026 : les postes juniors qui se contentent de « dessiner des interfaces » sont très disputés, mais les développeurs « à l'aise en Swift + SwiftUI + avec une app publiée » restent très recherchés. Le salaire médian des postes iOS figure depuis toujours dans le haut du classement des différentes technos. Pendant ton apprentissage, ton meilleur CV, c'est l'app que tu as faite toi-même et disponible sur la boutique.

Q5 : Que faire si l'app est refusée lors de la validation ?

Pas de panique, c'est tout à fait normal — une première soumission a de bonnes chances d'être refusée. Apple motive ses refus de façon très précise (quelle page, quelle règle) ; corrige point par point, réponds avec tes explications dans App Store Connect, puis renvoie. Les trois grandes causes de refus : l'usage des permissions mal expliqué, des bugs d'interface, des métadonnées (captures/description) qui ne correspondent pas au produit. Vérifie ces trois points à l'avance et tu économiseras un tour d'attente.

#### III. Aide-mémoire des raccourcis Xcode les plus utilisés

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Action</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Raccourci</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Exécuter / Tester</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘R / ⌘U</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ouvrir l'aperçu du canvas</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌥⌘↩</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ouvrir rapidement un fichier</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘O</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Recherche globale</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘F</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Réindenter le code</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌃I</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Commenter / Décommenter</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘/</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Nettoyer le cache de build</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘K</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Aller à la définition</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘ + clic</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Renommer (renommage global sécurisé)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Clic droit → Refactor → Rename</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Aide-mémoire des raccourcis Xcode les plus utilisés

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Petit conseil : en cas de compilation mystérieuse, vide d'abord le cache

{class="mt-1"}
Les événements paranormaux du type « hier ça tournait, aujourd'hui plus rien » viennent dans six à sept cas sur dix d'un cache de build corrompu. Un ⇧⌘K pour nettoyer puis recompiler guérit la grande majorité de ces bizarreries. Si ça ne suffit pas, redémarre Xcode (voire le Mac entier), et en dernier recours « supprime le dossier DerivedData » — c'est le rituel en trois temps que se transmettent les développeurs iOS.
:::

#### IV. Ressources d'apprentissage recommandées

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Type</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ressource</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Pourquoi c'est recommandé</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Officiel</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">developer.apple.com</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Documentation officielle d'Apple, où se trouvent les tutoriels SwiftUI/Swift : la référence numéro un</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Officiel</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Les SwiftUI Tutorials d'Apple</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cours officiel guidé pas à pas, convivialité maximale pour les débutants</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Officiel</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Site officiel de Swift (swift.org)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Documentation officielle du langage et bac à sable en ligne</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Communauté</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Hacking with Swift</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">La bibliothèque de tutoriels gratuits de Paul Hudson, dont la qualité est unanimement reconnue parmi les toutes meilleures</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Communauté</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Stack Overflow (tag swiftui)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Le premier réflexe pour demander de l'aide face à une erreur</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Vidéo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Chaîne officielle Apple Developer (vidéos des WWDC)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Les explications de référence des nouveautés chaque année</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Design</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Guide des interfaces humaines d'Apple (HIG)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">La bible officielle pour créer des interfaces au « goût d'Apple »</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Complément</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">La septième partie « Pratique de la programmation par IA » (chapitres 37 à 47)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">La méthode complète pour développer iOS avec l'aide de l'IA</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Liste des ressources pour apprendre le développement iOS (août 2026)

#### V. Conclusion : de la première app à l'énième app

Avec le recul, tu es passé de « je ne sais pas ce qu'est SwiftUI » à : installer Xcode, apprendre Swift, dessiner des interfaces avec SwiftUI, brancher une base de données et le réseau sur ton app, puis tester, empaqueter, publier — sur ce chemin, tu as déjà franchi le tronçon le plus difficile, celui qui mène de zéro à un.

Le monde de la technologie va très vite : les frameworks se mettent à niveau, les outils changent de génération, l'IA prend en charge de plus en plus de travail de « frappe au clavier ». Mais une chose ne se démode pas : ta capacité à décomposer une idée floue en étapes claires, puis à la réaliser pas à pas. Les outils sont des amplificateurs, la réflexion est le socle. Un amplificateur peut se remplacer, le socle ne doit pas bouger.

:::inline div .quote-line
Tu n'es plus juste "quelqu'un qui sait se servir de son téléphone" : tu peux transformer les idées de ta tête en apps qui tournent réellement sur des centaines de millions d'iPhone. À partir d'aujourd'hui, crée avec ton clavier – c'est ça, la poésie du développeur iOS.
:::

#### Références

{class="list-decimal pl-6 mb-3 space-y-1 text-xs text-gray-500"}
1. Apple Inc. (2026). SwiftUI Framework Documentation. developer.apple.com.
2. Apple Inc. (2026). Swift Programming Language Guide. swift.org.
3. Apple Inc. (2026). SwiftData Framework Documentation. developer.apple.com.
4. Apple Inc. (2026). App Store Review Guidelines. developer.apple.com/app-store/review.
5. Apple Inc. (2026). Human Interface Guidelines (HIG). developer.apple.com/design.
6. Apple Inc. (2026). Xcode 27 Release Notes and App Distribution Guide.
