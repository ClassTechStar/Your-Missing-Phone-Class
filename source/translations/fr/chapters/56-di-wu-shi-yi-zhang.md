---
id: di-wu-shi-yi-zhang
num: 51
part: an-zhuo-kai-fa-pian
nav: Chapitre 51 : Développement d'interfaces — initiation à Jetpack Compose
toc: default
kind: chapter
---

### Chapitre 51 : Les interfaces — débuter avec Jetpack Compose

{class="chapter-intro mb-4"}
L'interface, c'est tout ce que l'utilisateur voit. Avant l'arrivée de Compose, on écrivait les interfaces Android en XML — aussi fastidieux qu'un exercice à trous ; en 2021, Google a lancé Jetpack Compose : on « dessine » l'interface directement en code Kotlin, avec un rendu immédiat — change une ligne de code et l'aperçu se met à jour sur-le-champ. En 2026, Compose est la norme absolue des nouveaux projets. Ce chapitre, c'est notre leçon de « dessin ».

#### 1. La philosophie de Compose : l'interface est une fonction

La pensée centrale de Compose tient en une phrase : interface = fonction. Chaque élément affichable à l'écran (texte, bouton, image) est une « fonction composable » (Composable), marquée @Composable. Emboîte-les comme des briques : voilà ton interface.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Première interface Compose</span><span class="dots">···</span>
:::

```
@Composable
fun Greeting(name: String) {
    Text(text = "Bonjour, $name !")     // un "bloc de texte"
}

// composition imbriquée : grands blocs englobant des petits
@Composable
fun HomeScreen() {
    Column {                          // empilés en vertical
        Greeting(name = "Léa")
        Greeting(name = "Emma")
        Button(onClick = { /* quoi faire au clic */ }) {
            Text("Appuie ici")
        }
    }
}
```
:::

Note le « chapeau » @Composable — il dit au compilateur : « ceci est une brique d'interface ». Les briques peuvent s'emboîter à l'infini : voilà tout le secret de Compose.

#### 2. Les composants de base : texte, bouton, champ de saisie, image

Les composants de Compose sont des « briques » ; en voici les quatre plus courantes :

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Composant</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">À quoi ça sert</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Paramètre indispensable</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Afficher du texte</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">text (le texte à afficher)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bouton</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onClick (callback du clic)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Champ de saisie</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">value et onValueChange (callback du changement de saisie)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Image</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Afficher une image</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">painter (ressource image)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Les quatre composants de base de Compose

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Exemple de composants de base</span><span class="dots">···</span>
:::

```
@Composable
fun BasicWidgets() {
    Column {
        Text(text = "Ceci est un texte")
        Button(onClick = { println("Cliqué !") }) {
            Text("Bouton")
        }
        var input by remember { mutableStateOf("") }
        TextField(
            value = input,
            onValueChange = { input = it },
            label = { Text("Saisis quelque chose") }
        )
    }
}
```
:::

Dans les deux lignes du champ de saisie apparaît remember { mutableStateOf("") } — c'est la « magie d'état » de Compose, détaillée en section 5 de ce chapitre. Pour l'instant, contente-toi de la reconnaître de vue.

#### 3. Le trio de mise en page : Column, Row, Box

Les composants sont là, mais comment les disposer ? Retiens trois « boîtes » :

- Column : empile à la verticale (comme une file à la cantine) ;
- Row : aligne à l'horizontale (comme s'asseoir côte à côte) ;
- Box : superpose (comme des cartes empilées, parfait pour les badges d'angle et les masques).

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Le trio de layouts</span><span class="dots">···</span>
:::

```
Column {
    Text("Première ligne")
    Row {
        Text("Gauche")
        Text("Droite")
    }
    Box {
        Text("Couche du dessous")
        Text("badge superposé par-dessus")
    }
}
```
:::

Envie d'une mise en page plus jolie ? Ajoute un Modifier (modificateur) aux composants — c'est comme maquiller les briques :

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Modifier : gestes courants</span><span class="dots">···</span>
:::

```
Text(
    text = "Joli texte",
    modifier = Modifier
        .padding(16.dp)          // marge sur les quatre côtés
        .fillMaxWidth()          // remplit toute la largeur
        .background(Color.Blue)  // couleur de fond
        .clickable { /* au clic */ }// cliquable
)
// appels chaînés : l'un après l'autre ; l'ordre compte (d'abord padding puis fond ; le fond n'inclut pas la marge)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Attention : l'ordre des Modifier compte

{class="mt-1"}
padding(16.dp).background(Blue) et background(Blue).padding(16.dp) ne donnent pas le même résultat — le premier « réserve d'abord la marge puis colore » (le fond ne couvre pas la marge), le second « colore d'abord puis réserve la marge » (le fond inclut la marge). C'est là que les débutants dessinent le plus souvent cette « bordure blanche bizarre ». En cas de doute, inverse l'ordre : l'aperçu te donne la réponse aussitôt.
:::

#### 4. L'état : donner vie à l'interface

Une interface statique, c'est sans intérêt. Pour qu'un bouton ajoute +1 au clic ou qu'un champ accepte la saisie, il faut de l'état (State). La règle de Compose : l'interface reflète toujours fidèlement l'état ; quand l'état change, l'interface se redessine automatiquement.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · État : compteur de clics</span><span class="dots">···</span>
:::

```
@Composable
fun Counter() {
    // remember + mutableStateOf : mémorise cette valeur qui change
    var count by remember { mutableStateOf(0) }

    Column {
        Text(text = "Tu as cliqué $count fois")
        Button(onClick = { count++ }) {   // change l'état
            Text("Appuie +1")                // l'interface se rafraîchit toute seule
        }
    }
}
```
:::

Trois lignes de code, et voilà un compteur vivant. C'est là que Compose se révèle plus agréable que l'ancienne écriture : inutile de « rafraîchir l'interface » à la main, il suffit de changer les données. Retiens deux fonctions clés : remember (empêche la valeur d'être effacée lors de la recomposition de l'interface) et mutableStateOf (dit à Compose « cette valeur a changé, il faut redessiner »).

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hand-pointer mr-1"></i> L'utilisateur clique</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> L'état change (count++)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> Compose détecte le changement</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> Redessine l'interface (recomposition)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figure 3 : le flux de données unidirectionnel « état → interface » de Compose
:::

#### 5. Thème et mode sombre : une configuration, tout l'écran en profite

Le MyFirstAppTheme { ... } du projet modèle, c'est le thème. Basé sur les spécifications de design Material 3, il gère d'un seul tenant couleurs, polices et formes. Trois étapes suffisent pour prendre en charge le mode sombre :

1. Définis dans le thème deux palettes, claire et sombre (le modèle génère déjà la ColorScheme) ;
2. quand le système passe en mode sombre, isSystemInDarkTheme() le détecte automatiquement ;
3. utilise les couleurs fournies par le thème (par exemple MaterialTheme.colorScheme.primary) plutôt que des valeurs de couleur codées en dur.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Petit conseil : les couleurs dynamiques de Material 3

{class="mt-1"}
Depuis Android 12, « Material You » permet à une app d'extraire des couleurs de ton fond d'écran. Le modèle Compose le prend en charge par défaut (dynamicColor). Ton app « change de tenue » automatiquement selon le téléphone de chaque utilisateur : c'est la poésie de l'Android moderne.
:::

#### 6. Aperçu, animations et édition en direct : les « turbo » de Compose

Les trois « turbo » de Compose en matière d'expérience de développement : une fois adoptés, impossible de s'en passer :

- L'aperçu @Preview : ajoute l'annotation @Preview à un Composable et Android Studio rend l'interface instantanément à droite — tu modifies le code avec un rendu immédiat, sans devoir installer à chaque fois sur le téléphone ;
- L'édition en direct (Live Edit) : en 2026, Android Studio sait « recharger à chaud » certaines modifications sur l'émulateur ou l'appareil réel — changer la couleur d'un texte et autres petits ajustements s'appliquent en une seconde sur l'appareil ;
- Les API d'animation : animateFloatAsState et AnimatedVisibility permettent des transitions douces en quelques lignes de code — la « touche pro » se joue souvent à ces quelques dizaines de lignes près.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Animations en dix minutes</span><span class="dots">···</span>
:::

```
@Composable
fun AnimatedBox() {
    var big by remember { mutableStateOf(false) }
    // quand la valeur change, transition douce vers la valeur cible
    val size by animateDpAsState(if (big) 120.dp else 60.dp)

    Box(Modifier
        .size(size)
        .background(MaterialTheme.colorScheme.primary)
        .clickable { big = !big }
    )
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Petit conseil : d'abord la fonction, ensuite l'animation

{class="mt-1"}
Le travers classique des débutants : « se tracasser des animations avant même que l'interface ne soit juste ». Fais d'abord tourner les fonctionnalités, ajoute les effets à la fin — c'est aussi le principe « la simplicité d'abord » : l'animation est la cerise sur le gâteau, la fonctionnalité est le pain quotidien.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
À toi de jouer : fabrique un « bouton d'humeur »

{class="mt-1"}
Transforme le projet modèle en sélecteur d'humeur : un bouton qui, à chaque clic, fait un cycle entre 😀 content → 😢 triste → 😡 fâché, le texte et la couleur de fond changeant à chaque fois. Astuce : utilise when pour choisir le texte et la couleur selon l'état. Envoie-le ensuite jouer à tes amis, et récolte ta première vague de « waouh, tu sais faire des apps ! »
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Résumé du chapitre

- La philosophie de Compose : interface = fonction @Composable, emboîtement en briques
- Les quatre composants majeurs : Text / Button / TextField / Image
- Le trio de mise en page : Column empile, Row aligne, Box superpose
- Les Modifier se maquillent en chaîne : padding, fillMaxWidth, background, clickable — l'ordre a son importance
- L'état est l'âme : remember + mutableStateOf — change les données et l'interface se redessine
- Thème avec Material 3 + couleurs dynamiques ; le mode sombre se configure une fois et s'applique partout
:::
