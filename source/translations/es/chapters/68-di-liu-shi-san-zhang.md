---
id: di-liu-shi-san-zhang
num: 63
part: ios-kai-fa-pian
nav: Capítulo 63: Vistas, estado y navegación
toc: default
kind: chapter
---

### Capítulo 63: Vistas, estado y navegación

{class="chapter-intro mb-4"}
Ya sabes hacer apps de una sola pantalla. Este capítulo resuelve dos problemas de «crecimiento»: cómo saltar de unas páginas a otras (navegación) y cómo fluyen los datos entre páginas (gestión de estado). Al terminarlo podrás montar el esqueleto clásico de una app multipágina: «lista → detalle → edición».

#### 1. Panorama del flujo de datos para gestionar el estado

@State no es la única herramienta de estado de SwiftUI. Mira primero este panorama para entender «cuál usar en cada momento»:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Herramienta</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Qué gestiona</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Quién la usa</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Escenario típico</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@State</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Estado temporal privado de la página</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">La vista actual</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Contadores, texto de un campo</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Binding</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tomar prestado el estado de otro</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Una vista hija modifica a la padre</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Componentes personalizados</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@StateObject / @Observable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lógica compartida entre páginas</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Modelo de vista (ViewModel)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Carga de datos, lógica de negocio</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@EnvironmentObject / .environment</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Estado global compartido</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Toda la app</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sesión del usuario, ajustes del tema</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Panorama de las herramientas de estado de SwiftUI (en 2026, @Observable ya es lo habitual)

::: div .code-block
:::inline div .code-head
<span>SWIFT · Lo estándar en 2026: view models con @Observable</span><span class="dots">···</span>
:::

```
// la forma moderna de iOS 17+: la macro @Observable (recomendada para proyectos nuevos)
import Observation

@Observable
class CounterModel {                 // el view model
    var count = 0
    func increment() { count += 1 }
}

struct CounterView: View {
    @State private var model = CounterModel()   // mantiene el modelo

    var body: some View {
        VStack {
            Text("Has pulsado \(model.count) veces")
            Button("Púlsame") { model.increment() }
        }
    }
}
```
:::

Consejo directo para principiantes: usa @State para lo privado de la página y clases @Observable para lo que cruza páginas o lleva lógica. El @StateObject/@ObservableObject de los tutoriales viejos es la generación anterior: basta con saber leerlo; el código nuevo, hazlo como aquí.

#### 2. NavigationStack: la «pila» para saltar de página

Desde iOS 16, la navegación multipágina usa NavigationStack: funciona como una pila de platos, apilas uno sobre otro y al volver se van sacando:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Navegación con NavigationStack</span><span class="dots">···</span>
:::

```
struct HomeView: View {
    var body: some View {
        NavigationStack {
            List {
                NavigationLink("Las cuentas de Luis") {
                    DetailView(name: "Las cuentas de Luis")   // página destino
                }
                NavigationLink("Las cuentas de María") {
                    DetailView(name: "Las cuentas de María")
                }
            }
            .navigationTitle("Lista de cuentas")   // título grande arriba
        }
    }
}

struct DetailView: View {
    let name: String
    var body: some View {
        Text("Detalles de \(name)")
            .navigationTitle(name)
            .navigationBarTitleDisplayMode(.inline)
    }
}
```
:::

NavigationLink es el «enlace que se toca para navegar»; navigationTitle genera automáticamente el título de la barra de navegación y el botón de retroceso. Para navegar por código (por ejemplo, volver solo tras pulsar «Guardar»), usa @Environment(\.dismiss) para cerrar la página actual. Con estas dos técnicas cubres el 90 % de las necesidades de navegación.

#### 3. Ventanas modales y pestañas: sheet y TabView

Además de «empujar páginas», hay dos interacciones clásicas:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Diálogos sheet + pestañas con TabView</span><span class="dots">···</span>
:::

```
// 1. hoja que sube desde abajo, media pantalla o completa (la favorita de los formularios de alta)
struct HomeView: View {
    @State private var showAdd = false
    var body: some View {
        Button("Apuntar gasto") { showAdd = true }
            .sheet(isPresented: $showAdd) {
                AddRecordView()     // la pantalla de alta que se abre
            }
    }
}

// 2. barra de pestañas inferior (el "esqueleto" de la app)
struct MainTabView: View {
    var body: some View {
        TabView {
            RecordListView()
                .tabItem { Label("Cuentas", systemImage: "book") }
            StatsView()
                .tabItem { Label("Estadísticas", systemImage: "chart.pie") }
            SettingsView()
                .tabItem { Label("Ajustes", systemImage: "gear") }
        }
    }
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Consejo: ¿cuándo usar cada una?

{class="mt-1"}
Regla práctica: para el flujo principal, empuja páginas con NavigationStack (lista → detalle); para acciones temporales, ventanas con sheet (añadir, editar, confirmar); para bloques grandes al mismo nivel, TabView (pestañas inferiores). La combinación de los tres es el esqueleto de casi todas las apps.
:::

#### 4. List: la lista por excelencia de iOS

El componente más usado y con más «sabor Apple» de iOS es List: trae de fábrica separadores, borrado al deslizar y resaltado al tocar:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Listas con List + borrar deslizando</span><span class="dots">···</span>
:::

```
struct RecordListView: View {
    @State private var records = ["Comida 25.5", "Metro 6.0", "Nómina +8000"]

    var body: some View {
        List {
            ForEach(records, id: \.self) { r in
                Text(r)
            }
            .onDelete { indexSet in          // desliza a la izquierda para borrar
                records.remove(atOffsets: indexSet)
            }
        }
    }
}
```
:::

Lista + NavigationLink + sheet + TabView: combinando estas cuatro piezas ya puedes montar el esqueleto completo de una app de «lista de cuentas → abrir el detalle → pulsar + y registrar». Así se construye la libreta de cuentas del próximo capítulo.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Manos a la obra: monta un «esqueleto de tres páginas»

#### 5. Ciclo de vida de la app: primer plano y segundo plano

Como el ciclo de vida de las Activity de Android, las apps de iOS también pasan por estados de «nacer, primer plano, segundo plano y morir». En SwiftUI se observan con el valor de entorno scenePhase:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Observar el paso a primer/segundo plano</span><span class="dots">···</span>
:::

```
@main
struct MyApp: App {
    @Environment(\.scenePhase) private var phase

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .onChange(of: phase) { _, newPhase in
            switch newPhase {
            case .active:    print("vuelta a primer plano: reanudar el refresco")
            case .inactive:  print("en transición (llamada o el instante en que pasa a segundo plano)")
            case .background: print("pasa a segundo plano: guardar el borrador")
            @unknown default: break
            }
        }
    }
}
```
:::

Usos típicos: refrescar los datos al volver al primer plano y guardar el borrador al pasar a segundo plano. iOS es muy estricto con el trabajo en segundo plano: una app normal se suspende (se congela) poco después de ir a segundo plano, así que no cuentes con colar trabajo pesado ahí. Si de verdad necesitas tareas programadas, usa las notificaciones locales del capítulo 68, no un «servicio residente».

{class="mt-1"}
Haz un esqueleto de libreta de cuentas con datos falsos: un TabView con tres pestañas (cuentas / estadísticas / ajustes) → la página de cuentas muestra los datos falsos con una List y al tocar una fila salta al detalle (NavigationStack) → el botón «+» de la esquina superior derecha abre un sheet de registro. Sin guardar datos y sin internet, pura práctica de esqueleto: si este esqueleto te sale bien, rellenarlo con datos reales en el capítulo 65 será coser y cantar.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumen del capítulo

- Las cuatro herramientas de estado: @State (privado de la página), @Binding (prestado), @Observable (lógica) y .environment (global)
- En proyectos nuevos, escribe los view models con la macro @Observable; con el @ObservableObject de los tutoriales viejos basta con que sepas leerlo
- NavigationStack empuja páginas; @Environment(\.dismiss) permite volver por código
- En el flujo principal se empujan páginas, las acciones temporales se abren con sheet y los bloques paralelos van en un TabView
- List es la lista por excelencia: separadores y borrado al deslizar, de fábrica
:::
