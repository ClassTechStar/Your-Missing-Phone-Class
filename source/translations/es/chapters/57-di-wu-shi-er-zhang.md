---
id: di-wu-shi-er-zhang
num: 52
part: an-zhuo-kai-fa-pian
nav: Capítulo 52: Los cuatro componentes y el ciclo de vida de la Activity
toc: default
kind: chapter
---

### Capítulo 52: Los cuatro componentes y el ciclo de vida de la Activity

{class="chapter-intro mb-4"}
Si Compose es la "cara" de la app, este capítulo trata de su "esqueleto". Android tiene cuatro componentes básicos y toda app se monta con ellos; el más importante, la Activity, lleva consigo un "mapa del ciclo de vida" que todo desarrollador Android debe tener grabado en la cabeza. Al acabar el capítulo entenderás esos enigmas de siempre como "por qué mi app vuelve del segundo plano con el estado perdido".

#### 1. Los cuatro componentes: las vigas maestras de Android

Android define oficialmente cuatro componentes básicos, cada uno a cargo de un tipo de trabajo:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Componente</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Función</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Una comparación</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Activity</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Una interfaz visible</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">El escaparate de la tienda: el usuario lo ve y puede interactuar</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Service</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">El "invisible" que trabaja en segundo plano</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">El obrero del almacén: pone música, descarga archivos, no necesita interfaz</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">BroadcastReceiver</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Recibe avisos del sistema</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">La portería: el altavoz que anuncia "batería baja" o "se cortó la conexión"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ContentProvider</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Comparte datos entre apps</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">El archivador público: por ejemplo, presta los contactos a otras apps</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Vistazo rápido a los cuatro componentes de Android

En la etapa de principiante pasarás el 95 % del tiempo con la Activity; Service y BroadcastReceiver entran en juego al reproducir música o al lanzar notificaciones; ContentProvider es el menos usado (el sistema ya tiene bien envueltos los datos habituales). Y una cosa más: los cuatro componentes deben "empadronarse" en AndroidManifest.xml; si no consta el padrón, el sistema no los encuentra.

#### 2. El ciclo de vida de la Activity: el primer "mapa del tesoro" del desarrollo Android

Una app del móvil puede interrumpirse en cualquier momento: suena una llamada, el usuario se va un rato a WeChat, el sistema te mata por falta de memoria... La vida de una Activity es un viaje en bucle por este mapa:

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onCreate (nace: inicializa)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onStart (ya visible)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onResume (en primer plano, interactivo)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center">onPause (parcialmente tapado)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center">onStop (totalmente invisible)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center">onDestroy (destruido)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center">🔁 onRestart / onStart / onResume: al volver al primer plano, se repite el camino a la inversa</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figura 4: ciclo de vida de la Activity (sentido de avance: la fila de arriba es el nacimiento, la de abajo la salida; al volver se regresa por el mismo camino)
:::

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Retrollamada</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Cuándo se dispara</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Uso típico</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onCreate</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Al crear la Activity (una vez)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cargar la interfaz, preparar los datos</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onStart</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">La interfaz pasa a ser visible</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Arrancar alguna lógica ligera</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onResume</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Toma el foco y admite interacción</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Iniciar animaciones, reanudar la reproducción</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onPause</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Al quedar tapada en parte o al cambiar de app</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pausar animaciones, guardar borradores</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onStop</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ya del todo invisible</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Soltar recursos pesados, pausar descargas</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onDestroy</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Antes de ser destruida</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">La última limpieza</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Usos típicos de las seis retrollamadas del ciclo de vida

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Aviso para esquivar problemas: girar la pantalla "mata" la Activity

{class="mt-1"}
La caída más clásica del principiante: giras la pantalla y desaparece todo lo escrito en el campo de texto. Motivo: al girar, la Activity se destruye y se reconstruye por defecto (pasa por onDestroy → onCreate). Remedio: guardar el estado con rememberSaveable (el relevo de remember en Compose), que recupera los valores solo al reconstruir. Lo usaremos una y otra vez en los capítulos 6 y 7.
:::

#### 3. Intent: el "billete" para circular dentro y fuera de la app

El Intent (intención) es el "billete" con el que se comunican los componentes. Para saltar de una pantalla a otra, o abrir el navegador o la cámara, toca "comprar billete y subir":

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Navegar con Intent</span><span class="dots">···</span>
:::

```
// forma 1: Intent explícito — se indica claramente a qué página ir
val intent = Intent(this, DetailActivity::class.java)
intent.putExtra("name", "Luis")     // lleva "equipaje" en el coche (los datos)
startActivity(intent)

// forma 2: Intent implícito — solo dices qué hacer y el sistema busca quién lo hace
val web = Intent(Intent.ACTION_VIEW, Uri.parse("https://developer.android.com"))
startActivity(web)   // el sistema abrirá el navegador (o te dejará elegir)
```
:::

Cada modalidad tiene su terreno: el explícito sirve para saltos entre pantallas de tu propia app; el implícito, para usar capacidades del sistema o de otras apps (abrir webs, llamar por teléfono, compartir). En proyectos con Compose, coge el Context en el Composable con LocalContext.current y ya puedes hacer startActivity.

#### 4. Varias pantallas y navegación

Las apps de verdad tienen varias pantallas. El esquema de navegación recomendado oficialmente en Compose es Navigation Compose (la biblioteca androidx.navigation):

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Esqueleto de Navigation Compose</span><span class="dots">···</span>
:::

```
val navController = rememberNavController()

NavHost(navController, startDestination = "home") {
    composable("home") { HomeScreen(navController) }
    composable("detail/{name}") { entry ->
        val name = entry.arguments?.getString("name")
        DetailScreen(name ?: "Desconocido")
    }
}

// para navegar desde la pantalla:
navController.navigate("detail/Luis")     // con parámetro
navController.popBackStack()              // volver a la página anterior
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Consejo: ¿y cuando las pantallas son muchas?

{class="mt-1"}
Cuando el proyecto crezca, reúne todas las rutas de pantallas en un único archivo (por ejemplo, AppNavGraph.kt) y gestiónalas desde ahí; no dejes la lógica de "a dónde saltar" esparcida por cada pantalla. Es el primer paso de "funciona" a "se puede mantener".
:::

#### 5. De regalo, conocer: qué es un Fragment (y por qué este libro no lo enseña)

Rastreando tutoriales viejos te toparás seguro con el Fragment: un "fragmento de interfaz reutilizable" dentro de la Activity, protagonista absoluto de las arquitecturas multipantalla antiguas. Pero en la era de Compose basta con funciones Composable + rutas de Navigation, y Google ya le ha bajado el protagonismo. Por eso este libro no lo mete en su línea principal.

Mi consejo: en los proyectos nuevos no lo uses por iniciativa propia; con saber que es "un fragmento de interfaz incrustado en la Activity" te basta para leer código antiguo o salir del paso en una entrevista. A la hora de elegir material de estudio, prioriza siempre lo publicado desde 2023 en adelante: el "almanaque" del stack de Android caduca más rápido de lo que parece.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Manos a la obra: dale "memoria" al contador

{class="mt-1"}
Retoca el contador del capítulo 51: ① sustituye remember por rememberSaveable y gira la pantalla para comprobar que el número sigue ahí; ② añade un botón "Acerca de" que salte con Navigation a una segunda pantalla donde se muestre el número de versión; ③ imprime registros (Log.d) en onCreate/onPause de las dos pantallas y observa en Logcat el orden en que se llaman los estados del ciclo de vida. Hechos estos tres pasos, el ciclo de vida deja de ser teoría de sobremesa.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumen del capítulo

- Los cuatro componentes: Activity (escaparate), Service (segundo plano), BroadcastReceiver (altavoz), ContentProvider (archivador)
- Las seis retrollamadas del ciclo de vida: onCreate → onStart → onResume → onPause → onStop → onDestroy
- Girar la pantalla destruye y reconstruye la Activity: salva el estado con rememberSaveable
- El Intent es el "billete": explícito para saltar a tus pantallas, implícito para las capacidades del sistema
- Varias pantallas con Navigation Compose: NavHost + rutas composable
:::
