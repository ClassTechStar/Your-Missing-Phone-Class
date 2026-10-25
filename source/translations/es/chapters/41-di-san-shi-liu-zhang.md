---
id: di-san-shi-liu-zhang
num: 36
part: er-tong-pian
nav: Capítulo 36: El móvil y el hogar inteligente — que tu casa se vuelva lista
toc: default
kind: chapter
---

### Capítulo 36: El móvil y el hogar inteligente — que tu casa se vuelva lista

{class="chapter-intro mb-4"}
El móvil cumple una función cada vez más importante: ser el «mando a distancia» de toda la casa. Desde una bombilla o un enchufe hasta una cerradura, el hogar inteligente está pasando de «juguete para frikis» a «equipamiento habitual». Este capítulo te ordena las ideas sobre protocolos, ecosistemas, hubs y kits de iniciación, y lo cierra con una lista de seguridad para que la «inteligencia» no se vuelva en tu contra.

#### 1. Protocolos del hogar inteligente: elegir bien importa

Antes de comprar un dispositivo inteligente, mira qué protocolo admite: eso decide si tu móvil y tu ecosistema podrán «mandar» sobre él. Hoy hay cuatro protocolos principales, cada uno con su carácter:

- Protocolo Matter: publicado en 2022 por la CSA (Connectivity Standards Alliance), con Apple, Google, Amazon y Samsung entre sus impulsores. Su objetivo es uno solo: que los dispositivos inteligentes de todas las marcas hablen el mismo idioma. Entre 2023 y 2026 se está convirtiendo rápidamente en el estándar unificado; los dispositivos compatibles pueden conectarse a la vez a Apple HomeKit, Google Home, Amazon Alexa y Mi Home, sin quedar atados a un solo ecosistema.
- Protocolo Thread: la «tubería» de red subyacente de Matter. Bajo consumo, forma su propia red en malla (si un nodo se queda sin luz, la señal encuentra camino alternativo automáticamente), responde rápido y sin tirones. Compra dispositivos con router de borde Thread (como HomePod mini, Apple TV 4K o el gateway central de Xiaomi) y la experiencia será notablemente más estable.
- Wi-Fi: gran ancho de banda y conexión directa al router, pero consume mucho y, con muchos dispositivos, satura el canal; ideal para cámaras y robots aspiradores, que transmiten muchos datos.
- Bluetooth (BLE): fácil de configurar y de bajo consumo, pero de corto alcance y sin red en malla; apto para dispositivos con pocos datos, como cerraduras o termómetros de temperatura y humedad.
- Zigbee: protocolo veterano de bajo consumo con red en malla; necesita un gateway específico. Los dispositivos son baratos y estables, pero la interoperabilidad entre marcas es floja y está siendo sustituido poco a poco por Matter + Thread.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
El principio en una frase

{class="mt-1"}
En 2026, al comprar dispositivos inteligentes, prioriza los que lleven el sello «Matter over Thread»: hoy por hoy es la opción que mejor resiste el paso del tiempo. Los aparatos antiguos que solo admitan Wi-Fi o Bluetooth no hace falta jubilarlos con prisa: úsalos y ya pasarás a Matter en las próximas compras.
:::

#### 2. Comparación de los tres grandes ecosistemas

El protocolo es el «idioma»; el ecosistema, el «círculo». Aunque todo sea compatible con Matter, en el día a día seguirás eligiendo un ecosistema principal para montar las automatizaciones y el control por voz. Esta es la comparación de los tres principales:

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                    <thead>
                        <tr class="bg-light dark:bg-gray-700">
                            <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ecosistema</th>
                            <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ventajas</th>
                            <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Puntos débiles</th>
                            <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Para quién</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple HomeKit</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Privacidad de las más fuertes (procesamiento principalmente local) e integración fluida con iPhone/Siri/Atajos</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menos dispositivos y más caros; necesita un HomePod o un Apple TV como hub</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Usuarios con dispositivos Apple en toda la casa que valoran la privacidad y la experiencia</td>
                        </tr>
                        <tr>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mi Home (Xiaomi)</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">El catálogo más amplio, la mejor relación calidad-precio y un asistente Xiao AI muy práctico</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ecosistema bastante cerrado, muchos datos en la nube y bastantes anuncios</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Usuarios primerizos con presupuesto ajustado que quieren equipar toda la casa en un solo sitio</td>
                        </tr>
                        <tr>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Huawei Smart Life (HarmonyOS)</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Traslado sin costuras entre móviles/tabletas/relojes con HarmonyOS y un catálogo que crece rápido</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pocos dispositivos disponibles fuera de China; el ecosistema aún va a la zaga</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Usuarios de móviles Huawei que valoran la colaboración multi-dispositivo del «Super Terminal»</td>
                        </tr>
                    </tbody>
                </table>
```

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
Consejos para elegir ecosistema

{class="mt-1"}
Elige el ecosistema según tu móvil: los de iPhone, mejor HomeKit; los de Huawei, mejor Smart Life; y para el resto de Android, Mi Home es la opción más cómoda. Gracias al protocolo Matter, un mismo móvil puede controlar dispositivos de varios ecosistemas, así que no hace falta «tomar partido» de golpe.
:::

#### 3. El móvil como hub del hogar

En la mayoría de los montajes de iniciación, tu móvil es el «hub del hogar»: desde la app controlas luces, aire acondicionado, cortinas y seguridad, y además puedes crear escenas automatizadas para que la casa «funcione sola»:

- Control de dispositivos: abres la app de HomeKit, Mi Home o AI Life y puedes encender y apagar luces a distancia o en casa, ajustar la temperatura de color, fijar la temperatura del aire, abrir y cerrar cortinas y ver la imagen de las cámaras.
- Escenas automatizadas: combinas «condición → acción». Las tres escenas más usadas: Modo llegada a casa: el GPS detecta que llegas + es de noche → se enciende la luz de la entrada + el aire acondicionado + se cierran las cortinas + se cierra la cerradura.
- Modo fuera de casa: la última persona se va (el GPS detecta la salida o la cerradura se cierra) → se apagan las luces + el aire + los enchufes, se activan las cámaras y se arma la alarma.
- Modo dormir: todas las noches a las 23:00 → se apagan las luces principales de la casa + se cierran las cortinas + el aire pasa a 26 grados + se enciende la luz nocturna.

- Toque NFC: pega una etiqueta NFC en la puerta y, con solo acercar el móvil, se lanza la escena correspondiente (un toque enciende la luz de la entrada, otro toque activa el modo dormir). Con iPhone se configura con la automatización de «Atajos»; en Android se puede escribir la etiqueta con la app «Cartera» o la del fabricante.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Pruébalo: monta un «modo llegada a casa»

{class="mt-1"}
En la sección «Automatización» de tu app de hogar inteligente, crea una nueva: como condición elige «llegar a un lugar» (casa) y añade como acciones «encender la luz de la entrada», «aire a 26 grados» y «cerrar las cortinas». Guarda, sal a dar una vuelta y vuelve para ver si la luz se enciende sola: la satisfacción de que funcione por primera vez mola más que comprar un gadget nuevo.
:::

#### 4. Kit de iniciación recomendado

No hace falta comprarlo todo de golpe: con estas cuatro piezas cubrirás el 80 % de las necesidades diarias:

- Altavoz inteligente: Xiao AI (ecosistema Mi Home, gran relación calidad-precio) / HomePod mini (ecosistema Apple, sirve además de hub Thread) / Alexa (amplio ecosistema fuera de China). Ojo: el altavoz decide tu ecosistema de voz; primero elige ecosistema y después compra el altavoz.
- Bombillas inteligentes: Yeelight (Mi Home/Matter, ajuste de temperatura de color y brillo, baratas) / Philips Hue (buen color y estables, pero necesitan el gateway Hue y son caras). Ojo: antes de comprar, confirma el tipo de casquillo (E27/B22) y si necesitas regular el color.
- Enchufes inteligentes: Xiaomi Smart Plug (barato, con estadísticas de consumo) / TP-Link Kasa (buen soporte de Matter internacional). Ojo: si lo usas con electrodomésticos de alta potencia (calentador, calefactor), revisa sin falta la potencia nominal para no sobrecargarlo.
- Cerraduras inteligentes: Lockin/Xiaomi (calidad-precio e integración con Mi Home) / Kaadas (fabricante tradicional de cerraduras, mecánica sólida). Ojo: confirma si es compatible con Matter o con tu ecosistema, y fíjate en la duración de la batería y en dónde está el bombín de emergencia.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
Orden de compra sugerido

{class="mt-1"}
Primero el altavoz inteligente (fija el ecosistema) → luego las bombillas y los enchufes inteligentes (barrera baja, resultados inmediatos) → al final la cerradura y las cámaras (afectan a la seguridad, elige con cuidado). Añade una sola categoría cada vez, familiarízate y después amplía, para no acabar con aparatos que no sabes usar.
:::

#### 5. Precauciones de seguridad

Cuantos más dispositivos inteligentes tenga tu casa, mayor será la superficie de ataque. Estas cuatro reglas son innegociables; revísalas una a una:

1. Cambia las contraseñas por defecto: las contraseñas de fábrica de cámaras, routers y cerraduras circulan abiertas por internet; lo primero al comprar es poner una contraseña fuerte, «larga y sin repetir».
2. Actualiza el firmware a tiempo: las actualizaciones del fabricante suelen parchear fallos de seguridad; activa las «actualizaciones automáticas» en la app o revísalo manualmente al menos una vez al mes.
3. Aísla la red: pon los dispositivos IoT en un Wi-Fi aparte (o en la red de invitados), separado de la red principal del móvil y el ordenador. Si algún aparato cae, le costará mucho amenazar lateralmente tus datos importantes.
4. Protege la privacidad: en las cámaras, activa el «área de privacidad» (que no graben el dormitorio o el baño, por ejemplo), desactiva la grabación en la nube las 24 horas y no dejes que apps de terceros accedan durante mucho tiempo a las imágenes de las cámaras de cuando no estás en casa.

::: div .danger-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
Estos agujeros, no los pises

{class="list-disc pl-6 mt-1 space-y-1"}
- No uses la función de «apertura remota» de la cerradura con desconocidos: mejor una contraseña temporal que caduca en cuanto se usa.
- No apuntes la cámara directamente a la cama ni a la ventana: lo que filtras es tu propia intimidad.
- No compres por barato dispositivos «marcas blancas» sin nombre: casi nunca actualizan el firmware, o sea que estarías instalando una puerta trasera en tu casa.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumen del capítulo

{class="list-disc pl-5 text-sm space-y-0.5"}
- Matter + Thread es la dirección unificada de 2023-2026: al comprar un dispositivo nuevo, busca primero ese sello
- Cada ecosistema tiene su fuerte: Apple apuesta por la privacidad y la experiencia, Mi Home por la calidad-precio y Huawei por la colaboración entre dispositivos
- El móvil puede servir de hub: con las tres escenas de «llegada/salida/dormir» bien montadas, la casa se mueve sola
- El kit de iniciación: altavoz, bombilla, enchufe y cerradura inteligentes, añadiéndolos en este orden
- Cambiar las contraseñas por defecto, actualizar el firmware, aislar la red y ocultar la privacidad: cuatro mínimos de seguridad que no se negocian
:::
