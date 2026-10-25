---
id: di-shi-ba-zhang
num: 18
part: jin-jie-pian
nav: Capítulo 18: Copias de seguridad y migración de datos
toc: default
kind: chapter
---

### Capítulo 18: Respaldo y migración de datos

{class="chapter-intro mb-4"}
Una vecina dejó caer su móvil en una piscina; al sacarlo ya no encendía. Lo que más le dolía no era el móvil en sí, sino las fotos de tres años sin copia de seguridad —todo el registro del crecimiento de su hijo desde que nació hasta que aprendió a caminar. Al escucharla me sentí muy mal, porque esto era totalmente evitable. En este capítulo aseguraremos nuestros datos seriamente.

#### I. Entiende primero: que cosas de tu móvil se pierden para siempre

Los datos tienen diferentes "estados de supervivencia"; debes distinguirlos:

- <strong>Almacenados localmente en el móvil, se pierden definitivamente:</strong>:Fotos y videos (sin sincronización en la nube), notas, SMS, registro de llamadas, archivos descargados.
- <strong>Almacenados en servidores de Apps, al cambiar de móvil e iniciar sesion reaparecen:</strong>:Lista de contactos de WeChat, pedidos de Taobao, registros transacciónales de Apps bancarias. Estos datos estan almacenados en los servidores de las empresas correspondientes, no en tu móvil.
- <strong>En zona gris, requieren operaciones especiales:</strong>: historial de chat de WeChat (aunque el servidor de WeChat lo guarda, tú mismo no puedes descargarlo desde el servidor), credenciales de dispositivo vinculadas a banca móvil, claves de autenticación en dos pasos (tipo Google Authenticator).

Por tanto, debes proteger con prioridad la primera y tercera categorías.

#### II. Copia de seguridad completa: todo de una vez

La copia de seguridad completa es como hacer una "foto" completa del móvil —ajustes del sistema, disposición del escritorío, datos de Apps, fotos, contactos: todo empaquetado.

##### Opcion 1: Copia local en ordenador (la más fiable, recomendada si tienes PC)

- <strong>iPhone</strong>:Conecta el móvil al ordenador con cable, abre iTunes (Windows antiguo) o Finder (Mac), en la página del dispositivo elige "Hacer copia ahora". Asegúrate de marcar "Cifrar copia de seguridad", sino las contraseñas y datos de salud no se incluirán.
- <strong>Android</strong>: cada marca tiene su propio software para PC: Asistente de móvil Huawei, Asistente Xiaomi, Samsung Smart Switch. Conecta al ordenador y sigue las instrucciones.
- La ventaja de la copia en PC es que no pagas espacio en la nube y la restauración es mucho más rápida que desde la nube. La desventaja: debes recordar conectar el cable periódicamente — la mayoría no lo hace.

##### Opcion 2: Copia en la nube (la más comoda, recomendada para todos)

- <strong>iPhone</strong>:Ajustes &gt; Tu nombre &gt; iCloud &gt; Copia de seguridad en iCloud &gt; Activar. El móvil hace copias automáticas cuando está cargando, conectado a Wi-Fi y bloqueado. Los 5GB gratis probablemente no alcancen; recomiendo pagar 6 yuanes por 50GB.
- <strong>Android</strong>: cada marca tiene su función de copia en la nube. Huawei: busca "Copia de seguridad" en ajustes. Xiaomi: "Xiaomi Cloud". OPPO/vivo similar. Además hay la copia de Google (Ajustes &gt; Sistema &gt; Copia de seguridad); actívala también.
- La mayor ventaja del respaldo en la nube es que es "sin preocupaciones", se hace automáticamente. El mayor inconveniente: la restauración tarda mucho en descargar y el espacio gratuito suele no alcanzar.

#### III. Estrategia de copia por categorías: guarda lo importante por separado

La copia completa es el fondo de seguridad, pero algunas cosas son demasiado importantes para merecer una copia aparte:

##### Fotos y videos (los activos digitales más preciosos)

- <strong>Esquema de doble seguro</strong>:Activa la sincronización automática de Fotos de iCloud/Google Photos, y cada pocos meses copia manualmente las fotos al ordenador o un disco duro externo. Así tienes una copia en la nube y otra local; una respalda a la otra.
- <strong>Opcion sin coste:</strong>:Google Fotos ofrece 15 GB gratis; puedes configurar "calidad comprimida" para ahorrar espacio. O cada mes copia todas las fotos al PC via cable de datos.

##### Contactos (fácil de ignorar pero extremadamente importante)

- Los contactos de iPhone se sincronizan con iCloud por defecto; no necesitas copia extra. Para mayor seguridad, ve a iCloud.com y exporta un archivo vCard al ordenador.
- Los contactos de Android suelen sincronizarse con Google o la nube de la marca. Ve a Ajustes de la App de contactos y exporta un archivo .vcf: esa es una copia completa.

##### Historial de chat de WeChat (trato especial, lo más importante)

Esto merece mención aparte, porque en la copia completa el historial de WeChat suele estar incompleto, y las herramientas de transferencia de dispositivos no lo pueden mover.

- <strong>Método 1: Migrar a nuevo móvil</strong>.WeChat &gt; Yo &gt; Ajustes &gt; General &gt; Migración y copia del historial de chat &gt; Migrar &gt; Migrar a móvil/tablet. Ambos móviles en la misma Wi-Fi, escanea el código QR para transferir. Nota: no cierres WeChat en el viejo móvil hasta terminar.
- <strong>Método 2: Copiar al ordenador</strong>.Instala WeChat para PC, menú inferior izquierdo &gt; Migración y copia &gt; Copia y restauración &gt; Copiar historial de chat al ordenador. Luego puedes restaurarlo en el nuevo móvil.
- <strong>Metodo 3: Copia de seguridad en la nube</strong>. WeChat también permite copiar a iCloud o a la nube del móvil, pero ojo: esta copia solo se puede restaurar en el móvil actual, no en otro dispositivo. Para cambiar de móvil, usa los dos primeros métodos.

#### IV. Guia de cambio de móvil: del viejo al nuevo

Cambiar a un nuevo móvil es alegre, pero si no mueves los datos se vuelve una pesadilla. Tres situaciones diferentes:

##### Actualizacion misma marca (lo más simple)

- <strong>iPhone -&gt; Nuevo iPhone</strong>:Al encender el nuevo móvil, pon el viejo al lado; aparecerá "Inicio rápido". Escanea el código del nuevo con el viejo. Todos los datos, ajustes y disposición de Apps se transferirán intactos, incluidas las contraseñas de Wi-Fi. Tarda unos 20-30 minutos.
- <strong>Android misma marca</strong>:Usa la herramienta de transferencia de la marca. Huawei: "Clonación de móvil", Xiaomi: "Cambio Xiaomi", OPPO: "Mudanza de móvil", vivo: "Interconexión". Pasos similares: instala la misma App en ambos, escanea el código, selecciona qué transferir y envía.

##### Cambio de marca cruzado (Android a Android, diferente marca)

Usa herramientas de terceros o la App de transferencia de la antigua marca (la mayoría también soportan transferencia a otros Android). Lo que se puede mover: contactos, fotos, SMS, registro de llamadas, algunas Apps. Lo que NO se mueve: sesiones iniciadas en Apps (debes volver a iniciar sesion), historial de WeChat (usa la función propia de migración de WeChat).

##### Cambio de plataforma cruzado (Android a iPhone o viceversa)

- <strong>Android → iPhone</strong>:Apple tiene la App "Mover a iOS"; descárgala en Android y al activar el nuevo iPhone elige "Transferir desde dispositivo Android". Transfiere contactos, fotos, SMS básicos, pero no datos de Apps. El historial de WeChat necesita su propia función de migración.
- <strong>iPhone -&gt; Android</strong>:Las marcas Android tienen herramientas de migración correspondientes, pero sinceramente, la experiencia de migración cruzada no es tan buena como la misma plataforma. Haz primero lo más importante por separado: exportar contactos, copiar fotos, migrar historial de WeChat. Lo demás poco a poco.

#### V. Regla de oro del respaldo: principio 3-2-1

Este es un clásico en seguridad de datos, fácil de recordar:

- <strong>3</strong>:Datos importantes: mantén al menos 3 copias (1 original + 2 copias de seguridad).
- <strong>2</strong>:Usa dos medios de almacenamiento diferentes (ej: uno en la nube, uno en disco duro externo).
- <strong>1</strong>:Al menos una copia en ubicación física diferente (contra incendio, robo, etc.).

Para la mayoría, tener "una copia en la nube + una en el ordenador" ya es excelente. No te compliques demasiado; lo importante es que realmente lo hagas.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Atencion especial al historial de WeChat

{class="mt-1"}
¡El historial de chat de WeChat NO puede migrarse con ningúna herramienta de transferencia de móviles! No está cubierto por la copia completa. Debes usar la función propia "Migración de historial de chat" de WeChat o copiar a WeChat para PC. Mucha gente lo descubre después de cambiar de móvil cuando ya es tarde —el viejo móvil ya puede haber sido restablecido de fábrica.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Practica: haz una copia de seguridad completa

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Verifica que la Copia de seguridad en iCloud o de marca esté activa; cuándo fue la última copia.
2. Copia manual de fotos: conecta por cable al PC, copia las carpetas DCIM y Pictures.
3. Copia de contactos: los usuarios de iPhone van a iCloud.com para exportar la vCard; los de Android la exportan como archivo .vcf desde los ajustes de la App de contactos.
4. Copia de historial de WeChat: WeChat &gt; Yo &gt; Ajustes &gt; General &gt; Migración y copia &gt; Copiar al ordenador.
5. Copia la carpeta de fotos y el archivo de contactos .vcf exportados a un disco duro externo o memoria USB: cumples así la «copia fuera de casa» del 3-2-1.
:::
