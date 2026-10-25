---
id: di-si-shi-jiu-zhang
num: 49
part: an-zhuo-kai-fa-pian
nav: Capítulo 49: Preparar el entorno de desarrollo: Android Studio y el primer proyecto
toc: default
kind: chapter
---

### Capítulo 49: Preparar el entorno de desarrollo: Android Studio y el primer proyecto

{class="chapter-intro mb-4"}
Para hacer bien la faena, primero afila las herramientas. En este capítulo montaremos la "cocina": instalaremos Android Studio, haremos funcionar el emulador, crearemos tu primer proyecto Android y desmontaremos la estructura del proyecto para entenderla bien. Con el entorno listo, verás por primera vez cómo tu código se convierte en un botón que se puede pulsar: hay mucha gente que recuerda ese instante toda la vida.

#### 1. Instalar Android Studio

Android Studio es el entorno de desarrollo integrado (IDE) oficial de Google: gratuito y con todo incluido, porque escribir código, ver vistas previas de la interfaz, depurar y empaquetar cabe todo dentro. Son cuatro pasos de instalación:

1. Abre la web oficial developer.android.com/studio y descarga la última versión estable (en agosto de 2026, la posterior a Narwhal; hay para Windows/Mac/Linux);
2. Ejecuta el instalador y dale a "Siguiente" todo el camino: el asistente incluye automáticamente el Android SDK y los componentes del emulador;
3. Al arrancar por primera vez, descarga los componentes del SDK como te pida el programa (con las casillas por defecto basta; puede llevar unos minutos y varios GB de espacio);
4. Al terminar verás la pantalla de bienvenida. Enhorabuena: la "cocina" ya está montada.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Atención: ten claros los requisitos de hardware

{class="mt-1"}
Android Studio es un gran "comememoria": se recomienda partir de 16 GB de RAM (con 8 GB funciona, pero el emulador se arrastra al abrirlo), reservar más de 20 GB de disco y tener una CPU con virtualización (activa VT-x/AMD-V en la BIOS). Si tu ordenador es de verdad antiguo, puedes sustituir el emulador por la "depuración en dispositivo real" (se explica en la cuarta sección de este capítulo); la experiencia resultará incluso más fluida.
:::

#### 2. Crear tu primer proyecto

En la pantalla de bienvenida pulsa New Project, elige la plantilla Empty Activity (la más limpia para principiantes) y rellena tres cosas:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Campo</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Qué poner</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Descripción</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">My First App</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">El nombre de la app, que se muestra en la pantalla de inicio del móvil</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Package name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">com.example.myfirstapp</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Identificador único en el mundo; la costumbre es "el dominio al revés"; por ahora, deja el valor por defecto</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Minimum SDK</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">API 26(Android 8.0)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Versión mínima soportada, cubre más del 95 % de los dispositivos</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Las tres cosas que hay que rellenar al crear un proyecto

Al pulsar Finish, Android Studio usará Gradle para descargar las dependencias y construir el proyecto automáticamente (la primera vez toca esperar unos minutos; después, mucho más rápido). Al terminar la construcción tendrás una app que funciona, aunque por ahora solo sabe mostrar un "Hello Android!".

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Consejo: los entresijos del nombre de paquete

{class="mt-1"}
El nombre de paquete (package name) es como el "DNI" de la app: no puede repetirse en todo el mundo y, una vez publicada, ya no puede cambiarse. Para practicar basta con com.example.xxx; en un producto real debe ser tu propio dominio al revés (por ejemplo, com.tunombre.nombredeapp). No publiques con com.example: la tienda lo rechazará.
:::

#### 3. Ponerlo en marcha: emulador y dispositivo real

El código ya está escrito; falta encontrar un "móvil" donde ejecutarlo. Tienes dos opciones:

##### 1. El emulador (Emulator)

El emulador crea un móvil Android virtual dentro del ordenador. En Android Studio abre Device Manager → Create Device, elige un dispositivo (se recomienda la serie Pixel) → escoge una imagen de sistema (una con Google APIs) → descárgala → arráncala. Luego pulsa el triángulo verde Run de la barra de herramientas y, a los pocos segundos, tu app aparecerá en la pantalla del "móvil".

##### 2. Depurar en dispositivo real (todavía más recomendable)

Un dispositivo real es siempre el entorno de pruebas más auténtico: el tacto del deslizamiento, la red de verdad, los sensores de verdad; nada de eso lo iguala un emulador. Depurar en un móvil Android real es muy sencillo:

1. En el móvil, abre [Ajustes] → [Acerca del teléfono] y toca 7 veces seguidas el "Número de compilación" para activar las "Opciones de desarrollador";
2. En [Opciones de desarrollador], activa la Depuración por USB;
3. Conecta el móvil al ordenador con un cable de datos y, en la ventana emergente del móvil, elige "Permitir depuración por USB";
4. Vuelve a Android Studio: tu móvil aparecerá en el desplegable de dispositivos de la barra de herramientas. Pulsa Run.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Aviso para esquivar problemas: no dejes la Depuración por USB siempre activada

{class="mt-1"}
La Depuración por USB equivale a abrir una "puerta trasera" en el móvil. Cuando cargues en lugares públicos o te conectes a ordenadores poco fiables, desactívala sin falta para que nadie pueda leer tus datos a través de ella. Apágala cada vez que termines de desarrollar; hazlo costumbre.
:::

#### 4. Desmontar la estructura del proyecto: para qué sirve cada archivo

La primera vez que abras el proyecto, el árbol de archivos de la izquierda puede marearte. Tranquilo: en el día a día, el 90 % de tu tiempo lo pasarás solo con estos:

::: div .figure
```html
<svg style="max-width:100%;height:auto" width="600" height="300" viewBox="0 0 600 300" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="600" height="300" fill="#fafafa" rx="8"/>
      <text x="20" y="30" font-size="13" font-weight="bold" fill="#111827">MyFirstApp/ raíz del proyecto</text>
      <rect x="30" y="45" width="540" height="230" fill="#ffffff" stroke="#d1d5db" rx="6"/>
      <text x="45" y="70" font-size="11" fill="#4f46e5" font-weight="bold">app/ ← donde escribes tu código</text>
      <rect x="60" y="82" width="240" height="178" fill="#eef2ff" rx="5"/>
      <text x="70" y="102" font-size="10" fill="#1e1b4b" font-weight="bold">src/main/</text>
      <text x="80" y="120" font-size="10" fill="#374151">├ java/…/MainActivity.kt  ← la lógica</text>
      <text x="80" y="138" font-size="10" fill="#374151">├ res/  ← recursos (imágenes, textos, colores)</text>
      <text x="80" y="156" font-size="10" fill="#374151">└ AndroidManifest.xml  ← la "cédula de identidad" de la app</text>
      <text x="70" y="180" font-size="10" fill="#1e1b4b" font-weight="bold">build.gradle.kts</text>
      <text x="80" y="198" font-size="10" fill="#6b7280">declara las librerías de las que depende (versión del SDK, Compose, etc.)</text>
      <text x="70" y="222" font-size="10" fill="#1e1b4b" font-weight="bold">src/androidTest/ y test/</text>
      <text x="80" y="240" font-size="10" fill="#6b7280">código de tests automatizados (se usa en el cap. 56)</text>
      <rect x="320" y="82" width="230" height="178" fill="#f0fdf4" rx="5"/>
      <text x="330" y="102" font-size="10" fill="#065f46" font-weight="bold">otros archivos de la raíz</text>
      <text x="340" y="122" font-size="10" fill="#374151">gradle/ + gradlew.bat  ← scripts de build</text>
      <text x="340" y="142" font-size="10" fill="#374151">settings.gradle.kts  ← ajustes del proyecto</text>
      <text x="340" y="162" font-size="10" fill="#6b7280">(regla de oro para novatos: toca solo la carpeta app/,</text>
      <text x="340" y="180" font-size="10" fill="#6b7280">por ahora trata lo demás como "caja negra", no lo toques)</text>
      <text x="340" y="208" font-size="10" fill="#9ca3af">.gitignore  ← lista de ignorados del control de versiones</text>
    </svg>
```

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figura 2: la estructura del proyecto que un principiante debe conocer (regla para recordar: solo se toca la carpeta app/)
:::

- MainActivity.kt: la "puerta principal" de la app. Cuando el usuario toca el icono, es lo primero que despierta. En la plantilla actual se encarga de mostrar "Hello Android!".
- AndroidManifest.xml: el "registro civil" de la app: declara cómo se llama, qué icono usa, qué pantallas tiene y qué permisos necesita (cámara, ubicación, etc.).
- La carpeta res/: el almacén de recursos, donde viven imágenes, iconos, textos y colores. Poner los textos en archivos de recursos en vez de dejarlos clavados en el código es una buena costumbre del desarrollo Android (facilita cambiar de idioma o de tema).
- build.gradle.kts: la receta de construcción: declara la versión mínima soportada y de qué bibliotecas se depende (por ejemplo, Compose).

#### 5. Primera prueba: cambia "Hello" por tu nombre

Abre MainActivity.kt y verás el código generado por la plantilla de Compose. Localiza la línea Text("Hello Android!"), cambia lo que va entre comillas por tu nombre (por ejemplo, Text("Hola, soy Ana, ¡esta es mi primera app!")) y pulsa Ctrl+R (Cmd+R en Mac) para volver a ejecutar. A los pocos segundos, tu nombre aparece en el emulador.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · MainActivity.kt (cambia esta línea)</span><span class="dots">···</span>
:::

```
setContent {
    MyFirstAppTheme {
        Surface(modifier = Modifier.fillMaxSize()) {
            // ▼ cambia aquí por tu propio texto
            Text("¡Hola, Luis! Esta es mi primera app")
        }
    }
}
```
:::

Enhorabuena: acabas de completar un ciclo entero de "cambiar código → compilar → instalar → ejecutar". Ese ciclo será el pan de cada día del desarrollo. Aprovecha la racha y prueba a cambiar algo más: sube el tamaño de la letra, cambia el color; en el próximo capítulo descubrirás de dónde sale esa "magia".

#### 6. Primeros auxilios con errores habituales: la "sala de urgencias" de tus dos primeras semanas

Montando el entorno y durante la primera compilación es muy probable que te cruces con estos tres errores. Tranquilo: todos tienen antídoto:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Síntoma del error</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Causa habitual</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Antídoto</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gradle sync failed / descarga lenta de dependencias</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mala conexión con los repositorios</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Configura en Gradle repositorios espejo (por ejemplo, los mirrors maven de Alibaba Cloud o Tencent Cloud); busca en internet "gradle mirror china" y aplica los cambios</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Faltan componentes del SDK</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Se saltó la descarga del SDK al instalar</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Settings → SDK Manager: instala las plataformas y herramientas que falten</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">El emulador no arranca / se queda en negro</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Virtualización sin activar o imagen dañada</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Activa VT-x/AMD-V en la BIOS; borra el emulador y créalo de nuevo; o pasa directamente a depurar en dispositivo real</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Tabla de urgencias de errores de entorno para principiantes

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Consejo: la metodología para buscar errores

{class="mt-1"}
La primera línea del mensaje de error es la más valiosa: cópiala tal cual en el buscador y añade la palabra clave "android studio". No busques preguntas tan genéricas como "no consigo montar el entorno"; busca errores concretos como "Gradle sync failed: Could not resolve com.android.tools.build". Solo las preguntas exactas reciben respuestas exactas.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Manos a la obra: completa tu lista de "ritos de desarrollador"

{class="mt-1"}
① Instala Android Studio y deja funcionando el emulador; ② ejecuta tu app una vez en un dispositivo real y guarda una captura de recuerdo; ③ cambia el texto Hello por tu nombre; ④ comprime el proyecto y guárdalo. Con los cuatro pasos hechos ya puedes anunciar a tus contactos: yo también soy desarrollador Android (con captura como prueba).
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumen del capítulo

- Android Studio = el IDE oficial y gratuito; se recomiendan 16 GB de RAM + 20 GB de disco + virtualización activada
- Los tres imprescindibles de un proyecto nuevo: nombre, nombre de paquete (único en el mundo, no publiques con com.example) y SDK mínimo (desde API 26)
- Dos formas de ejecutar: el emulador (un móvil virtual en el ordenador) y el dispositivo real (activa la Depuración por USB y recuerda apagarla al acabar)
- La regla del proyecto: solo se toca la carpeta app/: MainActivity.kt es la puerta principal, el Manifest el registro civil y res/ el almacén de recursos
- El día a día del desarrollo = cambiar código → Run → ver el resultado, una y otra vez
:::
