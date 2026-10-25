---
id: di-er-shi-san-zhang-github
part: chao-yue-pian
nav:  Annexe : Guide de démarrage avec GitHub
toc: sub
kind: chapter
---

### Chapitre 23 Annexe : Guide de démarrage GitHub — de l'hébergement de code à la plateforme de collaboration

{class="chapter-intro mb-4"}
Dans le chapitre précédent, nous avons parlé de « pensée programmation », et pour vraiment la mettre en pratique et collaborer avec d'autres, un nom est incontournable — GitHub. Que vous soyez étudiant en informatique participant à des concours, que vous vouliez sauvegarder vos créations de code, ou simplement curieux de voir ce que les développeurs du monde entier bricolent, GitHub est une plateforme que vous devez connaître. Dans cette section, nous partons des concepts les plus fondamentaux pour vous construire une compréhension claire.

#### I. Qu'est-ce que GitHub exactement ?

En bref, GitHub est une <strong>plateforme d’hébergement de code et de collaboration</strong> basée sur Git. Lancée en 2008, acquise par Microsoft en 2018, elle reste la plus grande plateforme d’hébergement de code open source au monde, hébergeant des centaines de millions de dépôts couvrant presque tous les langages de programmation majeurs.

Pour comprendre par analogie :<strong>Git est le journal intime sur votre ordinateur, GitHub est une plateforme de blogs publique</strong>— vous pouvez publier vos créations, suivre les projets d’autres personnes, participer aux discussions et collaborer. Ce n’est pas seulement le « dépôt back-office des programmeurs », c’est plutôt une « cité technologique » co-construite par les développeurs du monde entier — les projets y naissent, itèrent, sont discutés et réutilisés.

Pour les non-techniciens, GitHub n'est pas hors de portée. Beaucoup de non-programmeurs l'utilisent pour héberger des notes, des livres numériques, des blogs personnels, voire sauvegarder des fichiers de configuration. Tant que vous avez le moindre besoin de « organiser vos contenus et les partager », GitHub mérite que vous le connaissiez.

#### II. La différence entre Git et GitHub (concepts clés !)

Beaucoup de gens confondent ces deux termes à la première rencontre, voici une clarification :

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                        <thead>
                            <tr class="bg-light dark:bg-gray-700">
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Élément de comparaison</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Git</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">GitHub</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Nature</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Outil de contrôle de version (logiciel)</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Plateforme d'hébergement de code (site web)</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lieu d'exécution</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sur l'ordinateur local</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Dans le cloud (accès par navigateur)</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Responsabilité principale</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Enregistrer chaque modification de fichier (comment, par qui, quand)</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mettre les dépôts Git dans le cloud pour faciliter le stockage, la présentation et la collaboration</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Connexion Internet requise</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Non, utilisable hors ligne</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Oui, accès nécessite le réseau</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Appartenance</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Logiciel open source, créé par Linus Torvalds (le père de Linux)</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Produit de Microsoft</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Concurrents</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SVN, Mercurial</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GitLab, Gitee, Bitbucket</td>
                            </tr>
                        </tbody>
                    </table>
```

En résumé :<strong>Git gère « comment enregistrer les modifications », GitHub gère « où les mettre et comment collaborer »</strong>. Git est un outil qui tourne en local ; GitHub est une plateforme qui met les dépôts Git dans le cloud pour faciliter la collaboration et la présentation. Vous pouvez utiliser Git sans GitHub (par exemple pour gérer les versions de votre propre code), mais utiliser GitHub implique nécessairement Git (car GitHub est basé sur Git).

#### III. Concepts et fonctions clés de GitHub

##### 📁 Concepts de base

Avant de passer à la pratique, familiarisez-vous avec quelques termes fréquents, sinon l'interface de GitHub vous laissera perplexe :

- <strong>Dépôt (Repository, abr. Repo)</strong>: un projet correspond à un dépôt, contenant tous les fichiers de code, versions historiques et documentation. Peut être compris comme un « dossier projet ».
- <strong>Commit</strong>: un enregistrement de modification du code. Chaque Commit a un message décrivant « ce qui a été modifié et pourquoi ». C’est la base permettant à Git/GitHub de « remonter le temps ».
- <strong>Branche (Branch)</strong>: ligne de développement indépendante issue de la branche principale. Par exemple, pour ajouter une fonctionnalité, créez une branche, développez dessus, puis fusionnez sans affecter les autres.
- <strong>Clonage (Clone)</strong>: copier intégralement le dépôt distant sur l’ordinateur local pour ensuite modifier le code localement.
- <strong>Pousser (Push) / Tirer (Pull)</strong>: Push envoie le code local vers GitHub, Pull télécharge le dernier code depuis GitHub. Ce sont les deux actions clés de synchronisation en collaboration d’équipe.
- <strong>Pull Request (PR)</strong>:quand vous avez modifié le code sur une branche et souhaitez fusionner dans la branche principale, ouvrez une PR pour que l’équipe examine le code avant fusion. C’est le mécanisme central de collaboration GitHub.
- <strong>Issue</strong>: utilisé pour enregistrer bugs, demandes de fonctionnalités, sujets de discussion. Chaque Issue est comme un fil de discussion avec assignation et étiquetage.
- <strong>Fork</strong>:copier le dépôt de quelqu’un sous votre compte, modifier librement votre copie sans affecter l’original. Envoyez ensuite une PR à l’auteur pour demander la fusion de vos améliorations.

##### 🛠️ Fonctions clés

GitHub offre bien plus que du stockage de code :

- <strong>Contrôle de version</strong>:Enregistre l’historique de chaque modification du code, permet de revenir à une version antérieure saine à tout moment.
- <strong>Collaboration d’équipe</strong>:Prend en charge le développement parallèle par plusieurs utilisateurs sur un même projet, sans écrasement ni conflit.
- <strong>Suivi de problèmes</strong>:Utilise les Issues pour enregistrer les bugs et demandes de fonctionnalités, facilitant le suivi par l’équipe.
- <strong>Gestion de projet</strong>:Intègre des outils de gestion comme les tâches à faire et les tableaux de projet (Projects), équivalent à un Trello léger intégré.
- <strong>Automatisation</strong>:Via <strong>GitHub Actions</strong>, réalise la compilation, les tests, le packaging et le déploiement automatiques après un push de code, c’est l’outil clé du « CI/CD (intégration continue / déploiement continu) » moderne.
- <strong>Gestion de documentation</strong>:Le README présente le projet, le Wiki stocke l’architecture détaillée et les normes de développement, Pages peut même héberger directement un site statique.
- <strong>Hébergement et présentation de code</strong>:Chaque dépôt a un bel affichage web avec coloration syntaxique, c’est la « vitrine » de vos réalisations techniques.
- <strong>Communauté open source</strong>:Vous pouvez Star (favoris) les projets que vous aimez, Watch (suivre) l’activité des projets, Follow (suivre) des développeurs, et participer à la collaboration open source mondiale.

#### IV. Inscription et prise en main : créez votre premier dépôt en cinq minutes

##### 📝 Inscription

1. Visitez<a href="https://github.com" class="text-primary hover:underline" target="_blank" rel="noopener">github.com</a>,cliquez sur « Sign up ».
2. Remplissez l'e-mail, définissez le mot de passe et le nom d'utilisateur (le nom d'utilisateur apparaîtra dans l'adresse de votre profil, utilisez de préférence l'anglais, par exemple<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">github.com/yourname</code>).
3. Complétez la vérification par e-mail et le test CAPTCHA.
4. Choisissez le plan gratuit (Free), largement suffisant pour un usage personnel.

##### 📁 Créer votre premier dépôt

1. Après connexion, cliquez sur le « + » en haut à droite, choisissez « New repository ».
2. Remplissez le nom du dépôt (Repository name), par exemple<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">my-first-project</code>.
3. Écrivez une brève description (Description), pour que les autres sachent à quoi sert ce dépôt.
4. Choisissez Public ou Private. Les dépôts publics sont visibles par tous, les privés uniquement par vous et vos collaborateurs. Les comptes gratuits prennent aussi en charge un nombre illimité de dépôts privés.
5. Cochez « Add a README file » — le README est le « mode d'emploi » du projet, chaque dépôt devrait en avoir un.
6. Cliquez sur « Create repository », votre premier dépôt GitHub est né !

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Le saviez-vous : qu'est-ce qu'un README

{class="mt-1"}
README.md est un fichier au format Markdown, c'est la première chose que les gens voient en ouvrant votre dépôt. Un bon README contient généralement : présentation du projet, méthode d'installation, exemples d'utilisation, licence, coordonnées. Bien rédiger un README est une compétence de base du programmeur, et la première condition pour que votre projet soit utilisé par d'autres.
:::

#### V. Flux de travail de base : du local au cloud

Comprendre le flux de travail GitHub, la clé est de retenir ce cycle :<strong>modification locale → indexation → commit → push → mise à jour cloud</strong>. Voici chaque étape en langage simple :

1. <strong>Modifier les fichiers</strong>: écrire du code ou modifier des documents dans l’éditeur sur l’ordinateur local.
2. <strong>git add</strong>: ajouter les fichiers modifiés à la « zone d’indexation », c’est dire à Git « je prépare l’enregistrement de ces modifications ».
3. <strong>git commit</strong>: enregistrer formellement les modifications indexées comme un « commit », avec un message descriptif, par exemple « correction du bug de connexion ». Cette étape ne se fait qu’en local.
4. <strong>git push</strong>: charger les commits locaux sur GitHub dans le cloud, pour que les autres puissent les voir.
5. <strong>git pull</strong>: avant de commencer à travailler, tirer le dernier code du cloud pour s’assurer que votre copie locale est synchronisée avec le reste de l’équipe.

Pour les débutants, retenez cette formule :<strong>« d’abord pull puis modifier, après modification add, commit avec message, enfin push »</strong>. Prenez cette habitude et la collaboration d’équipe se passera sans accroc.

#### VI. Flux de collaboration d'équipe : comment fonctionne une Pull Request

La plus grande force de GitHub réside dans son mécanisme de collaboration. Un flux de collaboration d'équipe typique :

1. <strong>Créer une branche</strong>: créer une nouvelle branche à partir de la branche principale (généralement main ou master), par exemple<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">feature/login</code>, pour développer la nouvelle fonctionnalité.
2. <strong>Développer et commiter</strong>: écrire le code sur la nouvelle branche, avec plusieurs commits pour enregistrer la progression.
3. <strong>Pousser sur GitHub</strong>: push la branche vers le dépôt distant.
4. <strong>Ouvrir une Pull Request</strong>: sur la page GitHub, ouvrez une PR pour demander la fusion de votre branche dans la branche principale. Expliquez clairement les modifications et leurs raisons.
5. <strong>Revue de code (Code Review)</strong>: l’équipe examine votre code, émet des avis ou suggestions de modification. Vous pouvez continuer à commiter selon les retours, la PR se met à jour automatiquement.
6. <strong>Fusion</strong>: après approbation, cliquez sur « Merge » pour fusionner le code dans la branche principale. Votre contribution entre officiellement dans le projet !

Ce flux garantit que <strong>tout code est examiné avant d’entrer dans la branche principale</strong>, réduisant considérablement le risque d’erreur. Les projets open source utilisent le même mécanisme pour accepter les contributions d’inconnus du monde entier — vous pouvez tout à fait soumettre une PR sur un projet open source célèbre, et une fois acceptée, vous en êtes contributeur.

#### VII. Scénarios d'application typiques de GitHub

##### 🎓 Étudiants en concours et projets de cours

Les étudiants en informatique participant à des concours ACM, des hackathons ou des projets de fin d'études ne peuvent presque pas s'en passer de GitHub. Il sert à la fois de plateforme de collaboration et de vitrine de réalisations — les juges de concours peuvent directement consulter votre dépôt pour évaluer la qualité du code et le processus collaboratif. Beaucoup d'entreprises demandent aussi un lien GitHub lors du recrutement, comme preuve de compétence technique.

##### 📚 Base de connaissances personnelle et hébergement de notes

Les non-programmeurs aussi peuvent utiliser GitHub. Beaucoup s'en servent pour héberger des notes d'étude, des blogs techniques (avec GitHub Pages, création de site gratuite), des livres numériques. Rédaction en Markdown + gestion de versions Git + sauvegarde cloud, trois en un.

##### 🌐 Participer à des projets open source

GitHub est le bastion du mouvement open source mondial. Vous pouvez Forker les projets que vous aimez, modifier et envoyer une PR pour contribuer à la communauté ; ou simplement Star vos coups de cœur et suivre leurs mises à jour. Participer à l'open source est un excellent moyen de progresser techniquement et de bâtir sa réputation.

##### 🤖 Déploiement automatisé et CI/CD

Avec GitHub Actions, on peut réaliser un flux entièrement automatique « un push de code → test automatique + déploiement automatique sur le serveur ». Beaucoup de blogs personnels et de sites de documentation sont construits ainsi : écrivez un article, poussez-le, et le site se met à jour automatiquement.

##### 💾 Sauvegarde de code et synchronisation multi-appareils

Utilisez le dépôt de code comme un cloud : changez d'ordinateur, travaillez sur plusieurs appareils, un git pull suffit pour récupérer le code le plus récent — plus besoin de copier avec une clé USB.

#### VIII. Quelques conseils pour les débutants

- <strong>Rédigez des messages de commit clairs</strong>: n’écrivez pas « update ». Un bon message : « correction de la redirection erronée après connexion utilisateur », même six mois plus tard vous saurez ce qui a été fait.
- <strong>Commitez souvent, par petites étapes</strong>: faites un commit à chaque petite fonctionnalité plutôt qu’un seul commit en fin de journée. En cas de problème, il sera plus facile à localiser.
- <strong>Développez sur des branches, ne modifiez pas directement la branche principale</strong>: même pour un projet personnel, prenez l’habitude de créer des branches, vous ne serez pas débordé en travail d’équipe.
- <strong>Utilisez .gitignore</strong>: ce fichier indique à Git quels fichiers ne pas inclure dans le contrôle de version (mots de passe, produits de compilation, dossiers de dépendances), pour éviter d’envoyer des fichiers inutiles.
- <strong>Consultez les excellents projets open source</strong>: parcourez GitHub Trending, étudiez la structure du code, la rédaction du README et le flux collaboratif des projets à haute popularité, c’est le moyen gratuit le plus rapide de progresser.
- <strong>Demandez le GitHub Student Pack</strong>: après vérification étudiante, obtenez gratuitement de nombreux outils et services payants (Copilot, nom de domaine, services cloud, etc.), d’une valeur de milliers de dollars.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Rappel de sécurité

{class="list-disc pl-6 mt-1 space-y-1"}
- Ne soumettez jamais de mots de passe, clés API, chaînes de connexion à la base de données ou autres informations sensibles sur GitHub, surtout dans un dépôt public — une fois divulgués, ils seront captés par des crawlers en quelques secondes, avec des conséquences graves.
- Si vous avez accidentellement soumis des informations sensibles, supprimer le fichier ne suffit pas (l’historique le contient encore), utilisez<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">git filter-branch</code> ou un outil professionnel pour nettoyer l’historique, et changez immédiatement les clés compromises.
- Les dépôts privés ne sont pas non plus totalement sûrs ; les informations sensibles sont mieux gérées via des variables d'environnement, hors du dépôt de code.
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Remarques sur l'accès à GitHub depuis Chine

{class="mt-1"}
L’accès à GitHub depuis la Chine est parfois instable, avec des risques de page inaccessible ou de clonage lent. Vous pouvez essayer : ① utiliser des miroirs nationaux (GitClone, ghproxy) pour accélérer le clonage ; ② configurer les Hosts ou utiliser un proxy ; ③ si la collaboration est principalement nationale, envisagez l’alternative chinoise <strong>Gitee</strong>, aux fonctionnalités similaires et à l’accès plus rapide. Beaucoup d’équipes hébergent simultanément sur GitHub et Gitee, combinant internationalisation et rapidité nationale.
:::

::: div .success-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Usage avancé : créez un blog personnel gratuit avec GitHub Pages

{class="mt-1"}
GitHub Pages vous permet d'héberger gratuitement un site statique, couplé à des générateurs comme Jekyll, Hexo ou Hugo, vous pouvez facilement créer un blog personnel. Poussez un article Markdown vers le dépôt, le blog se met à jour automatiquement, avec HTTPS et nom de domaine personnalisé inclus. D'innombrables blogs techniques sont construits ainsi — zéro coût, sans publicité, avec contrôle de versions.
:::

#### IX. Résumé : pourquoi tout le monde devrait connaître GitHub

GitHub n’est plus seulement « l’outil des programmeurs », c’est plutôt une <strong>façon de travailler de l’ère numérique</strong>: le contrôle de version rend tout traçable, les mécanismes de collaboration font tourner les équipes efficacement, l’esprit open source fait circuler librement le savoir. Même sans coder, comprendre les concepts de « commit, branche, fusion » vous aidera à mieux gérer tout contenu nécessitant « modifications répétées + collaboration » — des mémoires aux documents, des notes aux plans.

Pour les étudiants en informatique, GitHub est une compétence indispensable : c'est votre portfolio, votre plateforme de collaboration, votre bibliothèque de ressources d'apprentissage, et le « CV » le plus convaincant lors de la recherche d'emploi. Inscrivez-vous tôt, mettez en ligne vos travaux de cours et petits projets, accumulez progressivement — quelques années plus tard, vous aurez un parcours technique qui fera briller les yeux des recruteurs.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>À vous : accomplissez votre première expérience GitHub

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Inscrivez-vous sur GitHub, complétez votre profil (avatar, bio, domaines techniques d'intérêt).
2. Créez un dépôt nommé<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">hello-github</code> public, en cochant « Add a README file ».
3. Entrez dans le dépôt, cliquez sur le bouton d'édition du README.md (icône crayon), rédigez une brève auto-présentation en Markdown, et soumettez les modifications.
4. Dans la barre de recherche GitHub, cherchez un mot-clé qui vous intéresse (par exemple<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">python-tutorial</code>), et Star deux projets qui vous plaisent.
5. (Avancé) Installez Git sur votre ordinateur, clonez le dépôt en local, modifiez le README puis poussez vers le cloud — accomplissez un flux complet « local → cloud ».
:::
