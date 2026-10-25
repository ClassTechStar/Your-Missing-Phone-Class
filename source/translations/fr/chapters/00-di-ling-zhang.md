---
id: di-ling-zhang
num: 00
part: ji-chu-pian
nav: Chapitre 0 : Salut, avant de commencer
toc: default
kind: chapter
---

### Chapitre 0 : Salut, avant de commencer

{class="mb-3"}
Avant l'exploration formelle, parlons d'abord de quelques règles de base pour vous assurer de comprendre tout ce qui suivra. Ne vous inquiétez pas, aiguiser sa hache n'empêche pas de couper du bois.

#### I. Ce que ce livre peut faire pour vous (et ce qu'il ne peut pas faire)

Il peut vous aider à comprendre systématiquement comment utiliser un smartphone, à saisir la logique derrière les fonctionnalités, et que vous soyez team Android ou team Apple, la plupart des raisonnements sont universels. Il vous guidera dans des exercices pratiques pour passer de « savoir utiliser » à « comprendre l'utilisation ».

Ce n'est pas le manuel d'un modèle de smartphone spécifique, ni des actualités technologiques sur les nouveaux produits, encore moins un guide pour vous rendre accro à votre téléphone. Honnêtement, si vous espériez apprendre « comment regarder des vidéos plus confortablement », vous risquez d'être déçu — nous nous soucions bien plus de la façon dont le smartphone vous sert vraiment, plutôt que l'inverse.

#### II. Notre « code secret »

Pour être plus clairs, le livre utilise quelques petites notations, comme un code tacite entre nous :

- <strong>[Nom du bouton]</strong>: désigne un bouton précis à l'écran ou le nom d'une application, par exemple [Paramètres], [OK].
- <strong>></strong>: indique l'ordre des opérations, par exemple « appuyer sur [Paramètres] &gt; [Son] » signifie d'abord appuyer sur Paramètres, puis sur Son.
- <strong>Gras</strong>: très important ! Il peut s'agir d'un concept clé ou d'un avertissement de sécurité, veuillez y prêter une attention particulière.
- <em>Italique</em>: quelques pensées complémentaires ou métaphores pour vous aider à mieux comprendre.

#### III. Android et iOS, nous parlons des deux

Devinez quoi, certaines choses portent des noms différents mais font le même travail. Par exemple : application (Android) et App (iOS), Paramètres (appelés pareil partout), Gestionnaire de fichiers (Android) et Fichiers (iOS). L'essentiel est de savoir que c'est la même chose, ne vous laissez pas embrouiller par les termes.

Par ailleurs, dans le camp Android, il y a aussi le système HarmonyOS de Huawei, qui a ses propres caractéristiques et que nous aborderons spécifiquement plus loin. Bref, quel que soit votre smartphone, ce livre peut vous aider.

#### IV. Capacité du smartphone : pourquoi après avoir acheté 128 Go, il en reste moins de 110 disponibles ?

Vous connaissez les unités de capacité : 1 To = 1024 Go, 1 Go = 1024 Mo, 1 Mo = 1024 Ko... Mais il y a un piège : les fabricants de disques calculent généralement en base 1000, tandis que le système calcule en base 1024, donc le disque « 128 Go » que vous achetez verra sa capacité réelle « rétrécir ».

Mais la perte de capacité de votre smartphone s'explique principalement par trois raisons :

1. <strong>Le système lui-même occupe de la place</strong>: le système d'exploitation est comme les murs porteurs d'une maison, il doit exister. Les systèmes actuels occupent facilement 10 à 20 Go, c'est tout à fait normal.
2. <strong>Les applications préinstallées par le fabricant</strong>: les applications livrées avec le nouveau smartphone occupent aussi de l'espace, certaines peuvent être désinstallées, d'autres pas.
3. <strong>Pertes de partitionnement et de formatage</strong>: pour des raisons techniques, comme la doublure d'un sac à dos qui prend aussi du volume.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Petit conseil pour l'achat d'un smartphone

{class="mt-1"}
Aujourd'hui, 128 Go ne suffisent plus vraiment, 256 Go est un minimum prudent. Si vous aimez prendre des photos ou jouer, envisagez directement 512 Go voire plus. Rappelez-vous, pour l'espace de stockage, mieux vaut avoir trop que pas assez.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>À vous de jouer : regardez la « carte d'identité » de votre smartphone

{class="mt-1"}
Ouvrez [Paramètres], trouvez À propos du téléphone (ou une option similaire), et notez : le modèle, la version du système, l'espace de stockage total et l'espace restant. C'est la première étape pour le connaître. Profitez-en pour vérifier l'état de santé de la batterie, pour avoir une idée.
:::

{class="text-lg font-semibold mt-6 mb-2"}
#### V. Votre smartphone est une « bibliothèque d'actifs numériques »

Avant d'entrer dans les connaissances spécifiques, établissons d'abord une compréhension fondamentale :<strong>le smartphone n'est plus seulement un outil de communication, c'est notre plus importante bibliothèque d'actifs numériques</strong>. Contacts, historiques de discussion, photos de famille, documents professionnels, applications bancaires, codes de paiement, données de santé, pièces d'identité électroniques... Toutes ces données réunies valent souvent plus que le smartphone lui-même.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-vault mr-2"></i>Pourquoi est-ce important ?

{class="mt-1"}
Si votre smartphone est perdu ou cassé, vous ne perdez pas seulement du matériel valant plusieurs milliers de yuans,<strong>mais surtout des données irremplaçables accumulées au fil des années</strong>— les photos de la croissance de vos enfants, les messages vocaux d'un proche disparu, des contrats importants non sauvegardés. Des habitudes rationnelles d'organisation et de protection vous protègent sur trois dimensions :

{class="list-disc pl-6 mt-2 space-y-1"}
- <strong>Amélioration des performances</strong>: une classification normalisée des fichiers accélère la recherche par le système, le smartphone reste fluide plus longtemps.
- <strong>Prolongation de la durée de vie</strong>: une gestion de stockage raisonnable réduit la charge de lecture/écriture des puces, la batterie et le stockage durent plus longtemps.
- <strong>Protection de la sécurité des données</strong>: gestion par couches + sauvegarde régulière + restriction des permissions, pour éloigner les « catastrophes de données ».
:::

{class="font-semibold mt-4 mb-1"}
##### Notre philosophie centrale : « La prévention d'abord, associer prévention et traitement »

Comme on ne commence à soigner sa santé que lorsqu'on est malade,<strong>la gestion du smartphone doit aussi commencer par les « habitudes quotidiennes »</strong>. Ce que ce livre souligne constamment, ce n'est pas une technique avancée particulière, mais ces principes simples :

- <strong>Prévention d'abord</strong>: installer des applications uniquement depuis les boutiques officielles, anonymiser les photos avant de les partager, ne pas réutiliser les mots de passe — ces « petits gestes » coûtent très peu mais bloquent la grande majorité des risques.
- <strong>Bilans réguliers</strong>: nettoyer le dossier Téléchargements une fois par mois, auditer les permissions une fois par trimestre, sauvegarde complète une fois par semestre — un rythme fixe est cent fois plus efficace que d'éteindre un incendie à la dernière minute.
- <strong>Garder une porte de sortie</strong>: activer la synchronisation cloud, noter soigneusement les comptes et mots de passe, rédiger une « liste d'héritage numérique » — pour qu'en cas d'imprévu, vous et votre famille puissiez y faire face sereinement.
