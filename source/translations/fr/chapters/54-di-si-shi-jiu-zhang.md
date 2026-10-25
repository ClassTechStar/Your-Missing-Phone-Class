---
id: di-si-shi-jiu-zhang
num: 49
part: an-zhuo-kai-fa-pian
nav: Chapitre 49 : Installer l'environnement de développement — Android Studio et le premier projet
toc: default
kind: chapter
---

### Chapitre 49 : Monter l'environnement de développement — Android Studio et le premier projet

{class="chapter-intro mb-4"}
Pour bien faire le travail, il faut d'abord aiguiser ses outils. Dans ce chapitre, on monte la « cuisine » : installer Android Studio, faire tourner l'émulateur, créer ton tout premier projet Android, puis démonter la structure du projet pour bien la comprendre. Une fois l'environnement prêt, tu verras pour la première fois ton code se transformer en un bouton cliquable — un instant que beaucoup gardent en mémoire toute leur vie.

#### 1. Installer Android Studio

Android Studio est l'environnement de développement intégré (IDE) officiel de Google : gratuit, et avec la panoplie complète — écrire du code, prévisualiser l'interface, déboguer, générer le paquet, tout s'y trouve. Quatre étapes pour l'installer :

1. Ouvre le site officiel developer.android.com/studio et télécharge la dernière version stable (en août 2026, une version postérieure à Narwhal ; disponible pour Windows/Mac/Linux) ;
2. lance le programme d'installation et clique sur « Suivant » jusqu'au bout — l'assistant installe automatiquement le SDK Android et les composants de l'émulateur ;
3. au premier lancement, télécharge les composants du SDK comme indiqué (garde les cases par défaut ; prévois quelques minutes et plusieurs Go d'espace) ;
4. à la fin, tu arrives sur la page d'accueil — félicitations, la « cuisine » est montée.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Attention : garde en tête la configuration requise

{class="mt-1"}
Android Studio est un grand mangeur de mémoire : 16 Go de RAM recommandés pour bien démarrer (8 Go suffisent pour tourner, mais l'émulateur sera un peu lent), réserve plus de 20 Go de disque et vérifie que le processeur prend en charge la virtualisation (active VT-x/AMD-V dans le BIOS). Si ton ordinateur est vraiment ancien, tu peux remplacer l'émulateur par le « débogage sur appareil réel » (expliqué en section 4 de ce chapitre) : l'expérience en sera même plus fluide.
:::

#### 2. Créer ton premier projet

Sur la page d'accueil, clique sur New Project, choisis le modèle Empty Activity (le plus épuré pour les débutants), puis remplis trois choses :

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Champ de configuration</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Quoi remplir</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Explication</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">My First App</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Le nom de l'app, affiché sur l'écran d'accueil du téléphone</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Package name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">com.example.myfirstapp</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Identifiant unique au monde ; l'habitude veut qu'on inverse un nom de domaine — garde la valeur par défaut pour l'instant</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Minimum SDK</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">API 26(Android 8.0)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Version minimale prise en charge, couvrant plus de 95 % des appareils</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Les trois choses à remplir à la création du projet

Après avoir cliqué sur Finish, Android Studio télécharge automatiquement les dépendances et construit le projet avec Gradle (compte quelques minutes la première fois, ce sera bien plus rapide ensuite). Une fois la construction terminée, tu as une app qui tourne — même si elle n'affiche encore qu'un simple « Hello Android! ».

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Petit conseil : les subtilités du nom de package

{class="mt-1"}
Le nom de package (package name) est comme le « numéro de carte d'identité » de l'app : il doit être unique dans le monde entier et ne peut plus être changé après publication. Pour t'exercer, com.example.xxx suffit ; pour un vrai produit, remplace-le par ton propre domaine inversé (par exemple com.tonnom.nomdelapp). Ne publie jamais avec com.example — la boutique refuserait l'app.
:::

#### 3. Faire tourner : émulateur et appareil réel

Le code est écrit, il faut maintenant un « téléphone » pour le faire tourner. Tu as deux options :

##### 1. L'émulateur (Emulator)

L'émulateur crée un téléphone Android virtuel dans ton ordinateur. Dans Android Studio, ouvre Device Manager > Create Device, choisis un appareil (les Pixel sont recommandés), sélectionne une image système (avec les Google APIs), télécharge-la, puis démarre-la. Clique ensuite sur le triangle vert Run de la barre d'outils : quelques secondes plus tard, ton app apparaît sur l'écran du « téléphone ».

##### 2. Le débogage sur appareil réel (encore mieux)

Un appareil réel reste l'environnement de test le plus authentique — la sensation du tactile, un vrai réseau, de vrais capteurs : l'émulateur ne peut pas rivaliser. Le débogage sur un téléphone Android est tout simple :

1. Sur le téléphone, ouvre [Réglages] > [À propos du téléphone] et tape 7 fois de suite sur « Numéro de version » pour activer les « Options développeur » ;
2. dans [Options développeur], active le débogage USB ;
3. relie le téléphone à l'ordinateur avec un câble USB et choisis « Autoriser le débogage USB » dans la fenêtre qui s'affiche ;
4. retourne dans Android Studio : ton téléphone apparaît dans la liste déroulante des appareils de la barre d'outils ; clique sur Run.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Piège à éviter : ne laisse pas le débogage USB activé en permanence

{class="mt-1"}
Le débogage USB équivaut à ouvrir une « porte dérobée » à l'ordinateur. Quand tu charges ton téléphone dans un lieu public ou que tu le branches sur un ordinateur dont tu n'es pas sûr, désactive toujours le débogage USB pour empêcher quiconque de lire tes données par ce biais. Prends l'habitude de le couper dès la session de développement terminée.
:::

#### 4. Anatomie du projet : à quoi sert chaque fichier

En ouvrant un projet pour la première fois, l'arborescence de fichiers à gauche peut donner le vertige. Pas de panique : au quotidien, tu passeras 90 % de ton temps avec ces seuls éléments :

::: div .figure
```html
<svg style="max-width:100%;height:auto" width="600" height="300" viewBox="0 0 600 300" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="600" height="300" fill="#fafafa" rx="8"/>
      <text x="20" y="30" font-size="13" font-weight="bold" fill="#111827">MyFirstApp/ racine du projet</text>
      <rect x="30" y="45" width="540" height="230" fill="#ffffff" stroke="#d1d5db" rx="6"/>
      <text x="45" y="70" font-size="11" fill="#4f46e5" font-weight="bold">app/ ← là où tu écris ton code</text>
      <rect x="60" y="82" width="240" height="178" fill="#eef2ff" rx="5"/>
      <text x="70" y="102" font-size="10" fill="#1e1b4b" font-weight="bold">src/main/</text>
      <text x="80" y="120" font-size="10" fill="#374151">├ java/…/MainActivity.kt  ← la logique</text>
      <text x="80" y="138" font-size="10" fill="#374151">├ res/  ← ressources (images, textes, couleurs)</text>
      <text x="80" y="156" font-size="10" fill="#374151">└ AndroidManifest.xml  ← la "carte d'identité" de l'app</text>
      <text x="70" y="180" font-size="10" fill="#1e1b4b" font-weight="bold">build.gradle.kts</text>
      <text x="80" y="198" font-size="10" fill="#6b7280">déclare les bibliothèques dépendantes (version du SDK, Compose, etc.)</text>
      <text x="70" y="222" font-size="10" fill="#1e1b4b" font-weight="bold">src/androidTest/ et test/</text>
      <text x="80" y="240" font-size="10" fill="#6b7280">code de tests automatisés (utilisé au chap. 56)</text>
      <rect x="320" y="82" width="230" height="178" fill="#f0fdf4" rx="5"/>
      <text x="330" y="102" font-size="10" fill="#065f46" font-weight="bold">autres fichiers à la racine</text>
      <text x="340" y="122" font-size="10" fill="#374151">gradle/ + gradlew.bat  ← scripts de build</text>
      <text x="340" y="142" font-size="10" fill="#374151">settings.gradle.kts  ← réglages du projet</text>
      <text x="340" y="162" font-size="10" fill="#6b7280">(règle d'or du débutant : ne touche qu'au dossier app/,</text>
      <text x="340" y="180" font-size="10" fill="#6b7280">pour le reste, considère une "boîte noire", n'y touche pas)</text>
      <text x="340" y="208" font-size="10" fill="#9ca3af">.gitignore  ← liste d'exclusions du gestionnaire de versions</text>
    </svg>
```

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figure 2 : la structure du projet que tout débutant doit connaître (règle d'or : ne touche qu'au dossier app/)
:::

- MainActivity.kt : la « porte d'entrée » de l'app. Quand l'utilisateur touche l'icône, c'est elle qui est réveillée en premier. Dans le modèle actuel, elle se charge d'afficher « Hello Android! ».
- AndroidManifest.xml : le « livret de famille » de l'app — il déclare le nom de l'app, son icône, ses écrans et les permissions nécessaires (appareil photo, localisation, etc.).
- Le dossier res/ : l'entrepôt de ressources, où sont rangées images, icônes, textes et couleurs. Placer les textes dans les fichiers de ressources plutôt qu'en dur dans le code est une bonne pratique Android (pratique pour changer de langue ou de thème).
- build.gradle.kts : la recette de construction — elle déclare la version minimale prise en charge et les bibliothèques dont le projet dépend (Compose, par exemple).

#### 5. Premier essai : remplace « Hello » par ton prénom

Ouvre MainActivity.kt : tu verras le code généré par le modèle Compose. Trouve la ligne Text("Hello Android!"), remplace le texte entre guillemets par ton prénom, par exemple Text("Salut, Jean Dupont ! C'est ma première app"), puis relance avec Ctrl+R (Cmd+R sur Mac). Quelques secondes plus tard, ton prénom s'affiche sur l'émulateur.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · MainActivity.kt (modifie cette ligne)</span><span class="dots">···</span>
:::

```
setContent {
    MyFirstAppTheme {
        Surface(modifier = Modifier.fillMaxSize()) {
            // ▼ remplace ici par ton propre texte
            Text("Bonjour Léa ! Voici ma première app")
        }
    }
}
```
:::

Félicitations : tu viens de boucler un cycle complet « modifier le code → compiler → installer → exécuter ». Ce cycle, c'est le quotidien du développeur pour tous les jours à venir. Tant que le fer est chaud, essaie d'autres modifications : agrandis la taille du texte, change la couleur — le chapitre suivant t'expliquera d'où viennent ces « magies ».

#### 6. Premiers secours contre les erreurs fréquentes : les « urgences » des deux premières semaines

Pendant l'installation de l'environnement et la première construction, tu rencontreras très probablement les trois erreurs suivantes. Pas de panique, chacune a son remède :

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Symptôme de l'erreur</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Cause fréquente</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Remède</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gradle sync failed / téléchargement lent des dépendances</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Accès réseau aux dépôts difficile</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Configure un dépôt miroir chinois pour Gradle (miroirs maven d'Alibaba Cloud ou de Tencent Cloud) ; cherche « gradle miroir chinois » sur Internet et suis les instructions</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Composants du SDK manquants</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Le téléchargement du SDK a été ignoré lors de l'installation</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Complète les plateformes et outils manquants via Settings > SDK Manager</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">L'émulateur ne démarre pas / écran noir</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Virtualisation non activée, image corrompue</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Active VT-x/AMD-V dans le BIOS ; supprime l'émulateur et recrée-le ; ou passe directement au débogage sur appareil réel</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Table de secours des erreurs d'environnement pour débutants

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Petit conseil : la méthode pour chercher une erreur

{class="mt-1"}
La première ligne du message d'erreur est la plus précieuse — copie-la telle quelle dans un moteur de recherche en ajoutant le mot-clé « android studio ». Ne cherche pas des questions vagues du genre « je n'arrive pas à installer mon environnement » ; cherche l'erreur précise, du type « Gradle sync failed: Could not resolve com.android.tools.build ». Aux questions précises, les réponses précises.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
À toi de jouer : accomplis ta liste de « rituel de développeur »

{class="mt-1"}
① Installe Android Studio et fais tourner l'émulateur ; ② exécute ton app une fois sur un appareil réel et garde une capture d'écran en souvenir ; ③ remplace le texte Hello par ton prénom ; ④ compresse le projet et archive-le. Après ces quatre étapes, tu pourras annoncer à tes amis : moi aussi je suis développeur Android (capture d'écran à l'appui).
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Résumé du chapitre

- Android Studio = l'IDE officiel gratuit ; recommandé : 16 Go de RAM + 20 Go de disque + virtualisation activée
- Les trois clés d'un nouveau projet : le nom, le nom de package (unique au monde, ne publie pas avec com.example) et le SDK minimal (à partir de l'API 26)
- Deux façons d'exécuter : l'émulateur (téléphone virtuel dans l'ordinateur) et l'appareil réel (active le débogage USB, pense à le couper ensuite)
- Règle d'or du projet : ne touche qu'au dossier app/ — MainActivity.kt est la porte d'entrée, le Manifest le livret de famille, res/ l'entrepôt de ressources
- Le quotidien du développeur = modifier le code → Run → observer le résultat, encore et encore
:::
