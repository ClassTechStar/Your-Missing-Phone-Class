---
id: di-wu-shi-yi-zhang
num: 51
part: an-zhuo-kai-fa-pian
nav: Capítulo 51: Desarrollo de interfaces: primeros pasos con Jetpack Compose
toc: default
kind: chapter
---

### Capítulo 51: Desarrollo de interfaces: primeros pasos con Jetpack Compose

{class="chapter-intro mb-4"}
La interfaz es todo lo que el usuario ve. Antes de llegar Compose, las interfaces de Android se escribían en XML, tedioso como un ejercicio de rellenar huecos; en 2021 Google presentó Jetpack Compose: la interfaz se "dibuja" directamente con código Kotlin, ves lo que haces y, al tocar una línea de código, la vista previa se refresca al instante. Para 2026, Compose ya era la corriente mayoritaria absoluta en los proyectos nuevos. En este capítulo aprenderemos a "dibujar".

#### 1. La idea de Compose: la interfaz es una función

La idea central de Compose cabe en una frase: interfaz = función. Cada cosa que puede verse en pantalla (texto, botones, imágenes) es una "función composable" (Composable), marcada con @Composable. Anidarlas como piezas de un juego de construcción da como resultado la interfaz.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Primera interfaz con Compose</span><span class="dots">···</span>
:::

```
@Composable
fun Greeting(name: String) {
    Text(text = "¡Hola, $name!")     // un "bloque de texto"
}

// composición anidada: bloques grandes que contienen bloques pequeños
@Composable
fun HomeScreen() {
    Column {                          // apilados en vertical
        Greeting(name = "Luis")
        Greeting(name = "María")
        Button(onClick = { /* qué hacer al pulsar */ }) {
            Text("Púlsame")
        }
    }
}
```
:::

Fíjate en ese "sombrero" llamado @Composable: le dice al compilador "esto es una pieza de interfaz". Las piezas se pueden anidar sin límite, y ese es todo el secreto de Compose.

#### 2. Componentes básicos: texto, botón, campo de texto e imagen

Los componentes de Compose son "bloques de construcción"; los cuatro más habituales:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Componente</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Qué hace</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Parámetros imprescindibles</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mostrar texto</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">text (el texto a mostrar)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Botón</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onClick (retrollamada al pulsar)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Campo de texto</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">value y onValueChange (retrollamada al cambiar la entrada)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Image</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mostrar imagen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">painter (recurso de imagen)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Los cuatro componentes básicos de Compose

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Ejemplo de componentes básicos</span><span class="dots">···</span>
:::

```
@Composable
fun BasicWidgets() {
    Column {
        Text(text = "Esto es un texto")
        Button(onClick = { println("¡Pulsado!") }) {
            Text("Botón")
        }
        var input by remember { mutableStateOf("") }
        TextField(
            value = input,
            onValueChange = { input = it },
            label = { Text("Escribe algo") }
        )
    }
}
```
:::

En las líneas del campo de texto aparece remember { mutableStateOf("") }: es la magia del "estado" de Compose, que detallamos en la quinta sección de este capítulo. Por ahora basta con que te suene.

#### 3. El trío de maquetación: Column, Row y Box

Ya tienes los componentes, ¿cómo se colocan? Recuerda tres "cajas":

- Column: apila en vertical (como la cola del comedor);
- Row: alinea en horizontal (como sentados lado a lado);
- Box: coloca en capas (como un mazo de cartas apiladas; ideal para insignias y superposiciones).

::: div .code-block
:::inline div .code-head
<span>KOTLIN · El trío de layouts</span><span class="dots">···</span>
:::

```
Column {
    Text("Primera fila")
    Row {
        Text("Izquierda")
        Text("Derecha")
    }
    Box {
        Text("Capa inferior")
        Text("etiqueta superpuesta encima")
    }
}
```
:::

¿Quieres un diseño más bonito? Añade a los componentes Modifier (modificador): es como "maquillar" las piezas:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Modifier: trucos habituales</span><span class="dots">···</span>
:::

```
Text(
    text = "Texto bonito",
    modifier = Modifier
        .padding(16.dp)          // margen en los cuatro lados
        .fillMaxWidth()          // ocupa todo el ancho
        .background(Color.Blue)  // color de fondo
        .clickable { /* al pulsar */ }// se puede pulsar
)
// llamadas encadenadas: una tras otra; el orden importa (primero padding y luego fondo; el fondo no incluye el margen)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Atención: el orden de Modifier importa

{class="mt-1"}
padding(16.dp).background(Blue) y background(Blue).padding(16.dp) no dan el mismo resultado: el primero es "primero margen, luego pintura" (el fondo no incluye el margen) y el segundo, "primero pintura, luego margen" (el fondo sí lo incluye). Aquí es donde los principiantes más dibujan "bordes blancos raros". Si dudas, invierte el orden y prueba: la vista previa te dará la respuesta al instante.
:::

#### 4. Estado: que la interfaz cobre "vida"

Una interfaz estática es sosa. Para que un botón sume +1 al pulsarlo o que un campo admita escribir, hace falta estado (State). La regla de Compose: la interfaz refleja siempre fielmente el estado; si el estado cambia, la interfaz se redibuja sola.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Estado: contador de clics</span><span class="dots">···</span>
:::

```
@Composable
fun Counter() {
    // remember + mutableStateOf: recuerda este valor que cambia
    var count by remember { mutableStateOf(0) }

    Column {
        Text(text = "Has pulsado $count veces")
        Button(onClick = { count++ }) {   // cambia el estado
            Text("Púlsame +1")                // la interfaz se actualiza sola
        }
    }
}
```
:::

Tres líneas de código y tienes un contador vivo. Ahí está lo agradable de Compose frente a la forma antigua: no hay que "refrescar la interfaz" a mano, basta con cambiar los datos. Recuerda dos funciones clave: remember (evita que el valor se borre al recomponerse la interfaz) y mutableStateOf (avisa a Compose de que "este valor cambió y toca redibujar").

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hand-pointer mr-1"></i> El usuario pulsa</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> Cambia el estado (count++)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> Compose detecta el cambio</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> Redibuja la interfaz (recomposición)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figura 3: el flujo de datos unidireccional "estado → interfaz" de Compose
:::

#### 5. Temas y modo oscuro: se configura una vez y manda en toda la app

El MyFirstAppTheme { ... } del proyecto de plantilla es el tema. Se apoya en las directrices de diseño Material 3 y te ayuda a llevar colores, tipografías y formas con un mismo criterio. Dar soporte al modo oscuro solo exige tres pasos:

1. definir en el tema las dos paletas, clara y oscura (la plantilla ya genera sola el ColorScheme);
2. isSystemInDarkTheme() detecta solo cuando el sistema pasa al modo oscuro;
3. usar los colores que da el tema (por ejemplo, MaterialTheme.colorScheme.primary) en vez de valores clavados a mano.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Consejo: el color dinámico de Material 3

{class="mt-1"}
"Material You", que existe desde Android 12, permite a la app sacar colores de tu fondo de pantalla. Las plantillas de Compose lo traen por defecto (dynamicColor). Tu app se "cambiará de traje" sola en el móvil de cada usuario: esa es la poesía del Android moderno.
:::

#### 6. Vista previa, animaciones y edición en vivo: los "extras" de Compose

Tres "extras" de Compose para la experiencia de desarrollo: una vez probados, ya no hay vuelta atrás:

- Vista previa con @Preview: al añadir la anotación @Preview a un Composable, Android Studio dibuja la interfaz al momento en el panel de la derecha: ves lo que escribes sin tener que instalar cada vez en el móvil;
- Edición en vivo (Live Edit): Android Studio en 2026 admite "recargar en caliente" ciertos cambios sobre el emulador o el dispositivo real; retoques pequeños como cambiar el color de un texto se ven al segundo en el dispositivo;
- APIs de animación: con unas pocas líneas de animateFloatAsState o AnimatedVisibility los elementos pasan de un estado a otro con suavidad; esa "sensación premium" suele estar a esas pocas líneas de distancia.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Animaciones en diez minutos</span><span class="dots">···</span>
:::

```
@Composable
fun AnimatedBox() {
    var big by remember { mutableStateOf(false) }
    // cuando el valor cambia, transita suavemente al valor objetivo
    val size by animateDpAsState(if (big) 120.dp else 60.dp)

    Box(Modifier
        .size(size)
        .background(MaterialTheme.colorScheme.primary)
        .clickable { big = !big }
    )
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Consejo: primero la función, luego la animación

{class="mt-1"}
El vicio típico del principiante es "apurar animaciones cuando la interfaz todavía no funciona". Primero logra que la función ande y deja los efectos para el final; también es el principio de "sencillez ante todo": la animación es la guinda, la función es el pastel.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Manos a la obra: crea un "botón del humor"

{class="mt-1"}
Transforma el proyecto de plantilla en un conmutador de humor: un botón que al pulsarlo rota entre 😀feliz → 😢triste → 😡enfadado, con el texto y el color de fondo cambiando al compás. Pista: usa when para elegir el texto y el color según el estado. Cuando lo acabes, pásaselo a tus amigos y recoge tu primera oleada de "vaya, ¿ya haces apps?".
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumen del capítulo

- La idea de Compose: interfaz = funciones @Composable anidadas como bloques
- Cuatro componentes básicos: Text / Button / TextField / Image
- Trío de maquetación: Column en vertical, Row en horizontal, Box en capas
- Modifier se "maquilla" en cadena: padding, fillMaxWidth, background, clickable; el orden importa
- El estado es el alma: remember + mutableStateOf; cambias los datos y la interfaz se redibuja sola
- Tema con Material 3 + color dinámico; el modo oscuro se configura una vez y manda en toda la app
:::
