---
id: di-si-shi-wu-zhang
num: 45
part: ai-biancheng-pian
nav: Capítulo 45: Garantía de calidad — que el código escrito por la IA sea fiable
toc: default
kind: chapter
---

### Capítulo 45: Garantía de calidad — que el código escrito por la IA sea fiable

{class="chapter-intro mb-4"}
El código escrito por la IA tiene un rasgo característico: suele "parecer correcto", con nombres de variables bien puestos, comentarios completos y lógica clara. Pero "parecer correcto" no es "ser correcto". Los problemas escondidos en el código de la IA suelen ser más difíciles de descubrir que en el escrito a mano, porque su calidad superficial es tan alta que invita a bajar la guardia. Este capítulo te enseña a montar un sistema eficaz de garantía de calidad para el código de la IA: con tres líneas de defensa (pruebas, revisión y control de versiones) pasaremos de "parece correcto" a "es correcto".

#### I. Guiado por pruebas: deja que la IA escriba las pruebas

Las pruebas son la primera línea de defensa de la calidad en la programación con IA. La buena noticia: pedirle a la IA que escriba pruebas es más fácil y más fiable que pedirle el código de la función, porque el comportamiento esperado de una prueba está bien definido y es raro que produzca algo que "parece correcto pero no lo es".

El flujo de la programación con IA guiada por pruebas es: primero pides a la IA el código de la función; cuando lo básico funciona, le pides enseguida los casos de prueba. Los casos de prueba deben cubrir el camino normal, los casos límite y las situaciones de error. Después, la IA corrige el código de la función según los resultados de las pruebas. La ventaja de este flujo: una vez escritas, las pruebas se convierten en una herramienta de verificación permanente: cualquier cambio posterior puede validarse ejecutándolas y confirmar que no se han colado regresiones.

::: div .code-block
:::inline div .code-head
<span>Instrucción para la IA: escribir tests</span><span class="dots">···</span>
:::

```
Escribe pruebas unitarias para la función calculate_discount.
Los casos de prueba deben cubrir:
1. Camino normal:
   - 100 yuan con 20 % de descuento -> 80
   - 200 yuan con 50 % de descuento -> 100
2. Casos límite:
   - 0 yuan con 20 % de descuento -> 0
   - 100 yuan sin descuento -> 100 (no hay rebaja)
   - 100 yuan a precio completo -> 100 (precio íntegro)
3. Casos de error:
   - precio negativo -> debe lanzar un error
   - descuento > 1 -> debe lanzar un error
   - entrada no numérica -> Debe lanzar un error
Usa el framework Vitest y dame el archivo de tests completo.
```
:::

Fíjate en los rasgos de esta instrucción: enumera de forma explícita los tres tipos de casos de prueba (normal, límite y error) y no deja a la IA margen para "elegir qué probar". A veces la IA solo escribe pruebas del camino feliz para "cumplir rápido"; listar todas las categorías evita ese problema.

#### II. Técnicas de revisión de código

Aunque haya pruebas, el código que produce la IA necesita también tu revisión humana. Revisar código no es leerlo línea por línea: sería lentísimo y dependería demasiado de tu nivel de programación. Una revisión eficaz del código de la IA debe fijarse en estas dimensiones clave:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Dimensión de revisión</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Qué observar</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Problemas habituales</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Seguridad</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Validación de entradas, manejo de claves, protección contra inyección SQL</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">La IA suele olvidar validar las entradas y escribe las claves dentro del código</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Manejo de errores</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Si se capturan las excepciones y si los mensajes de error son razonables</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">A la IA le gusta poner bloques catch vacíos o solo un console.log</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Rendimiento</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Si hay problemas de rendimiento evidentes, como consultas N+1 o bucles infinitos</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">A veces la IA escribe algoritmos en O(n²)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mantenibilidad</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Si la estructura del código es clara y los nombres significan algo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">De vez en cuando la IA genera código excesivamente abstracto</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gestión de dependencias</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Si las dependencias incorporadas son necesarias y las versiones están claras</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">La IA tiende a meter librerías innecesarias</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Dimensiones clave de la revisión del código de la IA

No tienes que comprobarlo todo tú mismo: puedes pedirle a la IA que haga la primera ronda de revisión. Una instrucción como: "revisa la seguridad, el manejo de errores y el rendimiento de este código y señala los posibles problemas". La capacidad de autorrevisión de la IA mejora sin parar; no sustituye del todo a la revisión humana, pero te filtra la mayoría de los problemas evidentes.

#### III. Control de versiones: el papel de Git en la programación con IA

En la programación con IA, Git importa todavía más que en la programación tradicional. Como cada cambio de la IA puede traer variaciones imprevisibles, necesitas un "remedio" fiable: el control de versiones es ese remedio.

La mejor práctica de Git en la programación con IA es "confirmar a menudo, avanzar en pasos pequeños". Cada vez que completes un punto de función verificable, haz un commit. Así, si un cambio de la IA sale mal, puedes volver con precisión al último estado utilizable sin tirar todo el trabajo por la borda.

Otro truco útil es el "aislamiento por ramas". Para los cambios de la IA con resultado incierto (por ejemplo, una gran refactorización), crea antes una rama nueva y trabaja en ella. Si el resultado convence, la fusionas con la rama principal; si no, la borras directamente, sin tocar la principal. Es mucho más seguro que estar retocando una y otra vez la rama principal.

1. Antes de cada cambio de la IA, asegúrate de que el área de trabajo está limpia (sin cambios sin confirmar). Así, si el cambio de la IA no convence, puedes revertir enseguida con git checkout .
2. Después de cada cambio de la IA, en cuanto pase la verificación, haz el commit de inmediato. El mensaje del commit describe qué hizo ese cambio, por ejemplo "feat: añadir la función de registro de usuarios".
3. Para las grandes refactorizaciones, crea primero una rama: git checkout -b refactor/auth-system. Termina los cambios en la rama y fusiona cuando las pruebas pasen.
4. Adquiere el hábito de mirar el diff. Tras cada cambio de la IA, usa git diff para ver qué cambió exactamente. Además de ayudarte a detectar problemas, te ayuda a aprender del código.

#### IV. Trampas frecuentes y guía para esquivarlas

En la programación con IA hay varias trampas que se repiten y en las que caen casi todos los principiantes. Saberlas de antemano te ahorrará muchos desvíos.

##### 1. Trampa uno: la trampa de la confianza

"El código de la IA parece tan profesional que seguro no falla, ¿no?": es la trampa más peligrosa. El código generado por la IA es impecable en apariencia: nombres correctos, comentarios completos, estructura clara; esa "sensación de profesionalidad" relaja la alerta. Pero lo pulido por fuera no garantiza la corrección de la lógica. Antídoto: valida siempre con pruebas y no juzgues por "si parece correcto".

##### 2. Trampa dos: la trampa del código hinchado

"Si la IA me escribe el código, ¿por qué no hacer las funciones bien completas?": eso acaba en código hinchado. A la IA le encanta "dar de más": le pides una página de inicio de sesión y te entrega un sistema completo de gestión de usuarios. Las funciones de más no solo añaden complejidad, sino también probabilidad de bugs. Antídoto: sigue a rajatabla el principio Simplicity First y dile a la IA con claridad "solo esta función, no añadas nada más".

##### 3. Trampa tres: la trampa de la comprensión

"La IA me entenderá, ¿no?": no necesariamente. Aunque la IA entiende muy bien, ante requisitos ambiguos sigue "adivinando". Y cuando adivina mal, el código que produce está mal. Peor aún: su código equivocado suele "parecer muy razonable" y te hace creer que te entendió. Antídoto: da en la instrucción suficientes detalles concretos para reducir el margen de adivinanza de la IA.

##### 4. Trampa cuatro: la trampa del contexto

"Ya lo dije en una conversación anterior, la IA se acordará, ¿no?": lo más probable es que no. A medida que la conversación se alarga o se abre una sesión nueva, la IA pierde el contexto inicial. Si una restricción clave no quedó escrita en el archivo de memoria del proyecto, es muy probable que la ignore en cambios posteriores. Antídoto: escribe las restricciones clave en el archivo de memoria del proyecto; no dependas de la memoria de la conversación.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Repaso rápido de las cuatro trampas

{class="mt-1"}
Trampa de la confianza: no te fíes de lo que "parece correcto"; trampa del hinchado: a la IA le encanta "dar de más"; trampa de la comprensión: ante requisitos ambiguos "adivina"; trampa del contexto: la memoria de la conversación "olvida". Los antídotos correspondientes: validar con pruebas, cortar lo superfluo, dar todos los detalles y escribirlo en el archivo de memoria.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Manos a la obra: levanta tres líneas de defensa en tu proyecto

{class="mt-1"}
Si ya empezaste el proyecto uno (la web de herramientas): ① pide a la IA que escriba los 3 tipos de casos de prueba para las funciones clave; ② revisa el código según las cinco dimensiones (seguridad, manejo de errores, rendimiento, mantenibilidad y dependencias); ③ inicializa el proyecto con git y haz el primer commit. Con las tres líneas de defensa en pie, tu proyecto será de verdad tuyo.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumen del capítulo

- El código de la IA "parece correcto" ≠ "es correcto": su calidad superficial tan alta invita a bajar la guardia
- Deja que la IA escriba las pruebas: lista de forma explícita los tres tipos de casos (normal, límite y error) para evitar las "pruebas selectivas"
- Cinco dimensiones de revisión: seguridad, manejo de errores, rendimiento, mantenibilidad y gestión de dependencias
- Git es el "remedio": confirmar a menudo, avanzar en pasos pequeños, aislar por ramas y mirar el diff siempre
- Cuatro trampas: confianza (validar con pruebas), hinchado (cortar lo superfluo), comprensión (dar todos los detalles) y contexto (escribirlo en el archivo de memoria)
:::
