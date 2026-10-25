---
id: di-yi-zhang
num: 01
part: ji-chu-pian
nav: Chapitre 1 : Bonjour, mon ordinateur personnel
toc: default
kind: chapter
---

### Chapitre 1 : Bonjour, mon ordinateur personnel

{class="chapter-intro mb-4"}
Votre smartphone est en réalité le superordinateur le plus personnel de votre poche. Il est infiniment plus puissant que l'ordinateur qui a envoyé l'homme sur la Lune, et pourtant il repose silencieusement dans le creux de votre main. Aujourd'hui, allons à la rencontre de ce « géant silencieux ».

#### I. Les « organes internes » du matériel du smartphone : analyse approfondie

Aussi petit soit-il, le smartphone a tous ses organes. Comme lors d'un cours d'anatomie, découvrons un par un ces composants de précision.

##### 1. SoC (System on Chip) : le « cerveau + cœur » du smartphone

SoC signifie System on Chip, ce qui se traduit par « mettre tout le système sur une seule puce ». Ce n'est pas seulement le CPU (unité centrale de traitement), il intègre le CPU, le GPU (unité de traitement graphique), le NPU (unité de traitement neuronal), l'ISP (processeur de signal image), la bande de base (responsable des communications), etc.

C'est comme construire l'hôtel de ville, la centrale électrique, le centre de communication et le commissariat d'une ville dans un seul bâtiment, avec une efficacité redoutable.

##### CPU : le cœur du calcul généraliste

Le CPU est le composant le plus central du SoC, chargé de traiter la grande majorité des tâches de calcul. Les CPU de smartphones adoptent l'architecture ARM, différente de l'architecture x86 des ordinateurs. L'architecture ARM se distingue par un jeu d'instructions réduit (RISC), avec une consommation plus faible, mieux adaptée aux appareils mobiles.

<strong>Conception big.LITTLE du CPU</strong>: les CPU modernes de smartphones adoptent généralement une architecture « gros/petits cœurs » (technologie big.LITTLE d'ARM), qui divise les cœurs en différents niveaux de performance :

- <strong>Super cœur / gros cœur</strong>: performance maximale, chargé des tâches lourdes. Chargement de jeux, lancement d'applications, calculs complexes. Fréquence la plus élevée (3 GHz+), mais aussi consommation la plus forte.
- <strong>Cœur moyen</strong>: équilibre performance/consommation, traite les tâches de charge intermédiaire courantes. Scroller sur Weibo, regarder des vidéos, basculer entre applications s'appuient principalement sur lui.
- <strong>Petit cœur / cœur d'efficacité</strong>: consommation minimale, traite les tâches légères en arrière-plan. Veille, musique, réception de messages, etc., presque sans consommation électrique.

Les trois niveaux de cœurs travaillent ensemble : l'ordonnanceur du système alloue automatiquement selon la charge — les tâches légères aux petits cœurs pour économiser, les gros travaux aux gros cœurs pour attaquer fort, puis retour aux petits cœurs une fois terminé. C'est pourquoi le smartphone peut faire tourner fluidement des jeux tout en restant en veille toute la journée.

<strong>Caractéristiques d'architecture par marque</strong>:

- <strong>Qualcomm Snapdragon 8 Elite</strong>: adopte l'architecture CPU Oryon propriétaire (issue de l'acquisition de Nuvia), 2 super cœurs (4,32 GHz) + 6 cœurs de performance (3,53 GHz), tous basés sur le procédé 3 nm de deuxième génération de TSMC. Adieu définitivement l'architecture ARM publique, les performances monocœur et multicœur font un bond en avant. Le GPU Adreno 830 adopte une architecture en tranches, les performances graphiques progressent de 40 %, le NPU Hexagon atteint environ 45 TOPS, les performances d'inférence IA augmentent de 45 %. (Note : la version personnalisée Galaxy de Samsung a des fréquences plus élevées, le super cœur pouvant atteindre 4,47 GHz.)
- <strong>MediaTek Dimensity 9400</strong>: 1 super cœur (Cortex-X925, 3,62 GHz) + 3 cœurs de performance (Cortex-X4, 3,3 GHz) + 4 cœurs d'efficacité (Cortex-A720, 2,4 GHz), poursuite de l'architecture tous gros cœurs, procédé 3 nm de deuxième génération de TSMC. GPU Immortalis-G925 (12 cœurs), performances de pointe en hausse de 41 %, performances de lancer de rayons en hausse de 40 %. Le processeur IA est le NPU 890 de huitième génération, qui prend en charge l'exécution de grands modèles d'IA en local, l'entraînement LoRA local et la génération vidéo locale.
- <strong>Apple A18 Pro</strong>: 2 cœurs de performance (environ 4,04 GHz) + 4 cœurs d'efficacité (environ 2,4 GHz), procédé 3 nm de deuxième génération de TSMC. Le GPU 6 cœurs prend en charge le lancer de rayons matériel, le NPU 16 cœurs (environ 35 TOPS) fournit une puissance de calcul importante pour l'IA locale et Apple Intelligence. L'architecture propriétaire d'Apple reste en tête sur les performances monocœurs et le ratio performance/consommation, l'architecture mémoire unifiée offrant un avantage de bande passante pour l'inférence IA.
- <strong>HiSilicon Kirin 9020 de Huawei</strong>: embarqué sur la série Mate 70, adopte l'architecture CPU Taishan propriétaire, les capacités NPU et ISP continuent de se renforcer, prend en charge la 5.5G et la communication par satellite, représentant la dernière percée des puces nationales.

##### GPU : moteur de rendu graphique

Le GPU (Graphics Processing Unit) est spécialisé dans les tâches graphiques et de calcul parallèle. Son nombre de cœurs est bien supérieur à celui du CPU (souvent des centaines, voire des milliers de cœurs), mais chaque cœur est relativement simple, adapté au traitement simultané de grandes quantités de calculs similaires.

<strong>Processus de rendu graphique</strong>:

1. <strong>Traitement des sommets</strong>: calcule les coordonnées de position de chaque sommet du modèle 3D.
2. <strong>Rastérisation</strong>: convertit le graphique 3D en pixels sur l'écran 2D.
3. <strong>Ombrage des pixels</strong>: calcule la couleur, la texture et les effets d'éclairage de chaque pixel.
4. <strong>Composition de sortie</strong>: compose tous les calques en image finale et l'envoie à l'écran pour affichage.

<strong>Impact du GPU sur l'usage quotidien</strong>: pas seulement pour les jeux ! Le défilement de l'interface, les animations, la lecture vidéo, les filtres photo, les applications AR dépendent tous du GPU. Un smartphone avec un GPU faible peut souffrir de saccades lors du défilement, et les jeux seront carrément lagués.

<strong>GPU par marque</strong>: Qualcomm utilise son GPU Adreno propriétaire ; MediaTek utilise le GPU Mali d'ARM ; Apple utilise son GPU propriétaire, qui sert de référence dans l'industrie en termes de performances et d'efficacité énergétique.

##### NPU : moteur d'accélération IA

Le NPU (Neural Processing Unit) est un processeur spécialement conçu pour les calculs de réseaux de neurones. Comparé au CPU et au GPU, le NPU est plus efficace et moins énergivore pour les tâches d'IA.

<strong>Méthode de calcul des réseaux de neurones</strong>: l'opération centrale du NPU est la multiplication matricielle et la convolution — ce sont précisément les calculs les plus fondamentaux et les plus fréquents des réseaux de neurones. Grâce à une optimisation au niveau matériel, le NPU peut traiter en parallèle un grand nombre de calculs matriciels, des dizaines de fois plus vite que le CPU, avec une consommation bien moindre.

<strong>Processus de traitement IA</strong>:

1. <strong>Entrée des données</strong>: images de la caméra, audio du microphone, données de capteurs, etc.
2. <strong>Prétraitement</strong>: ajuste le format et la taille des données pour les adapter aux exigences d'entrée du réseau de neurones.
3. <strong>Calcul d'inférence</strong>: le NPU charge le modèle entraîné, effectue le calcul avant sur les données d'entrée et produit un résultat.
4. <strong>Post-traitement</strong>: convertit la sortie de l'IA en résultats utilisables, comme les coordonnées d'un visage, le contenu textuel, les étiquettes de scène.

<strong>Scénarios d'application concrets</strong>:

- <strong>Photographie computationnelle</strong>: synthèse de mode nuit, flou d'arrière-plan portrait, traitement HDR, beauté par IA.
- <strong>Assistant vocal</strong>: reconnaissance vocale, compréhension du langage naturel, synthèse vocale.
- <strong>Traduction en temps réel</strong>: sous-titres IA, traduction de conversation.
- <strong>Reconnaissance intelligente</strong>: reconnaissance de texte (OCR), reconnaissance d'objets, reconnaissance de scènes.
- <strong>Grands modèles IA sur terminal</strong>: les puces phares les plus récentes prennent déjà en charge l'exécution locale de petits grands modèles d'IA (niveau 7B paramètres), permettant des fonctions telles que dialogue IA hors ligne, résumé de documents, rédaction intelligente. Le NPU Hexagon du Snapdragon 8 Elite offre environ 45 TOPS, le NPU 890 du Dimensity 9400 prend également en charge les grands modèles en local (vitesse d'inférence LLM en hausse de 80 %), et le NPU 16 cœurs de l'Apple A18 Pro fournit environ 35 TOPS.
- <strong>Traitement d'image par IA</strong>: effacement IA (supprimer en un clic les passants sur une photo), extension d'image IA (agrandir les bords d'une image), conversion de style IA, génération d'images à partir de texte, etc.

##### ISP : processeur de signal image

L'ISP traite les données brutes provenant de la caméra et transforme les signaux lumineux en belles photos.

<strong>Comment évaluer les performances ?</strong> Regardez le modèle ! Apple A18 Pro, Qualcomm Snapdragon 8 Elite, MediaTek Dimensity 9400, Huawei Kirin 9020 sont tous de niveau phare. En milieu de gamme, regardez Snapdragon 8s Gen3/7+ Gen3, Dimensity 8400. Ne vous fiez pas qu'au nombre de cœurs : l'architecture et le procédé (nombre de nanomètres) sont plus importants. Le procédé 3 nm est actuellement le plus avancé, avec un ratio performance/consommation bien supérieur à 5 nm et 4 nm.

##### 2. Mémoire vive (RAM) : plan de travail temporaire

La RAM est comme votre bureau : plus il est grand, plus vous pouvez étaler de fichiers en même temps. 12 Go est la norme actuelle, 16 Go convient aux utilisateurs intensifs, 24 Go et plus est le choix des joueurs et des geeks.

Le type de RAM compte aussi : LPDDR5 est plus rapide et plus économe que LPDDR4X. Bien qu'Apple n'ait pas beaucoup de RAM, l'optimisation du système fait qu'elle paraît « suffisante ».

<strong>Que se passe-t-il quand la RAM est insuffisante ?</strong> Les apps sont tuées en arrière-plan par le système, et doivent se recharger lors du basculement. C'est pourquoi parfois, quand vous revenez d'un court instant sur WeChat, votre jeu a disparu.

##### 3. Stockage (ROM/flash) : entrepôt à long terme

Le stockage est comme votre bibliothèque — l'endroit où sont rangées toutes les photos, vidéos et apps. La norme actuelle est UFS 3.1 ou UFS 4.0, plusieurs fois plus rapide que l'ancien eMMC.

<strong>Pourquoi la vitesse de stockage est-elle importante ?</strong> Elle détermine la vitesse d'ouverture des apps, de chargement des jeux et d'enregistrement des photos. Avec le temps, un stockage lent rendra le smartphone de plus en plus lagué.

##### 4. Écran : vos yeux

L'écran est la principale fenêtre d'interaction entre vous et le smartphone ; sa qualité affecte directement l'expérience.

- <strong>Matériau</strong>: OLED offre des couleurs vives, un contraste élevé et une meilleure efficacité énergétique (les pixels ne s'allument pas en noir), mais à basse luminosité peut présenter un scintillement fatigant pour les yeux ; LCD est plus doux pour les yeux et moins coûteux, mais le contraste et les couleurs sont inférieurs à l'OLED.
- <strong>Résolution</strong>: 1080p est la norme, 2K est plus net mais plus énergivore. Le concept d'« écran Rétina » d'Apple signifie : à une certaine distance, l'œil humain ne peut pas distinguer les pixels.
- <strong>Taux de rafraîchissement</strong>: 60 Hz est standard, 90 Hz/120 Hz est plus fluide, le défilement devient soyeux. Les taux élevés consomment plus, donc beaucoup de smartphones prennent en charge le taux adaptatif (LTPO), qui s'ajuste dynamiquement selon le contenu.
- <strong>Taux d'échantillonnage tactile</strong>: affecte la réactivité du tactile ; les joueurs doivent y prêter attention, plus c'est élevé, plus c'est réactif.
- <strong>Méthode de gradation</strong>: la gradation DC est plus douce pour les yeux que la gradation PWM, moins de fatigue à basse luminosité. Beaucoup de smartphones prennent désormais en charge la gradation PWM à haute fréquence, également pour protéger les yeux.

##### Technologie HDR d'écran

Le HDR (High Dynamic Range) permet à l'écran d'afficher simultanément des zones claires plus lumineuses et des zones sombres plus sombres, améliorant considérablement le relief de l'image.

- <strong>Principe</strong>: la plage de luminosité d'un écran ordinaire (SDR) est limitée, l'écart entre le plus clair et le plus sombre n'est pas suffisant. Les écrans HDR ont une luminosité de crête plus élevée (généralement plus de 1000 nits), un contraste plus important, une gamme de couleurs plus large, et peuvent afficher plus de détails.
- <strong>Normes principales</strong>: HDR10 (la plus basique, gratuite et open source), HDR10+ (poussée par Samsung, métadonnées dynamiques), Dolby Vision (qualité d'image optimale mais nécessite une licence). La norme prise en charge par le smartphone dépend du matériel d'écran et de la licence système.
- <strong>Effet réel</strong>: lors du visionnage de vidéos HDR, le soleil est plus éblouissant, les ombres plus profondes, les couleurs plus riches. À condition que la vidéo elle-même soit produite en HDR et que l'écran prenne en charge l'affichage HDR.

##### Technologie HDR d'image

Le HDR en photo et le HDR d'écran sont deux choses différentes. Le HDR d'image résout par algorithme le problème des « zones claires surexposées, zones sombres bouchées ».

- <strong>Principe algorithmique</strong>: lorsque vous appuyez sur le déclencheur, le smartphone prend en réalité plusieurs photos à différentes expositions (sous-exposée pour préserver les détails clairs, surexposée pour préserver les détails sombres, exposition normale pour préserver les tons moyens), puis les synthétise en une seule photo à plage dynamique élevée.
- <strong>Processus de traitement</strong>: capture multi-images → alignement et compensation (anti-tremblement) → fusion d'exposition / mappage de tons → correction des couleurs → sortie de la photo finale.
- <strong>Optimisation de l'effet</strong>: les smartphones actuels peuvent déjà faire du « HDR en temps réel » — ce que vous voyez dans le viseur est l'image après traitement HDR, WYSIWYG. Le Smart HDR d'Apple et le HDR automatique d'Android sont très aboutis.

##### 5. Batterie et charge : source d'énergie

La batterie est la pièce la plus « courte durée de vie » du smartphone, elle vieillit visiblement après deux ou trois ans. La capacité principale actuelle est de 5500-7500 mAh.

- <strong>Puissance de charge</strong>: le camp Android est déjà monté à 100 W voire 200 W, recharge en une dizaine de minutes ; Apple en est encore à 20-30 W. La charge rapide abîme-t-elle la batterie ? Avec les accessoires d'origine, ça passe, le smartphone a une protection thermique.
- <strong>Charge sans fil</strong>: pratique mais inefficace, chauffe beaucoup. Adaptée à la recharge au bureau, pas adaptée quand on est pressé de sortir.
- <strong>Charge inversée</strong>: le smartphone se transforme en batterie externe, pour recharger écouteurs et montres, en cas d'urgence.

##### 6. Caméras : la magie de la lumière et de l'ombre

Aujourd'hui, les smartphones ont souvent trois ou quatre caméras, chacune avec son rôle :

- <strong>Caméra principale</strong>: la plus utilisée, le capteur le plus grand, la meilleure qualité d'image.
- <strong>Grand angle</strong>: pour les paysages, les bâtiments, champ de vision plus large.
- <strong>Téléobjectif</strong>: pour photographier au loin, distinction entre zoom optique et zoom numérique.
- <strong>Macro</strong>: pour les toutes petites choses de très près.

<strong>Le nombre de pixels n'est pas tout !</strong> La taille du capteur (un grand capteur écrase un petit), l'ouverture (f/1.8 est plus grande que f/2.4), la stabilisation (OIS optique est importante) affectent toutes la qualité d'image. La photographie computationnelle (algorithmes IA) est de plus en plus importante, capable de synthétiser plusieurs photos en une seule bonne photo.

##### Téléobjectif périscopique

Les téléobjectifs traditionnels nécessitent un long chemin optique, ce qui épaissit le smartphone. Le téléobjectif périscopique utilise un prisme à 90 degrés pour réfracter la lumière, de sorte que le chemin optique se déploie latéralement à l'intérieur du smartphone, réalisant ainsi un zoom optique 5x voire 10x tout en gardant le smartphone fin.

- <strong>Principe structurel</strong>: la lumière entre par l'objectif → réfraction à 90° par le prisme → traverse le groupe de lentilles le long de la largeur du smartphone → atteint le capteur. Cela revient à poser un télescope vertical à l'horizontale.
- <strong>Caractéristiques optiques</strong>: zoom optique élevé (5x-10x), qualité d'image bien supérieure au zoom numérique. Mais le capteur est généralement plus petit que celui de la caméra principale, performance en basse lumière moyenne.
- <strong>Avantage d'image</strong>: photographier la lune, les bâtiments éloignés, les gros plans sur scène — hors de portée des smartphones ordinaires.

##### OIS stabilisation optique vs EIS stabilisation électronique

La stabilisation est une technologie clé affectant la qualité de photo et de vidéo ; les deux méthodes ont des principes totalement différents :

- <strong>OIS (stabilisation optique)</strong>: compense les tremblements de la main en déplaçant physiquement l'objectif ou le capteur. L'objectif contient un gyroscope miniature qui détecte la direction et l'amplitude du tremblement, puis entraîne un moteur pour déplacer le groupe de lentilles en sens inverse. L'avantage est qu'il n'y a pas de perte de qualité d'image ; l'inconvénient est le coût élevé et l'encombrement.
- <strong>EIS (stabilisation électronique)</strong>: compense les tremblements par recadrage et décalage logiciels de l'image. Le smartphone enregistre une zone légèrement plus grande, puis recadre une zone stable selon les données du gyroscope. L'avantage est qu'aucun matériel supplémentaire n'est nécessaire ; l'inconvénient est qu'il recadre l'image (champ de vision réduit) et peut flouter en basse lumière.
- <strong>Choix pratique</strong>: pour la photo, privilégiez l'OIS ; pour la vidéo, la combinaison des deux donne le meilleur résultat. Beaucoup de smartphones phares prennent désormais en charge la stabilisation par déplacement de capteur « Sensor-Shift », plus efficace que la stabilisation d'objectif traditionnelle.

##### Zoom optique vs zoom numérique

- <strong>Zoom optique</strong>: modifie la focale en déplaçant physiquement le groupe de lentilles, sans perte de qualité. Sur smartphone, le zoom optique n'a généralement que des rapports fixes (2x, 3x, 5x, 10x), il ne peut pas zoomer en continu comme un appareil photo.
- <strong>Zoom numérique</strong>: agrandit la zone centrale de l'image, c'est essentiellement un recadrage + interpolation. Plus on zoome, plus la qualité se dégrade. Le zoom numérique 100x a l'air cool, mais la qualité réelle est déjà très floue.
- <strong>Zoom hybride</strong>: combine optique et numérique, compense la perte de qualité entre les rapports de zoom optique par un algorithme de fusion multi-images. Meilleur que le zoom numérique pur, mais toujours inférieur au zoom optique.

##### Audio : haut-parleurs et puce graphique dédiée

<strong>Haut-parleur unique vs double haut-parleurs</strong>:

- <strong>Haut-parleur unique</strong>: un seul élément sonore en bas, le son penche d'un côté, sans effet stéréo. Courant sur les smartphones d'entrée et milieu de gamme.
- <strong>Double haut-parleurs (stéréo)</strong>: un en haut et un en bas, formant un champ stéréo. Lors du visionnage de vidéos ou de l'écoute de musique, les canaux gauche et droit sont bien séparés, l'immersion est bien meilleure. L'écouteur fait souvent office de haut-parleur supérieur.
- <strong>Différence de qualité sonore</strong>: les doubles haut-parleurs ne sont pas seulement « plus forts », ils offrent surtout une sensation d'espace et de relief. Regarder un film avec un seul haut-parleur donne toujours l'impression qu'il manque quelque chose.

<strong>Puce graphique dédiée des smartphones gaming</strong>:

Certains smartphones gaming et de performance sont équipés d'une puce de traitement d'affichage dédiée, dont le rôle est :

- <strong>Insertion d'images</strong>: interpole par algorithme les images de jeu de 30 fps à 60 fps ou 120 fps, pour un rendu plus fluide. Ce processus est effectué sur la puce dédiée, sans occuper les ressources GPU du SoC.
- <strong>Super-résolution</strong>: améliore par algorithme IA une image basse résolution en haute résolution, pour une meilleure netteté.
- <strong>Réduction de consommation</strong>: comme l'insertion d'images et la super-résolution sont prises en charge par la puce dédiée, la charge du SoC diminue, la chaleur et la consommation baissent, le jeu est plus stable.

##### GPS : mono-fréquence et bi-fréquence

La localisation du smartphone dépend principalement de systèmes de navigation par satellite tels que le GPS.

- <strong>GPS mono-fréquence</strong>: ne reçoit que le signal de la bande L1, précision de positionnement d'environ 3-5 mètres. Suffisant en zone dégagée, mais dans les canyons urbains denses en gratte-ciel, la réflexion du signal entraîne un positionnement plus erroné.
- <strong>GPS bi-fréquence</strong>: reçoit simultanément les signaux des bandes L1 et L5. La bande L5 a une longueur d'onde plus longue et une meilleure résistance aux interférences ; le calcul combiné bi-fréquence permet d'éliminer la plupart des erreurs ionosphériques, avec une précision de 1-3 mètres. Avantage net en navigation urbaine et pour la localisation des VTC.
- <strong>Support multi-constellations</strong>: les smartphones modernes prennent en charge non seulement le GPS, mais aussi BeiDou (Chine), GLONASS (Russie), Galileo (Europe) et d'autres systèmes satellites. Plus on connecte de satellites simultanément, plus la localisation est rapide et précise.

##### 7. Capteurs : les petites antennes du smartphone

Une dizaine de capteurs cachés dans le smartphone travaillent en silence :

- <strong>Accéléromètre + gyroscope</strong>: perçoit l'orientation du smartphone, sert à tourner dans les jeux, à la rotation automatique de l'écran.
- <strong>Capteur de luminosité</strong>: règle automatiquement la luminosité de l'écran.
- <strong>Capteur de proximité</strong>: éteint l'écran quand le smartphone est collé à l'oreille pendant un appel.
- <strong>Capteur d'empreintes</strong>: la norme actuelle est l'empreinte optique sous écran ou ultrasonique.
- <strong>Reconnaissance faciale</strong>: le Face ID d'Apple est en lumière structurée 3D, niveau de sécurité élevé ; beaucoup d'Android utilisent la reconnaissance 2D par photo, sécurité moyenne.
- <strong>NFC</strong>: communication en champ proche, pour les cartes de transport, badges d'accès, cartes bancaires.
- <strong>Baromètre</strong>: mesure l'altitude, détecte même la montée d'un étage.
- <strong>Capteur à effet Hall</strong>: détecte l'ouverture/fermeture d'une coque magnétique.

#### II. Système d'exploitation : Android VS iOS VS HarmonyOS

Le matériel est le corps, le système d'exploitation est l'âme. Les trois systèmes ont chacun leur caractère :

- <strong>Android</strong>: comme une communauté open source, les fabricants peuvent le personnaliser en profondeur, beaucoup de choix. Vous pouvez changer de thème, installer des magasins d'applications tiers, bidouiller toutes sortes de choses. Mais en raison de cette ouverture, la fragmentation est grave, l'expérience varie beaucoup selon les marques.
- <strong>iOS</strong>: comme un jardin soigneusement entretenu, Apple maîtrise le matériel et le logiciel, l'expérience est unifiée et fluide. La qualité des applications est élevée, la protection de la vie privée est bonne, mais la liberté est faible, il faut suivre les règles d'Apple.
- <strong>HarmonyOS</strong>: la nouvelle espèce de Huawei, axée sur les capacités distribuées, permettant à différents appareils de collaborer sans couture. Nous en parlerons spécifiquement plus loin.

Les trois écosystèmes sont extrêmement riches, choisissez le mode de vie que vous préférez. Il n'y a pas de bon ou de mauvais absolu, seulement ce qui vous convient ou non.

#### III. Analyse complète des interfaces du smartphone

Les interfaces du smartphone sont les ponts vers le monde extérieur, et leurs différences sont grandes :

##### Micro USB

- <strong>Caractéristiques physiques</strong>: interface trapézoïdale plate, avec sens de branchement (ne s'insère pas à l'envers). Essentiellement éliminée des smartphones, mais encore utilisée sur certains appareils bas de gamme et anciens.
- <strong>Limites de transmission</strong>: ne prend en charge que la norme USB 2.0, débit maximal de 480 Mbps, puissance de charge généralement inférieure à 10 W.
- <strong>Inconvénient</strong>: pas réversible, durée de vie de branchement courte, vitesse de transmission lente, puissance de charge faible.

##### Lightning (interface Apple, éliminée)

- <strong>Caractéristiques physiques</strong>: interface 8 broches propriétaire d'Apple, réversible. Utilisée sur l'iPhone 14 et antérieurs, désormais totalement éliminée.
- <strong>Limites de transmission</strong>: Lightning ne prend physiquement en charge que la norme USB 2.0, débit maximal de 480 Mbps. Même avec un câble USB-C vers Lightning, la vitesse de transmission est limitée par l'interface Lightning elle-même.
- <strong>Raison de l'élimination</strong>: l'UE a adopté une réglementation exigeant que tous les smartphones utilisent l'USB-C à partir de 2024 ; Apple est passé au Type-C à partir de la série iPhone 15. L'interface Lightning s'est officiellement retirée de la scène.
- <strong>Attention</strong>: les câbles certifiés MFi d'Apple contiennent une puce d'authentification ; les câbles non certifiés peuvent ne pas charger ou transmettre correctement. Si vous utilisez encore un ancien iPhone, gardez un câble Lightning à portée de main.

##### USB Type-C

- <strong>Caractéristiques physiques</strong>: interface ovale 24 broches, réversible. Devenue l'interface standard des smartphones et de la plupart des appareils électroniques. L'UE a légiféré pour exiger que tous les smartphones, tablettes, écouteurs et autres appareils portables utilisent l'USB-C à partir de 2024, et d'autres régions suivent.
- <strong>Protocole de transmission</strong>: Type-C n'est que la forme de l'interface, la capacité de transmission réelle dépend du protocole interne. Prend en charge USB 2.0 (480 Mbps), USB 3.0/3.1/3.2 (5-20 Gbps) voire USB4 (40 Gbps).
- <strong>Distinction importante</strong> : Tous les ports USB-C ne prennent pas en charge USB 3.0 ! Beaucoup de smartphones utilisent un port USB-C, mais ne connectent en interne que les broches USB 2.0, offrant une vitesse de transfert aussi lente que les anciens ports. Les iPhone 16/17 standard ne prennent en charge que la vitesse USB 2.0, et seules les versions Pro prennent en charge USB 3.0 (avec un câble USB-C to USB-C).
- <strong>Capacité de charge</strong>: prend en charge les protocoles de charge rapide tels que USB PD, jusqu'à 240 W.
- <strong>Sortie vidéo</strong>: prend en charge DisplayPort Alt Mode, peut sortir de la vidéo vers un écran via un adaptateur.

##### Interface audio 3,5 mm

- <strong>Caractéristiques physiques</strong>: jack rond 3 ou 4 segments, 3 segments transmettent les canaux audio gauche/droit, 4 segments ajoutent un canal microphone.
- <strong>Caractéristiques</strong>: transmission de signal analogique, plug-and-play, sans pilote ni conversion. Qualité sonore stable, latence nulle.
- <strong>État actuel</strong>: la plupart des smartphones phares ont supprimé l'interface 3,5 mm, il faut un adaptateur Type-C ou utiliser des écouteurs Bluetooth. Certains smartphones milieu de gamme et gaming la conservent.

#### IV. Gamme de produits et règles de nommage

Face à la gamme éblouissante de chaque marque, comprendre les règles de nommage peut vous aider à rapidement cibler le modèle qui vous convient.

##### Séries de produits des grandes marques :

- <strong>Apple</strong> : iPhone (standard) / iPhone Plus (grand écran) / iPhone Pro (professionnel) / iPhone Pro Max (grand écran professionnel) / iPhone SE (économique) / iPhone 16e (économique avec IA, équipé de la puce A18 et du modem C1 conçu par Apple). En 2026, la série iPhone 17 est équipée de la puce A19 Pro, avec des capacités IA encore améliorées.
- <strong>Huawei</strong>: série Mate (phare business) / série P/Pura (phare photographique) / série Mate X (phare pliable) / série nova (milieu de gamme jeune) / série Enjoy (entrée de gamme)
- <strong>Xiaomi</strong>: série numérique Xiaomi (phare) / Xiaomi MIX (phare d'exploration/pliable) / série Redmi K (phare de performance) / série Redmi Note (milieu de gamme) / série numérique Redmi (entrée de gamme)
- <strong>OPPO</strong>: série Find X (phare) / série Reno (milieu de gamme) / série A (entrée de gamme) / série numérique OnePlus (phare de performance)
- <strong>vivo</strong>: série X (phare photographique) / série numérique iQOO (phare de performance) / série S (selfie milieu de gamme) / série Y (entrée de gamme)
- <strong>Samsung</strong>: série Galaxy S (phare) / Galaxy Z Fold/Flip (phare pliable) / série Galaxy A (milieu de gamme)

##### Signification des suffixes courants :

- <strong>Pro</strong>: abréviation de Professional, version professionnelle. Généralement, sur la base de la version standard, met à niveau la caméra, l'écran, le processeur et autres configurations clés.
- <strong>Max</strong>: version la plus grande. Écran le plus grand, batterie la plus grande, mais la configuration n'est pas nécessairement supérieure à Pro.
- <strong>Ultra</strong>: version ultime. Représente généralement la configuration la plus élevée de la série, le plus de matériel, le prix le plus haut. Ex. Samsung S24 Ultra, Xiaomi 14 Ultra.
- <strong>SE</strong>: Special Edition, en réalité souvent une version économique. Configuration réduite, prix abaissé. Ex. iPhone SE.
- <strong>Plus</strong>: version agrandie. Écran plus grand que la version standard, batterie aussi, mais configuration essentiellement identique.
- <strong>Lite / version jeunesse</strong>: version allégée. Configuration simplifiée, prix plus bas.
- <strong>Note</strong>: désignait à l'origine un smartphone à grand écran, aujourd'hui l'usage varie selon les marques. Redmi Note est une série milieu de gamme.
- <strong>Neo</strong>: version novatrice. Désigne généralement un modèle milieu de gamme orienté performance.

#### V. Baseband et antennes : les héros méconnus de la communication

Si le smartphone peut appeler et aller sur Internet, c'est grâce au duo baseband + antenne.

##### Puce baseband :

Le baseband est le processeur du smartphone responsable de la communication radio : il module le signal numérique en ondes radio émises, et démodule les ondes radio reçues en signal numérique. Les performances du baseband affectent directement la qualité d'appel, la vitesse Internet et la stabilité du signal. Qualcomm est le plus grand fournisseur de baseband pour smartphones ; MediaTek et Samsung ont aussi leur baseband propriétaire. Apple a commencé à embarquer son baseband C1 propriétaire sur l'iPhone 16e, marquant l'entrée d'Apple dans l'ère du baseband propriétaire : le C1 utilise un procédé 4 nm, avec une excellente consommation ; l'iPhone 16/16 Plus/16 Pro/16 Pro Max utilise encore un baseband Qualcomm (Snapdragon X75 5G), et l'on s'attend à une transition progressive vers le baseband propriétaire sur les modèles suivants. Plus tôt, l'iPhone XS/11 avec baseband Intel souffrait de mauvaise réception, un point douloureux pour de nombreux utilisateurs.

##### Conception d'antennes :

Les antennes du smartphone sont cachées à l'intérieur, généralement disposées autour du châssis. La conception des antennes affecte directement la performance de réception du signal :

- <strong>Technologie MIMO</strong>: multiple entrée multiple sortie, utilise plusieurs antennes pour émettre et recevoir simultanément, améliore la vitesse et la stabilité. 4×4 MIMO est plus rapide que 2×2 MIMO.
- <strong>Nombre d'antennes</strong>: les smartphones phares ont généralement une dizaine d'antennes (cellulaire, Wi-Fi, Bluetooth, NFC, GPS chacune nécessite une antenne indépendante).
- <strong>Impact du châssis métallique</strong>: le métal blinde le signal, donc les smartphones à châssis métallique nécessitent des bandes d'antenne (bandes plastiques sur le châssis). Les châssis en verre et plastique affectent peu le signal.

##### Évolution des technologies réseau :

- <strong>4G LTE</strong>: débit théorique maximal 1 Gbps en descendant / 500 Mbps en montant (Cat.18), expérience réelle généralement 50-150 Mbps. Couverture la plus large, suffisant.
- <strong>5G NR</strong>: débit théorique maximal 10 Gbps+ en descendant. La bande Sub-6 GHz a une meilleure couverture, l'onde millimétrique mmWave est extrêmement rapide mais avec une couverture très réduite.
- <strong>5G-A (5G Advanced)</strong> : Version améliorée de la 5G, aussi appelée 5.5G. Le débit descendant peut atteindre 10 Gbps, le débit montant 1 Gbps, avec une densité de connexion et une précision de localisation largement améliorées. Depuis 2024, China Mobile, China Telecom et China Unicom déploient des réseaux 5G-A dans les principales villes. Les séries Huawei Mate 70/80, Xiaomi 15/16 et autres smartphones phares prennent déjà en charge la 5G-A. La 5G-A apporte également une capacité de « communication et perception intégrées », où les stations de base peuvent simultanément communiquer et percevoir l'environnement, fournissant l'infrastructure pour l'économie des basses altitudes (livraison par drones) et la connectivité véhicule.

##### Classification des bandes de fréquences réseau :

Les bandes de fréquences prises en charge par le smartphone déterminent dans quels pays et sur quels opérateurs il peut être utilisé :

- <strong>FDD-LTE Band (série B)</strong>: ex. B1, B3, B5, etc., bandes 4G. Différents pays utilisent différentes bandes ; la Chine utilise principalement B1/B3/B5/B8/B34/B38/B39/B40/B41.
- <strong>TDD-LTE Band</strong>: autre norme 4G, largement utilisée en Chine sur B38/B39/B40/B41.
- <strong>5G NR Band (série N)</strong>: ex. n1, n3, n28, n41, n78, n79, etc. n78 (3,5 GHz) est la bande 5G principale en Chine, n41 (2,5 GHz) est surtout utilisée par China Mobile.
- <strong>Conseil d'achat</strong>: si vous devez voyager à l'étranger, vérifiez avant l'achat si le smartphone prend en charge les bandes du pays cible. Les smartphones officiel chinois prennent généralement en charge toutes les bandes chinoises, mais peuvent manquer certaines bandes étrangères.

#### VI. Votre smartphone, combien de rôles joue-t-il ?

Il y a bien longtemps cessé d'être un simple téléphone :

1. <strong>Outil de communication</strong>: téléphone, SMS, WeChat, e-mail...
2. <strong>Appareil photo intelligent</strong>: photo, vidéo, scan de documents...
3. <strong>Portefeuille</strong>: paiement, carte de transport, carte bancaire, carte de membre...
4. <strong>Portail d'information</strong>: actualités, météo, bourse, connaissances...
5. <strong>Console de jeux</strong>: du match-3 aux blockbusters AAA...
6. <strong>Bureau mobile</strong>: documents, tableaux, réunions, collaboration...
7. <strong>Assistant santé</strong>: podomètre, fréquence cardiaque, sommeil, sport...
8. <strong>Télécommande de maison connectée</strong>: contrôler lumières, climatisation, TV, robot aspirateur...
9. <strong>Pièce d'identité numérique</strong>: carte d'identité électronique, permis de conduire électronique, code santé...
10. <strong>Centre de divertissement</strong>: musique, vidéo, livres électroniques, podcasts...

Réfléchissez-y : un si petit appareil, combien il porte de votre vie ! Donc, apprendre à bien l'utiliser, c'est apprendre à mieux vivre.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Passons à la pratique : connaître la configuration matérielle

{class="mt-1"}
Dans [Réglages], voyez si vous pouvez trouver le modèle de processeur, la taille spécifique de la RAM et du stockage (ROM). Ayez une idée des capacités de votre smartphone. Les utilisateurs Android peuvent télécharger « AnTuTu » ou « DevCheck » pour voir les informations matérielles détaillées.
:::
