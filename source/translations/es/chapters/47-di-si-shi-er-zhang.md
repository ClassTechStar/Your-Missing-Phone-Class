---
id: di-si-shi-er-zhang
num: 42
part: ai-biancheng-pian
nav: Capítulo 42: Panorama de los grandes modelos y práctica con la API
toc: default
kind: chapter
---

### Capítulo 42: Panorama de los grandes modelos y práctica con la API

{class="chapter-intro mb-4"}
Los capítulos anteriores hablaban de «cómo colaborar con la IA»; este capítulo responde a una pregunta más básica: «¿qué IA usar y cómo?». El panorama de los grandes modelos de agosto de 2026 es riquísimo: a nivel internacional compiten los tres grandes, GPT, Claude y Gemini, mientras que en China florecen DeepSeek, Tongyi Qianwen, GLM, Kimi y Doubao. Cada modelo tiene su carácter y sus fortalezas: elegir bien te ahorra la mitad del esfuerzo; elegir mal te cuesta el doble. Este capítulo no solo te presenta estos modelos, sino que también te enseña a conectarlos a tus propias aplicaciones mediante la API y a elegir el Token Plan (plan de consumo) adecuado según tus necesidades.

#### 1. Los grandes modelos internacionales: un terreno de tres potencias

En el mercado internacional de grandes modelos de agosto de 2026 se ha consolidado un triángulo de potencias: OpenAI (serie GPT), Anthropic (serie Claude) y Google (serie Gemini). Cada una tiene un carácter muy marcado; vamos a conocerlas una por una.

##### 1. Serie GPT-5.6 de OpenAI: el todoterreno equilibrado

OpenAI fue quien inició la ola de los grandes modelos y la serie GPT sigue siendo la más usada del mundo. La serie GPT-5.6, lanzada en julio de 2026, adopta una estrategia de tres gamas: la insignia GPT-5.6 Sol para necesidades de razonamiento avanzado, la equilibrada GPT-5.6 Terra para el desarrollo diario y la ligera GPT-5.6 Luna para escenarios de alta concurrencia y bajo costo. Los tres modelos comparten una ventana de contexto de 1,05 millones de tokens y admiten entrada de imágenes, llamadas a funciones y salida estructurada.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Modelo</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Gama</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Entrada (/millón de tokens)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Salida (/millón de tokens)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ventana de contexto</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GPT-5.6 Sol</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Insignia, razonamiento</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">5,00 USD (≈36 CNY)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">30,00 USD (≈217 CNY)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1,05 M de tokens</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GPT-5.6 Terra</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Equilibrada, diaria</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2,50 USD (≈18 CNY)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">15,00 USD (≈109 CNY)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1,05 M de tokens</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GPT-5.6 Luna</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ligera, bajo costo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1,00 USD (≈7 CNY)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">6,00 USD (≈44 CNY)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1,05 M de tokens</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Precios de la serie GPT-5.6 de OpenAI (agosto de 2026)

La ventaja central de la serie GPT es su «equilibrio»: razonamiento, programación, redacción y multimodalidad, sin debilidades evidentes. Suma además el enorme ecosistema de complementos y la comunidad de desarrolladores de OpenAI, con la documentación y las cadenas de herramientas más completas. Para los casos de «no sé qué elegir», GPT es la respuesta por defecto que «no falla ni con los ojos cerrados». Sus puntos débiles: desde China se necesita red especial para acceder, su chino suena a veces «traducido» y su precio de API es de nivel medio-alto.

::: div .success-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Buenas noticias

{class="mt-1"}
En agosto de 2026, OpenAI anunció que el modelo por defecto de los usuarios gratuitos pasa a ser GPT-5.6 Luna, con chat de texto ilimitado. Esto significa que puedes probar las capacidades básicas de GPT a costo cero y solo pagar cuando necesites más razonamiento o llames a la API.
:::

##### 2. Serie Claude de Anthropic: la cima de la programación y el rigor

Si GPT es el todoterreno, Claude es la «cima» del ámbito de la programación. La serie Claude de Anthropic lidera con ventaja sostenida en SWE-bench (el benchmark de ingeniería de software), con la mejor calidad de generación de código y la mayor capacidad de aterrizar proyectos a nivel de ingeniería del sector. Más destacable aún: Claude tiene la tasa de alucinaciones (probabilidad de generar información falsa) más baja de todos los modelos, de apenas un 1 %, lo que lo hace especialmente apto para escenarios de alta precisión como la academia o lo jurídico.

El otro as en la manga de Claude es su contexto ultra largo: admite una ventana de contexto de 1 millón de tokens y puede «leer» de una sola vez cientos de páginas de contrato o un repositorio de código entero sin perder detalle. En escenarios como la refactorización de código o el análisis de documentos largos es prácticamente insustituible. Claude Code, como herramienta de programación con IA en terminal, alcanzó a mediados de 2026 unos ingresos anualizados de 2.500 millones de dólares: la mayor prueba del reconocimiento a la capacidad de programación de Claude.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Modelo</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Gama</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Entrada (/millón de tokens)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Salida (/millón de tokens)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ventana de contexto</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Fable 5</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Insignia</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">10,00 USD (≈72 CNY)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">50,00 USD (≈362 CNY)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1 M de tokens</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Opus 4.8</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Profesional</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">5,00 USD (≈36 CNY)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">25,00 USD (≈181 CNY)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1 M de tokens</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Sonnet 5</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Económica</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2,00 USD (≈14 CNY)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">10,00 USD (≈72 CNY)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1 M de tokens</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Precios de la serie Claude de Anthropic (agosto de 2026; Sonnet 5 a precio promocional)

El punto débil de Claude es el precio: la salida de Fable 5 es la más cara de todos los modelos, 50 dólares por millón de tokens. Su capacidad multimodal (comprensión de imágenes y vídeo) también es relativamente débil. Para desarrolladores individuales con presupuesto limitado, Sonnet 5 ofrece una relación calidad-precio muy destacada durante el periodo promocional.

##### 3. Serie Gemini de Google: el rey de la multimodalidad

La serie Gemini de Google llegó en 2026 a la versión 3.1 Pro. Su mayor as es la multimodalidad nativa: análisis preciso de texto e imágenes, reconocimiento de tablas por OCR sin errores, extracción eficiente de fotogramas de vídeo y análisis profundo de audio y vídeo. Está profundamente integrado con el ecosistema de Google (búsqueda, correo, servicios en la nube) y destaca en la recuperación de información en tiempo real y la comprensión entre modalidades. Además admite una entrada de contexto ultra largo de 2 millones de tokens: la ventana de contexto más grande de los modelos actuales.

Gemini se posiciona como «la primera opción para razonamiento científico y escenarios multimodales». Si tu proyecto implica mucho análisis de imágenes, comprensión de vídeo o cálculo científico, Gemini casi no tiene rival. Pero en la generación de código de texto puro queda algo por detrás de Claude, y su chino tampoco resulta tan natural como el de los modelos chinos.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Aspecto</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">GPT-5.6</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Claude Fable 5</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Gemini 3.1 Pro</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Puntuación global</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">94.8</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">95.0</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">92.1</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Programación (SWE-bench)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">74.9%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">64.3% (Pro)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Media</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ventana de contexto</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1,05 M de tokens</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1 M de tokens</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2 M de tokens</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Capacidad multimodal</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Equilibrada</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Débil</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">La más fuerte</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tasa de alucinaciones</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Baja</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">La más baja (≈1 %)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Baja</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Disponibilidad desde China</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Requiere red especial</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Requiere red especial</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Requiere red especial</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ecosistema de API</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">El más completo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">En crecimiento</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ligado al ecosistema de Google</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Comparativa de los tres grandes modelos internacionales (agosto de 2026)

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Ojo: el obstáculo real para usarlos desde China

{class="mt-1"}
Para los desarrolladores en China, el obstáculo principal de GPT, Claude y Gemini es el acceso por red. Aunque se pueden usar de forma indirecta mediante proxies de Azure, plataformas agregadoras de API y otros medios, la estabilidad y el cumplimiento normativo deben evaluarse por tu cuenta. Si tu proyecto tiene requisitos estrictos de seguridad de datos, conviene priorizar los modelos chinos.
:::

#### 2. Los grandes modelos chinos: cien flores en flor

En 2026 los grandes modelos chinos han pasado de «perseguidores» a «corredores en paralelo», e incluso a «líderes» en algunos campos. A diferencia de la polémica de 2023 sobre los «envoltorios», los modelos insignia chinos de 2026 ya están a la altura de los modelos internacionales de primera línea en razonamiento lógico, generación de código y comprensión del chino, con una brecha reducida a menos del 5 %. Más importante aún: los modelos chinos tienen ventajas insustituibles en escenarios en chino, costos y despliegue conforme a la normativa.

##### 1. DeepSeek V4: el rey de la relación calidad-precio

DeepSeek es un fenómeno entre los grandes modelos chinos. A principios de 2025, DeepSeek-V3 sacudió el mercado con su posicionamiento de «una décima parte del precio de GPT y la misma capacidad», y el sector la llamó «la línea de matanza de los grandes modelos de IA de propósito general»: no hay nada más barato que funcione tan bien, ni nada más caro que dé tanta potencia y cantidad. En agosto de 2026 se lanzó la versión oficial de DeepSeek V4-Pro: arquitectura MoE de 1,6 billones de parámetros con unos 49B activados, contexto sin pérdida de 1 millón de tokens y una relación calidad-precio en código considerada ampliamente como la mejor del mundo.

DeepSeek V4 dio un gran salto en capacidades de agente: el benchmark DeepSWE pasó de 12,8 a 62,7 (+390 %) y NL2Repo subió de 38,5 a 61,5. Su API añadió soporte de doble protocolo (Responses API y Anthropic API) y ya es compatible con herramientas de programación populares como Codex y Claude Code. Esto significa que puedes sustituir la API de Claude por la de DeepSeek dentro de Claude Code: el costo baja varias veces y la experiencia es casi idéntica.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Modelo</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Gama</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Entrada (/millón de tokens)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Salida (/millón de tokens)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ventana de contexto</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DeepSeek V4 Pro</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Insignia, razonamiento</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3 CNY (≈0,43 USD)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">6 CNY (≈0,87 USD)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1 M de tokens</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DeepSeek V4 Flash</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ligera, rápida</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1 CNY (≈0,14 USD)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2 CNY (≈0,28 USD)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1 M de tokens</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Precios de la serie DeepSeek V4 (agosto de 2026, precios promocionales)

Comparación de precios: con el mismo 1 millón de tokens de entrada + 1 millón de salida, DeepSeek V4 Flash cuesta unos 0,42 dólares, GPT-5.6 Sol unos 35 dólares y Claude Fable 5 unos 60 dólares. Una brecha de hasta 80-140 veces.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Aviso para evitar sorpresas: DeepSeek va a subir precios

{class="mt-1"}
DeepSeek anunció oficialmente el 6 de agosto de 2026 que «planea subir de forma sustancial el precio de su API en breve», así que los precios promocionales pueden no durar mucho. Algunos medios rumoraron que el aumento podría llegar a 30 veces, y hasta el 14 de agosto la empresa no había publicado el plan de precios definitivo. Además, la versión oficial de DeepSeek V4 introduce un esquema de precios por horas valle y pico: en horas pico, la llamada cuesta el doble. Consulta los anuncios oficiales para conocer los precios más recientes.
:::

##### 2. Tongyi Qianwen Qwen3.7 Max: la opción empresarial de Alibaba Cloud

La serie Tongyi Qianwen (Qwen) de Alibaba Cloud se apoya en su ecosistema y tiene ventajas naturales en el despliegue empresarial. El Qwen3.7 Max de julio de 2026 es la insignia actual: un modelo denso de 235B de parámetros, con contexto nativo de 256K ampliable a 1M. Las ventajas centrales de Qwen: un ecosistema de código abierto maduro (toda la serie, de 7B a 235B, es abierta), una comprensión precisa de los escenarios en chino y una integración profunda con la infraestructura de Alibaba Cloud.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Modelo</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Precio de salida (/millón de tokens)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Casos de uso</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">qwen-turbo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">0,6 CNY</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Preguntas y respuestas simples, clasificación de texto, alta concurrencia</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">qwen-long</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2,0 CNY</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Procesamiento de contexto ultra largo de 10M</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">qwen3.7-flash</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">7,2 CNY</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Conversación general, generación de contenido</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">qwen3.7-plus</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">12,0 CNY</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Multimodal (imágenes + vídeo), creación en chino</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">qwen3.7-max</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">36,0 CNY</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Capacidad insignia en chino, tareas complejas</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Precios escalonados de la serie Qwen de Tongyi Qianwen (agosto de 2026)

Qwen fija sus precios por tramos: desde el ultrabarato qwen-turbo (salida a 0,6 CNY por millón de tokens) hasta la insignia qwen3.7-max (salida a 36 CNY por millón de tokens), cubriendo todo el abanico, de las preguntas ligeras al razonamiento complejo. Para las empresas que ya usan Alibaba Cloud, Qwen es la opción de integración más cómoda.

##### 3. GLM-5.1 de Zhipu: número 1 chino en SWE-bench

La serie GLM de Zhipu AI brilló en 2026. GLM-5.1 logró el primer puesto entre los modelos chinos en SWE-bench: arquitectura híbrida MoE-densa de 744B con soporte de 1 millón de tokens de contexto. Se caracteriza por una comprensión semántica del chino muy precisa y por admitir el despliegue privado conforme a la normativa china, algo crucial para escenarios como las finanzas y la administración pública, con requisitos estrictos de seguridad de datos. GLM-5.1 se ofrece a 6 CNY de entrada y 24 CNY de salida por millón de tokens, un nivel intermedio entre los modelos chinos.

##### 4. Kimi K3: el rey del texto ultra largo

La serie Kimi de Moonshot AI es famosa por procesar textos ultra largos. Kimi K3, lanzado en julio de 2026, alcanza los 2,8 billones de parámetros y entra en la élite mundial en varias evaluaciones de tareas complejas. El terreno natural de Kimi es el análisis de bases de código grandes y la generación aumentada por recuperación de documentos largos: puede procesar el texto de un libro entero o el código de un proyecto completo, y destaca en las tareas de búsqueda de «agujas en un pajar». Su precio es relativamente alto (salida de unos 12-20 CNY por millón de tokens), pero su relación calidad-precio en textos largos no tiene competencia.

##### 5. Doubao: el todoterreno de ByteDance

La serie Doubao de ByteDance se mantuvo estable en 2026. Doubao Seed 2.1 Pro es el modelo insignia de Volcengine, con contexto de 256K, un rendimiento general estable en pruebas reales y una experiencia destacada en chino. Las ventajas de Doubao: regala una gran cantidad de tokens gratis al registrarte, se integra muy bien en el ecosistema de Volcengine y su precio está entre los más bajos de China. Para principiantes que quieran probar rápido la programación con IA, Doubao es una puerta de entrada sin barreras.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Aspecto</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">DeepSeek V4</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Qwen3.7 Max</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">GLM-5.1</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Kimi K3</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Doubao 2.1 Pro</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Puntuación global</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">87.5</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">89.7</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">90.5</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">88+</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">85+</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Programación</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Altísima</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Fuerte</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">N.º 1 chino en SWE</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Fuerte</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Media-alta</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Comprensión del chino</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Excelente</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Excelente</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Precisa</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Excelente</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Excelente</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ventana de contexto</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1 M</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">256K-1M</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1 M</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ultra larga</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">256K</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Precio de salida (CNY/M)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">6</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">36</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">24</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">12-20</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">30</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Código abierto</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Licencia MIT</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Toda la serie abierta</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Parcialmente abierto</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cerrado</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cerrado</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Despliegue privado</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sí</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sí</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sí</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">No</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">No</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Comparativa de los cinco grandes modelos chinos (agosto de 2026)

Una tendencia importante: ya desapareció la sensación de «generación de diferencia» entre los modelos chinos y GPT/Claude. En razonamiento lógico y competiciones matemáticas, la diferencia entre los insignia chinos y GPT-5 es de apenas un dígito. En pensamiento arquitectónico sistémico y razonamiento de ingeniería compleja, Claude sigue adelante: propone soluciones de arquitectura con más «chispa», mientras que los modelos chinos a veces resultan «doctrinarios». Pero en escenarios en chino, control de costos y despliegue conforme a la normativa, los modelos chinos tienen una ventaja arrolladora.

::: div .figure
```html
<svg style="max-width:100%;height:auto" width="620" height="290" viewBox="0 0 620 290" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="620" height="290" fill="#ffffff" rx="8"/>
      <line x1="70" y1="230" x2="590" y2="230" stroke="#9ca3af" stroke-width="1.5"/>
      <line x1="70" y1="230" x2="70" y2="20" stroke="#9ca3af" stroke-width="1.5"/>
      <line x1="70" y1="60" x2="590" y2="60" stroke="#e5e7eb" stroke-width="1" stroke-dasharray="4,4"/>
      <line x1="70" y1="116" x2="590" y2="116" stroke="#e5e7eb" stroke-width="1" stroke-dasharray="4,4"/>
      <line x1="70" y1="173" x2="590" y2="173" stroke="#e5e7eb" stroke-width="1" stroke-dasharray="4,4"/>
      <text x="62" y="234" font-size="10" fill="#6b7280" text-anchor="end">0</text>
      <text x="62" y="120" font-size="10" fill="#6b7280" text-anchor="end">50</text>
      <text x="62" y="64" font-size="10" fill="#6b7280" text-anchor="end">100</text>
      <text x="340" y="262" font-size="10.5" fill="#374151" text-anchor="middle">Precio de salida (yuan/millón de tokens)</text>
      <!-- bars: price -->
      <rect x="95" y="218" width="60" height="12" fill="#4f46e5"/><text x="125" y="212" font-size="9" fill="#374151" text-anchor="middle">6</text><text x="125" y="248" font-size="9.5" fill="#374151" text-anchor="middle">DeepSeek</text>
      <rect x="195" y="146" width="60" height="84" fill="#4f46e5"/><text x="225" y="140" font-size="9" fill="#374151" text-anchor="middle">36</text><text x="225" y="248" font-size="9.5" fill="#374151" text-anchor="middle">Qwen</text>
      <rect x="295" y="182" width="60" height="48" fill="#4f46e5"/><text x="325" y="176" font-size="9" fill="#374151" text-anchor="middle">24</text><text x="325" y="248" font-size="9.5" fill="#374151" text-anchor="middle">GLM</text>
      <rect x="395" y="200" width="60" height="30" fill="#4f46e5"/><text x="425" y="194" font-size="9" fill="#374151" text-anchor="middle">16</text><text x="425" y="248" font-size="9.5" fill="#374151" text-anchor="middle">Kimi</text>
      <rect x="495" y="170" width="60" height="60" fill="#4f46e5"/><text x="525" y="164" font-size="9" fill="#374151" text-anchor="middle">30</text><text x="525" y="248" font-size="9.5" fill="#374151" text-anchor="middle">Doubao</text>
      <!-- scores -->
      <circle cx="125" cy="118" r="5" fill="#d4a017"/><text x="140" y="114" font-size="9" fill="#78350f">87.5</text>
      <circle cx="225" cy="110" r="5" fill="#d4a017"/><text x="240" y="106" font-size="9" fill="#78350f">89.7</text>
      <circle cx="325" cy="105" r="5" fill="#d4a017"/><text x="340" y="101" font-size="9" fill="#78350f">90.5</text>
      <circle cx="425" cy="112" r="5" fill="#d4a017"/><text x="440" y="108" font-size="9" fill="#78350f">88+</text>
      <circle cx="525" cy="116" r="5" fill="#d4a017"/><text x="540" y="112" font-size="9" fill="#78350f">85+</text>
      <rect x="90" y="30" width="12" height="12" fill="#4f46e5"/><text x="108" y="41" font-size="9.5" fill="#374151">Precio de salida (menor es mejor)</text>
      <circle cx="170" cy="36" r="5" fill="#d4a017"/><text x="182" y="40" font-size="9.5" fill="#374151">Puntuación global (mayor es mejor)</text>
    </svg>
```

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figura 4: comparación de precio y rendimiento de los cinco modelos (mejor cuanto más bajo el precio y más alta la puntuación)
:::

#### 3. Marco de decisión para elegir modelo

Ya que conoces las particularidades de cada modelo, ¿cómo elegir uno para tu proyecto? Aquí tienes el «método de decisión de cuatro preguntas»: responde cuatro preguntas y darás con el modelo que mejor te conviene.

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-globe mr-1"></i> ¿Tu proyecto se despliega en China o a nivel internacional?</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">En China → elige modelos nacionales</span><span class="text-gray-400 mx-1">│</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">Internacional → modelos extranjeros como opción</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-laptop-code mr-1"></i> ¿La tarea principal es programar u otra cosa?</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">Programación → Claude o DeepSeek</span><span class="text-gray-400 mx-1">│</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center">Otra cosa → sigue evaluando</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-book mr-1"></i> ¿Necesitas un contexto muy largo (&gt;500 000 tokens)?</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">Sí → Gemini o Kimi</span><span class="text-gray-400 mx-1">│</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center">No hace falta → sigue evaluando</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-coins mr-1"></i> ¿Presupuesto ajustado?</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">Ajustado → DeepSeek o Qwen-turbo</span><span class="text-gray-400 mx-1">│</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">No tanto → GPT-5.6 o Claude</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figura 5: método de decisión de cuatro preguntas para elegir un gran modelo
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Consejo: estrategia de combinación

{class="mt-1"}
Este método de decisión no es un dogma: muchos escenarios requieren combinar varios modelos. Una estrategia común: DeepSeek o Qwen para el desarrollo diario (baratos y buenos en chino), Claude para el diseño de arquitecturas clave (razonamiento fuerte y pocas alucinaciones) y Gemini para el análisis multimodal (procesamiento de imágenes y vídeo). Cambia de modelo según lo que necesites, en vez de «usar uno hasta el final de los tiempos».
:::

#### 4. Primeros pasos con la API: integrar un gran modelo desde cero

Muchos tutoriales de programación con IA solo enseñan a usar la interfaz de chat, pero la verdadera «programación con IA» —hacer que tu aplicación llame a un gran modelo— pasa por la API. La API (Application Programming Interface, interfaz de programación de aplicaciones) es el protocolo de comunicación entre programas. Con la API, tu código puede invocar la capacidad de un gran modelo igual que llama a una función.

##### 1. Qué es un token

Antes de entender la API hay que comprender el concepto de «token». El token es la unidad básica de facturación de los grandes modelos; puedes verlo como la «unidad de lectura y escritura de la IA». Un token equivale aproximadamente a 0,75 palabras en inglés (4 caracteres) y a entre 0,5 y 1 carácter chino. Un texto chino de 1000 caracteres consume unos 1500-2000 tokens.

Un token no es una palabra ni un carácter. Los grandes modelos usan un tokenizador especializado para dividir el texto en tokens. La misma palabra puede ocupar un número distinto de tokens en cada modelo: por ejemplo, «inteligencia artificial» puede ser 3 tokens en GPT y 2 en DeepSeek. La API de la mayoría de los modelos devuelve el número real de tokens consumidos, y puedes consultarlo en la respuesta.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Estimación rápida del costo en tokens

{class="mt-1"}
1 millón de caracteres chinos equivalen a unos 1,5 millones de tokens. Procesar 1 millón de caracteres de entrada + 1 millón de salida con DeepSeek V4 Flash cuesta unos 0,42 dólares (unos 3 CNY); con Claude Fable 5, la misma cantidad cuesta unos 60 dólares (unos 434 CNY). Por eso la elección del modelo afecta directamente al costo de tu proyecto.
:::

##### 2. Obtener una API Key

El primer paso para usar la API de un gran modelo es obtener una API Key, una clave usada para autenticarte. Cada proveedor de modelos tiene su propia plataforma de API, donde debes registrarte y crear la API Key. Estas son las plataformas de API de los modelos principales, con su proceso de obtención:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Modelo</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Plataforma de API</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Proceso de obtención</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Cuota gratuita</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DeepSeek</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">platform.deepseek.com</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Registro → verificación de identidad → crear API Key</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cuota de regalo para nuevos usuarios</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tongyi Qianwen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">bailian.aliyun.com (plataforma Bailian)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Iniciar sesión con cuenta de Alibaba Cloud → activar el servicio → crear la Key</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Prueba gratuita para nuevos usuarios</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Zhipu GLM</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">open.bigmodel.cn</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Registro → verificación de identidad → crear API Key</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cuota de regalo para nuevos usuarios</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kimi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">platform.moonshot.cn</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Registro → verificación de identidad → crear API Key</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cuota gratuita limitada</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Doubao</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">volcengine.com (Volcengine)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Registro → activar Ark → crear API Key</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Regala muchos tokens al registrarte</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OpenAI GPT</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">platform.openai.com</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Registro → vincular tarjeta de crédito → crear API Key</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sin cuota gratuita (de pago)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Anthropic Claude</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">console.anthropic.com</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Registro → vincular tarjeta → crear API Key</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cuota pequeña para nuevos usuarios</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Plataformas de API de los modelos principales y cómo obtener la Key (agosto de 2026)

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Aviso de seguridad: la API Key es como la contraseña de tu monedero

{class="mt-1"}
La API Key equivale a la contraseña de tu monedero: cualquiera que la consiga puede usar tu cuota para llamar al modelo. Por eso: nunca escribas la API Key en el código (gestiónala con variables de entorno); nunca subas a un repositorio Git público código que contenga la Key; nunca compartas en redes sociales capturas donde aparezca. Si la Key se filtra, bórrala de inmediato en la plataforma y crea una nueva.
:::

##### 3. Tu primera llamada a la API

Con la API Key en mano, puedes llamar a la API de un gran modelo con cualquier lenguaje de programación. Aquí tienes, con Python, la llamada más simple posible: enviar un mensaje a DeepSeek y recibir su respuesta.

::: div .code-block
:::inline div .code-head
<span>PYTHON · Primera llamada a la API</span><span class="dots">···</span>
:::

```
# Instala el SDK: pip install openai
# DeepSeek es compatible con el SDK de OpenAI, se puede usar directamente
from openai import OpenAI
import os

# 1. crear el cliente (la API Key se lee de la variable de entorno)
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

# 2. enviar la petición
response = client.chat.completions.create(
    model="deepseek-chat",  # indica el modelo
    messages=[
        {"role": "system", "content": "Eres un asistente de programación en Python."},
        {"role": "user", "content": "Escribe una función de ordenación rápida."}
    ]
)

# 3. obtener la respuesta
print(response.choices[0].message.content)

# 4. ver el consumo de tokens
print(f"Tokens de entrada: {response.usage.prompt_tokens}")
print(f"Tokens de salida: {response.usage.completion_tokens}")
print(f"Tokens totales: {response.usage.total_tokens}")
```
:::

La lógica central de este código es: crear el cliente (con la API Key y la dirección del modelo) → construir la lista de mensajes (system define el rol, user es la entrada del usuario) → enviar la petición → recibir la respuesta. Este patrón sirve para casi todos los modelos compatibles con el formato de OpenAI: basta con cambiar api_key y base_url para cambiar de modelo. Por eso muchos modelos chinos eligen ser compatibles con el SDK de OpenAI: el desarrollador solo cambia dos líneas de código para cambiar de modelo, con un costo de migración mínimo.

Estas son las diferencias de código para cambiar a otros modelos; fíjate en que solo hay que cambiar dos líneas:

::: div .code-block
:::inline div .code-head
<span>PYTHON · Cambiar de modelo solo exige dos líneas</span><span class="dots">···</span>
:::

```
# DeepSeek
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)
# model="deepseek-chat"

# Qwen (plataforma Bailian)
client = OpenAI(
    api_key=os.environ.get("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)
# model="qwen-plus"

# GLM de Zhipu
client = OpenAI(
    api_key=os.environ.get("GLM_API_KEY"),
    base_url="https://open.bigmodel.cn/api/paas/v4"
)
# model="glm-4"

# OpenAI GPT
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    # con el base_url por defecto basta
)
# model="gpt-5.6-terra"
```
:::

##### 4. Respuestas en streaming

En aplicaciones reales, normalmente no querrás esperar a que la IA termine de escribir todo para mostrarlo de una vez; harías esperar demasiado al usuario. Las respuestas en streaming te permiten mostrar el texto palabra por palabra mientras la IA lo genera, lo que mejora muchísimo la experiencia. Es como una máquina de escribir: las palabras van apareciendo una a una, y para el usuario la sensación es completamente distinta.

::: div .code-block
:::inline div .code-head
<span>PYTHON · Respuesta en streaming</span><span class="dots">···</span>
:::

```
# Respuesta en streaming: sale palabra a palabra
stream = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "user", "content": "Escribe un tutorial del algoritmo de burbuja en Python"}
    ],
    stream=True  # activa el streaming
)

# recibe e imprime por bloques
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="", flush=True)
# la salida aparecerá letra a letra, como una máquina de escribir
```
:::

#### 5. Guía para comprar un Token Plan

La mayoría de los proveedores de modelos ofrece dos formas de facturación: pago por consumo (Pay-as-you-go) y suscripción de plan (Token Plan / Subscription). Entender la diferencia entre ambas puede reducir mucho tu costo de uso.

##### 1. Pago por consumo frente a suscripción

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Dimensión</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Pago por consumo (Pay-as-you-go)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Suscripción (Subscription)</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Forma de facturación</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pagas por los tokens que usas</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pago anticipado fijo a cambio de una cuota</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Casos ideales</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Consumo variable, llamadas ocasionales</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Consumo estable, llamadas frecuentes</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ventaja de precio</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Precio estándar</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">De un 20 % a un 50 % más barato</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Flexibilidad</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Disponible en cualquier momento, sin compromiso</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Requiere pago por adelantado; la cuota puede caducar</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Si superas la cuota</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Facturación automática por consumo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Al agotar la cuota, pasa a pago por consumo</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Plataformas representativas</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Plataformas de API oficiales de cada modelo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OpenAI Plus/Pro, Claude Pro, Cursor Pro</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Comparación de las dos formas de facturación

Para principiantes, conviene empezar con el pago por consumo: sin pagos anticipados, pagas por lo que usas. Cuando tu consumo mensual se estabilice (por ejemplo, por encima de 50 CNY al mes), considera pasarte a una suscripción para conseguir un precio unitario más bajo.

##### 2. Un vistazo a las suscripciones más populares

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Plan</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Cuota mensual</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Qué incluye</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">A quién va dirigido</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ChatGPT Free</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gratis</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Chat de texto ilimitado con GPT-5.6 Luna</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Para empezar desde cero</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ChatGPT Plus</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">20 USD/mes</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GPT-5.6 Sol, generación de imágenes, análisis de datos, acceso a complementos</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Usuarios de uso moderado</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ChatGPT Pro</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">200 USD/mes</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Uso ilimitado de todos los modelos, acceso prioritario a las novedades</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Profesionales de uso intensivo</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Free</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gratis</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Conversaciones con Claude limitadas</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Para empezar desde cero</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Pro</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">20 USD/mes</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Uso ilimitado de Claude, acceso prioritario a modelos nuevos</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Desarrolladores</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cursor Free</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gratis</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Autocompletado y chat con IA limitados</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Prueba para principiantes</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cursor Pro</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">20 USD/mes</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Autocompletado con IA ilimitado, 500 peticiones avanzadas al mes</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Desarrolladores habituales</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cursor Business</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">40 USD/mes por persona</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Colaboración en equipo, panel de administración, modo privacidad</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Equipos</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Planes de suscripción de las principales herramientas de IA (agosto de 2026)

Los planes de suscripción de los modelos chinos son algo distintos. DeepSeek factura principalmente por consumo y no tiene suscripción mensual: recargas saldo y se descuenta según tu uso real. Tongyi Qianwen ofrece paquetes prepagados en la plataforma Bailian (compras una cantidad de tokens a precio con descuento). Doubao tiene esquemas prepagados similares en Volcengine. Para los desarrolladores en China, la combinación más económica suele ser: DeepSeek por consumo (desarrollo diario) + la cuota gratuita de Doubao (pruebas y experimentos).

##### 3. Plataformas agregadoras de API

Si necesitas usar varios modelos a la vez, una plataforma agregadora de API es una opción muy cómoda. Con una única API Key común puedes llamar a decenas de modelos de todo el mundo sin registrarte en cada plataforma.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Plataforma</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Características</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ventaja de precio</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Casos ideales</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OpenRouter (openrouter.ai)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Plataforma agregadora internacional: una Key para llamar a modelos de todo el mundo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Precios transparentes, con comparación en tiempo real</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Quien necesite alternar con flexibilidad entre varios modelos internacionales</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SiliconFlow (siliconflow.cn)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Plataforma agregadora china con API de varios modelos chinos</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">De un 20 % a un 30 % más barata que la oficial</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Desarrolladores en China que comparan precios entre modelos</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Azure OpenAI (proxy de Microsoft)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">API de OpenAI vía el proxy de Microsoft Azure</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Batch API con 50% de descuento</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Llamadas a OpenAI de nivel empresarial, tareas asíncronas en grandes lotes</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Baidu Qianfan (qianfan.baidubce.com)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Plataforma de IA en la nube de Baidu, con modelos como Wenxin (ERNIE)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Crédito de regalo para nuevos usuarios</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Usuarios del ecosistema de Baidu</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Principales plataformas agregadoras de API (agosto de 2026)

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Aviso antitrampas: no compres "keys compartidas"

{class="mt-1"}
No compres las llamadas "API keys compartidas" en plataformas como Taobao o Xianyu: esas keys suelen venir de origen desconocido, pueden bloquearse en cualquier momento y suponen riesgo de fuga de datos. Consigue siempre tu API key a través de plataformas oficiales o agregadores serios.
:::

##### 4. Estrategias de optimización de costes

Elegir bien el modelo es solo el primer paso; saber "usarlo de forma ahorrativa" es igual de importante. Estas son varias estrategias de optimización de costes probadas en la práctica:

1. Aprovecha los aciertos de caché. Muchos modelos ofrecen una función de "caché": cuando tu petición incluye contenido ya procesado antes (como el prompt del sistema), esa parte se cobra a un precio bajísimo. En DeepSeek, un acierto de caché cuesta solo 1/60 del precio normal. Colocar el prompt fijo del sistema al principio de la lista de mensajes maximiza los aciertos de caché.
2. Enrutamiento por niveles: usa modelos baratos para tareas simples y modelos caros para tareas complejas. Por ejemplo, usa DeepSeek V4 Flash para clasificar texto (salida a 2 yuanes por millón de tokens) y Claude para diseñar la arquitectura (salida a 181 yuanes por millón de tokens). En un proyecto, el 80% de las llamadas puede usar el modelo barato.
3. Limita la longitud de la salida. La API cobra por los tokens de salida: cuanto más larga, más cara. En los escenarios donde no necesitas discursos largos, usa el parámetro max_tokens para limitar la longitud y evitar que la IA "se enrolle".
4. Usa la Batch API para tareas que no sean en tiempo real. Si tienes muchas tareas que no requieren respuesta inmediata (como el etiquetado masivo de datos o los resúmenes de documentos), la Batch API te da un 50% de descuento. OpenAI y Azure ofrecen esta función.
5. Vigila el consumo de tokens. Casi todas las plataformas de API incluyen un panel de estadísticas de uso. Revisa con regularidad cómo se reparte el consumo, localiza las llamadas que más tokens gastan y optimízalas específicamente. Un pequeño ajuste del prompt (por ejemplo, cambiar "explícalo con detalle" por "explícalo en 3 frases") puede ahorrar un 50% de tokens.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Estrategia de optimización</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ahorro</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Dificultad de implantación</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Descripción</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Acierto de caché</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Hasta un 98%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bajo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pon el contenido fijo al principio de los mensajes</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Enrutamiento por niveles</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">50%-80%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Medio</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Modelos baratos para tareas simples</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Limita la longitud de la salida</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">30%-60%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bajo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Configura el parámetro max_tokens</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Batch API</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">50%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bajo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Procesamiento por lotes para tareas no en tiempo real</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Optimización del prompt</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">20%-50%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Medio</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Simplifica el prompt y reduce redundancias</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Estrategias de optimización de costes y su efecto (agosto de 2026)

#### VI. Práctica: conectar la API de un gran modelo en tu proyecto

Cerramos el capítulo con un ejercicio práctico completo: crear un "generador de resúmenes con IA": el usuario introduce un texto largo y se llama a la API de un gran modelo para generar un resumen. Esta práctica muestra el flujo completo de una llamada a la API: configuración del entorno, llamada, gestión de errores y control de costes.

::: div .code-block
:::inline div .code-head
<span>PYTHON · ai_summarizer.py</span><span class="dots">···</span>
:::

```
# ai_summarizer.py - generador de resúmenes con IA
import os
from openai import OpenAI

# 1. Configuración (la API Key se lee de la variable de entorno, nunca se escribe en el código)
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

def summarize(text: str, max_length: int = 200) -> dict:
    """Genera un resumen del texto

    Args:
        text: texto original a resumir
        max_length: longitud máxima del resumen (en tokens)

    Returns:
        dict: incluye el resumen y los datos de consumo de tokens
    """
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {
                    "role": "system",
                    "content": "Eres un generador de resúmenes."
                               "Resume el texto del usuario en un lenguaje claro y conciso."
                               "El resumen no supera las 3 frases."
                },
                {
                    "role": "user",
                    "content": f"Resume el siguiente texto:\n\n{text}"
                }
            ],
            max_tokens=max_length,  # limita la longitud de la salida
            temperature=0.3  # temperatura baja = más estable
        )

        return {
            "success": True,
            "summary": response.choices[0].message.content,
            "input_tokens": response.usage.prompt_tokens,
            "output_tokens": response.usage.completion_tokens,
            "total_tokens": response.usage.total_tokens
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

# 2. ejemplo de uso
if __name__ == "__main__":
    long_text = """
    (pega aquí un texto largo...)
    """

    result = summarize(long_text)

    if result["success"]:
        print(f"Resumen: {result['summary']}")
        print(f"Tokens consumidos: {result['total_tokens']}")
        # Coste estimado: DeepSeek V4 Flash
        cost = result['total_tokens'] * 0.000004  # ≈ 0,4 centavos por 1000 tokens
        print(f"Coste estimado: {cost:.4f} yuan")
    else:
        print(f"Error: {result['error']}")
```
:::

Este código refleja varias buenas prácticas de las llamadas a la API: la API key se lee de una variable de entorno y nunca va escrita en el código; la función tiene documentación clara y anotaciones de tipos; se establece un max_tokens para limitar la longitud de la salida; temperature se fija en un valor bajo (0.3) para obtener salidas más estables; hay una gestión de errores completa; y se devuelve la información del consumo de tokens para hacer seguimiento de los costes. Cuando le pidas a la IA que te escriba este código, puedes comunicarle estos requisitos: es perfectamente capaz de implementarlos por ti.

:::inline div .quote-line
La gran lección de este capítulo: los modelos son la "munición" y la metodología, la "táctica". Elegir bien la munición facilita la batalla, pero sin buena táctica ni la mejor munición gana la guerra. Ya conoces las particularidades de cada modelo y su API: tienes un "arsenal" bien surtido; cómo librar esa batalla depende de la metodología de pensamiento de los capítulos anteriores.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Manos a la obra: consigue tu primera llamada a la API

{class="mt-1"}
Regístrate en una plataforma china de modelos (te recomiendo DeepSeek o Zhipu: ambas regalan crédito a los nuevos usuarios), crea una API key, guárdala en las variables de entorno del sistema (¡no en el código!) y ejecuta el código de la "primera llamada a la API" de arriba. En el momento en que veas impresa la respuesta de la IA, habrás cruzado la línea que separa "usar la IA" de "crear aplicaciones con IA".
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumen del capítulo

- Los tres grandes internacionales: GPT-5.6 (equilibrado y todoterreno), Claude (la cima en programación y solo un 1% de alucinaciones) y Gemini (el rey multimodal, con 2 millones de tokens de contexto)
- Los cinco grandes nacionales: DeepSeek V4 (el rey de la relación calidad-precio, ojo a los avisos de subida de precios), Qwen3.7 (nivel empresarial), GLM-5.1 (el mejor nacional en SWE), Kimi K3 (textos súper largos) y Doubao (gratis para empezar)
- Método de las cuatro preguntas para decidir: ¿dónde se despliega? ¿programación u otra cosa? ¿contexto súper largo? ¿presupuesto ajustado?
- El token es la unidad de facturación: un carácter chino equivale a unos 1,5-2 tokens; 1 millón de caracteres son unos 1,5 millones de tokens
- La API key es la contraseña de tu cartera: guárdala en variables de entorno; jamás la escribas en el código ni la subas a Git
- Los modelos nacionales suelen ser compatibles con el SDK de OpenAI: cambiar de modelo solo exige tocar dos líneas, api_key y base_url
- Cinco trucos para ahorrar: aciertos de caché, enrutamiento por niveles, limitar la salida, Batch API y monitorizar el consumo
:::
