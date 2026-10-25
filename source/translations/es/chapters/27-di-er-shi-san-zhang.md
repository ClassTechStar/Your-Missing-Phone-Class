---
id: di-er-shi-san-zhang
num: 23
part: chao-yue-pian
nav: Capítulo 23: Pensamiento de programación e iniciación a la automatización
toc: default
kind: chapter
---

### Capítulo 23: Pensamiento de programación e iniciación a la automatización

{class="chapter-intro mb-4"}
En los dos capítulos anteriores, construimos un "muro de seguridad" para tu móvil y conocimos su "cerebro IA", cada vez más inteligente dentro de ese muro. Ahora, desbloqueemos uno de los últimos potenciales del móvil: hacer que "piense" como un programador y ejecute automáticamente tareas continuas que tu configures. Podrias decir: "Yo no se programar, que tiene que ver conmigo?" Tranquilo: este capítulo no requiere que escribas ni una sola linea de código — los móviles modernos han bajado la barrera de la "programacion" al nivel de arrastrar y soltar.

#### I. ¿Qué es la automatización?

En palabras simples: automatización es:<strong>hacer que el móvil ejecute una serie de acciones automáticamente cuando se cumple cierta condición.</strong> No necesitas operar manualmente cada vez ni recordar que hacer — el móvil juzga el momento y ejecuta por si mismo.

Un ejemplo: cada mañana al despertar apagas a mano el modo No molestar, abres WeChat para ver los mensajes, abres la App del tiempo para ver qué ponerte y abres tu música. Si empaquetas estos pasos en un flujo de automatización configurado como «ejecutar cada día a las 7:00», al despertar solo tienes que coger el móvil: todo está listo.

En esencia, la automatización es una cadena lógica de "si... entonces...", el if-else de la programacion. Una vez que entiendas este modo de pensamiento, aunque nunca escribas código en tu vida, tu capacidad para resolver problemas de forma sistematica mejorara notablemente. Elementos clave:

1. <strong>Condicion disparadora (trigger)</strong>: cuando empezar? Puede ser "cada día a las 7", "cuando me conecto al Wi-Fi de casa", "cuando llego a cierto lugar", "cuando la batería baja del 20%".
2. <strong>Accion a ejecutar</strong>: que hacer exactamente? Puede ser enviar un mensaje de WeChat, abrir una App, ajustar el volumen, cambiar el fondo de pantalla, reproducir música, enviar notificaciones... casi todo lo que puedas hacer manualmente en tu móvil, la automatización puede hacerlo.
3. <strong>Lógica intermedia</strong>(opcional pero potente): si la situación es A, haz X; si no, haz Y. Por ejemplo: "si es día laborable reproduce podcasts de noticias, si es fin de semana reproduce música". Esto se llama "ramificación condicional".

#### II. "Atajos" de iOS: la herramienta de automatización para usuarios Apple

La App "Atajos" (Shortcuts) de Apple viene preinstalada, no necesita descarga. Su concepto central es ensamblar varias operaciones como si fueran bloques de construccion. Primero algúnos conceptos clave:

- <strong>"Atajos"</strong>: un flujo de automatización completo; puede ejecutarse manualmente o activarse por voz con Siri. Por ejemplo, dices "Oye Siri, modo casa" y ejecuta automáticamente las operaciones que configuraste.
- <strong>"Automatización"</strong>: instrucciones que se ejecutan automáticamente cuando se cumple el trigger, sin necesidad de activacíon manual. Por ejemplo: "cuando el móvil se conecta al Bluetooth del coche, abre automáticamente la App de mapas". La automatización se configura en la pestana "Automatización", separada de "Atajos".
- <strong>"Accion"</strong>: la unidad mínima de ejecucion. Abrir una App es una acción, enviar un mensaje es una acción, obtener el clima es una acción, ajustar el brillo es una acción. Puedes encadenar cientos o miles de acciones.

Aqui tienes varios ejemplos realmente útiles; siguiendolos una vez lo entenderas todo:

##### Ejemplo 1: Flujo "Buenos días" con un toque

Cada manana tocas una vez (o dices a Siri "buenos días") y el móvil automáticamente: obtiene el clima del día → lee el clima y la temperatura → muestra tu agenda del día → abre tu App de música favorita y empieza a reproducir. Pasos: crear nuevo atajo -&gt; anadir acción "obtener clima actual" -&gt; anadir "leer texto" -&gt; anadir "obtener eventos del calendario" -&gt; anadir "mostrar recordatorío" -&gt; anadir "abrir App" seleccionar NetEase Cloud Music. Asi de simple, todo arrastrando y soltando.

##### Ejemplo 2: "Modo ahorro de energía" automático

: en la pestana «Automatización», crea una nueva automatización → «nivel de batería» → «por debajo del 30 %» → añade «activar el modo de ahorro de energía», «bajar el brillo al 30 %» y «apagar el Bluetooth». Desde entonces, con menos del 30 % el móvil entra solo en ahorro de energía, sin que te preocupes.

##### Ejemplo 3: escanear el código registra los gastos automáticamente

Cada vez que pagas con WeChat/Alipay escaneando un código QR, el móvil lee la notificación de pago y registra automáticamente el monto y el comerciante en una nota o tabla de Numbers. Esto requiere usar el trigger "recibir SMS/notificación" de "Automatización" (iOS 17+ soporta lectura de transacciones de monedero), combinado con la acción "anadir a Numbers". Para quienes quieren llevar cuentas pero son perezosos para registrar manualmente, es una salvacíon.

Otro truco que poca gente conoce: puedes añadir un Atajo a la pantalla de inicio para que parezca un icono de App. Por ejemplo, crea un Atajo «taxi a casa», pon el icono en el escritorio y, con un toque, se abre DiDi con tu casa como destino: mucho más rápido que abrir la App y escribir la dirección.

#### III. Automatización Android - Tasker y amigos

En Android la cosa es un poco más compleja, pero el techo también es más alto. Empecemos por lo sencillo:

##### Nivel de entrada: el auto-clicker

Muchos móviles Android traen un «auto-clicker» de serie o se descarga de la tienda de Apps. Su principio es simple: operas una vez a mano, graba tus coordenadas e intervalos y luego los reproduce a alta velocidad. Si una App da una recompensa diaria por iniciar sesión, grabas el proceso una vez y lo dejas correr solo cada día. Inconveniente: solo reconoce coordenadas; si cambia la interfaz (por ejemplo, por un anuncio), clicka donde no es.

##### Nivel intermedio: Tasker — el rey de la automatización Android

Tasker es la herramienta de automatización más potente y reconocida de Android, lidera los rankings desde hace años. Seamos sinceros: su curva de aprendizaje es algo empinada y su interfaz no es precisamente bonita, pero una vez dominado sentirás que tu móvil puede cualquier cosa. El núcleo de Tasker también es el patrón «trigger → tarea»:

- <strong>Perfil (Profile)</strong>: define "cuándo activar". Los triggers pueden ser: tiempo, ubicación, estado de conexión Wi-Fi, Bluetooth, recepción de notificaciones específicas, estado de batería, orientación de pantalla... Tasker soporta una cantidad absurda de triggers — decenas de tipos.
- <strong>Tarea (Task)</strong>: define "qué hacer al activarse". Una tarea puede contener múltiples acciones que se ejecutan secuencialmente. Tipos de acciones: ajustar configuración del sistema (volumen, brillo, Wi-Fi, Bluetooth, modo avión), enviar SMS, peticiones HTTP, ejecutar comandos Shell, control de reproducción multimedia, mostrar diálogos, etc.

Aqui tienes algúnos escenarios clásicos y prácticos de Tasker:

- <strong>Encender Wi-Fi al llegar a casa</strong>: configura el trigger como "conexión a antena específica" (porque cerca de casa te conectas a una antena fija) -&gt; tarea "activar Wi-Fi". No usa GPS ni consume batería; el móvil enciende el Wi-Fi automáticamente en cuanto entra en tu vecindad.
- <strong>Modo reunión</strong>: condición disparadora (trigger) ="título de evento de calendario contiene'reunión'"-&gt; tarea "activar modo silencioso, bajar volumen multimedia, auto-responder WeChat (requiere plugin)". Nunca más tendrás que preocuparte de que suene el móvil durante una reunión.
- <strong>Protección nocturna para los ojos</strong>: condición disparadora (trigger) ="22:00-06:00"-&gt; tarea"activa el modo protección visual,, reducir brillo al 20%, poner pantalla en blanco y negro (modo escala de grises)". La pantalla en blanco y negro tiene un efecto mágico contra la adicción a videos cortos — en cuanto se pone gris, ya no quieres seguir deslizando.
- <strong>Auriculares automáticos para podcasts</strong>: trigger "conexión de auricular con cable / conexión Bluetooth" -&gt; tarea "abrir App Xiaoyuzhou y reproducir último episodio". Ponte los auriculares y escucha, sin tener que desbloquear el móvil ni buscar la App.

Si Tasker te resulta demasiado complicado, prueba su hermano simplificado:<strong>MacroDroid</strong>. Su interfaz es mucho más amigable, tiene plantillas abundantes e ideal para usuarios que no quieren complicarse. Además, muchos sistemas Android chinos (MIUI de Xiaomi, HarmonyOS de Huawei, ColorOS de OPPO) incluyen funciones de "Escenas" o "Asistente inteligente"; aunque no tan potentes como Tasker, son suficientes para la automatización diaria.

#### IV. Aplicacion cotidiana del pensamiento de automatización

El mayor beneficio de aprender automatización no es ahorrar ese poco tiempo, sino <strong>cambiar tu forma de pensar</strong>. Una vez que te acostumbras al modo de pensamiento "si ocurre X, haz automáticamente Y", descubriras que un monton de tareas repetitivas de la vida pueden eliminarse. Por ejemplo:

- Tras cada foto, respaldo automático a la nube y compresión de fotos locales a tamano reducido para ahorrar espacio.
- Cada manana lee automáticamente la agenda del día, genera un texto y lo envia por WeChat a tu familia.
- Al recibir SMS de confirmacion de entrega de paquete, anade automáticamente una tarea "recoger paquete" en notas.
- Cuando la batería se llena completamente, emite un aviso de voz para desconectar el cargador (evitar sobrecarga).
- A la hora de salida del trabajo, si sigues cerca de la oficina (por localización de antena), recuerda automáticamente "es hora de irse".

Esto suena avanzado, pero en realidad solo necesitas dominar los dos conceptos básicos "trigger + acción", combinados con Atajos o Tasker, y puedes hacerlo todo. La clave es <strong>darte cuenta primero de "esto puede automatizarse"</strong>— mucha gente no es que no sepa, es que ni se le cruza por la cabeza.

#### V. Guia de trampas: problemas comunes de la automatización

La automatización tampoco es un camino de rosas; aquí te adelanto algúnos obstáculos que ya he encontrado:

- <strong>Los triggers por ubicación pueden fallar</strong>: el trigger "llegar/salir de ubicación" de iOS usa tecnología de geocercado; la precision depende de la senal GPS y la optimización del sistema. A veces tarda 10 minutos en activarse después de llegar. Se recomienda usar conexión Wi-Fi o antena como trigger en lugar de ubicación: más fiable y ahorra batería.
- <strong>La "Automatización" de Atajos requiere autorización</strong>: en iOS, la mayoría de los triggers bajo la pestana "Automatización" requieren confirmacion manual (mecanismo de seguridad de iOS). Sin embargo, los triggers de conexión Wi-Fi, Bluetooth y alarma detenida pueden ejecutarse totalmente automáticos sin confirmacion.
- <strong>Tasker necesita permisos de accesibilidad</strong>: muchas funciones avanzadas (como simulación de clics) requieren el servicio de accesibilidad, lo que muestra una notificación persistente en configuración. Es un diseno de seguridad de Android y no se puede eliminar.
- <strong>No compliques demasiado la automatización</strong>: al empezar, comienza con flujos pequenos de "2-3 acciones". No intentes crear un superflujo de 20 pasos de inmediato — depurarlo te volvera loco.

::: div .success-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Consejo:La postura correcta para un Principiante en automatización

{class="mt-1"}
Dedica primero 5 minutos a pensar: cuales son las 3 cosas que más repites en tu móvil cada día? Por ejemplo: tu rutina matinal de cada día, tus hábitos al conectar los auriculares Bluetooth, tu configuración antes de salir... Empieza por estas pequenas tareas frecuentes y crea una automatización simple para cada una. Aunque cada una solo te ahorre 5 segundos, con el tiempo suma mucho. Y la satisfacción de crearlas es realmente adictiva.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Practica: tres desafios de automatización para Principiantes

{class="mt-1 mb-2"}
Elige el que mejor se adapte a ti; cuando lo completes, ya seras Principiante:

{class="list-decimal pl-6 mt-1 space-y-1"}
1. <strong>Desafio 1: Automatización de buenos días</strong>: iOS: en Atajos crea nuevo atajo -&gt; anadir "obtener clima actual" -&gt; "leer texto" -&gt; "abrir App" seleccionar NetEase Cloud Music. Luego puedes decir a Siri "buenos días" para activarlo. Android: en Tasker nueva tarea -&gt; anadir "obtener clima" -&gt; "leer" -&gt; "abrir App" -&gt; configurar trigger a las 7:00 diarias.
2. <strong>Desafio 2: Ahorro automático de batería baja</strong>: iOS: pestana Automatización -&gt; nuevo -&gt; "nivel de batería" -&gt; menos del 25% -&gt; anadir "activar modo bajo consumo" + "fijar brillo 25%". Android: Tasker nuevo Profile -&gt; Estado -&gt; Bateria -&gt; 0-25% -&gt; tarea "activar modo ahorro" + "reducir brillo".
3. <strong>Desafio 3: Navegacion automática al conectar Bluetooth del coche</strong>: iOS: Automatización -&gt; nuevo -&gt; "Bluetooth" -&gt; selecciona tu Bluetooth de coche -&gt; anadir "abrir App Amap/Gaode" + "volumen multimedia al 80%". Android: Tasker -&gt; Profile -&gt; Estado -&gt; Bluetooth conectado -&gt; selecciona Bluetooth de coche -&gt; tarea "abrir Amap" + "subir volumen multimedia".
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Caso 3: Automatización del "flujo de buenos días"

{class="list-disc pl-6 mt-1 space-y-1"}
- <strong>Escenario</strong>: Todos los días a las 7:00, pronóstico del tiempo automático + silencio desactivado + abrir noticias.
- <strong>Pasos</strong>: iOS: Atajos &gt; Automatización &gt; Activación por hora &gt; añadir "Obtener clima" + "Ajustar volumen" + "Abrir app"; Android: MacroDroid &gt; Disparador (hora 7:00) &gt; Acción (volumen multimedia / abrir URL / TTS leer clima).
- <strong>Resultado esperado</strong>: Se puede usar sin instalación, reduciendo la barrera de entrada.
:::
