---
id: di-liu-shi-zhang
num: 60
part: ios-kai-fa-pian
nav: Chapitre 60 : Installer l'environnement de développement — Xcode et le premier projet
toc: default
kind: chapter
---

### Chapitre 60 : Monter l’environnement de développement — Xcode et le premier projet

{class="chapter-intro mb-4"}
Pour bien faire le travail, il faut d’abord affûter ses outils. Dans ce chapitre, on monte la « cuisine » : installer Xcode, faire tourner le simulateur, créer le tout premier projet iOS de ta vie, puis décortiquer la structure du projet pour tout comprendre. Une fois l’environnement prêt, tu verras pour la première fois ton code se transformer en bouton cliquable — un instant que beaucoup gardent toute leur vie en mémoire.

#### 1. S’équiper d’un Mac

Commençons par le prérequis : le développement iOS doit se dérouler sur macOS. Sans Mac, trois options : en acheter un (un Mac mini ou un MacBook Air d’occasion suffit largement), louer un Mac dans le cloud pour une courte durée, ou commencer par lire la huitième partie, « Android en pratique » (possible sous Windows).

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Élément de configuration</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Minimum requis</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Zone de confort (recommandé)</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Puce</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple Silicon (M1 ou plus)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">M2 ou plus récent</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mémoire</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">8GB</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">16GB</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Disque</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Prévoir 40 Go et plus (Xcode est bien dodu)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">256 Go pour commencer</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Système</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Le dernier macOS</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mises à jour automatiques maintenues</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Configuration de référence d’un Mac de développement (août 2026)

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Astuce : sans Mac, tu peux déjà apprendre le langage

{class="mt-1"}
Swift Playgrounds, gratuit sur iPad, permet d’apprendre les bases du langage Swift (sans Mac) ; il s’installe même sur iPhone. Familiarise-toi d’abord dans Playgrounds avec les notions de langage du chapitre 61, et tu décolleras dès que tu auras un Mac. Préparer ses outils ne fait jamais perdre de temps : c’est exactement ça.
:::

#### 2. Installer Xcode

Xcode est l’environnement de développement intégré officiel d’Apple, et il est gratuit. Trois étapes suffisent :

1. Sur Mac, ouvre l’App Store, cherche « Xcode » et clique sur Installer — attention, il pèse plusieurs Go, choisis un créneau avec du bon réseau ;
2. au premier lancement après l’installation, accepte le contrat et laisse se terminer l’installation des composants (c’est automatique) ;
3. dans le menu Xcode → Settings → Locations, vérifie que Command Line Tools est bien sélectionné — les outils en ligne de commande sont le préalable de beaucoup de scripts et d’outils tiers.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Attention : le jeu d’appariement entre versions et système

{class="mt-1"}
Un Xcode récent exige souvent le dernier macOS, et un vieux Mac reste coincé sur une version ancienne. Pour publier sur l’App Store, Apple demande une version assez récente de Xcode (avec en général un délai de grâce). Ne reporte donc pas trop les mises à jour du système — les développeurs iOS sont ceux qui courtisent le plus assidûment les nouveautés.
:::

#### 3. Créer ton premier projet

Ouvre Xcode → Create New Project → choisis iOS → le modèle App, puis remplis :

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Élément</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Quoi remplir</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Explication</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Product Name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstApp</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Nom de l’app</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Team</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ton identifiant Apple (gratuit)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pour la signature, un compte personnel suffit</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Organization Identifier</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">com.example</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Se combine au Product Name pour former l’identifiant du bundle</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Interface</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Le framework fil conducteur de ce livre</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Language</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sans commentaire</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Les cinq champs à remplir à la création du projet

Après avoir cliqué sur Create, Xcode génère un projet qui tourne immédiatement. Choisis un simulateur en haut à gauche (par exemple iPhone 17) et clique sur ▶ — quelques secondes plus tard, une fenêtre affichant « Hello, world! » apparaît sur l’écran du simulateur. Ta première app iOS vient de naître.

#### 4. Anatomie du projet : à quoi sert chaque fichier

À gauche se trouve le navigateur de projet ; en tant que débutant, il te suffit de reconnaître ceci :

::: div .figure
```html
<svg style="max-width:100%;height:auto" width="600" height="290" viewBox="0 0 600 290" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="600" height="290" fill="#fafafa" rx="8"/>
      <text x="20" y="28" font-size="13" font-weight="bold" fill="#111827">MyFirstApp/ racine du projet</text>
      <rect x="30" y="42" width="540" height="225" fill="#ffffff" stroke="#d1d5db" rx="6"/>
      <rect x="45" y="56" width="250" height="196" fill="#eef2ff" rx="5"/>
      <text x="56" y="78" font-size="11" fill="#1e1b4b" font-weight="bold">MyFirstApp/ (dossier de code)</text>
      <text x="66" y="100" font-size="10" fill="#374151">├ MyFirstAppApp.swift  ← point d'entrée</text>
      <text x="66" y="120" font-size="10" fill="#374151">├ ContentView.swift  ← écran principal</text>
      <text x="66" y="140" font-size="10" fill="#374151">└ Assets.xcassets  ← icônes, images, couleurs</text>
      <text x="56" y="166" font-size="10" fill="#6b7280">(les nouveaux fichiers vont dans ce dossier)</text>
      <text x="56" y="196" font-size="10" fill="#1e1b4b" font-weight="bold">onglet Info / Info.plist</text>
      <text x="66" y="216" font-size="10" fill="#6b7280">déclaration de l'app : nom, permissions, réglages</text>
      <rect x="310" y="56" width="245" height="196" fill="#f0fdf4" rx="5"/>
      <text x="321" y="78" font-size="11" fill="#065f46" font-weight="bold">autres emplacements importants</text>
      <text x="331" y="100" font-size="10" fill="#374151">📁 Preview Content/  ← éléments d'aperçu</text>
      <text x="331" y="122" font-size="10" fill="#374151"><i class="fas fa-bullseye mr-1"></i> réglages de la Target (icône bleue du projet)</text>
      <text x="331" y="142" font-size="10" fill="#6b7280">——version, système minimal et signature sont ici</text>
      <text x="331" y="168" font-size="10" fill="#374151"><i class="fas fa-flask mr-1"></i> MyFirstAppTests/  ← tests unitaires</text>
      <text x="331" y="188" font-size="10" fill="#374151">📱 MyFirstAppUITests/ ← tests d'interface</text>
      <text x="331" y="216" font-size="10" fill="#9ca3af">(le modèle de tests est déjà généré, utilisé au chap. 67)</text>
    </svg>
```

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figure 2 : la structure d’un projet Xcode que tout débutant doit connaître
:::

- MyFirstAppApp.swift : le point d’entrée du programme ; en SwiftUI, il ne compte que quelques lignes — « démarre, puis affiche l’écran principal » ;
- ContentView.swift : la vue de l’écran principal ; tout ce que tu vois en ce moment est ici ;
- Assets.xcassets : l’entrepôt des ressources — icônes, images et couleurs se rangent ici ;
- Réglages du Target : clique sur l’icône bleue du projet à gauche pour y entrer ; le numéro de version, la version minimale d’iOS et la signature s’y trouvent. Le nom d’affichage de l’app et l’icône se règlent aussi ici.

#### 5. Astuces d’efficacité dans Xcode : les cinq « raccourcis bonus » du débutant

Une fois rodés, ces raccourcis te donneront des allures de « grand pro » :

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Action</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Raccourci</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Effet</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Exécuter</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘R</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Compiler et lancer</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ouvrir/basculer l’aperçu du canevas</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌥⌘↩</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">L’interrupteur du WYSIWYG</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Formater l’indentation</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌃I</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Réajuster automatiquement l’indentation du code sélectionné</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ouvrir un fichier à la volée</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘O</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tape le nom du fichier, il s’ouvre à la seconde (le plus utilisé !)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Commenter/décommenter</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Activer/désactiver du code à la volée pendant le débogage</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Raccourcis très utilisés de Xcode (le kit de cinq du débutant)

Deux bonus cachés : le multi-simulateur (faire tourner en même temps iPhone et iPad pour comparer les dispositions) et la bibliothèque d’extraits de code (glisse tes quelques lignes favorites dans le panneau Snippets à droite, et insère-les en un clic la prochaine fois) — utilise ces outils d’efficacité, et le tour de main viendra tout seul.

#### 6. Débogage sur appareil réel : installer l’app dans ton iPhone

Le simulateur est bien, mais l’appareil réel reste la destination finale. Avec un identifiant Apple gratuit, tu peux déboguer sur un vrai appareil :

1. relie l’iPhone par câble (ou débogue en sans fil sur le même Wi-Fi) ;
2. dans la liste des appareils en haut de Xcode, choisis ton téléphone ; au premier essai, il te proposera de te connecter à ton identifiant Apple et configurera la signature automatiquement ;
3. sur l’iPhone, [Réglages] → [Général] → [VPN et gestion des appareils] → accorde ta confiance au certificat de développeur ;
4. clique sur ▶, et l’app s’installe dans l’appareil réel.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Attention : la « limite de sept jours » du compte gratuit

{class="mt-1"}
Une app signée avec un identifiant Apple gratuit expire au bout de 7 jours (il suffit de relancer une fois pour la renouveler). C’est un mécanisme anti-abus d’Apple, largement suffisant pour la phase d’apprentissage ; le compte développeur payant (99 dollars par an) n’a pas cette limite, le détail au chapitre 67.
:::

#### 7. Premier essai + premiers secours contre les erreurs courantes

Ouvre ContentView.swift, remplace le texte de Text("Hello, world!") par ton prénom, puis relance avec ⌘R — quelques secondes plus tard, ton prénom s’affiche sur le simulateur. Félicitations, tu viens d’accomplir ta première boucle complète « modifier le code → compiler → installer → exécuter ».

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Symptôme d’erreur</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Cause fréquente</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Remède</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Erreur de signature (Signing)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Team non sélectionnée, certificat expiré</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Dans Target → Signing, coche ton compte ; avec un compte gratuit, relance une fois</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Simulateur en écran noir / impossible à ouvrir</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Image corrompue</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menu Device → Erase All Content ; ou supprime le simulateur et recrée-le</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Téléchargement de Xcode trop lent / installation impossible</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Le réseau de l’App Store s’affole</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Change de créneau ; ou télécharge le paquet .xip hors ligne depuis le site des développeurs Apple</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Table de premiers secours contre les erreurs d’environnement du débutant

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
À toi de jouer : achève ta liste des « rituels du développeur »

{class="mt-1"}
① Installe Xcode et fais tourner le simulateur ; ② lance une fois ton app sur un appareil réel et garde une capture en souvenir ; ③ remplace le texte Hello par ton prénom ; ④ dans les réglages du Target, change le nom d’affichage de l’app en « Ma première app ». Ces quatre étapes faites, tu es quelqu’un qui possède une création.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Résumé du chapitre

- Prérequis dur : Mac + Xcode ; sans Mac, commence par apprendre le langage avec Swift Playgrounds sur iPad
- Xcode s’installe depuis l’App Store ; une version neuve exige un système à jour, ne tarde pas à mettre à jour
- Les cinq éléments d’un nouveau projet : nom, Team, identifiant d’organisation, SwiftUI, Swift
- La maxime du projet : tout le code est dans le dossier MyFirstApp/ ; les réglages du Target gèrent version et signature
- Avec un identifiant Apple gratuit, la signature sur appareil réel est limitée à 7 jours ; le compte payant n’a pas cette limite
- Le quotidien du développeur = modifier le code → ⌘R → observer le résultat, encore et encore
:::
