---
id: di-wu-shi-er-zhang
num: 52
part: an-zhuo-kai-fa-pian
nav: Chapitre 52 : Les quatre composants et le cycle de vie des Activity
toc: default
kind: chapter
---

### Chapitre 52 : Les quatre composants et le cycle de vie de l'Activity

{class="chapter-intro mb-4"}
Si Compose est le « visage » de l'app, ce chapitre parle de son « squelette ». Android possède quatre composants fondamentaux, et toutes les apps sont assemblées à partir d'eux ; le plus important d'entre eux, l'Activity, a un « schéma de cycle de vie » que tout développeur Android doit graver dans sa tête. À la fin de ce chapitre, tu comprendras enfin des énigmes intemporelles comme « pourquoi, au retour de l'arrière-plan, l'état de mon app a disparu ? »

#### 1. Les quatre composants : les piliers d'Android

Android définit officiellement quatre composants de base, chacun chargé d'un type de travail :

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Composant</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Rôle</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">L'image pour comprendre</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Activity</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Un écran visible</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">La devanture de la boutique — visible et manipulable par l'utilisateur</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Service</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">L'« invisible » qui travaille en arrière-plan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">L'ouvrier d'entrepôt — jouer de la musique, télécharger des fichiers, sans interface</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">BroadcastReceiver</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Recevoir les diffusions du système</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Le poste de gardiennage — le haut-parleur qui annonce « batterie bientôt vide », « réseau coupé »</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ContentProvider</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Partager des données entre apps</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Le meuble à dossiers public — partager les contacts avec d'autres apps, par exemple</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Aperçu des quatre composants d'Android

Au stade débutant, tu passeras 95 % de ton temps avec l'Activity ; tu utiliseras Service et BroadcastReceiver pour lire de la musique ou envoyer des notifications ; ContentProvider est le moins employé (le système encapsule déjà les données courantes). Autre point à noter : les quatre composants doivent être « déclarés » dans AndroidManifest.xml — sans déclaration, le système ne les trouve pas.

#### 2. Le cycle de vie de l'Activity : la première « carte au trésor » du développeur Android

Une app sur téléphone peut être interrompue à tout moment : un appel arrive, l'utilisateur bascule vers WeChat pour répondre, le système manque de mémoire et te supprime… La vie d'une Activity est un voyage en boucle sur ce schéma :

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onCreate (naissance : initialisation)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onStart (visible)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onResume (au premier plan)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center">onPause (partiellement masqué)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center">onStop (complètement invisible)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center">onDestroy (détruit)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center">🔁 onRestart / onStart / onResume : au retour au premier plan, même chemin en sens inverse</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figure 4 : le cycle de vie de l'Activity (sens de parcours : rangée du haut pour naître → rangée du bas pour quitter ; au retour, on remonte le même chemin)
:::

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Callback</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Quand il est déclenché</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Usage typique</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onCreate</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">À la création de l'Activity (une fois)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Charger l'interface, initialiser les données</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onStart</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">L'interface devient visible</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Démarrer une logique légère</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onResume</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Prend le focus, devient interactive</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lancer les animations, reprendre la lecture</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onPause</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Partiellement masquée ou quittée à l'instant</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mettre les animations en pause, sauvegarder le brouillon</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onStop</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Totalement invisible</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Libérer les ressources lourdes, mettre les téléchargements en pause</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onDestroy</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Avant la destruction</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Le grand ménage final</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Les usages typiques des six callbacks du cycle de vie

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Piège à éviter : la rotation de l'écran « tue » l'Activity

{class="mt-1"}
La scène de chute la plus classique chez les débutants : l'app pivote et tout le texte des champs de saisie disparaît. La cause : par défaut, une rotation détruit et recrée l'Activity (en passant par onDestroy puis onCreate). La solution : enregistrer l'état avec rememberSaveable (le remplaçant de remember dans Compose), qui retrouvera automatiquement les valeurs à la recréation. Tu l'utiliseras souvent aux chapitres 6 et 7.
:::

#### 3. L'Intent : le « billet » qui circule dans l'app et au-dehors

L'Intent (intention) est le « billet » de communication entre composants. Pour sauter d'un écran à un autre, ouvrir le navigateur ou lancer l'appareil photo, il faut « acheter son billet et monter à bord » :

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Naviguer avec Intent</span><span class="dots">···</span>
:::

```
// méthode 1 : Intent explicite — on précise clairement vers quelle page aller
val intent = Intent(this, DetailActivity::class.java)
intent.putExtra("name", "Léa")     // emporte des "bagages" dans la voiture (les données)
startActivity(intent)

// méthode 2 : Intent implicite — tu dis seulement quoi faire, le système trouve qui le fait
val web = Intent(Intent.ACTION_VIEW, Uri.parse("https://developer.android.com"))
startActivity(web)   // le système ouvrira le navigateur (ou te laissera choisir)
```
:::

Les deux modes ont chacun leur usage : l'explicite pour naviguer entre les écrans de ta propre app ; l'implicite pour faire appel aux capacités du système ou d'autres apps (ouvrir une page web, appeler, partager). Dans un projet Compose, récupère le Context dans un Composable avec LocalContext.current, et tu pourras appeler startActivity.

#### 4. Écrans multiples et navigation

Les vraies apps ont plusieurs écrans. La solution de navigation officiellement recommandée pour Compose est Navigation Compose (bibliothèque androidx.navigation) :

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Squelette de Navigation Compose</span><span class="dots">···</span>
:::

```
val navController = rememberNavController()

NavHost(navController, startDestination = "home") {
    composable("home") { HomeScreen(navController) }
    composable("detail/{name}") { entry ->
        val name = entry.arguments?.getString("name")
        DetailScreen(name ?: "Inconnu")
    }
}

// pour naviguer depuis l'écran :
navController.navigate("detail/Léa")     // avec paramètre
navController.popBackStack()              // revenir à la page précédente
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Petit conseil : et quand les écrans se multiplient ?

{class="mt-1"}
Quand le projet grandit, regroupe toutes les routes des écrans dans un seul fichier (par exemple AppNavGraph.kt) pour les gérer d'un seul tenant — ne disperse pas la logique « où va-t-on ? » dans chaque écran. C'est le premier pas de « ça tourne » vers « c'est maintenable ».
:::

#### 5. Au passage : c'est quoi un Fragment (et pourquoi ce livre ne l'enseigne pas)

En fouillant les anciens tutos, tu tomberas forcément sur le Fragment — un « fragment d'interface réutilisable » au sein d'une Activity, acteur absolu des anciennes architectures multi-écrans. Mais à l'ère de Compose, les fonctions Composable + les routes de Navigation suffisent, et l'éditeur officiel a relégué le Fragment au second plan. C'est pourquoi ce livre ne l'a pas mis dans son fil principal.

Mon conseil : dans un nouveau projet, n'utilise pas de ta propre initiative les Fragments ; mais en lisant du vieux code ou en entretien, sache simplement que c'est un « fragment d'interface enchâssé dans une Activity ». Pour tes ressources d'apprentissage, choisis toujours en priorité ce qui est postérieur à 2023 — le « vieil almanach » de la pile technique Android se périme plus vite qu'on ne l'imagine.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
À toi de jouer : donne une « mémoire » au compteur

{class="mt-1"}
Retravaille le compteur du chapitre 51 : ① remplace remember par rememberSaveable et fais pivoter l'écran pour vérifier que le chiffre reste en place ; ② ajoute un bouton « À propos » qui, via Navigation, mène à un second écran affichant le numéro de version ; ③ imprime des logs (Log.d) dans onCreate/onPause des deux écrans et observe dans Logcat l'ordre d'appel du cycle de vie. Ces trois étapes accomplies, le cycle de vie cessera d'être de la théorie.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Résumé du chapitre

- Les quatre composants : Activity (la devanture), Service (l'arrière-plan), BroadcastReceiver (le haut-parleur), ContentProvider (le meuble à dossiers)
- Les six callbacks du cycle de vie : onCreate → onStart → onResume → onPause → onStop → onDestroy
- La rotation détruit et recrée l'Activity : préserve l'état avec rememberSaveable
- L'Intent est le « billet » : explicite pour naviguer dans l'app, implicite pour les capacités du système
- Les écrans multiples avec Navigation Compose : NavHost + routes composable
:::
