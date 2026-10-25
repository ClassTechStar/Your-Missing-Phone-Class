---
id: di-wu-shi-san-zhang
num: 53
part: an-zhuo-kai-fa-pian
nav: Chapitre 53 : Stockage des données et requêtes réseau
toc: default
kind: chapter
---

### Chapitre 53 : Stockage des données et requêtes réseau

{class="chapter-intro mb-4"}
Une app qui ne sait que « montrer » est morte ; une app qui sait stocker des données et se connecter au réseau vit. Ce chapitre te fait connaître le « trio » de la couche données d'Android : DataStore (les petits réglages), Room (les données structurées), Retrofit (le dialogue avec le serveur), sans oublier leur « chef d'orchestre » — les coroutines. Ce chapitre digéré, tu sauras écrire de vraies apps qui mémorisent les habitudes de l'utilisateur et mettent leur contenu à jour en temps réel.

#### 1. Choisir la solution de stockage : commence par ce tableau

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Solution</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ce qu'elle convient de stocker</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Caractéristiques</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Où ce livre l'emploie</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DataStore</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Réglages épars (thème, interrupteurs)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Paires clé-valeur, simple et sûr</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Les réglages du carnet de comptes, chapitre 54</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Données structurées (écritures, utilisateurs)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Une vraie encapsulation de base de données SQLite, interrogeable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Les écritures du carnet de comptes, chapitre 54</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Données du serveur (pas de stockage, récupérées en ligne)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">La norme de facto des bibliothèques de requêtes HTTP</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Les données météo, chapitre 55</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
La répartition du travail au sein du trio de données

Grave ce refrain : « les petits réglages vont dans DataStore, les données en série vont dans Room, les données d'ailleurs passent par Retrofit ». Les SharedPreferences des anciens tutos ont été remplacées par DataStore, et le SQL écrit à la main pour SQLite a cédé la place à Room — apprends directement le nouveau, ne prends pas les vieilles routes.

#### 2. DataStore : ranger les petits réglages

Pour mémoriser des valeurs éparses comme « la devise choisie la dernière fois » ou « le mode sombre est-il activé », utilise DataStore (version Preferences) :

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Exemple avec DataStore</span><span class="dots">···</span>
:::

```
val Context.dataStore by preferencesDataStore(name = "settings")

// écrire : stocker une valeur
suspend fun saveTheme(isDark: Boolean) {
    context.dataStore.edit { prefs ->
        prefs[THEME_KEY] = isDark
    }
}

// lire : récupérer (Flow notifie automatiquement les changements)
val themeFlow: Flow<Boolean> = context.dataStore.data
    .map { it[THEME_KEY] ?: false }
```
:::

Note que ce qui est renvoyé est un Flow — un flux de données qui « coule ». Dès que la valeur change, tous les endroits qui l'observent reçoivent automatiquement la nouvelle. Ce concept (le réactif) est la pierre angulaire de l'Android moderne ; tu le mettras en pratique au chapitre 54.

#### 3. Room : offrir aux données une « vraie maison »

Un carnet de comptes accumule des centaines, voire des milliers d'écritures, avec des requêtes et des statistiques par catégorie et par mois — il faut une base de données. Room est l'encapsulation officielle de SQLite : créer des tables et interroger des données devient aussi naturel qu'écrire du Kotlin. Trois ingrédients :

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Le trio de Room : Entity / Dao / Database</span><span class="dots">···</span>
:::

```
// 1. Entity : la structure de table (une table = un data class)
@Entity(tableName = "records")
data class Record(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val amount: Double,
    val category: String,
    val note: String,
    val date: String
)

// 2. Dao : l'interface d'opérations (ajout, suppression, modification, lecture)
@Dao
interface RecordDao {
    @Query("SELECT * FROM records ORDER BY date DESC")
    fun getAll(): Flow<List<Record>>

    @Insert
    suspend fun insert(record: Record)

    @Delete
    suspend fun delete(record: Record)

    @Query("SELECT SUM(amount) FROM records WHERE category = :c")
    suspend fun sumByCategory(c: String): Double
}

// 3. Database : l'assemblage final
@Database(entities = [Record::class], version = 1)
abstract class AppDatabase : RoomDatabase() {
    abstract fun recordDao(): RecordDao
}
```
:::

Ce modèle « en trois pièces » se glisse tel quel dans n'importe lequel de tes projets — change juste les noms des champs. Les requêtes renvoient un Flow et l'interface se rafraîchit automatiquement au gré des données : un enchantement.

#### 4. Retrofit : parler au serveur

Météo, actualités, taux de change… ces données ne sont pas dans le téléphone, elles sont sur le serveur de quelqu'un d'autre. Retrofit rend « demander des données au serveur » aussi simple qu'appeler une fonction. En trois étapes :

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Retrofit en trois étapes</span><span class="dots">···</span>
:::

```
// 1. définir l'interface : décrire les requêtes HTTP comme des fonctions
interface WeatherApi {
    @GET("v1/weather")
    suspend fun getWeather(@Query("city") city: String): WeatherResponse
}

// 2. créer l'instance
val api = Retrofit.Builder()
    .baseUrl("https://api.example.com/")
    .addConverterFactory(GsonConverterFactory.create())
    .build()
    .create(WeatherApi::class.java)

// 3. appeler comme une fonction (dans une coroutine)
val result = api.getWeather("Paris")
```
:::

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Piège à éviter : les deux lois d'airain du réseau

{class="mt-1"}
① Jamais de requête réseau sur le thread principal — l'interface se figerait, voire planterait (NetworkOnMainThreadException). Tout appel réseau doit passer par une coroutine (viewModelScope.launch). ② Le HTTP en clair est interdit par défaut : depuis Android 9, HTTPS est exigé. En test, si tu dois utiliser une adresse locale en http://, déclare explicitement usesCleartextTraffic dans le Manifest — mais un vrai produit doit passer intégralement par HTTPS.
:::

#### 5. Analyser le JSON : « traduire » les données du réseau

Les données renvoyées par le serveur sont pour l'essentiel du JSON — un texte ressemblant à un « dictionnaire imbriqué ». Retrofit a besoin d'un « interprète » pour le convertir en objets Kotlin. Les deux solutions dominantes en 2026 :

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Solution</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Caractéristiques</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Cas d'usage recommandé</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gson / Moshi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">La solution historique par réflexion, configuration sans coût</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Les petits projets à démarrage rapide et à peu de champs</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">kotlinx.serialization</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">La solution officielle à la compilation, plus rapide et plus sûre</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Le premier choix des nouveaux projets (dominant en 2026)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Les deux grandes solutions d'analyse JSON

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Exemple avec kotlinx.serialization</span><span class="dots">···</span>
:::

```
// annote le data class avec @Serializable
@Serializable
data class WeatherResponse(
    val weather: List<Weather>,
    val main: Main,
    val name: String
)

// on branche sur Retrofit le Converter correspondant (exemple avec le support officiel de Retrofit 2.11+) :
// .addConverterFactory(json.asConverterFactory("application/json".toMediaType()))
```
:::

Quelle que soit la solution, la loi d'airain reste : observe d'abord le JSON réellement renvoyé, définis ensuite les champs. Bien des bugs d'« échec d'analyse » viennent d'un nom de champ mal orthographié ou d'un niveau d'imbrication deviné à tort — affiche le JSON brut et compare : dix secondes suffisent pour localiser le problème.

#### 6. Les coroutines : la « langue commune » de la concurrence Android

Les suspend et launch vus plus haut viennent des coroutines Kotlin (Coroutine) — la solution officielle de concurrence d'Android. Tu peux le comprendre grossièrement ainsi : faire en sorte que les opérations « qui demandent d'attendre un peu » (réseau, base de données) ne bloquent pas l'interface.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Premières corroutines</span><span class="dots">···</span>
:::

```
// démarre une coroutine dans le ViewModel
viewModelScope.launch {
    val records = dao.getAll().first()  // suspend : se suspend et attend automatiquement
    // mettre à jour l'état de l'interface…
}

// pense-bête des mots-clés :
// suspend   —— "je dois attendre, ne bloquez pas les autres"
// launch    —— "au travail !"
// viewModelScope —— l'"atelier" qui suit l'écran ; il se replie tout seul quand l'écran est détruit
```
:::

En tant que grand débutant, retiens d'abord l'usage ; le principe sous-jacent de « suspension et reprise » pourra attendre. Au quotidien, 90 % de ce que tu écriras suivra ce modèle.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
À toi de jouer : une petite app « une phrase par jour »

{class="mt-1"}
Trouve une API de citations gratuite (hitokoto ou similaire), tire « la phrase du jour » avec Retrofit, affiche-la au centre de l'écran et ajoute un bouton « une autre » (nouvelle requête dans une coroutine). Range ensuite tes phrases préférées dans un « favoris » avec Room. Cet exercice mobilise DataStore, Room, Retrofit et les coroutines — une fois fait, les chapitres 7 et 8 seront un jeu d'enfant.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Résumé du chapitre

- Le refrain : les petits réglages dans DataStore, les données en série dans Room, les données d'ailleurs via Retrofit
- DataStore renvoie un Flow : dès que la valeur change, les observateurs la reçoivent automatiquement
- Le trio Room : @Entity (la table) + @Dao (les opérations) + @Database (l'assemblage final), modèle réutilisable tel quel
- Retrofit en trois étapes : définir l'interface → créer l'instance → appeler dans une coroutine
- Deux lois d'airain : pas de réseau sur le thread principal ; HTTPS obligatoire pour un vrai produit
- Coroutine = une attente qui ne bloque pas l'interface ; viewModelScope est l'atelier réservé de l'écran
:::
