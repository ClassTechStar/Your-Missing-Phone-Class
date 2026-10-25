---
id: di-er-shi-yi-zhang
num: 21
part: chao-yue-pian
nav: Chapitre 21 : Exploration approfondie des réseaux mobiles et de la sécurité de l'information
toc: default
kind: chapter
---

### Chapitre 21 : Exploration approfondie des réseaux mobiles et de la sécurité de l'information

{class="chapter-intro mb-4"}
Nous utilisons tous les jours le smartphone pour naviguer sur Internet, payer, discuter, c'est très pratique. Mais avez-vous déjà pensé à vos historiques de discussion, mots de passe de paiement, photos... combien de fois ces informations « circulent à découvert » sur le réseau ? Honnêtement, la plupart des gens n'y pensent jamais, mais une fois que ça arrive — par exemple un compte piraté, une carte bancaire vidée — il est trop tard pour regretter. Ce chapitre va parler sérieusement de comment rendre votre vie numérique moins « transparente ».

#### I. VPN : la « cape d'invisibilité » du réseau

VPN, abréviation de Virtual Private Network (réseau privé virtuel). Vous pouvez l'imaginer comme un tunnel souterrain dédié et chiffré construit entre votre domicile et le site web que vous voulez visiter. Vous vous déplacez dans le tunnel, les personnes à l'extérieur ne peuvent pas voir ce que vous tenez ni où vous allez.

- <strong>Navigation ordinaire</strong>: votre smartphone → réseau public → site web cible. Les routeurs et commutateurs intermédiaires, n'importe quel maillon peut « espionner » les données que vous envoyez. Surtout sur les WiFi publics des cafés, aéroports, pour être honnête, c'est carrément « à découvert ».
- <strong>Avec VPN</strong>: votre smartphone → tunnel chiffré VPN → serveur VPN → site web cible. Les données sont chiffrées et encapsulées, les « espions » ne voient qu'un tas de caractères incompréhensibles. De plus, le site web cible voit l'adresse IP du serveur VPN, pas votre véritable IP.

Que peut donc faire un VPN ? En résumé : premièrement,<strong>protéger votre vie privée sur les WiFi publics</strong>; deuxièmement,<strong>contourner les restrictions géographiques</strong>(par exemple regarder certains contenus disponibles uniquement dans des pays spécifiques) ; troisièmement,<strong>empêcher votre fournisseur d'accès Internet (FAI) d'enregistrer vos habitudes de navigation</strong>. Mais je dois vous rappeler :<strong>n'utilisez pas de VPN gratuits !</strong> Derrière le gratuit, vos données sont souvent leur « marchandise ». Un ami a utilisé un VPN gratuit, et son smartphone a commencé à afficher des publicités mystérieuses, plus tard il a découvert que ce VPN avait vendu ses données de navigation à des annonceurs. Donc pour choisir un VPN, soit vous choisissez une grande marque payante (comme NordVPN, ExpressVPN), soit vous n'en utilisez pas du tout.

Par ailleurs, le VPN n'est pas omnipotent. Il ne protège que les données « en transit », si le site web cible lui-même n'est pas sûr, ou si votre smartphone est déjà infecté par un logiciel malveillant, le VPN ne peut rien pour vous.

#### II. Le « piège doux » du WiFi public — plus dangereux que vous ne le pensez

Vous pourriez penser, ce n'est qu'un WiFi gratuit, quel risque cela peut-il présenter ? Laissez-moi vous raconter une histoire vraie : des chercheurs en sécurité ont fait une expérience, ils ont installé un point d'accès WiFi appelé « Starbucks_Free » dans un aéroport, en moins d'une heure, plus d'une centaine de personnes s'y sont connectées. En réalité, ce point d'accès était installé par les chercheurs eux-mêmes, tout le <strong>trafic non chiffré</strong> passant par ce point d'accès — par exemple le contenu des pages web HTTP que vous visitez, les communications d'applications sans TLS — ils pouvaient effectivement les intercepter et les consulter.

Mais attention à une condition préalable cruciale : aujourd'hui, WeChat, les applications bancaires, Alipay que vous utilisez quotidiennement sont presque tous passés au chiffrement HTTPS. Autrement dit, même si les attaquants interceptent les paquets de données, ils ne voient qu'un tas de caractères incompréhensibles,<strong>impossibles à lire directement pour vos discussions ou mots de passe de paiement</strong>. Cependant, ils peuvent toujours savoir quels sites vous avez visités (noms de domaine), si certaines vieilles applications ou pages web utilisent encore HTTP en clair, le contenu sera complètement exposé. Cette attaque s'appelle « attaque de l'homme du milieu » (Man-in-the-Middle), le principe est que l'attaquant « s'intercale » entre vous et le véritable routeur WiFi. Plus effrayant encore, le smartphone de beaucoup de gens est réglé sur « connexion automatique aux WiFi connus », l'attaquant n'a qu'à nommer son point d'accès comme un WiFi que vous avez déjà connecté (par exemple « ChinaNet » ou « CMCC »), votre smartphone s'y connectera automatiquement.

Comment s'en protéger ? Quelques conseils pratiques :

- <strong>Repérez le HTTPS</strong>: la barre d'adresse commence par https://, le « s » supplémentaire signifie Secure. Lorsque vous accédez à un site nécessitant un mot de passe, si vous voyez http:// (sans s), arrêtez immédiatement, ne saisissez rien ! Les navigateurs modernes affichent un avertissement « non sécurisé » devant les sites non HTTPS, soyez vigilants en voyant ce marquage.
- <strong>Désactivez la « connexion automatique »</strong>: que ce soit iPhone ou Android, dans les réglages WiFi, désactivez « rejoindre automatiquement » ou « connexion automatique ». Mieux vaut appuyer manuellement à chaque fois que de laisser le téléphone décider.
- <strong>Utilisez les données mobiles pour les opérations sensibles</strong>: virements, connexion bancaire, saisie de numéro de carte d'identité... ces opérations, utilisez fidèlement vos données 4G/5G, n'économisez pas ces quelques mégaoctets.
- <strong>Oubliez les WiFi peu utilisés</strong>: au retour d'un déplacement ou d'un voyage, « oubliez » les WiFi d'hôtel, d'aéroport que vous avez temporairement connectés. Ainsi, la prochaine fois, le téléphone ne se connectera pas automatiquement à un faux point d'accès du même nom.

#### III. Comment le HTTPS vous protège-t-il ? — Handshake SSL/TLS

Je viens de mentionner le HTTPS, mais comment fonctionne-t-il réellement ? Chaque fois que vous accédez à un site HTTPS, le navigateur et le serveur procèdent à un « handshake SSL/TLS », tout le processus ressemble à ceci :

1. Votre navigateur dit : « Hé, serveur, je veux communiquer sécurisement avec toi, voici ma liste de capacités de chiffrement (algorithmes de chiffrement pris en charge, etc.). »
2. Le serveur répond : « D'accord, j'ai choisi cet ensemble de chiffrement dans ta liste, voici mon certificat numérique, qui contient ma clé publique, signé et certifié par telle autorité de certification. »
3. Le navigateur vérifie l'authenticité du certificat : est-il émis par une CA de confiance ? A-t-il expiré ? Le nom de domaine correspond-il ?
4. Après vérification, les deux parties utilisent la clé publique pour chiffrer et convenir d'une « clé de session », toutes les communications ultérieures sont chiffrées avec cette clé.

C'est comme aller à la banque : vous présentez d'abord votre carte d'identité (certificat), le guichetier vérifie votre identité, puis vous convenez d'un mot de code, les conversations suivantes ne sont compréhensibles que par vous deux. Même si quelqu'un écoute, il n'entend que du charabia chiffré.

Mais attention : le HTTPS garantit uniquement que le « processus de transmission » est chiffré, il ne garantit pas que le site cible est bienveillant. Les sites de phishing peuvent aussi utiliser HTTPS — cette petite icône de cadenas indique seulement que vous êtes connecté à « un site », pas que ce site est bien celui que vous voulez visiter. Donc, vérifiez vous-même si l'adresse est correcte.

#### IV. Sécurité DNS : votre « annuaire téléphonique réseau » est-il sûr ?

Le DNS (Domain Name System) est comme l'annuaire téléphonique d'Internet : vous saisissez « baidu.com », le DNS vous aide à trouver à quelle adresse IP il correspond (par exemple 110.242.68.66), puis le navigateur peut s'y connecter. Le problème est que les requêtes DNS traditionnelles sont en <strong>clair</strong>,<strong>non chiffrées</strong>! Autrement dit, votre FAI, votre fournisseur WiFi, ou n'importe quel nœud intermédiaire peut voir quels sites vous avez visités.

Plus détestable encore, le « détournement DNS » : l'attaquant manipule la phase DNS, redirige « baidu.com » vers un faux site de phishing. Vous avez saisi la bonne adresse, mais vous êtes dirigé vers une page de connexion identique mais en réalité fausse, une fois le mot de passe saisi, c'est fini.

Heureusement, il existe maintenant des solutions DNS chiffrées :

- <strong>DNS over HTTPS (DoH)</strong>: cache les requêtes DNS dans le trafic HTTPS, mélangées dans le trafic normal de navigation web, impossible de distinguer quelles sont les requêtes DNS.
- <strong>DNS over TLS (DoT)</strong>: utilise le protocole de chiffrement TLS pour protéger spécifiquement les requêtes DNS, port indépendant, l'administrateur réseau peut savoir que vous utilisez DoT mais ne peut pas voir le contenu.

Personnellement, je recommande d'utiliser le 1.1.1.1 de Cloudflare ou le 8.8.8.8 de Google comme serveurs DNS, ils prennent tous en charge le DNS chiffré. Dans les réglages « DNS privé » d'Android, saisissez directement « one.one.one.one » ou « dns.google », c'est très simple. L'iPhone est un peu plus compliqué, nécessite d'installer un profil de description ou de passer par une application, mais cela vaut le coup.

#### V. La « navigation privée » rend-elle vraiment invisible ?

D'abord la conclusion :<strong>le mode navigation privée est le rideau de votre maison, pas une cape d'invisibilité.</strong>

Ce qu'il fait : ne laisse pas de traces localement — après fermeture de la fenêtre privée, le navigateur ne conserve pas votre historique de navigation, cookies, saisie de formulaires, historique de recherche. Pour emprunter l'ordinateur de quelqu'un pour chercher quelque chose, ou acheter un cadeau sans que la famille ne le découvre dans l'historique, le mode navigation privée est approprié.

Ce qu'il ne peut pas faire :

- Le site que vous visitez <strong>peut toujours voir que vous êtes venu</strong>, votre adresse IP, informations sur l'appareil, comportement de navigation, le site le sait clairement.
- Votre fournisseur d'accès Internet <strong>peut toujours voir quels sites vous avez visités</strong>, juste pas le contenu spécifique (si HTTPS est utilisé).
- L'administrateur réseau de l'entreprise/école <strong>peut aussi surveiller</strong> votre comportement en ligne.
- Les fichiers que vous téléchargez, les favoris que vous ajoutez sont <strong>conservés</strong>, ils ne disparaissent pas à la fermeture de la fenêtre.

Donc retenez : le mode navigation privée est un « effaceur local », pas un « vêtement d'invisibilité réseau ». Si vous avez vraiment besoin de cacher vos traces en ligne, il faut utiliser la combinaison VPN + navigateur Tor, mais pour un usage quotidien, connaître ces éléments suffit.

#### VI. Vie privée du navigateur : ne laissez pas le navigateur vous vendre

Vous ne vous en rendez peut-être pas compte, mais le navigateur lui-même est un énorme collecteur d'informations. Cookies, historique de navigation, cache, remplissage automatique, permissions de localisation... chacun peut révéler votre vie privée. Quelques conseils :

- <strong>Nettoyez régulièrement les données de navigation</strong>: de temps en temps, allez dans les réglages pour nettoyer cookies, cache, historique. Ce n'est pas pour empêcher « le suivi » — ça, nettoyer les cookies ne sert plus à grand-chose — mais pour éviter que le téléphone ne devienne de plus en plus lent. Le cache du navigateur peut occuper plusieurs Go.
- <strong>Oubliez le fantasme « Ne pas me suivre »</strong>: l'option « envoyer la demande 'Ne pas me suivre' » dans le navigateur demande essentiellement aux sites de ne pas vous suivre. Mais si le site écoute ou non, c'est une autre histoire, la plupart des sites ignorent. N'en attendez rien.
- <strong>Utilisez des navigateurs protecteurs de la vie privée</strong>: Firefox Focus, DuckDuckGo Browser, Brave bloquent par défaut les traqueurs et publicités, bien plus propres que les paramètres par défaut de Chrome et Safari.
- <strong>Le moteur de recherche compte aussi</strong>: utilisez DuckDuckGo à la place de Baidu/Google, il n'enregistre pas votre historique de recherche, ne construit pas de profil utilisateur. Honnêtement, les résultats de recherche sont moins précis que Google, mais pour des recherches quotidiennes, c'est suffisant.
- <strong>Vérifiez les permissions des applications</strong>: allez dans les réglages du téléphone pour voir quelles permissions ont été accordées à votre navigateur. A-t-il vraiment besoin d'accéder à votre localisation, micro, contacts ? Très probablement non.

#### VII. Liste de sécurité pratique : protégez-vous à partir de maintenant

Après tout cela, voici une liste de sécurité simple et directe, une demi-heure pour tout régler, la sécurité de votre smartphone fera un bond en avant :

1. <strong>Désactivez la connexion WiFi automatique</strong>: iPhone dans Réglages-WiFi, Android dans les réglages WiFi.
2. <strong>Changez pour un DNS chiffré</strong>: Android, réglez le DNS privé sur « dns.google », iPhone, utilisez une application ou un profil de description pour configurer le DoH de 1.1.1.1.
3. <strong>Activez l'authentification à deux facteurs (2FA)</strong>: WeChat, Alipay, identifiant Apple, compte Google, activez 2FA partout où c'est possible. Le code SMS est déjà le niveau le plus bas de 2FA, TOTP (comme Google Authenticator, Microsoft Authenticator) est préférable.
4. <strong>Vérifiez toutes les permissions des applications</strong>: passez en revue les permissions de chaque application, en particulier localisation, contacts, SMS, micro, caméra. Vous découvrirez que certaines applications lampe de poche demandent vos contacts — désinstallez-les immédiatement.
5. <strong>Nettoyez régulièrement les données du navigateur</strong>: programmez un rappel calendrier, une fois par mois, nettoyez le cache, les cookies.
6. <strong>N'utilisez pas les câbles des bornes de recharge publiques</strong>: le port USB peut à la fois charger et transmettre des données, les bornes de recharge malveillantes (appelées « Juice Jacking ») peuvent voler des données pendant que vous chargez. Emportez votre propre chargeur et câble.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Faites-le maintenant : faites un « check-up de sécurité » de votre smartphone

{class="list-decimal pl-6 mt-1 space-y-1"}
1. <strong>Mise à niveau DNS</strong>: Android : Réglages &gt; Connexions et partage &gt; DNS privé &gt; saisissez « one.one.one.one » ou « dns.google ». iPhone : recherchez « 1.1.1.1 DNS profile » dans Safari, installez le profil de description, ou téléchargez l'application 1.1.1.1 de Cloudflare.
2. <strong>Audit WiFi</strong>: ouvrez la liste WiFi, « oubliez » tous les points d'accès inconnus, peu utilisés, au nom bizarre.
3. <strong>Grand nettoyage des permissions</strong>: entrez dans Réglages &gt; Confidentialité/Gestion des permissions, passez en revue les permissions application par application. Marquez les applications aux exigences de permissions déraisonnables (comme une calculatrice demandant les contacts), envisagez de les désinstaller ou de trouver des alternatives.
4. <strong>Vérifiez la sécurité du compte</strong>: ouvrez la page de sécurité de votre identifiant Apple ou compte Google, regardez s'il y a des connexions d'appareils inconnus, confirmez que 2FA est activé, vérifiez que les contacts de récupération sont fiables.
:::
