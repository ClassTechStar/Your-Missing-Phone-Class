---
id: di-liu-shi-ba-zhang
num: 68
part: ios-kai-fa-pian
nav: Chapitre 68 : Montée en compétence — permissions, notifications et architecture moderne
toc: default
kind: chapter
---

### Chapitre 68 : Le chemin de l'avancement — permissions, notifications et architecture moderne

{class="chapter-intro mb-4"}
Savoir fabriquer une App n'est que le commencement. Ce chapitre discute des marches à franchir entre « savoir faire » et « bien faire » : demander les permissions avec élégance, envoyer des notifications sans devenir insupportable, élever l'architecture d'un cran encore, et — en 2026 — écrire du code iOS en tandem avec l'IA. Chacun de ces sujets se présentera à toi tout de suite dans un vrai projet.

#### 1. Les permissions : frapper d'abord, entrer ensuite

Caméra, localisation, contacts, notifications… pour ces « zones sensibles », iOS exige que l'App demande à l'utilisateur par une fenêtre au moment de l'usage. La règle tient en trois pas : « déclarer + demander + dégrader avec élégance » :

::: div .code-block
:::inline div .code-head
<span>SWIFT · Demande de permissions (exemple : localisation)</span><span class="dots">···</span>
:::

```
// 1. déclare dans Info.plist le texte d'usage (sans déclaration, crash immédiat !)
// Privacy - Location When In Use Usage Description: "Servira à consulter la météo de ta ville"

// 2. la demander au moment de l'usage
import CoreLocation

@Observable
class LocationModel {
    private let manager = CLLocationManager()

    func request() {
        switch manager.authorizationStatus {
        case .notDetermined: manager.requestWhenInUseAuthorization()
        case .denied, .restricted: /* guider vers les réglages pour l'activer */
        default: /* accordé, on y va */
        }
    }
}

// 3. dégrader élégamment après un refus : afficher un message et aller aux réglages
// UIApplication.shared.open(URL(string: UIApplication.openSettingsURLString)!)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Attention : les permissions iOS ne passent qu'« une fois »

{class="mt-1"}
La fenêtre de permission iOS ne s'affiche qu'une seule fois — après un refus, elle ne reviendra jamais. Donc : choisis le moment de la demande « à l'instant où l'utilisateur s'apprête à s'en servir » (et non une salve au lancement), et écris un texte qui explique l'usage. Le guidage d'interface après refus (« active la localisation dans Réglages ») est d'équipement ; ne laisse pas l'utilisateur enfermé dans une impasse.
:::

#### 2. Les notifications : dire des choses utiles au bon moment

Les notifications sont le canal par lequel l'App rejoint l'utilisateur, et la fonction qu'il « bloque » le plus volontiers. Avec le framework UserNotifications d'iOS, trois disciplines pour en envoyer : ne diffuser que l'utile, laisser l'utilisateur couper, ne pas harceler au milieu de la nuit. L'usage de base :

::: div .code-block
:::inline div .code-head
<span>SWIFT · Notifications locales</span><span class="dots">···</span>
:::

```
import UserNotifications

// 1. demander la permission de notification (une seule fenêtre)
UNUserNotificationCenter.current()
    .requestAuthorization(options: [.alert, .sound, .badge]) { granted, _ in
        print(granted ? "Accordé" : "Refusé")
    }

// 2. programmer un "rappel de dépenses chaque jour à 20 h"
func scheduleDailyReminder() {
    let content = UNMutableNotificationContent()
    content.title = "Rappel de dépenses"
    content.body = "Tu n'as encore rien noté aujourd'hui"
    content.sound = .default

    var comps = DateComponents()
    comps.hour = 20
    let trigger = UNCalendarNotificationTrigger(dateMatching: comps, repeats: true)

    let request = UNNotificationRequest(
        identifier: "daily-reminder",
        content: content,
        trigger: trigger
    )
    UNUserNotificationCenter.current().add(request)
}
```
:::

Attention : la permission de notification d'iOS, elle aussi, ne se demande « qu'une fois », et l'utilisateur peut la couper à tout instant dans les réglages du système — la valeur perçue du contenu des notifications est donc capitale : un seul abus peut te priver de l'utilisateur pour toujours.

#### 3. Architecture avancée : MVVM en profondeur et testabilité

Tu as déjà utilisé MVVM au chapitre 65 ; voici trois points avancés pour compléter :

- L'abstraction par protocole : fais dépendre le ViewModel d'un protocole (protocol) plutôt que d'une classe concrète — aux tests, tu peux injecter une « fausse source de données » ; c'est la pierre d'angle de la testabilité ;
- Responsabilité unique : un ViewModel ne s'occupe que d'une seule chose (celui des comptes ne gère pas la météo) ; quand les fonctions s'entassent, on scinde ;
- Ne surconçois pas : pour un petit projet en solo, « classe @Observable + abstraction par protocole » suffit amplement. Les architectures lourdes de type VIPER ou Clean Architecture attendront que l'équipe et la complexité sonnent à ta porte — les outils servent un objectif, ils ne servent pas à se pavaner.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Astuce : les « dividendes de l'écosystème » de SwiftUI

{class="mt-1"}
L'écosystème iOS cache encore deux façons avancées « réservées à la maison » : les widgets (WidgetKit) laissent l'utilisateur lire l'information sans ouvrir l'App (les « dépenses du mois » du carnet posées sur l'écran d'accueil), et les raccourcis (App Intents) laissent l'utilisateur invoquer tes fonctions par Siri ou l'automatisation. Les deux s'appuient sur des frameworks officiels, peu coûteux à apprivoiser, mais au gain d'expérience utilisateur énorme — sur la route de l'avancement, ce sont des déverrouillages à traiter en priorité.
:::

#### 4. Les nouveautés de 2026 : le développement iOS assisté par l'IA

En 2026, l'IA est déjà profondément enchâssée dans le flux de développement Apple. Si tu veux gagner en vitesse, cette combinaison est bien rodée :

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Étape</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Comment l'IA aide</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ta responsabilité</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Écrire le code</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Complétion de code intégrée à Xcode + génération par des plugins IA tiers</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Décrire clairement le besoin, passer au crible le produit</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Chercher la documentation</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Donner la doc officielle et les messages d'erreur à l'IA pour les décoder</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Revenir à la doc officielle pour vérifier les conclusions clés</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Écrire les tests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Faire générer par l'IA des cas XCTest en trois classes « normal / limites / exception »</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Confirmer que les cas collent au sens métier</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Corriger les bugs</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Coller le journal de plantage + le code concerné, l'IA localise et répare</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Comprendre les modifications, lancer les tests pour valider</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Les quatre scénarios du développement iOS assisté par l'IA

La méthode concrète — comment donner des instructions à l'IA, comment passer la recette, comment éviter les pièges — occupe onze chapitres complets dans la septième partie de ce livre, « Pratique de la programmation avec l'IA » (chapitres 37-47) ; je te conseille chaudement de lire les deux en parallèle : la syntaxe de Swift pour cette partie, l'art de collaborer avec l'IA pour la septième.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
À toi de jouer : ajoute le « trio » au carnet de comptes

#### 5. L'essentiel de la concurrence Swift : @MainActor et Task

Le régime de concurrence de Swift 6 comporte deux règles que tout débutant doit comprendre :

- L'interface ne se met à jour que sur le thread principal : les vues SwiftUI sont @MainActor par défaut ; les rappels réseau reviennent sur le thread principal avant de toucher à l'état (await MainActor.run { ... }, ou bien marque le ViewModel comme @MainActor) ;
- Les tâches asynchrones se pilotent avec Task : le modificateur .task { } démarre tout seul quand la vue apparaît et s'annule tout seul à sa disparition — c'est la posture standard pour lancer un travail asynchrone en SwiftUI ; évite d'écrire des Task à nu en vrac dans le body.

::: div .code-block
:::inline div .code-head
<span>SWIFT · La façon asynchrone standard</span><span class="dots">···</span>
:::

```
struct WeatherScreen: View {
    @State private var vm = WeatherViewModel()

    var body: some View {
        Group {
            switch vm.state {
            case .loading: ProgressView()
            case .success(let d): WeatherContent(data: d)
            case .error(let m): Text(m)
            }
        }
        .task {                       // démarre à l'apparition, s'annule à la disparition
            await vm.search(city: "Paris")
        }
    }
}
```
:::

Derrière ces deux règles se tient la conception de Swift 6 « sûr contre les courses de données » — le compilateur te signale l'erreur dès que tu écris de travers, au lieu d'attendre que l'App plante pour le découvrir. Les erreurs du compilateur ne te cherchent pas des noises : elles interceptent les balles à ta place.

{class="mt-1"}
① Ajoute au carnet le « rappel de comptes quotidien à 20 h » (permission de notification + notification locale) ; ② transforme la source de données du ViewModel en abstraction par protocole et écris un test unitaire qui injecte de fausses données ; ③ ajoute un widget d'écran d'accueil « dépenses du mois ». Le trio terminé, ton projet aura les allures d'une « troupe régulière ».
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Résumé du chapitre

- Trois pas de la permission : déclaration dans Info.plist (l'omettre = plantage assuré), demande au moment de l'usage, guidage vers Réglages en cas de refus
- La fenêtre de permission iOS ne passe qu'une fois : choisis « l'instant où on s'en sert », et écris clairement l'usage
- Trois disciplines de notification : ne diffuser que l'utile, pouvoir couper, ne pas harceler ; framework UserNotifications
- MVVM avancé : abstraction par protocole (testable), responsabilité unique, pas de surconception
- Dividendes de l'écosystème : widgets WidgetKit + raccourcis App Intents
- Quatre scénarios d'assistance par l'IA : coder, chercher la doc, écrire les tests, corriger les bugs ; méthode en septième partie (chapitres 37-47)
:::
