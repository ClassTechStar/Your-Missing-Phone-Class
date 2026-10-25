---
id: di-san-shi-jiu-zhang
num: 39
part: ai-biancheng-pian
nav: Capítulo 39: Ingeniería de contexto — que la IA entienda tu intención
toc: default
kind: chapter
---

### Capítulo 39: Ingeniería de contexto — que la IA entienda tu intención

{class="chapter-intro mb-4"}
¿Te ha pasado? Abres una ventana de chat nueva y la IA parece amnésica: se ha olvidado de todo lo básico de tu proyecto. No es que quiera ponerte a prueba: es que de por sí «tiene mala memoria». Este capítulo te enseña a instalarle un «sistema de memoria a largo plazo» y, de paso, te presenta uno de los paradigmas de desarrollo con más tirón en 2026: el desarrollo guiado por especificaciones.

#### 1. El archivo de memoria del proyecto: la «memoria a largo plazo» de la IA

Los modelos de IA tienen una limitación de fondo: su memoria es «a corto plazo». Cada conversación empieza con la IA sabiendo cero de tu proyecto. Tienes que repetirle en el chat «usamos React», «el backend es Node.js», «la base de datos es PostgreSQL», «en el código usamos comillas dobles». No solo es ineficiente, sino que es fácil olvidar algo: como tener que hacer la inducción a un compañero nuevo cada día.

La solución es el «archivo de memoria del proyecto»: un archivo de texto plano en la raíz del proyecto que las herramientas de IA leen automáticamente al empezar cada conversación. Cada herramienta tiene su convención de nombre:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Herramienta</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Nombre del archivo</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cursor</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.cursorrules</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Code</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">CLAUDE.md</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GitHub Copilot</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">copilot-instructions.md</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Solución universal</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">AGENTS.md</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Convenciones de nombre del archivo de memoria de proyecto de cada herramienta

Aunque cambie el nombre, el principio es el mismo: escribes en este archivo la información que quieres que la IA «recuerde siempre». Un buen archivo de memoria de proyecto debe incluir: el resumen del proyecto (qué es), el stack técnico (qué tecnologías usa), las convenciones de código (nombres, indentación, estilo de comentarios), la estructura de directorios (cómo se organiza el código) y los acuerdos de desarrollo (estrategia de ramas, normas de commits, requisitos de pruebas). El CLAUDE.md de Karpathy tiene solo 70 líneas, pero cubre toda la información clave: conciso y completo.

::: div .code-block
:::inline div .code-head
<span>CLAUDE.md</span><span class="dots">···</span>
:::

```
# Proyecto: app de control de gastos personal
## Resumen
Es una app full-stack de control de gastos personales que ayuda al usuario a registrar ingresos y gastos diarios.
## Stack técnico
- Frontend: React + TypeScript + Tailwind CSS
- Backend: Node.js + Express + TypeScript
- Base de datos: SQLite (desarrollo) / PostgreSQL (producción)
- Tests: Vitest
## Estilo de código
- Usar comillas dobles
- Indentación de 2 espacios
- Nombres de función en camelCase
- Definiciones de tipos en PascalCase
- Cada función debe tener su comentario JSDoc
## Estructura de directorios
/src
  /frontend  - código del frontend
  /backend   - código del backend
  /shared    - tipos compartidos frontend/backend
  /tests     - archivos de test
## Convenciones de desarrollo
- Mensajes de commit en español
- Toda función nueva debe tener primero su test
- Las respuestas de la API usan siempre el formato { success, data, error }
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Ojo: no lo conviertas en «el segundo documento de requisitos»

{class="mt-1"}
Controla la longitud de este archivo: no lo conviertas en un documento de requisitos de decenas de páginas. El objetivo del archivo de memoria del proyecto es «dar a la IA una visión de contexto rápida», no «describir cada función al detalle». Mantenlo conciso y estructurado, y escribe solo lo que la IA necesita saber.
:::

#### 2. Desarrollo guiado por especificaciones (SDD)

El Spec-Driven Development (SDD, desarrollo guiado por especificaciones) es un paradigma de desarrollo que fue madurando en 2026, con una idea central que cabe en una frase: primero se escribe la especificación, después el código. A diferencia del TDD tradicional (desarrollo guiado por pruebas), la «especificación» del SDD no son solo casos de prueba: incluye la descripción de los requisitos, la definición de las interfaces, los modelos de datos y más. La IA genera el código a partir de esas especificaciones, y la responsabilidad del ser humano es escribirlas y mantenerlas.

El flujo de trabajo del SDD tiene cinco pasos:

1. Describe la especificación de requisitos en lenguaje natural (en un archivo .md);
2. Define las interfaces y las estructuras de datos (en el archivo de especificación);
3. Pide a la IA que genere la implementación del código según la especificación;
4. Ejecuta las pruebas para verificar si el resultado cumple la especificación;
5. Si no cumple, corrige la especificación o pide a la IA que corrija el código.

En este flujo, el archivo de especificación es la «única fuente de verdad»: el código se puede regenerar, pero la especificación debe ser correcta primero.

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> Escribir el documento de especificaciones</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> ¿La especificación está completa?</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> Completa</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-robot mr-1"></i> La IA genera código a partir de la especificación</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> Ejecutar tests para verificar el resultado</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-times-circle mr-1"></i> Incompleta / tests fallidos</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-tools mr-1"></i> Problema de código → corrige el código; problema de especificación → corrige la especificación</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> Volver a verificar</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> Todo correcto → entrega</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figura 3: flujo de trabajo del desarrollo guiado por especificaciones (SDD)
:::

La gran ventaja del SDD: los archivos de especificación son más estables que el código. Cuando cambie el modelo o las herramientas de base, tus archivos de especificación siguen siendo válidos; basta pedir a la nueva herramienta de IA que regenere el código. Por eso este libro insiste en que «la metodología importa más que las herramientas»: el archivo de especificación es el soporte concreto de tu metodología.

#### 3. Gestión de la ventana de contexto

Aunque tengas el archivo de memoria del proyecto, seguirás topándote en la conversación con el problema de «contexto que no basta». La ventana de contexto del modelo de IA (la cantidad de información que puede procesar a la vez) es limitada. Cuando la conversación se alarga o citas demasiados archivos, la IA «olvida» la información temprana y la calidad de la producción baja: como hablar seis horas seguidas con un amigo, que ya no recuerda lo primero que le dijiste al empezar.

La estrategia central para gestionar la ventana de contexto es «referenciar por capas»:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Capa de contexto</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Contenido</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Cómo se gestiona</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Capa 1: memoria del proyecto</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Stack técnico, convenciones, estructura de directorios</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Va en archivos como CLAUDE.md; se carga sola y no hay que repetirla</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Capa 2: referencias a archivos</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Los archivos de código implicados en la tarea actual</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Se referencian con precisión con el símbolo @, sin pegar el texto completo en la conversación</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Capa 3: contexto de la conversación</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">El historial de conversación de la tarea actual</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Al terminar una tarea, abre una conversación nueva para evitar que el contexto se sobrecargue</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cuarto nivel: instrucciones inmediatas</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Los requisitos concretos del paso actual</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claras, concisas y con un objetivo concreto; evita las descripciones largas</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Estrategia de gestión por niveles de la ventana de contexto

#### 4. Claves prácticas de la ingeniería de contexto

La ingeniería de contexto no es una configuración única, sino un proceso de mejora continua. Estos son algunos puntos que la práctica ha validado una y otra vez:

1. Mantén el archivo de memoria actualizado a medida que evoluciona el proyecto. Cuando introduzcas una tecnología nueva o cambies de arquitectura, actualiza el archivo de memoria de inmediato, en lugar de explicarlo sobre la marcha en la conversación.
2. Saca partido a las referencias @ en lugar de pegar el texto completo. La mayoría de las herramientas de programación con IA admiten la sintaxis @file o @folder, que inyecta en segundo plano el contenido del archivo en el contexto de la IA: es más eficiente que pegarlo a mano y no contamina la conversación.
3. Conversaciones «cortas y al grano». Una conversación para una sola tarea o un solo punto de funcionalidad; al terminar, abre una nueva para lo siguiente. Las conversaciones largas no solo consumen la ventana de contexto, sino que también «distraen» a la IA.
4. Enséñale a la IA los resultados en lugar de describírselos. Cuando te salga un error, referencia el registro de errores directamente con @, en vez de describirlo con tus palabras («creo que hay algún error»). Para la IA es más efectivo ver la información original que leer tu paráfrasis.
5. Limpia y archiva con regularidad. Las conversaciones terminadas y los archivos temporales ocupan espacio de trabajo. Purga de vez en cuando lo que no sirva y mantén ordenado el directorio del proyecto: eso también ayuda a la IA a entender la estructura del proyecto de manera más eficiente.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Manos a la obra: escribe un archivo de memoria de 70 líneas para tu proyecto

{class="mt-1"}
Elige un proyecto que estés haciendo (o que planees hacer) y escribe un CLAUDE.md: descripción general (2 o 3 frases), stack tecnológico (enumerado), normas de código (3 a 5), estructura de directorios (dibuja un árbol) y convenciones de desarrollo (2 o 3). No pases de 70 líneas: al terminarlo descubrirás que entiendes tu proyecto bastante mejor.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumen del capítulo

- La memoria de la IA es «a corto plazo»: en cada conversación nueva su conocimiento del proyecto parte de cero
- El archivo de memoria del proyecto (CLAUDE.md y similares) es la «memoria a largo plazo» de la IA y se carga automáticamente en cada conversación
- Un buen archivo de memoria = descripción general + stack + normas + directorios + convenciones; con 70 líneas basta
- Desarrollo guiado por especificaciones (SDD): primero la especificación, después el código; la especificación es la «única fuente de verdad» y es más estable que el código
- El contexto se gestiona en cuatro niveles: memoria del proyecto → referencias @archivo → historial de conversación → instrucciones inmediatas
- Cinco claves prácticas: actualizar en sincronía, referencias @, conversaciones cortas, dar la información original y limpiar con regularidad
:::
