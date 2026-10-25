---
id: di-shi-ba-zhang
num: 18
part: jin-jie-pian
nav: Chapitre 18 : Sauvegarde et migration des données
toc: default
kind: chapter
---

### Chapitre 18 : Sauvegarde et migration des données

{class="chapter-intro mb-4"}
Une voisine a fait tomber son téléphone dans un bassin, après l'avoir repêché, il ne s'allumait plus. Ce qui lui faisait le plus mal, ce n'était pas le téléphone lui-même, mais les photos de trois ans non sauvegardées — tous les souvenirs de l'enfant de la naissance à ses premiers pas. En l'écoutant, je me sentais mal, parce que c'était tout à fait évitable. Ce chapitre va sérieusement souscrire une assurance pour vos données.

#### I. D'abord, comprenez : quelles sont les choses sur votre téléphone qui, une fois perdues, sont vraiment perdues

Les différentes données n'ont pas le même « statut de survie », vous devez les distinguer :

- <strong>Stockées localement sur le téléphone, perdues pour de bon si le téléphone est perdu</strong>: photos et vidéos (si la synchronisation cloud n'est pas activée), notes, SMS, historique d'appels, fichiers téléchargés.
- <strong>Stockées sur les serveurs des applications, récupérées en se reconnectant sur un nouveau téléphone</strong>: liste de contacts WeChat, commandes Taobao, historique de transactions dans l'application bancaire. Ces éléments sont stockés sur les serveurs des entreprises correspondantes, pas sur votre téléphone.
- <strong>Zone grise, nécessite des opérations spéciales</strong>: historique des discussions WeChat (bien que les serveurs WeChat les stockent, vous ne pouvez pas les télécharger depuis le serveur vous-même), les certificats d'appareil liés à l'application bancaire, les clés dans les applications d'authentification à deux facteurs (comme Google Authenticator).

Ce que vous devez donc protéger en priorité, c'est la première et la troisième catégorie.

#### II. Sauvegarde complète de l'appareil : tout régler en une fois

La sauvegarde complète de l'appareil, c'est comme prendre un « instantané » complet du téléphone — réglages système actuels, disposition du bureau, données des applications, photos, contacts, tout est emballé.

##### Option 1 : sauvegarde locale sur ordinateur (la plus fiable, recommandée pour ceux qui ont un ordinateur)

- <strong>iPhone</strong>: connectez le téléphone à l'ordinateur avec un câble de données, ouvrez iTunes (ancienne version Windows) ou Finder (Mac), dans la page de l'appareil, sélectionnez « Sauvegarder maintenant ». Attention à cocher « chiffrer la sauvegarde », sinon les mots de passe et les données de santé ne seront pas inclus dans la sauvegarde.
- <strong>Android</strong>: chaque marque a son propre logiciel sur ordinateur, comme Huawei HiSuite, Xiaomi Assistant, Samsung Smart Switch. Connectez à l'ordinateur et suivez les instructions.
- L'avantage de la sauvegarde sur ordinateur est qu'il n'est pas nécessaire de payer pour l'espace cloud, et la restauration est beaucoup plus rapide que depuis le cloud. L'inconvénient est qu'il faut penser à brancher régulièrement le câble pour sauvegarder — la plupart des gens n'y arrivent pas.

##### Option 2 : sauvegarde cloud (la plus tranquille, recommandée pour tous)

- <strong>iPhone</strong>: Réglages → votre nom → iCloud → Sauvegarde iCloud → activer. Le téléphone se sauvegarde automatiquement lorsqu'il est branché sur secteur, connecté au WiFi et verrouillé. Les 5 Go gratuits ne suffiront probablement pas, il est conseillé de payer 6 yuans pour passer à 50 Go.
- <strong>Android</strong>: chaque marque de cloud a une fonction de sauvegarde. Huawei recherchez « sauvegarde cloud » dans les réglages, Xiaomi dans « Xiaomi Cloud Services », OPPO/vivo similaire. Il y a aussi une sauvegarde Google intégrée (Réglages → Système → Sauvegarde), activez-la aussi.
- Le plus grand avantage de la sauvegarde cloud est « sans intervention de votre part », c'est automatique. Le plus grand inconvénient est que la restauration prend beaucoup de temps à télécharger, et l'espace gratuit est généralement insuffisant.

#### III. Stratégie de sauvegarde par catégorie : les éléments importants méritent une copie séparée

La sauvegarde complète de l'appareil est un filet de sécurité, mais certaines choses sont trop importantes pour mériter une copie séparée :

##### Photos et vidéos (les actifs numériques les plus précieux)

- <strong>Solution double protection</strong>: activez la synchronisation automatique iCloud Photos/Google Photos, et tous les quelques mois, copiez manuellement les photos sur un ordinateur ou un disque dur externe. Ainsi, une copie dans le cloud, une copie locale, sauvegardes mutuelles.
- <strong>Solution sans dépenser</strong>: Google Photos offre 15 Go gratuits, peut être réglé sur « qualité compressée » pour économiser de l'espace. Ou bien, tous les mois, utilisez un câble de données pour copier toutes les photos sur l'ordinateur.

##### Carnet de contacts (souvent négligé mais extrêmement important)

- Les contacts iPhone sont synchronisés par défaut avec iCloud, tant que la synchronisation est activée, pas besoin de sauvegarde supplémentaire. Mais pour plus de sécurité, vous pouvez exporter un fichier vCard depuis iCloud.com et le stocker sur l'ordinateur.
- Les contacts Android sont généralement synchronisés avec Google ou le cloud de la marque. Allez dans les réglages de l'application Contacts pour exporter un fichier .vcf, c'est une sauvegarde complète.

##### Historique des discussions WeChat (à traiter séparément, le plus important)

Il faut en parler séparément, car dans la sauvegarde complète de l'appareil, l'historique WeChat est souvent incomplet, et les outils de migration de téléphone ne parviennent pas à le déplacer.

- <strong>Méthode 1 : migrer vers un nouveau téléphone</strong>. WeChat → Moi → Réglages → Général → Migration et sauvegarde de l'historique des discussions → Migrer → Migrer vers un téléphone/tablette. Les deux téléphones connectés au même WiFi, scannez le code pour transférer. Attention : avant la fin de la migration, ne déconnectez pas WeChat sur l'ancien téléphone.
- <strong>Méthode 2 : sauvegarder sur l'ordinateur</strong>. Installez WeChat PC sur l'ordinateur, trois barres en bas à gauche → Migration et sauvegarde → Sauvegarde et restauration → Sauvegarder l'historique des discussions sur l'ordinateur. Ensuite, en changeant de téléphone, vous pourrez restaurer sur le nouveau téléphone.
- <strong>Méthode 3 : sauvegarder sur le cloud</strong>. WeChat prend également en charge la sauvegarde sur iCloud ou l'espace cloud du téléphone, mais attention : cette sauvegarde ne peut être restaurée que sur le téléphone actuel, pas sur un autre appareil. Pour changer de téléphone, il faut utiliser les deux premières méthodes.

#### IV. Guide de changement de téléphone : de l'ancien au nouveau

Changer de téléphone est une joie, mais si les données ne sont pas migrées, cela devient un casse-tête. Trois situations, trois approches :

##### Mise à niveau même marque (le plus simple)

- <strong>iPhone → nouvel iPhone</strong>: lors de l'activation, placez l'ancien téléphone à côté, « Démarrage rapide » apparaîtra automatiquement, scannez le motif sur le nouveau téléphone avec l'ancien. Toutes les données, réglages, disposition des applications seront transférés tels quels, y compris les mots de passe WiFi. Comptez environ vingt à trente minutes.
- <strong>Android même marque</strong>: utilisez l'outil de migration intégré à la marque. Huawei utilise « Clone Phone », Xiaomi « Mi Mover », OPPO « Phone Clone », vivo « EasyShare ». Les étapes sont similaires : installez la même application sur les deux téléphones, scannez pour connecter, cochez ce que vous voulez transférer, lancez.

##### Changement de marque (Android vers Android, marques différentes)

Utilisez un outil de migration tiers ou l'application de migration intégrée à l'ancienne marque (la plupart des applications de migration des marques prennent également en charge la migration vers d'autres téléphones Android). Ce qui peut être transféré : contacts, photos, SMS, historique d'appels, certaines applications. Ce qui ne peut pas être transféré : l'état de connexion dans les applications (vous devez vous reconnecter), l'historique des discussions WeChat (utilisez la fonction de migration de WeChat).

##### Changement de plateforme (Android vers iPhone, ou inversement)

- <strong>Android → iPhone</strong>: Apple a une application « Transférer vers iOS », téléchargez-la sur le téléphone Android, puis lors de l'activation du nouvel iPhone, sélectionnez « Migrer des données depuis un appareil Android ». Peut transférer les contacts, photos, SMS et autres données de base, mais pas les données d'application. L'historique WeChat doit utiliser la fonction de migration de WeChat.
- <strong>iPhone → Android</strong>: chaque marque Android a son outil de migration correspondant, mais honnêtement, l'expérience de migration interplateforme n'est pas aussi bonne que sur la même plateforme. Faites d'abord les choses les plus importantes : exportez les contacts, sauvegardez les photos, migrez l'historique WeChat. Le reste viendra progressivement.

#### V. Règle d'or de la sauvegarde : le principe 3-2-1

C'est un principe classique du domaine de la sécurité des données, simple à retenir :

- <strong>3</strong>: conservez au moins trois copies des données importantes (un original, deux sauvegardes).
- <strong>2</strong>: utilisez deux supports de stockage différents pour les sauvegardes (par exemple, une dans le cloud, une sur disque dur externe).
- <strong>1</strong>: au moins une sauvegarde doit être conservée dans un lieu physique différent (pour éviter qu'un incendie, un vol, etc. ne détruise toutes les données simultanément).

Pour une personne ordinaire, faire « une dans le cloud, une sur l'ordinateur » est déjà très bien. Pas besoin de trop compliquer, l'important est de vraiment le faire.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Attention particulière à l'historique WeChat

{class="mt-1"}
L'historique WeChat ne peut pas être migré par aucun outil de migration de téléphone ! Il n'est pas couvert par la sauvegarde complète de l'appareil. Vous devez utiliser la fonction « migration de l'historique des discussions » intégrée à WeChat, ou le sauvegarder sur WeChat pour ordinateur. Beaucoup de gens découvrent après être passés au nouveau téléphone que l'historique a disparu, et il est trop tard — l'ancien téléphone a peut-être déjà été réinitialisé aux paramètres d'usine.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Exercez-vous : faites un exercice de sauvegarde complet

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Vérifiez si la sauvegarde cloud iCloud ou la sauvegarde cloud de la marque est activée, confirmez la date de la dernière sauvegarde.
2. Sauvegardez manuellement les photos : connectez l'ordinateur avec un câble de données, copiez les dossiers DCIM et Pictures vers l'ordinateur.
3. Sauvegardez les contacts : les utilisateurs d'iPhone exportent un vCard depuis iCloud.com ; les utilisateurs d'Android exportent un fichier .vcf depuis les réglages de l'application Contacts.
4. Sauvegardez l'historique WeChat : ouvrez WeChat → Moi → Réglages → Général → Migration et sauvegarde de l'historique des discussions → Sauvegarder sur l'ordinateur.
5. Copiez le fichier vcf des contacts exporté et le dossier de photos sur un disque dur externe ou une clé USB, pour accomplir le « une copie hors ligne ailleurs » du principe 3-2-1.
:::
