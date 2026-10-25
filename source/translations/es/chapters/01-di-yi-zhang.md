---
id: di-yi-zhang
num: 01
part: ji-chu-pian
nav: Capítulo 1: Hola, mi ordenador personal
toc: default
kind: chapter
---

### Capítulo 1: Hola, mi computadora personal

{class="chapter-intro mb-4"}
Tu móvil, en realidad, es la computadora personal más poderosa en tu bolsillo. Es infinitamente más potente que la computadora que llevó al ser humano a la Luna, y sin embargo descansa silenciosamente en tu palma. Hoy, vamos a conocer bien a este "gigante silencioso".

#### 1. Las "vísceras" del hardware del móvil: análisis profundo

Aunque el móvil es pequeño, tiene todos los órganos. Como en una clase de anatomía, conozcamos uno por uno estos componentes de precisión.

##### 1. SoC (System on Chip): el "cerebro + corazón" del móvil

SoC significa System on Chip, que se traduce como "todo el sistema metido en un chip". No es solo la CPU (unidad central de procesamiento), sino que integra CPU, GPU (unidad de procesamiento gráfico), NPU (unidad de procesamiento neuronal), ISP (procesador de señales de imagen), módem (responsable de comunicación), etc., todo en uno.

Es como construir el edificio del gobierno, la central eléctrica, el centro de comunicaciones y la comisaría de una ciudad todos en un solo edificio, la eficiencia es altísima.

##### CPU: el núcleo de la computación general

La CPU es el componente más central del SoC, responsable de procesar la mayoría de las tareas de cálculo. Las CPU de móviles usan la arquitectura ARM, a diferencia de la arquitectura x86 de las computadoras, ARM se carácteriza por un conjunto de instrucciones reducido (RISC), con menor consumo de energía, más adecuada para dispositivos móviles.

<strong>Diseño big.LITTLE de la CPU</strong>: las CPU modernas de móviles adoptan comúnmente una arquitectura "big.LITTLE" (tecnología big.LITTLE de ARM), dividiendo los núcleos en diferentes niveles de rendimiento:

- <strong>Supernúcleo/Núcleo grande</strong>: el de mayor rendimiento, responsable de tareas pesadas. Como carga de juegos, inicio de aplicaciones, cálculos complejos. Frecuencia más alta (3GHz+), pero también mayor consumo.
- <strong>Núcleo medio</strong>: equilibrio entre rendimiento y consumo, procesa tareas de carga media diaria. Navegar redes sociales, ver videos, cambiar entre aplicaciones depende principalmente de él.
- <strong>Núcleo pequeño/Núcleo de eficiencia</strong>: el de menor consumo, procesa tareas ligeras en segúndo plano. Reposo, escuchar música, recibir mensajes, etc., casi no gasta batería.

Los tres niveles de núcleos trabajan juntos: el planificador del sistema asigna automáticamente según la carga de la tarea—las tareas ligeras al núcleo pequeño para ahorrar energía, el trabajo pesado al núcleo grande a toda máquina, y vuelve al pequeño al terminar. Por eso el móvil puede ejecutar juegos fluidamente y también estar en reposo todo el día.

<strong>Características de cada marca</strong>:

- <strong>Qualcomm Snapdragon 8 Elite</strong>: adopta la arquitectura CPU auto-desarrollada Oryon (originada de la adquisición de Nuvia), 2 supernúcleos (4.32GHz) + 6 núcleos de rendimiento (3.53GHz), todos basados en el proceso de 3nm de segúnda generación de TSMC. Se despide definitivamente de la arquitectura de referencia ARM, con mejoras saltadas en rendimiento single-core y multi-core. La GPU es Adreno 830, adopta arquitectura de tiles, el rendimiento gráfico mejora un 40%, la NPU Hexagon tiene una potencia de cálculo de unos 45 TOPS, el rendimiento de inferencia de IA mejora un 45%. (Nota: la versión personalizada de Samsung Galaxy tiene frecuencias más altas, el supernúcleo puede alcanzar 4.47GHz.)
- <strong>MedíaTek Dimensity 9400</strong>: 1 supernúcleo (Cortex-X925, 3.62GHz) + 3 núcleos de rendimiento (Cortex-X4, 3.3GHz) + 4 núcleos de eficiencia (Cortex-A720, 2.4GHz), continúa la arquitectura all-big-core, proceso de 3nm de segúnda generación de TSMC. La GPU es Immortalis-G925 (12 núcleos), el rendimiento pico mejora un 41%, el rendimiento de trazado de rayos mejora un 40%. El procesador de IA es la NPU 890 de octava generación, soporta ejecución de grandes modelos en el dispositivo, entrenamiento LoRA en el dispositivo y generación de video en el dispositivo.
- <strong>Apple A18 Pro</strong>: 2 núcleos de rendimiento (aprox. 4.04GHz) + 4 núcleos de eficiencia (aprox. 2.4GHz), proceso de 3nm de segúnda generación de TSMC. La GPU de 6 núcleos soporta trazado de rayos a nivel de hardware, la NPU de 16 núcleos (aprox. 35 TOPS) proporciona potencia de cálculo para IA en el dispositivo y Apple Intelligence. La arquitectura auto-desarrollada de Apple sigue líderando en rendimiento single-core y eficiencia energética, la arquitectura de memoria unificada proporciona ventaja de ancho de banda para la inferencia de IA.
- <strong>HiSilicon Kirin 9020 de Huawei</strong>: montado en la serie Mate 70, adopta la arquitectura CPU auto-desarrollada Taishan, las capacidades de NPU e ISP se refuerzan continuamente, soporta 5.5G y comunicación por satélite, representa el último avance de los chips nacionales.

##### GPU: motor de renderizado gráfico

La GPU (Graphics Processing Unit) se encarga específicamente de tareas gráficas y de cálculo paralelo. Su número de núcleos es muy superior al de la CPU (fácilmente cientos o miles de núcleos), pero cada núcleo tiene una función relativamente simple, adecuada para procesar simultáneamente grandes cantidades de cálculos similares.

<strong>Flujo de renderizado gráfico</strong>:

1. <strong>Procesamiento de vértices</strong>: calcula las coordenadas de posición de cada vértice en el modelo 3D.
2. <strong>Rasterización</strong>: convierte los gráficos 3D en píxeles en la pantalla 2D.
3. <strong>Sombreado de píxeles</strong>: calcula color, textura, efectos de iluminación para cada píxel.
4. <strong>Composición de salida</strong>: compone todas las capas en la imagen final y la envía a la pantalla.

<strong>Impacto de la GPU en el uso diario</strong>: ¡no solo juegos! El deslizamiento por la interfaz, efectos de animación, reproducción de video, filtros de fotos, aplicaciones AR dependen de la GPU. Un móvil con GPU débil puede tener caídas de frames al deslizar la interfaz, y los juegos se atascan directamente.

<strong>GPU de cada marca</strong>: Qualcomm usa la GPU Adreno auto-desarrollada; MedíaTek usa la GPU Mali de ARM; Apple usa GPU auto-desarrollada, el rendimiento y la eficiencia son referentes en la industria.

##### NPU: motor de aceleración de IA

La NPU (Neural Processing Unit) es un procesador diseñado específicamente para cálculos de redes neuronales. Comparada con CPU y GPU, la NPU es más eficiente y consume menos en tareas de IA.

<strong>Método de cálculo de redes neuronales</strong>: la operación central de la NPU es la multiplicación de matrices y la convolución—precisamente los cálculos más básicos y frecuentes en redes neuronales. La NPU, mediante optimización a nivel de hardware, puede procesar en paralelo grandes cantidades de operaciones matriciales, decenas de veces más rápida que la CPU, con un consumo mucho menor.

<strong>Flujo de procesamiento de IA</strong>:

1. <strong>Entrada de datos</strong>: imagen de la cámara, audio del micrófono, datos de sensores, etc.
2. <strong>Preprocesamiento</strong>: ajusta el formato y tamaño de los datos, adapta los requisitos de entrada de la red neuronal.
3. <strong>Cálculo de inferencia</strong>: la NPU carga el modelo entrenado, realiza el cálculo forward con los datos de entrada, obtiene el resultado.
4. <strong>Postprocesamiento</strong>: convierte la salida de IA en un resultado útilizable, como coordenadas faciales, contenido de texto, etiquetas de escena.

<strong>Escenarios de aplicación reales</strong>:

- <strong>Fotografía computacional</strong>: síntesis nocturna, desenfoque de retrato, procesamiento HDR, embellecimiento con IA.
- <strong>Asistente de voz</strong>: reconocimiento de voz, comprensión del lenguaje natural, síntesis de voz.
- <strong>Traducción en tiempo real</strong>: subtítulos con IA, traducción de diálogo.
- <strong>Reconocimiento inteligente</strong>: reconocimiento de texto (OCR), reconocimiento de objetos, reconocimiento de escenas.
- <strong>Grandes modelos en el dispositivo</strong>: los últimos chips insignia ya soportan ejecutar pequeños modelos de IA en el móvil (nivel de 7B parámetros), logrando diálogo de IA sin conexión, resumen de documentos, escritura inteligente, etc. La NPU Hexagon del Snapdragon 8 Elite tiene una potencia de unos 45 TOPS, la NPU 890 del Dimensity 9400 también soporta grandes modelos en el dispositivo (velocidad de inferencia LLM mejora un 80%), la NPU de 16 núcleos del Apple A18 Pro proporciona unos 35 TOPS.
- <strong>Procesamiento de imágenes con IA</strong>: eliminación con IA (eliminar personas de fotos con un toque), expansión de imagen con IA (expandir los bórdenes), conversión de estilo con IA, generación de imágenes a partir de texto, etc.

##### ISP: procesador de señales de imagen

El ISP procesa los datos originales de la cámara, convirtiendo señales de luz en fotos bonitas.

<strong>¿Cómo evaluar el rendimiento?</strong>¡Mira el modelo! Apple A18 Pro, Qualcomm Snapdragon 8 Elite, MedíaTek Dimensity 9400, HiSilicon Kirin 9020 de Huawei son todos de nivel insignia. En la gama media mira el Snapdragon 8s Gen3/7+ Gen3, Dimensity 8400. No mires solo el número de núcleos, la arquitectura y el proceso (nanómetros) son más importantes. El proceso de 3nm es el más avanzado actualmente, con eficiencia energética muy superior a 5nm y 4nm.

##### 2. RAM (memoria de trabajo): mesa de trabajo temporal

La RAM es como tu escritorío, cuanto más grande, más archivos puedes extender a la vez. 12GB es lo mainstream ahora, 16GB para usuarios intensos, más de 24GB es para gamers y geeks.

El tipo de RAM también es importante: LPDDR5 es más rápida y eficiente que LPDDR4X. Apple aunque no tiene mucha RAM, la optimización del sistema es buena, por eso parece "suficiente".

<strong>¿Qué pasa si no hay suficiente RAM?</strong> Las Apps serán cerradas por el sistema en segúndo plano, al cambiar necesitarán recargar. Por eso a veces al cambiar a WeChat, el juego se ha ido.

##### 3. Almacenamiento (ROM/flash): almacén a largo plazo

El almacenamiento es como tu librería, donde se guardan todas las fotos, videos, Apps. Ahora lo mainstream es UFS 3.1 o UFS 4.0, varias veces más rápido que el antiguo eMMC.

<strong>¿Por qué es importante la velocidad de almacenamiento?</strong> Determina la velocidad de apertura de Apps, de carga de juegos, de guardado de fotos. Con el uso, un almacenamiento lento hará el móvil cada vez más lento.

##### 4. Pantalla: tus ojos

La pantalla es la principal ventana de interacción entre tú y el móvil, su calidad afecta directamente la experiencia.

- <strong>Material</strong>: OLED tiene colores vivos, alto contraste, más eficiente (al mostrar negro los píxeles no emiten luz), pero a baja luminosidad puede tener parpadeo que cansa la vista; LCD es más amable con los ojos, más barato, pero el contraste y los colores no son tan buenos como OLED.
- <strong>Resolución</strong>: 1080P es lo mainstream, 2K es más nítido pero gasta más batería. El concepto de "pantalla Retina" de Apple es: a cierta distancia, el ojo humano no distingue los píxeles.
- <strong>Tasa de refresco</strong>: 60Hz es el estándar, 90Hz/120Hz es más fluido, el deslizamiento es sedoso. La alta tasa de refresco gasta batería, por eso muchos móviles soportan tasa de refresco adaptativa (LTPO), ajustándose dinámicamente según el contenido.
- <strong>Tasa de muestreo táctil</strong>: afecta la velocidad de respuesta táctil, los gamers deben prestarle atención, cuanto más alta, más responde.
- <strong>Método de atenuación</strong>: la atenuación DC es más amable con los ojos que la PWM, a baja luminosidad cansa menos. Ahora muchos móviles soportan PWM de alta frecuencia, también para cuidar los ojos.

##### Tecnología HDR de pantalla

HDR (High Dynamic Range) permite a la pantalla mostrar simultáneamente zonas más brillantes y más oscuras, mejorando mucho la sensación de profundidad de la imagen.

- <strong>Principio de implementación</strong>: el rango de luminosidad de una pantalla normal es limitado (SDR), la diferencia entre lo más brillante y lo más oscuro no es suficiente. Las pantallas HDR tienen mayor luminosidad pico (normalmente más de 1000 nits), mayor contraste, gama de colores más amplia, pueden mostrar más detalles.
- <strong>Estándares principales</strong>: HDR10 (el más básico, gratuito y de código abierto), HDR10+ (impulsado por Samsung, metadatos dinámicos), Dolby Vision (la mejor calidad pero requiere licencia). Qué estándar soporta el móvil depende del hardware de pantalla y la licencia del sistema.
- <strong>Efecto real</strong>: al ver video HDR, la luz del sol es más deslumbrante, las sombras más profundas, los colores más ricos. La condición es que el video mismo esté producido en HDR y la pantalla soporte HDR.

##### Tecnología HDR de imagen

El HDR al fotografiar y el HDR de pantalla son dos cosas distintas. El HDR de imagen resuelve mediante algoritmos el problema de "sobreexposición en zonas claras, negro muerto en zonas oscuras".

- <strong>Principio del algoritmo</strong>: al pulsar el obturador, el móvil en realidad toma varias fotos con diferentes exposiciónes (subexpuesta para conservar detalles de zonas claras, sobreexpuesta para conservar detalles de zonas oscuras, exposición normal para conservar tonos medios), luego las sintetiza en una foto de alto rango dinámico.
- <strong>Flujo de procesamiento</strong>: captura multi-fotograma → alineación y compensación (anti-sacudida) → fusión de exposición/mapeo de tonos → corrección de color → salida de la foto final.
- <strong>Optimización del efecto</strong>: ahora los móviles ya pueden hacer "HDR en tiempo real"—lo que ves en el visor es el efecto procesado con HDR, lo que ves es lo que obtienes. El Smart HDR de Apple y el HDR automático de Android son muy maduros.

##### 5. Batería y carga: la fuente de energía

La batería es el componente "más efímero" del móvil, tras dos o tres años se degrada notablemente. La capacidad mainstream ahora es 5500-7500mAh.

- <strong>Potencia de carga</strong>: el campo Android ha llegado a 100W incluso 200W, se llena en unos minutos; Apple sigue en 20-30W. ¿La carga rápida daña la batería? Con accesorios originales no hay mucho problema, el móvil tiene protección de temperatura.
- <strong>QC 5.0</strong>: cómoda pero ineficiente y con mucho calor. Adecuada para cargar en la oficina, no para cuando tienes prisa por salir.
- <strong>Carga inversa</strong>: el móvil se convierte en power bank, carga auriculares, reloj, para emergencias.

##### 6. Cámara: la magia de luz y sombra

Ahora los móviles tienen fácilmente tres o cuatro cámaras, cada una con su función:

- <strong>Cámara principal</strong>: la más usada, con el sensor más grande, la mejor calidad.
- <strong>Ultra gran angular</strong>: para paisajes, edificios, campo de visión más amplio.
- <strong>Teleobjetivo</strong>: para cosas lejanas, hay zoom óptico y zoom digital.
- <strong>Macro</strong>: para cosas muy pequeñas de muy cerca.

<strong>¡Los megapíxeles no lo son todo!</strong> El tamaño del sensor (un sensor mayor es mejor), la apertura (f/1.8 es mayor que f/2.4), el estabilizador (el OIS óptico es importante) afectan la calidad. La fotografía computacional (algoritmos de IA) es cada vez más importante, puede combinar varias fotos en una buena foto.

##### Teleobjetivo periscópico

Los teleobjetivos tradicionales necesitan una ruta óptica larga, lo que haría el móvil muy grueso. El teleobjetivo periscópico usa un prisma de 90 grados para refractar la luz, permitiendo que la ruta óptica se despliegue horizontalmente dentro del móvil, logrando así zoom óptico de 5x o incluso 10x manteniendo el móvil delgado.

- <strong>Principio estructural</strong>: la luz entra por la lente → el prisma la refracta 90 grados → atraviesa el grupo de lentes a lo ancho del móvil → llega al sensor. Equivale a poner un telescopio vertical en horizontal.
- <strong>Características ópticas</strong>: alto zoom óptico (5x-10x), calidad muy superior al zoom digital. Pero el sensor suele ser más pequeño que el de la cámara principal, el rendimiento en poca luz es normal.
- <strong>Ventajas de imagen</strong>: fotografiar la luna, edificios lejanos, primeros planos en un escenario, inalcanzable para móviles normales.

##### OIS estabilización óptica vs EIS estabilización electrónica

La estabilización es una tecnología clave que afecta la calidad de fotos y video, los dos métodos tienen principios completamente distintos:

- <strong>OIS (estabilización óptica)</strong>: compensa el temblor de la mano moviendo físicamente la lente o el sensor. La lente tiene internamente un giroscopio miniatura que detecta la dirección y amplitud del temblor, luego accióna un motor para mover el grupo de lentes en sentido contrario. La ventaja es que no pierde calidad, la desventaja es el coste y el espacio.
- <strong>EIS (estabilización electrónica)</strong>: compensa el temblor recortando y desplazando la imagen mediante algoritmos. El móvil graba un área ligeramente mayor, luego recorta la zona estable según los datos del giroscopio. La ventaja es que no necesita hardware adicional, la desventaja es que recorta la imagen (menor campo de visión), en poca luz puede salir borrosa.
- <strong>Elección práctica</strong>: para fotos prioriza OIS, para video la combinación de ambos es lo mejor. Ahora muchos móviles insignia soportan estabilización por desplazamiento del sensor "Sensor-Shift", mejor que la estabilización tradicional de lente.

##### Zoom óptico vs zoom digital

- <strong>Zoom óptico</strong>: cambia la distancia focal moviendo físicamente el grupo de lentes, sin pérdida de calidad. El zoom óptico en móviles suele ser de multiplicadores fijos (como 2x, 3x, 5x, 10x), no puede hacer zoom continuo como una cámara.
- <strong>Zoom digital</strong>: amplía la zona central de la imagen, en esencia es recorte + interpolación. Cuanto más amplíes, peor calidad. Un zoom digital de 100x parece impresionante, pero la calidad ya es muy borrosa.
- <strong>Zoom híbrido</strong>: combina óptico y digital, entre los multiplicadores de zoom óptico usa algoritmos de síntesis multi-fotograma para compensar la pérdida de calidad. Mejor que el digital puro, pero aún inferior al óptico.

##### Audio: altavoces y chip gráfico dedicado

<strong>Altavoz único vs altavoces duales</strong>:

- <strong>Altavoz único</strong>: solo una unidad de sonido en la parte inferior, el sonido se desvía a un lado, sin sensación estéreo. Común en móviles de gama media-baja.
- <strong>Altavoces duales (estéreo)</strong>: un altavoz arriba y otro abajo, formando un campo sonoro estéreo. Al ver videos o escuchar música, los canales izquierdo y derecho son nítidos, la inmersión es mucho mayor. Que el auricular funcióne también como altavoz superior es una solución común.
- <strong>Diferencia de calidad de sonido</strong>: los altavoces duales no solo son "más ruidosos", la clave es la sensación espacial y la jerarquía. Ver películas con un solo altavoz siempre parece faltar algo.

<strong>Chip gráfico dedicado para móviles gaming</strong>:

Algunos móviles gaming y de rendimiento equipan un chip dedicado de procesamiento de pantalla, su función es:

- <strong>Insertar frames</strong>: interpola la imagen de juego de 30fps a 60fps o 120fps mediante algoritmos, la imagen es más fluida. Este proceso se completa en el chip gráfico dedicado, sin ocupar recursos GPU del SoC.
- <strong>Superresolución</strong>: mejora la imagen de baja resolución a alta resolución mediante algoritmos de IA, la calidad es más nítida.
- <strong>Reducción de consumo</strong>: como la inserción de frames y la superresolución las hace el chip dedicado, la carga del SoC se reduce, el calor y el consumo disminuyen, el juego es más estable.

##### GPS: single-frequency y dual-frequency

El posiciónamiento del móvil depende principalmente de sistemas de navegación por satélite como el GPS.

- <strong>GPS single-frequency</strong>: solo recibe señales de la banda L1, precisión de posiciónamiento de unos 3-5 metros. Suficiente en zonas abiertas, pero en cañones urbanos con muchos rascacielos, la reflexión de señales causa mayores desviaciones.
- <strong>GPS dual-frequency</strong>: recibe simultáneamente las bandas L1 y L5. La banda L5 tiene una longitud de onda mayor y mayor resistencia a interferencias, el cálculo conjunto dual-frequency puede eliminar la mayoría del error ionosférico, la precisión llega a 1-3 metros. Ventaja evidente en navegación urbana y posiciónamiento de taxis.
- <strong>Soporte multi-constelación</strong>: los móviles modernos no solo soportan GPS, también soportan BeiDou (China), GLONASS (Rusia), Galileo (Europa) y otros sistemas de satélites. Cuantos más satélites se conecten simultáneamente, más rápido y preciso es el posiciónamiento.

##### 7. Sensores: las pequeñas antenas del móvil

El móvil esconde más de una docena de sensores, trabajando silenciosamente:

- <strong>Acelerómetro + giroscopio</strong>: percibe la postura del móvil, giro en juegos, rotación automática de pantalla.
- <strong>Sensor de luz</strong>: ajusta automáticamente el brillo de la pantalla.
- <strong>Sensor de proximidad</strong>: apaga la pantalla al acercar el móvil a la oreja en una llamada.
- <strong>Sensor de huellas</strong>: ahora lo mainstream es huella óptica o ultrasónica bajo la pantalla.
- <strong>Reconocimiento facial</strong>: el Face ID de Apple es estructura de luz 3D, nivel de seguridad alto; muchos Android usan reconocimiento de foto 2D, seguridad normal.
- <strong>Has establecido contrasena de bloqueo?</strong>: comunicación de campo cercano, tarjetas de transporte, tarjetas de acceso, tarjetas bancarias.
- <strong>Barómetro</strong>: mide la altitud, hasta subir escaleras lo detecta.
- <strong>Sensor Hall</strong>: detecta la apertura/cierre de fundas magnéticas.

#### 2. Sistema operativo: Android VS iOS VS HarmonyOS

El hardware es el cuerpo, el sistema operativo es el alma. Los tres sistemas tienen sus carácterísticas:

- <strong>Android</strong>: como una comunidad de código abierto, los fabricantes pueden personalizarlo profundamente, muchas opciones. Puedes cambiar temas, instalar tiendas de aplicaciones de terceros, probar todo tipo de cosas. Pero precisamente por ser abierto, la fragmentación es grave, la experiencia varía mucho entre marcas.
- <strong>iOS</strong>: como un jardín cuidado, Apple controla hardware y software, experiencia unificada y fluida. Calidad de aplicaciones alta, protección de privacidad buena, pero libertad baja, muchas cosas se hacen según las reglas de Apple.
- <strong>HarmonyOS</strong>: la nueva especie de Huawei, su capacidad distribuida permite que diferentes dispositivos colaboren sin fisuras. Lo trataremos especialmente más adelante.

Los tres ecosistemas son extremadamente ricos, elige el estilo de vida que te guste. No hay buenos ni malos absolutos, solo adecuado o no.

#### 3. Análisis completo de interfaces del móvil

Las interfaces del móvil son el puente que conecta con el mundo exterior, las diferentes interfaces tienen grandes diferencias:

##### Micro USB

- <strong>Características físicas</strong>: interfaz trapezoidal plana, diferencia frente/dorso (no entra si la insertas al revés). Básicamente eliminada en móviles, pero algúnos dispositivos de gama baja y antiguos aún la usan.
- <strong>Limitaciones de transmisión</strong>: solo soporta el estándar USB 2.0, velocidad máxima de 480Mbps, potencia de carga normalmente no superior a 10W.
- <strong>Desventajas</strong>: sin inserción reversible, corta vida útil de inserción/extracción, velocidad de transmisión lenta, baja potencia de carga.

##### Lightning (interfaz relámpago de Apple, obsoleta)

- <strong>Características físicas</strong>: interfaz de 8 pines auto-desarrollada por Apple, se puede insertar por ambos lados. Usada en iPhone 14 y modelos anteriores, ahora completamente obsoleta.
- <strong>Limitaciones de transmisión</strong>: la interfaz Lightning físicamente solo soporta el estándar USB 2.0, velocidad máxima de 480Mbps. Incluso con cable USB-C a Lightning, la velocidad está limitada por la propia interfaz Lightning.
- <strong>Razón de obsolescencia</strong>: la UE aprobó una normativa que exige que desde 2024 todos los móviles unifiquen el uso de interfaz USB-C, Apple desde la serie iPhone 15 cambió completamente a Type-C. La interfaz Lightning sale oficialmente del escenario histórico.
- <strong>Nota</strong>: los cables certificados MFi de Apple contienen un chip de certificación, los cables no certificados pueden no cargar o transmitir datos correctamente. Si aún usas un iPhone antiguo, conviene tener cables Lightning a mano.

##### USB Type-C

- <strong>Características físicas</strong>: interfaz ovalada de 24 pines, se puede insertar por ambos lados. Se ha convertido en la interfaz estándar de móviles y la mayoría de dispositivos electrónicos. La UE ha legislado que desde 2024 todos los móviles, tablets, auriculares y otros dispositivos portátiles unifiquen el uso de interfaz USB-C, y otras regiones del mundo le siguen.
- <strong>Protocolo de transmisión</strong>: Type-C es solo la forma de la interfaz, la capacidad real de transmisión depende del protocolo interno. Soporta USB 2.0 (480Mbps), USB 3.0/3.1/3.2 (5-20Gbps) e incluso USB4 (40Gbps).
- <strong>Distinción importante</strong>: ¡No todos los puertos Type-C soportan USB 3.0! Muchos móviles usan el puerto Type-C, pero internamente solo conectan los pines de USB 2.0, por lo que la velocidad de transferencia es igual de lenta que con el puerto antiguo. Las versiones estándar del iPhone 16/17 solo soportan velocidad USB 2.0; las versiones Pro soportan USB 3.0 (necesita cable USB-C a USB-C).
- <strong>Capacidad de carga</strong>: soporta protocolos de carga rápida como USB PD, hasta 240W.
- <strong>Salida de video</strong>: soporta DisplayPort Alt Mode, puede salida de video a un monitor mediante cable adaptador.

##### Interfaz de audio de 3.5mm

- <strong>Características físicas</strong>: jack circular de 3 o 4 segmentos, el de 3 segmentos transmite audio de canal izquierdo/derecho, el de 4 segmentos añade un canal de micrófono.
- <strong>Características</strong>: transmisión de señal analógica, plug-and-play, sin necesidad de driver o conversión. Calidad de sonido estable, latencia cero.
- <strong>Situación actual</strong>: la mayoría de móviles insignia han eliminado el jack de 3.5mm, necesita cable adaptador Type-C o auriculares bluetooth. Algunos móviles de gama media y móviles gaming aún lo conservan.

#### 4. Sistema de productos del móvil y reglas de nomenclatura

Ante la deslumbrante gama de productos de cada marca, entender las reglas de nomenclatura te ayuda a localizar rápidamente el modelo adecuado.

##### Series de productos de marcas principales:

- <strong>Apple</strong>: iPhone (versión estándar) / iPhone Plus (pantalla grande) / iPhone Pro (versión profesional) / iPhone Pro Max (pantalla grande profesional) / iPhone SE (versión económica) / iPhone 16e (versión económica con IA, con chip A18 y módem C1 propio de Apple). En 2026, la serie iPhone 17 incorpora el chip A19 Pro en todos sus modelos, con capacidades de IA mejoradas.
- <strong>Huawei</strong>: serie Mate (insignia business) / serie P/Pura (insignia imagen) / serie Mate X (insignia plegable) / serie nova (gama media joven) / serie Enjoy (entrada)
- <strong>Xiaomi</strong>: serie numérica Xiaomi (insignia) / Xiaomi MIX (insignia exploración/plegable) / serie Redmi K (insignia rendimiento) / serie Redmi Note (gama media) / serie numérica Redmi (entrada)
- <strong>OPPO</strong>: serie Find X (insignia) / serie Reno (gama media) / serie A (entrada) / serie numérica OnePlus (insignia rendimiento)
- <strong>vivo</strong>: serie X (insignia imagen) / serie numérica iQOO (insignia rendimiento) / serie S (selfie gama media) / serie Y (entrada)
- <strong>Samsung</strong>: serie Galaxy S (insignia) / Galaxy Z Fold/Flip (insignia plegable) / serie Galaxy A (gama media)

##### Significado de sufijos comunes:

- <strong>Pro</strong>: abreviatura de Professional, versión profesional. Normalmente mejora cámara, pantalla, procesador y otras configuraciones clave sobre la versión estándar.
- <strong>Max</strong>: versión máxima. Pantalla más grande, batería más grande, pero la configuración no necesariamente supera a Pro.
- <strong>Ultra</strong>: versión extrema. Normalmente representa la configuración más alta de la serie, los mejores componentes, también el precio más alto. Como Samsung S24 Ultra, Xiaomi 14 Ultra.
- <strong>SE</strong>: Special Editíon, edición especial, en realidad suele ser versión económica. Configuración reducida, precio más bajo. Como iPhone SE.
- <strong>Plus</strong>: versión ampliada. Pantalla más grande que la estándar, batería también, pero configuración básicamente igual.
- <strong>Lite/Versión Youth</strong>: versión ligera. Configuración simplificada, precio más bajo.
- <strong>Note</strong>: originalmente se refería a móviles de pantalla grande, ahora cada marca lo usa diferente. Redmi Note es una serie de gama media.
- <strong>Neo</strong>: versión nueva. Normalmente se refiere a modelos de gama media orientados al rendimiento.

#### 5. Módem y antena: los héroes anónimos de la comunicación del móvil

El móvil puede llamar y conectarse gracias a la pareja del chip módem y la antena.

##### Chip módem:

El módem es el procesador responsable de la comunicación inalámbrica en el móvil, modula señales digitales en ondas de radio para emitir, y demodula las ondas de radio recibidas en señales digitales. El rendimiento del módem afecta directamente la calidad de llamada, la velocidad de conexión y la estabilidad de la señal. Qualcomm es el mayor proveedor de módems de móvil, MedíaTek y Samsung también tienen módems auto-desarrollados. Apple desde el iPhone 16e monta su chip módem C1 auto-desarrollado, marcando la entrada oficial de Apple en la era de módems auto-desarrollados, el módem C1 usa proceso de 4nm, excelente rendimiento de consumo; el iPhone 16/16 Plus/16 Pro/16 Pro Max aún usan módem Qualcomm (Snapdragon X75 5G), se espera que modelos posteriores transiciónen gradualmente a módems auto-desarrollados. Los iPhone XS/11 anteriores usaban módem Intel con rendimiento de señal deficiente, fue un dolor para muchos usuarios.

##### Diseño de antena:

Las antenas del móvil están escondidas dentro del cuerpo, normalmente dispuestas alrededor del marco. El diseño de la antena afecta directamente al rendimiento de recepción de señal:

- <strong>Tecnología MIMO</strong>: multiple-input multiple-output, usa múltiples antenas para enviar y recibir datos simultáneamente, mejora velocidad y estabilidad. 4×4 MIMO es más rápido que 2×2 MIMO.
- <strong>Número de antenas</strong>: los móviles insignia suelen tener más de una docena de antenas (celular, Wi-Fi, bluetooth, NFC, GPS cada uno necesita antena independiente).
- <strong>Impacto del cuerpo metálico</strong>: el metal apantalla la señal, por eso los móviles con cuerpo metálico necesitan bandas de antena (las tiras de plástico en el marco). Los cuerpos de cristal y plástico afectan menos a la señal.

##### Evolución de la tecnología de red:

- <strong>4G LTE</strong>: tasa pico teórica 1Gbps bajada/500Mbps subida (Cat.18), experiencia real normalmente 50-150Mbps. Cobertura más amplia, suficiente.
- <strong>5G NR</strong>: tasa pico teórica 10Gbps+ bajada. La banda Sub-6GHz tiene mejor cobertura, la onda milimétrica mmWave es muy rápida pero con cobertura muy pequeña.
- <strong>5G-A (5G Advanced)</strong>: La versión mejorada del 5G, también llamada 5.5G. La velocidad de bajada puede alcanzar 10 Gbps y la de subida 1 Gbps, con gran mejora en la densidad de conexiones y la precisión de posicionamiento. Desde 2024, China Mobile, China Telecom y China Unicom han comenzado a desplegar redes 5G-A en ciudades clave. Los buques insignia como la serie Huawei Mate 70/80 y la serie Xiaomi 15/16 ya soportan 5G-A. El 5G-A también aporta la capacidad de "integración de comunicación y percepción": las estaciones base pueden comunicarse y percibir el entorno simultáneamente, proporcionando infraestructura para la economía de baja altitud (entregas con drones) y la conectividad vehicular.

##### Clasificación de bandas de red:

Las bandas de red soportadas por el móvil determinan en qué países y redes de operadores puede usarse:

- <strong>FDD-LTE Band (serie B)</strong>: como B1, B3, B5, etc., bandas 4G. Diferentes países usan diferentes bandas, China usa principalmente B1/B3/B5/B8/B34/B38/B39/B40/B41.
- <strong>TDD-LTE Band</strong>: otro estándar de 4G, China usa mucho B38/B39/B40/B41.
- <strong>5G NR Band (serie N)</strong>: como n1, n3, n28, n41, n78, n79, etc. n78 (3.5GHz) es la banda principal de 5G en China, n41 (2.5GHz) la usa mucho Mobile.
- <strong>Consejo de compra</strong>: si necesitas usarlo en el extranjero, confirma antes de comprar si el móvil soporta las bandas del país de destino. Los móviles de versión china normalmente soportan mejor las bandas chinas, pero pueden faltar algunas bandas extranjeras.

#### 6. Tu móvil, ¿cuántos roles está desempeñando?

Hace tiempo que no es solo un teléfono:

1. <strong>Herramienta de comunicación</strong>: teléfono, SMS, WeChat, email...
2. <strong>Cámara inteligente</strong>: fotos, video, escanear documentos...
3. <strong>Billetera</strong>: pagos, tarjeta de transporte, tarjeta bancaria, tarjeta de miembro...
4. <strong>Portal de información</strong>: noticias, clima, bolsa, conocimiento...
5. <strong>Consola de juegos</strong>: desde match-3 hasta títulos AAA...
6. <strong>Oficina móvil</strong>: documentos, hojas de cálculo, reuniones, colaboración...
7. <strong>Asistente de salud</strong>: podómetro, ritmo cardíaco, sueño, ejercicio...
8. <strong>Control remoto de hogar inteligente</strong>: controlar luces, aire acondiciónado, TV, robot aspirador...
9. <strong>Identidad digital</strong>: documento de identidad electrónico, licencia de conducir electrónica, código de salud...
10. <strong>Centro de entretenimiento</strong>: música, video, libros electrónicos, podcasts...

Piénsalo, ¡un pequeño dispositivo cargando cuánta vida! Por eso, aprender a usarlo bien es aprender a vivir mejor.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Practica: conoce la configuración de hardware

{class="mt-1"}
En [Configuración], mira si puedes encontrar el modelo de procesador, el tamaño específico de la memoria (RAM) y del almacenamiento (ROM). Ten una idea de las capacidades de tu móvil. Los usuarios de Android pueden descargar "AnTuTu" o "DevCheck" para ver información detallada del hardware.
:::
