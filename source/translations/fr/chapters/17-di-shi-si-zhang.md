---
id: di-shi-si-zhang
num: 14
part: ruan-jian-pian
nav: Chapitre 14 : Dossier spécial gestionnaires de mots de passe
toc: default
kind: chapter
---

### Chapitre 14 : Spécial gestionnaires de mots de passe

{class="chapter-intro mb-4"}
À l'ère numérique, le mot de passe est la clé de votre maison. Mais trop de clés, trop complexes, que faire ? Le gestionnaire de mots de passe est votre « concierge universel des clés ».

#### I. Pourquoi avez-vous besoin d'un gestionnaire de mots de passe ?

Une personne moderne a en moyenne des dizaines, voire des centaines de comptes en ligne. Si vous utilisez le même mot de passe pour chaque compte, dès qu'un site est piraté, tous vos comptes sont en danger. Si vous utilisez un mot de passe complexe différent pour chaque compte, impossible de tous les retenir.

Le gestionnaire de mots de passe résout ce dilemme : vous n'avez qu'à retenir un seul mot de passe maître, il retient tous les autres pour vous.

#### II. Principe de fonctionnement du gestionnaire de mots de passe

1. <strong>Stockage chiffré</strong>: tous les mots de passe sont stockés avec un chiffrement haute intensité, seul vous pouvez les déchiffrer.
2. <strong>Mot de passe maître</strong>: vous définissez un mot de passe maître pour déverrouiller le coffre-fort. Le mot de passe maître lui-même n'est pas stocké sur les serveurs.
3. <strong>Remplissage automatique</strong>: sur les pages de connexion des sites web ou applications, le gestionnaire remplit automatiquement les identifiants.
4. <strong>Génération de mots de passe</strong>: peut générer des mots de passe aléatoires et complexes, améliorant la sécurité.

#### III. Introduction aux principes de chiffrement

Comprendre les principes de chiffrement des gestionnaires de mots de passe vous aide à juger si un prestataire mérite votre confiance. Voici une explication en termes simples de quelques concepts fondamentaux.

##### 1. Chiffrement AES-256

AES (Advanced Encryption Standard) est un algorithme de chiffrement symétrique approuvé par le NIST (National Institute of Standards and Technology), largement utilisé par les banques, l'armée et les gouvernements. « 256 » fait référence à la longueur de clé de 256 bits — il faudrait théoriquement plus que l'âge de l'univers pour le briser par force brute. Les principaux gestionnaires de mots de passe (1Password, Bitwarden, KeePass, etc.) utilisent tous le chiffrement AES-256 pour votre coffre-fort de mots de passe.

##### 2. Architecture zéro connaissance (Zero-Knowledge Architecture)

« Zéro connaissance » ne signifie pas que le prestataire ne stocke rien, mais que <strong>le chiffrement et le déchiffrement sont effectués localement sur votre appareil, le serveur ne stocke que le texte chiffré</strong>. Processus spécifique :

1. Vous saisissez votre mot de passe principal sur le client.
2. Le client dérive la clé de chiffrement à partir du mot de passe principal (cette étape s'effectue sur votre smartphone/ordinateur).
3. Seul le texte chiffré est téléchargé sur le serveur.
4. Lors de la prochaine connexion, le serveur renvoie le texte chiffré et le client le déchiffre à nouveau avec le mot de passe principal.

Point clé :<strong>Le mot de passe principal ne quitte jamais votre appareil</strong>, et n'est pas non plus sur le serveur. Donc même si le prestataire est piraté, le pirate n'obtient qu'un ensemble de textes chiffrés indéchiffrables — à moins qu'il ne devine votre mot de passe principal.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Pourquoi « zéro connaissance » signifie-t-il que le prestataire ne peut pas voir vos mots de passe ?

{class="mt-1"}
Parce que la clé de déchiffrement est dérivée de votre mot de passe principal, et que celui-ci n'existe que dans votre tête et n'est utilisé que sur votre appareil local. Le serveur du prestataire ne contient ni le mot de passe principal ni la clé de déchiffrement, seulement le texte chiffré. C'est pourquoi les prestataires sérieux comme Bitwarden et 1Password déclarent explicitement « nous ne pouvons pas non plus voir vos mots de passe » — ce n'est pas qu'ils ne le veulent pas, c'est techniquement impossible.
:::

##### 3. Fonction de dérivation de clé : PBKDF2 et Argon2

Le mot de passe principal ne peut pas être directement utilisé comme clé de chiffrement — il doit être traité par une « fonction de dérivation de clé ». Le rôle de cette fonction est de <strong>ralentir volontairement le calcul</strong>, afin de rendre le coût d'une attaque par force brute prohibitif.

- <strong>PBKDF2</strong> : Standard établi, largement utilisé par le trousseau iCloud, Bitwarden, LastPass, etc. Ralentit le cassage par itérations hachées répétées (généralement plus de 100 000 fois).
- <strong>Argon2</strong> : Champion du concours de hachage de mots de passe 2015, plus moderne que PBKDF2. Outre la « consommation de calcul », il introduit une « consommation de mémoire » — rendant difficile l'accélération du cassage par du matériel spécialisé comme GPU/ASIC. Bitwarden, KeePassXC, etc. le prennent déjà en charge.

Plus le nombre d'itérations est élevé, plus c'est sécurisé, mais plus le déverrouillage est lent. Les prestataires sérieux publient l'algorithme de dérivation et le nombre d'itérations utilisés, pour permettre l'audit par la communauté de sécurité.

##### 4. Étude de cas : la fuite de données LastPass de 2022

En août 2022, le vétéran des gestionnaires de mots de passe LastPass a annoncé que son environnement de développement avait été compromis ; en novembre de la même année, il a révélé que le pirate avait récupéré les sauvegardes des coffres-forts de mots de passe des utilisateurs (texte chiffré). Leçons clés de l'incident :

- <strong>L'architecture zéro connaissance a tenu la ligne</strong> : Comme le coffre-fort est lui-même chiffré, le pirate a obtenu le texte chiffré mais ne peut pas le déchiffrer — à condition que le mot de passe principal de l'utilisateur soit suffisamment fort.
- <strong>Les utilisateurs avec un mot de passe principal faible sont les plus exposés</strong> : Le pirate peut casser les mots de passe principaux faibles hors ligne par force brute, les utilisateurs avec des mots de passe principaux faibles ou réutilisés courent donc un risque réel.
- <strong>Les métadonnées ont également fuité</strong> : Bien que le contenu des mots de passe soit chiffré, les métadonnées telles que les URL des sites et les notes peuvent ne pas l'être, révélant les services utilisés par l'utilisateur.

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Ce qu'on apprend de l'incident LastPass

{class="mt-1"}
Premièrement, le mot de passe principal doit être long et unique (16 caractères minimum, avec majuscules, minuscules, chiffres et symboles) ; deuxièmement, privilégiez les prestataires prenant en charge Argon2id avec un nombre d'itérations élevé ; troisièmement, pour les comptes à haute valeur (banque, e-mail), activez impérativement une authentification à deux facteurs indépendante, ne vous fiez pas uniquement au gestionnaire de mots de passe.
:::

#### IV. Recommandations de gestionnaires de mots de passe

##### Intégrés au système :

- <strong>Trousseau iCloud</strong>: premier choix pour les utilisateurs de l'écosystème Apple. Intégration transparente avec Safari et les applications, gratuit, sécurisé. L'inconvénient est l'utilisation multiplateforme peu pratique.
- <strong>Gestionnaire de mots de passe Google</strong>: pratique pour les utilisateurs Android. Intégré à Chrome et Android, gratuit.
- <strong>Coffre-fort de mots de passe Huawei</strong>: intégré à HarmonyOS, adapté aux utilisateurs Huawei.

##### Outils professionnels tiers :

- <strong>Bitwarden</strong>: open source et gratuit, puissant, prend en charge toutes les plateformes. Fortement recommandé pour les utilisateurs soucieux de leur vie privée.
- <strong>1Password</strong>: belle interface, riche en fonctionnalités, adapté aux familles et aux équipes. Payant.
- <strong>LastPass</strong>: gestionnaire de mots de passe historique, la version gratuite a des fonctions limitées.
- <strong>KeePass</strong>: stockage entièrement local, open source et gratuit. Adapté aux utilisateurs avertis.

#### V. Évaluation réelle de la force des mots de passe

Les gestionnaires de mots de passe affichent généralement un indicateur de « force du mot de passe » (rouge/jaune/vert), mais cette évaluation ne prend souvent en compte que la longueur et les types de caractères, ce qui n'est pas exhaustif. Pour juger vraiment si un mot de passe est sécurisé, il faut considérer l'« entropie » et « s'il a déjà fuité ».

##### 1. Entropie : la mesure scientifique de la force d'un mot de passe

L'« entropie » mesure l'incertitude d'un mot de passe, l'unité est le bit. Plus l'entropie est élevée, plus le nombre de tentatives nécessaires pour une attaque par force brute est important.

- <strong>"123456"</strong> : Entropie extrêmement faible, cassage instantané.
- <strong>"P@ssw0rd"</strong> : Semble complexe, mais apparaît dans toutes les listes d'attaque par dictionnaire, l'entropie reste faible.
- <strong>"correct horse battery staple"</strong> : Quatre mots aléatoires, entropie d'environ 44 bits, difficulté de cassage bien supérieure à « P@ssw0rd ».
- <strong>16 caractères aléatoires (majuscules + minuscules + chiffres + symboles)</strong> : Entropie d'environ 100 bits, incassable par force brute avec la puissance de calcul actuelle.

Conclusion :<strong>« Longueur + aléatoire » est plus important que « symboles complexes »</strong>. C'est aussi la raison pour laquelle les mots de passe longs et aléatoires générés par les gestionnaires de mots de passe sont vraiment sécurisés.

##### 2. HaveIBeenPwned : vérifiez si votre mot de passe a fuité

Maintenu par le chercheur en sécurité Troy Hunt <a href="https://haveibeenpwned.com" class="text-primary hover:underline" target="_blank" rel="noopener">haveibeenpwned.com</a> recense les comptes et mots de passe ayant fuité lors des principales fuites de données. Vous pouvez :

1. Saisir votre e-mail pour vérifier si votre compte a été exposé lors d'une fuite.
2. Utiliser la fonction Pwned Passwords pour vérifier si un mot de passe figure dans la base des fuites connues (les gestionnaires de mots de passe et les navigateurs intègrent déjà cette vérification).

Si un mot de passe apparaît dans la base des fuites,<strong>quelle que soit sa complexité apparente, il faut le changer immédiatement</strong> — car les attaques par dictionnaire essaient en priorité ces mots de passe connus.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-shield-alt mr-2"></i>Principe de requête k-anonymat

{class="mt-1"}
Inquiet de saisir votre mot de passe sur HaveIBeenPwned et de provoquer une nouvelle fuite ? Pas d'inquiétude. Les requêtes modernes utilisent le protocole « k-anonymat » : le navigateur n'envoie que les 5 premiers caractères du hachis du mot de passe au serveur, qui renvoie la liste de tous les hachis commençant par ces 5 caractères, puis la comparaison se fait localement. Autrement dit, le serveur ne voit jamais le hachis complet de votre mot de passe. La « détection de mots de passe fuités » de 1Password et Bitwarden fonctionne ainsi.
:::

##### 3. Fonctions de surveillance intégrées aux gestionnaires de mots de passe

- <strong>1Password Watchtower</strong> : Surveillance en temps réel des mots de passe faibles, réutilisés, fuités, périmés et des sites sans 2FA, avec un classement rouge/orange/jaune.
- <strong>Bitwarden Vault Health</strong> : La version gratuite permet de voir les mots de passe faibles et réutilisés ; la version payante détecte les mots de passe fuités (basé sur HaveIBeenPwned).
- <strong>« Conseils de sécurité » du trousseau iCloud</strong> : Réglages iOS → Mots de passe → Conseils de sécurité, indique quels mots de passe figurent dans des fuites connues et lesquels sont réutilisés.
- <strong>« Outil de vérification des mots de passe » de Google Password Manager</strong> : Intégré à Chrome, vérifie en un clic les mots de passe fuités, faibles et réutilisés.

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Vérifiez maintenant : vos mots de passe sont-ils sécurisés ?

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Ouvrez haveibeenpwned.com, saisissez votre e-mail habituel et voyez dans quelles fuites il apparaît.
2. Utilisateurs iPhone : Réglages → Mots de passe → Conseils de sécurité, traitez un par un les avertissements rouges.
3. Utilisateurs Chrome : Réglages → Mots de passe → Vérifier les mots de passe, modifiez selon les suggestions.
4. Utilisateurs 1Password/Bitwarden : ouvrez Watchtower/Health Reports, traitez en priorité les éléments « fuités » et « réutilisés ».
:::

#### VI. Passkey : l'avenir de la connexion sans mot de passe

En 2024-2026, la technologie des mots de passe traverse une révolution —<strong>Passkey (clé d'accès)</strong> devrait éliminer complètement les mots de passe traditionnels. Promu conjointement par Apple, Google et Microsoft, avec le soutien de la FIDO Alliance et du W3C, c'est le plus grand changement de méthode de connexion depuis des décennies.

##### 1. Qu'est-ce qu'un Passkey ?

Passkey est basé sur la norme FIDO2 / WebAuthn, utilisant <strong>une paire de clés sur l'appareil</strong> à la place d'un mot de passe. Le principe peut être simplifié ainsi :

- Votre smartphone génère une paire de clés :<strong>Clé publique</strong>(enregistrée auprès du site) + <strong>Clé privée</strong>(stockée pour toujours dans la puce de sécurité de votre appareil).
- Lors de la connexion, le site envoie un « défi », votre smartphone le signe avec la clé privée, puis le site vérifie avec la clé publique.
- Avant la signature, vous devez confirmer votre identité par biométrie (Face ID / empreinte) ou code PIN de l'appareil.
- Pendant tout le processus,<strong>aucun mot de passe n'est transmis sur le réseau</strong>.

##### 2. Passkey vs mot de passe traditionnel

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                        <thead>
                            <tr class="bg-light dark:bg-gray-700">
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Dimension</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Mot de passe traditionnel</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Passkey</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Résistance au hameçonnage</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Faible, les sites d'hameçonnage peuvent voler le mot de passe</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Naturellement résistant, la clé privée ne signe que pour le vrai domaine</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Impact d'une fuite du serveur</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Le hachis du mot de passe peut être cassé</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Le serveur ne stocke que la clé publique, aucune incidence en cas de fuite</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Commodité</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Nécessite mémorisation/saisie/gestion</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Connexion en une seconde avec Face ID/empreinte</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Attaque par rejeu</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Peut être interceptée et rejouée par un homme du milieu</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Chaque signature est à usage unique, impossible à rejouer</td>
                            </tr>
                        </tbody>
                    </table>
```

##### 3. Prise en charge par plateforme

- <strong>Passkey du trousseau iCloud d'Apple</strong> : Pris en charge nativement à partir d'iOS 16+ / macOS Ventura+, les Passkey se synchronisent entre tous les appareils connectés au même Apple ID, pas besoin de recréer sur un nouvel appareil.
- <strong>Passkey de Google Password Manager</strong> : Pris en charge nativement par Android + Chrome, les Passkey sont stockés dans le compte Google et synchronisés entre appareils Android ; depuis 2023, les comptes Google personnels prennent en charge la connexion par Passkey.
- <strong>Microsoft</strong> : Windows 11 / Edge prend déjà en charge Passkey ; les comptes Microsoft, Outlook, Office, etc. ouvrent progressivement la connexion Passkey, gérable dans Microsoft Authenticator.
- <strong>1Password / Bitwarden</strong> : Prend en charge la création, le stockage et la synchronisation multiplateforme des Passkey, pour ne pas être limité à un seul écosystème.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>La synchronisation multi-appareils est une percée clé

{class="mt-1"}
La plus grande difficulté des premiers Passkey était d'être « liés à un seul appareil » — il fallait les recréer en changeant de smartphone. À partir de 2023, Apple, Google et Microsoft ont mis en œuvre la synchronisation cloud des Passkey : le trousseau iCloud synchronise entre appareils Apple, Google Password Manager entre appareils Android. 1Password et d'autres tiers ont ouvert la synchronisation inter-écosystèmes. Cela signifie que Passkey est désormais assez mature pour remplacer les mots de passe.
:::

##### 4. Comment créer et utiliser un Passkey sur smartphone

<strong>Cheminement iOS (iPhone) :</strong>

1. Sur la page de sécurité du compte d'un site prenant en charge Passkey (par exemple Google, Microsoft, Amazon, eBay, PayPal), choisissez « Ajouter une clé d'accès / Add passkey ».
2. Le système affiche la fenêtre de vérification Face ID / Touch ID ; une fois validé, le Passkey est automatiquement généré et enregistré dans le trousseau iCloud.
3. Lors de la prochaine connexion, saisissez votre nom d'utilisateur puis choisissez « Se connecter avec iPhone », un scan Face ID suffit.
4. Entrée de gestion : Réglages → Mots de passe → trouvez le site correspondant, l'entrée Passkey est visible.

<strong>Cheminement Android :</strong>

1. Sur la page de sécurité du compte d'un site prenant en charge Passkey, choisissez « Ajouter une clé d'accès ».
2. Fenêtre Google Password Manager → choisissez votre compte Google → vérification du verrouillage d'écran (empreinte/schéma/PIN).
3. Le Passkey est automatiquement enregistré dans Google Password Manager et synchronisé entre les appareils Android du même compte.
4. Lors de la prochaine connexion, choisissez « Utiliser Passkey », déverrouillez l'écran et c'est fait.
5. Entrée de gestion : Réglages Android → Mots de passe, clés et remplissage automatique → Gestionnaire de mots de passe → google.com.

##### 5. Connexion Passkey multi-appareils

Si vous vous connectez sur un ordinateur Windows à un site pour lequel seul votre iPhone a un Passkey, vous pouvez autoriser par scan de code QR :

1. Sur la page de connexion du site, choisissez « Utiliser Passkey ».
2. Choisissez « Utiliser un autre appareil ».
3. L'ordinateur affiche un code QR, scannez-le avec l'iPhone.
4. L'iPhone affiche la vérification Face ID, après confirmation le site se connecte sur l'ordinateur.

Ce processus utilise une communication doublement chiffrée par Bluetooth + Internet, la clé privée Passkey ne quitte jamais votre iPhone.

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Essayez maintenant : découvrez la connexion sans mot de passe

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Connectez-vous à votre compte Google → Sécurité → Clés d'accès → Ajouter une clé d'accès, découvrez la connexion Face ID/empreinte.
2. Connectez-vous à votre compte Microsoft → Sécurité → Options de sécurité avancées → Ajouter une clé d'accès.
3. Essayez sur Taobao, JD, eBay, PayPal et d'autres services prenant déjà en charge Passkey.
4. Conservez les mots de passe traditionnels comme solution de secours, migrez progressivement les comptes à haute valeur vers Passkey.
:::

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Recommandations pour la période de transition

{class="mt-1"}
Passkey n'a pas complètement remplacé les mots de passe — de nombreux sites sont encore au stade « Passkey + mot de passe » coexistant. Recommandation : activez Passkey en priorité pour les comptes à haute valeur, mais <strong>ne supprimez pas immédiatement les mots de passe traditionnels</strong>, gardez-les comme secours ; continuez à utiliser un gestionnaire de mots de passe, car tous les sites ne prennent pas en charge Passkey. Considérez Passkey comme un « puissant complément au gestionnaire de mots de passe » et non comme un « remplacement immédiat ».
:::

#### VII. Clés de sécurité matérielles

Si vos exigences de sécurité sont supérieures à celles de l'utilisateur ordinaire — par exemple, détention d'une grande quantité de cryptomonnaies, statut de cadre/journaliste/activiste, ou protection de comptes d'entreprise critiques — une clé de sécurité matérielle est un choix plus fiable que le code SMS.

##### 1. Qu'est-ce qu'une clé de sécurité matérielle ?

Une clé matérielle est un dispositif physique (ressemblant à une clé USB), dont la puce de sécurité interne stocke votre clé privée, nécessitant un contact physique ou NFC pour l'authentification. Produits représentatifs :

- <strong>YubiKey</strong>(Yubico) : Le plus répandu, prend en charge FIDO2/WebAuthn, U2F, OTP, PIV, OpenPGP, avec USB-C / USB-A / NFC, etc. Série 5 : 50-70 USD.
- <strong>Google Titan</strong> : Produit par Google, USB-C + NFC / Bluetooth, environ 30-40 USD.
- <strong>OnlyKey</strong> : Alternative open source, prend en charge de multiples protocoles.
- <strong>Alternatives nationales</strong> : Par exemple ePasskey de Feitian, prix plus abordable.

##### 2. Pourquoi les clés matérielles sont-elles plus sûres que les codes SMS ?

- <strong>Résistance au hameçonnage</strong> : Comme Passkey, la clé matérielle ne répond qu'au vrai domaine, les sites d'hameçonnage ne peuvent pas obtenir le code.
- <strong>Résistance au détournement de SIM</strong> : Les codes SMS peuvent être interceptés par une attaque SIM swap, la clé matérielle ne nécessite pas de numéro de téléphone.
- <strong>Résistance à l'homme du milieu</strong> : Le protocole FIDO2 inclut un défi dans chaque signature, impossible à rejouer.
- <strong>Isolation physique</strong> : La clé privée reste toujours dans la puce matérielle, même si un logiciel malveillant compromet votre ordinateur, il ne peut pas la lire.

##### 3. Scénarios d'utilisation

- Comptes d'échanges de cryptomonnaies, récupération de portefeuille.
- SSO d'entreprise, VPN de télétravail, connexion SSH à des serveurs.
- E-mail, GitHub, réseaux sociaux et autres « comptes principaux » — une fois compromis, ils permettent de réinitialiser tous les autres comptes.
- Personnes très sensibles : journalistes, avocats, cadres dirigeants, etc.

##### 4. Comment configurer une clé matérielle pour l'authentification à deux facteurs

Exemple avec un compte Google + YubiKey :

1. Achetez un YubiKey (il est recommandé d'en acheter deux à la fois, un pour un usage quotidien et un de secours, stockés dans des endroits différents).
2. Connectez-vous à myaccount.google.com → Sécurité → Validation en deux étapes.
3. Choisissez « Ajouter une clé de sécurité » → insérez le YubiKey dans le port USB-C ou approchez-le de la zone NFC du smartphone.
4. Suivez les instructions pour toucher le contact métallique du YubiKey et terminer l'enregistrement.
5. Il est recommandé d'enregistrer une deuxième clé de secours.
6. Dans les paramètres de « Validation en deux étapes », définissez la clé matérielle comme méthode de vérification préférée et le code SMS comme secours.

Sites prenant principalement en charge : Google, GitHub, Microsoft, Apple ID, Facebook, Twitter, Dropbox, GitLab, AWS, Coinbase, Binance, etc.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Stratégie à double clé

{class="mt-1"}
Le plus grand risque d'une clé matérielle est la « perte ». Recommandations : ① enregistrez simultanément deux clés différentes ; ② portez-en une sur vous (porte-clés) et stockez l'autre dans un coffre-fort à domicile ou à la banque ; ③ certains sites permettent d'imprimer des « codes de récupération de secours » à conserver hors ligne. Ainsi, même en cas de perte de la clé principale, vous ne serez pas définitivement verrouillé hors de votre compte.
:::

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Prudence sur le canal d'achat

{class="mt-1"}
Achetez impérativement auprès de la boutique officielle ou d'un revendeur autorisé, n'achetez pas de clés d'occasion ou d'origine inconnue — en théorie, du matériel préconfiguré peut avoir été compromis. Le firmware du YubiKey ne peut pas être mis à jour après l'usine, mais Yubico publie continuellement des bulletins de sécurité, suivez son site officiel.
:::

#### VIII. Partage de mots de passe en famille / en équipe

Dans un contexte familial, Netflix, le Wi-Fi familial, l'interface du routeur et le mot de passe de la serrure connectée doivent être partagés par toute la famille ; dans un contexte d'équipe, les serveurs, bases de données et comptes de réseaux sociaux nécessitent une collaboration multi-personnes.<strong>Envoyer des mots de passe par WeChat ou les écrire dans un document partagé sont des pratiques à haut risque</strong> — dès que l'historique des discussions ou les permissions du document fuitent, le mot de passe fuit aussi.

##### 1. « Coffre-fort partagé » (Vault) de 1Password

1Password est le produit de référence pour le partage familial et en équipe. Son mécanisme central est <strong>plusieurs coffres-forts</strong>:

- <strong>Coffre-fort personnel</strong> : Visible uniquement par vous, par exemple les comptes personnels comme la banque et l'e-mail.
- <strong>Coffre-fort partagé</strong> : Visible par tous les membres de la famille ou de l'équipe, par exemple Netflix, le Wi-Fi familial, la carte de crédit partagée.
- <strong>Hiérarchie des permissions</strong> : La version équipe permet de définir certains membres en « consultation seule » ou « consultation sans modification ».

Les membres de la famille ou de l'équipe n'ont pas besoin de partager le mot de passe principal, chacun se connecte avec son propre compte, mais peut voir le contenu du coffre-fort partagé autorisé. Les modifications de mot de passe sont synchronisées en temps réel pour tous les membres.

##### 2. Fonction « Organisation » de Bitwarden

La version gratuite de Bitwarden prend en charge le partage de mots de passe personnels (via la fonction « Send » pour un partage à durée limitée d'un seul mot de passe) ; la version payante permet de créer une « Organisation » pour partager plusieurs entrées avec les membres de la famille ou les collègues, avec des permissions fines. Bitwarden propose également une option d'auto-hébergement, adaptée aux entreprises exigeantes en matière de souveraineté des données.

##### 3. Scénario familial : partage sécurisé des mots de passe Netflix, Wi-Fi, etc.

- <strong>Netflix / sites de streaming</strong> : Stockez le mot de passe de connexion dans le « coffre-fort partagé » de 1Password Families, chaque membre de la famille se connecte individuellement, sans avoir à l'envoyer dans le groupe.
- <strong>Mot de passe Wi-Fi familial</strong> : Entre appareils iOS, le mot de passe Wi-Fi peut être partagé directement via AirDrop aux invités, sans avoir à le dicter ; Android 12+ dispose également de la fonction « Partage Wi-Fi à proximité ».
- <strong>Serrures connectées, électroménager intelligent</strong> : Dans la mesure du possible, utilisez la fonction « membres de la famille » de l'application du fabricant pour créer un compte distinct pour chaque personne, plutôt que de partager un compte administrateur.
- <strong>Interface du routeur domestique</strong> : Stockez le mot de passe administrateur dans le coffre-fort partagé 1Password, et créez un SSID distinct pour le Wi-Fi des invités.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Rapport qualité-prix de 1Password Families

{class="mt-1"}
1Password Families coûte environ 4,99 USD/mois, prend en charge jusqu'à 5 membres de la famille, chacun disposant d'un coffre-fort personnel indépendant + 4 coffres-forts partagés. Cela représente moins de 1 USD/mois par personne, c'est actuellement la meilleure solution de partage familial. La version familiale de Bitwarden à 10 USD/an prend en charge 6 personnes, avec un meilleur rapport qualité-prix, mais une interface légèrement inférieure.
:::

##### 4. Scénario d'équipe : partage des mots de passe serveur/base de données

- <strong>1Password Teams / Business</strong> : Possibilité de créer plusieurs coffres-forts par département ou groupe de projet, contrôle fin des permissions, auditabilité de toutes les actions d'accès.
- <strong>Bitwarden Teams / Enterprise</strong> : Solution open source, auto-hébergeable, la version entreprise prend en charge l'intégration SSO et la synchronisation d'annuaire.
- <strong>Principe de séparation des responsabilités</strong> : Le mot de passe administrateur ne doit pas être détenu par une seule personne — désignez 2-3 « contacts d'urgence » pour garantir la continuité en cas de départ ou de congé du personnel clé.
- <strong>Procédure de départ</strong> : En cas de départ d'un employé, révoquez immédiatement son accès au gestionnaire de mots de passe et, si nécessaire, faites tourner tous les mots de passe hautement sensibles auxquels il a eu accès.

##### 5. Accès d'urgence (Emergency Access) : au cas où il vous arrive quelque chose

Imaginez un scénario : vous gérez seul tous les comptes familiaux importants, mais vous êtes hospitalisé d'urgence ou décédez, et votre famille ne peut pas se connecter aux comptes bancaires, e-mail et d'assurance.<strong>La fonction « Accès d'urgence »</strong> est précisément conçue pour cela — autoriser un membre de la famille ou un ami de confiance à accéder à votre coffre-fort de mots de passe lorsque vous ne pouvez pas répondre.

<strong>Configuration de l'accès d'urgence Bitwarden :</strong>

1. Connectez-vous à Bitwarden Web Vault → Réglages → Accès d'urgence.
2. Ajoutez l'e-mail d'un contact de confiance et invitez-le à accepter.
3. Définissez une « période d'attente » (7-14 jours recommandés) : la fenêtre temporelle entre la demande de l'autre partie et votre confirmation.
4. Si vous ne répondez pas pendant la période d'attente (refus ou inaction), l'autre partie obtient automatiquement l'accès à l'expiration du délai.
5. Vous pouvez à tout moment refuser manuellement la demande ou révoquer l'accès d'urgence.

<strong>Accès d'urgence 1Password :</strong>

1. 1Password ne l'appelle pas directement « accès d'urgence », mais cela peut être réalisé via la fonction « organisation familiale/équipe » — après avoir ajouté les membres de la famille à la version familiale, placez certaines entrées dans le « coffre-fort partagé ».
2. Pour les utilisateurs de la version personnelle, il est recommandé de communiquer le mot de passe principal à un membre de la famille hautement digne de confiance, ou de le consigner dans une enveloppe scellée conservée dans un coffre-fort.
3. 1Password fournit également un « code de récupération », à imprimer et conserver impérativement lors de l'activation de l'authentification à deux facteurs.

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Configurez maintenant : laissez un « double » à votre famille

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Choisissez un membre de la famille de confiance comme « contact d'urgence ».
2. Configurez l'accès d'urgence dans le gestionnaire de mots de passe (Bitwarden) ou ajoutez-le au coffre-fort partagé familial (1Password).
3. Écrivez le mot de passe principal + le code de récupération sur papier, mettez-les dans une enveloppe scellée, conservez-les dans un coffre-fort à domicile ou informez un membre de la famille digne de confiance.
4. Révisez tous les six mois pour confirmer que le contact d'urgence est toujours approprié.
:::

#### IX. Bonnes pratiques d'utilisation du gestionnaire de mots de passe

- <strong>Définir un mot de passe maître fort</strong>: le mot de passe maître est la dernière ligne de défense, définissez un mot de passe long et complexe, et mémorisez-le bien.
- <strong>Activer l'authentification à deux facteurs</strong>: activez l'authentification à deux facteurs pour le compte du gestionnaire, ajoutez une couche de protection.
- <strong>Vérifier régulièrement les mots de passe faibles</strong>: la plupart des gestionnaires ont une fonction « audit de sécurité » qui vous aide à trouver les mots de passe faibles et dupliqués.
- <strong>Ne pas oublier le mot de passe maître</strong>: le mot de passe maître ne peut pas être récupéré, l'oublier signifie perdre tous les mots de passe. Il est recommandé de l'écrire sur papier et de le garder dans un endroit sûr.
- <strong>Accès d'urgence</strong>: définissez un contact d'urgence, au cas où vous ne pourriez plus accéder, une personne de confiance peut récupérer vos mots de passe.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Rappel important

{class="mt-1"}
Le gestionnaire de mots de passe est pratique, mais comporte des risques : si le mot de passe maître fuite, tous les mots de passe sont exposés. Le mot de passe maître ne doit donc jamais être identique aux autres mots de passe, ni écrit dans un endroit facile à trouver. Par ailleurs, il est recommandé de choisir un prestataire avec un bon historique de sécurité.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Essayez maintenant : commencez à utiliser un gestionnaire de mots de passe

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Choisissez un gestionnaire de mots de passe (Bitwarden recommandé ou intégré au système).
2. Créez un compte, définissez un mot de passe maître fort.
3. Importez les mots de passe existants (le cas échéant) ou commencez à ajouter de nouveaux mots de passe.
4. Installez l'extension de navigateur ou l'application mobile, essayez le remplissage automatique.
5. Consultez le rapport d'audit de sécurité, identifiez les mots de passe à améliorer.
:::
