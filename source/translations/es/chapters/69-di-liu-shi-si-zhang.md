---
id: di-liu-shi-si-zhang
num: 64
part: ios-kai-fa-pian
nav: Capítulo 64: Almacenamiento de datos y peticiones de red
toc: default
kind: chapter
---

### Capítulo 64: Almacenamiento de datos y peticiones de red

{class="chapter-intro mb-4"}
Una app que solo sirve para «mirar» está muerta; la que guarda datos y se conecta a internet está viva. Este capítulo presenta el «trío» de la capa de datos de iOS: UserDefaults (configuraciones pequeñas), SwiftData (datos estructurados) y URLSession (hablar con el servidor), más Codable para interpretar JSON y el moderno async/await. Al terminarlo, podrás escribir apps de verdad que recuerdan los hábitos del usuario y actualizan su contenido al momento.

#### 1. Cómo elegir el almacenamiento: mira primero esta tabla

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Opción</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Qué guardar</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Características</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Dónde se usa en este libro</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UserDefaults</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Configuraciones sueltas (interruptores, preferencias)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pares clave-valor, simple y directo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ajustes del capítulo 65, ciudades favoritas del capítulo 66</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftData</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Datos estructurados (movimientos, registros)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Envoltorio oficial de base de datos; se declara con @Model en una línea</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Movimientos del capítulo 65</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">URLSession</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Datos del servidor (no se guardan, se traen de la red)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Framework de red del sistema, sin dependencias de terceros</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Datos del tiempo del capítulo 66</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Cómo se reparten el trabajo los tres

Memoriza esta regla: «las configuraciones pequeñas van a UserDefaults, los datos en bloque van a SwiftData y los datos de fuera viajan por URLSession». Core Data, de los tutoriales antiguos, sigue funcionando (SwiftData es su disfraz moderno), y el SQLite escrito a mano prácticamente no hace falta tocarlo: aprende directo lo nuevo, no tomes el camino viejo.

#### 2. UserDefaults: guardar unas configuraciones pequeñas

::: div .code-block
:::inline div .code-head
<span>SWIFT · Ejemplo con UserDefaults</span><span class="dots">···</span>
:::

```
// escribir: guardar un valor
UserDefaults.standard.set(true, forKey: "isDarkMode")
UserDefaults.standard.set("Madrid", forKey: "favoriteCity")

// leer: sacarlo (si no hay, devuelve el valor por defecto)
let isDark = UserDefaults.standard.bool(forKey: "isDarkMode")
let city = UserDefaults.standard.string(forKey: "favoriteCity") ?? "Madrid"

// borrar: eliminar una clave
UserDefaults.standard.removeObject(forKey: "isDarkMode")
```
:::

Ojo: solo sirve para configuraciones pequeñas y sueltas. Si tienes decenas o cientos de registros, pásalos a SwiftData; no uses UserDefaults como base de datos (ralentiza el arranque y resulta incómodo para consultar).

#### 3. SwiftData: dar a los datos «casa de verdad»

SwiftData es la solución oficial de base de datos desde iOS 17 y reduce al mínimo crear tablas y hacer altas, bajas, cambios y consultas: con una sola anotación @Model, una clase de datos se convierte en tabla:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Ejemplo con SwiftData</span><span class="dots">···</span>
:::

```
import SwiftData

// 1. @Model: esta clase se convierte automáticamente en "tabla"
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

// 2. se acopla el contenedor en el punto de entrada de la app
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .modelContainer(for: Record.self)   // base de datos lista
    }
}

// 3. en la vista se lee con @Query y se escribe con @Environment
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
        context.insert(r)     // guardar
        try? context.save()   // persistir en disco
    }
}
```
:::

Esta plantilla de «@Model + modelContainer + @Query» la puedes copiar tal cual a cualquiera de tus proyectos: solo cambia los nombres de los campos. En cuanto cambian los datos, @Query refresca la interfaz por su cuenta: una maravilla.

#### 4. Codable: «traducir» el JSON

Los datos de los servidores suelen llegar en JSON. El protocolo Codable de Swift hace que la conversión «JSON ⇄ struct» ocurra sola: si los nombres de los campos coinciden, la magia funciona:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Parsear JSON con Codable</span><span class="dots">···</span>
:::

```
// JSON: {"name":"Madrid","main":{"temp":26.5},"weather":[{"description":"Despejado"}]}
struct WeatherResponse: Codable {
    let name: String
    let main: Main
    let weather: [Weather]
}
struct Main: Codable { let temp: Double }
struct Weather: Codable { let description: String }

// de cadena JSON a struct
let decoder = JSONDecoder()
let data = jsonString.data(using: .utf8)!
let result = try decoder.decode(WeatherResponse.self, from: data)
print(result.weather[0].description)   // "Despejado"
```
:::

Regla de hierro: mira primero el JSON real que devuelve el servidor y luego define los campos. Muchos errores de «no lo puedo interpretar» son nombres de campo mal escritos o tipos mal adivinados (el servidor manda "26.5" como texto y tú lo declaras como Double): imprime el JSON original y compáralo, y lo localizas en diez segundos.

#### 5. URLSession + async/await: hablar con el servidor

Para conectarse a internet, iOS usa el URLSession que trae el sistema, junto con async/await de Swift (funciones asíncronas): «esperar la red» resulta tan natural como «esperar un paquete»:

::: div .code-block
:::inline div .code-head
<span>SWIFT · URLSession + async/await</span><span class="dots">···</span>
:::

```
struct WeatherService {
    // función asíncrona: async marca "tengo que esperar un rato", throws marca "puede fallar"
    func fetchWeather(city: String) async throws -> WeatherResponse {
        let url = URL(string:
            "https://api.example.com/weather?city=\(city)")!
        let (data, _) = try await URLSession.shared.data(from: url)
        return try JSONDecoder().decode(WeatherResponse.self, from: data)
    }
}

// punto de llamada (dentro de .task):
.task {
    do {
        let weather = try await service.fetchWeather(city: "Madrid")
        // actualizar la interfaz…
    } catch {
        print("Error: \(error)")
    }
}
```
:::

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Para evitar tropiezos: dos reglas de hierro de la red

{class="mt-1"}
① Las conexiones van con async/await y jamás bloquean el hilo principal: una interfaz congelada es una experiencia de emergencia. La concurrencia estructurada de Swift lo hace muy natural, pero no olvides el try await ni el do/catch. ② ATS prohíbe por defecto el HTTP sin cifrar: iOS exige HTTPS. Para probar un servicio http:// local necesitas abrir una excepción temporal en Info.plist (NSAppTransportSecurity), pero un producto real debe ir todo por HTTPS: en la revisión también se fijan en eso.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Manos a la obra: una miniapp de «frase del día»

#### 6. Los errores de red también se «clasifican»: no le tires todos los fallos al usuario

Sin conexión, tiempo agotado, 404, error 500 del servidor… a cada error le corresponde un mensaje distinto para el usuario:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Gestión de errores por niveles</span><span class="dots">···</span>
:::

```
func friendlyMessage(_ error: Error) -> String {
    if let urlError = error as? URLError {
        switch urlError.code {
        case .notConnectedToInternet: return "Sin red, ¿revisas la conexión?"
        case .timedOut:               return "Tiempo de espera agotado, ¿intentas más tarde?"
        case .cannotFindHost:         return "No se encuentra el servidor"
        default:                      return "Problema de red: \(urlError.code)"
        }
    }
    if let d = error as? DecodingError {
        return "Formato de datos incorrecto (quizá cambió la API)"
    }
    return "Error: \(error.localizedDescription)"
}
```
:::

Enséñale al usuario «palabras de humano» y deja «la letra original» para los registros (imprime el error completo). No le lances al usuario el galimatías en inglés de error.localizedDescription: la sensación de producto cuidado vive en estos detalles.

{class="mt-1"}
Busca una API gratuita de frases (como hitokoto u otra parecida) y usa URLSession + async/await para traer la «frase del día», muéstrala en el centro de la pantalla y añade un botón «Otra». Luego guarda con SwiftData tus frases favoritas en una «colección». Este ejercicio usa UserDefaults, SwiftData, Codable y URLSession todos a la vez: si lo terminas, los capítulos 7 y 8 serán pan comido.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumen del capítulo

- La regla: configuraciones pequeñas a UserDefaults, datos en bloque a SwiftData, datos de fuera por URLSession
- Los tres movimientos de SwiftData: @Model declara la tabla, modelContainer monta el contenedor, @Query lee y context.insert escribe
- Codable «traduce» el JSON sin que lo pidas: si los campos coinciden, la magia funciona
- URLSession + async/await: conectarse es como esperar un paquete; do/catch se encarga de los fallos
- Dos reglas de hierro: no bloquear el hilo principal; el producto real, por HTTPS (ATS)
:::
