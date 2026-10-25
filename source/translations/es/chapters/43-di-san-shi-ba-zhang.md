---
id: di-san-shi-ba-zhang
num: 38
part: ai-biancheng-pian
nav: Capítulo 38: Los cinco principios de pensamiento de la programación con IA
toc: default
kind: chapter
---

### Capítulo 38: Los cinco principios de pensamiento de la programación con IA

{class="chapter-intro mb-4"}
Si solo puedes quedarte con un capítulo de este libro, que sea este. Los cinco principios de pensamiento son el corazón de la obra; todos los capítulos posteriores —contexto, requisitos, conversación, calidad— son estos cinco principios desplegados en distintos escenarios. Tranquilo: ninguno es difícil de entender, pero cada uno merece que lo «metas en el músculo» con un par de proyectos.

El origen de la historia es curioso: al publicar su proyecto como código abierto, Andrej Karpathy adjuntó un archivo CLAUDE.md de apenas 70 líneas que resumía cuatro principios centrales para colaborar con la IA. Ese archivo acumuló más de 70.000 estrellas en GitHub y se convirtió en la guía más citada por la comunidad mundial de programación con IA. No son consignas vacías, sino hábitos de pensamiento accionables destilados de mucha práctica. Sobre esa base, este libro añade un quinto principio —la verificación iterativa— y completa el sistema de los cinco principios.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
¿Por qué vale tanto un archivo de 70 líneas?

{class="mt-1"}
¿Qué significan 70.000 estrellas? En GitHub, la inmensa mayoría de los proyectos jamás llega a esa cifra. Que un archivo de texto de 70 líneas la consiga demuestra una cosa: en la era de la IA, lo escaso no es el código, sino la capacidad de «pensar con claridad». Esas 70 líneas son la versión condensada de «pensar con claridad».
:::

#### 1. Principio 1: Think Before Coding (piensa primero, programa después)

Es el principio más contraintuitivo de los cinco. Si la IA puede escribir el código por nosotros, ¿para qué «pensar primero»? La respuesta es sencilla: la calidad de lo que produce la IA es proporcional a la calidad de tu entrada. Si ni tú tienes claro qué quieres hacer, sus respuestas te meterán en un bucle interminable de «cambiar y volver a cambiar»: lo que popularmente se llama «que la IA se pierda contigo».

«Pensar primero» significa que, antes de dar una instrucción a la IA, respondes tres preguntas que forman un «triángulo de pensamiento» del que no puede faltar ninguna esquina:

1. ¿Qué problema quiero resolver? (objetivo)
2. ¿Cómo quiero que sea el resultado? (criterios de aceptación)
3. ¿Qué restricciones debo respetar? (límites)

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Dimensión de pensamiento</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Entrada vaga (mal)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Entrada clara (bien)</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Definición del problema</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Hazme una web</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Hazme un sitio personal de herramientas con tarjetas de acceso a 3 utilidades de IA</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Resultado esperado</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Que se vea bonito</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Diseño responsive, tema oscuro, tarjetas con animación al pasar el cursor y usable en el móvil</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Restricciones</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">(no se indican)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sin frameworks, HTML+CSS+JS puro, despliegue en un solo archivo y sin backend</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Comparación de entrada vaga y entrada clara para la misma necesidad

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Ojo: pensar primero ≠ escribir antes un documento perfecto

{class="mt-1"}
«Pensar primero» no es «redactar un PRD perfecto antes de empezar». Es un proceso de reflexión rápido pero ordenado: dedicar 30 segundos a las tres preguntas de arriba rinde mucho más que 30 minutos de correcciones repetidas en la conversación. En las tareas pequeñas las tres preguntas pueden ser breves; en los proyectos grandes puedes ampliarlas a un documento completo de requisitos (más detalles en el capítulo 40).
:::

#### 2. Principio 2: Simplicity First (primero lo simple)

La mayor trampa de la programación con IA no es «no poder hacerlo», sino «hacer demasiado». Cuando le pides a la IA «hazme un sistema de gestión de usuarios», puede generar todo un kit: autenticación, permisos, roles, registros de auditoría, exportación de datos… y quizá tú solo necesitabas una página de inicio de sesión sencilla. La sobre-generación es la causa principal de la hinchazón del código de la IA.

«Primero lo simple» exige aplicar el principio del «mínimo viable» en cada instrucción: implementar la función central con el mínimo código, resolver el problema con la solución más sencilla y validar la idea con las funciones justas. Karpathy lo resumió en una metáfora brillante: «si quieres calcular un precio con descuento, no necesitas un motor de e-commerce».

En la práctica, «primero lo simple» se traduce en unos hábitos concretos:

- Pedir a la IA un solo punto de función cada vez, en lugar de describir el sistema entero de un tirón;
- Preferir la biblioteca estándar y las soluciones sencillas antes que introducir dependencias complejas;
- Si algo se resuelve con 50 líneas de código, no dejar que la IA escriba 500;
- Y cuando la producción de la IA se pase del alcance esperado, decirle con valentía: «recorta lo que sobra».

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Escenario</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Solución excesiva (evitar)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Solución simple (recomendada)</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Necesitas guardar datos</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Montar una base de datos MySQL + ORM</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Empezar con un archivo JSON o SQLite</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Necesitas inicio de sesión de usuarios</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OAuth2.0 + JWT + permisos por roles</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Empezar con una verificación de contraseña simple</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Necesitas un framework de frontend</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">React + Redux + Router</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Probar primero HTML puro + JS nativo</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Necesitas desplegar en producción</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Docker + CI/CD + K8s</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Primero hacer que funcione en local</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Comparación de soluciones excesivas y simples en escenarios habituales

#### 3. Principio 3: Surgical Changes (cambios quirúrgicos)

Cuando iteras sobre un proyecto ya existente, cada cambio debería ser tan preciso como una operación quirúrgica: tocar solo lo que hay que tocar y no meter mano a lo demás. Esto importa aún más en la programación con IA, porque la IA tiende a «aprovechar para retocar»: le pides arreglar un bug y de paso te refactoriza medio archivo.

La exigencia central de los «cambios quirúrgicos» es: en cada instrucción a la IA, delimita con claridad el alcance y los límites del cambio. Dile «modifica solo la función calculate_discount», «no toques el resto» y «mantén el estilo de código actual». Si la IA se sale del alcance que pediste, exige de inmediato que revierta lo que sobra.

Karpathy lo ilustró con un ejemplo de diff (comparación de cambios). Imagina que pides a la IA añadir la lógica de «precio de socio» a la función de cálculo de descuentos del carrito: una buena producción modifica solo esa función y añade unas pocas líneas; una mala reescribe el archivo entero — por elegante que quede el código nuevo, no puedes asegurar que no haya introducido bugs nuevos. En la programación con IA, «parece mejor» nunca puede justificar desviarse de la instrucción.

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
Instrucción mala (alcance vago)

{class="font-mono text-xs leading-relaxed"}
Ayúdame a optimizar la lógica de descuentos de este proyecto
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
Instrucción buena (alcance preciso)

{class="font-mono text-xs leading-relaxed"}
Modifica solo la función calculate_discount de cart.py: 1. Añade la lógica de precio de socio sobre los descuentos existentes 2. Los socios reciben un 10 % adicional de descuento 3. No cambies la firma de la función ni las demás funciones 4. Mantén el estilo de nombres de variables actual
:::
:::

#### 4. Principio 4: Goal-Driven Execution (ejecución orientada a objetivos)

Este principio responde a una pregunta clave: ¿debes darle a la IA instrucciones de «cómo hacerlo» o de «qué hacer»? La respuesta de Karpathy es lo segundo. En lugar de decirle «primero crea una clase, luego añade métodos y después escribe las pruebas», dile «necesito una herramienta que lea archivos CSV y cuente los valores únicos de cada columna». Deja que la IA decida la ruta de implementación; tú te encargas de aceptar el resultado.

Las ventajas de «orientarse al objetivo» son dobles. Para la IA: gana un mayor margen de autonomía y puede elegir la ruta de implementación óptima en lugar de quedar atada a tus pasos intermedios. Para ti: trasladas tu atención del «cómo se hace» al «si lo que se hizo está bien», que es justamente lo que debe hacer un director.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Ojo: orientación al objetivo ≠ dejarlo suelto

{class="mt-1"}
Exige que, tras ejecutar la IA, hagas una aceptación rigurosa: ¿el resultado cumple los requisitos? ¿Se manejan los casos límite? ¿Hay sobre-ingeniería evidente? Si el resultado no es el esperado, da una retroalimentación concreta: no «reescríbelo», sino «el problema está en que con una lista vacía como entrada lanza un IndexError; añade una comprobación de valores nulos».
:::

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Estilo de instrucción</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ejemplo</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Cómo resulta</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Imperativo (cómo hacerlo)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">«Primero crea una clase de Python llamada DataParser, añade un método parse que reciba un parámetro filename y lea con el módulo csv…»</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">La IA se convierte en mecanógrafa; tus pasos intermedios quizá no sean la ruta óptima</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Por objetivos (qué hacer)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">«Necesito una herramienta: lee un archivo CSV, cuenta los valores únicos de cada columna y da la salida en formato JSON. Dame la implementación completa.»</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">La IA elige sola la ruta óptima y tú te encargas de aceptar el resultado</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Comparación entre instrucciones imperativas y por objetivos

#### 5. Principio 5: Iterate and Verify (iterar y verificar)

Es el quinto principio que este libro añade a los cuatro de Karpathy. Su convicción central: la primera producción de la IA casi nunca es la versión final. Programar bien con IA es un bucle iterativo de «generar-verificar-corregir», no un «instrucción-producción» de una sola vez.

«Iterar y verificar» no es ese «si falla, reintenta» pasivo, sino un proceso de verificación estructurado. Cada vez que la IA entrega algo, verifica en tres niveles:

- Nivel 1 · verificación funcional: ¿funciona? ¿Las entradas y las salidas son correctas?
- Nivel 2 · verificación de límites: ¿qué pasa con entradas vacías, demasiado largas o anómalas?
- Nivel 3 · verificación de arquitectura: ¿la estructura del código es razonable? ¿Hay valores codificados a mano? ¿Se puede ampliar después con facilidad?

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-bullseye mr-1"></i> Definir el objetivo</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-robot mr-1"></i> La IA genera código</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> Verificación funcional</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> Correcto</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> Verificación de límites</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> Correcto</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-landmark mr-1"></i> Revisión de la arquitectura</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> Correcto, al siguiente paso</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-times-circle mr-1"></i> Incorrecto</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> Dar feedback concreto</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> Regenerar</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figura 2: el bucle de iteración y verificación de la programación con IA
:::

La clave del bucle está en el paso «dar retroalimentación concreta». Cuando la verificación falla, no digas «mal, hazlo otra vez», sino «la función lanza un IndexError con listas vacías; añade la comprobación de nulos en la línea 15». La retroalimentación concreta permite a la IA corregir con precisión; la vaga solo la obliga a adivinar otra vez tu intención.

#### 6. Harness Engineering: Agente = Modelo + Harness

A mediados de 2026 empezó a popularizarse en la comunidad de programación con IA un concepto llamado Harness Engineering. Su fórmula central es muy sencilla:

:::inline div .quote-line .text-center .text-base .font-bold
<strong>Capacidad del Agent = capacidad del modelo × calidad del Harness</strong>
:::

La capacidad del modelo es el techo intelectual del cerebro de la IA; el Harness es el «entorno de trabajo» construido en torno al modelo: gestión del contexto, integración de herramientas, orquestación de flujos, sistemas de memoria, etc.

Este concepto resuelve una confusión frecuente: ¿por qué, usando el mismo GPT-4 o Claude, hay quien saca proyectos asombrosos y quien solo obtiene código mediocre? La diferencia no está en el modelo, sino en el Harness. Un buen Harness incluye: archivos de especificación del proyecto claros, una integración de herramientas sensata, un contexto de conversación ordenado y un proceso de verificación completo. El modelo fija el techo intelectual; el Harness decide hasta dónde llegas a aprovecharlo.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
La metáfora del becario genio

{class="mt-1"}
Imagina el modelo como un becario genio: cociente intelectual altísimo, pero si no le das la documentación del proyecto, no le dices qué herramientas usar ni le fijas plazos y criterios de aceptación, tampoco producirá nada bueno. El Harness Engineering es la ingeniería de «cómo montar el entorno de trabajo perfecto para un becario genio».
:::

Los capítulos que quedan de este libro son, en el fondo, un manual para construir un buen Harness: el capítulo 39 te enseña a gestionar el contexto (el sistema de memoria del proyecto), el 40 a definir los requisitos (PRD), el 43 las técnicas de conversación (capas de prompt) y el 45 la garantía de calidad (procesos de verificación). Todo junto es tu Harness.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Manos a la obra: desmenuza tu próxima idea con el «triángulo de pensamiento»

{class="mt-1"}
Elige esa cosita que llevas tiempo queriendo hacer y nunca empiezas (por ejemplo, una web de cuenta atrás o un script que te recuerde beber agua). Tómate 3 minutos para responder: ① ¿Qué problema resuelve? ② ¿Cómo sería una vez hecha? ③ ¿Qué restricciones hay (tiempo, tecnología, entorno)? Luego escribe las respuestas en un párrafo. Enhorabuena: acabas de completar tu primer «Think Before Coding» de la vida, y ese párrafo ya es una instrucción de calidad digna de ese nombre.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumen del capítulo

- Los cinco principios vienen del CLAUDE.md de 70 líneas de Karpathy (más de 70.000 estrellas); este libro añade el quinto, «iterar y verificar»
- Think Before Coding: antes de hablar, responde tres preguntas: ¿qué hacer? ¿cómo será el resultado? ¿qué restricciones hay?
- Simplicity First: la mayor trampa de la IA es «hacer demasiado»; para calcular un descuento no hace falta un motor de e-commerce
- Surgical Changes: cambia con precisión quirúrgica y rechaza el «aprovecho para retocar» de la IA
- Goal-Driven Execution: di «qué hacer», no «cómo hacerlo», y deja que la IA elija la ruta
- Iterate and Verify: verificación en tres niveles (funcional/límites/arquitectura) + retroalimentación concreta, iterando en bucle
- Harness Engineering: capacidad = modelo × Harness; trata a la IA como a un «becario genio» y gestiona su entorno
:::
