---
id: di-liu-shi-liu-zhang
num: 66
part: ios-kai-fa-pian
nav: Chapitre 66 : Projet 2 — App météo (version réseau)
toc: default
kind: chapter
---

### Chapitre 66 : Projet 2 — l'App météo (version réseau)

{class="chapter-intro mb-4"}
Le carnet de comptes, c'était « forger son fond » ; l'App météo, c'est « voir du pays » — elle doit se frotter à Internet. Avec ce projet, tu apprendras à : demander une API gratuite, analyser le JSON, gérer les trois états d'interface « chargement / succès / échec », et bien planquer ta clé d'API. Une fois terminé, tu seras capable de faire n'importe quelle App « connectée » — actualités, taux de change, traduction : la recette est rigoureusement la même.

#### 1. Demander une API météo gratuite

Pour s'entraîner à titre personnel, mise sur OpenWeatherMap ou, côté chinois, QWeather — les deux offrent un quota gratuit utilisable dès l'inscription. Prenons OpenWeatherMap pour exemple :

1. Crée un compte → génère une clé (apikey) dans la page API keys ;
2. La version gratuite peut appeler l'interface Current Weather : api.openweathermap.org/data/2.5/weather? q=beijing&appid=taCle&units=metric ;
3. Essaie d'abord une fois dans le navigateur, pour voir la tête du JSON renvoyé — c'est le « devoir préparatoire » à faire avant de brancher n'importe quelle API.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Piège à éviter : jamais de clé en dur dans le code

{class="mt-1"}
Une clé d'API vaut le « mot de passe de ton portefeuille » : à peine écrite dans le code et poussée sur GitHub, elle est ramassée par des robots et essorée en quelques heures. La bonne manière iOS : place-la dans Config.xcconfig (un fichier de configuration déjà ignoré par gitignore) et lis-la dans le code via Info.plist. Cherche « gérer les clés API avec un xcconfig sous iOS » et suis le pas-à-pas.
:::

#### 2. La couche réseau : URLSession + Codable

Définis d'abord le modèle d'après le JSON renvoyé par l'API, puis écris le service :

::: div .code-block
:::inline div .code-head
<span>SWIFT · Modèle de données + service</span><span class="dots">···</span>
:::

```
// JSON: {"weather":[{"description":"Ensoleillé"}],"main":{"temp":26.5,"humidity":40},"name":"Paris"}
struct WeatherResponse: Codable {
    let weather: [Weather]
    let main: Main
    let name: String
}
struct Weather: Codable { let description: String }
struct Main: Codable { let temp: Double; let humidity: Int }

struct WeatherService {
    let key: String   // lu depuis xcconfig

    func fetchWeather(city: String) async throws -> WeatherResponse {
        var comps = URLComponents(string: "https://api.openweathermap.org/data/2.5/weather")!
        comps.queryItems = [
            URLQueryItem(name: "q", value: city),
            URLQueryItem(name: "appid", value: key),
            URLQueryItem(name: "units", value: "metric"),
            URLQueryItem(name: "lang", value: "zh_cn")
        ]
        let (data, _) = try await URLSession.shared.data(from: comps.url!)
        return try JSONDecoder().decode(WeatherResponse.self, from: data)
    }
}
```
:::

#### 3. Trois états d'interface : chargement / succès / échec

L'âme d'une App connectée tient à la « gestion des états ». Réseau lent, connexion coupée, nom de ville mal tapé… chaque situation doit être portée à la connaissance de l'utilisateur par l'interface. Représente-les avec élégance au moyen d'une énumération + switch :

::: div .code-block
:::inline div .code-head
<span>SWIFT · État de l'interface</span><span class="dots">···</span>
:::

```
enum LoadState {
    case loading                  // chargement
    case success(WeatherResponse) // succès
    case error(String)            // échec
}

@Observable
class WeatherViewModel {
    var state: LoadState = .loading
    private let service = WeatherService(key: Config.apiKey)

    func search(city: String) async {
        state = .loading
        do {
            let data = try await service.fetchWeather(city: city)
            state = .success(data)
        } catch {
            state = .error("Ville introuvable, essaies un autre nom ?")
        }
    }
}

// dans l'interface :
switch vm.state {
case .loading: ProgressView("Chargement…")
case .success(let d): WeatherContent(data: d)
case .error(let msg): Text(msg).foregroundColor(.secondary)
}
```
:::

Ce triptyque loading/success/error est le « gabarit passe-partout » des interfaces connectées : apprends-le par cœur, et décline-le plus tard pour toutes tes Apps en ligne.

#### 4. Le code d'interface en conditions réelles : peindre la météo

::: div .code-block
:::inline div .code-head
<span>SWIFT · Écran météo (extrait clé)</span><span class="dots">···</span>
:::

```
struct WeatherContent: View {
    let data: WeatherResponse

    var body: some View {
        VStack(spacing: 12) {
            Text(data.name)
                .font(.title.bold())
            Text("\(Int(data.main.temp))°C")
                .font(.system(size: 76, weight: .thin))
            Text(data.weather.first?.description ?? "Inconnu")
                .font(.title3)
                .foregroundColor(.secondary)
            HStack(spacing: 24) {
                Label("Humidité \(data.main.humidity)%", systemImage: "humidity")
                Label("Ressenti \(Int(data.main.temp))°C", systemImage: "thermometer")
            }
        }
        .padding()
    }
}
```
:::

Quelques petits détails à apprendre : first? prend sans danger le premier élément (la liste peut être vide), ?? "Inconnu" apporte le texte de repli ; un chiffre de température en taille 76 et graisse fine est la recette classique des Apps météo ; Label est le composant officiel « icône + texte », plus réglementaire qu'un HStack assemblé à la main.

#### 5. Détails d'interaction et villes favorites

- Champ de recherche : le modificateur .searchable en haut, avec l'interaction de recherche du système, appelle vm.search à la validation ;
- Villes favorites : range les villes consultées souvent dans UserDefaults, et la recherche repart toute seule à la prochaine ouverture ;
- Tirer pour rafraîchir : .refreshable { await vm.search(...) } règle la question en une ligne ;
- Icônes météo : fais la correspondance par description avec Image(systemName:) (sun.max / cloud.rain / snowflake), et l'interface s'éveille aussitôt.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Astuce : le « piège » des noms de villes en chinois

{class="mt-1"}
OpenWeatherMap gère moyennement les noms de villes chinois : chercher « Pékin » en chinois peut ne rien renvoyer alors que "beijing" passe. Pour en faire un produit, on embarque une table de correspondance « nom de ville → anglais/coordonnées », ou on branche un service météo chinois. Le temps de l'entraînement, contente-toi des noms de villes en pinyin/anglais ; ne te bagarre pas avec ça.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
À toi de jouer : la liste de recette de l'App météo

#### 6. Déboguer les requêtes réseau : impression, capture et réseau lent simulé

Quand une App connectée déraille, neuf fois sur dix c'est « la requête mal envoyée » ou « la réponse mal analysée ». Trois instruments de débogage :

1. Imprimer les données brutes : imprime String(data: data, encoding: .utf8) pour voir le JSON d'origine — noms de champs et types en un clin d'œil, dix fois plus vite qu'en devinant ;
2. Outils de capture : Proxyman (gratuit sur Mac) ou l'open source Charles interceptent toutes les requêtes et réponses de l'App, et rendent la couche réseau lisible comme une radiographie ;
3. Simuler un réseau faible : dans le menu du simulateur, Features → Network Link Conditioner (un outil à télécharger sur le site des développeurs) permet de simuler de la 3G, de la forte latence — et de débusquer les expériences « qui tournent en rond un temps fou ».

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Astuce : la requête se prend ATS ?

{class="mt-1"}
Si la requête déclenche une erreur "App Transport Security" dès l'envoi, c'est très probablement une adresse http:// en clair. Les API officielles doivent être en HTTPS ; pour le débogage local, ouvre une exception temporaire (NSAllowsLocalNetworking dans Info.plist) et pense à tout nettoyer avant la mise en boutique.
:::

{class="mt-1"}
① La recherche météo marche normalement ; ② réseau coupé, l'App affiche l'erreur avec élégance sans planter (teste en coupant le réseau du Mac depuis le simulateur !) ; ③ une ville inexistante déclenche un message aimable ; ④ deux villes favorites sont encore là après redémarrage de l'App ; ⑤ en mode sombre, l'interface ne brûle pas les yeux. Les cinq points passés, le projet est bon pour la remise des diplômes.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Résumé du chapitre

- Essaie d'abord l'API dans le navigateur, comprends le JSON, ensuite seulement écris le code — le « devoir préparatoire » n'est jamais une perte
- La clé d'API cachée dans le xcconfig, jamais dans le dépôt de code
- Modèle Codable + URLSession async/await : champs concordants, le JSON s'analyse tout seul
- Le triptyque d'états loading/success/error, le passe-partout des interfaces connectées
- Réseau coupé, saisie vide, ville inexistante — bien traiter les erreurs est la note de passage d'une App connectée
:::
