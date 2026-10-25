---
id: di-wu-shi-qi-zhang
num: 57
part: an-zhuo-kai-fa-pian
nav: Capítulo 57: El camino avanzado: permisos, notificaciones y arquitectura moderna
toc: default
kind: chapter
---

### Capítulo 57: El camino avanzado: permisos, notificaciones y arquitectura moderna

{class="chapter-intro mb-4"}
Poder crear una App es solo el comienzo. Este capítulo habla de los obstáculos que hay entre "saber hacer" y "hacer bien": cómo pedir permisos con elegancia, cómo enviar notificaciones sin resultar molesto, cómo subir un nivel la arquitectura y, en 2026, cómo programar en Android en pareja con la IA. Todo esto lo vas a encontrar enseguida en proyectos reales.

#### 1. Permisos en tiempo de ejecución: primero toca la puerta, luego entra

Cámara, ubicación, contactos, notificaciones... para estas "zonas sensibles", Android exige que la App lo pida al usuario en tiempo de ejecución (desde Android 6). La regla es: primero declarar (Manifest), después solicitar (código) y, si el usuario rechaza, degradar con elegancia. En Compose, lo más cómodo es usar rememberPermissionState de la librería oficial Accompanist:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Permisos en tiempo de ejecución (versión Compose)</span><span class="dots">···</span>
:::

```
// declara primero en el Manifest:
// &lt;uses-permission android:name="android.permission.CAMERA" /&gt;

@Composable
fun CameraButton() {
    val permission = rememberPermissionState(
        permission = android.Manifest.permission.CAMERA
    )
    Button(onClick = {
        when {
            permission.status.isGranted -&gt; openCamera()
            permission.status.shouldShowRationale -&gt; showExplainDialog()
            else -&gt; permission.launchPermissionRequest()
        }
    }) { Text("Hacer foto") }
}
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Atención: ¿y si te rechazan el permiso para siempre?

{class="mt-1"}
Si el usuario marcó "no volver a preguntar", launchPermissionRequest ya no mostrará el diálogo. En ese caso, guíalo a los ajustes del sistema para que lo active a mano (con un Intent que abra la página de ajustes de la app) y explica en la interfaz "para qué sirve este permiso". Con un buen trato, muchos más usuarios querrán activarlo: el texto con el que pides el permiso merece escribirse con cuidado.
:::

#### 2. Notificaciones: decir cosas útiles en el momento correcto

Las notificaciones son el canal para llegar al usuario y también la función que más rápido "bloquea" el usuario. Tres reglas para enviarlas: manda solo lo útil, deja que el usuario pueda apagarlas y no molestes de madrugada. Uso básico:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Enviar una notificación</span><span class="dots">···</span>
:::

```
// en Android 13+ hay que pedir primero el permiso POST_NOTIFICATIONS (ver sección anterior)

// 1. crear el canal de notificaciones (obligatorio en Android 8+)
val channel = NotificationChannel(
    "reminder", "Recordatorios", NotificationManager.IMPORTANCE_DEFAULT
)
val manager = getSystemService(NotificationManager::class.java)
manager.createNotificationChannel(channel)

// 2. enviar la notificación
val notification = NotificationCompat.Builder(this, "reminder")
    .setSmallIcon(R.drawable.ic_notification)
    .setContentTitle("Recordatorio de gastos")
    .setContentText("Hoy aún no has anotado nada")
    .setPriority(NotificationCompat.PRIORITY_DEFAULT)
    .build()
if (ActivityCompat.checkSelfPermission(this,
        Manifest.permission.POST_NOTIFICATIONS) == PackageManager.PERMISSION_GRANTED
) {
    manager.notify(1, notification)
}
```
:::

Las tareas programadas (por ejemplo, "recordar anotar los gastos a las 20:00 cada día") se hacen con WorkManager: es el "mayordomo de tareas en segundo plano" recomendado oficialmente, garantiza que la tarea se ejecute en el momento adecuado y te ahorra preocuparte por la optimización de batería. Para necesidades tipo alarma, es la elección segura.

#### 3. Arquitectura avanzada: inyección de dependencias y modularización

Cuando el proyecto crece, aparecen dos "problemas dulces":

- Creación de objetos caótica: cada pantalla crea por su cuenta la base de datos y la API; usa Hilt (framework de inyección de dependencias) para gestionarlo todo de forma centralizada: "quien pide algo, lo recibe";
- Código amontonado: un proyecto de un solo módulo se vuelve cada vez más lento de modificar; divídelo en varios módulos (app / core / feature-xxx) para desarrollar y probar cada función por separado.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Consejo: no te compliques de más

{class="mt-1"}
Hilt y la modularización son buenas herramientas, pero en un proyecto individual no tengas prisa por usarlas. Para la app de gastos, un solo módulo con dependencias creadas a mano basta de sobra. Introdúcelas cuando toque: cuando el código pase de decenas de miles de líneas, la compilación se vuelva lenta o colaboren varias personas. Las herramientas sirven al objetivo, no son para presumir: es el principio de "simplicidad ante todo" de este libro de programación con IA.
:::

#### 4. Lo nuevo de 2026: desarrollo Android asistido por IA

En 2026, la IA ya está profundamente integrada en el flujo de desarrollo Android. Si quieres ir más rápido, esta combinación está muy madura:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Etapa</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Cómo ayuda la IA</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Tu responsabilidad</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Escribir código</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gemini integrado en Android Studio o plugins de IA de terceros para autocompletar y generar</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Describir bien los requisitos y revisar el resultado</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Buscar información</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Dar a la IA la documentación oficial y los mensajes de error para que los interprete</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Verificar las conclusiones clave en la documentación oficial</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Escribir pruebas</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pedir a la IA que genere casos de tres tipos: "normal / límite / error"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Confirmar que los casos encajan con la lógica del negocio</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Arreglar bugs</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pegar el stacktrace más el código relacionado y que la IA localice y repare</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Entender los cambios y ejecutar las pruebas para verificar</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Los cuatro escenarios del desarrollo Android asistido por IA

La metodología concreta (cómo dar instrucciones a la IA, cómo aceptar los resultados y cómo evitar trampas) está desarrollada en 11 capítulos completos de la séptima parte de este libro, "Programación con IA en la práctica" (capítulos 37-47); te recomiendo mucho leerlos juntos: la sintaxis de Android va en esta parte y el arte de colaborar con la IA en la séptima.

#### 5. Optimización de rendimiento y herramientas de depuración en Compose

Con Compose se escribe a gusto, pero la "recomposición excesiva" también provoca tirones. Tres trucos prácticos:

- Estabiliza los parámetros: añade @Immutable a tus data classes o usa derivedStateOf para evitar que cambios de estado sin relación disparen recomposiciones enormes;
- Recuerda usar key: items(list, key = { it.id }) hace que, al añadir o borrar, la lista solo toque lo que debe tocar; sin key, borrar un elemento puede redibujar la lista entera;
- Modo Compose del Layout Inspector: muestra en tiempo real cuántas veces se recompone cada Composable; quién se recompone demasiado queda a la vista, y optimiza a partir de esos puntos calientes.

Además, activa los informes del compilador de Compose (Metrics), que generan un reporte de "qué componentes son inestables": en el camino avanzado, los datos siempre son más fiables que las sensaciones.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Manos a la obra: añade el "trío" a tu app de gastos

{class="mt-1"}
① Añade a la app de gastos un "recordatorio para anotar gastos a las 20:00 cada día" (WorkManager + canal de notificaciones + permiso de notificaciones de Android 13); ② cambia la creación de la base de datos y de la API a inyección con Hilt; ③ prueba a acelerar la función de "filtro mensual" con herramientas de IA y luego revisa el resultado con el método de aceptación en tres niveles. Con las tres piezas hechas, tu proyecto tendrá un aire verdaderamente profesional.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumen del capítulo

- Permisos sensibles: declaración en el Manifest + solicitud en tiempo de ejecución + guía elegante tras un rechazo
- Tres reglas de las notificaciones: solo lo útil, que se puedan apagar y sin molestar; canal + permiso, no falta uno
- Las tareas programadas van con WorkManager; no reinventes la rueda
- Hilt gestiona los objetos y la modularización gestiona el código; en proyectos pequeños individuales, no tengas prisa
- Cuatro escenarios de ayuda con IA: escribir código, buscar información, escribir pruebas y arreglar bugs; la metodología está en la séptima parte (capítulos 37-47)
:::
