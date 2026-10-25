---
id: di-liu-shi-er-zhang
num: 62
part: ios-kai-fa-pian
nav: Chapitre 62 : Développement d'interfaces — initiation à SwiftUI
toc: default
kind: chapter
---

### Chapitre 62 : Créer l'interface — initiation à SwiftUI

{class="chapter-intro mb-4"}
L'interface, c'est tout ce que l'utilisateur voit. SwiftUI est le framework d'interface déclaratif lancé par Apple en 2019 : tu te contentes de « déclarer » à quoi ressemble l'interface, et le système gère tout seul le rendu, le mode sombre et l'adaptation aux écrans de toutes sortes. En 2026, SwiftUI est le choix dominant des nouveaux projets. Dans ce chapitre, on apprend à « dessiner ».

#### 1. La philosophie de SwiftUI : déclaratif, pas impératif

L'ancienne façon de faire les interfaces était « impérative » : tu dictais au système, pas à pas, « crée un bouton → place-le en (20,30) → règle la couleur ». SwiftUI est « déclaratif » : tu décris directement « l'interface contient un bouton rouge sur lequel est écrit 'Appuie-moi' », et le système se débrouille seul pour savoir comment dessiner et quand redessiner.

::: div .code-block
:::inline div .code-head
<span>SWIFT · Première vue SwiftUI</span><span class="dots">···</span>
:::

```
import SwiftUI

struct ContentView: View {
    var body: some View {      // body : décrit "à quoi ressemble l'interface"
        VStack {               // empilés en vertical
            Text("Bonjour, le monde !")
                .font(.largeTitle)      // modificateur : grand titre
            Button("Appuie ici") {
                print("Cliqué !")
            }
            .buttonStyle(.borderedProminent)  // bouton bleu plein
        }
        .padding()
    }
}
```
:::

Points clés : une vue = une struct conforme au protocole View, la propriété body décrit l'interface, et les .modificateurs() s'enchaînent comme des couches de maquillage. Voilà tout le socle de SwiftUI.

#### 2. Les vues de base : texte, bouton, champ de saisie, image

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Vue</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">À quoi ça sert</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Exemple</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Afficher du texte</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text("Bonjour")</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bouton</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button("Appuie-moi") { action }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Champ de saisie</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField("Indication", text: $texte)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Image</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Afficher une image</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Image(systemName: "star.fill")</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Les quatre vues de base de SwiftUI

Note Image(systemName:) : Apple embarque la bibliothèque d'icônes SF Symbols (des milliers d'icônes gratuites) ; un simple nom comme "star.fill" affiche aussitôt une étoile pleine. C'est un bonus caché du développement iOS : pour faire une interface, on ne cherche presque plus d'icônes.

#### 3. Le trio de mise en page : VStack, HStack, ZStack

- VStack : empile verticalement (comme la file à la cantine) ;
- HStack : aligne horizontalement (comme des sièges côte à côte) ;
- ZStack : superpose (comme des cartes empilées, idéal pour les badges et les masques).

::: div .code-block
:::inline div .code-head
<span>SWIFT · Le trio de layouts + modificateurs courants</span><span class="dots">···</span>
:::

```
VStack(alignment: .leading, spacing: 12) {
    HStack {
        Text("Addition")
        Spacer()                 // espace élastique : pousse la droite jusqu'au bout
        Text("-25.5 yuan").foregroundColor(.red)
    }
    Divider()                    // séparateur
    Text("Note : déjeuner")
}
.padding(16)                     // marge sur les quatre côtés
.background(Color(.systemGray6)) // fond gris clair
.cornerRadius(12)                // coins arrondis

// l'ordre des modificateurs compte : d'abord padding puis background ; le fond n'inclut pas la marge
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Attention : l'ordre des modificateurs compte

{class="mt-1"}
padding(16).background(gris) et background(gris).padding(16) ne donnent pas le même résultat : le premier « ménage l'espace puis peint » (le fond n'inclut pas la marge), le second « peint puis ménage l'espace » (le fond inclut la marge). C'est de là que vient le fameux « liseré blanc bizarre » des débutants. Dans le doute, inverse l'ordre : l'aperçu te donne la réponse tout de suite.
:::

#### 4. État et liaison : donner vie à l'interface

Une interface statique, c'est triste. La règle de SwiftUI : l'interface reflète toujours fidèlement l'état ; dès que l'état change, elle se redessine automatiquement.

::: div .code-block
:::inline div .code-head
<span>SWIFT · Compteur avec @State</span><span class="dots">···</span>
:::

```
struct CounterView: View {
    @State private var count = 0   // @State : si cette valeur change, il faut redessiner

    var body: some View {
        VStack {
            Text("Tu as cliqué \(count) fois")
            Button("Appuie +1") {
                count += 1          // change l'état et l'interface se rafraîchit toute seule
            }
        }
    }
}
```
:::

Le champ de saisie exige une « liaison bidirectionnelle » — le symbole $ transmet à la fois la valeur et le droit de la modifier :

::: div .code-block
:::inline div .code-head
<span>SWIFT · Liaison bidirectionnelle avec @Binding</span><span class="dots">···</span>
:::

```
struct InputView: View {
    @State private var text = ""

    var body: some View {
        TextField("Saisis quelque chose", text: $text)  // liaison bidirectionnelle avec $
            .textFieldStyle(.roundedBorder)
        Text("Tu as saisi : \(text)")   // se met à jour en direct pendant la saisie
    }
}
```
:::

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hand-pointer mr-1"></i> Action de l'utilisateur</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> L'état change (count += 1)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> SwiftUI détecte le changement</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> Redessine l'interface (body recalculé)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figure 3 : le flux de données unidirectionnel « état → interface » de SwiftUI
:::

#### 5. Aperçu, thème et animations : les « turbo » de SwiftUI

- La macro #Preview : ajoute #Preview { ContentView() } au bas du fichier et le canevas à droite fait le rendu en temps réel — tu modifies le code, l'effet est immédiat (WYSIWYG) ;
- Le mode sombre offert : emploie les couleurs système (Color(.systemGray6), .primary) plutôt que des couleurs en dur, et l'adaptation au mode sombre se fait toute seule — pas une ligne de plus à écrire ;
- L'animation en une ligne : withAnimation { count += 1 }, ou .animation(.default, value: count) posé sur la vue — des transitions d'une fluidité parfaite.

::: div .code-block
:::inline div .code-head
<span>SWIFT · Animations en dix minutes</span><span class="dots">···</span>
:::

```
struct AnimatedHeartView: View {
    @State private var liked = false

    var body: some View {
        Button {
            withAnimation(.spring(duration: 0.4)) {
                liked.toggle()
            }
        } label: {
            Image(systemName: liked ? "heart.fill" : "heart")
                .font(.system(size: 48))
                .foregroundColor(liked ? .red : .gray)
                .scaleEffect(liked ? 1.3 : 1.0)
        }
    }
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Astuce : d'abord la fonction, ensuite l'animation

{class="mt-1"}
Le travers classique du débutant : « peaufiner les animations alors que l'interface n'est même pas juste ». Fais d'abord marcher les fonctionnalités, ajoute les animations à la fin — l'animation est la cerise sur le gâteau, la fonctionnalité est le pain du quotidien. C'est aussi notre principe de toujours : la simplicité avant tout.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
À toi de jouer : crée un « bouton d'humeur »

#### 6. Mémo des modificateurs courants : une page sous la main, plus de souci d'interface

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ce que tu veux faire</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Modificateur</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Marge (padding)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.padding(16)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Coins arrondis</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.cornerRadius(12)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Couleur de fond</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.background(Color(.systemGray6))</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Police et taille</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.font(.title.bold())</code> / <code class="inline">.font(.system(size: 20))</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Couleur de premier plan (texte/icônes)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.foregroundColor(.red)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Occuper toute la largeur</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.frame(maxWidth: .infinity)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Taille fixe</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.frame(width:100, height: 44)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Alignement</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">VStack(alignment: .leading)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Transparence</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.opacity(0.6)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ombre</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.shadow(radius: 5)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Geste de tap</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.onTapGesture { ... }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Type de clavier</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.keyboardType(.decimalPad)</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Mémo des modificateurs SwiftUI courants

Inutile de les apprendre par cœur — cette page est faite pour être consultée. Les quatre plus utilisés sont en réalité les premiers : padding, coins arrondis, fond et police.

{class="mt-1"}
Transforme le projet modèle en sélecteur d'humeur : un seul bouton qui, à chaque tap, cycle entre 😀 content → 😢 triste → 😡 furieux, le texte et la couleur de fond suivant le mouvement. Indice : mets les trois paires (texte + couleur) dans un tableau, l'indice dans une @State, et au tap calcule (index + 1) % 3. Quand c'est fini, envoie-le à des amis et récolte ta première vague de « waouh, tu sais faire des Apps ! ».
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Résumé du chapitre

- SwiftUI est déclaratif : tu décris « à quoi ça ressemble », le système dessine et redessine
- Vue = struct conforme au protocole View ; body décrit l'interface ; les modificateurs s'enchaînent comme du maquillage
- Quatre vues de base : Text / Button / TextField / Image ; la bibliothèque SF Symbols offre des icônes gratuites à volonté
- Trio de mise en page : VStack vertical, HStack horizontal, ZStack superposé ; Spacer est l'espace élastique
- @State met l'interface en vie ; $ lie dans les deux sens pour nourrir les champs de saisie
- #Preview, WYSIWYG ; les couleurs système s'adaptent au mode sombre ; withAnimation anime en une ligne
:::
