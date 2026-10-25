---
id: di-liu-shi-ba-zhang
num: 68
part: ios-kai-fa-pian
nav: Capítulo 68: El camino avanzado — permisos, notificaciones y arquitectura moderna
toc: default
kind: chapter
---

### Capítulo 68: El camino avanzado — permisos, notificaciones y arquitectura moderna

{class="chapter-intro mb-4"}
Saber hacer una app es solo el comienzo. Este capítulo habla de los escalones que van de «saber hacer» a «hacerlo bien»: cómo pedir permisos con elegancia, cómo mandar notificaciones sin resultar pesado, cómo elevar un peldaño más la arquitectura y —en 2026— cómo escribir código iOS en compañía de la IA. Cada punto te lo vas a encontrar enseguida en proyectos reales.

#### 1. Permisos: primero toca la puerta, luego entra

Cámara, ubicación, contactos, notificaciones… en estas «zonas sensibles», iOS exige que la app pida permiso al usuario con una ventana en el momento de usarlas. La norma son tres pasos: «declarar + solicitar + degradar con elegancia»:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Solicitud de permisos (ejemplo: ubicación)</span><span class="dots">···</span>
:::

```
// 1. declara en Info.plist el texto de uso (¡sin declararlo, crash directo!)
// Privacy - Location When In Use Usage Description: "Se usa para consultar el tiempo de tu ciudad"

// 2. pedirlo en el momento de usarlo
import CoreLocation

@Observable
class LocationModel {
    private let manager = CLLocationManager()

    func request() {
        switch manager.authorizationStatus {
        case .notDetermined: manager.requestWhenInUseAuthorization()
        case .denied, .restricted: /* guiar a Ajustes para activarlo */
        default: /* concedido, adelante */
        }
    }
}

// 3. degradar con elegancia tras un rechazo: mostrar aviso y saltar a Ajustes
// UIApplication.shared.open(URL(string: UIApplication.openSettingsURLString)!)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Ojo: los permisos de iOS son «de una sola vez»

{class="mt-1"}
La ventana de permisos de iOS solo aparece una vez: si el usuario la rechaza, no vuelve a salir jamás. Por eso: pide el permiso «en el momento justo en que el usuario va a usarlo» (no una ráfaga de ventanas al arrancar) y explica en el texto para qué lo necesitas. La guía en la interfaz tras un rechazo («activa la ubicación en Ajustes») es de serie: no dejes al usuario atrapado en un callejón sin salida.
:::

#### 2. Notificaciones: decir cosas útiles en el momento correcto

Las notificaciones son el canal con el que la app llega al usuario y también la función que más fácil «bloquea» él. iOS usa el framework UserNotifications y hay tres disciplinas para notificar: mandar solo lo útil, dejar que el usuario las apague y no molestar de madrugada. Uso básico:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Notificaciones locales</span><span class="dots">···</span>
:::

```
import UserNotifications

// 1. pedir el permiso de notificaciones (una sola ventana emergente)
UNUserNotificationCenter.current()
    .requestAuthorization(options: [.alert, .sound, .badge]) { granted, _ in
        print(granted ? "Concedido" : "Denegado")
    }

// 2. programar un "recordatorio de gastos a las 20:00 cada día"
func scheduleDailyReminder() {
    let content = UNMutableNotificationContent()
    content.title = "Recordatorio de gastos"
    content.body = "Hoy aún no has anotado nada"
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

Ojo: el permiso de notificaciones de iOS también «solo se pide una vez» y el usuario puede apagarlo cuando quiera en los Ajustes del sistema; por eso importa el valor del contenido de cada notificación: abusar una sola vez puede costarte al usuario para siempre.

#### 3. Arquitectura avanzada: MVVM en profundidad y testeabilidad

Ya usaste MVVM en el capítulo 65; aquí van tres puntos avanzados:

- Abstracción con protocolos: haz que el ViewModel dependa de un protocol (protocolo) y no de una clase concreta: en las pruebas puedes inyectar «fuentes de datos falsas»; es la piedra angular de la testeabilidad;
- Responsabilidad única: cada ViewModel se ocupa de una sola cosa (el de cuentas no se mete con el tiempo); si crecen las funciones, divídelo;
- No hagas sobreingeniería: en un proyecto pequeño de una persona, «clase @Observable + abstracción con protocolos» basta. Las arquitecturas pesadas como VIPER o Clean Architecture, cuando lleguen el equipo y la complejidad: las herramientas sirven a los objetivos, no para presumir.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Consejo: el «dividendo del ecosistema» de SwiftUI

{class="mt-1"}
El ecosistema iOS tiene además dos jugadas avanzadas «que solo existen aquí»: los widgets (WidgetKit) permiten ver información sin abrir la app (el «gasto del mes» de la libreta en la pantalla de inicio) y los Atajos (App Intents) permiten llamar a tus funciones con Siri o automatizaciones. Ambos tienen frameworks oficiales y cuestan poco de aprender, pero suman muchísimo a la experiencia: valen que los desbloquees de los primeros en el camino avanzado.
:::

#### 4. Lo nuevo de 2026: desarrollo de iOS asistido por IA

En 2026, la IA ya está profundamente metida en el flujo de desarrollo de Apple. Si quieres ganar velocidad, esta combinación está muy madura:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Fase</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Cómo ayuda la IA</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Tu responsabilidad</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Escribir código</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Autocompletado integrado en Xcode + generación con plugins de IA de terceros</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Describir bien los requisitos y revisar el resultado</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Consultar documentación</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Dar a la IA la documentación oficial y los mensajes de error para que los interprete</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Verificar las conclusiones clave en la documentación oficial</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Escribir pruebas</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pedir a la IA casos de XCTest por tres categorías: «normal / límite / anómalo»</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Confirmar que los casos encajan con la semántica del negocio</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Arreglar errores</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pegar el registro del cuelgue + el código relacionado, y la IA localiza y corrige</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Entender el cambio y verificarlo ejecutando las pruebas</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Los cuatro escenarios del desarrollo de iOS asistido por IA

La metodología concreta —cómo dar instrucciones a la IA, cómo aceptar los resultados, cómo evitar tropiezos— está desarrollada en 11 capítulos completos de la séptima parte de este libro, «Práctica de programación con IA» (capítulos 37-47); se recomienda encarecidamente leerla a la par: la sintaxis de Swift, en esta parte; los trucos de colaborar con la IA, en la séptima.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Manos a la obra: añade a la libreta «el trío»

#### 5. Claves de la concurrencia de Swift: @MainActor y Task

El sistema de concurrencia de Swift 6 tiene dos reglas que un principiante debe entender:

- La interfaz solo se actualiza en el hilo principal: las vistas de SwiftUI son @MainActor por defecto; cuando llegue la respuesta de la red, vuelve al hilo principal para cambiar el estado (con await MainActor.run { ... } o marcando el ViewModel como @MainActor);
- Las tareas asíncronas se gestionan con Task: el modificador .task { } arranca solo cuando aparece la vista y se cancela solo cuando desaparece: es la postura estándar para lanzar trabajo asíncrono en SwiftUI; no andes escribiendo Task a pelo dentro del body.

::: div .code-block
:::inline div .code-head
<span>SWIFT · La forma estándar asíncrona</span><span class="dots">···</span>
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
        .task {                       // arranca al aparecer, se cancela al desaparecer
            await vm.search(city: "Madrid")
        }
    }
}
```
:::

Detrás de estas dos reglas está el diseño de «seguridad frente a carreras de datos» de Swift 6: el compilador te avisa en cuanto te equivocas, en lugar de esperar a que la app se cuelgue para enterarse. Los errores del compilador no buscan pelea: te paran balas.

{class="mt-1"}
① Añade a la libreta el «recordatorio de anotar cuentas a las 20:00 todos los días» (permiso de notificaciones + notificación local); ② cambia la fuente de datos del ViewModel a una abstracción con protocolo y escribe una prueba unitaria con datos falsos inyectados; ③ añade un widget de «gasto del mes» para la pantalla de inicio. Con el trío completo, tu proyecto ya tiene aire de «ejército regular».
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumen del capítulo

- Los tres pasos del permiso: declarar en Info.plist (si falta, cuelgue seguro), pedirlo al usarlo y guiar a Ajustes si lo rechazan
- La ventana de permisos de iOS solo sale una vez: elige el momento «justo cuando va a usarse» y explica con claridad el uso
- Las tres disciplinas de las notificaciones: solo lo útil, poder apagarlas, no molestar; framework UserNotifications
- MVVM avanzado: abstracción con protocolos (testeable), responsabilidad única y nada de sobreingeniería
- Dividendo del ecosistema: widgets con WidgetKit + Atajos con App Intents
- Los cuatro escenarios de la IA: escribir código, consultar documentación, escribir pruebas y arreglar errores; la metodología, en la séptima parte (capítulos 37-47)
:::
