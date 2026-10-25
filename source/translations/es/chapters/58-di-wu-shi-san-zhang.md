---
id: di-wu-shi-san-zhang
num: 53
part: an-zhuo-kai-fa-pian
nav: Capítulo 53: Guardar datos y pedir cosas a la red
toc: default
kind: chapter
---

### Capítulo 53: Guardar datos y pedir cosas a la red

{class="chapter-intro mb-4"}
Una app que solo "mira" está muerta; la que guarda datos y se conecta a la red vive de verdad. En este capítulo conocerás el "trío" de la capa de datos de Android: DataStore (ajustes pequeños), Room (datos estructurados) y Retrofit (hablar con el servidor), más su "coordinador general", las corrutinas. Al acabarlo podrás escribir apps de verdad que recuerdan los hábitos del usuario y refrescan contenido en vivo.

#### 1. Cómo elegir dónde guardar: mira primero esta tabla

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Opción</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Qué conviene guardar</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Características</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Dónde se usa en este libro</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DataStore</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ajustes sueltos (tema, interruptores)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pares clave-valor, sencillo y seguro</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Los ajustes de la app de gastos del capítulo 54</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Datos estructurados (movimientos, usuarios)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Envoltura real de una base de datos SQLite, con consultas</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Los movimientos del capítulo 54</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">(no se guarda: se trae de la red) Datos del servidor</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">El estándar de facto de las bibliotecas de peticiones HTTP</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Los datos del tiempo del capítulo 55</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Reparto de tareas del trío de datos

Grábate esta regla: "los ajustes pequeños van a DataStore, los datos en bloque van a Room y los datos de fuera viajan por Retrofit". SharedPreferences, tan visto en tutoriales viejos, ya fue reemplazado por DataStore, y el SQL a mano sobre SQLite también cedió el puesto a Room: aprende directo lo nuevo y no tomes el camino viejo.

#### 2. DataStore: guardar ajustes pequeños

Para recordar valores sueltos como "la moneda que eligió el usuario la última vez" o "si está activado el modo oscuro", usa DataStore (versión Preferences):

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Ejemplo con DataStore</span><span class="dots">···</span>
:::

```
val Context.dataStore by preferencesDataStore(name = "settings")

// escribir: guardar un valor
suspend fun saveTheme(isDark: Boolean) {
    context.dataStore.edit { prefs ->
        prefs[THEME_KEY] = isDark
    }
}

// leer: sacar el valor (Flow avisa solo de los cambios)
val themeFlow: Flow<Boolean> = context.dataStore.data
    .map { it[THEME_KEY] ?: false }
```
:::

Fíjate en que devuelve un Flow, un flujo de datos que "fluye". En cuanto el valor cambia, todos los puntos que lo observan reciben el nuevo valor sin que nadie les avise. Ese concepto (reactividad) es la piedra angular del Android moderno y lo llevarás a la práctica en el capítulo 54.

#### 3. Room: dar a los datos "casa propia"

La app de gastos acumula cientos o miles de apuntes y necesita consultar y resumir por categoría y por mes: eso pide una base de datos. Room es la envoltura oficial de SQLite y deja "crear tablas y consultar" tan natural como escribir Kotlin. Son tres piezas:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · El trío de Room: Entity / Dao / Database</span><span class="dots">···</span>
:::

```
// 1. Entity: la estructura de la tabla (una tabla = un data class)
@Entity(tableName = "records")
data class Record(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val amount: Double,
    val category: String,
    val note: String,
    val date: String
)

// 2. Dao: la interfaz de operaciones (alta, baja, cambio, consulta)
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

// 3. Database: el ensamblaje final
@Database(entities = [Record::class], version = 1)
abstract class AppDatabase : RoomDatabase() {
    abstract fun recordDao(): RecordDao
}
```
:::

Esta plantilla del "trío" puede mudarse tal cual a cualquiera de tus proyectos: basta con cambiar los nombres de los campos. Las consultas devuelven Flow y la interfaz se refresca al compás de los datos; no tiene precio.

#### 4. Retrofit: hablar con el servidor

El tiempo, las noticias, los tipos de cambio... esos datos no viven en el móvil, sino en servidores ajenos. Retrofit deja pedir datos al servidor tan fácil como llamar a una función. Tres pasos:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Retrofit en tres pasos</span><span class="dots">···</span>
:::

```
// 1. definir la interfaz: describe las peticiones HTTP como funciones
interface WeatherApi {
    @GET("v1/weather")
    suspend fun getWeather(@Query("city") city: String): WeatherResponse
}

// 2. crear la instancia
val api = Retrofit.Builder()
    .baseUrl("https://api.example.com/")
    .addConverterFactory(GsonConverterFactory.create())
    .build()
    .create(WeatherApi::class.java)

// 3. llamar como si fuera una función (dentro de una corrutina)
val result = api.getWeather("Madrid")
```
:::

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Aviso para esquivar problemas: dos leyes de hierro de la red

{class="mt-1"}
① Las peticiones de red jamás en el hilo principal: congelarían la interfaz o provocarían un cierre (NetworkOnMainThreadException). Toda llamada de red debe ir dentro de una corrutina (viewModelScope.launch). ② El HTTP en claro está prohibido por defecto: desde Android 9 se exige HTTPS. Si en pruebas necesitas una dirección local http://, tendrás que declarar usesCleartextTraffic a mano en el Manifest; pero un producto real debe ir todo por HTTPS.
:::

#### 5. Parsear JSON: "traducir" los datos de la red

La mayor parte de los datos que devuelve el servidor llega en JSON, un texto parecido a "diccionarios anidados". Retrofit necesita un "intérprete" que lo convierta en objetos de Kotlin. Las dos opciones mayores de 2026:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Opción</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Características</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Escenario recomendado</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gson / Moshi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">El veterano basado en reflexión, con coste de configuración cero</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Proyectos pequeños de arranque rápido y con pocos campos</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">kotlinx.serialization</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">La opción oficial en tiempo de compilación, más rápida y segura</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Primera opción para proyectos nuevos (la corriente de 2026)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Las dos grandes opciones para parsear JSON

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Ejemplo con kotlinx.serialization</span><span class="dots">···</span>
:::

```
// anota el data class con @Serializable
@Serializable
data class WeatherResponse(
    val weather: List<Weather>,
    val main: Main,
    val name: String
)

// Retrofit se le acopla el Converter correspondiente (ejemplo con el soporte oficial de Retrofit 2.11+):
// .addConverterFactory(json.asConverterFactory("application/json".toMediaType()))
```
:::

Con cualquiera de las dos, la ley es la misma: mira primero el JSON real que llega y define los campos después. Muchos bugs de "fallo de parseo" vienen de nombres de campo mal escritos o de niveles de anidamiento mal adivinados; imprime el JSON en crudo y coteja: en diez segundos lo tienes.

#### 6. Corrutinas: el "idioma común" de la concurrencia en Android

Los suspend y launch que han ido saliendo arriba vienen de las corrutinas de Kotlin (Coroutine), la solución oficial de concurrencia de Android. Puedes entenderlo a lo burro así: hace que las operaciones "que obligan a esperar" (red, base de datos) no bloqueen la interfaz.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Primer contacto con las corrutinas</span><span class="dots">···</span>
:::

```
// arranca una corrutina dentro del ViewModel
viewModelScope.launch {
    val records = dao.getAll().first()  // suspend: se suspende y espera automáticamente
    // actualizar el estado de la interfaz…
}

// chuleta de palabras clave:
// suspend   —— "tengo que esperar, no bloquee a los demás"
// launch    —— "¡al trabajo!"
// viewModelScope —— el "taller" que sigue a la pantalla; se recoge solo al destruirse esta
```
:::

Si partes de cero, con memorizar el uso basta; la teoría de "suspender y reanudar" que hay detrás puede esperar. El 90 % de lo que escribirás a diario sigue esta plantilla.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Manos a la obra: crea una mini app de "frase del día"

{class="mt-1"}
Busca una API de frases gratuita (algo tipo hitokoto), usa Retrofit para traer la "frase del día" y muéstrala en el centro de la pantalla, con un botón "Otra" que vuelva a pedir dentro de una corrutina. Después guarda las frases que te gusten en "favoritos" con Room. Este ejercicio pasa por DataStore/Room/Retrofit/corrutinas de arriba abajo; terminado, los capítulos 7 y 8 serán pan comido.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumen del capítulo

- La regla: ajustes pequeños a DataStore, datos en bloque a Room, datos de fuera por Retrofit
- DataStore devuelve un Flow: si el valor cambia, los observadores lo reciben solos
- El trío de Room: @Entity (tabla) + @Dao (operaciones) + @Database (montaje final); la plantilla se recicla tal cual
- Retrofit en tres pasos: definir la interfaz → crear la instancia → llamar dentro de una corrutina
- Dos leyes de hierro: la red jamás en el hilo principal; producto real, siempre HTTPS
- Corrutina = esperar sin bloquear la interfaz; viewModelScope es el taller exclusivo de cada pantalla
:::
