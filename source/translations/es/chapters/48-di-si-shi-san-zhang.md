---
id: di-si-shi-san-zhang
num: 43
part: ai-biancheng-pian
nav: Capítulo 43: Ingeniería del diálogo — técnicas de conversación para colaborar con eficiencia con la IA
toc: default
kind: chapter
---

### Capítulo 43: Ingeniería del diálogo — técnicas de conversación para colaborar con eficiencia con la IA

{class="chapter-intro mb-4"}
El diálogo es la forma central de interacción en la programación con IA. Pero ojo: "diálogo" no es lo mismo que "charlar": una conversación eficiente de programación con IA es una técnica de comunicación con estructura, y la llamamos "ingeniería del diálogo". Estudia cómo obtener el código de máxima calidad con el mínimo número de turnos de conversación. Dicho sin rodeos: este capítulo te enseña a "expresarte con claridad" con la IA.

#### I. Estrategia de prompts por capas

La conversación con la IA se puede dividir en tres capas, y cada una cumple una función distinta. Si entiendes esas tres capas, podrás combinar prompts eficientes como quien apila bloques.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Capa</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Función</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ejemplo</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Frecuencia</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Capa de sistema</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Fija el rol de la IA y las restricciones globales</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"Eres un experto en React y el código debe ir en TypeScript"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Se configura una vez, al iniciar el proyecto</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Capa de tarea</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Describe la tarea concreta que toca hacer</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"Crea un componente de formulario con campos de usuario y contraseña"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Se da al empezar cada tarea</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Capa de retroalimentación</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Evalúa y corrige lo que produce la IA</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"Al campo de contraseña le falta el interruptor de mostrar/ocultar; añádelo"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Se da según la calidad del resultado</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Las tres capas del prompt de conversación

El prompt de la capa de sistema suele escribirse en el archivo de memoria del proyecto (como CLAUDE.md) y no hace falta repetirlo en cada conversación. La capa de tarea es la que más usarás al conversar: debe incluir tres elementos: "qué hacer", "con qué tecnología" y "con qué restricciones". La capa de retroalimentación es la que más pone a prueba tu nivel: una buena retroalimentación permite a la IA corregir con precisión; una mala solo la llevará a adivinar otra vez.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Consejo: las tres claves de la retroalimentación

{class="mt-1"}
Una plantilla práctica de retroalimentación es "señalar el problema + decir qué esperas + aportar contexto". Por ejemplo: "el manejo de errores de la línea 25 solo usa console.log (señala el problema), en producción debería usarse un gestor de errores unificado y devolver mensajes comprensibles para el usuario (dices qué esperas), en el proyecto hay una función handleError que puedes usar (aportas contexto)". Este tipo de retroalimentación es diez veces más eficaz que un "arregla el manejo de errores".
:::

#### II. Diálogos de depuración: cómo describir un error para que la IA lo localice rápido

La depuración es uno de los escenarios más frecuentes de la programación con IA. Cuando te encuentres con un bug, la manera de describirle el problema a la IA decide directamente si puede ayudarte a localizarlo y arreglarlo rápido. Estos son los cuatro puntos clave del diálogo de depuración:

1. Dale a la IA la información "en crudo", no tu paráfrasis. Cítale directamente los registros de error, las trazas de excepciones y el código relacionado (con @), en lugar de describirlo con un "creo que salió un error". La IA lee la información original con más precisión que tu interpretación.
2. Describe la diferencia entre el "comportamiento esperado" y el "comportamiento real". "Espero que al pulsar el botón salte a la página de inicio (esperado), pero al pulsarlo la página no reacciona (real)": esta descripción sirve muchísimo más que "el botón está roto".
3. Aporta los pasos de reproducción. "Primero escribo el nombre de usuario, luego pulso el botón de iniciar sesión y aparece este error": con los pasos de reproducción, la IA puede simular tu ruta de uso y localizar el problema con más facilidad.
4. Aclara qué has probado ya. "Ya revisé la petición de red: devuelve 200 y los datos llegan bien": eso ayuda a la IA a descartar caminos ya verificados y no perder el tiempo repitiendo pruebas.

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
Descripción de depuración mala

{class="font-mono text-xs leading-relaxed"}
El botón no responde al pulsar, échale un ojo
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
Descripción de depuración buena

{class="font-mono text-xs leading-relaxed"}
Al pulsar el botón de iniciar sesión, la página no reacciona. Comportamiento esperado: al pulsar, navegar a la página /home Comportamiento real: al pulsar no pasa nada y la consola no muestra errores Pasos de reproducción: 1. En la página de inicio de sesión, introduce el usuario admin y la contraseña 123456 2. Pulsa el botón "Iniciar sesión" 3. La página no reacciona Comprobaciones ya hechas: - La petición de red funciona y devuelve 200 - El evento onClick está vinculado - Revisé el código del componente LoginButton Archivos relacionados: @src/components/LoginButton.tsx @src/pages/Login.tsx
:::
:::

#### III. Estrategias de iteración: pasos pequeños y rápidos frente a la gran refactorización

En la programación con IA hay dos estrategias básicas de iteración, válidas para escenarios distintos. Entender sus diferencias te ayudará a elegir bien en cada situación.

La estrategia de "pasos pequeños y rápidos" sirve para desarrollar funciones y corregir bugs. Su esencia: cada vez pides a la IA un solo cambio pequeño y, cuando lo validas, pasas al siguiente. Ventaja: cada paso es verificable y reversible, con el riesgo bajo control. Desventaja: es más lenta y exige muchas interacciones. Apta para: desarrollar funciones nuevas, explorar cuando aún no tienes clara la mejor solución e iterar con cautela cuando no te fías del todo del resultado de la IA.

La estrategia de "gran refactorización" sirve para cambios a gran escala con un objetivo claro. Su esencia: describes el objetivo completo de una sola vez y dejas que la IA planifique y ejecute todo el cambio de forma autónoma. Ventaja: es rápida y, al ver el panorama global, la IA toma mejores decisiones de arquitectura. Desventaja: el riesgo es alto: si la IA se equivoca de interpretación, corregir sale caro. Apta para: mejoras de arquitectura bien definidas, migraciones masivas de código y refactorizaciones respaldadas por suficientes pruebas.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Dimensión</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Pasos pequeños y rápidos</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Gran refactorización</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tamaño de cada cambio</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Un punto de función o un bug</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Un módulo o una capa de arquitectura</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Frecuencia de verificación</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Se verifica justo después de cada cambio</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Se verifica todo junto al terminar todos los cambios</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Turnos de conversación</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Muchos (5-10 por función)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pocos (1-3 por módulo)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Riesgo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bajo, cada paso puede revertirse</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Alto, corregir desvíos sale caro</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Escenarios indicados</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Funciones nuevas, desarrollo exploratorio</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Refactorizaciones y migraciones con objetivo claro</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Requisito previo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ninguno especial</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Necesita cobertura de pruebas</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Comparación de las dos estrategias de iteración

En la práctica, las dos estrategias suelen combinarse. Por ejemplo, al refactorizar un módulo, primero usa la "gran refactorización" para que la IA presente el plan general y, una vez revisado el plan, ejecuta paso a paso con "pasos pequeños y rápidos". Así conservas la visión global y controlas el riesgo de ejecución.

#### IV. Gestión del contexto en conversaciones de varios turnos

A medida que aumentan los turnos, tienes que gestionar activamente el contexto de la conversación para evitar el problema de que "la IA olvide la información de los primeros mensajes". Estos son algunos trucos prácticos de gestión del contexto.

Primero, "ancla" la información clave. Al empezar la conversación, escribe con claridad las restricciones clave y recuérdalas en su momento durante los mensajes siguientes. Por ejemplo: "recuerda que guardamos los datos en localStorage y no podemos usar base de datos": reitera esa restricción en las peticiones de cambio relacionadas para que la IA no la olvide.

Segundo, domina el truco de "resumir y continuar". Cuando la conversación se haga muy larga, pide a la IA que "resuma el avance actual y las tareas pendientes", abre una conversación nueva y parte de ese resumen. Así conservas el contexto clave y evitas la degradación de las conversaciones largas.

Tercero, "una conversación, una tarea". Es la estrategia de gestión del contexto más simple y más eficaz. Cada conversación atiende una sola tarea o un solo punto de función; al terminar, abres una nueva para lo siguiente. Esto limita de forma natural la longitud de la conversación y mantiene el contexto despejado.

Cuarto, aprovecha las funciones de gestión de contexto de las herramientas. Casi todas las herramientas de programación con IA tienen un botón de "limpiar contexto" o de "nueva sesión": cuando notes que baja la calidad de las respuestas, no lo dudes, abre una sesión nueva. Perder parte del historial es mucho mejor que seguir batallando dentro de un contexto degradado.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Manos a la obra: haz de "paciente" ante tu IA

{class="mt-1"}
Crea a propósito una página pequeña en el navegador y provoca un bug (por ejemplo, un botón que no reacciona). Después descríbeselo a la IA de una pieza siguiendo el formato de la "descripción de depuración buena" de este capítulo: información en crudo, esperado frente a real, pasos de reproducción y comprobaciones ya hechas. Nota la diferencia de velocidad con la que la IA localiza el problema y entenderás por qué "describir un problema" es, en sí mismo, un oficio.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumen del capítulo

- Tres capas del prompt: sistema (va al archivo de memoria), tarea (qué hacer + tecnología + restricciones) y retroalimentación (problema + expectativa + contexto)
- Cuatro claves de la depuración: dar la información en crudo, esperado frente a real, pasos de reproducción y comprobaciones ya hechas
- Pasos pequeños y rápidos: riesgo bajo y muchos turnos, ideal para funciones nuevas; gran refactorización: riesgo alto y pocos turnos, necesita respaldo de pruebas
- Cuatro trucos de gestión del contexto: anclar la información clave, resumir y continuar, una conversación una tarea y abrir sesión nueva sin vacilar
:::
