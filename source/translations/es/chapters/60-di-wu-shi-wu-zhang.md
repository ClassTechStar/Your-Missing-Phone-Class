---
id: di-wu-shi-wu-zhang
num: 55
part: an-zhuo-kai-fa-pian
nav: Capítulo 55: Proyecto 2: app del tiempo (versión en red)
toc: default
kind: chapter
---

### Capítulo 55: Proyecto 2: app del tiempo (versión en red)

{class="chapter-intro mb-4"}
La app de gastos era "forjar el fondo"; la del tiempo es "ver mundo": tiene que entenderse con internet. En este proyecto aprenderás a pedir una API gratuita, a parsear JSON, a llevar los tres estados de interfaz "cargando/éxito/error" y a esconder bien la clave de la API. Al acabarlo tendrás la capacidad de hacer cualquier "app conectada": noticias, divisas, traducción; la receta es idéntica.

#### 1. Pedir una API de tiempo gratuita

Para practicar en casa van bien OpenWeatherMap o, en China, QWeather (HeFeng); ambas tienen cuota gratuita y funcionan al registrarte. Tomemos OpenWeatherMap como ejemplo:

1. Crea una cuenta → genera una Key (apikey) en la página API keys;
2. El plan gratuito permite llamar al endpoint Current Weather (tiempo actual): api.openweathermap.org/data/2.5/weather? q=beijing&appid=TU_CLAVE&units=metric;
3. Pruébalo primero en el navegador para ver cómo es el JSON que devuelve: es la "lección previa" obligatoria antes de enchufarte a cualquier API.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Aviso para esquivar problemas: la clave jamás clavada en el código

{class="mt-1"}
La API Key equivale a "la contraseña de tu cartera": la escribes en el código, lo subes a GitHub y en cuestión de horas los crawlers la barren y te la gastan. Lo correcto: meterla en local.properties (un archivo que gitignore ya ignora) y leerla en el código a través del buildConfig de Gradle. Busca "Android hide API key best practices" y sigue los pasos.
:::

#### 2. La capa de red: Retrofit + parseo de JSON

Define primero el "modelo de datos" según el JSON que devuelve la API; los campos que no encajen, ignóralos sin más:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Modelo de datos + interfaz</span><span class="dots">···</span>
:::

```
// JSON: {"weather":[{"description":"Despejado"}],"main":{"temp":26.5,"humidity":40},"name":"Madrid"}
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

Gson meterá el JSON solo dentro de esas data class: si los nombres de campo coinciden, la magia ocurre sola.

#### 3. Los tres estados de interfaz: cargando / éxito / error

El alma de una app conectada está en la "gestión de estados". Red lenta, sin conexión, nombre de ciudad mal escrito... ante cada caso la interfaz debe dar la cara y explicarse. Una forma elegante de representarlo es un sealed class (clase sellada):

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Estado de la interfaz</span><span class="dots">···</span>
:::

```
sealed class UiState {
    object Loading : UiState()                    // cargando
    data class Success(val data: WeatherResponse) : UiState()  // éxito
    data class Error(val message: String) : UiState()          // fallo
}

// en el ViewModel:
fun search(city: String) {
    viewModelScope.launch {
        _state.value = UiState.Loading
        _state.value = try {
            UiState.Success(api.getWeather(city))
        } catch (e: Exception) {
            UiState.Error("No encuentro esa ciudad, ¿pruebas con otro nombre?")
        }
    }
}

// en la interfaz:
when (val s = state) {
    is UiState.Loading -&gt; CircularProgressIndicator()   // rueda de carga
    is UiState.Success -&gt; WeatherContent(s.data)        // muestra
    is UiState.Error -&gt; Text(s.message)                 // muestra el error
}
```
:::

Este esquema en tres tramos Loading/Success/Error es la "plantilla todoterreno" de las interfaces conectadas: apréndetela de memoria y, a partir de ahora, calca el molde en todas tus apps conectadas.

#### 4. Código de interfaz en la práctica: dibujar el tiempo

Con el estado listo, la interfaz queda así (fragmentos clave):

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Pantalla del tiempo (fragmento clave)</span><span class="dots">···</span>
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
            data.weather.firstOrNull()?.description ?: "Desconocido",
            fontSize = 20.sp,
            color = Color.Gray
        )
        Spacer(Modifier.height(16.dp))
        Row {
            Text("💧 Humedad ${data.main.humidity}%")
            Spacer(Modifier.width(24.dp))
            Text("🌡️ Sensación ${data.main.temp}°C")
        }
    }
}
```
:::

Detalles que valen la pena aprender: firstOrNull() coge el primer elemento sin riesgo (la lista puede estar vacía) y ?: "desconocido" aporta el texto de reserva; el principio de seguridad frente a nulos manda igual en la interfaz. La temperatura presume con un tamaño grande de 72.sp y el peso "Light" da elegancia a las cifras: es la receta clásica de las apps del tiempo.

#### 5. Detalles de interfaz e interacción

- Cuadro de búsqueda: un TextField arriba, escribes el nombre de la ciudad y pulsas buscar (configura la acción "Buscar" en el teclado: enter y busca);
- Tarjeta del tiempo: temperatura en letra grande (26,5°), descripción del tiempo (despejado), humedad y nombre de la ciudad;
- Ciudades favoritas: guarda las que consultas a menudo en DataStore y la próxima vez que abras la app se consultan solas; de regalo, repaso del capítulo 6;
- Deslizar para actualizar: en Compose usa PullToRefreshBox (lo trae Material 3) y la sensación pasa a "profesional" al instante.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Consejo: las imágenes dan vida a la interfaz

{class="mt-1"}
Asigna a cada tipo de tiempo un emoji o icono (☀️🌧️❄️) mapeándolos con when(description): tres líneas de código y la "temperatura humana" de la interfaz se duplica. También puedes cargar una biblioteca de iconos del tiempo de terceros, pero en la etapa de práctica bastan los emojis.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Manos a la obra: la lista de comprobación de la app del tiempo

{class="mt-1"}
① La búsqueda del tiempo funciona con normalidad; ② corta la red y la app avisa con elegancia sin cerrarse (¡pruébalo en modo avión!); ③ tecleas una ciudad que no existe y avisa con amabilidad; ④ guardas dos ciudades favoritas y siguen ahí al reiniciar la app; ⑤ girar la pantalla no pierde el estado. Con las cinco superadas, este proyecto se gradúa.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumen del capítulo

- Prueba la API en el navegador y entiende el JSON antes de escribir código: la "lección previa" nunca sale cara
- La API Key se esconde en local.properties y jamás entra al repositorio de código
- Interfaz de Retrofit + data class: si los campos encajan, el JSON se parsea solo
- El esquema en tres estados Loading/Success/Error es el todoterreno de las interfaces conectadas
- Sin red, entrada vacía, ciudad inexistente: manejar errores es la nota mínima de una app conectada
:::
