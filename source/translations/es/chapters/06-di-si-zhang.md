---
id: di-si-zhang
num: 04
part: ji-chu-pian
nav: Capítulo 4: Instalar y gestionar apps
toc: default
kind: chapter
---

### Capítulo 4: Instalar y gestionar App — las "habilidades" del teléfono

{class="chapter-intro mb-4"}
Las App hacen que el teléfono pueda hacer de todo, pero también hay que gestionarlas. Igual que asignarías un puesto y permisos a un nuevo empleado, instalar App requiere un procedimiento normalizado.

#### I. Tiendas oficiales: el "supermercado de aplicaciones" más seguro

- <strong>Android</strong>: Google Play (en el extranjero) o la tienda integrada de cada marca (como Huawei AppGallery, Xiaomi App Store).
- <strong>iOS</strong>: solo App Store.
- <strong>HarmonyOS</strong>: Huawei AppGallery.

Importancia central de la seguridad: pasa por una revisión, las actualizaciones están garantizadas y el pago es seguro. Guía de acción:<strong>¡descarga preferentemente solo desde tiendas oficiales!</strong>

#### II. Modo puro/protección: activa el "antivirus" del teléfono

Las principales marcas nacionales (Huawei, Xiaomi, OPPO, vivo, Honor) integran un <strong>modo puro</strong> o <strong>modo de protección</strong>, un interruptor de seguridad a nivel de sistema.<strong>Se recomienda encarecidamente a todos los usuarios activarlo</strong>.

##### 1. ¿Qué es exactamente?

La función <strong>central del modo puro (también llamado "modo de protección") es bloquear la instalación de App de terceros</strong>: cuando está activo, el sistema <strong>solo permite instalar App desde la tienda oficial</strong>; los paquetes de instalación descargados desde el navegador, códigos QR, software de chat, etc., se interceptan directamente, eliminando el malware desde la raíz.

##### 2. Usuaríos a los que aplica

- <strong>Usuaríos mayores</strong>: que no distinguen entre publicidad "oficial" y "falsa"; el modo puro es la protección más fiable.
- <strong>Usuaríos poco sensibles a los permisos de las aplicaciones</strong>: que no necesitan instalar App minoritarias, versiones beta ni juegos de servidores extranjeros.
- <strong>Cualquier usuario que quiera mejorar la seguridad del dispositivo</strong>: incluso para entusiastas, tenerlo activado es mejor que no hacerlo; si hay una necesidad puntual, se desactiva temporalmente.

##### 3. Ruta de activación (ejemplo con Huawei/Xiaomi)

- <strong>Huawei/HarmonyOS</strong>: [Configuración] &gt; [Sistema y actualizaciones] &gt; <strong>[Modo puro]</strong>, elige "Activar".
- <strong>Xiaomi</strong>: [Configuración] &gt; [Protección de privacidad] &gt; <strong>[Proteger privacidad]</strong> o [Configuración] &gt; [Ajustes de aplicación] &gt; [Instalación de aplicaciones], desactiva "Instalar aplicaciones de origen desconocido".
- <strong>: puedes configurar Nginx o Apache para montar servidores web estáticos.</strong>: [Configuración] &gt; [Seguridad] &gt; <strong>[Instalar aplicaciones de fuentes externas]</strong>, desactiva la autorización una por una.

{class="font-semibold mt-4 mb-1"}
##### 4. Mecanismo de seguridad de la tienda de aplicaciones

La tienda de aplicaciones no es un "adorno"; detrás hay una cadena de seguridad completa:

- <strong>Análisis de virus</strong>: antes de publicarse, cada App pasa por un escaneo conjunto de varios motores antivirus que identifica firmas conocidas de troyanos y virus.
- <strong>Revisión de permisos</strong>: la tienda revisa si los permisos que solicita la App son "razonables": ¿una App de linterna pide acceso a los contactos? Se rechaza o se retira.
- <strong>Certificación de desarrollador</strong>: para publicar hace falta certificación empresarial, de identidad personal o de tarjeta de crédito. Si surge un problema, se puede localizar a alguien; no es una "App negra".
- <strong>Supervisión continua</strong>: las App ya publicadas también se reescanean de forma continua; los comportamientos maliciosos detectados se retiran forzosamente.

#### III. Fuentes de terceros y "parásitos electrónicos": ¡alto riesgo!

Descargar App desde páginas web o enlaces desconocidos puede traer virus, robar privacidad y clonar pagos. Aquí introducimos un concepto nuevo: el <strong>"parásito electrónico"</strong>.

::: div .danger-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-bug mr-2"></i>¿Qué es un "parásito electrónico"?

{class="mt-1"}
Se refiere a <strong>software "pirateado" con troyanos incrustados</strong>: crees que "te has ahorrado dinero", pero en realidad "te has infectado". Formás habituales:

{class="list-disc pl-6 mt-2 space-y-1 text-sm"}
- Versiones "pirateadas", "gratuitas", "sin anuncios" de software de pago;
- Herramientas grisáceas como "generadores de likes", "cazadores de sobres rojos", "cheats de juegos";
- App supuestamente "versiones internas" recomendadas por "publicidad pequeña" en grupos de chat.

{class="mt-2"}
Estos programas funcionan en apariencia, pero en segúndo plano pueden <strong>robar contactos, leer SMS, espiar el micrófono o minar criptomonedas</strong>. El modo puro es la <strong>primera línea de defensa</strong> contra ellos: directamente impide su instalación.
:::

##### Recomendaciones para la segúnda línea de defensa:

- <strong>Análisis completo de virus periódico</strong>: usa el centro de seguridad integrado en el teléfono (como Huawei Phone Manager, Xiaomi Security Center) para escanear una vez al mes.
- <strong>Concede permisos sensibles con precaución</strong>: contactos, SMS, ubicación, cámara, micrófono — estos cinco "permisos de alto riesgo" deben revisarse estrictamente.
- <strong>Vigila anomalías en consumo y datos</strong>: si el teléfono se calienta de repente, la batería cae rápido o los datos se consumen de madrugada, lo más probable es que haya un "parásito" oculto en segúndo plano.

Si no hay más remedio que instalar una App de terceros:

1. Asegúrate de que la fuente sea absolutamente fiable.
2. Revisa atentamente los permisos solicitados antes de instalar.
3. Después, escanea con una App de seguridad.

Consejo definitivo: en los ajustes del sistema, desactiva el permiso "Instalar aplicaciones de origen desconocido".

#### IV. Instalar, actualizar, desinstalar

- <strong>Instalar</strong>: en la tienda, pulsa "Obtener" o "Instalar"; al abrir por primera vez tras la instalación, te pedirá permisos.
- <strong>Actualizar</strong>:<strong>¡hay que hacerlo!</strong> Principalmente repara vulnerabilidades de seguridad. Se recomienda activar la actualización automática.
- <strong>Desinstalar</strong>: mantén pulsado el icono y arrástralo a la zona de desinstalación. Para borrar de forma más completa, ve a [Configuración] &gt; [Gestión de aplicaciones], búscala y desinstálala.

#### V. Gestión de permisos: tú eres el "jefe" de la App

Que una App pida permisos (como contactos o ubicación) a veces es razonable (un mapa necesita la ubicación) y a veces no (una linterna pide contactos).

```html
<ul class="list-disc pl-6 mb-3 space-y-1">
                        <li><strong>Opciones de permisos</strong>: "Permitir siempre", "Permitir solo durante el uso", "Denegar", "Preguntar siempre".</li>
                        <li><strong>Principios de gestión</strong>:
                            <ol class="list-alpha pl-6 mt-1 space-y-1">
                                <li>Minimización: no conceder lo que no sea necesario.</li>
                                <li>Auditoría posterior: revisa periódicamente en los ajustes de permisos quién se "pasa de la raya".</li>
                                <li>Contextual: con una App de transporte, por ejemplo, concede la ubicación solo cuando la uses.</li>
                            </ol>
                        </li>
                    </ul>
```

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-shield-alt mr-2"></i>Permisos a vigilar especialmente

{class="list-disc pl-6 mt-1 space-y-1"}
- Contactos/SMS: pueden usarse para enviar SMS basura.
- Ubicación en tiempo real: puede rastrear tus movimientos.
- Cámara/micrófono: pueden usarse para espiar o grabar a escondidas.
- Acceso a archivos: puede leer tus archivos privados.
:::

{id="di-si-zhang-apk"}
#### VI. Componentes del paquete de instalación

¿Te has preguntado qué hay dentro del paquete de instalación que descargas de la tienda de aplicaciones? Conocer la estructura del paquete te ayuda a entender cómo funcionan las App y a saber por dónde empezar cuando surge un problema.

##### 1. Estructura del archivo APK de Android

Un APK (Android Package Kit) es esencialmente un archivo ZIP comprimido; al descomprimirlo se ven los siguientes directoríos y archivos clave:

- <strong>AndroidManifest.xml</strong>: el "DNI" y el "manual" de la aplicación. Registra el nombre del paquete, el número de versión, los permisos necesarios, las versiones de sistema compatibles, la Activity de entrada y otra información clave. El sistema lee primero este archivo al instalar la aplicación.
- <strong>classes.dex</strong>: el código central de la aplicación. El código fuente en Java/Kotlin se compila a bytecode Dalvik y se guarda en este archivo. Una aplicación puede tener varios archivos dex (como classes2.dex, classes3.dex).
- <strong>resources.arsc</strong>: tabla de índices de recursos compilados. Registra los ID de todos los recursos y sus correspondencias.
- <strong>directorío res/</strong>: carpeta de recursos. Contiene imágenes, archivos de diseño, cadenas, definiciones de color, etc. Las imágenes de distintas resoluciiones se colocan en carpetas drawable distintas (como drawable-hdpi, drawable-xhdpi).
- <strong>directorío assets/</strong>: carpeta de recursos sin procesar. Almacena recursos que no se compilan, como archivos web, fuentes, audio, etc. La App puede leerlos en tiempo de ejecución a través de AssetManager.
- <strong>directorío lib/</strong>: carpeta de bibliotecas nativas. Almacena archivos .so compilados (productos de la compilación de código C/C++), clasificados por arquitectura de CPU (como arm64-v8a, armeabi-v7a). Los juegos y las App que necesitan cálculos de alto rendimiento suelen tener este directorío.
- <strong>directorío META-INF/</strong>: carpeta de información de firma. Contiene tres archivos (MANIFEST.MF, CERT.SF, CERT.RSA) para verificar la integridad y la firma del APK.

##### 2. Estructura del archivo IPA de iOS

Un IPA (iOS App Store Package) también es un paquete comprimido, con una estructura ligeramente distinta:

- <strong>directorío Payload/</strong>: donde está el contenido central. Dentro hay una carpeta .app que contiene todo el contenido de la aplicación.
- <strong>Info.plist</strong>: archivo de configuración de la aplicación, similar al AndroidManifest.xml de Android. Registra el ID de la aplicación, la versión, los permisos necesarios, los dispositivos compatibles, etc.
- <strong>Archivo ejecutable</strong>: programa principal con el mismo nombre que la carpeta .app; es un archivo binario en formato Mach-O compilado.
- <strong>directorío Frameworks/</strong>: bibliotecas dinámicas y marcos de los que depende la aplicación.
- <strong>Archivos de recursos</strong>: imágenes, audio, video y otros recursos, normalmente guardados dentro de la carpeta .app.
- <strong>directorío _CodeSignature/</strong>: información de firma del código, para verificar la integridad y el origen de la aplicación.

##### 3. Mecanismo de verificación de firmas

¿Por qué las App descargadas de la tienda oficial son más seguras? La verificación de firmas es la clave.

```html
<ul class="list-disc pl-6 mb-3 space-y-1">
                        <li><strong>Firma de Android</strong>: el desarrollador firma el APK con su clave privada y el sistema la verifica con la clave pública al instalar. Si el APK ha sido manipulado (por ejemplo, con un virus inyectado), la firma deja de ser válida y el sistema rechaza la instalación. Google Play además exige App Signing, con Google custodíando las claves de firma, para proteger aún más la seguridad de la aplicación.</li>
                        <li><strong>Firma de iOS</strong>: la revisión de Apple es más estricta. Cada IPA debe estar firmado con un certificado emitido por Apple, de lo contrario no se puede instalar. Por eso en iOS solo se pueden instalar App desde la App Store o con un certificado empresarial. Las App firmadas con certificado empresarial tienen una validez limitada y Apple puede revocarlas en cualquier momento.</li>
                        <li><strong>Función de la firma</strong>:
                            <ol class="list-alpha pl-6 mt-1 space-y-1">
                                <li>Verificar el origen: confirmar que la aplicación proviene efectivamente del desarrollador que dice ser.</li>
                                <li>Verificar la integridad: asegurar que la aplicación no ha sido manipulada durante la transmisión.</li>
                                <li>Evitar suplantaciones: una aplicación maliciosa no puede hacerse pasar por otra.</li>
                            </ol>
                        </li>
                    </ul>
```

##### 4. Tamaño del paquete de instalación y optimización

Puede que notes que el tamaño de la App mostrado en la tienda no coincide con el espacio que ocupa tras la instalación. Esto se debe a:

- <strong>Tamaño de descarga</strong>: el tamaño del APK/IPA comprimido.
- <strong>Tamaño de instalación</strong>: el tamaño tras la descompresión, normalmente mucho mayor que el de descarga.
- <strong>Ocupación en tiempo de ejecución</strong>: al ejecutarse, la App también genera caché y archivos de datos que ocupan más espacio.

Medios de optimización de las App modernas:

- <strong>App Bundle (Android)</strong>: tecnología de distribución dinámica de Google Play. Al descargar, el usuario solo obtiene los recursos adecuados para su dispositivo (por ejemplo, solo las imágenes de la resolución de su pantalla), lo que reduce enormemente el tamaño de descarga.
- <strong>App Thinning (iOS)</strong>: tecnología similar; Apple recorta automáticamente los recursos innecesarios según el dispositivo.
- <strong>Descarga bajo demanda</strong>: las aplicaciones grandes, como los juegos, pueden descargar primero un paquete central y los paquetes de recursos más adelante.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Sabías que: ¿por qué algúnos paquetes de instalación son especialmente grandes?

{class="mt-1"}
Las App de juegos suelen ser las más grandes, porque contienen muchas texturas en alta definición, modelos 3D y archivos de audio. Las App sociales también son bastante grandes, por la cantidad de módulos funcionales que deben admitir. Las App de herramientas suelen ser las más pequeñas. Si descubres que una App de herramientas es especialmente grande, sospecha si incluye funciones innecesarias.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Práctica: audita los permisos de 3 App

{class="mt-1"}
Elige 3 App de uso habitual (por ejemplo, social, compras, herramientas), entra en la página de gestión de permisos de [Configuración], revísalas una por una y desactiva los permisos sensibles innecesarios o cámbialos a "Permitir solo durante el uso".
:::
