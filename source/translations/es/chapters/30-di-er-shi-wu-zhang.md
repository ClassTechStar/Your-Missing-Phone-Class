---
id: di-er-shi-wu-zhang
num: 25
part: chao-yue-pian
nav: Capítulo 25: Qué hacer con un móvil de segunda mano y la herencia digital
toc: default
kind: chapter
---

### Capítulo 25: Tratamiento de móviles de segúnda mano y legado digital

{class="chapter-intro mb-4"}
De "centrado en dispositivo" a "centrado en identidad"

#### : tu caja fuerte de datos personales en la nube es el verdadero centro.

Principio fundamental: la limpieza de datos no es "eliminar", sino "sobrescribir". Mucha gente piensa que arrastrar fotos a la papelera de reciclaje y vaciar el álbum es suficiente, pero cuando se transfiere el teléfono, el nuevo propietario usa software de recuperación de datos y recupera fotos antiguas, historial de chat, fotos de documentos de identidad: este tipo de "exposición pública" ocurre cada año.

1. <strong>Una pregunta última siempre existe: somos "dioses" empoderados por la tecnología, o "cerebros en cubiletes" alimentados por algoritmos?</strong>: Realiza una última copia de seguridad completa, cierra sesión en todas las cuentas (iCloud, cuenta de Huawei/Xiaomi/Samsung, cuenta de Google), desactiva "Buscar mi móvil"; de lo contrario, el siguiente usuario será bloqueado por el bloqueo de activación.
2. <strong>Cuando enciendes la pantalla inconscientemente cada pocos minutos, ¿es eso un hábito tuyo o una "conducta adictiva" diseñada?</strong>: El "restablecimiento de fábrica" de los teléfonos modernos suele incluir un borrado cifrado: destruye la propia clave de cifrado, y una vez que la clave desaparece, todos los datos del disco se convierten instantáneamente en galimatías.
3. <strong>El último "truco de ilusionismo" (solo para dispositivos antiguos)</strong>: Los teléfonos modernos (iOS 8+, Android 6+) ya tienen cifrado completo de disco (FBE) por defecto, el restablecimiento de fábrica destruye las claves de cifrado y los datos teóricamente no se pueden recuperar,<strong>no se necesita este paso</strong>. Solo para dispositivos muy antiguos sin cifrado (anteriores a 2015), es necesario llenar el almacenamiento con archivos basura después del restablecimiento de fábrica y luego ejecutar otro restablecimiento de fábrica.

<strong>Tabla de referencia rápida de rutas de borrado de datos por marca</strong>: Aunque los principios son similares, cada marca oculta el "restablecimiento de fábrica" en un lugar ligeramente diferente. Las diferencias clave son las siguientes.

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                        <thead>
                            <tr class="bg-light dark:bg-gray-700">
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Marca</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ruta de borrado</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Diferencias clave y notas</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Huawei</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ajustes &gt; Sistema y actualizaciones &gt; Restablecer &gt; Restablecer datos de fábrica</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Primero cierra sesión en la cuenta de Huawei y desactiva "Buscar mi móvil", de lo contrario se activará el bloqueo de activación; en modo purificado puede requerir verificación de contraseña.</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xiaomi / Redmi</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ajustes &gt; Mi dispositivo &gt; Restablecer datos de fábrica</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">En la parte inferior hay opciones de "Formatear tarjeta SD virtual" y "Borrar todo el contenido y ajustes"; ambas deben estar marcadas; cierra sesión en la cuenta de Xiaomi antes de desactivar "Buscar dispositivo".</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OPPO / OnePlus</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ajustes &gt; Otros ajustes &gt; Restaurar teléfono &gt; Borrar completamente todos los datos</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ColorOS ofrece un modo de "borrado completo" que sobrescribe el almacenamiento múltiples veces; requiere introducir la contraseña de bloqueo de pantalla para confirmar.</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">vivo</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ajustes &gt; Gestión del sistema &gt; Copia de seguridad y restablecimiento &gt; Borrar todos los datos</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Marca "Formatear almacenamiento del teléfono" para limpiar la zona de la tarjeta SD; cierra sesión en la cuenta de vivo, desactiva "Buscar móvil".</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Samsung</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ajustes &gt; Gestión general &gt; Restablecer &gt; Restablecer datos de fábrica</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Primero elimina la cuenta de Samsung y desactiva "Buscar mi móvil"; algunos modelos tienen opción de "sobrescritura automática", recomendada activar.</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sinceramente, es normal que el móvil empiece a irse lento tras un ano de uso. La causa no necesariamente es que este roto; más a menudo es "acumulacion de basura": archivos basura, procesos en segúndo plano, espacio de almacenamiento llenandose poco a poco.</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ajustes &gt; General &gt; Transferir o restablecer iPhone &gt; Borrar todo el contenido y ajustes</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Debes cerrar sesión en Apple ID primero, de lo contrario el siguiente usuario será bloqueado por el bloqueo de activación de iCloud; iOS 15+ soporta "mantener datos de iCloud al cerrar sesión" para consulta posterior.</td>
                            </tr>
                        </tbody>
                    </table>
```

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Las tres cosas más fáciles de pasar por alto

{class="list-disc pl-6 mt-2 space-y-1"}
- <strong>No cerrar sesión en la cuenta</strong>: Tras vender el teléfono, este es bloqueado remotamente y tú tampoco puedes desbloquearlo; al final tendrás que ir con tu documento de identidad al servicio oficial para desbloquearlo.
- <strong>Tarjeta SD no retirada</strong>: El restablecimiento de fábrica no formatea las fotos de la tarjeta SD externa; recuerda retirarla manualmente o formatearla por separado.
- <strong>Dispositivos USB/OTG no desconectados</strong>: Si hay dispositivos externos conectados durante el borrado, pueden borrarse sus datos por error o interrumpirse el proceso.
:::

#### Construye tu sólida "retaguardía digital".

Los datos de tu teléfono ya no son "virtuales". Contienen tu dinero, relaciones sociales, obras creativas e incluso tu "identidad digital".<strong>Cuando una persona fallece, ¿cómo deberían gestionarse estos activos?</strong> Esta ya no es una pregunta abstracta, sino un dilema real que cada vez más familias enfrentan: los familiares no conocen las contraseñas, las plataformas no permiten heredar, las criptomonedas se pierden para siempre.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-gavel mr-2"></i>Base legal: Artículo 49 de la Ley de Protección de Información Personal

{class="mt-1"}
La "Ley de Protección de Información Personal de la República Popular China", vigente desde 2021, establece en su artículo 49:<strong>Cuando fallece una persona física, sus familiares cercanos pueden ejercer los derechos de acceso, copia, rectificación y supresión de la información personal del fallecido previstos en este capítulo, en beneficio de sus propios intereses legítimos; salvo que el fallecido haya dispuesto otra cosa en vida.</strong>

{class="mt-2"}
Esto significa:

{class="list-disc pl-6 mt-1 space-y-1"}
- <strong>Los familiares cercanos tienen base legal</strong> para solicitar a las plataformas la gestión de las cuentas e información personal del fallecido.
- Los "intereses legítimos" suelen incluir la gestión de herencias, cierre de cuentas, eliminación de información sensible, etc.
- Si el fallecido dispuso algo en vida mediante testamento o acuerdo (como designar un contacto de herencia), se respeta su voluntad.
- Las plataformas no pueden negarse a cooperar alegando "privacidad del usuario", pero los procesos específicos varían según la plataforma.
:::

{class="font-semibold mt-4 mb-1"}
##### 1. WeChat y Alipay: las cuentas no se heredan, pero el dinero sí

Las dos apps más usadas por los chinos tienen reglas diferentes:

- <strong>Cuenta de WeChat</strong>: Según el "Acuerdo de licencia y servicio del software WeChat de Tencent", la propiedad de la cuenta pertenece a Tencent y el usuario solo tiene derecho de uso,<strong>la cuenta en sí no se puede heredar ni transferir</strong>. Pero el dinero dentro de la cuenta, como <strong>saldo de WeChat Pay y fondos de Qianliantong</strong> pertenece a bienes personales; los familiares pueden solicitar el retiro o transferencia a Tenpay con certificado de defunción, certificado de parentesco y escritura notarial de herencia.
- <strong>Alipay</strong>: La cuenta tampoco se puede heredar directamente, pero el saldo de Alipay, Yu'ebao, fondos de gestión financiera, etc.<strong>son bienes heredables</strong>. Los herederos pueden tramitar a través de la "línea de atención al cliente" de Alipay o presentando presencialmente el certificado de defunción y la escritura notarial de herencia; los productos financieros de Ant Wealth deben seguir el proceso de la gestora de fondos.
- <strong>Historial de chat</strong>: Legalmente es privacidad personal; la plataforma no lo proporcionará activamente a la familia. Si involucra pistas sobre la herencia, se puede solicitar mediante demanda o notaría.

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Lo que nunca debes hacer

{class="list-disc pl-6 mt-2 space-y-1"}
- <strong>No entregues las contraseñas de la cuenta del fallecido directamente a la familia para "seguir usándola"</strong>: esto viola el acuerdo de la plataforma, y si los fondos se congelan o se activan controles de riesgo, será más difícil justificarlo.
- <strong>No intentes usar el teléfono del fallecido para recibir códigos de verificación y "retirar dinero"</strong>: puede ser considerado como uso fraudulento, incurriendo en delito.
- <strong>No lo pospongas</strong>: algunas cuentas que no se usan durante mucho tiempo se cancelan automáticamente, dificultando la recuperación de fondos.
:::

{class="font-semibold mt-4 mb-1"}
##### 2. "Contacto de herencia" de Apple: designar con antelación ahorra muchos problemas

Desde iOS 15.2, Apple introdujo la función "contacto de herencia", que permite a los usuarios designar de antemano un contacto de confianza; tras el fallecimiento, este contacto puede presentar <strong>certificado de defunción + clave de acceso del contacto de herencia</strong> para solicitar acceso a los datos de iCloud del fallecido (fotos, notas, contactos, etc.). Pasos:

1. En el iPhone, ve a <strong>[Ajustes] &gt; [tu nombre] &gt; [Inicio de sesión y seguridad] &gt; [Contacto de herencia]</strong>.
2. Toca "Añadir contacto de herencia", usa Face ID para confirmar tu identidad.
3. Selecciona un contacto (de tus contactos); el sistema generará una <strong>clave de acceso</strong>.
4. Entrega la clave de acceso por SMS, correo o imprímela en papel y entrégala, recordando a la persona que la guarde con cuidado.
5. Puedes añadir varios contactos como respaldo, evitando un único punto de fallo.

La persona designada no necesita un dispositivo Apple; con la clave y el certificado de defunción puede solicitar acceso en el sitio web de Apple. El proceso suele completarse en 7 días.

{class="font-semibold mt-4 mb-1"}
##### 3. "Gestor de cuentas inactivas" de Google: gestión automática post mortem

Google ofrece el "Gestor de cuentas inactivas (Inactive Account Manager)", que puede ejecutar automáticamente acciones preestablecidas cuando el usuario no inicia sesión durante mucho tiempo; este es uno de los mecanismos de herencia digital más completos actualmente.

1. : escribe código en la nueva rama, haciendo multiples commits para registrar el progreso. <strong>myaccount.google.com/inactive</strong>, inicia sesión en tu cuenta de Google.
2. Establece el período de inactividad: se activa tras 3 / 6 / 12 / 18 meses sin inicio de sesión.
3. Añade contactos de confianza (hasta 10 personas) y configura qué datos puede acceder cada uno (Gmail, Fotos, Drive, etc.).
4. Opcional: configura una respuesta automática de correo informando a los remitentes que ya no estás disponible.
5. Elige finalmente: al expirar el plazo, ¿<strong>compartir datos con los contactos</strong>, o <strong>eliminar la cuenta directamente</strong>.
6. Configura un número de teléfono como verificación de respaldo para evitar activaciones accidentales.

{class="font-semibold mt-4 mb-1"}
##### 4. Cuentas sociales nacionales: memorialización y proceso de cancelación

Las principales plataformas sociales nacionales tienen dos enfoques para gestionar las cuentas de personas fallecidas:<strong>"Memorialización" (conservar la cuenta para que familiares y amigos la recuerden)</strong> Incluir contexto en vez de aislarlo <strong>"Cancelación" (borrado completo)</strong>. Los familiares pueden solicitar al servicio de atención al cliente de la plataforma presentando certificado de defunción, certificado de parentesco y documento de identidad del solicitante.

- <strong>Weibo</strong>: Soporta la "memorialización" de la cuenta; los familiares solicitan con certificado de defunción y la cuenta se bloquea sin permitir inicio de sesión pero el contenido se conserva, mostrando en el perfil "Esta cuenta se ha establecido como cuenta conmemorativa". También se puede solicitar la cancelación, requiriendo escritura notarial de herencia.
- <strong>Douyin (TikTok China)</strong>: A través de "Yo - Ajustes - Ayuda y comentarios - Cuenta y seguridad - Cancelar cuenta" o atención al cliente manual, presentando certificado de defunción, certificado de parentesco y documento de identidad del solicitante; tras la aprobación, se puede cancelar o convertir en estado conmemorativo.
- <strong>Bilibili</strong>: A través del canal de atención al cliente, presentando certificado de defunción y certificado de parentesco, se puede solicitar la cancelación de la cuenta o su conservación como página conmemorativa; la gestión de videos publicados debe combinar la declaración de derechos de autor.
- <strong>Xiaohongshu</strong>: A través de reclamación al servicio de atención al cliente oficial, presentando certificado de defunción y certificado de parentesco, se puede solicitar la cancelación de la cuenta y el borrado del contenido.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Recordatorio importante

{class="list-disc pl-6 mt-2 space-y-1"}
- Las reglas de las plataformas se actualizan; antes de tramitar, consulta las últimas instrucciones del servicio de atención al cliente oficial.
- Se recomienda escanear y respaldar todos los documentos antes de presentarlos; conserva los originales con cuidado.
- Al tramitar múltiples plataformas a la vez, puedes solicitar una única <strong>escritura notarial de herencia</strong> ahorrando trámites repetidos.
:::

{class="font-semibold mt-4 mb-1"}
##### 5. El desafío de heredar activos digitales

Además de las cuentas sociales, cada vez más personas poseen <strong>activos digitales realmente valiosos</strong>, cuya herencia es aún más compleja:

- <strong>Criptomonedas (Bitcoin, Ethereum, etc.)</strong>: Basado en el principio de "la clave privada es la propiedad",<strong>sin la clave privada, los activos desaparecen</strong>. Los herederos no pueden "reclamar" a la cadena de bloques mediante documentos legales. Recomendación: guarda las frases semilla/claves privadas en fragmentos en múltiples ubicaciones físicas seguras (como caja de seguridad bancaria + caja fuerte en casa) e indica el método de acceso en el testamento.
- <strong>Cuentas de exchange</strong>: Similar a las cuentas bancarias, se puede solicitar a un exchange (como Binance, OKX) la disposición con escritura notarial de herencia, pero los procesos transfronterizos son lentos.
- <strong>Dominios</strong>: Son bienes heredables; los herederos pueden tramitar la transferencia presentando la escritura notarial de herencia ante el registrador de dominios (como Alibaba Cloud, GoDaddy).
- <strong>Propiedad intelectual (artículos originales, videos, patentes, derechos de autor de software)</strong>: Los derechos patrimoniales de los derechos de autor son heredables (los derechos morales no se heredan); los derechos de explotación pueden ser disfrutados por los herederos hasta 50 años después de la muerte del autor.
- <strong>Almacenamiento en la nube y discos de red</strong>: El contenido de los datos pertenece al individuo y es heredable; pero algunos acuerdos de plataforma establecen que la cuenta en sí no es transferible, necesitando descargar primero y luego cancelar.

::: div .danger-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-skull-crossbones mr-2"></i>El coste real de la "desaparición" de las criptomonedas

{class="mt-1"}
Según un informe de Chainalysis, a nivel mundial ya hay <strong>más de 3 millones de Bitcoin</strong> perdidos para siempre por claves privadas perdidas, equivalente a un sexto del total existente. Si posees activos cripto, asegúrate de que al menos una persona en la que confíes absolutamente conozca la <strong>ruta de recuperación</strong>; de lo contrario, esta riqueza permanecerá dormida para siempre en la blockchain.
:::

{class="font-semibold mt-4 mb-1"}
##### 6. Una plantilla de "testamento digital"

Los testamentos tradicionales no cubren los activos digitales. Te recomiendo actualizar anualmente un anexo de "testamento digital" y guardarlo junto con el testamento formal. La siguiente plantilla es de referencia:

::: div .bg-light .dark:bg-gray-700 .rounded-lg .p-4 .mt-2 .mb-3 .text-sm
{class="font-semibold mb-2"}
"Anexo de disposición de activos digitales personales" (plantilla)

{class="mb-1"}
<strong>Parte 1: Lista de cuentas</strong>(Registra solo el nombre de cuenta y la plataforma,<strong>no escribas contraseñas</strong>)

{class="list-disc pl-6 mb-2 space-y-0.5"}
- Sociales: WeChat (cuenta xxx), Weibo, Douyin, Bilibili, Xiaohongshu, etc.
- Pago: Alipay, WeChat Pay, apps bancarias
- Nube: iCloud, Huawei Cloud, Xiaomi Cloud, cuenta de Google, cuenta de Microsoft
- Correo: QQ Mail, NetEase Mail, Gmail, etc.
- Otros: discos de red, servicios de suscripción, cuentas de juegos, etc.

{class="mb-1"}
<strong>Parte 2: Plan de custodia de contraseñas</strong>

{class="list-disc pl-6 mb-2 space-y-0.5"}
- Almacenamiento de la contraseña maestra: usa un gestor de contraseñas (como Bitwarden, 1Password); la contraseña maestra se anota en papel y se guarda en la caja fuerte de casa.
- Claves de recuperación/frases semilla: se guardan en fragmentos en al menos dos ubicaciones físicas (como caja de seguridad bancaria + caja fuerte de casa).
- Persona autorizada para consultar: nombre, número de documento de identidad, relación con el titular, información de contacto.

{class="mb-1"}
<strong>Parte 3: Voluntad de disposición</strong>

{class="list-disc pl-6 mb-2 space-y-0.5"}
- ¿Qué cuentas deseas "memorializar" y cuáles "cancelar"?
- ¿Se designan "contacto de herencia" de iCloud / Google o "gestor de cuentas inactivas"?
- Quién hereda los activos cripto, con instrucciones de acceso a las claves privadas.
- Quién disfruta de los ingresos por derechos de autor.

{class="mb-1"}
<strong>Parte 4: Contactos y plataformas</strong>

{class="list-disc pl-6 space-y-0.5"}
- Nombre del albacea de confianza, información de contacto, contacto de respaldo.
- Canales de atención al cliente de las plataformas habituales y lista de documentos necesarios.
- Fecha de actualización de este anexo: ____/__/__ , próxima revisión: ____/__/__ .
:::

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Advertencia legal sobre "contraseñas"

{class="mt-1"}
Escribir las contraseñas directamente en el testamento conlleva riesgo de fuga, y tras la publicación del testamento todos los herederos podrán verlas.<strong>Es más prudente: en el testamento solo se indica "lista de cuentas + voluntad de disposición + ubicación de custodia de contraseñas", y la contraseña real se transmite al albacea de confianza mediante la contraseña maestra del gestor de contraseñas</strong>. Así se cumplen los requisitos legales y se reduce el riesgo de filtración de contraseñas.
:::

#### Artículo 3: Nuestro objetivo común es mejorar la eficiencia y la experiencia vital. Si mediante diseños inducentes me haces adicto, tengo derecho a desinstalarte.

Un teléfono móvil contiene oro, plata, cobre, tierras raras y decenas de metales; tirarlo libremente contamina el suelo y desperdicia recursos. Hay tres tipos de canales de reciclaje correctos, cada uno con sus ventajas:

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                        <thead>
                            <tr class="bg-light dark:bg-gray-700">
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Canal</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Precio de reciclaje</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Seguridad de datos</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Casos de uso</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Trueque oficial (Huawei/Apple/Xiaomi, etc.)</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Medio, a menudo con vales de descuento añadidos</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">El más alto, con proceso estandarizado oficial</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Más rentable al cambiar a un teléfono nuevo de la misma marca</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Plataforma de reciclaje de terceros (Aihuishou, Zhuanzhuan, Huishoubao, etc.)</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ligeramente superior, se puede comparar</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Relativamente alto, con informe de borrado de datos</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Para monetizar directamente sin vincularse a una marca</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Donación benéfica (como escuelas rurales, organizaciones caritativas)</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sin retorno económico</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Requiere borrado completo por cuenta propia</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">El dispositivo aún funciona y quieres hacer una buena acción</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Segunda vida (modificación propia)</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ahorra dinero en nuevos dispositivos</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">El propietario original sigue usándolo, sin riesgo</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">El dispositivo aún funciona bien y hay necesidades de modificación en casa</td>
                            </tr>
                        </tbody>
                    </table>
```

- <strong>V. Apéndices</strong>: El método más recomendado; el proceso es estandarizado y la seguridad de datos está garantizada. Apple, Huawei, Xiaomi y otras marcas tienen entradas de "trueque" en sus sitios web oficiales; tras la evaluación se puede descontar del precio del teléfono nuevo.
- <strong>Apndice A: Flujo "paso a paso" para desempaquetar un móvil nuevo</strong>: Elige plataformas de reciclaje grandes y de buena reputación; tras hacer el pedido, SF Express recoge el dispositivo en tu casa, lo evalúa y transfiere el pago. Asegúrate de elegir <strong>plataformas que ofrezcan "informe de borrado de datos"</strong> y conserva el comprobante.
- <strong>Donación benéfica</strong>: Puedes contactar con escuelas rurales locales u organizaciones comunitarias; los teléfonos antiguos se pueden adaptar como tablets educativos o teléfonos para ancianos.<strong>Antes de donar, ejecuta el proceso de borrado completo y retira todas las tarjetas SIM/SD</strong>.
- <strong>Revisar apariencia</strong>: Se puede convertir en navegador de coche, centro de control de hogar inteligente, cámara de vigilancia, monitor de bebé, marco de fotos digital. Un teléfono antiguo puede seguir siendo útil durante varios años.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-leaf mr-2"></i>La verdad sobre la basura electrónica

{class="mt-1"}
La placa de circuito de un teléfono contiene <strong>oro, plata, paladio, cobre</strong> y otros metales preciosos; cada tonelada de placas de circuito recicladas contiene decenas de veces más oro que el mineral de oro. Pero si se desecha libremente, el plomo, mercurio y cadmio filtrarán al suelo y al agua subterránea, contaminando durante décadas.<strong>El reciclaje correcto protege el medio ambiente y permite que los metales escasos se reciclen.</strong>
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Verificar información

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Última copia de seguridad completa: sube fotos a la nube, copia archivos importantes al ordenador, exporta y archiva el historial de chat.
2. Cierra sesión en todas las cuentas: iCloud / Huawei / Xiaomi / cuenta de Google, desactiva "Buscar mi móvil".
3. Retira la tarjeta SIM y la tarjeta SD, desconecta todos los periféricos OTG.
4. Ejecuta el restablecimiento de fábrica cifrado; si es necesario, marca "formatear almacenamiento" manualmente.
5. (Solo dispositivos antiguos) Llena el almacenamiento con archivos basura y vuelve a restablecer de fábrica una vez más.
6. Elige su próxima parada: trueque oficial, plataforma de reciclaje certificada, donación benéfica o regalo a un familiar.
7. Actualiza tu "lista de herencia digital" tachando los dispositivos retirados.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-calendar-check mr-2"></i>Lista de tareas de este mes

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Designa un "contacto de herencia" de Apple o configura el "gestor de cuentas inactivas" de Google para tu teléfono principal.
2. Redacta un "Anexo de disposición de activos digitales personales" usando la plantilla de esta sección y habla con tu familia sobre dónde guardarlo.
3. Comprueba si hay más de 2 teléfonos antiguos sin usar en casa y reserva un reciclaje oficial o de plataforma certificada.
:::
