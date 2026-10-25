---
id: di-san-shi-ba-zhang
num: 38
part: ai-biancheng-pian
nav: Chapitre 38 : Les cinq principes de pensée de la programmation par IA
toc: default
kind: chapter
---

### Chapitre 38 : Les cinq grands principes de la programmation IA

{class="chapter-intro mb-4"}
Si ce livre ne devait vous faire retenir qu'un chapitre, ce serait celui-ci. Les cinq principes en sont le cœur ; tous les suivants — contexte, besoins, dialogue, qualité — les déploient dans diverses situations. Rassurez-vous : chacun est simple à comprendre, mais chacun mérite de s'ancrer dans vos réflexes au fil de plusieurs projets.

L'histoire est amusante : en open-sourçant son projet, Andrej Karpathy a joint un fichier CLAUDE.md de seulement 70 lignes, résumant quatre principes de collaboration avec l'IA. Ce fichier a dépassé 70 000 stars sur GitHub et est devenu la référence la plus citée par les praticiens du monde entier. Ces principes ne sont pas des slogans, mais des habitudes de pensée opérationnelles nées de la pratique. Ce livre y ajoute un cinquième — l'itération-vérification — pour former un ensemble complet.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Pourquoi un fichier de 70 lignes vaut-il tant ?

{class="mt-1"}
70 000 stars, c'est colossal : la plupart des projets GitHub n'y parviendront jamais. Qu'un simple texte de 70 lignes les obtienne prouve une chose : à l'ère de l'IA, ce qui manque le plus, ce n'est pas le code, mais la capacité à « penser clairement ». Ces 70 lignes en sont la version concentrée.
:::

#### I. Principe 1 : Think Before Coding (penser avant de coder)

Le plus contre-intuitif des cinq. Si l'IA code pour nous, pourquoi encore penser d'abord ? Réponse simple : la qualité de la production de l'IA est proportionnelle à la qualité de votre entrée. Si vous n'avez pas clarifié ce que vous voulez, l'IA vous enfermera dans un cycle de corrections infinies — ce qu'on appelle « l'IA qui se perd avec vous ».

« Penser d'abord » signifie répondre à trois questions avant de donner une instruction : un « triangle de réflexion » dont aucun sommet ne peut manquer :

1. Quel problème résoudre ? (Objectif)
2. À quoi doit ressembler le résultat ? (Critères d'acceptation)
3. Quelles contraintes respecter ? (Limites)

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Dimension</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Entrée floue (mauvais)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Entrée claire (bon)</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Définition du problème</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Fais-moi un site web</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Fais-moi un site outil personnel avec 3 cartes d'accès vers de petites applications IA</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Résultat attendu</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Quelque chose de joli</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mise en page responsive, thème sombre, animation au survol des cartes, utilisable sur mobile</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Contraintes</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">(non précisées)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pas de framework, HTML+CSS+JS purs, déploiement en fichier unique, pas de backend</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Comparaison entrée floue vs entrée claire pour un même besoin

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Attention : penser d'abord ≠ rédiger un document parfait

{class="mt-1"}
« Penser d'abord » ne signifie pas « écrire un PRD parfait avant de commencer ». C'est une réflexion rapide mais structurée — 30 secondes pour clarifier les trois questions valent mieux que 30 minutes de corrections en boucle. Pour une petite tâche, les trois questions tiennent en quelques mots ; pour un gros projet, on peut les étendre en cahier des charges complet (voir chapitre 40).
:::

#### II. Principe 2 : Simplicity First (la simplicité d'abord)

Le plus grand piège de la programmation IA n'est pas « ne pas y arriver », mais « faire trop ». Dites « fais un système de gestion d'utilisateurs » : l'IA générera authentification, rôles, permissions, journaux d'audit, export de données… alors qu'il vous faut peut-être une simple page de connexion. La surproduction est la première cause de gonflement du code IA.

La simplicité impose le « minimum viable » à chaque instruction : le moins de code possible pour la fonctionnalité centrale, la solution la plus simple pour le problème, le minimum de fonctions pour valider l'idée. Karpathy le résume bien : « Pour calculer un prix remisé, vous n'avez pas besoin d'un moteur e-commerce. »

En pratique, quelques réflexes concrets :

- Ne demandez qu'un point fonctionnel à la fois, pas tout le système d'un coup ;
- Privilégiez la bibliothèque standard et les solutions simples plutôt que des dépendances complexes ;
- Si 50 lignes suffisent, n'acceptez pas 500 ;
- Quand la production dépasse le cadre, osez dire « coupez le superflu ».

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Situation</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Solution excessive (à éviter)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Solution simple (recommandée)</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Stocker des données</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Base MySQL + ORM</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">D'abord un fichier JSON ou SQLite</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Connexion utilisateur</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OAuth2.0 + JWT + rôles et permissions</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">D'abord une simple vérification de mot de passe</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Framework frontend</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">React + Redux + Router</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">D'abord HTML + JS natif</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mise en production</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Docker + CI/CD + K8s</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">D'abord le faire tourner en local</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Solutions excessives vs solutions simples selon les cas

#### III. Principe 3 : Surgical Changes (modifications chirurgicales)

Quand vous itérez sur un projet existant, chaque modification doit être chirurgicale : ne toucher qu'à ce qu'il faut. Essentiel en programmation IA, car l'IA a tendance à « en profiter pour retoucher » : vous demandez de corriger un bug, elle restructure la moitié du fichier.

Exigence centrale : préciser à chaque fois le périmètre et les limites. Dites « ne modifie que la fonction calculate_discount », « ne touche pas au reste », « garde le style de code actuel ». Si l'IA dépasse le cadre, demandez immédiatement d'annuler le superflu.

Karpathy l'illustre avec un diff. Vous demandez d'ajouter une logique « prix membre » au calcul de remise du panier : une bonne production ne touche qu'à cette fonction et ajoute quelques lignes ; une mauvaise restructure tout le fichier — plus « élégant » peut-être, mais impossible de savoir si de nouveaux bugs sont apparus. En programmation IA, « ça a l'air mieux » ne justifie jamais de sortir du cadre.

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
Mauvaise instruction (périmètre flou)

{class="font-mono text-xs leading-relaxed"}
Optimise la logique de remise de ce projet
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
Bonne instruction (périmètre précis)

{class="font-mono text-xs leading-relaxed"}
Ne modifie que la fonction calculate_discount dans cart.py : 1. Ajoute une logique prix membre par-dessus la remise existante 2. Les membres bénéficient de 10 % de remise supplémentaire 3. Ne change ni la signature ni les autres fonctions 4. Garde le style de nommage actuel
:::
:::

#### IV. Principe 4 : Goal-Driven Execution (exécution pilotée par l'objectif)

Ce principe répond à une question clé : faut-il dire à l'IA « comment faire » ou « quoi faire » ? Karpathy choisit la seconde option. Plutôt que « crée une classe, puis ajoute des méthodes, puis écris des tests », dites « j'ai besoin d'un outil qui analyse un CSV et compte les valeurs uniques de chaque colonne ». L'IA choisit son chemin ; vous validez le résultat.

L'avantage est double. L'IA gagne en autonomie et choisit la meilleure voie, libre de vos étapes intermédiaires ; vous passez du « comment » au « est-ce correct » — c'est exactement le travail du Conductor.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Attention : piloté par l'objectif ≠ laisser faire

{class="mt-1"}
Il faut une acceptation stricte après exécution : le résultat répond-il au besoin ? Les cas limites sont-ils traités ? Y a-t-il du surdimensionnement ? Si non, un retour précis — pas « recommence », mais « le problème : une liste vide lève une IndexError à l'entrée ; ajoute une vérification de valeur nulle ».
:::

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Style d'instruction</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Exemple</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Caractéristiques du résultat</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Impératif (comment faire)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">« Crée d'abord une classe Python DataParser, ajoute une méthode parse qui reçoit filename, lis avec le module csv… »</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">L'IA devient une dactylo ; vos étapes intermédiaires ne sont peut-être pas optimales</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Par objectif (quoi faire)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">« J'ai besoin d'un outil : lire un CSV, compter les valeurs uniques par colonne, sortir en JSON. Donne l'implémentation complète. »</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">L'IA choisit la meilleure voie, vous validez le résultat</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Comparaison instruction impérative vs par objectif

#### V. Principe 5 : Iterate and Verify (itérer et vérifier)

Cinquième principe ajouté par ce livre aux quatre de Karpathy. Conviction : la première production de l'IA n'est presque jamais la version finale. Une programmation IA efficace est un cycle « générer-vérifier-corriger », pas un unique « instruction-résultat ».

« Itérer et vérifier » n'est pas un passif « si c'est faux, on retente », mais un processus structuré. Après chaque production, vérifiez sur trois niveaux :

- Niveau 1 · Fonctionnel : ça tourne ? Entrées/sorties correctes ?
- Niveau 2 · Cas limites : entrée vide, très longue, anormale ?
- Niveau 3 · Architecture : structure raisonnable ? Code figé ? Facile à étendre ?

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-bullseye mr-1"></i> Définir l'objectif</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-robot mr-1"></i> L'IA génère le code</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> Vérification fonctionnelle</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> Réussi</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> Vérification des limites</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> Réussi</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-landmark mr-1"></i> Revue de l'architecture</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> Réussi, étape suivante</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-times-circle mr-1"></i> Échoué</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> Donner un retour concret</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> Régénérer</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figure 2 : boucle d'itération-vérification en programmation IA
:::

L'étape clé est le « retour précis ». Si la vérification échoue, ne dites pas « c'est faux, refais », mais « la fonction lève une IndexError avec une liste vide en entrée ; ajoute une vérification de valeur nulle à la ligne 15 ». Un retour précis permet une correction chirurgicale ; un retour flou ne fait que deviner.

#### VI. Harness Engineering : Agent = Modèle + Harness

À la mi-2026, le concept de Harness Engineering s'est répandu dans la communauté. Sa formule est simple :

:::inline div .quote-line .text-center .text-base .font-bold
<strong>Capacité de l'Agent = capacité du modèle × qualité du Harness</strong>
:::

La capacité du modèle est le plafond intellectuel du cerveau de l'IA ; le Harness est le « cadre de travail » autour du modèle — gestion du contexte, intégration d'outils, orchestration, mémoire, etc.

Ce concept explique une confusion courante : pourquoi, avec le même GPT-4 ou Claude, certains réalisent des projets éblouissants et d'autres du code médiocre ? La différence n'est pas dans le modèle, mais dans le Harness. Un bon Harness comprend : un cahier des charges clair, une intégration d'outils cohérente, un contexte ordonné, un processus de validation complet. Le modèle fixe le plafond ; le Harness détermine jusqu'où vous l'exploitez.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
La métaphore du stagiaire de génie

{class="mt-1"}
Imaginez le modèle comme un stagiaire brillant : sans document de contexte, sans liste d'outils, sans échéances ni critères d'acceptation, il ne produira rien de bon. Le Harness Engineering, c'est l'art d'organiser le cadre de travail d'un tel génie.
:::

Les chapitres suivants vous apprennent à construire un bon Harness : chapitre 39 pour la mémoire de projet, 40 pour le cahier des charges (PRD), 43 pour la technologie de dialogue (prompts par couches), 45 pour l'assurance qualité (processus de validation). Ensemble, ils forment votre Harness.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
À vous de jouer : décomposez votre prochaine idée avec le « triangle de réflexion »

{class="mt-1"}
Choisissez une petite idée en attente (page compte à rebours, script de rappel d'hydratation). En 3 minutes : ① quel problème ? ② à quoi ça ressemble ? ③ quelles contraintes (temps, technique, environnement) ? Écrivez les réponses en un paragraphe. Bravo, vous venez de vivre votre premier « Think Before Coding » — ce paragraphe est déjà une instruction de qualité.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Résumé du chapitre

- Les cinq principes viennent du CLAUDE.md de 70 lignes de Karpathy (70K+ stars) ; ce livre ajoute le cinquième : l'itération-vérification
- Think Before Coding : répondre aux trois questions — quoi faire ? quel résultat ? quelles contraintes ?
- Simplicity First : le piège est de « faire trop » — pour un prix remisé, pas besoin d'un moteur e-commerce
- Surgical Changes : modifications chirurgicales, refuser le « j'en profite pour retoucher »
- Goal-Driven Execution : dire « quoi », pas « comment », laisser l'IA choisir sa voie
- Iterate and Verify : trois niveaux (fonctionnel/cas limites/architecture) + retours précis, en boucle
- Harness Engineering : capacité = modèle × Harness, gérer l'IA comme un « stagiaire de génie »
:::
