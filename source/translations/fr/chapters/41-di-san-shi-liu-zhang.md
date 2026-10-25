---
id: di-san-shi-liu-zhang
num: 36
part: er-tong-pian
nav: Chapitre 36 : Téléphone et maison connectée — rendre la maison intelligente
toc: default
kind: chapter
---

### Chapitre 36 : Téléphone et maison intelligente — une maison qui pense

{class="chapter-intro mb-4"}
Le téléphone assume une tâche de plus en plus importante : devenir la « télécommande » de toute la maison. D'une simple ampoule ou prise à la serrure de porte, la maison intelligente passe du « jouet de geek » au confort quotidien. Ce chapitre clarifie protocoles, écosystèmes, hub et kit de démarrage, puis se termine par une liste de sécurité pour que le « smart » ne se retourne pas contre vous.

#### I. Protocoles de maison intelligente : bien choisir

Avant d'acheter un objet connecté, vérifiez son protocole : c'est lui qui détermine s'il répondra à votre téléphone et à votre écosystème. Quatre protocoles dominent, chacun avec son tempérament :

- Protocole Matter : publié en 2022 par la CSA (Connectivity Standards Alliance), porté par Apple, Google, Amazon, Samsung et d'autres. Objectif unique : faire parler tous les appareils de toutes les marques la même langue. Il devient rapidement le standard unifié et permet à un appareil compatible de rejoindre Apple HomeKit, Google Home, Amazon Alexa et Mi Home, sans être prisonnier d'un seul écosystème.
- Protocole Thread : le « tuyau » réseau de Matter. Faible consommation, maillage auto-organisé (si un nœud tombe, le signal contourne), réactif et stable. Les appareils avec routeur de bordure Thread (HomePod mini, Apple TV 4K, hub Xiaomi) offrent une expérience nettement plus fiable.
- Wi-Fi : grande bande passante, connexion directe au routeur, mais consommation élevée et canaux encombrés avec beaucoup d'appareils ; idéal pour caméras et robots aspirateurs qui transfèrent beaucoup de données.
- Bluetooth (BLE) : appairage simple, économe, mais portée courte et pas de maillage ; parfait pour serrures et capteurs de température/humidité.
- Zigbee : protocole ancien à faible consommation, nécessite une passerelle dédiée ; appareils bon marché et stables, mais interopérabilité limitée ; progressivement remplacé par Matter + Thread.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
En une phrase

{class="mt-1"}
En 2026, pour un nouvel appareil, privilégiez la mention « Matter over Thread » — le choix le plus durable. Un ancien appareil Wi-Fi ou Bluetooth peut rester en service ; pour les prochains achats, orientez-vous vers Matter.
:::

#### II. Comparatif des trois écosystèmes

Le protocole est la « langue », l'écosystème est le « cercle ». Même avec Matter, vous choisirez un écosystème principal pour l'automatisation et le contrôle vocal. Comparaison des trois grands :

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                    <thead>
                        <tr class="bg-light dark:bg-gray-700">
                            <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Écosystème</th>
                            <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Atouts</th>
                            <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Limites</th>
                            <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Public</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple HomeKit</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Confidentialité maximale (traitement local), intégration fluide iPhone/Siri/Raccourcis</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Appareils plus rares et plus chers, hub HomePod ou Apple TV requis</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Familles tout Apple, attentives à la vie privée et à l'expérience</td>
                        </tr>
                        <tr>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mi Home (Xiaomi)</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Le plus large catalogue, excellent rapport qualité-prix, assistant Xiao Ai agréable</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Écosystème relativement fermé, données souvent dans le cloud, publicités plus nombreuses</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Budget limité, volonté d'équiper toute la maison en une fois</td>
                        </tr>
                        <tr>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Huawei HiLink (HarmonyOS)</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Continuité fluide téléphone/tablette/montre HarmonyOS, catalogue en croissance rapide</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Moins d'appareils à l'étranger, écosystème qui rattrape son retard</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Utilisateurs de téléphones Huawei, partisans du « Super Device » multi-appareils</td>
                        </tr>
                    </tbody>
                </table>
```

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
Conseils de choix d'écosystème

{class="mt-1"}
Choisissez selon votre téléphone : iPhone → HomeKit en priorité ; Huawei → HiLink ; autres Android → Mi Home, le plus simple. Grâce à Matter, des appareils d'écosystèmes différents restent contrôlables depuis le même téléphone — inutile de choisir un camp tout de suite.
:::

#### III. Le téléphone comme hub de la maison

Dans la plupart des usages débutants, le téléphone est votre « hub » : via une application, il pilote lumières, climatisation, stores, sécurité, et crée des scénarios qui font vivre la maison :

- Contrôle des appareils : HomeKit/Mi Home/HiLink pour allumer ou éteindre à distance, régler la température de couleur, la clim, ouvrir/fermer les stores, voir les caméras.
- Scénarios d'automatisation : combinaisons « condition → action », trois cas courants : Mode « À la maison » : géolocalisation à domicile + nuit → allumer l'entrée, clim, fermer stores, verrouiller la porte.
- Mode « Absent » : le dernier à sortir (localisation hors domicile ou porte verrouillée) → éteindre lumières, clim, prises ; activer caméras et alarme.
- Mode « Nuit » : chaque soir à 23 h → éteindre les lumières principales, fermer les stores, clim à 26 °C, allumer la veilleuse.

- NFC « tap » : collez une étiquette NFC près de la porte ; un contact déclenche le scénario (allumer l'entrée, puis basculer en mode nuit). Sur iPhone, via les Raccourcis ; sur Android, via le Portefeuille ou l'application de la marque.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Essayez : créez un mode « À la maison »

{class="mt-1"}
Dans « Automatisation » de l'application maison intelligente, ajoutez : déclencheur « Arrivée à un lieu » (domicile), actions « allumer l'entrée », « clim 26 °C », « fermer les stores ». Sortez, rentrez, et regardez les lumières s'allumer seules — la première réussite est plus satisfaisante qu'une nouvelle commande.
:::

#### IV. Kit de démarrage recommandé

Inutile de tout acheter d'un coup : ces quatre appareils couvrent déjà 80 % des besoins quotidiens :

- Enceinte connectée : Xiao Ai (Mi Home, bon rapport qualité-prix) / HomePod mini (Apple, hub Thread) / Alexa (large écosystème international). Attention : l'enceinte fixe l'écosystème vocal — choisissez d'abord l'écosystème.
- Ampoule connectée : Yeelight (Mi Home/Matter, température et luminosité réglables, abordable) / Philips Hue (belles couleurs, stable, mais passerelle Hue et prix plus élevé). Vérifiez le culot (E27/B22) et le besoin de couleur.
- Prise connectée : Xiaomi Smart Plug (abordable, mesure de consommation) / TP-Link Kasa (bonne compatibilité Matter à l'international). Pour les appareils puissants (chauffe-eau, radiateur), vérifiez la puissance admissible et évitez les surcharges.
- Serrure connectée : Lockin/Xiaomi (rapport qualité-prix, Mi Home) / Kaadas (fabricant traditionnel, mécanique robuste). Vérifiez la compatibilité Matter ou votre écosystème, l'autonomie de la batterie et l'emplacement de la serrure de secours.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
Ordre d'achat conseillé

{class="mt-1"}
Enceinte d'abord (choix de l'écosystème) → ampoules et prises (simple, retour immédiat) → serrure et caméra (sécurité, à choisir soigneusement). Ajoutez une catégorie à la fois, puis élargissez, pour éviter les achats inexploités.
:::

#### V. Précautions de sécurité

Plus il y a d'objets connectés, plus la surface d'attaque est large. Quatre règles non négociables :

1. Changez les mots de passe par défaut : caméras, routeurs, serrures — leurs identifiants d'usine sont publics en ligne. Premier réflexe : un mot de passe long et unique.
2. Mettez à jour le firmware : les mises à jour corrigent souvent des failles ; activez « Mise à jour automatique » ou vérifiez au moins une fois par mois.
3. Isolez le réseau : placez les objets IoT sur un Wi-Fi dédié (ou réseau invités), séparé de téléphone et ordinateur. Un appareil compromis menacera moins vos données sensibles.
4. Vie privée : activez les « zones privées » des caméras (ne pas filmer chambre ou salle de bains), désactivez l'enregistrement cloud 24 h/24 ; ne laissez pas le flux d'une caméra ouvert en permanence à des applications tierces.

::: div .danger-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
Pièges à éviter

{class="list-disc pl-6 mt-1 space-y-1"}
- N'utilisez pas le « déverrouillage à distance » pour un inconnu — préférez un code temporaire qui expire après usage.
- Ne pointez pas la caméra vers le lit ou la fenêtre — vous exposez votre propre intimité.
- Évitez les appareils « blancs » sans marque — souvent sans mises à jour, une vraie porte dérobée chez vous.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Résumé du chapitre

{class="list-disc pl-5 text-sm space-y-0.5"}
- Matter + Thread est la direction unifiée 2023-2026 : vérifiez cette mention pour tout nouvel achat
- Trois écosystèmes, trois forces : Apple pour la vie privée et l'expérience, Mi Home pour le prix, Huawei pour la synergie multi-appareils
- Le téléphone peut servir de hub : configurez « à la maison / absent / nuit » et la maison vit seule
- Kit de démarrage : enceinte, ampoule, prise, serrure — dans cet ordre
- Mots de passe par défaut, firmware, isolation réseau, confidentialité — quatre lignes rouges à ne pas négliger
:::
