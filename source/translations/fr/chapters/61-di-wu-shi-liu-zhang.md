---
id: di-wu-shi-liu-zhang
num: 56
part: an-zhuo-kai-fa-pian
nav: Chapitre 56 : Peaufiner et publier — mise en ligne sur Google Play
toc: default
kind: chapter
---

### Chapitre 56 : Peaufiner et publier — tests, débogage et mise en ligne sur Google Play

{class="chapter-intro mb-4"}
Ton app est faite, et maintenant ? Ce chapitre répond aux trois questions qui mènent de « ça tourne » à « c’est livrable » : comment déboguer efficacement pour trouver les bugs, comment écrire des tests pour prévenir les régressions, et comment envoyer l’app sur Google Play pour que le monde entier la télécharge. La publication n’est pas qu’une cérémonie — c’est le tournant qui transforme une création en produit.

#### 1. Les trois armes du débogage : Logcat, points d’arrêt, inspecteur d’UI

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Outil</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">À quoi ça sert</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Comment l’utiliser</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Logcat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Consulter les logs du système et les siens</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Dans le code : Log.d("TAG","valeur=$x"), puis filtre en cherchant TAG dans le panneau</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Débogage par points d’arrêt</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Arrêter le programme sur une ligne donnée pour voir les valeurs des variables</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Clique à côté du numéro de ligne pour faire apparaître un point rouge, lance en mode Debug et avance pas à pas</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Layout Inspector</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Observer la structure de l’interface en cours d’exécution</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menu Tools → Layout Inspector, pour voir l’arbre des composants en temps réel</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Les trois armes du débogage

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Astuce : comment lire un message d’erreur ?

{class="mt-1"}
Après un plantage, Logcat affiche une pile rouge (stacktrace) : remonte du bas vers le haut jusqu’à la première ligne qui commence par ton propre nom de package (par exemple com.example.yourapp) — cette ligne est en général la scène du crime. Regarde d’abord le « type d’exception » (pointeur nul ? conversion de type ?), puis la ligne « at ... tonfichier:ligne ». Cette méthode résout 80 % des plantages.
:::

#### 2. Les tests : une assurance pour ton code

Le test manuel ne suffit pas : tu modifies une fonctionnalité, une autre casse en silence. Les tests sont à la fois la « pilule du remords » et le « gilet pare-balles ». Les tests Android se divisent en trois niveaux ; commence par maîtriser le premier :

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Niveau</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ce qu’on teste</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Où les placer</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Vitesse</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tests unitaires</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Logique pure (calculs, validations)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">app/src/test/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Quelques secondes</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tests instrumentés</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Le comportement de l’interface sur un appareil réel</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">app/src/androidTest/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Quelques minutes</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tests manuels</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Le ressenti et l’expérience d’un humain</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">——</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Toujours nécessaires</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Les trois niveaux de tests

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Exemple de test unitaire</span><span class="dots">···</span>
:::

```
// extraire en fonction pure la logique de "convertir le texte du montant en nombre"
fun parseAmount(input: String): Double? {
    val v = input.trim().toDoubleOrNull()
    return if (v != null && v > 0) v else null
}

// teste-la (JUnit4)
@Test
fun emptyInputReturnsNull() {
    assertEquals(null, parseAmount(""))
}
@Test
fun negativeReturnsNull() {
    assertEquals(null, parseAmount("-5"))
}
@Test
fun normalValueParses() {
    assertEquals(12.5, parseAmount("12.5"))
}
```
:::

La validation des montants et les calculs statistiques du carnet de comptes devraient tous être couverts par des tests unitaires. Pour lancer les tests : clic droit sur le dossier test → Run. Tout est au vert ? Tu peux modifier ton code l’esprit tranquille.

#### 3. Signer et empaqueter : apposer le « sceau » sur ton app

Android exige que chaque package d’installation soit signé — comme un cachet officiel qui prouve « ce package vient de moi et n’a pas été altéré ». En débogage, Android Studio utilise automatiquement la signature debug ; pour publier, il te faut ta propre signature release. La procédure :

1. Menu Build → Generate Signed Bundle / APK ;
2. crée le fichier keystore (magasin de clés) — définis un mot de passe et conserve-le précieusement ;
3. choisis release au format AAB, et la construction est terminée.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Attention au piège : keystore perdu = app perdue

{class="mt-1"}
Après la mise en ligne, toute mise à jour de l’app doit utiliser la même signature, sinon la boutique refusera la mise à jour. Si le fichier keystore ou le mot de passe est perdu, tu n’as plus qu’à créer une nouvelle app et la publier à nouveau — tous les anciens utilisateurs restent sur le carreau. Sauvegarde impérativement le keystore et le mot de passe dans un endroit sûr (cloud chiffré + carnet de notes) : c’est l’une des leçons les plus chères de l’histoire des développeurs Android.
:::

#### 4. Le parcours complet de publication sur Google Play

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> Créer le compte de développeur</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-invoice mr-1"></i> Préparer les éléments de la boutique</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-box mr-1"></i> Téléverser l'AAB</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-clipboard-list mr-1"></i> Remplir le formulaire de sécurité des données</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> Validation (de quelques heures à quelques jours)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-party-horn mr-1"></i> Publier</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figure 6 : les six étapes de la publication sur Google Play
:::

- Inscription : des frais uniques de 25 dollars, avec un compte Google utilisable ;
- Éléments : icône de l’app (512×512), captures d’écran (au moins 2), description des fonctionnalités, lien vers la politique de confidentialité (obligatoire dès qu’on collecte des données) ;
- Formulaire de sécurité des données : déclare honnêtement quelles données sont collectées — un carnet de comptes hors ligne peut revendiquer « zéro collecte » ;
- Examen : la première publication d’un nouveau compte passe souvent par une vérification humaine, de quelques heures à quelques jours ; en cas de rejet, corrige selon les remarques.

Note pour les utilisateurs en Chine : Google Play nécessite un environnement réseau particulier, et la distribution en Chine continentale passe généralement par les boutiques locales (Huawei, Xiaomi, Yingyongbao, etc.). Le processus de publication y est similaire, mais chaque boutique a ses propres critères d’examen — un même AAB/APK peut être distribué sur plusieurs boutiques. Pour t’entraîner, réussir une seule boutique est déjà une victoire.

#### 5. Réussir les éléments de la fiche boutique : la première impression, c’est le nombre de téléchargements

La fiche de la boutique est la vitrine que voient les utilisateurs en « promenade ». Trois éléments déterminent la première impression :

- Icône : 512×512, ne te contente pas d’une capture d’écran. Sans talent en design, génère une forme géométrique épurée avec un outil d’IA ; elle n’est valide que si on la reconnaît d’un coup d’œil une fois réduite sur l’écran d’accueil du téléphone ;
- Captures d’écran : au moins 2, idéalement 4 à 6, montrant les scénarios les plus essentiels ; accompagne chacune d’une phrase en langage humain (« Notez une dépense en une seconde » vaut dix fois mieux que « Une solution efficace de gestion des comptes ») ;
- Description : la première phrase doit dire clairement « ce que c’est + pour qui », sans entasser les « le plus pro, le plus puissant » — le classement de la boutique dépend surtout des mots-clés et du taux de conversion en téléchargements, et la sincérité bat l’exagération.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Astuce : compare-toi aux autres

{class="mt-1"}
Avant de publier, fais un tour dans le top 10 des apps du même genre sur la boutique et compare les captures : quel style d’icône ? quels arguments mettent-ils en avant ? comment écrivent-ils leurs titres ? S’inspirer n’est pas plagier — apprends les codes et remplace par ton propre contenu : c’est la leçon la plus rapide pour lancer n’importe quel produit.
:::

#### 6. Petite liste : optimisation des performances et signalement des plantages

Avant de publier ton app, ces deux tâches méritent chacune une demi-heure :

##### 1. Les quatre points d’autocontrôle des performances

1. Utilise LazyColumn pour les listes : ne dispose jamais une longue liste avec Column brut — le chargement paresseux est la première leçon de performance sur Android ;
2. Ne balance pas les images en pleine résolution : utilise la bibliothèque Coil pour redimensionner et mettre en cache automatiquement — une image brute de 5 Mo suffit à faire ramer à mort un téléphone d’entrée de gamme ;
3. Évite les travaux lourds sur le thread principal : base de données, réseau, gros fichiers, tout se fait dans des coroutines ;
4. Mesure avec le Profiler : l’analyseur de performances intégré à Android Studio montre la mémoire, le CPU et la consommation d’énergie — mesurer d’abord, optimiser ensuite, jamais au doigt mouillé.

##### 2. Le signalement des plantages

Que ton app ne plante pas pendant tes tests ne garantit rien sur le téléphone des utilisateurs. Avant la publication, intègre Firebase Crashlytics (officiel Google, gratuit) : quelques lignes de configuration, et à chaque plantage la pile d’erreurs est remontée automatiquement — dans la console, tu vois « quel modèle, quelle version, quelle ligne ». Publier sans suivi des plantages, c’est conduire les yeux bandés.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
À toi de jouer : « livre » une fois ton carnet de comptes

{class="mt-1"}
① Ajoute 3 tests unitaires à la logique parseAmount et consorts ; ② provoque toi-même un plantage, attrape-le avec Logcat et répare-le ; ③ génère un APK signé en release et envoie-le à un ami pour l’installer (c’est ça, la cérémonie de la « création ») ; ④ si tu as du temps, crée un compte développeur et soumets réellement le carnet de comptes à la publication. Les trois premières étapes se bouclent ce soir.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Résumé du chapitre

- Les trois armes du débogage : Logcat pour les logs, les points d’arrêt pour les variables, Layout Inspector pour l’interface
- Lire un plantage : remonte la pile du bas vers le haut jusqu’à la première ligne portant ton nom de package
- Trois niveaux de tests : unitaires (en secondes, commence par ceux-là) / instrumentés / manuels
- Publier, c’est signer obligatoirement : sauvegarde le keystore et le mot de passe, sinon ton app « change de propriétaire »
- Six étapes de publication : inscription → éléments → envoi de l’AAB → formulaire de sécurité des données → examen → mise en ligne
:::
