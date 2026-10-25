---
id: di-si-shi-zhang
num: 40
part: ai-biancheng-pian
nav: Chapitre 40 : Ingénierie des besoins — transformer tes idées en instructions pour l'IA
toc: default
kind: chapter
---

### Chapitre 40 : L'ingénierie des exigences — transformer ses idées en instructions que l'IA peut exécuter

{class="chapter-intro mb-4"}
Si l'ingénierie du contexte répond au problème « faire comprendre le contexte à l'IA », l'ingénierie des exigences répond à « faire savoir à l'IA ce qu'il faut faire précisément cette fois ». C'est l'étape de la programmation IA qui révèle le plus les écarts entre les personnes : avec les mêmes outils et les mêmes modèles, certains produisent des projets bluffants, d'autres des jouets médiocres. La différence tient rarement aux compétences techniques, mais plutôt à la capacité d'exprimer ses exigences.

#### 1. De l'idée floue aux exigences structurées

Chaque projet naît d'une idée floue — « je voudrais faire une appli de comptes », « je voudrais créer un site perso », « je voudrais un outil de liste de tâches ». Ces idées n'ont rien de mauvais en soi, mais si tu les balances telles quelles à l'IA, la qualité du résultat ne dépend que du hasard. L'objectif de l'ingénierie des exigences, c'est de transformer cette idée floue en exigences structurées que l'IA peut exécuter précisément.

Bonne nouvelle : structurer tes exigences ne demande pas un PRD de dizaines de pages. Il te suffit de répondre à cinq questions, que nous appelons les « cinq éléments d'une exigence » :

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Élément</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Question</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Exemple : appli de comptes</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pour qui ?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Usage personnel, pour noter les dépenses et recettes du quotidien</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Quoi ?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Une appli qui enregistre chaque dépense et recette, fait les totaux mensuels et visualise le tout</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pourquoi ?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pour comprendre ma structure de dépenses et repérer les sorties d'argent inutiles</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Comment, en gros ?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">React pour le front, données stockées en local dans le navigateur, pas de back-end ni de connexion pour l'instant</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Quelles contraintes ?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Développement solo, à terminer en 2 semaines, sans mise en ligne</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Les cinq éléments d'une exigence, avec exemples

Pas besoin de rédiger ces cinq éléments dans un document officiel : les passer rapidement en tête suffit. L'essentiel est de prendre l'habitude de « réfléchir avant de parler ». Tu verras : quand tu sais répondre clairement à ces cinq questions, la description de tes exigences se structure naturellement.

#### 2. L'art de découper les exigences par niveaux

Pour les projets un peu gros, une seule description d'exigence ne suffit pas. Il faut découper la grande exigence en sous-exigences petites et vérifiables indépendamment. Ce processus s'appelle le « découpage des exigences », et son principe fondamental est : chaque sous-exigence doit pouvoir être réalisée, vérifiée et livrée indépendamment.

Prenons l'exemple d'« une appli perso de comptes » ; un découpage raisonnable serait :

1. Implémenter la fonction de base d'enregistrement des dépenses et recettes (pouvoir ajouter, consulter, supprimer des entrées) ;
2. Ajouter les catégories (étiqueter chaque entrée : repas, transport, etc.) ;
3. Implémenter le récapitulatif mensuel (statistiques des dépenses et recettes par mois) ;
4. Ajouter la visualisation des données (graphiques de la structure des dépenses).

Chaque étape est un incrément fonctionnel qui peut tourner et se vérifier tout seul.

:::inline div .quote-line
Règle d'or pour découper les besoins : à la fin de chaque étape, le projet doit être "quelque chose d'utilisable", même si les fonctions sont rudimentaires. Ne laisse jamais le projet dans l'état "tout à moitié fait et rien ne marche".
:::

Ce découpage a deux avantages. D'abord, il te permet de toujours voir les progrès : à chaque étape terminée, ton appli gagne une fonction — ce cercle vertueux est vital pour les projets de longue haleine (tout le monde a besoin de ressentir des réussites). Ensuite, il rend chaque tâche de l'IA suffisamment petite, ce qui réduit le risque de « mauvaise interprétation par l'IA » : plus la tâche est petite, plus l'IA la comprend exactement et meilleure est la production.

#### 3. Modèle de PRD et mise en pratique

Pour les projets plus grands (par exemple une application full-stack avec front, back et plusieurs modules), les cinq éléments d'exigence peuvent ne pas suffire. Il te faut alors rédiger un document d'exigences du projet (PRD) plus formel. Un point souvent mal compris : le PRD n'est pas écrit pour l'IA — il est écrit pour toi-même, pour clarifier ta réflexion ; ensuite seulement tu pourras donner à l'IA des instructions plus précises.

Un bon PRD n'a pas besoin d'être long, mais il doit contenir six parties : la présentation du projet (ce que fait le produit, en un paragraphe), la liste des fonctionnalités (ce que fait chaque point), le choix technique (quelle stack, quelle architecture dans les grandes lignes), le modèle de données (les structures de données clés), la description de l'interface (à quoi ressemblent les pages principales) et le plan de développement (en combien d'étapes).

::: div .code-block
:::inline div .code-head
<span>PRD.md</span><span class="dots">···</span>
:::

```
# PRD de l'app de suivi de dépenses personnelles
## Description du projet
Une app légère de suivi de dépenses personnelles : enregistrement des revenus et dépenses, catégories, résumés mensuels et visualisation des données.
## Liste des fonctions
1. Enregistrer une opération : montant, type (revenu/dépense), catégorie, note, date
2. Gestion des catégories : repas, transport, achats, loisirs, autres préchargées
3. Résumé mensuel : revenus totaux, dépenses totales et solde par mois
4. Visualisation des dépenses : camembert avec la part de chaque catégorie
5. Export des données : export CSV
## Solution technique
- Frontend : React + TypeScript + Tailwind CSS
- Stockage : localStorage (pas de backend)
- Graphiques : Chart.js
- Build : Vite
## Modèle de données
Record {
  id: string
  amount: number
  type: 'income' | 'expense'
  category: string
  note: string
  date: string  // YYYY-MM-DD
}
## Plan de développement
Step 1 : enregistrement de base (CRUD)
Step 2 : gestion des catégories
Step 3 : résumé mensuel
Step 4 : visualisation des données
Step 5 : export des données
```
:::

Note le style de rédaction de ce PRD : des listes concises et un format structuré, plutôt que de longues tirades. Chaque fonctionnalité a une définition claire, le modèle de données est décrit avec des types simples. Ce style rend le PRD lisible pour toi, et quand tu le donnes à l'IA, celle-ci comprend précisément chaque exigence.

#### 4. En pratique : le parcours complet de l'idée au plan

La théorie seule, c'est ennuyeux : parcourons tout le processus d'ingénierie des exigences avec un exemple complet. Imaginons que ton idée soit : « je voudrais un traceur d'apprentissage qui suit ce que j'apprends chaque jour ».

Première étape : passe en revue les cinq éléments d'exigence.

- Who : usage personnel.
- What : un outil qui note ce que tu apprends chaque jour, suit le temps d'étude et permet de revoir ta progression.
- Why : créer une habitude d'apprentissage continu et voir tes acquis s'accumuler.
- How : commencer par une version web, avec les données stockées en local dans le navigateur.
- Constraint : développeur débutant complet, fonctions principales à terminer en 1 semaine.

Deuxième étape : découpe les exigences.

1. Étape 1 : implémenter la fonction « enregistrer une entrée d'apprentissage » (date, contenu, durée) ;
2. Étape 2 : ajouter les « statistiques de temps d'étude » (aujourd'hui, cumul de la semaine) ;
3. Étape 3 : implémenter la vue « calendrier d'apprentissage » (affichée comme le graphe de contributions GitHub) ;
4. Étape 4 : ajouter la fonction « révision d'apprentissage » (affiche au hasard les notes d'un jour passé, pour t'aider à réviser).

Troisième étape : rédige un PRD court. Pas besoin de longueur — le découpage ci-dessus constitue déjà l'essentiel du PRD. Range-le dans un fichier .md à la racine du projet, comme référence commune entre toi et l'IA.

Quatrième étape : commence le développement de la première étape. L'instruction à donner à l'IA peut être :

::: div .code-block
:::inline div .code-head
<span>Instruction pour l'IA</span><span class="dots">···</span>
:::

```
J'ai besoin de la première fonction d'un suiveur d'apprentissage : enregistrer des sessions d'étude.
L'utilisateur peut ajouter une entrée avec date, contenu étudié et durée (minutes).
Les données sont stockées dans localStorage.
Frontend en React + TypeScript.
Donne l'implémentation complète.
```
:::

Remarque les caractéristiques de cette instruction : elle décrit uniquement l'objectif de l'étape en cours (la fonction d'enregistrement), sans y mêler d'autres fonctionnalités ; elle fixe les contraintes techniques (React, TypeScript, localStorage) ; elle donne assez d'informations pour que l'IA sache « quoi faire » et « comment s'y prendre », tout en laissant l'implémentation à sa discrétion. Voilà une instruction de programmation IA de qualité, travaillée par l'ingénierie des exigences.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
À toi de jouer : écris une fiche aux cinq éléments pour ton « projet chouchou »

{class="mt-1"}
Choisis un petit projet que tu rumines depuis longtemps et prends 5 minutes pour remplir une fiche : Who / What / Why / How / Constraint, une phrase chacun. Puis découpe-le en 3 à 5 étapes « utilisables dès chaque étape ». Tu verras : une fois l'idée couchée sur le papier, elle passe du « rêve éveillé » à la « liste de tâches ».
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Résumé du chapitre

- Les cinq éléments d'exigence : Who / What / Why / How / Constraint — réfléchis bien avant de te lancer
- La règle d'or du découpage des exigences : après chaque étape, le projet reste « quelque chose d'utilisable »
- Le PRD s'écrit pour soi : présentation, liste des fonctionnalités, choix technique, modèle de données, interface, plan
- Une bonne instruction = décrire seulement l'étape en cours + contraintes explicites + dire « quoi faire » sans dicter « comment faire »
- Le modèle du parcours complet : cinq éléments → découpage → PRD → instruction, en quatre étapes
:::
