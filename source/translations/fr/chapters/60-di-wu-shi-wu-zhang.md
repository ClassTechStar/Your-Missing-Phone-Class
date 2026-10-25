---
id: di-wu-shi-wu-zhang
num: 55
part: an-zhuo-kai-fa-pian
nav: Chapitre 55 : Projet 2 — App météo (version réseau)
toc: default
kind: chapter
---

### Chapitre 55 : Projet 2 — L'app météo (version réseau)

{class="chapter-intro mb-4"}
Le carnet de comptes faisait « travailler les fondamentaux », l'app météo « ouvre sur le monde » — elle dialogue avec Internet. Ce projet t'apprendra : demander une API gratuite, analyser du JSON, gérer les trois états d'interface « chargement/succès/échec » et bien cacher ta clé d'API. Une fois terminé, tu seras capable de créer n'importe quelle app « connectée » — actualités, taux de change, traduction : la recette est exactement la même.

#### 1. Demander une API météo gratuite

Pour t'entraîner en solo, je recommande OpenWeatherMap ou le service chinois QWeather — les deux offrent un quota gratuit, utilisable dès l'inscription. Prenons OpenWeatherMap en exemple :

1. Crée un compte → sur la page API keys, génère une clé (apikey) ;
2. la version gratuite permet d'appeler l'interface Current Weather (météo actuelle) : api.openweathermap.org/data/2.5/weather? q=beijing&appid=taCle&units=metric ;
3. fais d'abord un essai dans le navigateur pour voir à quoi ressemble le JSON renvoyé — c'est le « devoir de préparation » obligatoire avant de brancher n'importe quelle API.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Piège à éviter : jamais de clé codée en dur dans le code

{class="mt-1"}
Une clé d'API équivaut au « mot de passe de ton portefeuille » : si tu la mets dans le code et pousse le tout sur GitHub, des robots la récupéreront et l'épuiseront en quelques heures. La bonne méthode : range-la dans local.properties (fichier déjà ignoré par le gitignore), puis lis-la dans le code via le buildConfig de Gradle. Cherche « meilleures pratiques pour masquer une clé d'API sur Android » et suis la démarche.
:::

#### 2. La couche réseau : Retrofit + analyse JSON

Définis d'abord le « modèle de données » d'après le JSON renvoyé par l'API ; ignore tout champ qui ne correspond pas :

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Modèle de données + interface</span><span class="dots">···</span>
:::

```
// JSON: {"weather":[{"description":"Ensoleillé"}],"main":{"temp":26.5,"humidity":40},"name":"Paris"}
data class WeatherResponse(
    val weather: List&lt;Weather&gt;,
    val main: Main,
    val name: String
)
data class Weather(val description: String)
data class Main(val temp: Double, val humidity: Int)

interface WeatherApi {
    @GET("data/2.5/weather")
    suspend fun getWeather(
        @Query("q") city: String,
        @Query("appid") key: String,
        @Query("units") metric: String = "metric",
        @Query("lang") lang: String = "zh_cn"
    ): WeatherResponse
}
```
:::

Gson remplit tout seul ces data class avec le JSON — noms de champs concordants, la magie opère d'elle-même.

#### 3. Les trois états d'interface : chargement / succès / échec

L'âme d'une app connectée, c'est la « gestion des états ». Réseau lent, hors ligne, nom de ville mal orthographié… chaque cas doit être expliqué à l'utilisateur par l'interface. Représente-les élégamment avec une sealed class (classe scellée) :

::: div .code-block
:::inline div .code-head
<span>KOTLIN · État de l'interface</span><span class="dots">···</span>
:::

```
sealed class UiState {
    object Loading : UiState()                    // chargement
    data class Success(val data: WeatherResponse) : UiState()  // succès
    data class Error(val message: String) : UiState()          // échec
}

// dans le ViewModel :
fun search(city: String) {
    viewModelScope.launch {
        _state.value = UiState.Loading
        _state.value = try {
            UiState.Success(api.getWeather(city))
        } catch (e: Exception) {
            UiState.Error("Ville introuvable, essaies un autre nom ?")
        }
    }
}

// dans l'interface :
when (val s = state) {
    is UiState.Loading -&gt; CircularProgressIndicator()   // roue de chargement
    is UiState.Success -&gt; WeatherContent(s.data)        // affiche
    is UiState.Error -&gt; Text(s.message)                 // affiche l'erreur
}
```
:::

Ce triptyque Loading/Success/Error est le « modèle passe-partout » des interfaces connectées : apprends-le par cœur, et tu le déclineras pour toutes tes futures apps en ligne.

#### 4. Le code d'interface en conditions réelles : dessiner la météo

Les états sont là ; voici à quoi ressemble l'interface (extraits clés) :

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Écran météo (extrait clé)</span><span class="dots">···</span>
:::

```
@Composable
fun WeatherContent(data: WeatherResponse) {
    Column(
        Modifier.fillMaxSize().padding(24.dp),
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Text(data.name, fontSize = 28.sp, fontWeight = FontWeight.Bold)
        Text(
            "${data.main.temp}°C",
            fontSize = 72.sp,
            fontWeight = FontWeight.Light
        )
        Text(
            data.weather.firstOrNull()?.description ?: "Inconnu",
            fontSize = 20.sp,
            color = Color.Gray
        )
        Spacer(Modifier.height(16.dp))
        Row {
            Text("💧 Humidité ${data.main.humidity}%")
            Spacer(Modifier.width(24.dp))
            Text("🌡️ Ressenti ${data.main.temp}°C")
        }
    }
}
```
:::

Quelques détails qui valent la leçon : firstOrNull() prend le premier élément sans risque (la liste peut être vide) et ?: "Inconnu" fournit le texte de repli — le principe de null safety vaut aussi dans l'interface. La température s'affiche en grande taille 72.sp pour imposer sa présence, et la graisse « légère » (Light) rend le chiffre élégant : c'est la recette classique des apps météo.

#### 5. Détails d'interface et d'interaction

- La zone de recherche : un TextField en haut, tu tapes le nom de la ville et tu lances la recherche (action « Recherche » sur le clavier, Entrée pour chercher) ;
- La carte météo : température en grand format (26,5°), description du temps (clair), humidité, nom de la ville ;
- Les villes favorites : range tes villes consultées souvent dans DataStore, et elles seront recherchées automatiquement à la prochaine ouverture — au passage, révision du chapitre 6 ;
- Tirer pour actualiser : dans Compose, utilise PullToRefreshBox (fourni par Material 3) et la sensation devient tout de suite « professionnelle ».

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Astuce : les images donnent vie à l’interface

{class="mt-1"}
Associe un emoji ou une icône à chaque type de temps (☀️🌧️❄️) via when(description) — trois lignes de code, et l’interface gagne doublement en chaleur. Tu peux aussi charger une bibliothèque d’icônes météo tierce, mais pour t’entraîner, les emoji suffisent.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
À toi de jouer : la liste de contrôle de l’app météo

{class="mt-1"}
① La recherche météo fonctionne normalement ; ② réseau coupé, l’app affiche une erreur élégante sans planter (teste en mode avion !) ; ③ une ville inexistante saisie déclenche un message sympathique ; ④ deux villes mises en favori sont toujours là après redémarrage de l’app ; ⑤ la rotation de l’écran ne fait rien perdre. Les cinq points validés, et le projet est diplômé.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Résumé du chapitre

- Teste d’abord l’API dans le navigateur et comprends le JSON avant d’écrire le code — « préparer le terrain » n’est jamais du temps perdu
- Cache la clé API dans local.properties, jamais dans le dépôt de code
- Interface Retrofit + data class : les champs correspondent, le JSON est analysé automatiquement
- L’état en trois phases Chargement/Succès/Erreur est la solution passe-partout des interfaces connectées
- Réseau coupé, saisie vide, ville inexistante — la gestion des erreurs est la note de passage d’une app connectée
:::
