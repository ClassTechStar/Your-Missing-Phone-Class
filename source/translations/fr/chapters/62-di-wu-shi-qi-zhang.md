---
id: di-wu-shi-qi-zhang
num: 57
part: an-zhuo-kai-fa-pian
nav: Chapitre 57 : Montée en compétence — permissions, notifications et architecture moderne
toc: default
kind: chapter
---

### Chapitre 57 : Le chemin de la maîtrise — permissions, notifications et architecture moderne

{class="chapter-intro mb-4"}
Savoir fabriquer une app n’est que le début. Ce chapitre aborde les marches qui mènent de « savoir faire » à « bien faire » : demander des permissions avec élégance, envoyer des notifications sans agacer, hisser l’architecture d’un étage, et — en 2026 — coder Android en duo avec l’IA. Chaque point est un obstacle que tu rencontreras très vite dans un vrai projet.

#### 1. Les permissions à l’exécution : frapper avant d’entrer

Caméra, localisation, contacts, notifications… pour ces « zones sensibles », Android exige que l’app les demande à l’utilisateur à l’exécution (depuis Android 6). La règle : déclarer d’abord (Manifest), demander ensuite (code), et dégrader élégamment en cas de refus. Dans Compose, le plus paisible est d’utiliser rememberPermissionState de la bibliothèque officielle Accompanist :

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Permissions à l'exécution (version Compose)</span><span class="dots">···</span>
:::

```
// déclare d'abord dans le Manifest :
// &lt;uses-permission android:name="android.permission.CAMERA" /&gt;

@Composable
fun CameraButton() {
    val permission = rememberPermissionState(
        permission = android.Manifest.permission.CAMERA
    )
    Button(onClick = {
        when {
            permission.status.isGranted -&gt; openCamera()
            permission.status.shouldShowRationale -&gt; showExplainDialog()
            else -&gt; permission.launchPermissionRequest()
        }
    }) { Text("Prendre une photo") }
}
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Attention : que faire en cas de refus définitif ?

{class="mt-1"}
Une fois que l’utilisateur a coché « ne plus demander », launchPermissionRequest n’affiche plus de fenêtre. Il faut alors le guider vers les réglages du système pour une activation manuelle (avec un Intent vers la page de réglages de l’app) et expliquer dans l’interface « à quoi servira cette permission ». Un ton bienveillant augmente nettement l’envie de l’utilisateur d’accorder la permission — le texte de demande de permission mérite d’être rédigé avec soin.
:::

#### 2. Les notifications : dire des choses utiles au bon moment

Les notifications sont le canal par lequel l’app atteint l’utilisateur, et aussi la fonctionnalité la plus vite « mise sur liste noire ». Trois règles d’or : n’envoyer que l’utile, laisser l’utilisateur pouvoir couper, ne pas harceler en pleine nuit. Usage de base :

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Envoyer une notification</span><span class="dots">···</span>
:::

```
// sur Android 13+, il faut d'abord demander la permission POST_NOTIFICATIONS (voir section précédente)

// 1. créer le canal de notification (obligatoire sur Android 8+)
val channel = NotificationChannel(
    "reminder", "Rappels", NotificationManager.IMPORTANCE_DEFAULT
)
val manager = getSystemService(NotificationManager::class.java)
manager.createNotificationChannel(channel)

// 2. envoyer la notification
val notification = NotificationCompat.Builder(this, "reminder")
    .setSmallIcon(R.drawable.ic_notification)
    .setContentTitle("Rappel de dépenses")
    .setContentText("Tu n'as encore rien noté aujourd'hui")
    .setPriority(NotificationCompat.PRIORITY_DEFAULT)
    .build()
if (ActivityCompat.checkSelfPermission(this,
        Manifest.permission.POST_NOTIFICATIONS) == PackageManager.PERMISSION_GRANTED
) {
    manager.notify(1, notification)
}
```
:::

Pour les tâches planifiées (par exemple « rappeler de noter ses dépenses chaque jour à 20 h »), utilise WorkManager — c’est le « majordome de l’ordonnancement en arrière-plan » recommandé par Google : il garantit que la tâche s’exécute au bon moment, sans que tu aies à te soucier de l’optimisation de batterie. Pour tout besoin de type réveil, c’est le bon choix, à coup sûr.

#### 3. Architecture avancée : injection de dépendances et modularisation

Quand le projet grossit, deux « douces misères » se présentent :

- La création d’objets part en vrille : chaque écran crée sa propre base de données, son propre API — utilise Hilt (framework d’injection de dépendances) pour tout centraliser : « qui veut quoi n’a qu’à demander, et on lui tend » ;
- Le code s’entasse en montagne : un projet mono-module devient de plus en plus lent à modifier — découpe-le en multi-modules (app / core / feature-xxx), chaque fonctionnalité se développant et se testant de façon indépendante.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Astuce : ne surconçois pas

{class="mt-1"}
Hilt et la modularisation sont de bons outils, mais ne t’y précipite pas sur un projet solo. Le carnet de comptes en un seul module + création manuelle des dépendances suffit largement. Attends que le code dépasse quelques dizaines de milliers de lignes, que la compilation ralentisse ou que tu passes à plusieurs, et introduis-les selon les besoins. Les outils servent l’objectif, ils ne servent pas à épater — c’est aussi le principe de « simplicité d’abord » de notre livre sur le codage avec l’IA.
:::

#### 4. La nouveauté de 2026 : le développement Android assisté par l’IA

En 2026, l’IA est déjà profondément encastrée dans le flux de développement Android. Si tu veux accélérer, cette combinaison est bien rodée :

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Étape</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Comment l’IA aide</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ton rôle</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Écrire du code</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Complétion et génération par Gemini intégré à Android Studio ou par extensions d’IA tierces</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Décrire clairement le besoin, relire le résultat</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Chercher de la documentation</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Donner à l’IA la documentation officielle et les messages d’erreur à interpréter</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Vérifier les conclusions clés dans la documentation officielle</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Écrire les tests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Faire générer par l’IA des cas selon trois catégories : « normal / limite / erreur »</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Vérifier que les cas collent au sens métier</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Corriger les bugs</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Coller la pile d’erreurs + le code concerné, l’IA localise et corrige</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Comprendre les modifications, lancer les tests pour valider</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Les quatre scénarios du développement Android assisté par l’IA

La méthodologie concrète — comment donner des instructions à l’IA, comment réceptionner les livraisons, comment éviter les pièges — est développée sur 11 chapitres complets dans la septième partie de ce livre, « L’IA en pratique » (chapitres 37 à 47) ; sa lecture en parallèle est vivement conseillée : la syntaxe Android ici, l’art de collaborer avec l’IA dans la septième partie.

#### 5. Optimisation des performances Compose et outils de débogage

Écrire avec Compose est un plaisir, mais un « excès de recomposition » peut provoquer des à-coups. Trois astuces pratiques :

- Stabilise les paramètres : ajoute @Immutable à tes data classes ou utilise derivedStateOf pour éviter que des changements d’état sans rapport ne déclenchent de vastes recompositions ;
- Pense à utiliser key : items(list, key = { it.id }) fait que les ajouts et suppressions ne touchent que les éléments concernés — sans key, supprimer un élément peut redessiner toute la liste ;
- Le mode Compose de Layout Inspector : il montre en temps réel le nombre de recompositions de chaque Composable — tu vois d’un coup d’œil qui se recompose trop souvent, et tu optimises ces points chauds.

Active aussi le rapport du compilateur Compose (Metrics) : il génère un rapport sur « quels composants sont instables » — sur la route de la maîtrise, les données sont toujours plus fiables que les impressions.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
À toi de jouer : ajoute le « trio » au carnet de comptes

{class="mt-1"}
① Ajoute au carnet de comptes le « rappel de comptes à 20 h chaque jour » (WorkManager + canal de notification + permission de notification d’Android 13) ; ② remplace la création de la base de données et de l’API par une injection Hilt ; ③ essaie d’accélérer la fonction « filtre mensuel » avec un outil d’IA, puis contrôle le résultat selon la méthode de réception en trois niveaux. Une fois le trio terminé, ton projet aura des allures « d’armée régulière ».
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Résumé du chapitre

- Permissions sensibles : déclaration dans le Manifest + demande à l’exécution + orientation élégante en cas de refus
- Les trois règles des notifications : n’envoyer que l’utile, pouvoir couper, ne pas harceler ; canal + permission, rien ne manque
- Tâches planifiées : WorkManager, ne réinvente pas la roue
- Hilt gère les objets, la modularisation gère le code — pas la peine de s’y précipiter sur un petit projet solo
- Quatre scénarios d’assistance IA : coder, chercher la doc, écrire les tests, corriger les bugs ; la méthodologie est dans la septième partie (chapitres 37 à 47)
:::
