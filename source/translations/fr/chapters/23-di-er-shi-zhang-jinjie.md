---
id: di-er-shi-zhang-jinjie
num: 20
part: jin-jie-pian
nav: Chapitre 20 : Mode développeur et permissions avancées
toc: default
kind: supplement
---

### Chapitre 20 : Mode développeur et permissions avancées

{class="chapter-intro mb-4"}
Ce chapitre est destiné à ceux qui veulent explorer en profondeur les « fonctionnalités cachées » du smartphone. Mode développeur, permissions Root, verrouillage BL... ces concepts très geek ne sont en réalité pas si éloignés des utilisateurs ordinaires.

#### I. Mode développeur : déverrouiller les réglages cachés

Le mode développeur est un menu caché intégré au système du téléphone, contenant de nombreuses fonctions inutiles aux utilisateurs ordinaires mais nécessaires aux développeurs.

##### Comment l'activer :

- <strong>Android</strong>: allez dans Réglages &gt; À propos du téléphone &gt; appuyez 7 fois sur « numéro de build », jusqu'à ce que le message « Vous êtes maintenant en mode développeur » apparaisse.
- <strong>HarmonyOS</strong>: Réglages &gt; À propos du téléphone &gt; appuyez 7 fois sur « version HarmonyOS ».
- <strong>iOS</strong>: les utilisateurs ordinaires ne peuvent pas activer le mode développeur complet, nécessite un compte Apple Developer payant.

##### Aperçu des fonctions courantes :

- <strong>Débogage USB</strong> : Interrupteur obligatoire pour les opérations avancées via ordinateur (flash, récupération de données, commandes ADB), voir la section « Commandes pratiques ADB » de ce chapitre.
- <strong>Afficher les opérations tactiles</strong> : Affiche les points de contact sur l'écran (un petit point suit le doigt), idéal pour enregistrer des tutoriels ou des démonstrations.

##### Lié aux performances et à la fluidité :

- <strong>Réglage de la vitesse d'animation (échelle d'animation de fenêtre / échelle d'animation de transition / échelle de durée d'animation)</strong> : Ces trois options contrôlent la durée des animations lors de l'ouverture d'applications et du changement de page. La valeur par défaut est 1x ; régler sur 0,5x rend le smartphone « apparemment » plus rapide (la vitesse d'exécution du programme ne change pas, seules les animations sont plus rapides) ; désactiver supprime les animations pour des transitions directes. La plupart des geeks règlent sur 0,5x, gardant une sensation de transition tout en paraissant plus rapide ; tout désactiver rend les opérations brutes et peut masquer les vrais ralentissements, vous donnant l'illusion que « c'est fluide ».
- <strong>Rendu GPU forcé (Force GPU Rendering)</strong> : Force tout le dessin 2D à être traité par le GPU plutôt que par le CPU. Sur les anciens modèles ou certaines applications mal optimisées, cela peut améliorer la fluidité de défilement, mais augmente également la charge du GPU et la consommation d'énergie. Les smartphones modernes utilisent déjà massivement le rendu GPU par défaut, cet interrupteur a un impact limité sur les modèles milieu et haut de gamme, c'est surtout une option héritée du passé, les utilisateurs ordinaires peuvent laisser la valeur par défaut.
- <strong>Analyse du mode de rendu GPU (Profile GPU Rendering)</strong> : Affiche en temps réel sur l'écran un histogramme du temps de rendu de chaque image, la ligne verte horizontale représente 16,6 ms (le seuil de temps d'image pour 60 fps). Si les barres dépassent la ligne verte, cela indique une perte d'images. C'est l'outil de prédilection des développeurs pour diagnostiquer les ralentissements d'applications, les utilisateurs ordinaires peuvent aussi l'utiliser pour comparer quelle application est mal optimisée — par exemple, si les barres d'une application dépassent souvent la ligne rouge lors du défilement, c'est probablement de sa faute.

##### Lié à l'arrière-plan et à l'autonomie :

- <strong>Limitation des processus en arrière-plan</strong> : Permet de définir « limitation standard », « 1 processus maximum », « 2 processus maximum », etc. En apparence, limiter les processus d'arrière-plan permet d'économiser de l'énergie, mais en réalité, la gestion intégrée d'Android est déjà performante, une limitation forcée provoque au contraire des rechargements fréquents des applications (le démarrage à froid consomme plus d'énergie et l'expérience se dégrade). Cette option est plutôt destinée au débogage, il n'est pas recommandé aux utilisateurs ordinaires de l'activer en permanence, conservez « limitation standard ».
- <strong>Ne pas conserver les activités</strong> : Détruit chaque interface dès que vous la quittez. Fortement déconseillé, provoque des écrans blancs fréquents et des rechargements d'applications, à utiliser uniquement pour tester la logique de restauration d'une application.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Précautions

{class="mt-1"}
Les réglages du mode développeur peuvent affecter la stabilité du système, ne modifiez pas les options que vous ne comprenez pas. Après avoir activé le débogage USB, soyez prudent lors de la connexion à un ordinateur, ne vous connectez pas à des ordinateurs non fiables.
:::

#### II. Déverrouillage OEM : l'« interrupteur de flash » dans les options de développement

Dans les options de développement se trouve un interrupteur discret mais important — « Déverrouillage OEM » (certaines marques l'appellent « Autoriser le déverrouillage OEM » ou « Déverrouillage de l'appareil »). Cet interrupteur ne déverrouille pas lui-même le bootloader, mais c'est une « autorisation préalable » : ce n'est qu'en l'activant que le fabricant vous permet de déverrouiller le BL via la commande fastboot ou l'outil de la marque.

- <strong>Rôle de l'interrupteur</strong> : Équivaut à déclarer au fabricant « j'accepte de renoncer à la garantie et d'assumer les risques, veuillez m'autoriser à déverrouiller le BL ». Si cet interrupteur est fermé, toute commande de déverrouillage du BL sera directement rejetée.
- <strong>Relation avec le verrouillage BL</strong> : Le déverrouillage OEM est la « demande de qualification », le déverrouillage BL est l'« opération réelle ». Le premier se fait d'un simple touché dans les réglages du smartphone, le second nécessite de demander un code de déverrouillage sur le site du fabricant et d'exécuter une commande fastboot sur ordinateur (par exemple <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">fastboot flashing unlock</code>), les deux sont indispensables.
- <strong>Une réinitialisation d'usine réinitialise-t-elle l'interrupteur ?</strong> : Oui. L'interrupteur « Déverrouillage OEM » revient à l'état fermé après une réinitialisation d'usine, mais le verrouillage BL, une fois déverrouillé, est un état physique qui ne se reverrouille pas avec une réinitialisation d'usine — il faut exécuter manuellement <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">fastboot flashing lock</code> pour le reverrouiller.
- <strong>Quand faut-il l'activer ?</strong> : À moins que vous ne soyez certain de vouloir flasher ou rooter, laissez-le fermé. Il est indépendant de l'« Débogage USB », les deux interrupteurs doivent généralement être activés simultanément lors du flash.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Le saviez-vous : pourquoi les fabricants ont-ils ajouté cet interrupteur ?

{class="mt-1"}
Les premières versions d'Android ne disposaient pas de cet interrupteur, les logiciels malveillants pouvaient flasher secrètement le système dès qu'ils obtenaient les permissions. Google a ensuite exigé que tous les fabricants Android intègrent un interrupteur « Déverrouillage OEM » dans les options de développement, comme une confirmation de « consentement éclairé de l'utilisateur ». C'est pourquoi, même si vous avez déverrouillé le BL, si l'interrupteur OEM est fermé, le reflash échouera.
:::

#### III. Verrouillage BL (Bootloader) : la première porte du flash

Le Bootloader est le programme qui charge le système d'exploitation au démarrage du téléphone. Le verrou BL est un verrou ajouté par les fabricants pour la sécurité, empêchant les utilisateurs de flasher un système non officiel.

##### Rôle du verrou BL :

- <strong>Protection de sécurité</strong>: empêche les logiciels malveillants d'être flashés dans le système.
- <strong>Anti-vol</strong>: même si le téléphone est flashé, il ne peut pas être utilisé sans le mot de passe du compte d'origine.
- <strong>Restriction de garantie</strong>: déverrouiller le BL signifie généralement perdre la garantie officielle.

##### Politique de verrou BL par marque :

- <strong>Xiaomi</strong>: peut être déverrouillé, nécessite de lier le compte et une période d'attente (7-30 jours).
- <strong>Huawei</strong>: a cessé de fournir les codes de déverrouillage après 2018, officiellement impossible à déverrouiller.
- <strong>OnePlus</strong>: peut être déverrouillé, relativement permissif.
- <strong>OPPO/vivo</strong>: certains modèles peuvent être déverrouillés, nécessite une demande.
- <strong>Samsung</strong>: peut être déverrouillé, mais déclenche le fusible Knox, perd Samsung Pay et d'autres fonctions.
- <strong>Apple</strong>: les appareils iOS n'ont pas de concept de verrou BL au sens traditionnel, mais ont un mécanisme de sécurité similaire.

#### IV. Commandes pratiques ADB : contrôler le smartphone depuis l'ordinateur

ADB signifie Android Debug Bridge, un outil en ligne de commande officiellement fourni par Google, permettant à un ordinateur de communiquer avec un smartphone Android via USB ou Wi-Fi. Il ne nécessite pas de Root, il suffit d'activer le « Débogage USB » sur le smartphone. On peut le comparer à une « télécommande permettant à l'ordinateur de donner des instructions au smartphone » — flash, installation d'applications, transfert de fichiers, consultation des journaux, tout dépend de lui.

##### Comment se connecter via USB :

1. Côté smartphone : accédez aux options de développement → activez « Débogage USB ».
2. Côté ordinateur : téléchargez Platform Tools depuis le site officiel de Google (incluant <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb</code> et <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">fastboot</code> deux fichiers exécutables), décompressez dans n'importe quel répertoire.
3. Connectez le smartphone et l'ordinateur avec un câble de données, le smartphone affichera la fenêtre « Autoriser le débogage USB ? », cochez « Toujours autoriser » et confirmez.
4. Dans la ligne de commande de l'ordinateur (PowerShell ou cmd sous Windows), exécutez <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb devices</code>, si la sortie ressemble à <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">List of devices attached / xxxxxxxx device</code>, la connexion est établie.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>N'ignorez pas les pilotes et la fenêtre d'autorisation

{class="mt-1"}
Si les utilisateurs Windows voient <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb devices</code> afficher « unauthorized » ou ne pas lister du tout l'appareil, c'est probablement parce que les pilotes ne sont pas correctement installés ou que vous avez oublié de cliquer sur « Autoriser » sur le smartphone. Les marques comme Samsung/Xiaomi peuvent installer leurs « pilotes USB » ou « assistants smartphone » respectifs pour compléter les pilotes ; Mac et Linux sont généralement sans pilote. Si vous avez accidentellement fermé la fenêtre contextuelle du smartphone, débranchez et rebranchez le câble pour la faire réapparaître.
:::

##### Commandes ADB courantes :

- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb install app.apk</code> : Installe un APK de l'ordinateur vers le smartphone (<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-r</code> indique une installation par-dessus en conservant les données ;<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-s</code> installer sur la carte SD).
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb uninstall com.xxx.xxx</code> : Désinstalle une application par nom de package.
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb push chemin_ordinateur /sdcard/chemin_destination</code> : Pousse un fichier de l'ordinateur vers le smartphone.
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb pull /sdcard/fichier chemin_ordinateur</code> : Tire un fichier du smartphone vers l'ordinateur (bien plus rapide que de s'envoyer sur WeChat puis de télécharger).
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell</code> : Entre dans le shell Linux du smartphone, permet d'exécuter directement <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">ls</code>, le<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pm</code>, le<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">am</code> et d'autres commandes.
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb reboot bootloader</code> : Redémarre le smartphone en mode Fastboot (point d'entrée du flash).
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb reboot recovery</code> : Redémarre en mode Recovery.
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm list packages</code> : Liste les noms de package de toutes les applications installées sur le smartphone (indispensable pour trouver un nom de package). Ajoutez <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-s</code> pour ne voir que les applications système, ajoutez <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-3</code> pour ne voir que les applications tierces.
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm uninstall --user 0 nom_de_package</code> : Désinstalle une application préinstallée pour l'utilisateur actuel, sans Root, voir la section pratique ci-dessous.

##### Pratique : désinstallation d'applications préinstallées sans Root :

C'est l'une des fonctions ADB les plus pratiques : utiliser la commande <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pm uninstall --user 0</code> permet de désinstaller une application préinstallée pour « l'utilisateur actuel », sans nécessiter de Root et sans affecter la partition système. L'application désinstallée « disparaît » du système, mais est toujours présente dans la partition système et reviendra après une réinitialisation d'usine.

1. Utilisez d'abord <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm list packages -s</code> pour lister toutes les applications système et trouver le nom de package que vous souhaitez désinstaller. Par exemple, le navigateur Xiaomi est <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.browser</code>, le magasin d'applications Huawei est <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.vmall.client</code>.
2. Vous ne savez pas à quelle application correspond un nom de package ? Sur l'ordinateur, utilisez <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm list packages | findstr mot-clé</code> pour rechercher, ou installez une application tierce « Package Viewer » pour consulter directement le nom de package de chaque application sur le smartphone.
3. Exécutez la désinstallation :<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm uninstall --user 0 nom_de_package</code>, par exemple <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm uninstall --user 0 com.android.browser</code>. Le retour de <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">Success</code> indique le succès.
4. Comment restaurer ? Deux méthodes : ① réinitialisation d'usine (la plus radicale mais fastidieuse) ; ② réinstallation :<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell cmd package install-existing nom_de_package</code>.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-skull-crossbones mr-2"></i>Ne supprimez jamais les packages système critiques

{class="mt-1"}
Bien que « pm uninstall --user 0 » soit une méthode sûre sans Root, supprimer aveuglément des applications système critiques (comme <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.systemui</code> barre d'état,<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.phone</code> téléphone,<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.settings</code> réglages) peut provoquer des crashs système, des écrans noirs, des impossibilités de démarrage et d'autres problèmes graves. Avant de supprimer, faites une recherche Google pour « ce nom de package peut-il être supprimé », mieux vaut supprimer moins que de se tromper. Il est recommandé de n'en supprimer qu'un ou deux à la fois, de confirmer qu'il n'y a pas de problème, puis de continuer.
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Le saviez-vous : que signifie --user 0 ?

{class="mt-1"}
Depuis Android 4.2, le multi-utilisateur est pris en charge, chaque utilisateur a un ID indépendant (le propriétaire est 0, les utilisateurs supplémentaires commencent à 10).<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">--user 0</code> signifie « désinstaller uniquement pour le propriétaire actuel », le fichier APK dans la partition système existe toujours, il est simplement masqué pour le propriétaire. C'est pourquoi il ne nécessite pas de Root — aucun fichier système n'est modifié, seule la « configuration utilisateur » est changée. C'est aussi la plus grande différence avec la désinstallation après Root : la désinstallation après Root supprime réellement du système, aucun utilisateur ne l'a plus ; la désinstallation ADB ne fait que « masquer pour l'utilisateur actuel ».
:::

#### V. Permissions Root : le « super administrateur » d'Android

Les permissions Root équivalent au superutilisateur sous Linux (contrôle total du répertoire /, lecture et écriture de n'importe quel fichier), c'est la permission la plus élevée du système Android. Il diffère fondamentalement de l'Administrator de Windows : Windows impose de nombreuses restrictions à l'administrateur par sécurité (la véritable permission la plus élevée est en fait TrustedInstaller), même l'Administrator ne peut pas exécuter directement comme le root Linux <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">sudo rm -rf /*</code>. Après avoir obtenu les permissions Root, vous pouvez modifier les fichiers système, désinstaller les applications préinstallées et utiliser des applications avancées nécessitant le Root.

##### Avantages du Root :

- Désinstaller les applications préinstallées non désinstallables.
- Utiliser des applications à fonctions avancées (comme Titanium Backup, Greenify).
- Modifier l'interface et les fonctions du système.
- Installer un Recovery tiers et des ROM personnalisées.

##### Risques du Root :

- <strong>Perte de la garantie</strong>: la plupart des fabricants ne garantissent pas les téléphones rootés.
- <strong>Risque de sécurité</strong>: les applications malveillantes peuvent obtenir les permissions Root, avec des conséquences graves.
- <strong>Instabilité du système</strong>: une mauvaise manipulation peut provoquer un crash du système.
- <strong>Applications bancaires inutilisables</strong>: de nombreuses applications bancaires et de paiement détectent le Root et refusent de fonctionner.
- <strong>Échec des mises à jour OTA</strong>: peut ne pas recevoir correctement les mises à jour système officielles.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-skull-crossbones mr-2"></i>Avertissement sérieux

{class="mt-1"}
L'opération de Root comporte des risques, peut rendre le téléphone inutilisable (brique). Si vous êtes débutant, il est conseillé de bien vous renseigner au préalable et de vous assurer d'avoir une sauvegarde complète. Avant toute opération, lisez attentivement le tutoriel, confirmez votre modèle de téléphone et la version du système.
:::

#### VI. Certification SafetyNet et Play Integrity : pourquoi les applications bancaires ne fonctionnent plus après le Root

Beaucoup d'utilisateurs Root ont connu ce moment de désarroi : après le Root, ils ont enthousiastement installé un tas de modules, puis en ouvrant l'application bancaire — « Votre appareil n'est pas sécurisé, utilisation impossible », Google Pay ne fonctionne plus, et même Netflix refuse la lecture HD. Derrière cela se cachent les deux mécanismes de certification d'intégrité d'appareil de Google : l'ancien SafetyNet et la nouvelle API Play Integrity.

##### Qu'est-ce que SafetyNet / Play Integrity :

- <strong>SafetyNet Attestation (ancienne version, depuis 2017)</strong> : API de vérification d'intégrité d'appareil lancée précocement par Google, les applications interrogent les serveurs de Google pour savoir « si cet appareil a passé les tests de compatibilité CTS et s'il est dans un état officiel non modifié ». Les résultats sont divisés en Basic Attestation (vérification de base) et Strong Attestation (vérification forte, reposant sur des clés matérielles). Google a annoncé que SafetyNet sera progressivement abandonné après 2024.
- <strong>Play Integrity API (nouvelle version, depuis 2022)</strong> : Solution de remplacement introduite par Google, plus stricte et plus complète que SafetyNet. Outre l'intégrité de l'appareil, elle inclut l'« intégrité de l'application » (l'app est-elle modifiée) et l'« intégrité du compte/autorisation » (le compte utilisateur est-il approuvé par Google). Les nouvelles applications devraient migrer vers Play Integrity.
- <strong>Qui l'utilise</strong> : Applications bancaires, financières et de paiement (par exemple Google Pay, les services bancaires en ligne de chaque banque, certains scénarios d'Alipay/WeChat Pay), streaming (protection des droits d'auteur Netflix HD), anti-triche pour certains jeux (par exemple certains jeux de Tencent/NetEase), applications de bureau d'entreprise (vérification de conformité des appareils MDM).

##### Trois niveaux de certification Play Integrity :

- <strong>MEETS_DEVICE_INTEGRITY (intégrité de l'appareil validée)</strong> : L'appareil exécute un système Android officiel, le bootloader n'est pas déverrouillé, pas de Root, les tests de compatibilité CTS sont passés. Les applications bancaires et de paiement peuvent être utilisées normalement.
- <strong>MEETS_BASIC_INTEGRITY (intégrité de base validée)</strong> : L'appareil est globalement fiable, mais peut présenter des anomalies mineures. Certaines applications peuvent être dégradées (par exemple, Netflix peut toujours lire mais avec une résolution limitée), certaines applications bancaires strictes refuseront directement.
- <strong>MEETS_STRONG_INTEGRITY (intégrité forte validée)</strong> : Le niveau le plus élevé, nécessite une attestation par clé matérielle (par exemple la puce Titan M de la série Google Pixel), la plupart des modèles de marques tierces ne l'atteignent pas même sans Root.
- <strong>Aucune étiquette (NO_INTEGRITY)</strong> : L'appareil est rooté, le BL est déverrouillé, une ROM tierce a été flashée ou l'appareil est identifié comme émulateur, la grande majorité des applications de paiement/bancaires refuseront de fonctionner.

##### Pourquoi ces applications cessent-elles de fonctionner après le Root :

Les applications envoient une demande de certification aux serveurs de Google via l'API Play Integrity, Google vérifie plusieurs indicateurs de l'appareil — l'état de verrouillage du bootloader, si la partition système a été modifiée, la présence du binaire su, si SELinux est en mode permissif, etc. Toute anomalie entraîne une baisse ou un vide du niveau de certification renvoyé, et l'application bancaire, voyant « appareil non sécurisé », refuse naturellement le service.

##### Solutions de masquage modernes : Magisk Hide / Shamiko / Zygisk :

Pour profiter de la commodité du Root tout en continuant à utiliser les applications bancaires, la communauté a développé une série de solutions pour « masquer l'état Root ». L'idée centrale est toujours : faire en sorte que le programme de détection voie non pas un système modifié, mais un appareil « d'apparence normale ».

- <strong>Magisk</strong> : La solution Systemless Root la plus répandue actuellement — ne modifie pas la partition système, mais implémente le Root par montage. L'avantage de cette conception est que le risque d'échec des mises à jour OTA est faible, la désinstallation est propre, et c'est la base de toutes les solutions de masquage ultérieures. Cependant, l'utilisation de Magisk nécessite toujours le déverrouillage du BL.
- <strong>Magisk Hide (abandonné)</strong> : Module de masquage intégré aux premières versions de Magisk, capable de masquer le Root pour des applications spécifiques. Mais il a été retiré de Magisk officiellement depuis 2021, la raison étant que Google n'a cessé d'améliorer ses méthodes de détection, les deux parties étant engagées dans un « jeu du chat et de la souris ».
- <strong>Zygisk</strong> : Nouveau mécanisme introduit dans Magisk 24.0+, similaire à Riru, implémente le chargement de modules en injectant le processus Zygote, plus discret que la modification directe du système. L'activation de Zygisk est un prérequis pour l'utilisation des solutions de masquage modernes.
- <strong>Shamiko</strong> : Le module de masquage le plus répandu actuellement, fonctionne avec Zygisk, peut masquer le Root pour des applications spécifiques (mode « liste blanche inversée »), masquer Magisk lui-même et falsifier l'état de verrouillage du bootloader. Shamiko est distribué via le dépôt LSPosed ou GitHub.
- <strong>Play Integrity Fix(osm0sis)</strong> : Module Magisk spécifiquement conçu contre la détection Google Play Integrity, modifie l'empreinte de l'appareil (fingerprint) pour que Google considère votre appareil comme un modèle officiel non rooté.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Le jeu du chat et de la souris ne finira jamais

{class="mt-1"}
Google met à jour les règles de détection de temps en temps, et les éditeurs d'applications suivent en améliorant la vérification Play Integrity. Une solution de masquage qui fonctionne aujourd'hui peut être identifiée demain. Si vous dépendez entièrement des applications bancaires/de paiement (par exemple, transferts quotidiens, paiements par code QR), le choix le plus sûr reste de ne pas rooter et de ne pas déverrouiller le BL. Les solutions de masquage conviennent mieux à une configuration de joueur du type « smartphone principal non rooté + smartphone de secours rooté ».
:::

#### VII. Conseils aux utilisateurs ordinaires

- <strong>Mode développeur</strong> : Peut être activé pour expérimenter l'accélération des animations, l'analyse du rendu GPU, etc., mais ne modifiez pas aveuglément d'autres options que vous ne comprenez pas.
- <strong>Déverrouillage OEM et verrouillage BL</strong> : Si vous n'avez pas l'intention de flasher ou de rooter, laissez les deux interrupteurs dans leur état par défaut (fermé) pour une sécurité maximale.
- <strong>ADB</strong> : Un outil puissant sans Root, utilisable par tout le monde — par exemple, utiliser <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pm uninstall --user 0</code> pour désinstaller des applications préinstallées. Mais avant de supprimer, vérifiez impérativement si le nom de package peut être supprimé.
- <strong>Root</strong> : Le Root n'est pas recommandé pour les utilisateurs ordinaires, les risques l'emportent sur les bénéfices. Si vous avez vraiment besoin de certaines fonctions, renseignez-vous d'abord sur l'existence d'alternatives ne nécessitant pas de Root (par exemple, désinstaller les applications préinstallées via ADB, utiliser Shizuku pour remplacer certaines fonctionnalités Root).

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>À faire : activez le mode développeur et ajustez la vitesse d'animation

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Allez dans Réglages &gt; À propos du téléphone.
2. Appuyez 7 fois sur « numéro de build », jusqu'à ce que le message indique que le mode développeur est activé.
3. Revenez aux réglages, trouvez « Options de développement » (généralement en bas des réglages ou dans « Système »).
4. Trouvez « Échelle d'animation de fenêtre », « Échelle d'animation de transition », « Échelle de durée d'animation », réglez-les toutes sur 0,5x ou désactivez-les.
5. Sentez si le téléphone est devenu plus rapide.
:::
