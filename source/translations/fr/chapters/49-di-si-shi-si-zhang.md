---
id: di-si-shi-si-zhang
num: 44
part: ai-biancheng-pian
nav: Chapitre 44 : Pratique de zéro à un — le parcours complet d'un projet
toc: default
kind: chapter
---

### Chapitre 44 : De 0 à 1 en pratique — le parcours complet d'un projet

{class="chapter-intro mb-4"}
La théorie est terminée, place à la pratique. Ce chapitre n'est pas un simple tutoriel à recopier : c'est une méthode de terrain pour apprendre « comment penser, comment demander, comment vérifier ». À travers trois projets de difficulté croissante, nous verrons tout le cheminement, du besoin au produit fini. Quel que soit l'outil que tu utilises, ce processus s'applique.

#### 1. Projet 1 : un mini-site d'outils personnels (niveau débutant)

##### 1. Réfléchir au besoin

Objectif : créer une page web d'outils personnels qui présente l'accès à 3 ou 4 petits outils pratiques. C'est un projet purement front-end, sans back-end ni base de données. L'important n'est pas la complexité des outils, mais de vivre le parcours complet « du besoin au produit fini ».

Selon les cinq éléments du besoin : Who — un usage personnel. What — une page web présentant l'accès aux outils. Why — regrouper les outils du quotidien sur une seule page, faciles d'accès. How — un fichier unique HTML+CSS+JS, sans framework. Constraint — à réaliser en 30 minutes, sans déploiement.

##### 2. Donner les instructions

En suivant le principe « Think Before Coding », ton instruction doit contenir assez d'informations pour que l'IA comprenne l'objectif, sans pour autant préciser chaque détail d'implémentation :

::: div .code-block
:::inline div .code-head
<span>Instruction pour l'IA</span><span class="dots">···</span>
:::

```
Crée une page web personnelle d'outils avec ces exigences :
1. HTML en un seul fichier (CSS et JS en ligne), sans framework
2. Thème sombre, style moderne et minimaliste
3. Affiche 4 cartes d'accès aux outils :
   - Résumeur de texte
   - Compteur de mots
   - Sélecteur de couleur
   - Générateur de QR codes
4. Chaque carte avec icône, titre et description courte
5. Les cartes ont une animation au survol
6. Mise en page responsive, utilisable sur mobile
7. Une barre de titre en haut
Donne directement le fichier HTML complet.
```
:::

##### 3. Réception et itération

Quand l'IA fournit le code, fais la réception avec les trois niveaux de vérification itérative. Premier niveau, fonctionnel : le fichier s'ouvre-t-il dans le navigateur ? Les 4 cartes s'affichent-elles toutes ? Les animations au survol fonctionnent-elles ? Deuxième niveau, limites : la mise en page tient-elle sur un écran de téléphone ? Les cartes passent-elles à la ligne quand la fenêtre est très étroite ? Troisième niveau, architecture : le code est-il lisible ? Le CSS est-il regroupé dans une seule balise style ? Y a-t-il des redondances évidentes ?

Si tu veux aussi implémenter la fonction d'un outil (et pas seulement son accès), procède par étapes — ajoute la fonction d'un outil, vérifie, puis ajoute le suivant. C'est l'application concrète de la stratégie des « petits pas rapides ».

#### 2. Projet 2 : une application de comptabilité full-stack (niveau intermédiaire)

##### 1. Réflexion sur le besoin et PRD

Objectif : une application de comptabilité full-stack avec front-end, back-end et base de données. Ce projet est bien plus complexe que le premier et mobilise la méthode d'ingénierie des besoins du chapitre 40.

Commence par rédiger le PRD. Sur le modèle de la section 3 du chapitre 40, décris la vue d'ensemble du projet, la liste des fonctionnalités, la solution technique, le modèle de données et le plan de développement. Pour la technique, applique le principe « Simplicity First » : React côté front mais sans gestion d'état complexe type Redux, Node.js côté back mais sans microservices, SQLite plutôt que PostgreSQL pour la base (en phase de développement).

Le plan de développement se découpe en 5 étapes : étape 1, le squelette de l'API back-end (serveur Express + SQLite + routes CRUD) ; étape 2, les pages de base du front-end (liste des enregistrements + formulaire d'ajout) ; étape 3, la liaison front-back (appels d'API + affichage des données) ; étape 4, les catégories et le filtrage ; étape 5, le récapitulatif mensuel et de simples graphiques. À chaque étape, tu obtiens quelque chose d'utilisable.

##### 2. Créer le fichier mémoire du projet

Avant de coder, crée d'abord le fichier mémoire du projet. C'est la pratique centrale de l'ingénierie du contexte : l'IA connaît le contexte du projet dès le début de chaque conversation.

::: div .code-block
:::inline div .code-head
<span>CLAUDE.md</span><span class="dots">···</span>
:::

```
# Projet : app full-stack de suivi de dépenses
## Aperçu
App de suivi de dépenses personnelles avec enregistrement des revenus et dépenses, catégories et résumés mensuels.
## Stack technique
- Frontend : React + TypeScript + Vite
- Backend : Node.js + Express + TypeScript
- Base de données : SQLite (via better-sqlite3)
- Types partagés entre frontend et backend
## Conventions de l'API
- Chemin de base : /api
- Format de réponse : { success: boolean, data: any, error: string }
- Style RESTful
## Modèle de données
Record { id, amount, type, category, note, date }
## Conventions de code
- Mode strict TypeScript
- Indentation de 2 espaces
- Fonctions avec commentaire JSDoc
- Commentaires et messages de commit en français
```
:::

##### 3. Implémenter pas à pas

Conformément au plan de développement, réalise chaque étape dans une conversation dédiée. Voici un exemple d'instruction pour la première étape :

::: div .code-block
:::inline div .code-head
<span>Instruction pour l'IA (Step 1)</span><span class="dots">···</span>
:::

```
J'ai besoin de créer le squelette de l'API backend.
Exigences :
1. Serveur Express, port 3001
2. Base de données SQLite, table records
3. Champs de la table records :
   id (TEXT PRIMARY KEY)
   amount (REAL)
   type (TEXT: 'income'|'expense')
   category (TEXT)
   note (TEXT)
   date (TEXT: YYYY-MM-DD)
4. Endpoints CRUD :
   GET /api/records - récupérer toutes les entrées
   POST /api/records - ajouter une entrée
   PUT /api/records/:id - mettre à jour une entrée
   DELETE /api/records/:id - supprimer une entrée
5. Middleware de gestion des erreurs
Donne la structure complète du code backend.
```
:::

Note ce qui fait la force de cette instruction : elle décrit uniquement l'étape en cours (le squelette back-end), sans y mêler de besoins front-end ; elle liste clairement les champs et les points d'entrée (assez de contraintes pour l'IA), tout en laissant le détail de l'implémentation à l'IA ; elle suit le principe « Goal-Driven Execution » — dire « quoi faire » plutôt que « comment faire ».

Dès que l'IA fournit le code, vérifie aussitôt : lance le serveur et teste chaque point d'entrée avec curl ou Postman. Une fois tout confirmé, ouvre une nouvelle conversation pour l'étape 2 (les pages de base du front-end). Chaque étape suit la boucle « instruction - vérification - nouvelle conversation ».

#### 3. Projet 3 : une application augmentée par l'IA (niveau avancé)

##### 1. Concevoir le projet

Objectif : une application connectée à l'API d'un grand modèle — par exemple un « assistant d'apprentissage IA » : l'utilisateur saisit un contenu à étudier, et l'IA produit un résumé, relie les notions entre elles et recommande des ressources. La particularité de ce projet : ton application appelle elle-même l'IA, et tu dois gérer l'appel d'API, l'ingénierie des prompts, la gestion des erreurs et autres nouveaux défis.

La leçon la plus importante de ce projet : quand tu « utilises l'IA pour écrire le code qui appelle l'IA », l'ingénierie des prompts demande une attention toute particulière. Les prompts que ton application envoie à l'API du grand modèle doivent eux aussi suivre les principes vus dans ce guide — clarté, concision, orientation objectif.

##### 2. Les points techniques clés

Ce projet soulève plusieurs points techniques que tu n'as pas rencontrés dans les deux premiers :

- Gestion des clés API : une clé ne doit jamais être codée en dur, gère-la via des variables d'environnement ;
- Traitement des réponses en flux : les réponses des grands modèles arrivent généralement en streaming, à afficher mot à mot ;
- Maîtrise de la consommation de tokens : les grands modèles facturent au token, il faut contrôler la consommation au niveau de l'application ;
- Gestion des modèles de prompts : chaque fonction a son propre modèle de prompt, à organiser de façon structurée.

Tu peux confier tous ces points à l'IA, mais tu dois en comprendre le « pourquoi » : pourquoi une clé ne doit pas être codée en dur ? pourquoi des réponses en flux ? pourquoi contrôler la consommation de tokens ? C'est en comprenant le « pourquoi » que tu pourras juger si la solution de l'IA tient la route.

#### 4. La liste de contrôle universelle des projets

Quelle que soit la taille du projet, voici une liste de contrôle universelle pour programmer avec l'IA. À chaque nouveau projet, parcoure-la pour ne rater aucune étape clé.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Phase</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Quoi faire</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Principe associé</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1. Réfléchir au besoin</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Passer en revue les cinq éléments du besoin, clarifier ce que l'on veut faire</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Think Before Coding</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2. Découper le besoin</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Découper le besoin en petites étapes vérifiables une à une</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Simplicity First</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3. Rédiger le PRD</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Le formaliser dans un document structuré, pour s'y référer</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Goal-Driven</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">4. Créer le fichier mémoire</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Créer CLAUDE.md ou un fichier équivalent</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Harness Engineering</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">5. Implémenter pas à pas</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Une conversation par étape : instruction, vérification, étape suivante</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Surgical Changes</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">6. Tester et vérifier</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tester le bon fonctionnement dès chaque étape terminée</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Iterate &amp; Verify</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">7. Relire le code</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Contrôler l'architecture, la sécurité, la maintenabilité</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Iterate &amp; Verify</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">8. Itérer et améliorer</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Affiner par itérations à partir des tests et de la relecture</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Iterate &amp; Verify</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
La liste de contrôle universelle de la programmation IA

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Passe à l'action : termine le « projet 1 » cette semaine

{class="mt-1"}
Prends le « mini-site d'outils » de la section 1 du chapitre 44 comme ton premier devoir de programmation IA : 5 minutes pour les cinq éléments du besoin, envoie l'instruction à l'IA (n'importe quel outil fera l'affaire), puis fais la réception avec les trois niveaux de vérification. Tu as 30 minutes — et voilà ta première réalisation en programmation IA. Une fois terminé, garde-la précieusement : c'est le trophée de ton passage de « lecteur » à « praticien ».
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
L'essentiel du chapitre

- Projet 1 (débutant) : un site d'outils pur front-end — tout le parcours en 30 minutes
- Projet 2 (intermédiaire) : une application de comptabilité full-stack — PRD + fichier mémoire + 5 étapes successives, chacune « utilisable »
- Projet 3 (avancé) : un assistant d'apprentissage IA — écrire avec l'IA le code qui appelle l'IA, en soignant les prompts
- Les huit étapes du processus universel : réflexion sur le besoin → découpage → PRD → fichier mémoire → implémentation pas à pas → tests → relecture → itération
- Chaque étape suit la boucle « instruction - vérification - nouvelle conversation »
:::
