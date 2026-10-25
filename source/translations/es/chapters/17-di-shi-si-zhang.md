---
id: di-shi-si-zhang
num: 14
part: ruan-jian-pian
nav: Capítulo 14: Especial en gestores de contraseñas
toc: default
kind: chapter
---

### Capítulo 14: Especial en gestores de contraseñas

{class="chapter-intro mb-4"}
En la era digital, tus contraseñas son las llaves de tu casa. Pero con demasiadas llaves, demasiado complejas: ¿qué hacer? El gestor de contraseñas es tu «mayordomo de llaves universal».

#### I. ¿Por qué necesitas un gestor de contraseñas?

Una persona moderna tiene decenas o incluso cientos de cuentas en línea. Si usas la misma contraseña para todo, basta una brecha para comprometerlas todas. Si usas una contraseña compleja distinta para cada cuenta, no podrás recordarlas.

El gestor de contraseñas resuelve este dilema: solo tienes que recordar una contraseña maestra; él recuerda todas las demás por ti.

#### II. Cómo funciona un gestor de contraseñas

1. <strong>Almacenamiento cifrado</strong>: Todas las contraseñas se guardan con un cifrado de alto nivel; solo tú puedes descifrarlas.
2. <strong>Contraseña maestra</strong>: Estableces una contraseña maestra para desbloquear la bóveda. La contraseña maestra no se guarda en el servidor.
3. <strong>Rellenado automático</strong>: En las páginas de inicio de sesión de webs y Apps, el gestor rellena cuenta y contraseña automáticamente.
4. <strong>Generador de contraseñas</strong>: Puede generar contraseñas aleatorias y complejas para aumentar la seguridad.

#### 3. Introduccion a los principios de cifrado

Entender el cifrado del gestor de contrasenas te ayuda a decidir si un proveedor es de confianza. A continuacion se explican varios conceptos basicos en lenguaje llano.

##### 1. Cifrado AES-256

AES (estandar de cifrado avanzado) es un algoritmo de cifrado simetrico reconocido por el NIST y ampliamente usado por bancos, militares y gobiernos. "256" indica una clave de 256 bits: en teoria se necesitaria mas tiempo que la edad del universo para forzarlo por fuerza bruta. Los principales gestores (1Password, Bitwarden, KeePass, etc.) cifran tu almacen con AES-256.

##### 2. Arquitectura de conocimiento cero (Zero-Knowledge)

"Conocimiento cero" no significa que el proveedor no almacene nada, sino que <strong>el cifrado y el descifrado se realizan en tu dispositivo; el servidor solo guarda el texto cifrado</strong>. El flujo es:

1. Introduces la contrasena maestra en el cliente.
2. El cliente deriva la clave de cifrado a partir de la contrasena maestra (en tu telefono u ordenador).
3. Solo se sube al servidor el texto cifrado.
4. Al iniciar sesion de nuevo, el servidor envia el texto cifrado y el cliente lo descifra con la contrasena maestra.

Punto clave:<strong>La contrasena maestra nunca sale de tu dispositivo</strong>, ni esta en el servidor. Aunque el proveedor sufra una brecha, el atacante solo obtiene texto cifrado indescifrable, salvo que adivine tu contrasena maestra.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Por que "conocimiento cero" implica que el proveedor tampoco ve tus contrasenas?

{class="mt-1"}
Porque la clave de descifrado se deriva de tu contrasena maestra, que solo existe en tu mente y se usa en tu dispositivo. En el servidor del proveedor no hay ni contrasena maestra ni clave de descifrado, solo texto cifrado. Por eso Bitwarden, 1Password y otros proveedores serios declaran que "tampoco pueden ver tus contrasenas": no es que no quieran, es que tecnicamente no pueden.
:::

##### 3. Funcion de derivacion de claves: PBKDF2 y Argon2

La contrasena maestra no se puede usar directamente como clave de cifrado; debe pasar por una "funcion de derivacion de claves". Su funcion es <strong>ralentizar el calculo a proposito</strong> para que el coste de un ataque por fuerza bruta sea inviable.

- <strong>PBKDF2</strong>: Estandar clasico usado por iCloud Keychain, Bitwarden, LastPass y otros. Ralentiza el descifrado mediante iteraciones repetidas (normalmente mas de 100.000) de hashing.
- <strong>Argon2</strong>: Ganador del concurso de hashing de 2015; mas moderno que PBKDF2. Ademas del consumo de CPU, anade consumo de memoria para que el hardware especializado (GPU/ASIC) no pueda acelerar el descifrado. Lo soportan Bitwarden, KeePassXC y otros.

Cuanto mas altas sean las iteraciones, mas seguro, pero mas lento el desbloqueo. Los proveedores serios publican su algoritmo de derivacion y el numero de iteraciones para que la comunidad de seguridad los audite.

##### 4. Leccion: filtracion de datos de LastPass en 2022

En agosto de 2022, el veterano gestor LastPass anuncio que su entorno de desarrollo habia sido comprometido; en noviembre revelo que el atacante se habia llevado copias de los almacenes de contrasenas de los usuarios (texto cifrado). Lecciones clave:

- <strong>La arquitectura de conocimiento cero resistio</strong>: Como el almacen esta cifrado, el atacante obtuvo texto cifrado pero no pudo descifrarlo, siempre que la contrasena maestra del usuario fuera suficientemente fuerte.
- <strong>Los usuarios con contrasena maestra debil son los mas vulnerables</strong>: El atacante puede forzar la contrasena debil sin conexion; los usuarios con contrasenas debiles o repetidas asumen un riesgo real.
- <strong>Tambien se filtraron metadatos</strong>: Aunque el contenido de las contrasenas esta cifrado, metadatos como URL del sitio y notas podrian no estarlo, revelando que servicios usaba cada usuario.

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Lecciones del incidente de LastPass

{class="mt-1"}
Primero, la contrasena maestra debe ser larga y unica (se recomiendan 16 o mas caracteres con mayusculas, minusculas, numeros y simbolos). Segundo, elige proveedores que soporten Argon2id y un alto numero de iteraciones. Tercero, activa verificacion en dos pasos independiente para cuentas de alto valor (banco, correo); no dependas solo del gestor de contrasenas.
:::

#### 4. Recomendacion de los principales gestores de contrasenas

##### Integrados en el sistema:

- <strong>iCloud Keychain</strong>: La primera opción para usuarios de Apple. Integrado a la perfección con Safari y las Apps, gratuito y seguro. Inconveniente: poco práctico fuera de la plataforma.
- <strong>Google Password Manager</strong>: Cómodo para usuarios de Android; integrado con Chrome y el sistema Android, gratuito.
- <strong>Huawei Password Safe</strong>: Integrado en HarmonyOS, ideal para usuarios de Huawei.

##### Herramientas de terceros:

- <strong>Bitwarden</strong>: Código abierto, gratuito y potente; compatible con todas las plataformas. Muy recomendado para quienes priorizan la privacidad.
- <strong>1Password</strong>: Interfaz cuidada, muchas funciones, ideal para familias y equipos. De pago.
- <strong>LastPass</strong>: Gestor de contraseñas veterano; versión gratuita con funciones limitadas.
- <strong>KeePass</strong>: Almacenamiento totalmente local; código abierto y gratuito. Ideal para usuarios técnicos.

#### 5. Evaluacion real de la seguridad de las contrasenas

Los gestores de contrasenas muestran una barra de "fortaleza" (rojo, amarillo, verde), pero suele basarse solo en longitud y tipos de caracteres, lo cual es incompleto. Para juzgar de verdad si una contrasena es segura hay que considerar la "entropia" y si "ha sido filtrada".

##### 1. Entropia: la medida cientifica de la seguridad de una contrasena

La "entropia" mide la incertidumbre de la contrasena; la unidad es el bit. Cuanto mayor sea la entropia, mas intentos se necesitan para forzarla por fuerza bruta.

- <strong>"123456"</strong>: Entropia bajisima; se descifra al instante.
- <strong>"P@ssw0rd"</strong>: Parece compleja, pero esta en todas las listas de ataques de diccionario; la entropia sigue siendo baja.
- <strong>"correct horse battery staple"</strong>: Cuatro palabras aleatorias; entropia de unos 44 bits; mucho mas dificil de descifrar que "P@ssw0rd".
- <strong>16 caracteres aleatorios (con mayusculas, minusculas, numeros y simbolos)</strong>: Entropia de unos 100 bits; la capacidad de calculo actual no puede forzarla.

Conclusion:<strong>"Longitud + aleatoriedad" es mas importante que "simbolos complejos"</strong>. Por eso las contrasenas largas y aleatorias generadas por el gestor son realmente seguras.

##### 2. HaveIBeenPwned: comprueba si tu contrasena se ha filtrado

Mantenido por el investigador de seguridad Troy Hunt <a href="https://haveibeenpwned.com" class="text-primary hover:underline" target="_blank" rel="noopener">haveibeenpwned.com</a> recoge cuentas y contrasenas de filtraciones masivas anteriores. Puedes:

1. Introducir tu correo para ver si tu cuenta aparecio en alguna filtracion.
2. Usar Pwned Passwords para comprobar si una contrasena esta en una base de datos de filtraciones conocida (los gestores y navegadores ya lo integran).

Si una contrasena aparece en una filtracion,<strong>por muy compleja que parezca, hay que cambiarla de inmediato</strong> porque los ataques de diccionario prueban primero estas contrasenas conocidas.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-shield-alt mr-2"></i>Principio de consulta k-anonimato

{class="mt-1"}
Te preocupa que introducir la contrasena en HaveIBeenPwned vuelva a filtrarla? No hace falta. Las consultas modernas usan el protocolo "k-anonimato": el navegador solo envia los primeros 5 caracteres del hash al servidor, que devuelve todos los hashes que empiezan por esos 5 caracteres y luego se comparan localmente. El servidor nunca ve el hash completo de tu contrasena. Asi funcionan las funciones de "deteccion de contrasenas filtradas" de 1Password y Bitwarden.
:::

##### 3. Funciones de monitorizacion integradas en el gestor

- <strong>1Password Watchtower</strong>: Monitoriza en tiempo real contrasenas debiles, repetidas, filtradas, expiradas y sitios sin 2FA; las clasifica en rojo, naranja o amarillo.
- <strong>Bitwarden Vault Health</strong>: La version gratuita muestra contrasenas debiles y repetidas; la de pago detecta contrasenas filtradas (basandose en HaveIBeenPwned).
- <strong>"Recomendaciones de seguridad" de iCloud Keychain</strong>: Ajustes de iOS &gt; Contrasenas &gt; Recomendaciones de seguridad; indica que contrasenas aparecen en filtraciones conocidas y cuales estan repetidas.
- <strong>"Comprobacion de contrasenas" de Google Password Manager</strong>: Integrado en Chrome; comprueba con un toque si hay contrasenas filtradas, debiles o repetidas.

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Hazlo ahora: comprueba si tus contrasenas son seguras

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Abre haveibeenpwned.com e introduce tu correo habitual para ver en que filtraciones aparece.
2. Usuarios de iPhone: Ajustes &gt; Contrasenas &gt; Recomendaciones de seguridad; resuelve una a una las alertas rojas.
3. Usuarios de Chrome: Ajustes &gt; Contrasenas &gt; Comprobar contrasenas; cambia lo que indique.
4. Usuarios de 1Password/Bitwarden: abre Watchtower/Health Reports y prioriza lo "filtrado" y lo "repetido".
:::

#### 6. Passkey: el futuro del inicio de sesion sin contrasena

Entre 2024 y 2026, la tecnologia de contrasenas esta viviendo una revolucion:<strong>Passkey (clave de acceso)</strong> podria eliminar las contrasenas tradicionales. Apple, Google y Microsoft la impulsan conjuntamente, con el respaldo de la alianza FIDO y el W3C; es el mayor cambio en el inicio de sesion en decadas.

##### 1. Que es Passkey?

Passkey se basa en el estandar FIDO2/WebAuthn y usa <strong>un par de claves en el dispositivo</strong> en lugar de contrasena. El principio se simplifica asi:

- Tu telefono genera un par de claves:<strong>Clave publica</strong>(registrada en el sitio) + <strong>Clave privada</strong>(que permanece en el chip de seguridad de tu dispositivo).
- Al iniciar sesion, el sitio envia un "reto"; tu telefono lo firma con la clave privada y el sitio lo verifica con la clave publica.
- Antes de firmar debes confirmar tu identidad con biometria (Face ID o huella) o el PIN del dispositivo.
- En todo este proceso,<strong>no se transmite ninguna contrasena por la red</strong>.

##### 2. Passkey frente a contrasena tradicional

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                        <thead>
                            <tr class="bg-light dark:bg-gray-700">
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Dimension</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Contrasena tradicional</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Passkey</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Resistencia al phishing</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Baja; el sitio de phishing puede robar la contrasena</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Resistencia natural; la clave privada solo firma para el dominio real</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Impacto de una filtracion del servidor</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">El hash de la contrasena podria descifrarse</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">El servidor solo guarda la clave publica; la filtracion no afecta</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Comodidad</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Hay que memorizar, escribir y gestionar</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Inicio de sesion con Face ID o huella en un segundo</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Ataque de reproduccion</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Podria ser interceptado y reproducido por un intermediario</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cada firma es unica; no se puede reproducir</td>
                            </tr>
                        </tbody>
                    </table>
```

##### 3. Soporte por plataforma

- <strong>Passkey en iCloud Keychain de Apple</strong>: Soporte nativo en iOS 16+ y macOS Ventura+; Passkey se sincroniza entre todos los dispositivos con el mismo Apple ID; al cambiar de dispositivo no hace falta recrearlo.
- <strong>Passkey en Google Password Manager</strong>: Soporte nativo en Android + Chrome; Passkey se guarda en la cuenta de Google y se sincroniza entre dispositivos Android; desde 2023, las cuentas personales de Google permiten iniciar sesion con Passkey.
- <strong>Microsoft</strong>: Windows 11 y Edge ya soportan Passkey; Microsoft account, Outlook, Office y otros servicios lo habilitan progresivamente; se puede gestionar en Microsoft Authenticator.
- <strong>1Password / Bitwarden</strong>: Soporta la creacion, el almacenamiento y la sincronizacion multiplataforma de Passkey; no estas limitado a un solo ecosistema.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>La sincronizacion entre dispositivos es el avance clave

{class="mt-1"}
Al principio, el mayor problema de Passkey era que se vinculaba a un unico dispositivo: al cambiar de telefono habia que recrearlo. Desde 2023, Apple, Google y Microsoft sincronizan Passkey en la nube: iCloud Keychain entre dispositivos Apple y Google Password Manager entre dispositivos Android. 1Password y otros de terceros permiten la sincronizacion entre ecosistemas. Passkey ya es practico para sustituir a la contrasena.
:::

##### 4. Como crear y usar Passkey en el telefono

<strong>Ruta en iOS (iPhone):</strong>

1. En la pagina de seguridad de la cuenta de un sitio compatible (como Google, Microsoft, Amazon, eBay o PayPal), selecciona "Anadir clave de acceso / Add passkey".
2. Aparece la verificacion de Face ID o Touch ID; al confirmarla, Passkey se genera y se guarda en iCloud Keychain.
3. La proxima vez, tras introducir el nombre de usuario, elige "Iniciar sesion con iPhone" y un toque de Face ID basta.
4. Gestion: Ajustes &gt; Contrasenas &gt; busca el sitio y veras la entrada de Passkey.

<strong>Ruta en Android:</strong>

1. En la pagina de seguridad del sitio compatible, selecciona "Anadir clave de acceso".
2. Aparece Google Password Manager &gt; elige tu cuenta de Google &gt; verifica con bloqueo de pantalla (huella, patron o PIN).
3. Passkey se guarda en Google Password Manager y se sincroniza entre dispositivos Android con la misma cuenta.
4. Al iniciar sesion, elige "Usar Passkey" y desbloquea la pantalla.
5. Gestion: Ajustes de Android &gt; Contrasenas, claves y autocompletado &gt; Gestor de contrasenas &gt; google.com.

##### 5. Inicio de sesion con Passkey entre dispositivos

Si inicias sesion en un PC Windows en un sitio donde solo tu iPhone tiene Passkey, puedes autorizar escaneando un codigo QR:

1. En la pagina de inicio de sesion elige "Usar Passkey".
2. Elige "Usar otro dispositivo".
3. El PC muestra un codigo QR; escanealo con el iPhone.
4. El iPhone muestra la verificacion de Face ID; al confirmarla, el inicio de sesion se completa en el PC.

Este proceso usa comunicacion doblemente cifrada por Bluetooth e Internet; la clave privada de Passkey no sale del iPhone.

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Pruebalo ahora: experimenta el inicio sin contrasena

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Inicia sesion en tu cuenta de Google &gt; Seguridad &gt; Claves de acceso &gt; Anadir clave de acceso; prueba el inicio con Face ID o huella.
2. Inicia sesion en tu cuenta de Microsoft &gt; Seguridad &gt; Opciones de seguridad avanzadas &gt; Anadir clave de acceso.
3. Pruebalo en servicios que ya soportan Passkey, como Taobao, JD.com, eBay o PayPal.
4. Conserva la contrasena tradicional como respaldo y migra gradualmente las cuentas de alto valor a Passkey.
:::

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Recomendacion para la transicion

{class="mt-1"}
Passkey no sustituye completamente a la contrasena; muchos sitios siguen en fase de coexistencia. Recomendacion: activa Passkey en las cuentas de alto valor, pero <strong>no borres la contrasena tradicional de inmediato</strong> como respaldo; sigue usando el gestor de contrasenas porque no todos los sitios soportan Passkey. Considera Passkey un "complemento potente del gestor", no un "sustituto inmediato".
:::

#### 7. Llaves de seguridad de hardware

Si tu nivel de seguridad supera al del usuario medio (por ejemplo, posees muchas criptomonedas, eres directivo, periodista o activista, o proteges cuentas criticas de la empresa), una llave de seguridad de hardware es mas fiable que el SMS de verificacion.

##### 1. Que es una llave de seguridad de hardware?

Es un dispositivo fisico (parecido a un pendrive) cuyo chip de seguridad interno almacena tu clave privada; requiere contacto fisico o NFC para verificar. Productos destacados:

- <strong>YubiKey</strong>(de Yubico): la mas habitual; soporta FIDO2/WebAuthn, U2F, OTP, PIV y OpenPGP; disponible en USB-C, USB-A y NFC; serie 5 entre 50 y 70 dolares.
- <strong>Google Titan</strong>: De Google; USB-C + NFC o Bluetooth; unos 30-40 dolares.
- <strong>OnlyKey</strong>: Alternativa de codigo abierto; soporta multiples protocolos.
- <strong>Alternativas nacionales</strong>: Como ePasskey de Feitian; precios mas asequibles.

##### 2. Por que una llave de hardware es mas segura que el SMS?

- <strong>Resistencia al phishing</strong>: Como Passkey, la llave solo responde al dominio real; los sitios de phishing no enganan a la llave.
- <strong>Resistencia al secuestro de SIM</strong>: El SMS puede interceptarse con un ataque de SIM swap; la llave de hardware no depende del numero de telefono.
- <strong>Resistencia al intermediario</strong>: El protocolo FIDO2 incluye un reto en cada firma; no se puede reproducir.
- <strong>Aislamiento fisico</strong>: La clave privada permanece en el chip de hardware; aunque el malware comprometa tu ordenador, no podra leerla.

##### 3. Escenarios de uso

- Cuentas de exchanges de criptomonedas y recuperacion de carteras.
- SSO empresarial, VPN de teletrabajo y acceso SSH a servidores.
- Correo, GitHub y redes sociales como "cuenta maestra": si se compromete, permite restablecer las demas.
- Personas de alto perfil: periodistas, abogados, directivos.

##### 4. Como configurar la llave de hardware como verificacion en dos pasos

Ejemplo con cuenta de Google y YubiKey:

1. Compra una YubiKey (recomendado comprar dos: una para uso diario y otra de respaldo, guardadas en lugares distintos).
2. Entra en myaccount.google.com &gt; Seguridad &gt; Verificacion en dos pasos.
3. Selecciona "Anadir llave de seguridad" &gt; inserta la YubiKey en el puerto USB-C o acerca al lector NFC del telefono.
4. Toca el contacto metalico de la YubiKey segun las instrucciones para completar el registro.
5. Recomendado registrar una segunda llave de respaldo.
6. En los ajustes de verificacion en dos pasos, establece la llave de hardware como metodo principal y el SMS como respaldo.

Sitios compatibles principales: Google, GitHub, Microsoft, Apple ID, Facebook, Twitter, Dropbox, GitLab, AWS, Coinbase, Binance, entre otros.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Estrategia de dos llaves

{class="mt-1"}
El mayor riesgo de la llave de hardware es perderla. Recomendaciones: 1) registra dos llaves distintas; 2) lleva una encima (en el llavero) y guarda otra en la caja fuerte de casa o del banco; 3) en algunos sitios puedes imprimir codigos de recuperacion y guardarlos sin conexion. Asi, si pierdes la principal, no te quedas fuera.
:::

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Cuidado con el canal de compra

{class="mt-1"}
Compra en la tienda oficial o distribuidor autorizado; evita llaves de segunda mano o de origen dudoso, ya que un hardware preconfigurado podria tener una puerta trasera. El firmware de la YubiKey no se actualiza tras la fabricacion, pero Yubico publica avisos de seguridad; consulta su web.
:::

#### 8. Compartir contrasenas en familia o equipo

En la familia, Netflix, el Wi-Fi, el router y la cerradura inteligente se comparten; en el equipo, servidores, bases de datos y cuentas de redes sociales requieren acceso de varias personas.<strong>Enviar contrasenas por WeChat o apuntarlas en un documento compartido son practicas de alto riesgo</strong> si se filtran los chats o los permisos del documento, la contrasena queda expuesta.

##### 1. "Caja fuerte compartida" (Vault) de 1Password

1Password es el producto de referencia para compartir en familia y equipos. Su mecanismo central son <strong>varios almacenes</strong>:

- <strong>Almacen personal</strong>: Solo tu lo ves; para cuentas privadas como banco o correo.
- <strong>Almacen compartido</strong>: Lo ven familiares o companeros de equipo; por ejemplo, Netflix, Wi-Fi de casa o tarjetas de credito compartidas.
- <strong>Permisos por niveles</strong>: La version para equipos permite que algunos miembros solo consulten o consulten sin editar.

Los familiares o companeros no comparten la contrasena maestra; cada uno inicia sesion con su cuenta y ve el contenido del almacen compartido autorizado. Cuando se modifica una contrasena, se sincroniza para todos en tiempo real.

##### 2. Funcion "Organizacion" de Bitwarden

La version gratuita de Bitwarden permite compartir contrasenas individuales (mediante "Send", con limite de tiempo); la version de pago crea "organizaciones" para compartir entradas con familiares o companeros, con permisos detallados. Bitwarden ofrece ademas la opcion de autoalojamiento para empresas que exigen soberania sobre los datos.

##### 3. Entorno familiar: como compartir contrasenas de Netflix, Wi-Fi y similares de forma segura

- <strong>Netflix / sitios de video</strong>: Guarda la contrasena en el almacen compartido de 1Password Families; cada miembro inicia sesion por su cuenta sin enviarla por el grupo.
- <strong>Contrasena del Wi-Fi de casa</strong>: Entre dispositivos iOS se puede compartir el Wi-Fi por AirDrop a los invitados sin decirlo en voz alta; en Android 12+ existe la funcion "Compartir Wi-Fi cercano".
- <strong>Cerraduras inteligentes y electrodomesticos</strong>: Usa la funcion "miembros de la familia" de la app del fabricante para crear cuentas individuales; evita compartir una sola cuenta de administrador.
- <strong>Panel del router domestico</strong>: Guarda la contrasena de administrador en el almacen compartido de 1Password; abre un SSID independiente para el Wi-Fi de invitados.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Relacion calidad-precio de 1Password Families

{class="mt-1"}
1Password Families cuesta unos 4,99 dolares al mes para hasta 5 miembros; cada uno tiene un almacen privado y 4 compartidos. Menos de 1 dolar por persona al mes; es la mejor experiencia de comparticion familiar. La version familiar de Bitwarden cuesta 10 dolares al ano para 6 personas; mejor precio, pero la interfaz es algo inferior.
:::

##### 4. Entorno de equipo: compartir contrasenas de servidores y bases de datos

- <strong>1Password Teams / Business</strong>: Crea almacenes por departamento o equipo de proyecto con permisos detallados; todas las acciones de acceso son auditables.
- <strong>Bitwarden Teams / Enterprise</strong>: Solucion de codigo abierto autoalojable; la version empresarial soporta SSO y sincronizacion de directorios.
- <strong>Principio de separacion de funciones</strong>: La contrasena de administrador no debe estar en manos de una sola persona; nombra 2 o 3 "contactos de emergencia" para que la baja o las vacaciones de alguien no detengan el servicio.
- <strong>Proceso de baja</strong>: Al marcharse un empleado, revoca de inmediato su acceso al gestor y, si es necesario, rota todas las contrasenas sensibles a las que tuvo acceso.

##### 5. Acceso de emergencia (Emergency Access): por si te pasa algo

Imagina que gestionas tu solo todas las cuentas familiares; si tienes un accidente o falleces, tu familia no podra acceder a banco, correo ni seguros.<strong>La funcion "Acceso de emergencia"</strong> esta diseñada para eso: autorizas a un familiar o amigo de confianza a acceder a tu almacen cuando tu no puedas responder.

<strong>Configuracion del acceso de emergencia en Bitwarden:</strong>

1. Entra en la caja fuerte web de Bitwarden &gt; Ajustes &gt; Acceso de emergencia.
2. Anade el correo del contacto de confianza e invitalo a aceptar.
3. Define un "periodo de espera" (recomendado 7-14 dias): el tiempo desde la peticion hasta tu confirmacion.
4. Si no respondes durante la espera (no rechazas ni haces nada), el acceso se concede automaticamente al expirar.
5. Puedes rechazar la peticion o revocar el acceso cuando quieras.

<strong>Acceso de emergencia en 1Password:</strong>

1. 1Password no lo llama "acceso de emergencia" directamente, pero se puede lograr mediante la funcion de "organizacion familiar o de equipo": anade a los familiares y coloca algunas entradas en el almacen compartido.
2. Para usuarios individuales, recomendamos dar la contrasena maestra a un familiar de maxima confianza o guardarla en un sobre cerrado en la caja fuerte.
3. 1Password ofrece tambien un "codigo de recuperacion"; al activar la verificacion en dos pasos, imprimelo y guardalo.

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Hazlo ahora: deja una "llave de repuesto" para tu familia

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Elige a un familiar de confianza como "contacto de emergencia".
2. Configura el acceso de emergencia (Bitwarden) o anadelo al almacen familiar compartido (1Password).
3. Escribe en papel la contrasena maestra y el codigo de recuperacion, metelos en un sobre y guardalos en la caja fuerte de casa o comunicaselo a un familiar de confianza.
4. Revisalo cada seis meses para confirmar que el contacto de emergencia sigue siendo el adecuado.
:::

#### 9. Mejores practicas en el uso del gestor de contrasenas

- <strong>Establece una contraseña maestra fuerte</strong>: La contraseña maestra es la última línea de defensa; elige una larga y compleja y memorízala.
- <strong>Activa la autenticación de dos factores (2FA)</strong>: Activa la verificación en dos pasos para la cuenta de tu gestor: una capa más de protección.
- <strong>Revisa periódicamente las contraseñas débiles</strong>: La mayoría de los gestores tienen una función de «auditoría de seguridad» que te ayuda a encontrar contraseñas débiles y repetidas.
- <strong>No olvides la contraseña maestra</strong>: La contraseña maestra no se puede recuperar; olvidarla significa perder todas las contraseñas. Anótala en papel y guárdala en un lugar seguro.
- <strong>Acceso de emergencia</strong>: Designa un contacto de emergencia para que, si no puedes acceder, una persona de confianza pueda obtener tus contraseñas.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Aviso importante

{class="mt-1"}
Los gestores de contraseñas son cómodos, pero conllevan riesgos: si se filtra la contraseña maestra, todas quedan expuestas. Nunca uses la misma contraseña maestra que para otras cuentas, ni la escribas donde pueda ser encontrada fácilmente. Además, elige proveedores con buen historial de seguridad.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Practica ahora: empieza a usar un gestor de contraseñas

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Elige un gestor (recomiendo Bitwarden o el del sistema).
2. Regístrate y establece una contraseña maestra fuerte.
3. Importar contraseñas existentes (si las tienes) o empezar a añadir nuevas.
4. Instala la extensión del navegador o la App móvil; prueba el relleno automático.
5. Revisa el informe de auditoría de seguridad; encuentra contraseñas que mejorar.
:::
