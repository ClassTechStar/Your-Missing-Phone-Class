---
id: di-yi-zhang-harmony
part: ji-chu-pian
nav:  Anexo del Capítulo 1: Tema especial del sistema operativo HarmonyOS
toc: default
kind: supplement
---

### Anexo del Capítulo 1: Tema especial del sistema operativo HarmonyOS

{class="chapter-intro mb-4"}
HarmonyOS es el sistema operativo auto-desarrollado por Huawei, desde su lanzamiento en 2019 ha pasado por varias versiones mayores. No es solo "otro sustituto de Android", es una nueva especie con una filosofía de diseño única. Conozcamos a fondo este sistema operativo en ascenso.

#### 1. ¿Qué es HarmonyOS? ¿Por qué es diferente?

La filosofía central de HarmonyOS es "interconexión de todas las cosas". A diferencia de los sistemas operativos tradicionales que sirven principalmente a un único dispositivo, HarmonyOS desde su diseño consideró la colaboración multi-dispositivo.

<strong>La arquitectura distribuida</strong> es el alma de HarmonyOS. En pocas palabras, puede virtualizar múltiples dispositivos en un "supertérmino". Tu móvil, tablet, computadora, reloj, TV, ya no son individuos aislados, sino "órganos" de un todo, pueden invocar capacidades entre sí.

Un ejemplo: estás viendo un video en el móvil y quieres verlo en pantalla grande, la forma tradicional es proyectar la pantalla; en HarmonyOS, puedes "transferir" el video a la TV para seguir viéndolo, el móvil se convierte en control remoto. No es una simple proyección, es la propia aplicación ejecutándose entre dispositivos.

#### 2. HarmonyOS 4.3: versión madura basada en AOSP

HarmonyOS 4.3 es la versión ampliamente desplegada actualmente en móviles Huawei. Cabe señalar que HarmonyOS 4.3 es compatible con el marco de código del proyecto de código abierto Android (AOSP), por lo que puede ser totalmente compatible con aplicaciones Android—la mayoría de las Apps que descargas de la AppGallery de Huawei son esencialmente aplicaciones Android, ejecutadas a través de la capa de compatibilidad de HarmonyOS. Pero HarmonyOS 4.3 no es simplemente un Android recubierto, sobre AOSP añade muchas capacidades distribuidas auto-desarrolladas por Huawei, el motor Ark, etc.

##### Características principales:

- <strong>Compatibilidad con aplicaciones Android</strong>: al desarrollarse sobre AOSP, HarmonyOS 4.3 puede ejecutar casi todas las aplicaciones Android, el usuario casi no nota diferencia.
- <strong>Motor Ark</strong>: compilador y runtime auto-desarrollado por Huawei, hace que las aplicaciones se ejecuten más fluidas y eficientes. Comparado con versiones tempranas, la fluidez mejora notablemente.
- <strong>Supertérmino</strong>: en el centro de control, puedes ver intuitivamente otros dispositivos HarmonyOS alrededor, con arrastrar se conectan. El móvil invoca el teclado/ratón del ordenador, la tablet invoca la cámara del móvil, muy práctico.
- <strong>Tarjetas de servicio</strong>: similares a los widgets de iOS, pero más flexibles. Puedes deslizar hacía arriba el icono de una App para expandir la tarjeta y mostrar información clave, sin abrir la App.
- <strong>modo puro</strong>: solo permite instalar aplicaciones desde la AppGallery oficial, reduce el riesgo de malware.
- <strong>Centro de privacidad</strong>: gestión centralizada de permisos de aplicaciones, consulta del registro de comportamiento de aplicaciones.

##### Características de la interfaz de usuario:

- <strong>Bloqueo de pantalla magazine</strong>: la pantalla de bloqueo muestra imágenes y artículos bonitos, desliza para entrar al escritorío.
- <strong>Tarjetas universales</strong>: los iconos del escritorío pueden expandirse en tarjetas, mostrando más información.
- <strong>Supertérmino de transferencia</strong>: un área de almacenamiento temporal, puedes guardar texto, imágenes, archivos y luego arrastrarlos a cualquier App. Compartir entre aplicaciones se vuelve súper fluido.
- <strong>Búsqueda inteligente</strong>: búsqueda global, puede buscar aplicaciones, archivos, ajustes, páginas web.

#### 3. HarmonyOS NEXT (HarmonyOS 6): el verdadero punto de partida del sistema operativo autónomo de Huawei

HarmonyOS NEXT (HarmonyOS NEXT 5.0) tiene una diferencia fundamental con HarmonyOS 4.3—adopta el microkernel HarmonyOS auto-desarrollado por Huawei, ya no depende del kernel Linux ni del código AOSP, y <strong>ya no soporta directamente aplicaciones Android</strong>. Este es el paso clave de HarmonyOS de "forma tránsitoria compatible con Android" a "sistema operativo completamente independiente".

##### Cambios importantes:

- <strong>Kernel completamente autónomo</strong>: HarmonyOS NEXT usa el kernel auto-desarrollado por Huawei, ya no contiene código AOSP. Sistema más ligero, más seguro, más eficiente.
- <strong>Ya no soporta aplicaciones Android</strong>: este es el mayor cambio. HarmonyOS NEXT solo puede ejecutar aplicaciones nativas de HarmonyOS, no puede instalar ni ejecutar archivos APK. Antes de actualizar, confirma que tus Apps habituales ya tienen versión nativa de HarmonyOS.
- <strong>Ecosistema de aplicaciones nativas</strong>: Huawei está impulsando a los desarrolladores a migrar aplicaciones a la plataforma nativa de HarmonyOS. Actualmente las Apps principales como WeChat, Alipay, Taobao ya tienen versión nativa de HarmonyOS, pero algunas aplicaciones de nicho pueden no estar adaptadas.
- <strong>Arquitectura de seguridad XingDun</strong>: nuevo sistema de seguridad, protección de cadena completa de hardware a software. Soporta control de permisos más fino, como "ubicación borrosa"—la aplicación solo puede saber aproximadamente dónde estás, no la posición precisa.
- <strong>Integración profunda de IA</strong>: capacidad de IA a nivel de sistema, no solo una App con IA. Por ejemplo, los subtítulos con IA pueden traducir video en tiempo real, el recorte con IA puede identificar inteligentemente el sujeto.
- <strong>Transferencia sin fisuras entre dispositivos</strong>: capacidad distribuida aún mayor. El estado de la aplicación puede cambiar sin fisuras entre dispositivos, el documento que editas en el móvil se abre automáticamente en el ordenador al acercarte.
- <strong>Meta-servicios</strong>: servicios ligeros usables sin instalar. Por ejemplo, escanear un código QR abre directamente una función, sin descargar primero una App.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Lectura obligatoria antes de actualizar a HarmonyOS NEXT

{class="mt-1"}
Tras actualizar a HarmonyOS NEXT, tu móvil no podrá ejecutar aplicaciones Android. Asegúrate antes de actualizar de: ① que tus Apps habituales ya tienen versión nativa de HarmonyOS; ② que tu trabajo o vida no depende de escenarios con aplicaciones Android. No se puede revertir a HarmonyOS 4.3 después de actualizar.
:::

##### Cambios en la lógica de operación:

- <strong>Navegación por gestos</strong>: deslizar desde el borde izquierdo/derecho para volver, deslizar hacía arriba desde abajo para ir al escritorío, deslizar hacía arriba y pausar para multitarea.
- <strong>Multiventana inteligente</strong>: soporta pantalla dividida, ventana flotante, vista paralela y otras formas de multitarea.
- <strong>Llamada Celia</strong>: servicio de videollamada de Huawei, soporta compartir pantalla, embellecimiento, desenfoque de fondo.

#### 4. Ecosistema HarmonyOS: dispositivos y aplicaciones

HarmonyOS no es solo un sistema de móvil, es un ecosistema que cubre múltiples dispositivos.

##### Tipos de dispositivos soportados:

- <strong>Móvil y tablet</strong>: dispositivos centrales, funciones más completas.
- <strong>Relojes inteligentes y pulseras</strong>: funcionamiento independiente o en colaboración con el móvil.
- <strong>Pantalla inteligente (TV)</strong>: centro de entretenimiento del hogar.
- <strong>Altavoz inteligente</strong>: entrada de interacción por voz.
- <strong>Automóvil</strong>: cabina HarmonyOS, experiencia de cabina inteligente.
- <strong>Hogar inteligente</strong>: frigorífico, aire acondiciónado, lavadora, etc.

##### Estado del ecosistema de aplicaciones:

La tienda de aplicaciones de HarmonyOS ya cuenta con millones de apps; las apps principales están prácticamente todas disponibles. Huawei también está impulsando activamente a los desarrolladores a crear aplicaciones nativas de HarmonyOS. A mediados de 2026, WeChat, Alipay, Taobao, Douyin, Meituan y JD.com ya han lanzado versiones nativas de HarmonyOS, y el uso diario es básicamente sin obstáculos. Algunas aplicaciones de nicho y sectoriales pueden seguir en proceso de adaptación; antes de actualizar, se recomienda confirmar si tus apps habituales ya están soportadas.

#### 5. Trucos prácticos de HarmonyOS

- <strong>Supertérmino</strong>: desliza hacía abajo desde la esquina superior derecha para abrir el centro de control, toca "Supertérmino", puedes ver otros dispositivos alrededor, arrastra para conectar.
- <strong>Supertérmino de transferencia</strong>: mantén pulsado texto/imagen/archivo, selecciona "Copiar al terminal de transferencia", luego en otras Apps mantén pulsado para pegar, o arrastra.
- <strong>Tarjetas de servicio</strong>: desliza hacía arriba el icono de la App para expandir la tarjeta, mantén pulsada la tarjeta para ajustar el tamaño o añadirla al escritorío.
- <strong>Multiventana inteligente</strong>: desliza desde el borde izquierdo/derecho hacía dentro y pausa, abre la barra lateral, toca la aplicación para abrirla como ventana flotante.
- <strong>Protección de privacidad</strong>: Configuración &gt; Privacidad, puedes consultar el registro de uso de permisos, configurar ubicación borrosa, etc.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Precauciones

{class="mt-1"}
HarmonyOS se actualiza continuamente, diferentes versiones pueden tener algunas diferencias. Esta descripción se basa en las principales carácterísticas de HarmonyOS 4.3 y 6, las funciones específicas dependerán de la versión real de tu móvil. Se recomienda mantener el sistema actualizado para obtener las últimas funciones y parches de seguridad.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Prueba ahora: experimenta las funciones carácterísticas de HarmonyOS

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Abre el centro de control, busca "Super Terminal" y verifica si hay otros dispositivos HarmonyOS alrededor.
2. Prueba la "Super Estación de Transferencia": copia un texto a la estación de transferencia y luego arrástralo en Notas.
3. Desliza hacía arriba varios iconos de App de uso frecuente y observa qué contenido muestran sus tarjetas de servicio.
4. Ve a Configuración &gt; Privacidad y revisa qué aplicaciones han usado permisos sensibles recientemente.
:::
