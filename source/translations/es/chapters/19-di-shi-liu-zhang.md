---
id: di-shi-liu-zhang
num: 16
part: jin-jie-pian
nav: Capítulo 16: Sistema de cuentas y servicios en la nube
toc: default
kind: chapter
---

### Capítulo 16: Sistema de cuentas y servicios en la nube

{class="chapter-intro mb-4"}
Tengo un amigo al que le robaron el móvil el año pasado. Su primera preocupación no fue "cuánto vale el móvil", sino "¿podré recuperar mis fotos?". Lamentablemente, no había activado la copia de seguridad en la nube. El móvil es un objeto material, pero los datos de tu cuenta son cosas que, si se pierden, no vuelven nunca. En este capítulo hablaremos de cómo asegurar tu vida digital de verdad.

#### 1. ¿Qué gestióna exactamente tu cuenta de móvil?

Mucha gente cree que las cuentas solo sirven para descargar Apps. En realidad, detrás de una cuenta de móvil hay muchas más cosas de las que imaginas:

- <strong>Agenda de contactos</strong>:Los números de teléfono que has guardado durante años o incluso décadas.
- <strong>Fotos y videos</strong>:Desde el nacimiento hasta la graduación de tus hijos, desde la primera cita hasta el viaje de boda.
- <strong>Notas</strong>:Notas espontáneas, diarios, contraseñas (sí, mucha gente guarda contraseñas en notas).
- <strong>Historial de compras de Apps</strong>:Apps de pago e compras integradas por las que pagaste cientos.
- <strong>"Buscar mi móvil"</strong>:Tras perder el móvil, es la única herramienta que te permite localizarlo, bloquearlo y borrar los datos remotamente.

Si usas iPhone, todo lo anterior está vinculado a tu Apple ID. Si usas Android, está en tu cuenta de Huawei/Xiaomi/OPPO/vivo y también en tu cuenta de Google. Estas cuentas son tu "libro de registro digital"; si lo pierdes, muchas cosas quedan sin explicación.

#### 2. Tres cosas obligatorias, hazlas ahora

1. <strong>Activa la autenticación de dos factores (2FA)</strong>: Tanto si usas Apple como Android, lo primero es activar la «verificación en dos pasos» en los ajustes de tu cuenta. Es como un pestillo extra en tu puerta: la contraseña sola no basta; tu móvil debe recibir un código. Aunque alguien adivine tu contraseña, sin tu móvil no podrá entrar.
2. <strong>Vincula un método de recuperación fiable</strong>:La autenticación de dos factores es segura, pero tiene un riesgo: ¿qué pasa si pierdes tu propio móvil? Por eso el sistema te pide configurar una "clave de recuperación" o "correo/número alternativo". Es tu única forma de recuperar la cuenta en emergencias; anótala en papel, no la guardes en el móvil.
3. <strong>Confirma que "Buscar mi móvil" está activado</strong>:Esta función te permite localizar, bloquear, hacer sonar e incluso borrar todos los datos del móvil tras perderlo. Es la última línea de defensa. Mucha gente salta este paso al comprar el móvil; cuando lo necesitan descubren que no está activado y ya es tarde.

#### 3. iCloud: el "aire" de los usuarios Apple

Quien usa iPhone tarde o temprano se enfrentará a una pregunta existencial: ¿qué hacer cuando iCloud está lleno?

Apple te regala 5GB gratis; sinceramente, ni para una sola copia de seguridad alcanza. Así que la mayoría acaba recibiendo ese molesto mensaje: "Almacenamiento iCloud lleno". En ese momento tienes tres opciones:

- <strong>Limpiar</strong>:Ve a Ajustes &gt; Tu nombre &gt; iCloud &gt; Gestíonar almacenamiento y mira qué lo ocupa. Generalmente, fotos y copias de seguridad son lo que más espacio ocupan. Puedes empezar borrando copias antiguas innecesarias.
- <strong>Actualizar</strong>:50GB cuesta unos 6 yuanes al mes, 200GB unos 21. Personalmente creo que 50GB bastan para la mayoría: principalmente para copias de seguridad y miniaturas de fotos.
- <strong>Solución indirecta</strong>:Si no quieres gastar, puedes exportar fotos periódicamente al ordenador y desactivar la sincronización de fotos de iCloud. Pero pierdes la comodidad de la copia automática.

Aviso importante: la biblioteca de fotos de iCloud no es "disco en la nube", es "sincronización". Si borras una foto en el móvil, también se borra en iCloud. Si quieres "subir a la nube y luego vaciar el móvil", iCloud Fotos no es lo que necesitas; necesitas Copia de seguridad en iCloud o un disco en la nube de terceros.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-crown mr-2"></i>iCloud+: el trio de privacidad solo para suscriptores de pago

{class="mt-1"}
Al pasar a cualquier nivel de pago de iCloud (50 GB, 200 GB, 2 TB, etc.) te conviertes automaticamente en <strong>iCloud+</strong> y desbloqueas tres funciones de privacidad:

{class="list-disc pl-6 mt-1 space-y-1"}
- <strong>Private Relay (rele privado)</strong>: El "VPN" de Apple. El trafico de Safari pasa por servidores de Apple antes de llegar al sitio; nadie (incluida Apple) puede ver a la vez quien eres y que visitas. Util para proteger la privacidad en Wi-Fi publico. Ruta:<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">Ajustes &gt; Tu nombre &gt; iCloud &gt; Rele privado</code>.
- <strong>Hide My Email (ocultar correo)</strong>: Al registrarte en sitios o apps genera un correo aleatorio de un solo uso; los mensajes se reenvian a tu correo real. Si no quieres recibir mas, desactiva esa direccion y el correo real no queda expuesto. Ruta:<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">Ajustes &gt; Tu nombre &gt; iCloud &gt; Ocultar mi correo</code>.
- <strong>Dominio de correo personalizado</strong>: Puedes enviar y recibir correo de iCloud con tu propio dominio (por ejemplo @tuapellido.com); util para marca personal o gestion del correo familiar.

{class="mt-1"}
Nota: Private Relay no esta disponible en algunos paises o regiones; los usuarios en China pueden necesitar soluciones complementarias.
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-shield-halved mr-2"></i>Proteccion avanzada de datos de iCloud (ADP): cifrado de extremo a extremo real

{class="mt-1"}
A finales de 2022 Apple lanzo <strong>Proteccion avanzada de datos de iCloud (Advanced Data Protection, ADP)</strong>, ampliando el cifrado de extremo a extremo (E2EE) de los pocos datos anteriores (salud, contrasenas) a <strong>la mayor parte de los datos de iCloud</strong>-- fotos, notas, copias de seguridad de iCloud, informacion del dispositivo, 23 categorias en total.

{class="list-disc pl-6 mt-1 space-y-1"}
- <strong>Que es E2EE</strong>: La clave de cifrado solo esta en tus dispositivos; ni los servidores de Apple la tienen. Aunque Apple sea hackeada o las autoridades soliciten los datos, Apple no puede entregar texto plano descifrable.
- <strong>Ruta de activación</strong>:<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">Ajustes &gt; Tu nombre &gt; iCloud &gt; Proteccion avanzada de datos</code>, sigue las instrucciones para configurar contactos o claves de recuperacion (<strong>obligatorio</strong>; si pierdes la clave, tus datos no se podran recuperar).
- <strong>Precauciones</strong>: 1) tras activarlo, guarda bien la clave de recuperacion o no podras recuperar tus datos; 2) albumes compartidos y fototeca compartida de iCloud no estan en E2EE; 3) el Apple ID de China continental no admite ADP; hay que cambiar a otra region.

{class="mt-1"}
En una frase: si tienes datos privados importantes y la region de tu cuenta lo permite, activa ADP; es la mayor proteccion de datos en la nube al alcance de cualquier persona.
:::

#### 4. Sincronización y copia de seguridad: no las confundas

Estas dos palabras suenan parecido, pero las consecuencias son completamente diferentes:

- <strong>Sincronización</strong> es bidireccional: si borras algo en el móvil, también se borra en la nube; si borras en la nube, también en el móvil. Fotos de iCloud, contactos y notas usan sincronización. Ventaja: consistencia multi-dispositivo. Desventaja: "borrado es definitivo".
- <strong>Copia de seguridad</strong> es unidireccional: el móvil toma una "foto instantánea" del estado actual y la guarda en la nube. Si luego borras algo en el móvil, la copia sigue existiendo. iCloud Backup, copia local en PC: todas son copias. Ventaja: datos más seguros. Desventaja: ocupa espacio y no se actualiza en tiempo real.

#### 5. Matriz de cuentas para usuarios Android

La situación en Android es más compleja que en Apple porque tus datos pueden estar dispersos en varias cuentas:

- <strong>Cuenta de marca</strong>(Huawei/Xiaomi/OPPO/vivo): Gestíona tu espacio en la nube, Buscar mi móvil, tienda de Apps, cartera. Cada marca tiene su propio servicio de nube: gratuito básico + pago por ampliación.
- <strong>Cuenta Google</strong>:Si usas Gmail, Google Fotos, Contactos de Google: todo está en tu cuenta de Google. Regala 15GB gratis (más generoso que Apple), pero compartido con Gmail y Drive.
- <strong>WeChat/QQ</strong>:Son independientes del sistema del móvil. Tu historial de chat y Guardar de WeChat no están ni en la cuenta de marca ni en Google; solo existen en los servidores de WeChat.

Por eso los usuarios de Android deben verificar tres cosas por separado: copia de seguridad de marca, copia de Google e historial de chat de WeChat; las tres son indispensables.

#### 6. Familia compartida: que tu familia también se beneficie

La «Familia compartida» de Apple te permite compartir compras de Apps, música, películas y espacio de iCloud con tu familia, y también la ubicación. Se pueden añadir hasta 6 personas. Se configura en: Ajustes → Tu nombre → Familia compartida. Huawei y Xiaomi tienen funciones similares; búscalas en los ajustes de cuenta como «Familia compartida» o «Nube familiar».

Un escenario muy práctico: Configura Familia compartida en el móvil de tus padres; así puedes ver su ubicación en cualquier momento (con su consentimiento). Si un mayor se pierde o no se puede contactar con su móvil, podrás localizarlo.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Las consecuencias de que roben tu cuenta son más graves de lo que imaginas

{class="mt-1"}
Si un hacker obtiene tu contraseña puede: bloquear remotamente tu móvil y exigir rescate, ver tus fotos y contactos, comprar cosas con tus métodos de pago. Peor aún: si tu cuenta está vinculada a muchas cosas, recuperarla es una pesadilla. Así que activa la 2FA, ya mismo.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Practica: haz un chequeo completo de tu cuenta

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Abre los ajustes del móvil, ve a la página de cuenta y confirma que la autenticación de dos factores está activada.
2. Verifica que el "número de confianza" y la "clave de recuperación" estén configurados; anota la clave en papel.
3. Ve a gestión de iCloud/espacio en la nube; revisa qué datos se sincronizan y desactiva lo innecesario.
4. Confirma que "Buscar mi móvil" está activado.
5. Si usas Android, verifica que las tres copias (de marca, Google y WeChat) estén cubiertas.
:::
