---
id: di-san-zhang
num: 03
part: ji-chu-pian
nav: Capítulo 3: Conecta el móvil a su «línea de vida»
toc: default
kind: chapter
---

### Capítulo 3: Conecta tu teléfono a la "línea de vida" — Redes

{class="chapter-intro mb-4"}
Sin red, el smartphone pierde la mitad de su "inteligencia". La red es la línea de vida del teléfono moderno; comprenderla, usarla bien y protegerla es una asignatura obligatoria para todo usuario de teléfono.

#### 0. No te pierdas al conectarte — distingue la "carretera" y el "vehículo" entre Wi-Fi y datos móviles

Muchas personas ven los iconos de Wi-Fi y de señal encendidos a la vez en la parte superior de la pantalla, pero no entienden la diferencia esencial. El error más clásico es:<strong>conectado al Wi-Fi pero las páginas no cargan</strong>— porque el router perdió la conexión a internet y el teléfono no conmutó automáticamente a los datos móviles. Para entenderlo a fondo, necesitamos construir un modelo mental de "carretera y vehículo".

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-road mr-2"></i>Metáfora central: carretera y vehículo

{class="mt-1"}
Imagina que internet es una ciudad. La <strong>"carretera"</strong> es el canal entre tu teléfono e internet; el <strong>"vehículo"</strong> son los datos que circulan por ella. Wi-Fi y datos móviles son dos carreteras distintas, pero los datos (los vehículos) son los mismos.
:::

{class="font-semibold mt-4 mb-1"}
##### 1. Diferencia esencial: canal local vs. autopista remota

Wi-Fi es esencialmente una <strong>tecnología de red de área local</strong>; es como la carretera inalámbrica tendida por tu edificio, encargada de transmitir los datos del router al teléfono. Pero si la banda ancha no se ha pagado o el cable de fibra está roto, la carretera sigue ahí, pero la "autopista" hacia el exterior se cortó y no se puede llegar a ningúna parte. Los datos móviles, en cambio, se transmiten a través de las estaciones base 4G/5G del operador; equivale a subir directamente a la línea de alta velocidad del operador: con solo haber señal, puedes conectarte a internet.

{class="font-semibold mt-4 mb-1"}
##### 2. Costo y escenarios: cuota mensual fija vs. facturación por uso

Wi-Fi suele ser una inversión única (cuota mensual de banda ancha); mientras haya electricidad, toda la familia puede usarlo de forma ilimitada, ideal para descargar películas, jugar y otros escenarios de gran consumo. Los datos móviles, en cambio, se facturan por uso; al superar el paquete pueden reducir la velocidad o cobrarse aparte, más adecuados para tareas ligeras en el metro, viajes de negocios u otros escenarios móviles.

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-hands-helping mr-2"></i>Prueba: revisa tu paquete de datos

{class="mt-1"}
Abre en el teléfono [Configuración] &gt; [Red móvil] &gt; [Gestión de datos] y comprueba cuántos datos te quedan este mes y qué App consumen más. Saberlo te evitará sustos al salir.
:::

{class="font-semibold mt-4 mb-1"}
##### 3. Consideraciones de seguridad: el Wi-Fi público es un "campo de pesca" oculto

En cuanto a seguridad, los datos móviles suelen ser más seguros que el Wi-Fi público. Los datos móviles van cifrados por el operador, mientras que el Wi-Fi público es vulnerable a "falsos puntos de acceso" montados por hackers para interceptar tráfico no cifrado. Hay que distinguir: hoy, con la generalización de HTTPS, el atacante puede interceptar <strong>qué sitios visitas</strong>(el dominio) y <strong>el contenido HTTP no cifrado</strong>; pero los datos cifrados con HTTPS, como los mensajes de WeChat o las contraseñas de la App bancaria,<strong>no se pueden leer directamente</strong>, salvo que se monte un ataque más complejo de degradación SSL y el usuario ignore las advertencias de certificado. Aun así, al realizar pagos fuera de casa, usar los datos móviles del teléfono sigue siendo la opción más segura.

::: div .danger-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-circle mr-2"></i>Alerta de seguridad

{class="mt-1"}
En aeropuertos, centros comerciales, caféterías y otros espacios públicos, no te conectes a Wi-Fi gratuito con nombres sospechosos (como "Free_WiFi_2024"). Aunque te conectes, nunca inicies sesión en la App del banco ni introduzcas contraseñas a través de él.
:::

{class="font-semibold mt-4 mb-1"}
##### 4. Cómo comprobarlo en el teléfono: lee el "lenguaje oculto" de la barra de estado

¿Cómo saber qué conexión está usando el teléfono? Tomando un teléfono Huawei como ejemplo, si aparece un <strong>icono de flechas bidireccionales</strong> junto a la señal del operador o a la señal de WLAN en la barra de estado, significa que se está usando ese método para acceder a internet; si ambos se encienden a la vez, la aceleración de red está activa y el teléfono aprovecha ambos canales simultáneamente.

En el iPhone es más intuitivo: si el icono de Wi-Fi está encendido, se está usando Wi-Fi; si no, fíjate en los barras de señal de la esquina superior derecha para saber si se usan datos móviles. Algunos teléfonos Android también muestran "5G" o "4G" en la barra de estado, indicando directamente el tipo de red móvil actual.

{class="text-lg font-semibold mt-6 mb-2"}
#### I. Redes móviles (4G/5G) y datos móviles

La red móvil es la base para conectarse en cualquier momento y lugar. De 2G a 5G, la velocidad se ha multiplicado por miles, pero el principio es parecido.

##### Estándares de red:

- <strong>4G LTE</strong>: hoy la cobertura más amplia, velocidad suficiente (teóricamente hasta 100 Mbps+), consumo relativamente bajo.
- <strong>5G</strong>: alta velocidad (teóricamente hasta 10 Gbps), pero la cobertura aún se está completando, mayor consumo. Ideal para descargar archivos grandes y ver videos en alta definición.
- <strong>5G SA vs NSA</strong>: SA es red independiente; NSA se apoya en estaciones base 4G. SA ofrece mejor experiencia, pero requiere compatibilidad tanto del operador como del teléfono.

##### Gestión de datos:

- <strong>Qué son los datos móviles</strong>: la cantidad de datos generada al navegar desde el teléfono. Ver videos y deslizar imágenes es lo que más consume; el texto y la voz consumen menos.
- <strong>Consejos de ahorro</strong>: activa el "modo ahorro de datos" en Configuración y actualiza App o mira videos en alta definición solo bajo Wi-Fi.
- <strong>Barras de señal ≠ velocidad</strong>: una señal fuerte solo indica buena conexión; la velocidad también depende de lo ocupada que esté la estación base y de la distancia a ella.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-circle mr-2"></i>Advertencia importante: ¡desactiva la [itinerancia de datos] antes de salir al extranjero!

{class="mt-1"}
Usar datos móviles en el extranjero puede generar facturas astronómicas. Antes de viajar, desactiva la itinerancia de datos en Configuración o compra con antelación una tarjeta de datos local o un paquete de itinerancia internacional.
:::

#### II. Wi-Fi: conexión, uso compartido y seguridad

Wi-Fi es la principal forma de conexión en hogares y oficinas: rápida y sin consumo de datos. Pero Wi-Fi también evoluciona y las diferencias entre estándares son grandes.

##### Conectarse a Wi-Fi:

Ve a [Configuración] &gt; [WLAN], elige la red e introduce la contraseña. Muchos teléfonos ya permiten conectarse escaneando un código QR, lo que es más cómodo.

##### Compartir la contraseña:

Tanto Android como iOS permiten compartir rápidamente la contraseña desde un teléfono ya conectado. Android genera un código QR; iOS puede compartirla automáticamente al acercar dispositivos.

##### Evolución de los estándares Wi-Fi:

Los estándares Wi-Fi los define IEEE; cada generación trae mejoras notables:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                            <thead>
                                <tr class="bg-light dark:bg-gray-700">
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Estándar</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Protocolo</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Banda</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Velocidad máxima</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Características</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Wi-Fi 4</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">802.11n</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2.4/5GHz</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">600Mbps</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Estándar antiguo, cobertura aceptable</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Wi-Fi 5</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">802.11ac</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">5GHz</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3.5Gbps</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">El más extendido hoy, velocidad suficiente</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Wi-Fi 6</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">802.11ax</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2.4/5GHz</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">9.6Gbps</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Buen rendimiento con múltiples dispositivos, baja latencia</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Wi-Fi 6E</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">802.11ax</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2.4/5/6GHz</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">9.6Gbps</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Añade la banda de 6GHz, menos congestión</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Wi-Fi 7</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">802.11be</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2.4/5/6GHz</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">46Gbps</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Transmisión ultrarrápida, agregación multienlace</td>
                                </tr>
                            </tbody>
                        </table>
```
:::

- <strong>Tecnologías clave de Wi-Fi 6</strong>: OFDMA (acceso múltiple por división de frecuencias ortogonales) permite que varios dispositivos transmitan a la vez; MU-MIMO (multiusuario, múltiples entradas y múltiples salidas) mejora la eficiencia con múltiples dispositivos; TWT (tiempo de activación objetivo) reduce el consumo de los dispositivos.
- <strong>Wi-Fi 6E</strong>: añade la banda de 6GHz sobre la base de Wi-Fi 6, con más canales y menos interferencias. Requiere compatibilidad tanto del teléfono como del router.
- <strong>Wi-Fi 7</strong>: Introduce MLO (Operación Multi-Enlace), permitiendo usar múltiples bandas simultáneamente para transmitir datos, reduciendo drásticamente la latencia. Los canales ultra anchos de 320 MHz permiten un salto en velocidad. Plataformas de chips insignia como Snapdragon 8 Elite Gen5 y Dimensity 9400 ya soportan Wi-Fi 7; modelos como Xiaomi 17, Huawei Mate 80 y Samsung S26 pueden usar redes Wi-Fi 7 (requiere un router Wi-Fi 7).
- <strong>2.4GHz vs 5GHz</strong>: 2.4GHz atraviesa mejor las paredes, pero es más lenta y tiene más interferencias; 5GHz es más rápida pero atraviesa peor. La banda de 6GHz de Wi-Fi 6E/7 es la más rápida, pero la que peor atraviesa las paredes, ideal para uso dentro de la misma habitación.

##### Riesgos del Wi-Fi público:

El Wi-Fi público puede exponerte a hackers que escuchan el tráfico o montan puntos de acceso falsos. Reglas:

- Evita iniciar sesión en cuentas bancarias o introducir contraseñas.
- Lo ideal es usar una VPN para cifrar la conexión.
- No te conectes automáticamente a Wi-Fi desconocido.
- Usa sitios HTTPS (icono de candado en la barra de direcciones).

#### III. Bluetooth: el todoterreno de la comunicación inalámbrica de corto alcance

Bluetooth es probablemente una de las tecnologías inalámbricas que más usas en tu teléfono: auriculares inalámbricos, smartwatch, sistemas del coche, teclados y ratones se conectan a través de él.

##### Principio técnico:

Bluetooth opera en la banda ISM de 2.4GHz y usa la técnica de espectro ensanchado por salto de frecuencia (FHSS) para repartir los datos en 79 canales y conmutar rápidamente, evitando interferencias. La distancia de comunicación se divide en tres clases: Clase 1 unos 100 metros, Clase 2 unos 10 metros (la habitual en teléfonos) y Clase 3 unos 1 metro.

##### Evolución de versiones:

- <strong>Bluetooth 4.0</strong>: introdujo Bluetooth de bajo consumo (BLE), permitiendo que dispositivos con baterías pequeñas como pulseras y bandas de frecuencia cardíaca se conectaran sin cables; la autonomía pasó de días a meses.
- <strong>Bluetooth 4.2</strong>: mejoró la velocidad de transmisión y la privacidad, con compatibilidad con IPv6 directo.
- <strong>Bluetooth 5.0</strong>: duplica la velocidad (2 Mbps), cuadruplica la distancia (teóricamente 300 metros) y octuplica la capacidad de difusión. Admite doble audio (conectar dos auriculares a la vez).
- <strong>Bluetooth 5.1</strong>: incorpora direccionamiento (AoA/AoD), con precisión de posiciónamiento de hasta centímetros.
- <strong>Bluetooth 5.2</strong>: nuevo estándar LE Audio, admite codificación LC3 (mejor calidad y menor consumo), audio multistream y audio de difusión.
- <strong>Bluetooth 5.3/5.4</strong>: optimización adicional del consumo y la estabilidad de conexión, difusión periódica mejorada.

<strong>Adopción de LE Audio</strong>: En 2025-2026, LE Audio ha entrado en una fase de rápida adopción. Los nuevos auriculares inalámbricos verdaderos de las principales marcas (como Huawei FreeBuds Pro 5, Xiaomi Buds 6 Pro, Samsung Galaxy Buds3 Pro, etc.) ya soportan LE Audio y la codificación LC3, ofreciendo menor latencia y mejor calidad de sonido. Al comprar auriculares nuevos, se recomienda priorizar los productos que soportan LE Audio.

##### Escenarios de aplicación:

- <strong>Transmisión de audio</strong>: auriculares inalámbricos, sistemas de audio del coche. LE Audio de Bluetooth 5.2 supone un salto cualitativo en calidad y latencia.
- <strong>Transmisión de datos</strong>: paso de archivos y fotos a corta distancia. Aunque es más lento que Wi-Fi Direct, destaca por su simplicidad.
- <strong>Emparejamiento de dispositivos</strong>: smartwatch, pulseras, teclados y ratones, gamepads.
- <strong>Servicios de ubicación</strong>: balizas Bluetooth (Beacon) para navegación interior y localización de objetos (como Apple AirTag).
- <strong>Hogar inteligente</strong>: red Bluetooth Mesh para controlar bombillas, cerraduras, etc.

#### IV. Control remoto por infrarrojos: el teléfono como mando universal

El control por infrarrojos es una de las tecnologías de control inalámbrico más antiguas, pero sigue siendo práctico en el teléfono. Algunos modelos Android (como Xiaomi y Huawei) incluyen un emisor de infrarrojos que permite controlar televisores, aires acondiciónados, decodificadores y otros electrodomésticos.

##### Principio de funcionamiento:

El mando por infrarrojos emite pulsos de luz infrarroja a una frecuencia específica (normalmente 38 kHz) a través de un LED infrarrojo; el receptor del electrodoméstico decodifica los pulsos y ejecuta la acción correspondiente. Las distintas marcas usan protocolos de codificación diferentes, como NEC, RC5, RC6, SONY, etc. La App de infrarrojos del teléfono incluye una biblioteca de códigos de cada marca: basta con elegir marca y modelo para emparejarlos.

##### Limitaciones:

- <strong>Direccionalidad</strong>: los infrarrojos se propagan en línea recta; hay que apuntar al dispositivo, no atraviesa paredes.
- <strong>Distancia corta</strong>: la distancia eficaz suele ser de 5-8 metros.
- <strong>Apple no lo admite</strong>: el iPhone no tiene emisor de infrarrojos y no puede usar esta función.

#### V. NFC: la magia de "tocar"

NFC (Near Field Commúnicatíon, comunicación de campo cercano) es una tecnología de comunicación inalámbrica de alta frecuencia a distancia muy corta (menos de 10 cm), con una frecuencia de funcionamiento de 13,56 MHz y una velocidad de transmisión de hasta 424 Kbps.

##### Principio de comunicación y modos:

NFC evoluciona a partir de la tecnología RFID y admite tres modos de funcionamiento:

- <strong>Modo lectura/escritura</strong>: el teléfono lee información de etiquetas NFC, como activar acciones al leer una pegatina NFC.
- <strong>Modo punto a punto</strong>: dos dispositivos NFC intercambian datos, como Android Beam (ya retirado).
- <strong>Modo de emulación de tarjeta</strong>: el teléfono emula una tarjeta inteligente; es el modo más usado: tarjetas de transporte, de control de acceso y bancarias funcionan así.

##### Mecanismos de seguridad:

- <strong>Distancia ultracorta</strong>: la comunicación a menos de 10 cm es ya una garantía física de seguridad; la escucha remota es prácticamente imposible.
- <strong>Chip seguro</strong>: el teléfono integra un chip seguro independiente (SE) o usa HCE (emulación de tarjeta por host); las claves de pago se guardan en la zona segura y no se pueden extraer aunque el teléfono esté rooteado.
- <strong>Verificación por huella/rostro</strong>: el pago requiere confirmación biométrica; aunque el teléfono se pierda, no se pueden hacer cargos fraudulentos.
- <strong>Tokenización</strong>: Apple Pay, Huawei Pay, etc., no transmiten el número real de la tarjeta, sino un token de un solo uso; aunque se intercepte, no se puede reutilizar.

##### Aplicaciones típicas:

- <strong>Tarjeta de transporte/control de acceso</strong>: graba la información de la tarjeta física en el teléfono y basta con acercarlo.
- <strong>Pago móvil</strong>: Apple Pay, Huawei Pay, etc., vinculan la tarjeta bancaria al teléfono y pagan con un toque.
- <strong>Emparejamiento de dispositivos</strong>: NFC empareja rápidamente auriculares y altavoces Bluetooth.
- <strong>Autenticación de identidad</strong>: lectura del DNI por NFC, verificación del permiso de conducir electrónico.

#### VI. Punto de acceso personal: convierte el teléfono en router Wi-Fi

Si te sobran datos móviles, puedes activar el punto de acceso para usarlo con la tablet o la computadora.

- <strong>Cómo activarlo</strong>: Configuración &gt; Punto de acceso personal/Compartir red, y actívalo.
- <strong>Precauciones</strong>: consume mucha batería y datos; recuerda poner una contraseña compleja y limitar el número de dispositivos conectados.
- <strong>Compartir por USB</strong>: conecta la computadora con un cable; es más estable y rápido que el punto de acceso inalámbrico.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Manos a la obra: configura y gestióna el punto de acceso

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Abre [Configuración], busca "Punto de acceso personal" o "Compartir red", actívalo y ajusta el nombre y la contraseña.
2. Con otro dispositivo (por ejemplo, la computadora), busca y conéctate a este Wi-Fi.
3. Comprueba desde el teléfono si puedes gestionar los dispositivos conectados o expulsar a los desconocidos.
:::
