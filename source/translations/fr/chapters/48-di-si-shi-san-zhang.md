---
id: di-si-shi-san-zhang
num: 43
part: ai-biancheng-pian
nav: Chapitre 43 : Ingénierie de la conversation — techniques de dialogue efficaces
toc: default
kind: chapter
---

### Chapitre 43 : L'ingénierie du dialogue — bien communiquer avec l'IA

{class="chapter-intro mb-4"}
Le dialogue est le mode d'interaction central de la programmation avec l'IA. Mais attention : « dialoguer » ne veut pas dire « bavarder » — une conversation efficace avec l'IA est une technique de communication structurée, que nous appelons « ingénierie du dialogue ». Son objet : obtenir du code de la meilleure qualité possible en un minimum de tours de conversation. En clair, ce chapitre t'apprend à « te faire comprendre » de l'IA.

#### 1. La stratégie des prompts par niveaux

Une conversation avec l'IA se divise en trois niveaux, chacun remplissant une fonction différente. Une fois ces trois niveaux compris, tu pourras assembler des prompts efficaces comme des briques de Lego.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Niveau</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Fonction</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Exemple</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Fréquence</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Niveau système</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Définir le rôle de l'IA et les contraintes globales</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">« Tu es un expert React, tout le code doit être en TypeScript »</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">À définir une fois au début du projet</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Niveau tâche</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Décrire la tâche précise à réaliser</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">« Crée un composant formulaire avec des champs nom d'utilisateur et mot de passe »</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">À donner au début de chaque tâche</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Niveau retour</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Évaluer et corriger ce que produit l'IA</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">« Le champ mot de passe n'a pas de bouton afficher/masquer, ajoute-le »</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">À donner selon la qualité du résultat</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Les trois niveaux du prompt en conversation

Le prompt du niveau système s'écrit généralement dans le fichier mémoire du projet (comme CLAUDE.md) et n'a pas besoin d'être répété à chaque conversation. Le niveau tâche est celui que tu utiliseras le plus souvent — il doit contenir trois éléments : « quoi faire », « avec quelle technologie » et « quelles contraintes ». Le niveau retour est le plus exigeant : un bon retour permet à l'IA de se corriger avec précision, un mauvais ne fait que la relancer dans ses conjectures.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Astuce : les trois coups du feedback

{class="mt-1"}
Un modèle de retour bien utile : « signaler le problème + préciser l'attendu + donner du contexte ». Par exemple : « la gestion d'erreurs de la ligne 25 se contente d'un console.log (le problème), en production il faut un gestionnaire d'erreurs unifié qui renvoie des messages compréhensibles pour l'utilisateur (l'attendu), le projet dispose d'une fonction handleError (le contexte) ». Ce type de retour est dix fois plus efficace qu'un simple « corrige la gestion d'erreurs ».
:::

#### 2. Le dialogue de débogage : décrire une erreur pour que l'IA la localise vite

Le débogage est l'un des scénarios les plus fréquents de la programmation avec l'IA. Face à un bug, la façon dont tu décris le problème à l'IA détermine directement sa capacité à le localiser et le corriger rapidement. Voici les quatre clés d'un dialogue de débogage efficace :

1. Montre à l'IA l'information brute, pas ton résumé. Cite directement les journaux d'erreurs, les piles d'exceptions et le code concerné avec @, au lieu de dire « il y a comme une erreur quelque part ». L'IA analyse l'information première avec plus de précision que ton interprétation.
2. Décris l'écart entre le « comportement attendu » et le « comportement constaté ». « Je m'attends à ce qu'un clic sur le bouton mène à la page d'accueil (attendu), mais en réalité rien ne se passe (constaté) » — ce genre de description est bien plus utile qu'un « le bouton est cassé ».
3. Donne les étapes de reproduction. « Je saisis d'abord le nom d'utilisateur, puis je clique sur le bouton de connexion, et l'erreur apparaît » — ces étapes permettent à l'IA de rejouer ton parcours et de cerner plus facilement le problème.
4. Dis clairement ce que tu as déjà essayé. « J'ai vérifié la requête réseau : elle renvoie 200 et les données sont correctes » — cela aide l'IA à écarter les pistes déjà validées, sans perdre de temps à les explorer à nouveau.

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
Mauvaise description du bug

{class="font-mono text-xs leading-relaxed"}
Le bouton ne réagit pas au clic, regarde ça
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
Bonne description du bug

{class="font-mono text-xs leading-relaxed"}
Clic sur le bouton de connexion : la page ne réagit pas. Comportement attendu : après le clic, redirection vers la page /home Comportement constaté : aucune réaction au clic, aucune erreur dans la console Étapes de reproduction : 1. Saisir le nom d'utilisateur admin et le mot de passe 123456 sur la page de connexion 2. Cliquer sur le bouton « Connexion » 3. La page ne réagit pas Pistes déjà vérifiées : - La requête réseau fonctionne et renvoie 200 - L'événement onClick est bien lié - Le code du composant LoginButton a été inspecté Fichiers concernés : @src/components/LoginButton.tsx @src/pages/Login.tsx
:::
:::

#### 3. Stratégies d'itération : petits pas rapides ou grande refactorisation

L'itération en programmation IA repose sur deux stratégies de base, adaptées à des contextes différents. Comprendre leur différence t'aide à choisir juste selon la situation.

La stratégie des « petits pas rapides » convient au développement de fonctionnalités et à la correction de bugs. Son principe : demander à l'IA une seule petite modification à la fois, vérifier, puis passer à la suivante. Avantages : chaque étape est vérifiable et réversible, le risque reste maîtrisé. Inconvénients : c'est plus lent et cela demande des allers-retours fréquents. Idéal pour : développer une nouvelle fonctionnalité, explorer quand la meilleure solution n'est pas évidente, itérer prudemment quand tu n'es pas très sûr de ce que produit l'IA.

La stratégie de la « grande refactorisation » convient aux modifications d'envergure dont l'objectif est clair. Son principe : décrire l'objectif complet en une fois et laisser l'IA planifier et exécuter toute la transformation. Avantages : c'est rapide et l'IA, voyant l'image d'ensemble, prend de meilleures décisions d'architecture. Inconvénients : le risque est élevé — si l'IA a mal compris, la correction coûte cher. Idéal pour : une montée en version d'architecture bien définie, une migration de code massive, une refactorisation bien couverte par les tests.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Critère</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Petits pas rapides</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Grande refactorisation</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ampleur de chaque modification</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Une fonctionnalité ou un bug</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Un module ou une couche d'architecture</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Fréquence de vérification</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Vérification immédiate après chaque modification</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Vérification globale une fois tout terminé</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tours de conversation</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Nombreux (5 à 10 par fonctionnalité)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Peu nombreux (1 à 3 par module)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Risque</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Faible, chaque étape est réversible</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Élevé, corriger un écart coûte cher</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cas d'usage</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Nouvelles fonctionnalités, développement exploratoire</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Refactorisation ou migration à objectif clair</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Prérequis</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Aucun prérequis particulier</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Exige une couverture de tests</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Comparaison des deux stratégies d'itération

En pratique, les deux stratégies se combinent souvent. Par exemple, pour refactoriser un module : commence par la « grande refactorisation » pour que l'IA propose un plan d'ensemble, examine-le, puis exécute-le pas à pas à coups de « petits pas rapides ». Tu gardes ainsi la vue d'ensemble tout en maîtrisant le risque d'exécution.

#### 4. La gestion du contexte dans les conversations à plusieurs tours

À mesure que la conversation s'allonge, tu dois gérer activement son contexte pour éviter le problème de l'« IA qui oublie les informations du début ». Voici quelques techniques bien utiles.

Première technique : « ancrer » les informations clés. Dès le début de la conversation, écris noir sur blanc les contraintes essentielles, puis rappelle-les au bon moment. Par exemple : « Retiens que nos données sont stockées en localStorage, pas de base de données » — redis cette contrainte dans les demandes de modification concernées pour éviter que l'IA ne l'oublie.

Deuxième technique : joue sur le duo « résumé-reprise ». Quand la conversation devient très longue, demande à l'IA de « résumer l'avancement et les tâches restantes », puis ouvre une nouvelle conversation qui démarre avec ce résumé. Tu conserves le contexte essentiel tout en évitant la dégradation des longues conversations.

Troisième technique : « une conversation, une tâche ». C'est la stratégie la plus simple et la plus efficace. Chaque conversation ne traite qu'une seule tâche ou fonctionnalité ; une fois terminée, tu en ouvres une nouvelle pour la suivante. Cela limite naturellement la longueur des échanges et garde le contexte clair.

Quatrième technique : exploite la gestion de contexte des outils. La plupart des outils de programmation IA ont un bouton « effacer le contexte » ou « nouvelle session » — quand tu sens que la qualité des réponses se dégrade, n'hésite pas : ouvre une nouvelle session. Perdre un peu d'historique vaut bien mieux que continuer à lutter dans un contexte dégradé.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Passe à l'action : joue le « patient » avec ton IA

{class="mt-1"}
Crée exprès une petite page dans le navigateur, avec un bug volontaire (un bouton sans réaction, par exemple). Puis décris-le une fois à l'IA en suivant le modèle de « bonne description du bug » de ce chapitre : informations brutes, attendu vs constaté, étapes de reproduction, pistes déjà vérifiées. Sens la différence de vitesse avec laquelle l'IA cible le problème — tu comprendras pourquoi « bien décrire un problème » est un savoir-faire à part entière.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
L'essentiel du chapitre

- Trois niveaux de prompt : système (dans le fichier mémoire), tâche (quoi faire + technologie + contraintes), retour (problème + attendu + contexte)
- Quatre clés du débogage : informations brutes, attendu vs constaté, étapes de reproduction, pistes déjà vérifiées
- Petits pas rapides : risque faible, nombreux tours, idéal pour du neuf ; grande refactorisation : risque élevé, peu de tours, exige des tests
- Quatre techniques de gestion du contexte : ancrer les infos clés, résumé-reprise, une conversation une tâche, nouvelle session sans hésiter
:::
