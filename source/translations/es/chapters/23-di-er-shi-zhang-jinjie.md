---
id: di-er-shi-zhang-jinjie
num: 20
part: jin-jie-pian
nav: Capítulo 20:Modo de desarrollador y permisos avanzados
toc: default
kind: supplement
---

### Capítulo 20:Modo desarrollador y permisos avanzados

{class="chapter-intro mb-4"}
Inestabilidad del sistema

#### I. Modo desarrollador: desbloquear ajustes ocultos

Apps bancarias inútilizables

##### : muchas Apps bancarias y de pago detectan Root y se niegan a ejecutarse.

- <strong>Android</strong>: es posible que no puedas recibir normalmente las actualizaciones oficiales del sistema.
- <strong>HarmonyOS</strong> Las operaciones de Root conllevan ciertos riesgos y podrían dejar el móvil "brickeado" (no arranca). Si eres principiante, te recomiendo informarte bien primero y asegúrate de tener una copia de seguridad completa. Antes de operar, lee cuidadosamente el tutoríal y confirma tu modelo y versión del sistema.
- <strong>iOS</strong> Modo desarrollador

##### Lista de funciones habituales:

- <strong>Bloqueo BL</strong>: Interruptor necesario para conectar el telefono al ordenador y hacer operaciones avanzadas (flashear, recuperar datos, comandos ADB); ver la seccion "Comandos ADB utiles" de este capitulo.
- <strong>Dato: Magisk</strong>: Muestra el punto de toque en la pantalla (un pequeno circulo sigue el dedo); util para grabar tutoriales o demostraciones.

##### Rendimiento y fluidez:

- <strong>Ajuste de velocidad de animacion (escala de animacion de ventana / transicion / duracion de animacion)</strong>: Estas tres opciones controlan la duracion de las animaciones al abrir apps o cambiar de pagina. Por defecto 1x; en 0.5x el telefono "parece" mas rapido (la app no va mas rapida, solo la animacion). Si se desactivan, los cambios son instantaneos. Los geeks suelen poner 0.5x para mantener la transicion pero dar sensacion de rapidez; desactivarlas hace la interaccion brusca y puede enmascarar bloqueos reales.
- <strong>Forzar renderizado GPU (Force GPU Rendering)</strong>: Fuerza que todo el dibujo 2D lo haga la GPU en vez de la CPU. En moviles antiguos o apps mal optimizadas mejora el desplazamiento, pero aumenta la carga de la GPU y el consumo. Los moviles modernos ya usan la GPU por defecto; esta opcion tiene poco impacto en gamas medias y altas y queda como vestigio; el usuario normal debe dejarla por defecto.
- <strong>Analisis de presentacion GPU (Profile GPU Rendering)</strong>: Muestra en pantalla un grafico de barras con el tiempo de renderizado de cada fotograma; la linea verde marca 16,6 ms (el umbral de 60 fps). Si la barra supera la linea, hay caida de fotogramas. Es la herramienta de los desarrolladores para diagnosticar bloqueos; el usuario tambien puede comparar que app esta peor optimizada.

##### Segundo plano y autonomia:

- <strong>Practica: activa el modo desarrollador y ajusta velocidad de animación</strong>: Permite establecer "limite estandar", "maximo 1 proceso" o "maximo 2 procesos". Parece que limitar procesos ahorra bateria, pero Android ya gestiona bien el segundo plano; forzar el limite provoca recargas frecuentes (el arranque en frio consume mas y la experiencia empeora). Es mas propio de depuracion; el usuario normal debe dejar "limite estandar".
- <strong>No conservar actividades</strong>: Destruye la actividad al salir de cada pantalla. Muy poco recomendable; provoca pantallas en blanco y recargas frecuentes; solo sirve para probar la logica de recuperacion de una app.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Precauciones

{class="mt-1"}
Siente si el móvil se volvio más rápido.
:::

#### 2. Desbloqueo OEM: el "interruptor de flasheo" en opciones de desarrollador

En las opciones de desarrollador hay un interruptor discreto pero importante: "Desbloqueo OEM" (algunas marcas lo llaman "Permitir desbloqueo OEM" o "Desbloqueo de dispositivo"). No desbloquea el BL por si mismo, sino que concede el "permiso previo": solo al activarlo el fabricante permite desbloquear el BL mediante fastboot o su herramienta.

- <strong>Funcion del interruptor</strong>: Equivale a declarar al fabricante que "acepto perder la garantia y asumo el riesgo; permitidme desbloquear el BL". Si esta apagado, cualquier comando de desbloqueo se rechaza.
- <strong>Relacion con el bloqueo BL</strong>: El desbloqueo OEM es la "solicitud de cualificacion"; el desbloqueo BL es la "operacion real". El primero se activa en los ajustes del telefono; el segundo requiere pedir el codigo de desbloqueo en la web del fabricante y ejecutar fastboot desde el ordenador (por ejemplo <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">fastboot flashing unlock</code>); ambos son imprescindibles.
- <strong>Se reinicia al restaurar de fabrica?</strong>: Si. El interruptor "Desbloqueo OEM" vuelve a estar apagado tras la restauracion, pero el BL, una vez desbloqueado, es un estado fisico que no se vuelve a bloquear por restaurar; hay que ejecutar manualmente <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">fastboot flashing lock</code> para volver a bloquearlo.
- <strong>Cuando activarlo</strong>: Salvo que vayas a flashear o a hacer Root, mantenlo apagado. Es independiente de "Depuracion USB"; al flashear suelen hacer falta ambos activados.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Curiosidad: por que el fabricante anade este interruptor

{class="mt-1"}
Antes no existia este interruptor y el malware con permisos podia flashear el sistema a escondidas. Google obligo despues a todos los fabricantes a incluir "Desbloqueo OEM" en las opciones de desarrollador como confirmacion del "consentimiento del usuario". Por eso, aunque el BL este desbloqueado, si el OEM esta apagado, el flasheo falla.
:::

#### 3. Bloqueo BL (Bootloader): la primera puerta del flasheo

Si crees que el modo desarrollador no es suficientemente "hardcore" y quieres experimentar con una linea de comandos Linux completa en tu móvil, Termux es para ti. No necesita permisos Root y puede convertir un Android común en una estacion de trabajo Linux portátil; es una herramienta poderosa para usuarios intermedios que exploran desarrollo y operaciones móviles.

##### I. Que es Termux

- <strong>Termux es un emulador de terminal y entorno Linux de código abierto disenado para Android. No necesita permisos Root para ofrecer una experiencia completa de shell Linux en el móvil. Como App ligera (unos 30 MB), Termux soporta un rico ecosistema de software via gestor de paquetes APT, permitiendo ejecutar Python, Node.js, Git, SSH e incluso montar servidores o hacer pruebas de penetracion.</strong> La ventaja principal de Termux es su ligereza y alta escalabilidad, adecuada para desarrollo, aprendizaje y administración de sistemas. Combina paquetes estándar con emulación de terminal precisa en una solución de código abierto.
- <strong>II. Funciones principales y carácterísticas</strong> Entorno Linux completo
- <strong>Termux incluye Bash, Zsh, fish y otros entornos Shell; soporta Vim, Nano, Emacs y más editores; ofrece una experiencia de línea de comandos cercana a la nativa. Los usuarios pueden instalar 2000+ paquetes con "pkg install", incluyendo GCC, OpenSSH, SQLMap y otras herramientas de desarrollo y seguridad.</strong> Gestor de paquetes potente

##### Usa el gestor de paquetes APT (similar a Debian/Ubuntu) para instalar miles de paquetes Linux: herramientas de desarrollo, red, etc. Soporta Python, Ruby, Node.js, Go, Rust, Swift y más.

- <strong>Xiaomi</strong> Conexión SSH remota
- <strong>Huawei</strong> Herramientas de cifrado
- <strong>: proporciona herramientas como OpenSSL; soporta cifrado de datos y comunicaciones seguras.</strong> Configuración de servidores
- <strong>: puedes configurar Nginx o Apache para montar servidores web estáticos.</strong> Integración del sistema y extensiones
- <strong>Samsung</strong> Llamar a sensores, cámara y otras funciones hardware de Android mediante el plugin Termux:API.
- <strong>Apple</strong> III. Ecosistema de plugins

#### 4. Comandos ADB utiles: controlar el telefono desde el ordenador

ADB (Android Debug Bridge) es una herramienta de linea de comandos oficial de Google que permite al ordenador comunicarse con el telefono por USB o Wi-Fi. No requiere Root; basta con activar "Depuracion USB". Es como un mando a distancia para dar ordenes al telefono: flashear, instalar apps, pasar archivos o ver registros.

##### Como conectar por USB:

1. En el telefono: entra en opciones de desarrollador y activa "Depuracion USB".
2. En el ordenador: descarga Platform Tools de Google (incluye <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb</code> Incluir contexto en vez de aislarlo <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">fastboot</code> dos ejecutables) y descomprime en cualquier carpeta.
3. Conecta el telefono por cable; aparecera "Permitir depuracion USB", marca "Permitir siempre" y acepta.
4. En la linea de comandos del ordenador (PowerShell o cmd en Windows) ejecuta <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb devices</code>; si la respuesta es algo como <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">List of devices attached / xxxxxxxx device</code> esta conectado.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>No ignores los drivers ni el cuadro de autorizacion

{class="mt-1"}
Si los usuarios de Windows ven <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb devices</code> muestra "unauthorized" o no lista el dispositivo, suele ser por falta de driver o por no haber pulsado "Permitir" en el telefono. Samsung/Xiaomi y otras marcas tienen sus "drivers USB" o "asistentes" para completarlos; en Mac y Linux no suele hacer falta. Si descartas el cuadro por error, vuelve a conectar el cable y volvera a aparecer.
:::

##### Comandos ADB habituales:

- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb install app.apk</code>: Instala un APK del ordenador en el telefono (<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-r</code> reinstala conservando datos;<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-s</code> instala en la tarjeta SD).
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb uninstall com.xxx.xxx</code>: Desinstala una app por nombre de paquete.
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb push ruta_del_ordenador /sdcard/ruta_destino</code>: Envia un archivo del ordenador al telefono.
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb pull /sdcard/archivo ruta_del_ordenador</code>: Trae un archivo del telefono al ordenador (mas rapido que enviartelo por WeChat y descargarlo).
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell</code>: Entra en la shell de Linux del telefono; puedes ejecutar directamente <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">ls</code>, <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pm</code>, <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">am</code> y otros comandos.
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb reboot bootloader</code>: Reinicia el telefono en modo Fastboot (entrada para flashear).
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb reboot recovery</code>: Reinicia en modo Recovery.
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm list packages</code>: Lista los nombres de paquete de todas las apps instaladas (imprescindible para encontrarlos). Anadiendo <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-s</code> solo apps del sistema; anadiendo <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-3</code> solo apps de terceros.
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm uninstall --user 0 nombre_paquete</code>: Desinstala una app preinstalada para el usuario actual sin Root; ver la practica mas abajo.

##### Practica: desinstalar apps preinstaladas sin Root:

Es una de las funciones mas utiles de ADB: con <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pm uninstall --user 0</code> puedes desinstalar apps preinstaladas para el "usuario actual" sin Root ni alterar la particion del sistema. La app "desaparece" del sistema pero sigue en la particion; al restaurar de fabrica vuelve.

1. Primero usa <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm list packages -s</code> para listar las apps del sistema y encontrar el nombre del paquete. Por ejemplo, el navegador de Xiaomi es <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.browser</code>, la tienda de Huawei es <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.vmall.client</code>.
2. No sabes que paquete es cada app? En el ordenador usa <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm list packages | findstr palabra_clave</code> para buscar, o instala una app de terceros como "Package Viewer" para ver el paquete de cada app en el telefono.
3. Ejecuta la desinstalacion:<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm uninstall --user 0 nombre_paquete</code>, por ejemplo <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm uninstall --user 0 com.android.browser</code>. Si devuelve <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">Success</code> ha tenido exito.
4. Como restaurar? Dos metodos: 1) restaurar de fabrica (mas completo pero engorroso); 2) reinstalar con<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell cmd package install-existing nombre_paquete</code>.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-skull-crossbones mr-2"></i>Nunca borres paquetes basicos del sistema

{class="mt-1"}
"pm uninstall --user 0" es un metodo seguro sin Root, pero borrar apps criticas del sistema (como <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.systemui</code> la barra de estado,<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.phone</code> el telefono,<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.settings</code> los ajustes) puede provocar cuelgues, pantalla negra o imposibilidad de encender. Antes de borrar, busca en Google "se puede borrar este paquete". Borra pocos cada vez y comprueba que todo va bien.
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Curiosidad: que significa --user 0

{class="mt-1"}
Desde Android 4.2 se soportan varios usuarios; cada uno tiene un ID (el propietario es 0 y los invitados empiezan en 10).<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">--user 0</code> significa "desinstalar solo para el propietario"; el APK sigue en la particion del sistema pero no se muestra. Por eso no necesita Root: no toca los archivos del sistema, solo cambia la configuracion del usuario. Se diferencia del Root en que este borra de verdad para todos los usuarios; ADB solo "oculta al usuario actual".
:::

#### 5. Permisos Root: el "superadministrador" de Android

El permiso Root equivale al superusuario de Linux (control total sobre / y lectura/escritura de cualquier archivo); es el nivel mas alto de Android. Se diferencia del Administrador de Windows, que por motivos de seguridad tiene muchas restricciones (el verdadero maximo es TrustedInstaller); ni siquiera el Administrador puede ejecutar directamente como root de Linux <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">sudo rm -rf /*</code>. Al obtener Root puedes modificar archivos del sistema, desinstalar apps preinstaladas y usar apps avanzadas que lo requieren.

##### Descripcion de función

- Termux:API
- Expone funciones de API de Android a programas de linea de comandos
- Termux:Boot
- Permite ejecutar scripts al iniciar el dispositivo

##### Termux:Float

- <strong>Móviles plegables</strong> Termux:Styling
- <strong>Habilita esquemas de color y personalizacion de fuentes para la terminal</strong> Termux:Tasker
- <strong>Integra scripts de Termux con la App de automatización Tasker</strong> Termux:Widget
- <strong>Permite ejecutar scripts desde widgets de la pantalla principal</strong> Nota importante
- <strong>Termux y sus plugins deben instalarse desde la misma fuente porque comparten el mismo sharedUserId. Mezclar fuentes (F-Droid y GitHub) causará errores de instalación.</strong> IV. Guia de instalación y configuración

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-skull-crossbones mr-2"></i>Pasos de instalación

{class="mt-1"}
Descargar App
:::

#### 6. SafetyNet y Play Integrity: por que las apps de banco no funcionan tras hacer Root

Muchos usuarios Root han vivido este momento: tras instalar modulos, abren la app del banco y ven "Su dispositivo no es seguro, no se puede usar"; Google Pay tampoco funciona y Netflix se niega a reproducir en HD. Detras estan los dos mecanismos de integridad de Google: el antiguo SafetyNet y el nuevo Play Integrity API.

##### Que son SafetyNet y Play Integrity:

- <strong>SafetyNet Attestation (antiguo, desde 2017)</strong>: API de comprobacion de integridad lanzado por Google; la app consulta al servidor "este dispositivo ha pasado el CTS y esta sin modificar". Devuelve Basic Attestation (basica) y Strong Attestation (fuerte, con clave de hardware). Google anunciara su desuso progresivo a partir de 2024.
- <strong>Play Integrity API (nuevo, desde 2022)</strong>: La alternativa de Google, mas estricta y completa. Ademas de la integridad del dispositivo, incluye la integridad de la app (si ha sido manipulada) y la de la cuenta o autorizacion (si Google confia en el usuario). Las apps nuevas deberian migrar a Play Integrity.
- <strong>Quienes lo usan</strong>: Apps de banca, finanzas y pagos (Google Pay, banca online, Alipay/WeChat Pay en ciertos casos), streaming (Netflix para proteger HD), algunos juegos anti-trampas (Tencent, NetEase) y apps empresariales (MDM de cumplimiento de dispositivos).

##### Tres niveles de Play Integrity:

- <strong>MEETS_DEVICE_INTEGRITY (integridad del dispositivo)</strong>: El dispositivo tiene Android oficial, Bootloader bloqueado, sin Root y supera el CTS. Permite usar apps de banco y pago.
- <strong>MEETS_BASIC_INTEGRITY (integridad basica)</strong>: El dispositivo es basicamente fiable, pero puede tener anomalias leves. Algunas apps bajan su nivel (Netflix puede reproducir pero limita la resolucion) y las mas estrictas rechazan el acceso.
- <strong>MEETS_STRONG_INTEGRITY (integridad fuerte)</strong>: El nivel mas alto; requiere respaldo de clave de hardware (como Titan M en Google Pixel); la mayoria de marcas no lo alcanza ni sin Root.
- <strong>Sin etiqueta (NO_INTEGRITY)</strong>: El dispositivo esta rooteado, BL desbloqueado, con ROM de terceros o detectado como emulador; casi todas las apps de banco y pago se niegan a funcionar.

##### Por que estas apps fallan tras el Root:

La app pide a Play Integrity la certificacion al servidor de Google, que revisa varios indicadores (Bootloader bloqueado, particion del sistema modificada, binario su, SELinux en modo permisivo...). Cualquier anomalia reduce el nivel o lo deja vacio; la app del banco ve "dispositivo no seguro" y rechaza el servicio.

##### Soluciones de ocultacion modernas: Magisk Hide / Shamiko / Zygisk:

Para poder usar apps bancarias sin perder las ventajas del Root, la comunidad ha desarrollado una serie de métodos para "ocultar el estado de Root". La idea central es hacer que el programa de detección vea un dispositivo "con apariencia normal" en lugar de un sistema modificado.

- <strong>Respaldo manual</strong>: El método de Root sin sistema más popular actualmente; no modifica la partición del sistema, sino que implementa el Root mediante montaje. La ventaja es menor probabilidad de fallo en actualizaciones OTA y una desinstalación más limpia, siendo la base de todos los métodos de ocultación posteriores. Sin embargo, usar Magisk sigue requiriendo desbloquear el bootloader.
- <strong>Magisk Hide (descontinuado)</strong>: Un módulo de ocultación integrado en Magisk que podía ocultar el Root a apps específicas. Sin embargo, fue eliminado oficialmente en 2021 debido a que Google mejoró continuamente sus métodos de detección, creando un "juego del gato y el ratón".
- <strong>Zygisk</strong>: Un nuevo mecanismo introducido en Magisk 24.0+, similar a Riru, que carga los módulos inyectándose en el proceso Zygote, siendo más discreto que la modificación directa del sistema. Activar Zygisk es un requisito previo para usar los métodos modernos de ocultación.
- <strong>Shamiko</strong>: El módulo de ocultación más popular actualmente, que funciona junto con Zygisk para ocultar el Root, ocultar el propio Magisk y falsificar el estado del bootloader a apps específicas (modo "lista blanca inversa"). Shamiko se distribuye a través del repositorio LSPosed o GitHub.
- <strong>Play Integrity Fix(osm0sis)</strong>: Un módulo de Magisk diseñado específicamente contra la detección de Google Play Integrity, que modifica la huella digital del dispositivo para que Google crea que tu dispositivo es un modelo oficial sin Root.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>El juego del gato y el ratón nunca terminará

{class="mt-1"}
Google actualiza periódicamente las reglas de detección y los desarrolladores de apps también mejoran la verificación de Play Integrity. Los métodos de ocultación que funcionan hoy pueden ser detectados mañana. Si dependes completamente de apps bancarias o de pago (como transferencias diarias, pagos con código QR), la opción más segura sigue siendo: no hacer Root, no desbloquear el bootloader. Los métodos de ocultación son más adecuados para una configuración de "teléfono principal sin Root + teléfono de respaldo con Root".
:::

#### VII. Recomendaciones para usuarios comunes

- <strong>Inicializar sistema</strong>: Puedes activarlos para probar aceleración de animaciones, análisis de renderizado GPU, etc., pero no cambies otras opciones que no entiendas.
- <strong>Desbloqueo OEM y bloqueo del bootloader</strong>: Si no planeas flashear ROMs ni hacer Root, mantén ambos interruptores en su estado predeterminado (apagado) por seguridad.
- <strong>ADB</strong>: Herramientas potentes sin Root que incluso los usuarios comunes pueden usar, como usar <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pm uninstall --user 0</code> para desinstalar apps preinstaladas. Pero asegúrate de verificar si el nombre del paquete se puede eliminar antes de borrarlo.
- <strong>Gracias por leer hasta el final este "curso de móviles"! Durante la escritura consultamos amplios manuales oficiales de fabricantes, guías de usuario y artículos de divulgacion técnica publicos para garantizar la exactitud de la información.</strong>: No se recomienda hacer Root para usuarios comunes; los riesgos superan a los beneficios. Si necesitas ciertas funciones, primero investiga si hay alternativas que no requieran Root (como desinstalar apps preinstaladas con ADB o usar Shizuku para reemplazar algunas funciones de Root).

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>pkg update &amp;&amp; pkg upgrade

{class="list-decimal pl-6 mt-1 space-y-1"}
1. para actualizar la lista de paquetes.
2. Optimizacion básica
3. Cambiar repositorio espejo
4. :usa el comando
5. termux-change-repo
:::
