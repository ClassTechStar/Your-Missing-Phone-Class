---
id: di-liu-shi-si-zhang
num: 64
part: ios-kai-fa-pian
nav: Chapitre 64 : Stockage des données et requêtes réseau
toc: default
kind: chapter
---

### Chapitre 64 : Stockage des données et requêtes réseau

{class="chapter-intro mb-4"}
Une App qui sait seulement « montrer » est une App morte ; une App qui stocke des données et se branche sur le réseau vit. Ce chapitre te présente le « trio » de la couche données d'iOS : UserDefaults (petits réglages), SwiftData (données structurées), URLSession (le dialogue avec le serveur), auxquels s'ajoutent Codable pour analyser le JSON et le moderne async/await. Après ce chapitre, tu pourras écrire de vraies Apps capables de retenir les habitudes de l'utilisateur et de mettre leur contenu à jour en direct.

#### 1. Choisir sa solution de stockage : d'abord ce tableau

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Solution</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ce qu'elle convient de stocker</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Particularités</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Où dans ce livre</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UserDefaults</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Réglages isolés (interrupteurs, préférences)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Paires clé-valeur, simple et direct</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Réglages au chapitre 65, villes favorites au chapitre 66</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftData</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Données structurées (écritures, enregistrements)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Encapsulation officielle de base de données, déclaration en une ligne via @Model</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Écritures comptables au chapitre 65</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">URLSession</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Données du serveur (pas de stockage, récupérées en ligne)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Framework réseau du système, aucune dépendance tierce</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Données météo au chapitre 66</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
La répartition des rôles du trio de données

Retiens cette formule : « les petits réglages vont dans UserDefaults, les données en série vont dans SwiftData, les données venues de dehors passent par URLSession ». Core Data des vieux tutos reste utilisable (SwiftData en est le costume moderne), et le SQLite écrit à la main s'évite en général — apprends directement le neuf, ne prends pas les vieux chemins.

#### 2. UserDefaults : ranger quelques petits réglages

::: div .code-block
:::inline div .code-head
<span>SWIFT · Exemple avec UserDefaults</span><span class="dots">···</span>
:::

```
// écrire : stocker une valeur
UserDefaults.standard.set(true, forKey: "isDarkMode")
UserDefaults.standard.set("Paris", forKey: "favoriteCity")

// lire : le récupérer (sinon renvoie la valeur par défaut)
let isDark = UserDefaults.standard.bool(forKey: "isDarkMode")
let city = UserDefaults.standard.string(forKey: "favoriteCity") ?? "Paris"

// supprimer : retirer une clé
UserDefaults.standard.removeObject(forKey: "isDarkMode")
```
:::

Souviens-toi qu'il ne convient qu'aux petits réglages isolés — dès quelques dizaines ou centaines d'enregistrements, remets le volant à SwiftData ; ne prends pas UserDefaults pour une base de données (ça ralentit le démarrage et les requêtes y sont peu commodes).

#### 3. SwiftData : offrir aux données un « vrai chez-soi »

SwiftData est la solution de base de données officielle depuis iOS 17 ; elle pousse la simplicité à l'extrême pour créer les tables et gérer ajouts, suppressions, modifications et lectures — une annotation @Model, et la classe de données devient une table :

::: div .code-block
:::inline div .code-head
<span>SWIFT · Exemple avec SwiftData</span><span class="dots">···</span>
:::

```
import SwiftData

// 1. @Model : cette classe devient automatiquement une "table"
@Model
class Record {
    var amount: Double
    var category: String
    var note: String
    var date: Date

    init(amount: Double, category: String, note: String, date: Date) {
        self.amount = amount
        self.category = category
        self.note = note
        self.date = date
    }
}

// 2. on branche le conteneur au point d'entrée de l'app
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .modelContainer(for: Record.self)   // base de données prête
    }
}

// 3. dans la vue on lit avec @Query et on écrit avec @Environment
struct RecordListView: View {
    @Query(sort: \Record.date, order: .reverse) var records: [Record]
    @Environment(\.modelContext) private var context

    var body: some View {
        List(records) { r in
            Text("\(r.category) \(r.amount) yuan")
        }
    }

    func add(amount: Double, category: String) {
        let r = Record(amount: amount, category: category, note: "", date: Date())
        context.insert(r)     // enregistrer
        try? context.save()   // persister sur disque
    }
}
```
:::

Ce gabarit « @Model + modelContainer + @Query » se transporte tel quel dans n'importe lequel de tes projets — il suffit de changer les noms de champs. Dès que les données bougent, @Query rafraîchit l'interface tout seul : la magie est délicieuse.

#### 4. Codable : « traduire » le JSON

Les données des serveurs sont pour l'essentiel du texte JSON. Le protocole Codable de Swift fait que la conversion « JSON ⇄ struct » se produit automatiquement — dès que les noms de champs concordent, la magie opère :

::: div .code-block
:::inline div .code-head
<span>SWIFT · Analyser du JSON avec Codable</span><span class="dots">···</span>
:::

```
// JSON: {"name":"Paris","main":{"temp":26.5},"weather":[{"description":"Ensoleillé"}]}
struct WeatherResponse: Codable {
    let name: String
    let main: Main
    let weather: [Weather]
}
struct Main: Codable { let temp: Double }
struct Weather: Codable { let description: String }

// de chaîne JSON vers struct
let decoder = JSONDecoder()
let data = jsonString.data(using: .utf8)!
let result = try decoder.decode(WeatherResponse.self, from: data)
print(result.weather[0].description)   // "Ensoleillé"
```
:::

Règle d'airain : regarde d'abord le JSON réellement renvoyé, définis les champs ensuite. Une foule de bugs d'« analyse impossible » tiennent à un nom de champ mal écrit ou à un type deviné de travers (le serveur envoie la chaîne "26.5", toi tu déclares un Double) — imprime le JSON brut et compare : dix secondes pour localiser.

#### 5. URLSession + async/await : parler au serveur

Pour se brancher, iOS emploie URLSession fourni avec le système ; associé à async/await de Swift (les fonctions asynchrones), « attendre le réseau » devient aussi naturel qu'« attendre son colis » :

::: div .code-block
:::inline div .code-head
<span>SWIFT · URLSession + async/await</span><span class="dots">···</span>
:::

```
struct WeatherService {
    // fonction async : async marque "j'ai besoin d'attendre un moment", throws marque "peut échouer"
    func fetchWeather(city: String) async throws -> WeatherResponse {
        let url = URL(string:
            "https://api.example.com/weather?city=\(city)")!
        let (data, _) = try await URLSession.shared.data(from: url)
        return try JSONDecoder().decode(WeatherResponse.self, from: data)
    }
}

// point d'appel (dans .task) :
.task {
    do {
        let weather = try await service.fetchWeather(city: "Paris")
        // mettre à jour l'interface…
    } catch {
        print("Erreur : \(error)")
    }
}
```
:::

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Piège à éviter : les deux règles d'airain du réseau

{class="mt-1"}
① Pour le réseau, obligatoirement async/await, et jamais de blocage du thread principal — une interface figée, c'est une expérience de crash. La concurrence structurée de Swift rend cela naturel, mais n'oublie pas try await et do/catch. ② ATS interdit par défaut le HTTP en clair : iOS exige HTTPS. Pour tester un service http:// local, il faut ouvrir une exception temporaire dans Info.plist (NSAppTransportSecurity), mais un produit officiel doit passer intégralement en HTTPS — la revue surveille aussi ce point.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
À toi de jouer : une petite App « phrase du jour »

#### 6. Classer aussi les erreurs réseau : ne pas balancer toutes les erreurs à l'utilisateur

Réseau coupé, délai dépassé, 404, erreur 500 du serveur… chaque erreur appelle son message :

::: div .code-block
:::inline div .code-head
<span>SWIFT · Gestion des erreurs par niveaux</span><span class="dots">···</span>
:::

```
func friendlyMessage(_ error: Error) -> String {
    if let urlError = error as? URLError {
        switch urlError.code {
        case .notConnectedToInternet: return "Réseau coupé, tu vérifies la connexion ?"
        case .timedOut:               return "Délai dépassé, tu réessailles plus tard ?"
        case .cannotFindHost:         return "Serveur introuvable"
        default:                      return "Problème de réseau : \(urlError.code)"
        }
    }
    if let d = error as? DecodingError {
        return "Format de données incorrect (l'API a peut-être changé)"
    }
    return "Erreur : \(error.localizedDescription)"
}
```
:::

À l'utilisateur, montre des « paroles humaines » ; aux journaux, garde la « langue d'origine » (print de l'erreur complète). Ne déballe pas devant l'utilisateur le charabia anglais de error.localizedDescription — le raffinement d'un produit se niche dans ces détails.

{class="mt-1"}
Trouve une API de citations gratuite (du genre hitokoto), tire la « phrase du jour » avec URLSession + async/await, affiche-la au centre de l'écran et ajoute un bouton « Une autre ». Puis range les phrases que tu aimes dans les « favoris » avec SwiftData. Cet exercice fait tourner UserDefaults, SwiftData, Codable et URLSession — une fois bouclé, les chapitres 7 et 8 seront un vrai jeu d'enfant.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Résumé du chapitre

- La formule : petits réglages dans UserDefaults, données en série dans SwiftData, données venues de dehors via URLSession
- Les trois coups de SwiftData : @Model déclare la table, modelContainer accroche le conteneur, @Query lit et context.insert écrit
- Codable « traduit » le JSON automatiquement : champs concordants, la magie opère
- URLSession + async/await : le réseau comme l'attente d'un colis ; do/catch pour traiter les échecs
- Deux règles d'airain : ne jamais bloquer le thread principal ; HTTPS obligatoire pour un produit officiel (ATS)
:::
