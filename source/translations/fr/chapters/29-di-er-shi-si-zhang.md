---
id: di-er-shi-si-zhang
num: 24
part: chao-yue-pian
nav: Chapitre 24 : Analyse approfondie des droits root et du verrou BL
toc: default
kind: chapter
---

### Chapitre 24 : Analyse approfondie des permissions Root et du verrou Bootloader

{class="chapter-intro mb-4"}
Ce chapitre approfondit le contenu du chapitre 20, pour ceux qui veulent vraiment comprendre les mécanismes bas niveau du smartphone, voire tenter le flashage. Attention, ces opérations comportent des risques, procédez avec prudence.

#### I. Comprendre en profondeur le Bootloader

Le Bootloader est le premier programme exécuté au démarrage du smartphone, sa tâche est d'initialiser le matériel et de charger le noyau du système d'exploitation. On peut le comprendre comme le « gardien » du smartphone.

##### Principe de fonctionnement du verrou BL :

- <strong>Vérification de signature</strong>:Le verrou BL vérifie la signature numérique de l'image de démarrage, seuls les systèmes signés par le fabricant peuvent démarrer.
- <strong>Prévention du retour en arrière</strong>:Empêche les utilisateurs de flasher une ancienne version du système pour exploiter des vulnérabilités connues.
- <strong>Protection des données</strong>:Même si un nouveau système est flashé, sans le compte et mot de passe originaux, les données utilisateur restent inaccessibles.

##### 🔐 Stockage et vérification au niveau matériel

L'état de verrouillage du BL (Locked/Unlocked) et la clé publique du fabricant sont généralement stockés dans une zone matérielle protégée (telle que la partition devinfo de Qualcomm, eFuse ou la partition RPMB), pour empêcher toute modification logicielle. À chaque démarrage, le bootloader lit l'état depuis cette zone sécurisée et décide en conséquence d'exécuter ou non une vérification de signature stricte.

##### 🔏 Vérification de signature numérique

Lors de la publication d'une mise à jour système ou d'une image, le fabricant la signe avec sa clé privée. Au démarrage de l'appareil, le bootloader vérifie l'image système (par exemple boot.img, recovery.img) avec la clé publique intégrée. Son fonctionnement est le suivant :

1. Recalcul de la valeur de hachage de l'image système.
2. Déchiffrement de la signature intégrée à l'image avec la clé publique pour obtenir une valeur de hachage.
3. Comparaison des deux valeurs de hachage, si elles correspondent, la vérification est réussie. Cela garantit que l'image système n'a pas été modifiée par un tiers.

##### 🔗 Chaîne de démarrage sécurisé

Le verrouillage BL est le premier maillon de toute la chaîne de démarrage sécurisé. Une fois la vérification réussie, il charge et exécute le programme de démarrage suivant (par exemple le noyau), garantissant ainsi de proche en proche la fiabilité de l'environnement de démarrage du système.

##### 📊 Verrouillé vs déverrouillé : l'impact à double tranchant du BL

Pour mieux comprendre les avantages et les inconvénients du verrouillage BL, nous utilisons un tableau comparatif pour montrer les différences sur 5 dimensions clés :

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 dark:border-gray-600 text-sm">
                            <thead>
                                <tr class="bg-gray-100 dark:bg-gray-800">
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Rôle principal</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">État verrouillé (par défaut)</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">État après déverrouillage</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Sécurité du système</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Empêche le flash de systèmes non officiels non signés, protège l'intégrité du système et la sécurité de bas niveau<br><span class="text-emerald-600 dark:text-emerald-400">✅ Sécurité élevée : charge uniquement les images signées officielles, protège efficacement contre la modification malveillante du firmware</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ Sécurité réduite : permet de flasher des ROM tierces, le mécanisme de vérification d'intégrité du système est désactivé, un logiciel malveillant obtenant les permissions Root peut modifier le système en profondeur</span></td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Stabilité du système</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Garantit que le smartphone exécute le système officiel testé et optimisé par le fabricant, assurant stabilité et fluidité<br><span class="text-emerald-600 dark:text-emerald-400">✅ Stable : utilise le firmware officiel, fonctionnalités complètes, mises à jour OTA fiables</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ Risque accru : les ROM tierces peuvent présenter des problèmes de compatibilité, pouvant provoquer des crashs système, un brickage, des dysfonctionnements matériels (par exemple caméra, charge rapide), et des échecs de mise à jour OTA</span></td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Droits de garantie</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Le fabricant verrouille le BL pour fournir un système officiel stable, afin d'offrir le service de garantie<br><span class="text-emerald-600 dark:text-emerald-400">✅ Garantie valide : bénéficie du service de garantie gratuit officiel (hors dommages intentionnels)</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ Garantie invalide : la grande majorité des fabricants considèrent le déverrouillage du BL comme une renonciation volontaire à la garantie, même en cas de reverrouillage, l'historique de déverrouillage peut être détecté et la garantie refusée</span></td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Sécurité des données</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Le processus de déverrouillage efface généralement les données de force, pour empêcher que les anciennes données soient exploitées malveillamment dans le nouvel environnement système<br><span class="text-emerald-600 dark:text-emerald-400">✅ Données sécurisées : en usage quotidien, le verrouillage BL limite la capacité des programmes malveillants à modifier la partition système</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ Risque pour les données : le déverrouillage efforce l'effacement de toutes les données utilisateur ; si le chiffrement n'est pas correctement configuré après le déverrouillage, le stockage des données peut être non sécurisé ; en cas de perte, les données sont plus facilement extractibles par flash</span></td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Restrictions fonctionnelles</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Garantit le fonctionnement normal des fonctions dépendant d'un environnement sécurisé (par exemple paiement, applications bancaires)<br><span class="text-emerald-600 dark:text-emerald-400">✅ Fonctions complètes : toutes les fonctions officielles peuvent être utilisées normalement</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ Fonctions limitées : certaines applications sensibles à la sécurité (par exemple Google Pay, applications bancaires) peuvent refuser de fonctionner en détectant l'état de déverrouillage du BL ; les services DRM peuvent être dégradés, affectant la lecture vidéo HD</span></td>
                                </tr>
                            </tbody>
                        </table>
```
:::

#### II. Procédure détaillée de déverrouillage du BL (exemple Xiaomi)

1. <strong>Demander la permission de déverrouillage</strong>:Demandez le déverrouillage sur le site de l'outil de déverrouillage Xiaomi.
2. <strong>Lier le compte</strong>:Liez votre compte Xiaomi dans les paramètres du smartphone.
3. <strong>Période d'attente</strong>:Selon le niveau du compte, une attente de 7 à 30 jours est requise.
4. <strong>Opération de déverrouillage</strong>:Utilisez l'outil de déverrouillage Xiaomi en connectant à l'ordinateur.

#### III. Les multiples solutions de Root

- <strong>Magisk</strong>:Solution de Root moderne, conception Systemless, permet de masquer l'état Root.
- <strong>Kernelsu</strong>:Solution de Root basée sur le noyau, plus bas niveau, meilleure dissimulation.
- <strong>SuperSU</strong>:Solution de Root classique, actuellement plus maintenue.

#### IV. Introduction au flashage

Le flashage consiste à installer un nouveau système d'exploitation sur le smartphone. Types de flashage courants :

- <strong>Flasher une ROM officielle</strong>:Installer un système officiel, pour débricker ou rétrograder.
- <strong>Flasher un Recovery tiers</strong>:Comme TWRP, pour la sauvegarde/restauration et le flashage de ROMs tierces.
- <strong>Flasher une ROM tierce</strong>:Comme LineageOS, Pixel Experience, etc., pour découvrir d'autres systèmes.

#### V. Samsung Knox : le coût irréversible du déverrouillage du BL

Contrairement aux autres fabricants Android, le mécanisme de déverrouillage du BL des smartphones Samsung possède une conception unique de « fusion » :<strong>Pour les smartphones Samsung, le déverrouillage déclenche la fusion Knox, entraînant la perte permanente de certaines fonctions de sécurité (telles que Samsung Pay) ; toutes les données protégées sont effacées ; la garantie est affectée</strong>. Plus précisément :

- <strong>Le fusible est à usage unique</strong> : Le smartphone contient un fusible eFuse qui, une fois qu'il détecte que le BL a été déverrouillé, grille définitivement et ne peut pas être restauré.
- <strong>Fonctions affectées</strong> : Samsung Pay (carte de transport/carte bancaire), le dossier sécurisé Knox, le contrôle MDM d'entreprise, et certaines applications d'assurance santé deviennent inutilisables.
- <strong>Effacement forcé des données</strong> : Une fois la fusion déclenchée, le smartphone force une réinitialisation d'usine, toutes les données locales sont effacées (les données cloud ne sont pas affectées).
- <strong>Impact sur la garantie</strong> : Le fabricant déclare explicitement qu'après la fusion Knox, le service de garantie n'est plus disponible.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Réfléchissez à deux fois avant d'agir

{class="mt-1"}
La fusion Knox de Samsung est <strong>irréversible</strong>, une fois déclenchée, il est impossible de revenir à l'état d'usine. Si vous souhaitez simplement utiliser certaines fonctions nécessitant normalement le Root, il est recommandé de vérifier d'abord s'il existe des alternatives ne nécessitant pas de Root.
:::

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-skull-crossbones mr-2"></i>Avertissement important

{class="mt-1"}
Le flashage comporte des risques, procédez avec prudence. Cela peut entraîner :

{class="list-disc pl-6 mt-1 space-y-1"}
- Smartphone brické (impossible de démarrer)
- Perte de la garantie
- Perte de données
- Dysfonctionnement des services de paiement

{class="mt-1"}
Avant le flashage, faites impérativement une sauvegarde complète, lisez attentivement le tutoriel, et vérifiez la compatibilité du modèle et de la version.
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Ressources recommandées

{class="list-disc pl-6 mt-1 space-y-1"}
- <strong>XDA Developers</strong>:La plus grande communauté de développeurs Android au monde, riche en tutoriels de flashage et ressources de ROM.
- <strong>Coolapk</strong>:Communauté numérique bien connue en Chine, avec de nombreux tutoriels et discussions en chinois.
- <strong>Forums par modèle</strong>:Comme la communauté Xiaomi, la communauté OnePlus, etc., avec des tutoriels officiels et communautaires.
:::

#### VI. Foire aux questions (FAQ)

::: div .qa-item .mt-3
{class="font-semibold mb-1"}
<i class="fas fa-question-circle text-primary mr-1"></i>Q1 : Peut-on revenir en arrière après avoir déverrouillé le BL ?

{class="mb-2 pl-6"}
<strong>A:</strong> Oui, il est possible de reverrouiller. Il faut généralement flasher le package complet de flash filaire officiel et utiliser un script de flash spécifique (par exemple, celui de Xiaomi <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">flash_all_lock.bat</code>) pour reverrouiller. Mais notez que même après reverrouillage, certaines sécurités déclenchées par le déverrouillage (telles que le Knox de Samsung) peuvent être irréversibles.
:::

::: div .qa-item .mt-3
{class="font-semibold mb-1"}
<i class="fas fa-question-circle text-primary mr-1"></i>Q2 : Comment rooter après le déverrouillage ?

{class="mb-2 pl-6"}
<strong>A:</strong> Le déverrouillage du BL n'est que la première étape. Le Root nécessite généralement :

{class="list-decimal pl-12 mb-2 space-y-1"}
1. Flasher un Recovery personnalisé (tel que TWRP).
2. Flasher un gestionnaire de Root tel que Magisk via le Recovery pour patcher l'image boot et obtenir les permissions Root.
:::
