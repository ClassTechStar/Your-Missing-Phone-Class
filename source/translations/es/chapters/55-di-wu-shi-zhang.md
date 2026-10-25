---
id: di-wu-shi-zhang
num: 50
part: an-zhuo-kai-fa-pian
nav: Capítulo 50: Kotlin de arranque rápido: el primer lenguaje del desarrollo Android
toc: default
kind: chapter
---

### Capítulo 50: Kotlin de arranque rápido: el primer lenguaje del desarrollo Android

{class="chapter-intro mb-4"}
En este capítulo nos ponemos en serio con el lenguaje. No te agobies: Kotlin tiene fama bien ganada de "amable con los principiantes" y no necesitas aprenderte el manual de sintaxis de memoria: dominando el 20 % de la sintaxis ya entiendes y escribes el 80 % del código de cada día. El resto se consulta sobre la marcha, mientras haces proyectos. Recuerda nuestro principio de estudio: entender > memorizar, saber usar > ser experto.

#### 1. Variables y tipos: poner nombre a los datos

Un programa es "datos + lógica". Una variable no es más que ponerle nombre a un dato y guardarlo. En Kotlin hay dos formas de declararla:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Variables</span><span class="dots">···</span>
:::

```
val name = "Luis"        // val: variable de solo lectura (usa esta por defecto)
var age = 18             // var: variable mutable (podrás cambiarla luego)

age = 19                 // <i class="fas fa-check-circle mr-1"></i> var sí se puede cambiar
// name = "María"         // <i class="fas fa-times-circle mr-1"></i> val no se puede cambiar: el compilador dará error

val score: Int = 100     // también se puede declarar el tipo explícitamente
val pi = 3.14            // si no lo escribes, se deduce automáticamente
```
:::

Los tipos más usados son solo unos pocos; apréndelos con esta tabla:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Tipo</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Qué guarda</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ejemplo</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Int</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Enteros</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">42</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Double</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Decimales</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3.14</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">String</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Texto</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"Hola"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Boolean</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Verdadero/falso</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">true / false</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">List&lt; T&gt;</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Un conjunto de datos</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">listOf(1, 2, 3)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Tipos básicos más usados de Kotlin

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Consejo: la regla de val primero

{class="mt-1"}
La ley de hierro de la comunidad de Kotlin: usa val por defecto y reserva var para cuando de verdad toque. Si usas var donde valía val, el IDE te lo avisará con letras amarillas. Este hábito te libra de toda una familia de bugs de "variable cambiada sin querer": cuanto menos cambia el código, más fácil es razonar sobre él.
:::

#### 2. Funciones: empaquetar la lógica en "botones"

Una función es un trozo de lógica con nombre, como un botón del mando a distancia: lo aprietas (la invocas) y se ejecuta una ristra de acciones. En Kotlin se declara con fun:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Funciones</span><span class="dots">···</span>
:::

```
fun greet(name: String): String {
    return "¡Hola, $name!"     // el símbolo $ inserta la variable en la cadena
}

println(greet("Luis"))        // salida: ¡Hola, Luis!

// las funciones de una línea se pueden escribir como expresión
fun add(a: Int, b: Int) = a + b

println(add(3, 5))            // salida: 8
```
:::

Algunos puntos clave: los parámetros van entre paréntesis (primero el nombre, luego el tipo, separados por dos puntos); el tipo de retorno se escribe después del paréntesis; y las plantillas de cadena $nombreVariable son la comodidad estrella de Kotlin: se acabó ir concatenando "cadena + variable" como en Java.

#### 3. Condicionales y bucles: que el programa "piense"

La "inteligencia" de un programa nace de dos cosas: saber decidir (if/when) y saber repetir (for/while).

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Condiciones y bucles</span><span class="dots">···</span>
:::

```
// condición: if / else
val age = 17
if (age >= 18) {
    println("Adulto")
} else {
    println("Menor de edad")
}

// varias ramas: when (cien veces mejor que switch)
val score = 85
val level = when {
    score >= 90 -> "Excelente"
    score >= 60 -> "Aprobado"
    else -> "¡Sigue así!"
}

// repetir: bucle for
val fruits = listOf("manzana", "plátano", "naranja")
for (fruit in fruits) {
    println("Me encanta comer $fruit")
}
```
:::

when es la forma más usada en Kotlin de escribir decisiones con varias ramas; en Android lo usarás a diario (por ejemplo, para mostrar una interfaz distinta según el estado).

#### 4. Seguridad frente a nulos: el "salvavidas" de Kotlin

El bug más famoso de la era Java se llama NullPointerException (excepción de puntero nulo): el programa toca algo "que no existe" y se viene abajo de golpe. Según las estadísticas, lleva años mandando en la lista de caídas de Android. Kotlin lo resuelve a nivel de lenguaje: por defecto no se permiten valores nulos.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Seguridad frente a null</span><span class="dots">···</span>
:::

```
var name: String = "Luis"   // tipo normal: nunca puede ser null
// name = null                // <i class="fas fa-times-circle mr-1"></i> error de compilación: te frena al instante

var nickname: String? = null // añade un signo ?: permite null
nickname = "Tommy"

// con tipos nullable hay que manejarlos con seguridad:
println(nickname?.length)    // llamada segura: si es null devuelve null, sin crash
val len = nickname?.length ?: 0   // operador Elvis: valor por defecto si es null
println(len)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Atención: no confundas ? con ?:

{class="mt-1"}
String? significa "puede ser nulo" y a ?: b significa "si a es nulo, usa b" (con ese peinado de Elvis que le sale, se llama operador Elvis). Cuando estés empezando, si el compilador te suelta un "error de null", lo más seguro es que hayas olvidado tratar un tipo nullable: el lenguaje te está protegiendo.
:::

#### 5. Clases y objetos: el molde para fabricar "piezas"

La clase es el "molde" de los objetos y el objeto, la "pieza salida del molde". Todo en Android (pantallas, botones, datos) son objetos. En Kotlin existe una joya llamada data class (clase de datos), hecha a posta para "llevar datos": una línea vale por decenas de Java:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Clases y data class</span><span class="dots">···</span>
:::

```
// clase normal: el molde
class Dog(val name: String) {
    fun bark() = println("$name: ¡guau!")
}

val dog = Dog("Rex")      // crea el objeto
dog.bark()                 // Rex: ¡guau!

// data class: la caja que guarda datos (con equals/copy etc. de serie)
data class User(val id: Int, val name: String, val email: String)

val me = User(1, "Luis", "zhangsan@example.com")
val twin = me.copy(name = "Luisa")   // copia y cambia un campo
```
:::

Cuando hagas tu app de gastos, cada movimiento será una data class: data class Record(val amount: Double, val category: String, val date: String). ¿Te das cuenta? Ya sabes escribir la estructura de código de un proyecto de verdad.

#### 6. Lambdas y funciones de orden superior: el "azúcar sintáctico" de Kotlin

En el código Android verás a diario esas "funciones sin nombre" con forma de { ... }; se llaman lambdas (funciones anónimas). El onClick = { count++ } de un Button es una lambda: empaqueta en un bloque "qué hacer al pulsar" y se lo entrega al botón.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Primer contacto con las lambda</span><span class="dots">···</span>
:::

```
// forma normal: defines una función con nombre y la pasas
fun double(x: Int) = x * 2
val result = listOf(1, 2, 3).map(::double)

// forma lambda: se define en el sitio, ágil y directa
val result2 = listOf(1, 2, 3).map { it * 2 }   // it = el elemento actual

// filtrar + transformar en cadena (súper común en proyectos reales)
val bills = listOf(12.5, 88.0, 5.0, 200.0)
val bigBills = bills.filter { it > 50 }.sorted()
// [88.0, 200.0]——"facturas de más de 50, ordenadas"
```
:::

Apúntate estos "combos" de colecciones de uso diario: filter (filtrar), map (transformar), sorted (ordenar) y sum (sumar). El 90 % del trabajo con listas que harás en el futuro es combinación de estas cuatro jugadas. La filosofía de Kotlin es: si una lógica se puede decir en una frase, jamás la escribas en cinco.

#### 7. Tarjeta de repaso rápido de sintaxis para quien parte de cero

No intentes memorizar toda la sintaxis en un día. Guarda esta tarjeta y consúltala mientras escribes código: en dos semanas te saldrá natural:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Qué quieres hacer</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Cómo se escribe</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Definir una variable de solo lectura</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">val x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Definir una variable modificable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">var x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Definir una función</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">fun nombre(parámetros): tipoDeRetorno { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Decidir</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if (condición) {...} else {...}</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Varias ramas</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">when { condición -> resultado }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Recorrer</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">for (x in lista) { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Unir cadenas</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"Hola, $name"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tratar nulos</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">x?.length ?: 0</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Definir una data class</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">data class X(val a: Int, val b: String)</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Tarjeta de repaso rápido de sintaxis de Kotlin (versión principiante)

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Manos a la obra: juega 10 minutos con Kotlin sin instalar nada

{class="mt-1"}
Abre en el navegador play.kotlinlang.org (el patio de juegos oficial de Kotlin), pega ahí cada trozo de código del capítulo y ejecútalo; cambia números y textos y mira cómo cambia la salida. Estos 10 minutos de "jugar antes de estudiar" harán que el capítulo 51 te cueste la mitad.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumen del capítulo

- val primero, var con cuentagotas; el tipo se puede inferir solo, aunque también puedes declararlo tras los dos puntos
- Función = lógica empaquetada; las plantillas de cadena con $ son la comodidad estrella
- if/when para decidir, for para repetir; when es el "todoterreno" del desarrollo Android
- La seguridad frente a nulos es el salvavidas de Kotlin: los tipos normales rechazan null y los nullable exigen tratarse con ? / ?:
- La data class es la caja donde se guardan datos: un campo por línea, y se usa todos los días en proyectos reales
- Con el 20 % de la sintaxis haces el 80 % del trabajo: primero saber usar, luego perfeccionar
:::
