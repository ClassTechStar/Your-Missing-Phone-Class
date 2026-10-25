---
id: di-er-shi-yi-zhang
num: 21
part: chao-yue-pian
nav: Capítulo 21: Radiografía de la seguridad de la red móvil y de la información
toc: default
kind: chapter
---

### Capítulo 21: Radiografía de la seguridad de la red móvil y de la información

{class="chapter-intro mb-4"}
Usamos el móvil todos los días para navegar, pagar, chatear... parece muy cómodo. ¿Alguna vez has pensado cuánto "desnuda" está tu información en internet? Sinceramente, la mayoría nunca se lo plantea. Pero cuando algo pasa —cuenta hackeada, tarjeta clonada— ya es tarde para arrepentirse. En este capítulo hablaremos de cómo hacer tu vida digital menos "transparente".

#### I. VPN: la "capa de invisibilidad" en la red

VPN, Red Privada Virtual (Virtual Private Network). Imagínalo como un túnel subterráneo exclusivo y cifrado entre tu casa y el sitio web que visitas. Dentro del túnel puedes moverte libremente; los de fuera no ven qué llevas ni a dónde vas.

- <strong>Navegacion normal</strong>: tu móvil &gt; red publica &gt; sitio web de destino. En cualquier punto intermedio (routers, conmutadores) alguien puede "espiar" los datos que envias. Especialmente en Wi-Fi publicas como cafés o aeropuertos; por decirlo suavemente, es como estar "desnudo".
- <strong>Usar VPN</strong>: tu móvil &gt; tunel cifrado VPN &gt; servidor VPN &gt; sitio web de destino. Los datos estan cifrados y encapsulados; los "espia" solo ven caracteres ilegibles. Además, el sitio web ve la IP del servidor VPN, no tu IP real.

Que puede hacer una VPN? En resumen: primero,<strong>protege tu privacidad en Wi-Fi publicas</strong>; segúndo,<strong>evita restricciones geográficas</strong>(como contenido solo disponible en ciertos países); tercero,<strong>evita que tu ISP registre tus hábitos de navegación</strong>. Pero te advierto:<strong>¡No uses VPNs gratuitos!</strong> Detras de lo gratuito suele estar que tus datos son su "producto". Un amigo uso una VPN gratuita y su móvil empezo a mostrar anuncios; resulto que esa VPN vendía sus datos de navegación a anunciantes. Asi que al elegir VPN, elige marcas de pago (NordVPN, ExpressVPN) o mejor no uses ningúna.

Además, la VPN no es todapoderosa. Solo protege los datos "en tránsito"; si el sitio web de destino no es seguro o tu móvil ya tiene malware, la VPN no puede ayudarte.

#### II. La "trampa dulce" del Wi-Fi publico: más peligrosa de lo que imaginas

Pensaras: "es solo conectar a un Wi-Fi gratis, que riesgo puede haber?" Te cuento un caso real: investigadores de seguridad hicieron un experimento en un aeropuerto, montando un punto de acceso Wi-Fi llamado "Starbucks_Free". En menos de una hora, cientos de personas se conectaron. En realidad ese punto era de los investigadores; todo el <strong>Tráfico sin cifrar</strong> que pasaba por el — como paginas HTTP o comunicaciones de Apps sin TLS — podían interceptarlo y verlo.

Pero hay una premisa clave: hoy en día, la mayoría de tus Apps diarias (WeChat, banca online, Alipay) ya usan cifrado HTTPS. Dicho claramente: aunque el atacante intercepte el paquete de datos, solo verá un montón de caracteres sin sentido,<strong>sin poder leer directamente el contenido de tu chat o tu contraseña de pago</strong>. Sin embargo, aún pueden saber qué sitios web visitas (dominio); si algúna App antigua o página web todavía usa transmisión HTTP en texto plano, el quedará completamente expuesto. Este ataque se llama "ataque de hombre en el medio" (Man-in-the-Middle): el principio es que el atacante se "cuela" entre tú y el router Wi-Fi real. Lo más aterrador es que muchos móviles tienen activada "conexión automática a Wi-Fi conocida"; el atacante solo necesita poner el nombre de su punto de acceso igual al de algún Wi-Fi al que te hayas conectado antes (por ejemplo "ChinaNet" o "CMCC") y tu móvil se conectará automáticamente.

¿Cómo prevenirlo? Algunos consejos prácticos:

- <strong>Confirma HTTPS</strong>:La barra de dirección empieza con https://; la "s" adicional significa Secure. En cualquier sitio donde introduzcas contraseñas, si ves http:// (sin s), ¡para inmediato! Los navegadores modernos muestran "No seguro" antes de sitios no HTTPS; al ver esa alerta, sé cauteloso.
- <strong>Desactiva "conexión automática"</strong>: Tanto iPhone como Android: en ajustes de Wi-Fi desactiva "Unirse automáticamente" o "Conexión automática". Mejor tocar manualmente cada vez que dejar que el móvil decida por ti.
- <strong>Usa datos móviles para operaciones sensibles</strong>: transferencias, banca online, introducir DNI... hazlo con tus propios datos 4G/5G; no escatimes en eso.
- <strong>"Olvida" Wi-Fi poco usadas</strong>: al volver de viajes, "olvida" las Wi-Fi de hoteles y aeropuertos que usaste temporalmente. Así tu móvil no se conectará automáticamente a puntos falsos con el mismo nombre.

#### III. Cómo te protege HTTPS — el handshake SSL/TLS

Mencionamos HTTPS; ¿cómo funciona exactamente? Cada vez que visitas un sitio HTTPS, navegador y servidor realizan un "protocolo de enlace SSL/TLS". El proceso es aproximadamente así:

1. El navegador dice: "Ola servidor, quiero comúnicarme contigo de forma segura; esta es mi lista de capacidades criptográficas (algoritmos soportados, etc.)".
2. El servidor responde: «De acuerdo, he elegido este esquema de cifrado de tu lista; aquí está mi certificado digital con mi clave pública, firmado por la autoridad CA correspondiente».
3. El navegador verifica el certificado: ¿está firmado por una CA confiable? ¿ha caducado? ¿coincide el dominio?
4. Tras verificar, ambas partes usan la clave pública para negociar una "clave de sesión"; toda la comunicación posterior se cifra con esa clave.

Es como ir al banco: presentas tu DNI (certificado), el cajero verifica tu identidad, luego acordáis una contraseña secreta; el resto de la conversación solo vosotros dos la entendéis. Aunque alguien escuche, solo oirá caracteres cifrados.

Pero ojo: HTTPS solo garantiza que el "proceso de transmisión" esta cifrado, no que el sitio web de destino sea de confianza. Los sitios de phishing también pueden usar HTTPS — el candadito solo indica que te conectaste a "un sitio web", no que sea el que querías. Asi que siempre verifica la URL.

#### IV. Seguridad DNS: tu "guía telefonico de red" es seguro?

DNS (Sistema de Nombres de Dominio) es como la guía telefonica de internet: escribes "baidu.com", DNS busca la IP correspondiente (ej: 110.242.68.66) y el navegador puede conectarse. El problema: las consultas DNS tradicionales son <strong>en texto plano</strong>,<strong>sin cifrar</strong>! Es decir, tu ISP, proveedor de Wi-Fi o cualquier nodo intermedio puede ver que sitios web visitas.

Peor aún: "secuestro de DNS": el atacante manipula DNS para que "baidu.com" apunte a un sitio falso. Escribes la URL correcta pero llegas a una página idéntica pero falsa; introduces tu cuenta y contraseña y listo.

Afortunadamente ahora hay soluciiones DNS cifradas:

- <strong>DNS over HTTPS (DoH)</strong>: esconde las consultas DNS dentro del tráfico HTTPS, mezcladas con la navegación web normal; no se puede distinguir cuáles son consultas DNS.
- <strong>DNS over TLS (DoT)</strong>: usa el protocolo TLS para proteger específicamente las consultas DNS; puerto independiente; el administrador sabe que usas DoT pero no ve el contenido.

Personalmente recomiendo Cloudflare 1.1.1.1 o Google 8.8.8.8 como servidores DNS; ambos soportan DNS cifrado. En Android, ve a "DNS privado" y escribe "one.one.one.one" o "dns.google"; súper simple. En iPhone es algo más complicado (necesitas un perfil o App), pero vale la pena.

#### V. ¿La navegación de incógnito te hace realmente invisible?

Primero, la conclusión:<strong>el modo incognito es tu cortina de casa, no una capa de invisibilidad.</strong>

Qué hace: no deja rastros locales —al cerrar la ventana incógnito, el navegador no guarda historial, Cookies, fórmularíos ni búsquedas. Útil para buscar algo en un ordenador ajeno o comprar regalos sin que la familia lo vea en el historial.

Qué NO hace:

- Los sitios web que visitas <strong>aún pueden ver que llegaste</strong>: tu IP, información del dispositivo, comportamiento de navegación; el sitio lo sabe todo.
- Tu ISP <strong>aún puede ver que sitios web visitas</strong>, aunque no el contenido específico (si usas HTTPS).
- Los administradores de red de empresa/escuela <strong>también pueden monitorizar</strong> tu actividad en linea.
- Los archivos que descargas y marcadores agregados <strong>se conservan</strong>; no desaparecen al cerrar la ventana.

Asi que recuerda: el modo incognito es un "borrador local", no una "capa de invisibilidad de red". Si realmente necesitas ocultar tus huellas en linea, necesitas una combinación VPN + navegador Tor; pero para el uso diario, con saber esto es suficiente.

#### VI. Privacidad del navegador: no dejes que el navegador te venda

Quizá no te des cuenta, pero el navegador en sí es un enorme recolector de información. Cookies, historial, caché, autocompletar, permisos de ubicación... todo puede filtrar tu privacidad. Algunos consejos:

- <strong>Limpieza periódica de datos de navegación</strong>:Periódicamente, ve a ajustes y limpia Cookies, caché e historial. No es para evitar "rastreo" (borrar Cookies ya no sirve tanto para eso) sino para evitar que el móvil se vuelva lento; la caché del navegador puede ocupar varios GB.
- <strong>Abandona la fantasía de "Do Not Track"</strong>:La opción "Enviar solicitud 'Do Not Track'" del navegador es básicamente "pedir por favor" que no te rastreen. Pero si los sitios hacen caso o no es otra cosa; la mayoría la ignoran. No cuentes con ello.
- <strong>Usa navegadores con protección de privacidad</strong>:Firefox Focus, DuckDuckGo Browser y Brave bloquean rastreadores y anuncios por defecto; mucho más limpios que Chrome o Safari con sus ajustes predeterminados.
- <strong>El buscador también importa</strong>:Usa DuckDuckGo en lugar de Baidu/Google; no guarda tu historial de búsquedas ni crea perfiles de usuario. Sinceramente los resultados no son tan precisos como Google, pero para consultas diarias basta.
- <strong>Revisa permisos de Apps</strong>:Ve a los ajustes del móvil y revisa qué permisos tiene tu navegador. ¿Realmente necesita acceso a tu ubicación, micrófono o contactos? Casi seguro que no.

#### VII. Lista de seguridad practica: protegete a partir de ahora

Después de todo esto, aquí tienes una lista de seguridad simple y directa. Dedicarle media hora mejorará cualitativamente la seguridad de tu móvil:

1. <strong>Desactiva conexión automática Wi-Fi</strong>:iPhone: Ajustes &gt; WLAN. Android: Ajustes de Wi-Fi.
2. <strong>Cambia a un DNS cifrado</strong>:Android: DNS privado a "dns.google". iPhone: usa App o perfil para configurar DoH 1.1.1.1.
3. <strong>Activa autenticacion en dos factores (2FA)</strong>:WeChat, Alipay, Apple ID, Google: activa 2FA en todos. El SMS ya es el nivel más bajo de 2FA; mejor usar TOTP (Google Authenticator, Microsoft Authenticator).
4. <strong>Revisa permisos de Apps</strong>:Revisa los permisos de cada App, especialmente ubicación, contactos, SMS, micrófono y cámara. Descubrirás que algunas Apps de linterna piden tus contactos —desinstálalas de inmediato.
5. <strong>Limpieza periódica de datos del navegador</strong>:Programa un recordatorío mensual: limpiar caché y Cookies.
6. <strong>No uses cables de puntos de carga publicos</strong>:El puerto USB carga y transfiere datos; puntos de carga maliciosos ("Juice Jacking") pueden robar datos mientras cargas. Lleva siempre tu propio cargador y cable.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Hazlo ya: haz un "chequeo de seguridad" completo a tu móvil

{class="list-decimal pl-6 mt-1 space-y-1"}
1. <strong>Mejora de DNS</strong>:Android: Ajustes &gt; Conexión y compartir &gt; DNS privado &gt; introduce "one.one.one.one" o "dns.google". iPhone: busca en Safari "1.1.1.1 DNS profile" para instalar el perfil, o descarga la App 1.1.1.1 de Cloudflare.
2. <strong>Auditoría de Wi-Fi</strong>:abre la lista de Wi-Fi y "olvida" todos los puntos de acceso que no reconozcas, uses poco o tengan nombres extraños.
3. <strong>Auditoría de permisos</strong>:ve a Ajustes &gt; Privacidad/Gestión de permisos y revisa los permisos de cada App una por una. Marca aquellas Apps cuyos permisos sean irracionales (por ejemplo, una calculadora que pide acceso a contactos) y considera desinstalarlas o usar alternativas.
4. <strong>Verificar seguridad de cuenta</strong>:abre la página de seguridad de tu Apple ID o cuenta Google, verifica si hay dispositivos desconectados desconocidos, confirma que 2FA está activado y comprueba si los contactos de recuperación son confiables.
:::
