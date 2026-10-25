---
id: di-si-shi-ba-zhang
num: 48
part: an-zhuo-kai-fa-pian
nav: Chapitre 48 : Découvrir Android — du système d'exploitation à l'écosystème de développement
toc: default
kind: chapter
---

### Chapitre 48 : Découvrir Android — du système d'exploitation à l'écosystème de développement

{class="chapter-intro mb-4"}
Félicitations pour cette décision — passer de « celui qui utilise son téléphone » à « celui qui crée des applications ». Avant de te lancer, étalons la carte : d'où vient Android ? Pourquoi les développeurs du monde entier écrivent-ils des applications pour lui ? Que se passe-t-il entre le moment où tes doigts tapent au clavier et celui où l'app arrive sur le téléphone d'un utilisateur ?

#### 1. Les origines d'Android : du « petit robot » au plus grand système du monde

L'histoire d'Android commence en 2003 : un ingénieur nommé Andy Rubin fonde la société Android, avec un objectif tout simple — concevoir un système d'exploitation intelligent qui « comprenne mieux l'appareil photo ». Google la rachète en 2005, fonde en 2007 l'Open Handset Alliance (OHA) avec des dizaines de fabricants, et en septembre 2008 sort officiellement le premier téléphone Android, le HTC Dream (G1).

La suite, tout le monde la connaît : en 2026, Android est le système d'exploitation mobile le plus répandu au monde, avec des milliards d'appareils actifs. Ton téléphone, ta box TV, le grand écran de ta voiture, ta montre connectée… tout tourne probablement sous Android. Qu'est-ce que cela signifie ? Que chaque ligne de code que tu écris peut servir au plus grand nombre de personnes possible.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Astuce : les gènes open source d'Android

{class="mt-1"}
Le cœur du code d'Android (AOSP, Android Open Source Project) est open source — chaque fabricant peut le modifier et le personnaliser. C'est pourquoi Xiaomi a MIUI (aujourd'hui HyperOS), Huawei sa couche de compatibilité HarmonyOS et Samsung One UI. Bonne nouvelle pour toi : tu apprends « le développement Android », pas « le développement d'une marque » — un seul savoir-faire, valable sur tous les téléphones.
:::

L'évolution des numéros de version est savoureuse : à partir du Cupcake (Android 1.5), chaque grande version portait le nom d'un dessert — Donut, Éclair, Frozen Yogurt, Gingerbread… Ce n'est qu'en 2019, avec Android 10, que l'on est passé aux chiffres purs. En août 2026, la dernière version officielle est Android 17 ; or ce qui compte vraiment en développement, c'est la « version minimale prise en charge » : les grandes apps la fixent en général entre Android 8 (API 26) et Android 10 (API 29) — viser les appareils d'il y a quelques années, c'est s'assurer un bassin d'utilisateurs assez large.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Version</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Nom de code / année</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">L'essentiel pour le développeur</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 8 (API 26)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Oreo · 2017</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Canaux de notification, restrictions en arrière-plan — le plancher de beaucoup d'anciens modèles</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 10 (API 29)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2019</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Le stockage cloisonné fait son apparition : les règles d'accès aux fichiers changent en profondeur</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 12 (API 31)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2021</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Material You et ses couleurs dynamiques : l'interface fait un grand bond visuel</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 13 (API 33)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2022</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Autorisation des notifications à l'exécution : une fenêtre demande « peut-on t'envoyer des notifications ? »</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 14-15 (API 34-35)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2023-2024</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retour prédictif, pages de 16 Ko, confidentialité encore resserrée</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 16-17 (API 36-37)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2025-2026</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Rythme plus soutenu des versions mineures, intégration des fonctions IA (extensions Gemini, par exemple)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Brève histoire des versions d'Android (à août 2026, l'essentiel pour le développement)

#### 2. Quel langage utiliser : Java ou Kotlin ?

Deux langages dominent l'histoire du développement Android. Java est le « doyen fondateur » — présent dès la naissance d'Android. Kotlin, choisi par Google en 2017 comme « citoyen de première classe », devient officiellement prioritaire à partir de 2019 (« Kotlin-first ») ; en 2026, presque tous les nouveaux projets sont en Kotlin et les anciens migrent progressivement.

Soyons francs : si tu pars de zéro, apprends directement Kotlin et ne touche pas à Java. Trois raisons. Un : le code Kotlin est 30 à 40 % plus court que le Java (à fonctionnalité égale, c'est plus bref et plus lisible). Deux : il protège nativement des « NullPointerException », ce cauchemar des débutants. Trois : tous les tutoriels modernes, la documentation officielle et les outils de programmation IA (tu te souviens de notre livre sur l'IA ?) sont calés sur Kotlin. Tu ne rencontreras Java que pour maintenir de vieux projets ou lire du vieux code.

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
Style Java (version verbeuse)

{class="font-mono text-xs leading-relaxed"}
public class MainActivity extends Activity {<br>&nbsp;&nbsp;@Override<br>&nbsp;&nbsp;protected void onCreate(Bundle b) {<br>&nbsp;&nbsp;&nbsp;&nbsp; super.onCreate(b);<br>&nbsp;&nbsp;&nbsp;&nbsp; setContentView(R.layout.activity);<br>&nbsp;&nbsp;}<br>}
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
Style Kotlin (version épurée)

{class="font-mono text-xs leading-relaxed"}
class MainActivity : ComponentActivity() {<br>&nbsp;&nbsp;override fun onCreate(b: Bundle?) {<br>&nbsp;&nbsp;&nbsp;&nbsp; super.onCreate(b)<br>&nbsp;&nbsp;&nbsp;&nbsp;setContent { App() }<br>&nbsp;&nbsp;}<br>}
:::
:::

Pour la même chose, Kotlin économise une pile d'accolades et de code passe-partout. On l'apprendra sérieusement au chapitre 50 ; pour l'instant, retiens juste : la « langue commune » du développement Android s'appelle Kotlin.

#### 3. Comment naît une application ?

Beaucoup imaginent que « développer une app » revient à s'installer devant l'ordinateur et à coder à toute vitesse. En réalité, entre l'idée et le téléphone de l'utilisateur, une app passe par une chaîne à peu près comme celle-ci :

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-lightbulb mr-1"></i> Idée</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center">📐 Conception (interface + fonctions)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-keyboard mr-1"></i> Écrire le code</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hammer mr-1"></i> Compiler et empaqueter (APK/AAB)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> Tester (émulateur + appareil réel)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-rocket mr-1"></i> Publier (boutique/installateur)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figure 1 : Le parcours complet d'une app Android, de l'idée à la publication
:::

Deux notions de ce parcours sont à connaître dès maintenant :

- APK : le format de paquet d'installation des applications Android (.apk). Un double-clic suffit pour l'installer sur le téléphone, comme un .exe sous Windows. Pour tes tests de tous les jours ou pour la partager entre amis, c'est le bon format.
- AAB : Android App Bundle (.aab), le « format d'emballage haut de gamme » réservé à la publication sur Google Play. La boutique le découpe dynamiquement selon le modèle de téléphone de l'utilisateur, pour que chacun télécharge un paquet plus léger. On ne peut pas l'installer soi-même : il passe obligatoirement par la boutique.

Tu entendras aussi sans cesse un mot : SDK (Software Development Kit, kit de développement logiciel). C'est tout l'équipement de développement fourni par Android — bibliothèques d'API de chaque version, outils de débogage, images d'émulateur, etc. Les classes comme Activity ou Button que tu appelles dans ton code viennent toutes du SDK.

#### 4. Le panorama de la stack Android : ta « liste d'armes »

Avant d'entrer dans le vif du sujet, voici la configuration standard d'un projet Android courant en 2026 — pas de panique si cette liste te semble opaque pour l'instant : relis-la à la fin du livre et tout s'éclairera :

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Couche</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Choix dominants (2026)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">À quoi ça sert</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Langage</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin 2.x</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Le langage de la logique</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Interface</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Jetpack Compose + Material 3</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Dessiner l'interface en code (le fil conducteur de ce livre)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Architecture</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MVVM + ViewModel</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Séparer l'interface de la logique pour garder un code propre</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Stockage des données</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room (base de données) + DataStore (préférences)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Stocker les données dans le téléphone</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Réseau</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit + OkHttp + coroutines Kotlin</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Dialoguer avec le serveur</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Outils de build</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gradle + Kotlin DSL</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Transformer le code en paquet installable</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Environnement de développement</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android Studio</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">L'IDE « tout-en-un » officiel de Google</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Panorama de la stack Android dominante en 2026

Ne te laisse pas impressionner par cette série de termes anglais. Ils sont comme les casseroles et les poêles de la cuisine : pour l'instant, tu as juste besoin de savoir « pour cuisiner, il faut entrer dans la cuisine » ; quant à savoir comment chaque outil s'utilise, les chapitres suivants te le démonteront un par un. Et bonne nouvelle : quand tu crées un nouveau projet, Android Studio configure automatiquement toute cette panoplie pour toi — tu n'as plus qu'à faire sauter.

#### 5. Android vs iOS : la première leçon de « choix de camp » du développeur

Tu as peut-être en main à la fois un appareil Android et un appareil Apple. En tant que développeur, les différences d'expérience entre les deux méritent d'être connues à l'avance — il ne s'agit pas de prendre parti sur « lequel est le meilleur », mais de faire des comptes bien réels : « de quel côté est-il plus facile de démarrer ? »

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Critère</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Développement Android</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Développement iOS</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ordinateur de développement</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Windows / Mac / Linux : tout convient</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mac obligatoire (Xcode est exclusif)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Outils de développement</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android Studio (gratuit)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode (gratuit) + 99 USD par an pour publier</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Revue avant publication</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Souple, de quelques heures à quelques jours</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Strict, 1 à 7 jours est la norme</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Essai sur l'appareil</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">APK : publication et installation en toute liberté</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Distribution restreinte, tests via signature/TestFlight</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Environnement de revenus</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Surtout publicité et canaux chinois</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Meilleures habitudes d'achat intégré sur l'App Store</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Coût d'apprentissage</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Beaucoup de concepts (les quatre composants, etc.)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Écosystème fermé mais unifié, documentation excellente</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Comparaison des parcours de développement Android et iOS (août 2026)

Soyons honnêtes : si ton ordinateur n'est pas un Mac, cette question ne se pose même pas — Android est la seule option. Si tu as un Mac, tu peux lire les parties 8 et 9 de ce livre en parallèle : la logique de programmation est la même, et apprendre le second côté après le premier ira bien plus vite.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
À toi de jouer : découvre « l'Android » de ton téléphone

{class="mt-1"}
Ouvre [Réglages] > [À propos du téléphone] (ou « À propos de l'appareil ») sur ton téléphone, trouve la ligne « Version Android » — tape dessus plusieurs fois de suite et tu déclencheras même le petit jeu caché du système. Note ton numéro de version et compare avec le tableau des versions ci-dessus pour voir à quelle génération il appartient. Ton téléphone, c'est ta première « machine de test de développement ».
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Résumé du chapitre

- Android est né en 2008 ; en 2026, c'est le système mobile le plus partagé au monde, avec des milliards d'appareils actifs
- La dernière version officielle est Android 17 ; les apps grand public visent au minimum Android 8-10 pour toucher un public assez large
- Pour tout nouveau projet, utilise Kotlin : 30 % de code en moins, protection contre les pointeurs nuls, choix officiel
- APK pour installer soi-même, AAB pour la boutique ; le SDK est la trousse officielle du développeur
- La pile technique standard de 2026 : Kotlin + Compose + MVVM + Room + Retrofit + Gradle + Android Studio
:::
