---
id: di-liu-shi-liu-zhang
num: 66
part: ios-kai-fa-pian
nav: Capítulo 66: Proyecto 2 — app del tiempo (versión conectada)
toc: default
kind: chapter
---

### Capítulo 66: Proyecto 2 — app del tiempo (versión conectada)

{class="chapter-intro mb-4"}
La libreta de cuentas era «entrenar en casa»; la app del tiempo es «salir al mundo»: tiene que entenderse con internet. En este proyecto aprenderás a pedir una API gratuita, interpretar JSON, manejar los tres estados de interfaz «cargando / éxito / fallo» y guardar bien la clave de la API. Al terminarlo tendrás lo necesario para hacer cualquier «app conectada»: noticias, divisas, traducción… el método es idéntico.

#### 1. Pedir una API gratuita del tiempo

Para practicar a nivel personal, te recomiendo OpenWeatherMap o la china QWeather: ambas tienen cuota gratuita y funcionan nada más registrarte. Con OpenWeatherMap como ejemplo:

1. Regístrate → en la página API keys genera una clave (apikey);
2. La versión gratuita puede llamar al endpoint Current Weather: api.openweathermap.org/data/2.5/weather? q=beijing&appid=TU_CLAVE&units=metric;
3. Pruébalo primero en el navegador para ver qué pinta tiene el JSON que devuelve: es la «tarea previa» obligatoria antes de conectar cualquier API.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Para evitar tropiezos: la clave jamás va incrustada en el código

{class="mt-1"}
La clave de la API es como «la contraseña de tu cartera»: si la metes en el código y lo subes a GitHub, en cuestión de horas los rastreadores la habrán recogido para gastar a tu costa. La forma correcta en iOS: guárdala en un Config.xcconfig (archivo de configuración, ya ignorado por gitignore) y léela en el código a través de Info.plist. Busca «gestionar claves con xcconfig en iOS» y sigue los pasos.
:::

#### 2. La capa de red: URLSession + Codable

Primero define el modelo según el JSON que devuelve la API y luego escribe el servicio:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Modelo de datos + servicio</span><span class="dots">···</span>
:::

```
// JSON: {"weather":[{"description":"Despejado"}],"main":{"temp":26.5,"humidity":40},"name":"Madrid"}
struct WeatherResponse: Codable {
    let weather: [Weather]
    let main: Main
    let name: String
}
struct Weather: Codable { let description: String }
struct Main: Codable { let temp: Double; let humidity: Int }

struct WeatherService {
    let key: String   // se lee de xcconfig

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

#### 3. Los tres estados de interfaz: cargando / éxito / fallo

El alma de una app conectada está en la «gestión de estados». Red lenta, sin conexión, nombre de ciudad mal escrito… en cada caso la interfaz debe dar cuentas al usuario. Se expresa con elegancia con enum + switch:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Estado de la interfaz</span><span class="dots">···</span>
:::

```
enum LoadState {
    case loading                  // cargando
    case success(WeatherResponse) // éxito
    case error(String)            // fallo
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
            state = .error("No encuentro esa ciudad, ¿pruebas con otro nombre?")
        }
    }
}

// en la interfaz:
switch vm.state {
case .loading: ProgressView("Cargando…")
case .success(let d): WeatherContent(data: d)
case .error(let msg): Text(msg).foregroundColor(.secondary)
}
```
:::

Este esquema de tres tramos loading/success/error es la «plantilla todoterreno» de las interfaces conectadas: apréndetelo primero y luego copia el molde en todas tus apps con red.

#### 4. Código de interfaz en acción: dibujar el tiempo

::: div .code-block
:::inline div .code-head
<span>SWIFT · Pantalla del tiempo (fragmento clave)</span><span class="dots">···</span>
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
            Text(data.weather.first?.description ?? "Desconocido")
                .font(.title3)
                .foregroundColor(.secondary)
            HStack(spacing: 24) {
                Label("Humedad \(data.main.humidity)%", systemImage: "humidity")
                Label("Sensación \(Int(data.main.temp))°C", systemImage: "thermometer")
            }
        }
        .padding()
    }
}
```
:::

Hay detalles que merece la pena aprender: first? toma el primer elemento con seguridad (la lista puede estar vacía) y ?? "Desconocido" pone el texto de reserva; la temperatura en peso fino y tamaño 76 es la receta clásica de las apps del tiempo; y Label es el componente oficial de «icono + texto», más correcto que montar un HStack a mano.

#### 5. Detalles de interacción y ciudades favoritas

- Buscador: el modificador .searchable arriba, con la interacción de búsqueda del sistema; al enviar, llama a vm.search;
- Ciudades favoritas: guarda las ciudades que miras a menudo en UserDefaults y la próxima vez se consultan solas al abrir;
- Tirar para actualizar: .refreshable { await vm.search(...) } lo arregla en una línea;
- Iconos del tiempo: usa Image(systemName:) mapeando por descripción (sun.max / cloud.rain / snowflake) y la interfaz cobra vida al instante.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Consejo: la peculiaridad de los nombres de ciudades en chino

{class="mt-1"}
OpenWeatherMap no se entiende demasiado bien con los nombres de ciudades en chino: buscar «Beijing» en chino puede no dar resultados mientras que "beijing" sí funciona. Lo que haría un producto de verdad es incluir una tabla de equivalencias «nombre de ciudad → inglés/coordenadas», o conectar con un servicio chino del tiempo. En la fase de práctica basta con soportar nombres en pinyin o inglés; no te pelees con ello.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Manos a la obra: lista de comprobación de la app del tiempo

#### 6. Cómo depurar las peticiones de red: imprimir, capturar el tráfico y simular red lenta

Cuando una app conectada falla, nueve de cada diez veces es porque «la petición no se envió bien» o «la respuesta no se interpretó bien». Tres herramientas de depuración:

1. Imprimir los datos crudos: imprime String(data: data, encoding: .utf8) para ver el JSON original: nombres de campos y tipos a simple vista, diez veces más rápido que adivinar;
2. Herramientas de captura: en Mac, el gratuito Proxyman / el de código abierto Charles interceptan todas las peticiones y respuestas de la app, como una radiografía de la capa de red;
3. Simular red lenta: en el menú del simulador, Features → Network Link Conditioner (hay que descargar la herramienta de la web de desarrolladores), que simula 3G y latencia alta y delata esos problemas de experiencia de «dar vueltas cargando media vida».

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Consejo: ¿la petición no pasa el ATS?

{class="mt-1"}
Si la petición falla nada más salir con un error de "App Transport Security", lo más probable es que uses una dirección http:// sin cifrar. Los endpoints de verdad van por HTTPS; para depurar en local, abre una excepción temporal (añade NSAllowsLocalNetworking en Info.plist) y acuérdate de limpiarla antes de publicar.
:::

{class="mt-1"}
① Buscar el tiempo con normalidad; ② cortar la red y que la app avise con elegancia sin colgarse (¡pruébalo apagando la red del Mac con el simulador!); ③ escribir una ciudad que no existe y recibir un aviso amable; ④ guardar dos ciudades favoritas y que sigan ahí al reiniciar la app; ⑤ que la interfaz no deslumbre en modo oscuro. Solo si supera las cinco, este proyecto queda «graduado».
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumen del capítulo

- Primero prueba la API en el navegador y entiende el JSON, y luego escribe el código: la «tarea previa» nunca se pierde
- La clave de la API se esconde en el xcconfig y jamás entra en el repositorio
- Modelo Codable + URLSession con async/await: si los campos coinciden, el JSON se interpreta solo
- El esquema de tres estados loading/success/error es el todoterreno de las interfaces conectadas
- Sin conexión, entrada vacía, ciudad inexistente: el manejo de errores es la nota mínima de una app conectada
:::
