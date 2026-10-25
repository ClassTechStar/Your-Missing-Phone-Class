---
id: di-wu-shi-liu-zhang
num: 56
part: an-zhuo-kai-fa-pian
nav: Capítulo 56: Pulir y publicar: pruebas, depuración y salida a Google Play
toc: default
kind: chapter
---

### Capítulo 56: Pulir y publicar: pruebas, depuración y salida a Google Play

{class="chapter-intro mb-4"}
Ya tienes la App, ¿y ahora qué? Este capítulo responde a las tres tareas que separan "que funcione" de "que esté lista para entregar": cómo depurar con eficacia para encontrar bugs, cómo escribir pruebas que eviten regresiones y cómo subir la App a Google Play para que todo el mundo la descargue. Publicarla no es solo un acto ceremonial: es la línea que separa una obra de un producto.

#### 1. Las tres herramientas de depuración: Logcat, puntos de interrupción e inspector de UI

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Herramienta</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Para qué sirve</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Cómo se usa</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Logcat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ver los registros del sistema o los tuyos propios</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">En el código escribe Log.d("TAG", "valor=$x") y filtra buscando el TAG en el panel</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Depuración con puntos de interrupción</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Detener el programa en una línea y ver los valores de las variables</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Haz clic junto al número de línea para que salga un punto rojo, ejecuta en modo Debug y avanza paso a paso</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Layout Inspector</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ver la estructura de la interfaz en ejecución</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menú Tools → Layout Inspector, para ver el árbol de componentes en tiempo real</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Las tres herramientas de depuración

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Consejo: ¿cómo leer un error?

{class="mt-1"}
Tras un cierre inesperado, en Logcat aparece un stacktrace en rojo. Busca de abajo hacia arriba la primera línea que empiece por el nombre de tu paquete (por ejemplo, com.example.yourapp); esa línea es casi siempre la escena del crimen. Mira primero el "tipo de Exception" (¿puntero nulo?, ¿conversión de tipos?) y luego el "at ... tuarchivo:línea". Este truco resuelve el 80% de los cierres inesperados.
:::

#### 2. Las pruebas: un seguro para tu código

Las pruebas manuales no son de fiar: arreglas una función y otra se rompe en silencio. Las pruebas son a la vez el remedio arrepentido y el chaleco antibalas. Las pruebas en Android se dividen en tres niveles; si empiezas, domina primero el primero:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Nivel</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Qué prueba</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Dónde va</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Velocidad</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pruebas unitarias</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lógica pura (cálculos, validaciones)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">app/src/test/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Segundos</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pruebas instrumentadas</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Comportamiento de la interfaz en un dispositivo real</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">app/src/androidTest/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Minutos</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pruebas manuales</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Percepción y experiencia de una persona real</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">——</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Siempre necesarias</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Los tres niveles de pruebas

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Ejemplo de prueba unitaria</span><span class="dots">···</span>
:::

```
// extrae a una función pura la lógica de "convertir el texto del importe en número"
fun parseAmount(input: String): Double? {
    val v = input.trim().toDoubleOrNull()
    return if (v != null && v > 0) v else null
}

// pruébala (JUnit4)
@Test
fun emptyInputReturnsNull() {
    assertEquals(null, parseAmount(""))
}
@Test
fun negativeReturnsNull() {
    assertEquals(null, parseAmount("-5"))
}
@Test
fun normalValueParses() {
    assertEquals(12.5, parseAmount("12.5"))
}
```
:::

La validación de importes y los cálculos estadísticos de tu app de gastos deberían estar cubiertos por pruebas unitarias. Para ejecutarlas: clic derecho en la carpeta test → Run. Si todo sale en verde, puedes cambiar el código con tranquilidad.

#### 3. Firma y empaquetado: ponerle el "sello" a tu App

Android exige que todos los paquetes de instalación estén firmados: es como un sello oficial que certifica "este paquete sale de mí y no ha sido alterado". Al depurar, Android Studio usa automáticamente la firma debug; para publicar necesitas tu propia firma release. El proceso:

1. Menú Build → Generate Signed Bundle / APK;
2. Crea el archivo keystore (almacén de claves): define una contraseña y guárdala bien;
3. Elige release y el formato AAB, y la compilación queda lista.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Advertencia: perder el keystore = perder la App

{class="mt-1"}
Para actualizar la App después de publicarla debes usar la misma firma; si no, la tienda rechazará la actualización. Si pierdes el archivo keystore o la contraseña, solo te queda publicar una app nueva desde cero, y los usuarios antiguos se quedan sin poder actualizar. Haz siempre una copia de seguridad del keystore y de la contraseña en un lugar seguro (nube cifrada + un bloc de notas): es una de las lecciones más caras para un desarrollador Android.
:::

#### 4. Todo el proceso para publicar en Google Play

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> Registrar cuenta de desarrollador</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-invoice mr-1"></i> Preparar material de la tienda</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-box mr-1"></i> Subir el AAB</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-clipboard-list mr-1"></i> Rellenar el formulario de seguridad de datos</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> Revisión (de horas a días)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-party-horn mr-1"></i> Publicar</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figura 6: los seis pasos para publicar en Google Play
:::

- Registro: una cuota única de 25 USD y una cuenta de Google que funcione;
- Material: icono de la app (512×512), capturas de pantalla (al menos 2), descripción de funciones y enlace a la política de privacidad (obligatorio si recopilas datos);
- Formulario de seguridad de datos: declara con honestidad qué datos recopilas; una app de gastos sin conexión puede declarar "cero recopilación";
- Revisión: la primera publicación de una cuenta nueva suele pasar por revisión humana, que tarda de horas a días; si la rechazan, corrige según los comentarios.

Nota para usuarios de China: Google Play requiere un entorno de red especial y la distribución en China continental suele hacerse a través de tiendas nacionales (Huawei, Xiaomi, MyApp de Tencent, etc.). El proceso para publicar en esas tiendas es parecido, pero cada una tiene sus propios criterios de revisión; el mismo AAB/APK puede distribuirse en varias tiendas. Para practicar, con lograr publicar en una ya ganas.

#### 5. Cómo crear el material de la tienda: la primera impresión son las descargas

La página de la tienda es el escaparate que ven los usuarios al pasear por ella. Tres elementos deciden la primera impresión:

- Icono: 512×512; no uses una captura de pantalla como parche. Si no tienes ojo de diseñador, genera con una herramienta de IA una figura geométrica sencilla; solo vale si se reconoce de un vistazo incluso en tamaño reducido en la pantalla de inicio del móvil;
- Capturas: al menos 2, mejor entre 4 y 6, mostrando las funciones más importantes; acompaña cada una con una frase en lenguaje humano ("registra un gasto en un segundo" es diez veces mejor que "una solución eficiente de contabilidad");
- Descripción: la primera frase debe dejar claro "qué es + para quién es"; no acumules calificativos como "el más profesional, el más potente": el posicionamiento en la búsqueda de la tienda depende sobre todo de las palabras clave y de la conversión de descargas; la sinceridad funciona mejor que la exageración.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Consejo: compara con los de tu mismo gremio

{class="mt-1"}
Antes de publicar, date una vuelta por las diez primeras apps parecidas a la tuya en la tienda y guarda capturas para comparar: ¿qué estilo tienen sus iconos?, ¿qué puntos fuertes muestran sus capturas?, ¿cómo redactan el título? Imitar no es plagiar: aprende las fórmulas y pon tu propio contenido; es la lección que más rápido arranca cualquier producto nuevo.
:::

#### 6. Lista breve de optimización de rendimiento y reporte de errores

Antes de publicar tu App, estas dos tareas merecen media hora cada una:

##### 1. Cuatro puntos de autochequeo de rendimiento

1. Usa LazyColumn para las listas: jamás montes una lista larga con Column; la carga diferida es la primera lección de rendimiento en Android;
2. No metas las imágenes en resolución original: usa la librería Coil para reescalar y cachear automáticamente; una imagen original de 5 MB basta para atascar un móvil de gama baja;
3. Evita el trabajo pesado en el hilo principal: base de datos, red y archivos grandes van dentro de corrutinas;
4. Mide con el Profiler: el analizador de rendimiento incluido en Android Studio muestra memoria, CPU y consumo de batería. Primero mide, después optimiza; no vayas por intuición.

##### 2. Reporte de errores

Que no se caiga en tus pruebas no significa que no se caiga en el móvil del usuario. Antes de publicar, integra Firebase Crashlytics (oficial de Google, gratis): con unas líneas de configuración, cuando la app se caiga se envía automáticamente el stacktrace y en el panel verás "qué modelo, qué versión y en qué línea se cayó". Publicar sin monitoreo de errores es conducir con los ojos cerrados.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Manos a la obra: "entrega" tu app de gastos una vez

{class="mt-1"}
① Añade 3 pruebas unitarias a la lógica, como parseAmount; ② provoca un fallo tú mismo, atrápalo con Logcat y arréglalo; ③ genera un APK firmado en release y envíalo a un amigo para que lo instale (ese es el verdadero ritual de "obra terminada"); ④ si te sobran fuerzas, crea una cuenta de desarrollador y envía de verdad la app a la tienda. Los tres primeros puntos puedes hacerlos esta misma noche.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumen del capítulo

- Las tres herramientas de depuración: Logcat para los registros, puntos de interrupción para las variables y Layout Inspector para la interfaz
- Leer un fallo: en el stacktrace, de abajo hacia arriba, busca la primera línea con el nombre de tu paquete
- Tres niveles de pruebas: unitarias (segundos, aprende estas primero) / instrumentadas / manuales
- Para publicar hay que firmar: haz copia del keystore y de la contraseña; si los pierdes, la App "cambia de dueño"
- Seis pasos para publicar: registro → material → subir el AAB → formulario de seguridad de datos → revisión → publicación
:::
