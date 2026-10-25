---
id: di-san-shi-jiu-zhang
num: 39
part: ai-biancheng-pian
nav: Chapitre 39 : Ingénierie du contexte — faire comprendre tes intentions à l'IA
toc: default
kind: chapter
---

### Chapitre 39 : Ingénierie du contexte — faire comprendre votre intention à l'IA

{class="chapter-intro mb-4"}
Vous est-il arrivé qu'une nouvelle conversation fasse perdre à l'IA toute mémoire de votre projet ? Ce n'est pas de la malice : elle est « oublieuse » par nature. Ce chapitre vous apprend à lui installer un « système de mémoire longue » et vous fait découvrir l'un des paradigmes les plus en vogue en 2026 : le développement piloté par la spécification.

#### I. Fichier de mémoire de projet : la « mémoire longue » de l'IA

Un modèle d'IA a une limite fondamentale : sa mémoire est de courte durée. Au début de chaque conversation, sa connaissance de votre projet est nulle. Il faut sans cesse rappeler « nous utilisons React », « le backend est Node.js », « la base est PostgreSQL », « les chaînes en doubles guillemets ». Inefficace et source d'oublis — comme réformer chaque jour un nouveau collègue.

Solution : le fichier de mémoire de projet, un fichier texte à la racine du projet que l'outil IA lit automatiquement au début de chaque conversation. Chaque outil a sa convention de nommage :

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Outil</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Nom de fichier</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cursor</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.cursorrules</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Code</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">CLAUDE.md</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GitHub Copilot</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">copilot-instructions.md</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Solution générique</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">AGENTS.md</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Conventions de nommage des fichiers de mémoire de projet

Les noms diffèrent, le principe est le même : y consigner ce que l'IA doit « toujours se rappeler ». Un bon fichier contient : présentation du projet, pile technique, conventions de code (nommage, indentation, commentaires), structure des dossiers, règles de développement (branches, commits, tests). Le CLAUDE.md de Karpathy tient en 70 lignes et couvre l'essentiel — concis mais complet.

::: div .code-block
:::inline div .code-head
<span>CLAUDE.md</span><span class="dots">···</span>
:::

```
# Projet : app de suivi de dépenses personnelles
## Aperçu
C'est une app full-stack de suivi de dépenses qui aide l'utilisateur à enregistrer ses revenus et dépenses quotidiens.
## Stack technique
- Frontend : React + TypeScript + Tailwind CSS
- Backend : Node.js + Express + TypeScript
- Base de données : SQLite (développement) / PostgreSQL (production)
- Tests : Vitest
## Conventions de code
- Utiliser les guillemets doubles
- Indentation de 2 espaces
- Noms de fonctions en camelCase
- Définitions de types en PascalCase
- Chaque fonction doit avoir son commentaire JSDoc
## Structure des dossiers
/src
  /frontend  - code du frontend
  /backend   - code du backend
  /shared    - types partagés frontend/backend
  /tests     - fichiers de test
## Conventions de développement
- Messages de commit en français
- Toute nouvelle fonctionnalité commence par son test
- Les réponses de l'API utilisent toujours le format { success, data, error }
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Attention : ce n'est pas un second cahier des charges

{class="mt-1"}
Surveillez la longueur — pas des dizaines de pages de spécifications. L'objectif est que l'IA « contextualise vite », pas qu'elle décrive chaque fonction en détail. Restez concis, structuré, et ne notez que « ce que l'IA doit savoir ».
:::

#### II. Développement piloté par la spécification (SDD)

Le Spec-Driven Development (SDD) est un paradigme mûri en 2026, en une phrase : écrire la spécification avant le code. Contrairement au TDD, la « spécification » du SDD ne se limite pas aux cas de test : elle inclut la description des besoins, les interfaces, les modèles de données. L'IA génère le code à partir de ces spécifications ; l'humain écrit et maintient les spécifications.

Le flux SDD en cinq étapes :

1. Décrire le besoin en langage naturel (dans un fichier .md) ;
2. Définir interfaces et structures de données (dans la spécification) ;
3. Laisser l'IA générer le code à partir de la spécification ;
4. Exécuter les tests pour vérifier la conformité ;
5. Si non conforme, corriger la spécification ou demander à l'IA de corriger le code.

Dans ce flux, la spécification est la « source de vérité » — le code se régénère, mais la spécification doit d'abord être juste.

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> Rédiger le document de spécifications</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> La spécification est-elle complète ?</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> Complète</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-robot mr-1"></i> L'IA génère le code d'après la spécification</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> Lancer les tests pour vérifier le produit</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-times-circle mr-1"></i> Incomplète / tests échoués</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-tools mr-1"></i> Problème de code → corrige le code ; problème de spécification → corrige la spécification</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> Retour à la vérification</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> Tout est au vert → livraison</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figure 3 : flux de travail du développement piloté par la spécification (SDD)
:::

Avantage du SDD : la spécification est plus stable que le code. Si le modèle ou l'outil change, la spécification reste valable ; il suffit de régénérer le code. D'où l'insistance de ce livre : « la méthodologie prime sur les outils » — la spécification en est le support concret.

#### III. Gestion de la fenêtre de contexte

Même avec un fichier de mémoire, le contexte peut manquer. La fenêtre de contexte (quantité d'informations traitées simultanément) est limitée. Conversations trop longues ou fichiers trop nombreux : l'IA « oublie » le début et la qualité chute — comme un ami qui, après six heures de discussion, a oublié votre première phrase.

Stratégie clé : les références par couches.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Couche de contexte</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Contenu</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Gestion</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Couche 1 : mémoire de projet</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pile technique, conventions, structure des dossiers</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Dans CLAUDE.md etc., chargé automatiquement, sans répétition</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Couche 2 : références de fichiers</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Fichiers de code concernés par la tâche</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Référence précise avec @, sans coller tout le fichier dans la conversation</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Couche 3 : contexte de conversation</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Historique de la tâche en cours</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Nouvelle conversation après chaque tâche, pour éviter le gonflement du contexte</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Couche 4 : instructions immédiates</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Exigences précises de l'étape en cours</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claire, concise, ciblée — éviter les longueurs</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Stratégie de gestion par couches de la fenêtre de contexte

#### 4. Les points clés de la pratique de l'ingénierie du contexte

L'ingénierie du contexte n'est pas un réglage à faire une fois pour toutes, mais un processus d'amélioration continue. Voici quelques points maintes fois éprouvés sur le terrain :

1. Tiens le fichier de mémoire à jour au fil de l'évolution du projet. Quand tu introduis une nouvelle technologie ou changes d'architecture, mets-le à jour immédiatement, au lieu de l'expliquer à la volée dans la conversation.
2. Utilise bien les références @ plutôt que de coller le texte entier. La plupart des outils de programmation IA acceptent la syntaxe @file ou @folder, qui injecte le contenu du fichier dans le contexte de l'IA en arrière-plan — plus efficace qu'un collage manuel, et sans polluer la conversation.
3. Garde des conversations « courtes et percutantes ». Une conversation traite une seule tâche ou un seul point de fonctionnalité ; une fois terminé, ouvre une nouvelle conversation pour la suite. Les longues conversations épuisent la fenêtre de contexte et distraient l'IA.
4. Montre les résultats à l'IA au lieu de les décrire. Face à un bug, référence directement le journal d'erreurs à l'IA avec @, plutôt que de raconter avec tes mots « il semble y avoir une erreur quelque part ». L'IA comprend bien mieux l'information brute que ton résumé.
5. Nettoie et archive régulièrement. Les conversations terminées et les fichiers temporaires encombrent ton espace de travail. Fais périodiquement le ménage des contenus inutiles et garde le répertoire du projet bien rangé : l'IA comprendra d'autant mieux la structure du projet.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
À toi de jouer : écris un fichier de mémoire de 70 lignes pour ton projet

{class="mt-1"}
Choisis un projet en cours (ou prévu) et rédige un CLAUDE.md : présentation du projet (2 ou 3 phrases), stack technique (mets-la en liste), conventions de code (3 à 5 règles), structure des dossiers (dessine un arbre), conventions de développement (2 ou 3 règles). Reste sous les 70 lignes — une fois écrit, tu verras que ta compréhension du projet sera bien plus claire.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Résumé du chapitre

- La mémoire de l'IA est « à court terme » : à chaque nouvelle conversation, elle ne sait rien du projet
- Le fichier de mémoire du projet (CLAUDE.md, etc.) est la « mémoire long terme » de l'IA, chargé automatiquement à chaque conversation
- Un bon fichier de mémoire = présentation + stack + conventions + arborescence + accords, 70 lignes suffisent
- Le SDD (développement piloté par les spécifications) : on écrit d'abord les spécifications, puis le code ; la spécification est la « source unique de vérité », plus stable que le code
- Le contexte se gère en quatre couches : mémoire du projet → références @fichier → historique de conversation → instructions immédiates
- Cinq points de pratique : mises à jour synchronisées, références @, conversations courtes, informations brutes, nettoyage régulier
:::
