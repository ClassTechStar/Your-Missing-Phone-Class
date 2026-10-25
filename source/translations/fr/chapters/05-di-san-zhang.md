---
id: di-san-zhang
num: 03
part: ji-chu-pian
nav: Chapitre 3 : Brancher le téléphone à sa « ligne de vie »
toc: default
kind: chapter
---

### Chapitre 3 : Branchez votre smartphone à la « ligne de vie » — le réseau

{class="chapter-intro mb-4"}
Sans réseau, le smartphone perd la moitié de son intelligence. Le réseau est la ligne de vie du smartphone moderne ; le comprendre, bien l'utiliser, le protéger, est un cours obligatoire pour chaque utilisateur.

#### 0. Ne vous perdez plus en vous connectant — distinguez la « route » et les « voitures » du Wi-Fi et des données

Beaucoup de gens ont les icônes Wi-Fi et signal allumées simultanément en haut de l'écran, mais ne comprennent pas la différence essentielle. L'erreur classique est :<strong>connecté au Wi-Fi mais impossible de charger une page</strong>— parce que le routeur a perdu la connexion Internet, et le smartphone n'est pas automatiquement revenu aux données mobiles. Pour bien comprendre ce problème, nous devons construire un modèle cognitif « route et voitures ».

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-road mr-2"></i>Métaphore centrale : route et voitures

{class="mt-1"}
Imaginez Internet comme une ville. La <strong>« route »</strong> est le chemin entre votre smartphone et Internet, les <strong>« voitures »</strong> sont les données qui roulent sur la route. Le Wi-Fi et les données mobiles sont deux routes différentes, mais les données (voitures) sont les mêmes.
:::

{class="font-semibold mt-4 mb-1"}
##### 1. Différence essentielle : canal local vs autoroute distante

Le Wi-Fi est essentiellement une <strong>technologie de réseau local</strong>, comme une route posée sans fil sous votre immeuble, qui achemine les données du routeur vers le smartphone. Mais si la box n'est plus abonnée ou que le câble optique est coupé, la route existe toujours, mais l'« autoroute » vers l'extérieur est coupée, naturellement vous ne pouvez aller nulle part. Les données mobiles, en revanche, transitent par les stations de base 4G/5G de l'opérateur, comme si vous empruntiez directement l'autoroute de l'opérateur, tant qu'il y a du signal, vous vous connectez directement à Internet.

{class="font-semibold mt-4 mb-1"}
##### 2. Coût et scénarios : forfait mensuel fixe vs facturation à la consommation

Le Wi-Fi est généralement un investissement unique (forfait mensuel de la box), tant qu'il y a de l'électricité, toute la famille l'utilise sans limite, très adapté aux scénarios gourmands en données tels que le téléchargement de films ou les jeux. Les données mobiles, en revanche, sont facturées à la consommation, au-delà du forfait il peut y avoir bridage ou facturation supplémentaire, plus adaptées aux tâches légères en mobilité (métro, déplacements).

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-hands-helping mr-2"></i>Essayez : vérifiez votre forfait de données

{class="mt-1"}
Ouvrez [Réglages] &gt; [Réseau mobile] &gt; [Gestion des données] sur votre smartphone, regardez combien de données il vous reste ce mois-ci et quelles apps consomment le plus. Savoir où l'on en est permet de sortir serein.
:::

{class="font-semibold mt-4 mb-1"}
##### 3. Considérations de sécurité : le Wi-Fi public est un « terrain de pêche » discret

En matière de sécurité, les données mobiles sont généralement plus sûres que le Wi-Fi public. Les données mobiles sont chiffrées par l'opérateur, tandis que le Wi-Fi public peut effectivement être configuré en « faux point d'accès » par un hacker pour intercepter le trafic non chiffré. Mais distinguons : à l'ère de la généralisation du HTTPS, ce que l'attaquant peut intercepter, c'est <strong>les sites que vous visitez</strong>(domaine), et <strong>le contenu HTTP non chiffré</strong>; les messages WeChat, les mots de passe de connexion des apps bancaires et autres données chiffrées par HTTPS, l'attaquant <strong>ne peut pas les lire directement</strong>— sauf à mener une attaque plus complexe de type SSL stripping et que l'utilisateur ignore les avertissements de certificat. Cela dit, pour les paiements à l'extérieur, utiliser directement les données mobiles reste le choix le plus sûr.

::: div .danger-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-circle mr-2"></i>Rappel de sécurité

{class="mt-1"}
Dans les lieux publics tels que aéroports, centres commerciaux, cafés, ne vous connectez pas aux Wi-Fi gratuits au nom suspect (ex. « Free_WiFi_2024 »). Même si vous êtes connecté, ne vous y connectez jamais à une app bancaire et n'y saisissez jamais de mot de passe.
:::

{class="font-semibold mt-4 mb-1"}
##### 4. Côté smartphone : déchiffrez le « langage codé » de la barre d'état

Comment savoir ce que le smartphone utilise pour se connecter ? Sur Huawei, par exemple, l'icône <strong>à double flèche</strong> à côté du signal opérateur ou du signal WLAN dans la barre d'état indique que vous utilisez le mode correspondant pour Internet ; si les deux sont allumées, l'accélération réseau est active, le smartphone utilise simultanément les deux canaux.

Pour les utilisateurs iPhone, c'est plus intuitif : l'icône Wi-Fi allumée signifie Wi-Fi, éteinte, regardez les barres de signal en haut à droite pour savoir que vous utilisez les données. Certains smartphones Android affichent aussi « 5G » ou « 4G » dans la barre d'état, pour vous indiquer directement le type de réseau mobile actuel.

{class="text-lg font-semibold mt-6 mb-2"}
#### I. Réseau mobile (4G/5G) et données mobiles

Le réseau mobile est la base de votre connexion partout. De la 2G à la 5G, la vitesse a été multipliée par mille, mais le principe est à peu près le même.

##### Normes réseau :

- <strong>4G LTE</strong>: couverture la plus large actuellement, vitesse suffisante (théoriquement 100 Mbps+), consommation relativement faible.
- <strong>5G</strong>: vitesse élevée (théoriquement jusqu'à 10 Gbps), mais la couverture est encore en cours d'amélioration, consommation élevée. Adaptée au téléchargement de gros fichiers et à la vidéo haute définition.
- <strong>5G SA vs NSA</strong>: SA est un réseau autonome, NSA s'appuie sur les stations de base 4G. SA offre une meilleure expérience, mais nécessite que l'opérateur et le smartphone le prennent en charge.

##### Gestion des données :

- <strong>Qu'est-ce que les données</strong>: c'est le volume de données généré par la connexion Internet du smartphone. Regarder des vidéos, scroller des images consomme le plus de données, le texte et la voix en consomment peu.
- <strong>Astuce d'économie</strong>: activez le « mode économie de données » dans les réglages, et mettez à jour les apps ou regardez des vidéos HD sous Wi-Fi.
- <strong>Barres de signal ≠ vitesse</strong>: un signal fort signifie seulement une bonne connexion, la vitesse dépend aussi de la charge de la station de base et de votre distance à celle-ci.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-circle mr-2"></i>Avertissement important : désactivez [Itinérance de données] avant de partir à l'étranger !

{class="mt-1"}
Utiliser les données mobiles à l'étranger peut générer des factures astronomiques ! Avant de partir à l'étranger, désactivez absolument l'itinérance de données dans les réglages, ou achetez à l'avance une carte SIM locale / un forfait d'itinérance internationale.
:::

#### II. Wi-Fi : connexion, partage et sécurité

Le Wi-Fi est le principal mode de connexion à domicile et au bureau, rapide, sans consommation de données. Mais le Wi-Fi évolue aussi, les différences entre normes sont grandes.

##### Se connecter au Wi-Fi :

Allez dans [Réglages] &gt; [WLAN], choisissez le réseau et saisissez le mot de passe. Beaucoup de smartphones prennent désormais en charge la connexion par QR code, plus pratique.

##### Partager le mot de passe :

Android et iOS permettent tous les deux de partager rapidement le mot de passe Wi-Fi avec un ami. Android génère un QR code, iOS peut partager automatiquement en rapprochant les appareils.

##### Évolution des normes Wi-Fi :

Les normes Wi-Fi sont définies par l'IEEE, chaque génération apportant des améliorations significatives :

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                            <thead>
                                <tr class="bg-light dark:bg-gray-700">
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Norme</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Protocole</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Bande de fréquence</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Débit maximum</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Caractéristiques</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Wi-Fi 4</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">802.11n</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2,4/5 GHz</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">600 Mbps</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ancienne norme, couverture correcte</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Wi-Fi 5</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">802.11ac</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">5 GHz</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3,5 Gbps</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">La plus répandue actuellement, débit suffisant</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Wi-Fi 6</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">802.11ax</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2,4/5 GHz</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">9,6 Gbps</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Performances multi-appareils, faible latence</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Wi-Fi 6E</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">802.11ax</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2,4/5/6 GHz</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">9,6 Gbps</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ajout de la bande 6 GHz, moins de congestion</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Wi-Fi 7</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">802.11be</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2,4/5/6 GHz</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">46 Gbps</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Transmission ultra-rapide, agrégation multi-lien</td>
                                </tr>
                            </tbody>
                        </table>
```
:::

- <strong>Technologies clés du Wi-Fi 6</strong>: OFDMA (Accès multiple par répartition orthogonale en fréquence) permet à plusieurs appareils de transmettre simultanément, MU-MIMO (Multiple-Input Multiple-Output multi-utilisateur) améliore l'efficacité multi-appareils, TWT (Target Wake Time) permet aux appareils d'économiser la batterie.
- <strong>Wi-Fi 6E</strong>: Ajoute la bande 6 GHz au Wi-Fi 6, offrant davantage de canaux et réduisant les interférences. Nécessite que le smartphone et le routeur soient tous deux compatibles.
- <strong>Wi-Fi 7</strong> : Introduit le MLO (Multi-Link Operation), permettant d'utiliser simultanément plusieurs bandes de fréquences pour la transmission de données, réduisant considérablement la latence. Les canaux ultra-larges de 320 MHz offrent un bond en débit. Les plateformes phares comme Snapdragon 8 Elite Gen5 et Dimensity 9400 prennent déjà en charge le Wi-Fi 7. Les Xiaomi 17, Huawei Mate 80, Samsung S26, etc. peuvent utiliser les réseaux Wi-Fi 7 (nécessite un routeur Wi-Fi 7).
- <strong>2,4 GHz vs 5 GHz</strong>: Le 2,4 GHz traverse mieux les murs mais est plus lent et sujet aux interférences ; le 5 GHz est plus rapide mais traverse moins bien les murs. La bande 6 GHz du Wi-Fi 6E/7 offre la vitesse la plus élevée, mais la pénétration des murs est la plus faible, idéale pour une utilisation dans la même pièce.

##### Risques du Wi-Fi public :

Le Wi-Fi public peut être victime d'écoute piratesque ou de points d'accès de phishing. Règles à suivre :

- Évitez de vous connecter à votre compte bancaire ou de saisir des mots de passe.
- Utilisez idéalement un VPN pour chiffrer la connexion.
- Ne vous connectez pas automatiquement aux Wi-Fi inconnus.
- Utilisez des sites HTTPS (icône de cadenas dans la barre d'adresse).

#### 3. Bluetooth : le joueur polyvalent de la communication sans fil courte distance

Le Bluetooth est probablement l'une des technologies sans fil les plus utilisées sur votre smartphone — écouteurs sans fil, montre connectée, système embarqué, clavier et souris, tous se connectent via lui.

##### Principe technique :

Le Bluetooth fonctionne dans la bande ISM 2,4 GHz, utilisant la technique d'étalement de spectre par saut de fréquence (FHSS) pour répartir les données sur 79 canaux avec commutation rapide, évitant efficacement les interférences. La portée de communication Bluetooth est divisée en trois classes : Classe 1 environ 100 mètres, Classe 2 environ 10 mètres (courante sur les smartphones), Classe 3 environ 1 mètre.

##### Évolution des versions :

- <strong>Bluetooth 4.0</strong>: Introduction du Bluetooth basse consommation (BLE), permettant aux appareils à petite batterie comme les bracelets et les ceintures cardiaques de se connecter sans fil, avec une autonomie passant de jours à des mois.
- <strong>Bluetooth 4.2</strong>: Amélioration de la vitesse de transmission et de la protection de la vie privée, prise en charge de la connexion directe IPv6.
- <strong>Bluetooth 5.0</strong>: Vitesse de transmission doublée (2 Mbps), portée quadruplée (300 mètres théoriques), capacité de diffusion octuplée. Prise en charge du double audio (connexion simultanée de deux casques).
- <strong>Bluetooth 5.1</strong>: Introduction de la fonction de recherche directionnelle (AoA/AoD), précision de localisation allant jusqu'au centimètre.
- <strong>Bluetooth 5.2</strong>: Nouvelle norme LE Audio, prise en charge du codec LC3 (meilleure qualité sonore, consommation réduite), audio multi-flux, audio diffusé.
- <strong>Bluetooth 5.3/5.4</strong>: Optimisation accrue de la consommation et de la stabilité de connexion, amélioration de la diffusion périodique.

<strong>Adoption du LE Audio</strong> : En 2025-2026, LE Audio est entré dans une phase de diffusion rapide. Les nouveaux écouteurs True Wireless des grandes marques (Huawei FreeBuds Pro 5, Xiaomi Buds 6 Pro, Samsung Galaxy Buds3 Pro, etc.) prennent tous en charge LE Audio et le codec LC3, offrant une latence plus faible et une meilleure qualité audio. Pour l'achat de nouveaux écouteurs, privilégiez les produits prenant en charge LE Audio.

##### Scénarios d'application :

- <strong>Transmission audio</strong>: Écouteurs sans fil, audio embarqué. Le LE Audio du Bluetooth 5.2 fait faire un bond qualitatif à la fois en qualité sonore et en latence.
- <strong>Transmission de données</strong>: Transfert de fichiers et photos à courte distance. Bien que moins rapide que le Wi-Fi Direct, il est plus simple à utiliser.
- <strong>Association d'appareils</strong>: Montres connectées, bracelets, claviers, souris, manettes de jeu.
- <strong>Services de localisation</strong>: Les balises Bluetooth (Beacon) pour la navigation intérieure, le suivi d'objets (comme l'Apple AirTag).
- <strong>Maison connectée</strong>: Réseau Bluetooth Mesh pour contrôler les ampoules, serrures, etc.

#### 4. Télécommande infrarouge : le smartphone se transforme en télécommande universelle

La télécommande infrarouge est l'une des plus anciennes technologies de contrôle sans fil, mais elle reste pratique sur les smartphones. Certains smartphones Android (comme certains modèles Xiaomi et Huawei) intègrent un émetteur infrarouge permettant de télécommander les téléviseurs, climatiseurs, décodeurs et autres appareils électroménagers.

##### Principe de fonctionnement :

La télécommande infrarouge émet des signaux pulsés de lumière infrarouge à fréquence spécifique (généralement 38 kHz) via une diode électroluminescente infrarouge. Le récepteur infrarouge de l'appareil décode ces impulsions pour exécuter l'opération correspondante. Différentes marques utilisent différents protocoles de codage, les plus courants étant NEC, RC5, RC6, SONY, etc. L'application infrarouge du smartphone intègre une bibliothèque de codes de chaque marque ; il suffit de sélectionner la marque et le modèle pour trouver la correspondance.

##### Limites :

- <strong>Directionnalité</strong>: L'infrarouge se propage en ligne droite, il faut pointer vers l'appareil, ne traverse pas les murs.
- <strong>Courte portée</strong>: Distance efficace généralement de 5 à 8 mètres.
- <strong>Apple non pris en charge</strong>: L'iPhone n'a pas d'émetteur infrarouge, impossible d'utiliser cette fonction.

#### 5. NFC : la magie du toucher

Le NFC (Near Field Communication, communication en champ proche) est une technologie de communication sans fil à très courte distance (moins de 10 centimètres) à haute fréquence, fonctionnant à 13,56 MHz, avec un débit maximum de 424 Kbps.

##### Principe de communication et modes :

Le NFC est dérivé de la technologie RFID et prend en charge trois modes de fonctionnement :

- <strong>Mode lecture/écriture</strong>: Le smartphone lit les informations d'une étiquette NFC, comme la lecture d'un autocollant NFC pour déclencher une action.
- <strong>Mode point à point</strong>: Deux appareils NFC se transmettent des données, comme Android Beam (abandonné).
- <strong>Mode émulation de carte</strong>: Le smartphone simule une carte à puce, c'est le mode le plus utilisé — carte de transport, carte d'accès, carte bancaire utilisent toutes ce mode.

##### Mécanismes de sécurité :

- <strong>Ultra-courte distance</strong>: La portée de communication de moins de 10 cm constitue en soi une garantie de sécurité physique, l'écoute à distance est quasi impossible.
- <strong>Puce de sécurité</strong>: Le smartphone intègre une puce de sécurité (SE) indépendante ou utilise HCE (Host Card Emulation), les clés de paiement sont stockées dans une zone sécurisée, même si le smartphone est rooté, elles ne peuvent être extraites.
- <strong>Vérification empreinte/visage</strong>: Le paiement nécessite une confirmation biométrique, même en cas de perte du smartphone, il est impossible de frauder.
- <strong>Tokenisation</strong>: Apple Pay, Huawei Pay, etc. ne transmettent pas le vrai numéro de carte, mais utilisent un jeton à usage unique, même intercepté, il ne peut être réutilisé.

##### Applications typiques :

- <strong>Carte de transport/carte d'accès</strong>: Écrire les informations de la carte physique dans le smartphone, il suffit de le passer.
- <strong>Paiement mobile</strong>: Apple Pay, Huawei Pay, etc., lier la carte bancaire au smartphone, payer d'un toucher.
- <strong>Association d'appareils</strong>: Appairage rapide Bluetooth d'un toucher NFC pour écouteurs, enceintes.
- <strong>Authentification d'identité</strong>: Lecture de carte d'identité NFC, vérification de permis de conduire électronique.

#### 6. Point d'accès personnel : transformer le smartphone en routeur Wi-Fi

Quand vous avez beaucoup de données mobiles, vous pouvez activer le point d'accès pour la tablette ou l'ordinateur.

- <strong>Activation</strong>: Paramètres &gt; Point d'accès personnel/Partage de connexion, activez-le.
- <strong>Précautions</strong>: Consomme beaucoup de batterie et de données, pensez à définir un mot de passe complexe et à limiter le nombre d'appareils connectés.
- <strong>Partage USB</strong>: Connectez l'ordinateur avec un câble de données, plus stable et plus rapide que le point d'accès sans fil.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Essayez : configurer et gérer le point d'accès

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Ouvrez [Paramètres], trouvez « Point d'accès personnel » ou « Partage de connexion », activez-le, définissez le nom et le mot de passe.
2. Recherchez et connectez-vous à ce Wi-Fi depuis un autre appareil (par exemple un ordinateur).
3. Sur le smartphone, vérifiez si vous pouvez gérer les appareils connectés ou déconnecter un appareil inconnu.
:::
