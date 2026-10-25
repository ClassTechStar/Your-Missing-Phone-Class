---
id: di-yi-zhang-harmony
part: ji-chu-pian
nav: Chapitre 1 Annexe : spécial HarmonyOS
toc: default
kind: supplement
---

### Chapitre 1 Annexe : spécial HarmonyOS

{class="chapter-intro mb-4"}
HarmonyOS est le système d'exploitation développé par Huawei, qui a traversé plusieurs versions majeures depuis sa sortie en 2019. Ce n'est pas « juste un autre substitut d'Android », mais une nouvelle espèce avec une philosophie de conception unique. Plongeons dans ce système en plein essor.

#### I. Qu'est-ce que HarmonyOS ? Pourquoi est-il différent ?

La philosophie centrale de HarmonyOS est « l'interconnexion de toutes choses ». Contrairement aux systèmes d'exploitation traditionnels principalement au service d'un seul appareil, HarmonyOS a été conçu dès le départ pour la collaboration multi-appareils.

<strong>L'architecture distribuée</strong> est l'âme de HarmonyOS. En bref, elle peut virtualiser plusieurs appareils en un « super terminal ». Votre smartphone, tablette, ordinateur, montre, TV ne sont plus des entités isolées, mais des « organes » d'un tout, capables de s'invoquer mutuellement leurs capacités.

Par exemple : vous regardez une vidéo sur votre smartphone et voulez la voir sur grand écran ; la méthode traditionnelle est le screencast ; sur HarmonyOS, vous pouvez « faire couler » la vidéo vers la TV pour continuer à la regarder, le smartphone devient télécommande. Ce n'est pas un simple screencast, c'est l'application elle-même qui s'exécute à travers les appareils.

#### II. HarmonyOS 4.3 : version mature basée sur AOSP

HarmonyOS 4.3 est la version largement déployée sur les smartphones Huawei actuels. À noter, HarmonyOS 4.3 est compatible avec le cadre de code du projet open source Android (AOSP), il peut donc être entièrement compatible avec les applications Android — la plupart des apps que vous téléchargez sur l'AppGallery de Huawei sont essentiellement des applications Android, exécutées via la couche de compatibilité de HarmonyOS. Mais HarmonyOS 4.3 n'est pas un simple Android renommé : il ajoute de nombreuses capacités distribuées propriétaires de Huawei, le moteur Ark, etc., sur la base d'AOSP.

##### Caractéristiques clés :

- <strong>Compatibilité des applications Android</strong>: comme il est développé sur AOSP, HarmonyOS 4.3 peut exécuter presque toutes les applications Android, l'utilisateur ne ressent quasiment aucune différence.
- <strong>Moteur Ark</strong>: compilateur et runtime propriétaires de Huawei, qui rendent les applications plus fluides et plus économes en énergie. Comparé aux premières versions, la fluidité s'est nettement améliorée.
- <strong>Super terminal</strong>: dans le centre de contrôle, vous pouvez voir intuitivement les autres appareils HarmonyOS à proximité, glisser-déposer pour connecter. Le smartphone invoque le clavier/souris de l'ordinateur, la tablette invoque la caméra du smartphone, très pratique.
- <strong>Cartes de service</strong>: similaires aux widgets d'iOS, mais plus flexibles. Vous pouvez faire glisser vers le haut l'icône d'une app pour déployer une carte et afficher les informations clés sans ouvrir l'app.
- <strong>mode pur</strong>: n'autorise l'installation d'applications que depuis le marché d'applications officiel, réduisant le risque de logiciels malveillants.
- <strong>Centre de confidentialité</strong>: gère centralisé des autorisations des applications, consulte l'historique de comportement des applications.

##### Caractéristiques de l'interface utilisateur :

- <strong>Écran de verrouillage magazine</strong>: l'écran de verrouillage affiche de belles images et articles, glissez pour entrer sur le bureau.
- <strong>Cartes universelles</strong>: les icônes du bureau peuvent se déployer en cartes, afficher plus d'informations.
- <strong>Super hub de transit</strong>: une zone de stockage temporaire, peut stocker texte, images, fichiers, puis les glisser dans n'importe quelle app. Le partage inter-applications devient ultra fluide.
- <strong>Recherche intelligente</strong>: recherche globale, peut chercher apps, fichiers, réglages, pages web.

#### III. HarmonyOS NEXT (HarmonyOS 6) : le vrai point de départ du système d'exploitation propriétaire de Huawei

HarmonyOS NEXT (HarmonyOS NEXT 5.0) est fondamentalement différent de HarmonyOS 4.3 — il adopte le micro-noyau HarmonyOS propriétaire de Huawei, ne dépend plus du noyau Linux et du code AOSP, et <strong>ne prend plus directement en charge les applications Android</strong>. C'est l'étape clé qui fait passer HarmonyOS de « forme de transition compatible Android » à « système d'exploitation totalement indépendant ».

##### Changements majeurs :

- <strong>Noyau entièrement propriétaire</strong>: HarmonyOS NEXT utilise le noyau propriétaire de Huawei, ne contient plus aucun code AOSP. Le système est plus léger, plus sûr, plus efficace.
- <strong>Ne prend plus en charge les applications Android</strong>: c'est le plus grand changement. HarmonyOS NEXT ne peut exécuter que des applications HarmonyOS natives, impossible d'installer et d'exécuter des fichiers APK. Avant la mise à niveau, vérifiez que vos apps usuelles ont déjà une version native HarmonyOS.
- <strong>Écosystème d'applications natives</strong>: Huawei pousse activement les développeurs à migrer leurs applications vers la plateforme native HarmonyOS. Actuellement, les apps principales comme WeChat, Alipay, Taobao ont déjà des versions natives HarmonyOS, mais certaines applications de niche peuvent ne pas encore être adaptées.
- <strong>Architecture de sécurité Xingdun</strong>: tout nouveau système de sécurité, protection de bout en bout du matériel au logiciel. Prend en charge un contrôle des autorisations plus fin, par exemple « localisation floue » — l'application ne sait que approximativement où vous êtes, pas la position précise.
- <strong>Intégration profonde de l'IA</strong>: capacités IA au niveau système, pas seulement une app avec IA. Par exemple, les sous-titres IA peuvent traduire les vidéos en temps réel, le détourage IA peut identifier intelligemment le sujet.
- <strong>Transfert sans couture inter-appareils</strong>: capacités distribuées encore plus avancées. L'état de l'application peut basculer sans couture entre appareils : le document que vous éditez sur le smartphone s'ouvre automatiquement sur l'ordinateur quand vous vous en approchez.
- <strong>Méta-services</strong>: services légers utilisables sans installation. Par exemple, scanner un QR code ouvre directement une fonctionnalité, sans avoir à télécharger l'app au préalable.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>À lire avant la mise à niveau vers HarmonyOS NEXT

{class="mt-1"}
Après la mise à niveau vers HarmonyOS NEXT, votre smartphone ne pourra plus exécuter d'applications Android. Avant la mise à niveau, vérifiez absolument : ① vos apps usuelles ont déjà une version native HarmonyOS ; ② votre travail ou votre vie quotidienne n'a pas de scénario absolument dépendant des applications Android. Après la mise à niveau, impossible de revenir à HarmonyOS 4.3.
:::

##### Changements dans la logique d'utilisation :

- <strong>Navigation gestuelle</strong>: glisser depuis le bord gauche/droit pour revenir en arrière, glisser vers le haut depuis le bas pour revenir au bureau, glisser vers le haut et marquer un arrêt pour ouvrir le multitâche.
- <strong>Fenêtres intelligentes multiples</strong>: prend en charge l'écran partagé, les fenêtres flottantes, la vue parallèle et d'autres formes de multitâche.
- <strong>Appel MianLian</strong>: service d'appel vidéo de Huawei, prend en charge le partage d'écran, la beauté, le flou d'arrière-plan.

#### IV. Écosystème HarmonyOS : appareils et applications

HarmonyOS n'est pas qu'un système pour smartphone, c'est un écosystème couvrant de multiples appareils.

##### Types d'appareils pris en charge :

- <strong>Smartphones et tablettes</strong>: appareils centraux, fonctionnalités les plus complètes.
- <strong>Montres connectées et bracelets</strong>: fonctionnement indépendant ou en collaboration avec le smartphone.
- <strong>Écrans intelligents (TV)</strong>: centre de divertissement familial.
- <strong>Enceintes intelligentes</strong>: point d'entrée d'interaction vocale.
- <strong>Automobiles</strong>: cockpit HarmonyOS, expérience de cabine intelligente.
- <strong>Maison connectée</strong>: réfrigérateurs, climatiseurs, lave-linges, etc.

##### État de l'écosystème d'applications :

Le magasin d'applications HarmonyOS propose des millions d'applications ; les applications principales y sont presque toutes. Huawei pousse activement les développeurs à créer des applications natives HarmonyOS. À mi-2026, WeChat, Alipay, Taobao, Douyin, Meituan, JD et autres applications majeures ont toutes lancé des versions natives HarmonyOS, l'usage quotidien est globalement sans obstacle. Certaines applications de niche et professionnelles peuvent encore être en cours d'adaptation ; avant la mise à jour, vérifiez si vos applications habituelles sont déjà prises en charge.

#### V. Astuces pratiques HarmonyOS

- <strong>Super terminal</strong>: glissez vers le bas depuis le coin supérieur droit pour ouvrir le centre de contrôle, cliquez sur « Super terminal », vous voyez les autres appareils à proximité, glissez-déposez pour connecter.
- <strong>Super hub de transit</strong>: appui long sur texte/image/fichier, choisissez « Copier vers le hub », puis appui long dans une autre app pour coller, ou glissez-déposez.
- <strong>Cartes de service</strong>: glissez vers le haut l'icône d'une app pour déployer la carte, appui long sur la carte pour ajuster la taille ou l'ajouter au bureau.
- <strong>Fenêtres intelligentes multiples</strong>: glissez vers l'intérieur depuis le bord gauche/droit de l'écran et marquez un arrêt, ouvrez la barre latérale, cliquez sur une app pour l'ouvrir en fenêtre flottante.
- <strong>Protection de la vie privée</strong>: Réglages &gt; Confidentialité, permet de consulter l'historique d'utilisation des autorisations, de régler la localisation floue, etc.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Précautions

{class="mt-1"}
HarmonyOS est en constante évolution, les différentes versions peuvent présenter quelques différences. Cette description se base sur les principales caractéristiques de HarmonyOS 4.3 et 6, pour les fonctionnalités spécifiques, référez-vous à la version réelle de votre smartphone. Il est recommandé de maintenir le système à jour pour bénéficier des dernières fonctionnalités et des correctifs de sécurité.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Essayez maintenant : découvrez les fonctionnalités phares de HarmonyOS

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Ouvrez le centre de contrôle, cherchez « Super terminal », voyez s'il y a d'autres appareils HarmonyOS à proximité.
2. Essayez le « Super hub de transit » : copiez un texte vers le hub, puis glissez-le dans Notes.
3. Faites glisser vers le haut les icônes de quelques apps usuelles, regardez ce qu'affichent leurs cartes de service.
4. Allez dans Réglages &gt; Confidentialité, regardez quelles applications ont récemment utilisé des autorisations sensibles.
:::
