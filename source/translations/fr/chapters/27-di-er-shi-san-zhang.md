---
id: di-er-shi-san-zhang
num: 23
part: chao-yue-pian
nav: Chapitre 23 : Pensée algorithmique et initiation à l'automatisation
toc: default
kind: chapter
---

### Chapitre 23 : Pensée programmation et initiation à l'automatisation

{class="chapter-intro mb-4"}
Dans les deux chapitres précédents, nous avons construit pour le smartphone des « murs de protection » sécuritaires et découvert son « cerveau IA » de plus en plus intelligent à l'intérieur de ces murs. Maintenant, débloquons l'un des potentiels ultimes du smartphone : lui faire « penser » comme un programmeur et accomplir automatiquement les tâches consécutives que vous définissez. Vous direz peut-être : « Je ne sais pas coder, ça me concerne comment ? » Rassurez-vous, ce chapitre ne nécessite absolument pas d'écrire une seule ligne de code — les smartphones modernes ont abaissé le seuil de la « programmation » au point où il suffit de glisser-déposer pour s'en sortir.

#### I. Qu'est-ce que l'automatisation exactement ?

En langage simple, l'automatisation c'est :<strong>faire en sorte que le smartphone accomplisse automatiquement une série d'actions quand une certaine condition est remplie.</strong> Vous n'avez pas besoin d'opérer manuellement à chaque fois, ni de vous rappeler ce qu'il faut faire — le smartphone juge lui-même le moment et s'exécute.

Par exemple : chaque matin en vous réveillant, vous devez manuellement désactiver le mode Ne pas déranger, ouvrir WeChat pour voir les messages, ouvrir l'application Météo pour voir comment vous habiller, ouvrir NetEase Cloud pour lancer une chanson. Si vous empaquetez toutes ces étapes en un flux automatisé, configuré pour « s'exécuter automatiquement chaque matin à 7h », il vous suffit de prendre le smartphone en vous réveillant — tout est déjà prêt. Ça fait rêver, non ?

L'automatisation est essentiellement une chaîne logique « si… alors… », le if-else de la programmation. Une fois ce mode de pensée compris, même si vous ne codez jamais de votre vie, votre approche des problèmes sera beaucoup plus structurée. Les éléments clés :

1. <strong>Condition déclencheuse</strong>: Quand commencer ? Ça peut être « chaque matin à 7h », « quand je me connecte au Wi-Fi de la maison », « quand j'arrive à un certain endroit », « quand la batterie du smartphone descend sous 20% ».
2. <strong>Action à exécuter</strong>: Que faire concrètement ? Ça peut être envoyer un message WeChat, ouvrir une application, ajuster le volume, changer de fond d'écran, lancer de la musique, envoyer une notification… Presque tout ce que vous pouvez faire manuellement sur le smartphone, l'automatisation peut le faire.
3. <strong>Logique intermédiaire</strong>(optionnelle mais très puissante) : Si la situation A alors faire X, sinon faire Y. Par exemple « si c'est un jour ouvré, lancer le podcast d'actualités ; le week-end, lancer de la musique » — c'est ce qu'on appelle une branche conditionnelle.

#### II. « Raccourcis » iOS — l'outil d'automatisation des utilisateurs Apple

L'application « Raccourcis » (Shortcuts) d'Apple est préinstallée, pas besoin de la télécharger. Son concept clé est d'assembler les opérations comme des blocs de construction. Voici quelques notions fondamentales :

- <strong>« Raccourci »</strong>: un flux automatisé complet, exécutable manuellement ou par commande vocale Siri. Par exemple, dites « Hey Siri, mode maison » et il exécute automatiquement la série d’actions que vous avez définie.
- <strong>« Automatisation »</strong>: une instruction qui se déclenche automatiquement selon une condition, sans intervention manuelle. Par exemple « quand le smartphone se connecte au Bluetooth de la voiture, ouvre automatiquement l’appli Plans ». Les automatisations se configurent dans l’onglet « Automatisation », séparé des « Raccourcis ».
- <strong>« Action »</strong>: l’unité d’exécution minimale. Ouvrir une appli est une action, envoyer un message est une action, obtenir la météo est une action, ajuster la luminosité est une action. Vous pouvez enchaîner des centaines d’actions.

Voici quelques exemples vraiment utiles — suivez-les une fois et vous comprendrez :

##### Exemple 1 : Raccourci « Bonjour » en un clic

Chaque matin, un seul clic (ou dites « Bonjour » à Siri), et le smartphone fait automatiquement : obtenir la météo du jour → lire la météo et la température → afficher le calendrier → ouvrir votre appli musique habituelle. Étapes : nouveau raccourci → ajouter l'action « Obtenir la météo actuelle » → ajouter « Lire le texte » → ajouter « Obtenir les événements du calendrier » → ajouter « Afficher un rappel » → ajouter « Ouvrir l'appli » et choisir NetEase Cloud. C'est aussi simple que ça, tout par glisser-déposer.

##### Exemple 2 : Automatisation « Mode économie d'énergie »

Dans l'onglet « Automatisation », créez une nouvelle automatisation → choisissez « Niveau de batterie » → réglez sur « inférieur à 30 % » → ajoutez les actions « Activer le mode basse consommation », « Réduire la luminosité à 30 % », « Désactiver le Bluetooth ». Désormais, quand la batterie passe sous 30 %, le smartphone passe automatiquement en mode économie — sans que vous ayez à vous en soucier.

##### Exemple 3 : Comptabilisation automatique après scan

Après chaque paiement par scan WeChat/Alipay, le smartphone lit la notification de paiement et enregistre automatiquement le montant et le commerçant dans une note ou un tableau Numbers. Cela utilise le déclencheur « SMS/notification reçu » de l'automatisation des raccourcis (iOS 17+ prend en charge la lecture des transactions Wallet), couplé à l'action « Ajouter à Numbers ». Pour ceux qui veulent tenir leurs comptes sans l'effort manuel, c'est une bouée de sauvetage.

Une astuce méconnue : vous pouvez ajouter un raccourci à l'écran d'accueil sous forme d'icône d'appli. Par exemple, créez un raccourci « Taxi pour la maison », placez l'icône sur le bureau, un clic ouvre Didi et règle la destination sur votre domicile — bien plus rapide que d'ouvrir l'appli et de saisir l'adresse manuellement.

#### III. Automatisation Android — Tasker et ses amis

Du côté Android, c'est un peu plus complexe, mais le plafond est aussi plus élevé. Commençons par le plus simple :

##### Niveau débutant : Auto-cliqueur

Beaucoup de smartphones Android intègrent un « auto-cliqueur » ou on peut le télécharger sur le magasin d'applications. Le principe est ultra simple : vous effectuez les opérations manuellement une fois, il enregistre les coordonnées et les intervalles de temps de vos clics, puis peut les rejouer à haute vitesse. Par exemple, si une appli offre une récompense de connexion quotidienne, vous enregistrez la séquence de clics une fois, et ensuite elle se rejoue automatiquement chaque jour. L'inconvénient : il ne reconnaît que les coordonnées, donc si l'interface change (une pub qui apparaît), il clique à côté.

##### Niveau intermédiaire : Tasker — le roi de l'automatisation Android

Tasker est l'outil d'automatisation le plus puissant sur Android, au top des classements depuis des années. Honnêtement, sa courbe d'apprentissage est un peu raide et l'interface n'est pas très jolie, mais une fois que vous le maîtrisez, vous aurez l'impression que votre smartphone peut tout faire. Le cœur de Tasker est aussi le modèle « déclencheur → tâche » :

- <strong>Profil</strong>: définit « quand déclencher ». Les conditions peuvent être l’heure, le lieu, l’état de connexion Wi-Fi, le Bluetooth, la réception d’une notification spécifique, l’état de la batterie, l’orientation de l’écran… Tasker prend en charge un nombre incroyable de déclencheurs, des dizaines.
- <strong>Tâche</strong>: définit « quoi faire après le déclenchement ». Une tâche peut contenir plusieurs actions, exécutées en séquence. Types d’actions : ajuster les paramètres système (volume, luminosité, Wi-Fi, Bluetooth, mode avion), envoyer SMS, requête HTTP, exécuter commande Shell, contrôler lecture multimédia, afficher boîte de dialogue, etc.

Voici quelques scénarios classiques et pratiques avec Tasker :

- <strong>Wi-Fi automatique en rentrant</strong>: déclencheur « connexion à antenne spécifique » (antenne fixe près de chez vous) → tâche « Activer Wi-Fi ». Pas de GPS ni surconsommation, le Wi-Fi s’active dès l’entrée dans votre quartier.
- <strong>Mode réunion</strong>: déclencheur « titre calendrier contient « réunion » » → tâche « Mode silencieux, volume média coupé, auto-réponse WeChat (plugin) ». Plus jamais peur que le smartphone sonne en réunion.
- <strong>Protection oculaire nocturne</strong>: déclencheur « heure 22h-6h » → tâche « Protection oculaire, luminosité 20 %, écran N&amp; B (niveaux de gris) ». L’écran N&amp; B a un effet miraculeux contre l’envie de scroller — une fois grisé, vous n’avez plus envie.
- <strong>Podcast automatique au casque</strong>: déclencheur « insertion casque filaire / connexion Bluetooth casque » → tâche « Ouvrir Xiaoyuzhou et lancer dernier épisode ». Mettez le casque et écoutez, pas besoin de déverrouiller le smartphone.

Si Tasker vous semble trop difficile à prendre en main, essayez son cousin simplifié :<strong>MacroDroid</strong>. L’interface est bien plus conviviale, les modèles sont abondants, parfait pour les utilisateurs qui ne veulent pas se prendre la tête. Par ailleurs, beaucoup de systèmes Android chinois (MIUI de Xiaomi, HarmonyOS de Huawei, ColorOS d’OPPO) intègrent des fonctions « Scènes » ou « Assistant intelligent », moins puissantes que Tasker mais largement suffisantes pour l’automatisation quotidienne.

#### IV. Applications quotidiennes de la pensée automatisation

Le plus grand bénéfice de l’automatisation n’est pas de gagner quelques secondes, mais de <strong>changer votre façon de penser</strong>. Une fois habitué au raisonnement « si X se produit, alors faire Y automatiquement », vous découvrirez qu’une foule de tâches répétitives peuvent être éliminées. Par exemple :

- Après chaque photo, sauvegarde automatique sur le cloud puis compression de la photo locale pour économiser l'espace.
- Chaque matin, lecture automatique du calendrier du jour, génération d'un résumé envoyé à la famille via WeChat.
- À la réception d'un SMS de livraison, ajout automatique d'une tâche « récupérer le colis » dans les notes.
- Quand la batterie est pleine, rappel vocal automatique pour débrancher le chargeur (éviter la surcharge qui abîme la batterie).
- À l'heure de la fin de journée, si vous êtes encore près du bureau (géolocalisation par antenne), rappel automatique « il est temps de rentrer ».

Tout ça semble très avancé, mais avec les deux concepts de base « déclencheur + action », combinés aux Raccourcis ou Tasker, tout est réalisable. La clé est de <strong>prendre conscience que « cette tâche peut être automatisée »</strong>— beaucoup de gens n’en sont pas incapables, ils n’y pensent simplement pas.

#### V. Guide des pièges à éviter : problèmes courants de l'automatisation

L'automatisation n'est pas toujours un long fleuve tranquille, voici quelques pièges que j'ai déjà repérés pour vous :

- <strong>Le déclenchement par position peut être capricieux</strong>:Le déclenchement « arrivée/départ » d’iOS utilise la géofencing, la précision dépend du signal GPS et de l’optimisation système. Parfois le déclenchement n’intervient que 10 minutes après votre arrivée. Préférez le déclenchement par Wi-Fi ou antenne, plus fiable et plus économe en énergie.
- <strong>Les « Automatisations » des Raccourcis nécessitent une autorisation</strong>:Dans iOS, la plupart des déclencheurs de l’onglet « Automatisation » nécessitent une confirmation manuelle (mécanisme de sécurité iOS). Mais les déclencheurs connexion Wi-Fi, connexion Bluetooth et arrêt du réveil fonctionnent en plein automatique, sans confirmation.
- <strong>Tasker nécessite les permissions d’accessibilité</strong>:Beaucoup de fonctions avancées (comme la simulation de clic) nécessitent les permissions d’accessibilité, ce qui affiche une notification permanente dans les paramètres. C’est la conception de sécurité Android, impossible à supprimer.
- <strong>Ne rendez pas l’automatisation trop complexe</strong>:Commencez l’automatisation par des petits flux de « 2-3 actions ». Ne vous lancez pas d’emblée dans un super-flux de 20 étapes — le débogage vous rendra fou.

::: div .success-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Astuce : la bonne posture pour débuter en automatisation

{class="mt-1"}
Prenez d'abord 5 minutes pour réfléchir : quelles sont les 3 choses que vous répétez le plus sur votre smartphone chaque jour ? Par exemple, votre routine matinale, vos habitudes après la connexion du casque Bluetooth, vos réglages avant de sortir… Commencez par ces petites tâches à haute fréquence, créez une automatisation simple pour chacune. Même si chaque automatisation ne vous fait gagner que 5 secondes, à la longue c'est considérable. Et la satisfaction une fois que c'est fait, c'est vraiment addictif.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Entraînez-vous : trois défis d'automatisation pour débutants

{class="mt-1 mb-2"}
Choisissez celui qui vous convient le mieux, une fois terminé vous serez initié :

{class="list-decimal pl-6 mt-1 space-y-1"}
1. <strong>Défi 1 : Automatisation « Bonjour »</strong>:iOS : dans l’appli Raccourcis, créez un nouveau raccourci → ajoutez « Obtenir la météo actuelle » → « Lire le texte » → « Ouvrir l’appli et choisir NetEase Cloud ». Ensuite dites « Bonjour » à Siri pour déclencher. Android : dans Tasker, créez une nouvelle tâche → ajoutez « Obtenir la météo » → « Lire » → « Ouvrir l’appli » → définissez le déclencheur à 7h00 chaque jour.
2. <strong>Défi 2 : Économie d’énergie automatique</strong>:iOS : onglet Automatisation → nouveau → « Niveau de batterie » → inférieur à 25 % → ajoutez « Activer le mode basse consommation » + « Luminosité 25 % ». Android : Tasker, nouveau Profil → État → Alimentation → Batterie 0-25 % → tâche « Mode économie d’énergie » + « Baisser la luminosité ».
3. <strong>Défi 3 : Navigation automatique au Bluetooth voiture</strong>:iOS : Automatisation → nouveau → « Bluetooth » → sélectionnez le Bluetooth de votre voiture → ajoutez « Ouvrir l’appli Amap » + « Volume média à 80 % ». Android : Tasker → Profil → État → Bluetooth connecté → sélectionnez le Bluetooth voiture → tâche « Ouvrir Amap » + « Augmenter le volume média ».
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Cas 3 : Automatisation du « rituel du matin »

{class="list-disc pl-6 mt-1 space-y-1"}
- <strong>Scénario</strong> : Chaque jour à 7:00, annonce automatique de la météo + désactivation du mode silencieux + ouverture des actualités.
- <strong>Étapes</strong> : iOS : Raccourcis → Automatisation → Déclencheur temporel → Ajouter « Obtenir la météo » + « Régler le volume » + « Ouvrir l'app » ; Android : MacroDroid → Déclencheur (heure 7:00) → Actions (volume multimédia / ouvrir URL / TTS lecture météo).
- <strong>Résultat attendu</strong> : Réalisable sans installation, abaissant le seuil de prise en main.
:::
