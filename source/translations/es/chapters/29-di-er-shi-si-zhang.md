---
id: di-er-shi-si-zhang
num: 24
part: chao-yue-pian
nav: Capítulo 24: Permisos root y bloqueo BL a fondo
toc: default
kind: chapter
---

### Capítulo 24: Permisos Root y bloqueo BL

{class="chapter-intro mb-4"}
Este capítulo es una extensión profunda del contenido del Capítulo 20, dirigido a quienes quieren comprender realmente los mecanismos subyacentes del móvil e incluso intentar flashearlo. Nota: estas operaciones conllevan ciertos riesgos; procede con precaución.

#### I. Entendiendo el Bootloader en profundidad

El Bootloader es el primer programa que se ejecuta al arrancar el móvil; su tarea es inicializar el hardware y cargar el nucleo del sistema operativo. Puedes entender el Bootloader como el "portero" del móvil.

##### Cómo funciona el bloqueo BL:

- <strong>Verificacion de firma</strong>: el bloqueo BL verifica la firma digital de la imagen de arranque; solo sistemas firmados por el fabricante pueden iniciarse.
- <strong>Prevenir degradacion</strong>: evita que los usuarios flasheen versiones antiguas del sistema para explotar vulnerabilidades conocidas.
- <strong>Proteccion de datos</strong>: incluso si se flashea un nuevo sistema, sin la contrasena de la cuenta original no se puede acceder a los datos del usuario.

##### 🔐 Almacenamiento y verificación a nivel de hardware

El estado de bloqueo del bootloader (Locked/Unlocked) y la clave pública del fabricante se suelen almacenar en un área de hardware protegida (como la partición devinfo de Qualcomm, eFuse o partición RPMB), para evitar manipulación por software. En cada arranque, el bootloader lee el estado desde esta área segura y decide si ejecuta la verificación de firma estricta.

##### 🔏 Verificación de firma digital

Cuando los fabricantes publican actualizaciones del sistema o imágenes, las firman con su clave privada. Al iniciar el dispositivo, el bootloader usa la clave pública integrada para verificar la imagen del sistema (como boot.img, recovery.img). Su funcionamiento es:

1. Recalcular el valor hash de la imagen del sistema.
2. Descifrar la firma integrada en la imagen usando la clave pública para obtener un valor hash.
3. Comparar ambos valores hash; si coinciden, la verificación pasa. Esto asegura que la imagen del sistema no ha sido manipulada por terceros.

##### 🔗 Cadena de arranque seguro

El bloqueo del bootloader es el primer eslabón de toda la cadena de arranque seguro. Solo después de pasar la verificación, carga y ejecuta el siguiente programa de arranque (como el kernel), garantizando así capa por capa que el entorno de arranque del sistema es de confianza.

##### 📊 Bloqueado vs. Desbloqueado: El impacto dual del bloqueo del bootloader

Para comprender más intuitivamente las ventajas y desventajas del bloqueo del bootloader, usamos una tabla comparativa para mostrar las diferencias en 5 dimensiones clave:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 dark:border-gray-600 text-sm">
                            <thead>
                                <tr class="bg-gray-100 dark:bg-gray-800">
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Función principal</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Estado bloqueado (predeterminado)</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Estado desbloqueado</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Seguridad del sistema</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Evita flashear sistemas no oficiales sin firmar, protege la integridad del sistema y la seguridad subyacente<br><span class="text-emerald-600 dark:text-emerald-400">✅ Alta seguridad: solo carga imágenes firmadas oficialmente, resistiendo eficazmente la manipulación maliciosa del firmware</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ Seguridad reducida: permite flashear ROMs de terceros, la verificación de integridad del sistema falla, malware con permisos Root puede manipular profundamente el sistema</span></td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Estabilidad del sistema</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Garantiza que el teléfono ejecute el sistema oficial probado y optimizado por el fabricante, asegurando estabilidad y fluidez<br><span class="text-emerald-600 dark:text-emerald-400">✅ Estable: usa firmware oficial, funciones completas, actualizaciones OTA fiables</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ Mayor riesgo: las ROMs de terceros pueden tener problemas de compatibilidad, causando cuelgues, brick, fallos de funciones de hardware (como cámara, carga rápida), y las actualizaciones OTA pueden fallar</span></td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Garantía</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">El fabricante mantiene el sistema oficial estable bloqueando el bootloader para ofrecer servicio de garantía<br><span class="text-emerald-600 dark:text-emerald-400">✅ Garantía válida: disfrutar del servicio de garantía gratuito oficial (daños no intencionales)</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠� Garantía perdida: la mayoría de fabricantes considera que desbloquear el bootloader equivale a renunciar voluntariamente a la garantía; incluso si se vuelve a bloquear, puede detectarse el historial de desbloqueo y rechazar la garantía</span></td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Seguridad de datos</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">El proceso de desbloqueo suele borrar los datos a la fuerza, evitando que los datos antiguos sean explotados maliciosamente en el nuevo entorno del sistema<br><span class="text-emerald-600 dark:text-emerald-400">✅ Datos seguros: en uso diario, el bloqueo del bootloader limita la capacidad del malware para modificar particiones del sistema</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ Riesgo de datos: el desbloqueo borra a la fuerza todos los datos del usuario; si no se cifra correctamente tras el desbloqueo, el almacenamiento de datos puede ser inseguro; en caso de pérdida, es más fácil extraer datos flasheando el dispositivo</span></td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Restricciones de funciones</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Garantiza que las funciones que dependen de un entorno seguro (como pagos, apps bancarias) funcionen correctamente<br><span class="text-emerald-600 dark:text-emerald-400">✅ Funciones completas: todas las funciones oficiales se pueden usar normalmente</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ Funciones limitadas: algunas apps sensibles a la seguridad (como Google Pay, apps bancarias) pueden negarse a funcionar al detectar el estado de desbloqueo del bootloader; los servicios DRM pueden degradarse, afectando la reproducción de video en alta definición</span></td>
                                </tr>
                            </tbody>
                        </table>
```
:::

#### II. Proceso detallado de desbloqueo del BL (ejemplo con Xiaomi)

1. <strong>Solicitar permiso de desbloqueo</strong>: solicita el desbloqueo en la web de herramientas de desbloqueo de Xiaomi.
2. <strong>Vincular cuenta</strong>: vincula tu cuenta Xiaomi en la configuración del móvil.
3. <strong>Alerta de seguridad</strong>: según el nivel de cuenta, hay que esperar 7-30 días.
4. <strong>Operacion de desbloqueo</strong>: usa la herramienta de desbloqueo de Xiaomi conectada al ordenador.

#### III. Múltiples opciones de Root

- <strong>Magisk</strong>: solución de Root moderna, diseno Systemless, puede ocultar el estado de Root.
- <strong>KernelSU</strong>: solución de Root basada en nucleo, más profunda, mejor capacidad de ocultacion.
- <strong>SuperSU</strong>: solución de Root clásica, actualmente discontinuada.

#### IV. Flashear para principiantes

Flashear significa instalar un nuevo sistema operativo en el móvil. Tipos comunes de flasheo:

- <strong>Flashear ROM oficial</strong>: instalar el sistema oficial, para recuperar un "brick" o degradar.
- <strong>Flashear Recovery de terceros</strong>: como TWRP, para respaldo/restauración y flasheo de ROMs de terceros.
- <strong>Flashear ROM de terceros</strong>: como LineageOS, Pixel Experience, etc., para experimentar diferentes sistemas.

#### V. Samsung Knox: El coste irreversible del desbloqueo del bootloader

A diferencia de otros fabricantes Android, el mecanismo de bloqueo del bootloader de Samsung tiene un diseño único de "fusible":<strong>Para los teléfonos Samsung, desbloquear el bootloader activa el fusible Knox, perdiendo permanentemente algunas funciones de seguridad (como Samsung Pay); se borran todos los datos protegidos; afecta a la garantía</strong>. En concreto:

- <strong>El fusible es de un solo uso</strong>: Hay un fusible eFuse dentro del teléfono que, una vez detecta que el bootloader ha sido desbloqueado, se quema permanentemente sin posibilidad de recuperación.
- <strong>Funciones afectadas</strong>: Samsung Pay (tarjeta de transporte/bancaria), carpeta segura Knox, gestión MDM empresarial, algunas apps de seguro de salud quedarán inutilizables.
- <strong>Borrado forzado de datos</strong>: Tras activarse el fusible, el teléfono se restablece de fábrica a la fuerza, todos los datos locales se borran (los datos en la nube no se ven afectados).
- <strong>Impacto en la garantía</strong>: Samsung declara oficialmente que tras el fusible de Knox ya no se ofrece servicio de garantía.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Piénsalo dos veces antes de actuar

{class="mt-1"}
El fusible Knox de Samsung es <strong>irreversible</strong>, una vez activado no se puede volver al estado de fábrica. Si solo quieres usar algunas funciones que normalmente requieren Root, te recomiendo que primero busques alternativas que no lo necesiten.
:::

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-skull-crossbones mr-2"></i>Advertencia importante

{class="mt-1"}
Flashear conlleva riesgos; opera con precaución. Puede causar:

{class="list-disc pl-6 mt-1 space-y-1"}
- Movil "brickeado" (no arranca)
- Perdida de garantía
- Perdida de datos
- Funciones de pago anomalas

{class="mt-1"}
Antes de flashear haz un respaldo completo, lee cuidadosamente el tutoríal y confirma que el modelo y versión coinciden.
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Recursos recomendados

{class="list-disc pl-6 mt-1 space-y-1"}
- <strong>XDA Developers</strong>: la mayor comunidad de desarrolladores Android del mundo, con abundantes tutoríales de flasheo y recursos ROM.
- <strong>Coolapk (KuAn)</strong>: conocida comunidad digital china con muchos tutoríales y discusiones en chino.
- <strong>Foros por modelo</strong>: como Comunidad Xiaomi, Comunidad OnePlus, etc., con tutoríales oficiales y de la comunidad.
:::

#### VI. Preguntas frecuentes (Q&amp; A)

::: div .qa-item .mt-3
{class="font-semibold mb-1"}
<i class="fas fa-question-circle text-primary mr-1"></i>P1: ¿Se puede revertir el desbloqueo del bootloader?

{class="mb-2 pl-6"}
<strong>A:</strong> Se puede volver a bloquear. Normalmente necesitas flashear el paquete completo oficial y usar un script de flasheo específico (como el de Xiaomi <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">flash_all_lock.bat</code>) para volver a bloquearlo. Pero ten en cuenta que, tras volver a bloquearlo, algunos fusibles de seguridad activados por el desbloqueo (como Knox de Samsung) pueden ser irreversibles.
:::

::: div .qa-item .mt-3
{class="font-semibold mb-1"}
<i class="fas fa-question-circle text-primary mr-1"></i>P2: ¿Cómo hacer Root después de desbloquear?

{class="mb-2 pl-6"}
<strong>A:</strong> Desbloquear el bootloader es solo el primer paso. El Root normalmente requiere:

{class="list-decimal pl-12 mb-2 space-y-1"}
1. Flashear un Recovery personalizado (como TWRP).
2. A través del Recovery, flashear Magisk u otro gestor de Root para parchear la imagen boot y obtener permisos de Root.
:::
