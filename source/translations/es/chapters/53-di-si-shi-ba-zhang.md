---
id: di-si-shi-ba-zhang
num: 48
part: an-zhuo-kai-fa-pian
nav: Capítulo 48: Conocer Android — del sistema operativo al ecosistema de desarrollo
toc: default
kind: chapter
---

### Capítulo 48: Conocer Android — del sistema operativo al ecosistema de desarrollo

{class="chapter-intro mb-4"}
Enhorabuena por tomar esta decisión: pasas de "persona que usa el móvil" a "persona que hace apps para el móvil". Antes de ponernos en marcha, despleguemos el mapa: ¿de dónde viene Android? ¿Por qué los desarrolladores de todo el mundo le escriben apps? ¿Qué pasa entre que tus dedos teclean el código y la app llega al móvil del usuario?

#### I. Los orígenes de Android: de "pequeño robot" al "sistema más grande del mundo"

La historia de Android empieza en 2003, cuando un ingeniero llamado Andy Rubin fundó la empresa Android con un objetivo sencillo: crear un sistema operativo inteligente que "entendiera mejor la cámara". Google la compró en 2005; en 2007 fundó junto a decenas de fabricantes la Open Handset Alliance (OHA); y en septiembre de 2008 salió a la venta el primer móvil con Android, el HTC Dream (G1).

El resto de la historia ya la conoces: en 2026, Android es el sistema operativo móvil con mayor cuota de mercado del mundo, con miles de millones de dispositivos activos. Tu móvil, tu decodificador de TV, la pantalla del coche o tu reloj inteligente seguramente funcionan con Android. ¿Y qué significa esto? Que cada línea de código que escribas puede acabar en manos del mayor número de personas del mundo.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Consejo: los genes de código abierto de Android

{class="mt-1"}
El núcleo de Android (AOSP, Android Open Source Project) es de código abierto: cualquier fabricante puede tomarlo y personalizarlo. Por eso Xiaomi tiene MIUI (hoy HyperOS), Huawei su capa de compatibilidad con HarmonyOS y Samsung One UI. Para los desarrolladores es una buena noticia: aprendes "desarrollo Android", no "desarrollo de una marca"; un solo oficio, todos los móviles.
:::

La evolución de los números de versión también tiene su gracia: desde el Cupcake de la versión 1.5, cada versión grande llevaba nombre de postre (Donut, Eclair, Frozen Yogurt, Gingerbread...) hasta que Android 10, en 2019, pasó a números secos. A agosto de 2026, la versión estable más reciente es Android 17, y la "versión mínima soportada" que de verdad te importa al desarrollar suele situarse, en las apps habituales, entre Android 8 (API 26) y Android 10 (API 29): soportando los dispositivos de hace unos años, tu público será lo bastante grande.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Versión</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Nombre en clave/año</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Lo importante para el desarrollador</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 8 (API 26)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Oreo · 2017</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Canales de notificación y límites en segundo plano: la línea mínima de muchos móviles antiguos</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 10 (API 29)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2019</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Llega el almacenamiento por particiones y cambian mucho las reglas de acceso a archivos</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 12 (API 31)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2021</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Material You trae los colores dinámicos y renueva de arriba abajo el aspecto de la interfaz</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 13 (API 33)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2022</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Permiso de notificaciones en tiempo de ejecución: una ventana te pregunta si te deja enviar notificaciones</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 14-15 (API 34-35)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2023-2024</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Volver atrás predictivo, páginas de 16 KB y privacidad aún más estricta</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 16-17 (API 36-37)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2025-2026</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ritmo más rápido de versiones menores e integración de capacidades de IA (como la extensión de Gemini)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Breve historia de las versiones de Android (a agosto de 2026, con lo más relevante para el desarrollo)

#### II. ¿Con qué lenguaje se escribe: Java o Kotlin?

En la historia del desarrollo Android hubo dos lenguajes principales. Java es el "padre fundador": se usó desde el nacimiento de Android. Kotlin fue nombrado "ciudadano de primera clase" por Google en 2017 y, desde 2019, la postura oficial es "Kotlin primero" (Kotlin-first). Para 2026, casi todos los proyectos nuevos usan Kotlin, y los antiguos también van migrando poco a poco.

Siendo sinceros: si partes de cero absoluto, aprende Kotlin directamente y no vuelvas a mirar Java. Tres motivos: primero, el código Kotlin es un 30%-40% más corto que Java (la misma función, más breve y más clara); segundo, evita de nacimiento el "puntero nulo", esa pesadilla de los novatos; tercero, todos los tutoriales modernos, la documentación oficial y las herramientas de programación con IA (¿recuerdas nuestro libro de IA?) toman Kotlin como referencia. Java solo lo encontrarás al mantener proyectos antiguos o leer código viejo.

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
Estilo Java (versión prolija)

{class="font-mono text-xs leading-relaxed"}
public class MainActivity extends Activity {<br>&nbsp;&nbsp;@Override<br>&nbsp;&nbsp;protected void onCreate(Bundle b) {<br>&nbsp;&nbsp;&nbsp;&nbsp; super.onCreate(b);<br>&nbsp;&nbsp;&nbsp;&nbsp; setContentView(R.layout.activity);<br>&nbsp;&nbsp;}<br>}
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
Estilo Kotlin (versión limpia)

{class="font-mono text-xs leading-relaxed"}
class MainActivity : ComponentActivity() {<br>&nbsp;&nbsp;override fun onCreate(b: Bundle?) {<br>&nbsp;&nbsp;&nbsp;&nbsp; super.onCreate(b)<br>&nbsp;&nbsp;&nbsp;&nbsp;setContent { App() }<br>&nbsp;&nbsp;}<br>}
:::
:::

Para hacer lo mismo, Kotlin se ahorra un montón de llaves y código de relleno. En el capítulo 50 lo estudiaremos en serio; por ahora solo recuerda: el "idioma común" del desarrollo Android se llama Kotlin.

#### III. ¿Cómo nace una app?

Mucha gente cree que "desarrollar una app" es abrir el ordenador y escribir código sin parar. En realidad, desde la idea hasta el móvil del usuario, una app pasa más o menos por esta cadena de montaje:

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-lightbulb mr-1"></i> Idea</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center">📐 Diseño (interfaz + funciones)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-keyboard mr-1"></i> Escribir código</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hammer mr-1"></i> Compilar y empaquetar (APK/AAB)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> Probar (emulador y dispositivo real)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-rocket mr-1"></i> Publicar (tienda/instalador)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figura 1: El flujo completo de una app de Android, desde la idea hasta su publicación
:::

En esta cadena hay dos conceptos que conviene conocer ya:

- APK: el formato de paquete de instalación de las apps de Android (.apk); con solo abrirlo se instala en el móvil, como el .exe de Windows. Para tus pruebas de cada día y para pasárselo a amigos, usa este.
- AAB: Android App Bundle (.aab), el "formato de empaquetado avanzado" para publicar en Google Play. La tienda lo recorta dinámicamente según el modelo de móvil de cada usuario, para que cada quien descargue un paquete más pequeño. No sirve para instalártelo tú mismo: solo se entrega a la tienda.

Además, escucharás una y otra vez una palabra: SDK (Software Development Kit, kit de desarrollo de software). Es todo el "equipo de desarrollo" que ofrece la plataforma oficial de Android: librerías de API de cada versión, herramientas de depuración, imágenes de emulador, etc. Clases como Activity o Button que llamas al programar vienen todas del SDK.

#### IV. Panorama de la pila tecnológica de Android: tu "lista de armas"

Antes de estudiar en serio, conoce la configuración estándar de los proyectos Android dominantes en 2026. No pasa nada si ahora no la entiendes: al terminar el libro, volverás aquí y lo verás todo claro:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Capa</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Elección dominante (2026)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Para qué sirve</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lenguaje</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin 2.x</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">El lenguaje para escribir la lógica</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Interfaz</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Jetpack Compose + Material 3</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Dibujar la interfaz con código (el eje de este libro)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Arquitectura</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MVVM + ViewModel</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Separar interfaz y lógica para que el código no se vuelva un lío</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Almacenamiento de datos</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room (base de datos) + DataStore (configuración)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Guardar datos en el móvil</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Red</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit + OkHttp + corrutinas de Kotlin</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Hablar con el servidor</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Herramienta de compilación</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gradle + Kotlin DSL</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Convertir el código en el paquete instalable</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Entorno de desarrollo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android Studio</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">El IDE "todo en uno" oficial de Google</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Vistazo rápido a la pila tecnológica dominante de Android en 2026

Que no te asuste esa sarta de términos en inglés. Son como las ollas y sartenes de una cocina: por ahora basta con saber que "para cocinar hay que entrar en la cocina"; el uso de cada herramienta te lo iré desmenuzando capítulo a capítulo. Y la buena noticia: al crear un proyecto nuevo, Android Studio te configura todo este conjunto automáticamente; tú solo preocúpate de guisar.

#### V. Android frente a iOS: la primera "lección de elegir bando" del desarrollador

Puede que tengas entre manos dispositivos Android y Apple a la vez. Como desarrollador, conviene conocer de antemano las diferencias de experiencia entre ambos lados. No es un "cuál es mejor" para tomar partido, sino la cuenta real de "por dónde te conviene empezar":

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Dimensión</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Desarrollo Android</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Desarrollo iOS</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ordenador de desarrollo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sirve Windows, Mac o Linux</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Imprescindible Mac (Xcode es exclusivo)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Herramienta de desarrollo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android Studio (gratis)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode (gratis) + cuota anual de publicación de 99 dólares</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Revisión de publicación</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Laxa, de unas horas a unos días</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Estricta, entre 1 y 7 días es lo habitual</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Prueba libre en el dispositivo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Se pueden publicar e instalar APKs libremente</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Distribución restringida; para probar hacen falta firma/TestFlight</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Entorno de ingresos</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sobre todo publicidad y canales chinos</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mejores hábitos de pago en compras dentro de la App Store</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Curva de aprendizaje</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Más conceptos (los cuatro componentes principales, etc.)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ecosistema cerrado pero de sistema unificado y documentación excelente</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Comparación de las rutas de desarrollo de Android e iOS (agosto de 2026)

Siendo sinceros: si tu ordenador no es un Mac, esta pregunta ni se plantea, porque Android es la única opción. Si tienes un Mac, puedes leer las partes ocho y nueve de este libro en paralelo: la forma de programar es la misma y, tras aprender una, la otra te costará mucho menos.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Manos a la obra: mira el "Android" de tu móvil

{class="mt-1"}
Abre en tu móvil [Ajustes] → [Acerca del teléfono] (o "Información del teléfono") y busca la línea "Versión de Android": si la tocas varias veces seguidas, se activa el minijuego secreto del sistema. Anota tu número de versión y compáralo con la tabla de versiones de arriba para ver a qué generación pertenece. Tu móvil es tu primera "máquina de pruebas de desarrollo".
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumen del capítulo

- Android nació en 2008 y en 2026 es el sistema móvil con mayor cuota de mercado del mundo, con miles de millones de dispositivos activos
- La última versión oficial es Android 17; las apps principales piden como mínimo Android 8-10 para cubrir una base de usuarios lo bastante grande
- En los proyectos nuevos, Kotlin siempre: un 30 % menos de código, protección contra punteros nulos y la elección oficial
- El APK se instala por tu cuenta, el AAB va a la tienda; el SDK es el kit oficial de desarrollo
- La pila tecnológica estándar de 2026: Kotlin + Compose + MVVM + Room + Retrofit + Gradle + Android Studio
:::
