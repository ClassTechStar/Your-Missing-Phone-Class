---
id: di-si-shi-zhang
num: 40
part: ai-biancheng-pian
nav: Capítulo 40: Ingeniería de requisitos: convertir ideas en instrucciones que la IA pueda ejecutar
toc: default
kind: chapter
---

### Capítulo 40: Ingeniería de requisitos: convertir ideas en instrucciones que la IA pueda ejecutar

{class="chapter-intro mb-4"}
Si la ingeniería de contexto resuelve «que la IA conozca el contexto», la ingeniería de requisitos resuelve «que la IA sepa qué hay que hacer exactamente esta vez». Es la etapa donde más se nota la diferencia entre personas en la programación con IA: con las mismas herramientas y los mismos modelos, hay quien logra proyectos impresionantes y quien solo consigue juguetes mediocres. La diferencia suele estar no en la capacidad técnica, sino en la capacidad de expresar los requisitos.

#### 1. De la idea vaga al requisito estructurado

Todo proyecto empieza con una idea vaga: «quiero hacer una app de gastos», «quiero una web personal», «quiero una herramienta de tareas pendientes». Las ideas en sí no tienen nada de malo, pero si se las lanzas directamente a la IA, la calidad del resultado depende por completo de la suerte. El objetivo de la ingeniería de requisitos es convertir esa idea vaga en un requisito estructurado que la IA pueda ejecutar con precisión.

La buena noticia: los requisitos estructurados no exigen escribir un PRD de decenas de páginas. Solo necesitas responder cinco preguntas, a las que llamamos «los cinco elementos del requisito»:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Elemento</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Pregunta</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ejemplo: app de gastos</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">¿Para quién es?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Uso personal, para registrar ingresos y gastos diarios</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">¿Qué hace?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Una aplicación que registre cada ingreso y gasto, los resuma por mes y los visualice</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">¿Por qué hacerla?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Quiero conocer mi estructura de gastos y detectar gastos innecesarios</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">¿Cómo hacerla, a grandes rasgos?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Frontend con React, datos guardados en el navegador; de momento sin backend ni inicio de sesión</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">¿Qué limitaciones hay?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Desarrollo en solitario, terminada en 2 semanas, sin necesidad de publicarla en producción</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Los cinco elementos del requisito, con ejemplos

Estos cinco elementos no hace falta convertirlos en un documento formal; basta con repasarlos rápidamente en la cabeza. La clave es adquirir el hábito de «pensarlo bien antes de hablar». Descubrirás que, cuando puedes responder con claridad estas cinco preguntas, tu descripción de requisitos se vuelve estructurada de forma natural.

#### 2. El arte de descomponer requisitos por niveles

En proyectos grandes, una sola descripción de requisitos no basta. Necesitas descomponer el requisito grande en subrequisitos pequeños que se puedan verificar por separado. Este proceso se llama «descomposición de requisitos» y su principio central es: cada subrequisito debe poder completarse, verificarse y entregarse de forma independiente.

Tomemos como ejemplo «hacer una app personal de gastos»; una forma razonable de descomponerla sería:

1. Implementar la función básica de registro de ingresos y gastos (añadir, ver y eliminar registros);
2. Añadir la función de categorías (etiquetar cada registro como comida, transporte, etc.);
3. Implementar el resumen mensual (estadísticas de ingresos y gastos mes a mes);
4. Añadir la visualización de datos (mostrar la estructura de gastos con gráficos).

Cada paso es un incremento de funcionalidad que puede ejecutarse y verificarse por separado.

:::inline div .quote-line
Regla de oro para trocear requisitos: al terminar cada paso, el proyecto debe ser "algo que se pueda usar", aunque las funciones sean toscas. No dejes nunca el proyecto en el estado de "todo a medias y nada funciona".
:::

Esta forma de descomponer tiene dos ventajas. Primera: te permite ver siempre el progreso; cada paso completado añade una función a tu app, y esa retroalimentación positiva es vital en los proyectos largos (todos necesitamos sentirnos realizados). Segunda: mantiene cada tarea de la IA lo bastante pequeña, lo que reduce el riesgo de «malentendidos de la IA»: cuanto más pequeña es la tarea, más precisa es su comprensión y mejor es la calidad del resultado.

#### 3. Plantilla y práctica para escribir un PRD

Para proyectos más grandes (por ejemplo, una aplicación full-stack con frontend, backend y varios módulos de funcionalidad), los cinco elementos del requisito pueden quedarse cortos. Entonces necesitas escribir un documento de requisitos del proyecto (PRD) más formal. Un punto que suele malinterpretarse: el PRD no está escrito para la IA; está escrito para ti. Te ayuda a aclarar tus ideas, y solo después podrás darle a la IA instrucciones más precisas.

Un buen PRD no tiene que ser largo, pero debe incluir seis partes: descripción general (un párrafo que aclare qué se va a hacer), lista de funciones (qué es cada punto de funcionalidad), plan técnico (qué stack y arquitectura aproximada se usará), modelo de datos (las estructuras de datos centrales), descripción de la interfaz (cómo son las páginas principales) y plan de desarrollo (en cuántos pasos se completará).

::: div .code-block
:::inline div .code-head
<span>PRD.md</span><span class="dots">···</span>
:::

```
# PRD de la app de control de gastos personal
## Descripción del proyecto
Una app ligera de control de gastos personales que permite registrar ingresos y gastos, categorizarlos, ver resúmenes mensuales y visualizar los datos.
## Lista de funciones
1. Registrar movimientos: importe, tipo (ingreso/gasto), categoría, nota, fecha
2. Gestión de categorías: precargadas comida, transporte, compras, ocio, otras
3. Resumen mensual: ingresos totales, gastos totales y balance por mes
4. Visualización del gasto: gráfico circular con la proporción de cada categoría
5. Exportación de datos: exportar a CSV
## Solución técnica
- Frontend: React + TypeScript + Tailwind CSS
- Almacenamiento: localStorage (sin backend)
- Gráficos: Chart.js
- Build: Vite
## Modelo de datos
Record {
  id: string
  amount: number
  type: 'income' | 'expense'
  category: string
  note: string
  date: string  // YYYY-MM-DD
}
## Plan de desarrollo
Step 1: registro básico de movimientos (CRUD)
Step 2: gestión de categorías
Step 3: resumen mensual
Step 4: visualización de datos
Step 5: exportación de datos
```
:::

Fíjate en el estilo de escritura de este PRD: listas concisas y formato estructurado, en lugar de discursos interminables. Cada punto de funcionalidad tiene una definición clara y el modelo de datos se describe con tipos sencillos. Un PRD con este estilo no solo lo entiendes tú con facilidad: cuando se lo das a la IA, también comprende con precisión cada punto del requisito.

#### 4. En la práctica: una demostración completa, de la idea al plan

Teorizar sin práctica es aburrido; vamos a recorrer todo el proceso de la ingeniería de requisitos con un ejemplo completo. Supongamos que tu idea es: «quiero hacer un rastreador de aprendizaje que registre qué estudio cada día».

Primer paso: repasar los cinco elementos del requisito.

- Who (quién): uso personal.
- What (qué): una herramienta que registre lo que estudias cada día, controle el tiempo de estudio y permita repasar tu progreso.
- Why (por qué): quiero crear el hábito de aprender continuamente y ver cómo se acumula lo aprendido.
- How (cómo): primero hago una versión web, con los datos guardados en el navegador.
- Constraint (restricción): desarrollo desde cero, funcionalidades centrales terminadas en 1 semana.

Segundo paso: descomponer los requisitos.

1. Paso 1: implementar la función «registrar entradas de estudio» (fecha, contenido, duración);
2. Paso 2: añadir las «estadísticas de tiempo de estudio» (hoy y acumulado semanal);
3. Paso 3: implementar la vista «calendario de estudio» (mostrada como el gráfico de contribuciones de GitHub);
4. Paso 4: añadir la función «repaso de estudio» (muestra al azar los registros de un día pasado para ayudarte a repasar).

Tercer paso: escribir un PRD breve. No hace falta que sea largo: la descomposición de arriba ya constituye el cuerpo del PRD. Organízalo en un archivo .md, colócalo en la raíz del proyecto y úsalo como referencia compartida entre tú y la IA.

Cuarto paso: empezar a desarrollar el primer paso. La instrucción para la IA podría ser:

::: div .code-block
:::inline div .code-head
<span>Instrucción para la IA</span><span class="dots">···</span>
:::

```
Necesito la primera función de un registrador de estudio: registrar sesiones de estudio.
El usuario puede añadir un registro con fecha, contenido estudiado y duración (minutos).
Los datos se guardan en localStorage.
Frontend con React + TypeScript.
Dame la implementación completa.
```
:::

Fíjate en las características de esta instrucción: describe solo el objetivo del paso actual (la función de registro), sin mezclar otras funciones; explicita las restricciones técnicas (React, TypeScript, localStorage); da la información suficiente para que la IA sepa «qué hacer» y «cómo abordarlo», pero deja la implementación concreta en manos de la IA. Esta es una instrucción de programación con IA de alta calidad, pulida mediante la ingeniería de requisitos.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Manos a la obra: escribe una ficha de cinco elementos para tu «proyecto favorito»

{class="mt-1"}
Elige un pequeño proyecto que llevas tiempo rumiando y dedica 5 minutos a rellenar una ficha: Who / What / Why / How / Constraint, una frase para cada uno. Después descomponla en 3 a 5 pasos en los que «cada paso sea utilizable». Descubrirás algo: al poner la idea por escrito, deja de ser un «sueño fantasioso» y se convierte en una «lista de tareas».
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumen del capítulo

- Los cinco elementos del requisito: Who / What / Why / How / Constraint; piénsalo bien antes de hablar
- Regla de oro para descomponer requisitos: al terminar cada paso, el proyecto es «algo que ya funciona»
- El PRD lo escribes para ti: descripción general, lista de funciones, plan técnico, modelo de datos, interfaz y plan de desarrollo
- Buena instrucción = describir solo el paso actual + restricciones claras + decir «qué hacer», no «cómo hacerlo»
- Plantilla del proceso completo: cinco elementos → descomposición → PRD → instrucción, en cuatro pasos
:::
