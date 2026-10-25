---
id: di-si-shi-si-zhang
num: 44
part: ai-biancheng-pian
nav: Capítulo 44: De 0 a 1 en la práctica — el flujo completo de un proyecto
toc: default
kind: chapter
---

### Capítulo 44: De 0 a 1 en la práctica — el flujo completo de un proyecto

{class="chapter-intro mb-4"}
La teoría ya está; ahora toca hacer. Este capítulo no es un tutorial de "escribir lo que yo escribo", sino una metodología práctica de "cómo pensar, cómo pedir y cómo verificar". Con tres proyectos de distinta dificultad mostraremos el proceso completo de razonamiento, desde los requisitos hasta el producto terminado. Uses la herramienta que uses, este flujo te sirve.

#### I. Proyecto uno: web minimalista de herramientas personales (nivel inicial)

##### 1. Pensar los requisitos

Objetivo: crear una web de herramientas personales con entradas a 3-4 utilidades prácticas. Es un proyecto puramente frontend, sin backend ni base de datos. Lo importante no es lo sofisticadas que sean las herramientas, sino experimentar el flujo completo "de los requisitos al producto".

Según los cinco elementos del requisito: Quién: uso personal. Qué: una web que muestra entradas a herramientas. Por qué: reunir las utilidades de uso diario en una sola página para tenerlas a mano. Cómo: un solo archivo HTML+CSS+JS, sin frameworks. Restricción: terminarlo en 30 minutos, sin necesidad de despliegue.

##### 2. Dar la instrucción

Siguiendo el principio Think Before Coding, tu instrucción debe contener información suficiente para que la IA entienda el objetivo, sin que tengas que detallar cada pormenor de la implementación:

::: div .code-block
:::inline div .code-head
<span>Instrucción para la IA</span><span class="dots">···</span>
:::

```
Crea una web personal de herramientas con estos requisitos:
1. HTML de un solo archivo (CSS y JS en línea), sin frameworks
2. Tema oscuro, estilo moderno y minimalista
3. Muestra 4 tarjetas de acceso a herramientas:
   - Resumidor de texto
   - Contador de palabras
   - Selector de color
   - Generador de códigos QR
4. Cada tarjeta con icono, título y descripción breve
5. Las tarjetas tienen animación al pasar el ratón
6. Diseño responsive, usable en el móvil
7. Barra de título arriba
Dame directamente el archivo HTML completo.
```
:::

##### 3. Aceptación e iteración

Cuando la IA entregue el código, haz la aceptación con la verificación de tres capas. Primera capa, verificación funcional: ¿el archivo se abre en el navegador? ¿Se muestran las 4 tarjetas? ¿Va bien la animación al pasar el cursor? Segunda capa, verificación de límites: ¿la maquetación se ve bien en tamaño de pantalla de móvil? ¿Las tarjetas saltan de línea cuando la ventana es muy estrecha? Tercera capa, verificación de arquitectura: ¿el código se lee bien? ¿El CSS está dentro de una única etiqueta style? ¿Hay redundancias evidentes?

Si además quieres implementar la función de alguna tarjeta (y no solo la entrada), puedes ir añadiéndola poco a poco: añade la función de una herramienta, verifícala y pasa a la siguiente. Es la aplicación en la práctica de la estrategia de "pasos pequeños y rápidos".

#### II. Proyecto dos: sistema de contabilidad full stack (nivel intermedio)

##### 1. Pensar los requisitos y el PRD

Objetivo: una aplicación de contabilidad full stack con frontend, backend y base de datos. Este proyecto es mucho más complejo que el primero y necesita el método de ingeniería de requisitos del capítulo 40.

Escribe primero el PRD. Con la plantilla de la sección 3 del capítulo 40, redacta la visión general del proyecto, la lista de funciones, la solución técnica, el modelo de datos y el plan de desarrollo. Al elegir la solución técnica, aplica el principio Simplicity First: frontend con React pero sin Redux ni gestiones de estado complejas; backend con Node.js pero sin microservicios; base de datos SQLite y no PostgreSQL (en fase de desarrollo).

El plan de desarrollo se divide en 5 pasos: Paso 1, esqueleto de la API del backend (servidor Express + SQLite + endpoints CRUD); Paso 2, páginas básicas del frontend (lista de registros + formulario de alta); Paso 3, conexión frontend-backend (llamadas a la API + presentación de datos); Paso 4, funciones de categorías y filtros; Paso 5, resumen mensual y gráficos sencillos. Al terminar cada paso tendrás algo "utilizable".

##### 2. Configurar el archivo de memoria del proyecto

Antes de ponerte a programar, crea el archivo de memoria del proyecto. Es la práctica central de la ingeniería de contexto: conseguir que la IA conozca el trasfondo del proyecto al empezar cada conversación.

::: div .code-block
:::inline div .code-head
<span>CLAUDE.md</span><span class="dots">···</span>
:::

```
# Proyecto: app full-stack de control de gastos
## Resumen
App de control de gastos personales con soporte para registro de ingresos y gastos, categorías y resúmenes mensuales.
## Stack técnico
- Frontend: React + TypeScript + Vite
- Backend: Node.js + Express + TypeScript
- Base de datos: SQLite (vía better-sqlite3)
- Tipos compartidos entre frontend y backend
## Convenciones de la API
- Ruta base: /api
- Formato de respuesta: { success: boolean, data: any, error: string }
- Estilo RESTful
## Modelo de datos
Record { id, amount, type, category, note, date }
## Estilo de código
- Modo estricto de TypeScript
- Indentación de 2 espacios
- Funciones con comentario JSDoc
- Comentarios y mensajes de commit en español
```
:::

##### 3. Implementar paso a paso

Siguiendo el plan de desarrollo, completa cada paso en una conversación aparte. Esta es una instrucción de ejemplo para el primer paso:

::: div .code-block
:::inline div .code-head
<span>Instrucción para la IA (Step 1)</span><span class="dots">···</span>
:::

```
Necesito crear el esqueleto de la API del backend.
Requisitos:
1. Servidor Express, puerto 3001
2. Base de datos SQLite, tabla records
3. Campos de la tabla records:
   id (TEXT PRIMARY KEY)
   amount (REAL)
   type (TEXT: 'income'|'expense')
   category (TEXT)
   note (TEXT)
   date (TEXT: YYYY-MM-DD)
4. Endpoints CRUD:
   GET /api/records - obtener todos los registros
   POST /api/records - añadir un registro
   PUT /api/records/:id - actualizar un registro
   DELETE /api/records/:id - borrar un registro
5. Middleware de gestión de errores
Dame la estructura completa del código del backend.
```
:::

Fíjate en los rasgos de esta instrucción: describe solo el paso actual (el esqueleto del backend), sin mezclar requisitos del frontend; enumera con claridad campos y endpoints (le da a la IA restricciones suficientes), pero deja la implementación concreta en manos de la IA; y sigue el principio Goal-Driven Execution: dice "qué hacer", no "cómo hacerlo".

Cuando la IA entregue el código, verifícalo enseguida: arranca el servidor y prueba cada endpoint con curl o Postman. Si todo está bien, abre una conversación nueva para el Paso 2 (páginas básicas del frontend). En cada paso se repite el ciclo "instrucción, verificación, nueva conversación".

#### III. Proyecto tres: aplicación potenciada con IA (nivel avanzado)

##### 1. Concebir el proyecto

Objetivo: una aplicación conectada a la API de un gran modelo, por ejemplo un "asistente de estudio con IA": el usuario introduce el contenido que quiere aprender y la IA genera un resumen, relaciona conceptos y recomienda recursos de estudio. Lo especial de este proyecto es que tu propia aplicación llama a la IA, así que tendrás que resolver problemas nuevos: llamadas a la API, ingeniería de prompts, gestión de errores, etc.

La lección más importante de este proyecto: cuando "uses la IA para escribir código que llama a la IA", tienes que vigilar especialmente la ingeniería de prompts. Los prompts que tu aplicación usa al llamar a la API del gran modelo también deben seguir los principios que discute esta guía: claros, concisos y orientados al objetivo.

##### 2. Puntos técnicos clave

Este proyecto toca varios puntos técnicos que no aparecieron en los dos anteriores:

- Gestión de las claves de API: las claves nunca van dentro del código; se gestionan con variables de entorno;
- Tratamiento de respuestas en streaming: las respuestas de los grandes modelos suelen llegar en streaming y hay que mostrarlas palabra a palabra;
- Control del consumo de tokens: los grandes modelos cobran por token, así que el gasto se controla a nivel de aplicación;
- Gestión de plantillas de prompt: cada función usa su propia plantilla de prompt y conviene gestionarlas de forma estructurada.

La IA puede ayudarte a implementar todos estos puntos, pero tú necesitas entender el "porqué" de cada uno: ¿por qué las claves no van en el código? ¿Por qué hacen falta respuestas en streaming? ¿Por qué hay que controlar el consumo de tokens? Solo entendiendo el porqué podrás juzgar si la solución de la IA es razonable.

#### IV. Lista de control del flujo práctico universal

Sea el proyecto grande o pequeño, esta es una lista de control universal para programar con IA. Cada vez que empieces un proyecto nuevo, repásala para no dejar fuera ningún paso clave.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Fase</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Qué se hace</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Principio asociado</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1. Pensar los requisitos</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Repasa los cinco elementos del requisito y ten claro qué quieres hacer</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Think Before Coding</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2. Descomponer los requisitos</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Divide el requisito grande en pasos pequeños verificables por separado</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Simplicity First</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3. Escribir el PRD</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ordénalo en un documento estructurado para usarlo como referencia</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Goal-Driven</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">4. Configurar el archivo de memoria</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Crea CLAUDE.md o un archivo equivalente</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Harness Engineering</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">5. Implementar paso a paso</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Un paso por conversación: instrucción, verificación, siguiente</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Surgical Changes</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">6. Probar y verificar</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Al terminar cada paso, prueba enseguida que funciona correctamente</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Iterate &amp; Verify</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">7. Revisar el código</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Comprueba la arquitectura, la seguridad y la facilidad de mantenimiento</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Iterate &amp; Verify</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">8. Iterar y optimizar</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mejora iterando según los resultados de las pruebas y de la revisión</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Iterate &amp; Verify</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Lista de control del flujo práctico universal de la programación con IA

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Manos a la obra: termina el "proyecto uno" esta semana

{class="mt-1"}
Toma la "web de herramientas personales" de la sección 1 del capítulo 44 como tu primera tarea de programación con IA: dedica 5 minutos a los cinco elementos, manda la instrucción a la IA (cualquier herramienta vale) y haz la aceptación con la verificación de tres capas. Termínalo en 30 minutos y ya habrá nacido tu primera obra de programación con IA. Al acabar, guárdala bien: es el recuerdo de tu paso de "lector" a "practicante".
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumen del capítulo

- Proyecto uno (inicial): web de herramientas puramente frontend: vive el flujo completo, se acaba en 30 minutos
- Proyecto dos (intermedio): sistema de contabilidad full stack: PRD + archivo de memoria + 5 pasos, cada uno con algo "utilizable"
- Proyecto tres (avanzado): asistente de estudio con IA: usa la IA para escribir código que llama a la IA, con ojo en la ingeniería de prompts
- Ocho pasos del flujo universal: requisitos → descomposición → PRD → archivo de memoria → implementación paso a paso → pruebas → revisión → iteración
- En cada paso se repite el ciclo "instrucción, verificación, nueva conversación"
:::
