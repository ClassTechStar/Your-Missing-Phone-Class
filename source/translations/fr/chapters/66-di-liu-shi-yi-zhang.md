---
id: di-liu-shi-yi-zhang
num: 61
part: ios-kai-fa-pian
nav: Chapitre 61 : Prise en main rapide de Swift — le premier langage du développement Apple
toc: default
kind: chapter
---

### Chapitre 61 : Swift en prise rapide — le premier langage du développement Apple

{class="chapter-intro mb-4"}
Dans ce chapitre, on apprend officiellement le langage. Pas de stress — Swift est célèbre pour être « doux avec les débutants », et inutile d’apprendre la grammaire par cœur : maîtriser d’abord 20 % de la syntaxe te permet de comprendre et d’écrire 80 % du code du quotidien. Le reste se cherchera au fil du projet. Retiens notre principe d’apprentissage : comprendre > mémoriser, savoir utiliser > maîtriser.

#### 1. Variables et types : donner un nom aux données

Un programme, c’est « données + logique ». Une variable, c’est un nom donné à des données pour les garder. Swift les déclare avec let et var :

::: div .code-block
:::inline div .code-head
<span>SWIFT · Variables</span><span class="dots">···</span>
:::

```
let name = "Léa"        // let : constante (à privilégier par défaut)
var age = 18             // var : variable (modifiable plus tard)

age = 19                 // <i class="fas fa-check-circle mr-1"></i> var peut être modifié
// name = "Emma"         // <i class="fas fa-times-circle mr-1"></i> let ne peut pas être modifié : erreur de compilation

let score: Int = 100     // on peut aussi préciser le type explicitement
let pi = 3.14            // sans l'écrire, il est déduit automatiquement

print("Bonjour \(name)")   // interpolation de chaîne : antislash + parenthèses
```
:::

Les types courants à retenir en une table :

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Type</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ce qu’il stocke</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Exemple</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Int</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Entier</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">42</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Double</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Décimal</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3.14</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">String</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Texte</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"Bonjour"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bool</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Vrai/faux</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">true / false</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">[Int] (tableau)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Un ensemble de données</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">[1, 2, 3]</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Les types de base courants de Swift

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Astuce : le principe « let d’abord »

{class="mt-1"}
La règle d’airain de la communauté Swift : par défaut let, et var seulement en cas de vraie nécessité. Si tu emploies var là où let suffirait, Xcode te le signalera en jaune. Cette habitude t’épargne toute une famille de bugs « variable modifiée par mégarde » — moins le code varie, plus il est facile à raisonner.
:::

#### 2. Les optionnels (Optional) : le « talisman anti-plantage » de Swift

C'est le concept le plus important de Swift, et de loin. En une phrase : quand une valeur peut « ne pas exister », Swift t'oblige à la traiter — le langage élimine à la racine le crash « pointeur nul », ce cauchemar de la profession.

::: div .code-block
:::inline div .code-head
<span>SWIFT · Optionals</span><span class="dots">···</span>
:::

```
var name: String = "Léa"   // type normal : ne peut jamais être nil
// name = nil                // <i class="fas fa-times-circle mr-1"></i> erreur de compilation : ça te bloque direct

var nickname: String? = nil  // ajoute un point d'interrogation : autorise nil (optional)
nickname = "Tommy"

// avec les optionals, il faut les "déballer" :
if let n = nickname {        // if let : déballage sûr
    print("Bonjour \(n)")
} else {
    print("Pas encore de surnom")
}

let len = nickname?.count ?? 0   // ?? valeur par défaut (opérateur de coalescence)
print(len)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Attention : le ! est une opération à haut risque

{class="mt-1"}
Écrire nickname! dans le code (déballage forcé), c'est crier au compilateur « je te garantis que ce n'est pas nil » — et si tu te trompes, l'App plante sur-le-champ. Règle de débutant : utilise autant que possible if let / ?? et bannis le !. Quand Xcode complète ton code, il glisse parfois un ! sans te le demander : pense à le retirer.
:::

#### 3. Fonctions et closures : empaqueter la logique en « boutons »

Une fonction, c'est une logique qui porte un nom, comme un bouton sur une télécommande. Une closure (fermeture), c'est une « fonction sans nom » que l'on peut passer à d'autres à la volée :

::: div .code-block
:::inline div .code-head
<span>SWIFT · Fonctions et closures</span><span class="dots">···</span>
:::

```
// fonction : le nom devant ; paramètres et type de retour derrière
func greet(name: String) -> String {
    return "Bonjour, \(name) !"
}
print(greet(name: "Léa"))     // à l'appel, avec le nom du paramètre

// closure : définie sur place, légère et directe
let numbers = [1, 2, 3, 4]
let doubled = numbers.map { $0 * 2 }   // $0 = l'élément courant
// [2, 4, 6, 8]

let big = numbers.filter { $0 > 2 }    // filtrer
// [3, 4]
```
:::

En SwiftUI, les closures sont partout : les accolades qui suivent le Button("Appuie-moi") { ... } d'un bouton forment une closure. Grave bien les combos de collections map, filter et sorted — 90 % du traitement des listes, à l'avenir, sera une combinaison de ces trois-là.

#### 4. Structures et protocoles : le système « LEGO » de Swift

La préférence officielle de Swift est claire : privilégie les structures (struct) et n'utilise les classes (class) que pour l'héritage. La struct est un « type valeur » — chaque copie vit sa propre vie, ce qui élimine d'office toute une famille de bugs :

::: div .code-block
:::inline div .code-head
<span>SWIFT · Structs et protocoles</span><span class="dots">···</span>
:::

```
// le struct : la boîte à données
struct Record {
    var id = UUID()
    var amount: Double
    var category: String
    var date: Date

    // le struct embarque son "memberwise initializer" : création directe possible
}
let r = Record(amount: 25.5, category: "repas", date: Date())

// protocole : le contrat de "quelles capacités il doit avoir"
protocol Identifiable {
    var id: UUID { get }
}
struct Record: Identifiable { ... }   // adopter le protocole = promettre de remplir ses exigences
```
:::

En SwiftUI, presque tout est une struct (View est un protocole). Pas grave si tu ne le saisis pas encore : tu t'y frotteras chaque jour au chapitre 62 — dans le monde de Swift, adopte d'abord la struct.

#### 5. La fiche mémo de syntaxe pour grands débutants

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ce que tu veux faire</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Comment l'écrire</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Définir une constante / variable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">let x = 1</code> / <code class="inline">var x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Interpolation de chaîne</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"Bonjour, \(name)"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Définir une fonction</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">func nom(parametre: Type) -> TypeRetour { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Condition</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if condition { ... } else { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Boucle</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">for x in tableau { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Extraction sécurisée</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if let x = valeurOptionnelle { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Valeur par défaut</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">x ?? valeurParDefaut</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Définir une structure</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">struct X { var a: Int; var b: String }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Closure</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">{ $0 * 2 }</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Fiche mémo de syntaxe Swift (édition débutant)

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
À toi de jouer : 15 minutes de Swift dans Playgrounds

{class="mt-1"}
Si tu as un Mac, ouvre Xcode → Playground ; sinon, prends Swift Playgrounds sur iPad ou le terrain de jeu en ligne. Exécute chaque extrait de code de ce chapitre, change les chiffres et les textes, provoque exprès quelques erreurs pour voir comment Xcode t'alerte. Ces 15 minutes de « jouer avant d'apprendre » te rendront deux fois plus à l'aise au chapitre 62.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Résumé du chapitre

- let en priorité, var avec parcimonie ; le type se déduit tout seul, mais une déclaration explicite après le deux-points reste possible
- Les optionnels sont l'âme de Swift : une valeur potentiellement vide doit être traitée — if let / ?? sont tes talismans, le ! est une opération à haut risque
- Les appels de fonction portent le nom des paramètres ; une closure = une fonction sans nom, omniprésente en SwiftUI
- Privilégie la struct et respecte les protocoles (Protocol) ; en SwiftUI, presque tout est une struct
- 20 % de la syntaxe fait 80 % du travail : d'abord savoir s'en servir, la maîtrise viendra ensuite
:::
