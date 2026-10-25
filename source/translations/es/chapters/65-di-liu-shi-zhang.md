---
id: di-liu-shi-zhang
num: 60
part: ios-kai-fa-pian
nav: Capítulo 60: Preparar el entorno de desarrollo: Xcode y el primer proyecto
toc: default
kind: chapter
---

### Capítulo 60: Preparar el entorno de desarrollo: Xcode y el primer proyecto

{class="chapter-intro mb-4"}
Para hacer bien el trabajo, primero afila tus herramientas. En este capítulo montaremos la "cocina": instalaremos Xcode, haremos funcionar el simulador, crearemos el primer proyecto iOS de tu vida y desmenuzaremos la estructura del proyecto hasta entenderla. Con el entorno listo, verás por primera vez cómo tu código se convierte en un botón que puedes pulsar; ese instante mucha gente lo recuerda toda la vida.

#### 1. Consigue un Mac

Empecemos por el requisito: el desarrollo iOS debe hacerse sobre macOS. Si no tienes Mac, hay tres opciones: comprar uno (un Mac mini o un MacBook Air de segunda mano bastan), alquilar un Mac en la nube a corto plazo, o leer primero la octava parte, "Desarrollo Android en la práctica" (se puede con Windows).

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Componente</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Mínimo</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Zona cómoda (recomendado)</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Chip</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple Silicon (M1 o superior)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">M2 o más nuevo</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Memoria</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">8GB</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">16GB</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Disco</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Reservar 40 GB o más (Xcode ocupa mucho)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Desde 256 GB</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sistema</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">El macOS más reciente</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mantener las actualizaciones automáticas</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Referencia de configuración de un Mac de desarrollo (agosto de 2026)

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Consejo: sin Mac también puedes empezar con el lenguaje

{class="mt-1"}
La app gratuita Swift Playgrounds en el iPad permite aprender lo básico de Swift (sin Mac); incluso se puede instalar en el iPhone. Practica en Playgrounds el lenguaje del capítulo 61 y, cuando tengas tu Mac, despega directo. Afilar el hacha no retrasa la tala: de eso se trata.
:::

#### 2. Instalar Xcode

Xcode es el entorno de desarrollo integrado oficial de Apple, y es gratis. Se instala en tres pasos:

1. Abre el App Store en el Mac, busca "Xcode" y pulsa instalar; ojo, pesa varios GB, así que elige una franja con buena conexión;
2. Al abrirlo por primera vez tras la instalación, acepta el acuerdo y deja que se instalen los componentes (se hace solo);
3. En el menú Xcode → Settings → Locations, comprueba que Command Line Tools esté seleccionado; las herramientas de línea de comandos son requisito de muchos scripts y herramientas de terceros.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Atención: el juego de emparejar versión y sistema

{class="mt-1"}
El Xcode nuevo suele exigir el macOS más reciente, y los Mac viejos se quedan atascados en versiones antiguas. Para publicar en el App Store, Apple exige compilar con un Xcode relativamente nuevo (suele dar un plazo de gracia). Así que no demores demasiado las actualizaciones del sistema: los desarrolladores iOS son de los que con más puntualidad siguen las versiones nuevas.
:::

#### 3. Crea tu primer proyecto

Abre Xcode → Create New Project → elige iOS → plantilla App, y luego rellena:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Campo</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Qué rellenar</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Explicación</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Product Name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstApp</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Nombre de la app</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Team</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tu Apple ID (gratuito)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Para la firma; con una cuenta personal basta</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Organization Identifier</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">com.example</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Se combina con el Product Name para formar el identificador del paquete</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Interface</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">El framework eje de este libro</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Language</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">No necesita explicación</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Los cinco campos al crear un proyecto

Al pulsar Create, Xcode genera un proyecto que corre directamente. Elige un simulador arriba a la izquierda (por ejemplo, iPhone 17) y pulsa ▶ para ejecutar: a los pocos segundos, en la pantalla del simulador aparece una ventana con el texto "Hello, world!". Tu primera App iOS acaba de nacer.

#### 4. Anatomía del proyecto: para qué sirve cada archivo

A la izquierda está el navegador del proyecto; como principiante solo necesitas conocer estos:

::: div .figure
```html
<svg style="max-width:100%;height:auto" width="600" height="290" viewBox="0 0 600 290" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="600" height="290" fill="#fafafa" rx="8"/>
      <text x="20" y="28" font-size="13" font-weight="bold" fill="#111827">MyFirstApp/ raíz del proyecto</text>
      <rect x="30" y="42" width="540" height="225" fill="#ffffff" stroke="#d1d5db" rx="6"/>
      <rect x="45" y="56" width="250" height="196" fill="#eef2ff" rx="5"/>
      <text x="56" y="78" font-size="11" fill="#1e1b4b" font-weight="bold">MyFirstApp/ (carpeta de código)</text>
      <text x="66" y="100" font-size="10" fill="#374151">├ MyFirstAppApp.swift  ← punto de entrada</text>
      <text x="66" y="120" font-size="10" fill="#374151">├ ContentView.swift  ← pantalla principal</text>
      <text x="66" y="140" font-size="10" fill="#374151">└ Assets.xcassets  ← iconos, imágenes, colores</text>
      <text x="56" y="166" font-size="10" fill="#6b7280">(los archivos nuevos van en esta carpeta)</text>
      <text x="56" y="196" font-size="10" fill="#1e1b4b" font-weight="bold">pestaña Info / Info.plist</text>
      <text x="66" y="216" font-size="10" fill="#6b7280">declaración de la app: nombre, permisos, ajustes</text>
      <rect x="310" y="56" width="245" height="196" fill="#f0fdf4" rx="5"/>
      <text x="321" y="78" font-size="11" fill="#065f46" font-weight="bold">otros lugares importantes</text>
      <text x="331" y="100" font-size="10" fill="#374151">📁 Preview Content/  ← material de previsualización</text>
      <text x="331" y="122" font-size="10" fill="#374151"><i class="fas fa-bullseye mr-1"></i> ajustes del Target (icono azul del proyecto)</text>
      <text x="331" y="142" font-size="10" fill="#6b7280">——aquí están la versión, el sistema mínimo y la firma</text>
      <text x="331" y="168" font-size="10" fill="#374151"><i class="fas fa-flask mr-1"></i> MyFirstAppTests/  ← pruebas unitarias</text>
      <text x="331" y="188" font-size="10" fill="#374151">📱 MyFirstAppUITests/ ← pruebas de interfaz</text>
      <text x="331" y="216" font-size="10" fill="#9ca3af">(la plantilla de tests ya está generada, se usa en el cap. 67)</text>
    </svg>
```

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figura 2: la estructura de un proyecto Xcode que todo principiante debe conocer
:::

- MyFirstAppApp.swift: el punto de entrada del programa; en SwiftUI tiene solo unas líneas: "arranca y muestra la pantalla principal";
- ContentView.swift: la vista de la pantalla principal; todo lo que ves ahora vive aquí;
- Assets.xcassets: el almacén de recursos; iconos, imágenes y colores van aquí;
- Ajustes del Target: entra con el icono azul del proyecto a la izquierda; ahí están el número de versión, la versión mínima de iOS y la firma. El nombre visible de la App y el icono también se configuran aquí.

#### 5. Trucos de eficiencia en Xcode: los cinco "power-ups" de atajos para principiantes

Dominando estos parecerás "muy profesional":

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Acción</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Atajo</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Función</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ejecutar</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘R</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Compilar y arrancar</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Abrir o alternar la vista previa del canvas</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌥⌘↩</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">El interruptor del "lo que ves es lo que obtienes"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Formatear la sangría</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌃I</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Reordena automáticamente la sangría del código seleccionado</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Abrir archivos rápido</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘O</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Escribe el nombre del archivo y se abre al instante (¡el más usado!)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Comentar o quitar comentarios</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Activar o desactivar código al vuelo mientras depuras</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Atajos de Xcode de uso frecuente (el kit de cinco del principiante)

Dos regalos ocultos más: varios simuladores a la vez (ejecutar iPhone e iPad al mismo tiempo para comparar diseños) y la biblioteca de fragmentos de código (arrastra esas líneas que usas mucho al panel Snippets de la derecha y la próxima vez insértalas con un clic); usa primero las herramientas de eficiencia y la soltura llega sola.

#### 6. Depurar en un dispositivo real: instalar la App en tu iPhone

El simulador está bien, pero el dispositivo real es la meta. Con un Apple ID gratuito también puedes depurar en un móvil real:

1. Conecta el iPhone con el cable de datos (o depura por Wi-Fi en la misma red);
2. En la lista de dispositivos de la parte superior de Xcode elige tu móvil; la primera vez pedirá iniciar sesión con tu Apple ID y configurará la firma automáticamente;
3. En el iPhone: [Ajustes] → [General] → [VPN y gestión de dispositivos] → confía en tu certificado de desarrollador;
4. Pulsa ▶ y la App se instala en el dispositivo real.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Atención: la "limitación de siete días" de la cuenta gratuita

{class="mt-1"}
Las Apps firmadas con un Apple ID gratuito caducan a los 7 días (basta volver a ejecutar una vez para renovarlas). Es el mecanismo de Apple contra el abuso, y para aprender sobra; la cuenta de desarrollador de pago (99 USD al año) no tiene esta limitación, como se detalla en el capítulo 67.
:::

#### 7. Primera prueba + primeros auxilios para errores comunes

Abre ContentView.swift, cambia el texto de Text("Hello, world!") por tu nombre y pulsa ⌘R para volver a ejecutar: a los pocos segundos tu nombre aparece en el simulador. Enhorabuena: acabas de completar tu primer ciclo completo de "cambiar código → compilar → instalar → ejecutar".

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Síntoma del error</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Causa habitual</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Remedio</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Error de Signing</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Team sin elegir o certificado caducado</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">En Target → Signing, marca tu cuenta; con cuenta gratuita, vuelve a ejecutar una vez</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">El simulador se queda en negro o no abre</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Imagen dañada</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menú Device → Erase All Content; o borra el simulador y vuelve a añadirlo</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode descarga lento o no se instala</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Inestabilidad de red del App Store</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cambia de franja horaria; o descarga el paquete .xip desde el sitio de desarrolladores de Apple</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Tabla de primeros auxilios para errores de entorno del principiante

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Manos a la obra: completa tu lista de "ritos de desarrollador"

{class="mt-1"}
① Instala Xcode y haz funcionar el simulador; ② ejecuta tu App una vez en un dispositivo real y guarda la captura como recuerdo; ③ cambia el texto de Hello por tu nombre; ④ en los ajustes del Target, cambia el nombre visible de la App a "Mi primera App". Con estos cuatro pasos, ya eres alguien con una obra propia.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumen del capítulo

- Requisito duro: Mac + Xcode; sin Mac, empieza aprendiendo el lenguaje con Swift Playgrounds en el iPad
- Xcode se instala desde el App Store; las versiones nuevas exigen sistemas nuevos, no demores las actualizaciones
- Los cinco elementos al crear un proyecto: nombre, Team, identificador de organización, SwiftUI y Swift
- La regla del proyecto: el código vive en la carpeta MyFirstApp/; los ajustes del Target gestionan versión y firma
- La depuración en dispositivo real con Apple ID gratuito tiene el límite de firma de 7 días; la cuenta de pago no tiene esa restricción
- La rutina de desarrollo = cambiar código → ⌘R → ver el resultado, en bucle
:::
