---
id: di-liu-shi-yi-zhang
num: 61
part: ios-kai-fa-pian
nav: Capítulo 61: Iniciación rápida a Swift: el lenguaje principal del desarrollo Apple
toc: default
kind: chapter
---

### Capítulo 61: Iniciación rápida a Swift: el lenguaje principal del desarrollo Apple

{class="chapter-intro mb-4"}
En este capítulo empezamos en serio con el lenguaje. Sin agobios: Swift es famoso por ser "amable con los principiantes", y no necesitas memorizar el manual de sintaxis: dominando el 20% de la gramática entiendes y escribes el 80% del código del día a día; el resto lo consultarás mientras haces el proyecto. Recuerda nuestro principio de aprendizaje: entender > memorizar, saber usar > dominar.

#### 1. Variables y tipos: ponerle nombre a los datos

Un programa es "datos + lógica". Una variable es darle un nombre a un dato para guardarlo. En Swift se declaran con let y var:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Variables</span><span class="dots">···</span>
:::

```
let name = "Luis"        // let: constante (usa esta por defecto)
var age = 18             // var: variable (podrás cambiarla luego)

age = 19                 // <i class="fas fa-check-circle mr-1"></i> var sí se puede cambiar
// name = "María"         // <i class="fas fa-times-circle mr-1"></i> let no se puede cambiar: error de compilación

let score: Int = 100     // también se puede declarar el tipo explícitamente
let pi = 3.14            // si no lo escribes, se deduce automáticamente

print("Hola, \(name)")   // interpolación de cadenas: barra invertida + paréntesis
```
:::

Los tipos más usados, memorizados con una tabla:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Tipo</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Qué guarda</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ejemplo</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Int</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Enteros</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">42</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Double</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Decimales</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3.14</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">String</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Texto</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"Hola"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bool</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Verdadero/Falso</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">true / false</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">[Int] (array)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Una colección de datos</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">[1, 2, 3]</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Tipos básicos más usados de Swift

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Consejo: el principio de "let primero"

{class="mt-1"}
La regla de hierro de la comunidad Swift: usa let por defecto y var solo cuando de verdad haga falta. Si usas var donde bastaría let, Xcode te lo avisará con una advertencia amarilla. Este hábito te ahorra toda una familia de bugs de "variable modificada sin querer": cuanto menos cambia el código, más fácil es razonar sobre él.
:::

#### 2. Opcionales (Optional): el "amuleto anti caídas" de Swift

Es el concepto más importante de Swift, sin discusión. En una frase: cuando un valor puede "no existir", Swift te obliga a tratarlo, y así elimina a nivel de lenguaje la pesadilla gremial de los cierres por puntero nulo.

::: div .code-block
:::inline div .code-head
<span>SWIFT · Opcionales</span><span class="dots">···</span>
:::

```
var name: String = "Luis"   // tipo normal: nunca puede ser nil
// name = nil                // <i class="fas fa-times-circle mr-1"></i> error de compilación: te frena al instante

var nickname: String? = nil  // añade un signo ?: permite nil (opcional)
nickname = "Tommy"

// con opcionales hay que "desenvolverlos":
if let n = nickname {        // if let: desenvolvimiento seguro
    print("Hola, \(n)")
} else {
    print("Todavía no hay apodo")
}

let len = nickname?.count ?? 0   // ?? valor por defecto (operador de coalescencia)
print(len)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Atención: ¡! es una "operación de alto riesgo"

{class="mt-1"}
Escribir nickname! en el código (desenvoltura forzada) equivale a gritarle al compilador "te garantizo que no es nil"; si te equivocas, la App se cae al instante. Regla de novato: usa siempre if let / ?? y evita el !. A veces Xcode añade un ! de-propósito al autocompletar: acuérdate de quitarlo.
:::

#### 3. Funciones y closures: empaquetar la lógica en "botones"

Una función es un trozo de lógica con nombre, como un botón del mando a distancia. Un closure (cierre) es una "función sin nombre" que puedes pasarle a otro sobre la marcha:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Funciones y closures</span><span class="dots">···</span>
:::

```
// función: el nombre delante; parámetros y tipo de retorno detrás
func greet(name: String) -> String {
    return "¡Hola, \(name)!"
}
print(greet(name: "Luis"))     // al llamar, con el nombre del parámetro

// closure: se define en el sitio, ágil y directa
let numbers = [1, 2, 3, 4]
let doubled = numbers.map { $0 * 2 }   // $0 = el elemento actual
// [2, 4, 6, 8]

let big = numbers.filter { $0 > 2 }    // filtrar
// [3, 4]
```
:::

En SwiftUI los closures están por todas partes: las llaves tras Button("Púlsame") { ... } son un closure. Memoriza estos "combos de colecciones": map, filter y sorted; el 90% del procesamiento de listas del futuro será combinación de ellos.

#### 4. Estructuras y protocolos: el sistema "LEGO" de Swift

La preferencia oficial de Swift es clara: usa estructuras (struct) como primera opción y clases (class) solo cuando necesites herencia. Las estructuras son "tipos de valor": al copiarse, cada una va por su lado, y eso elimina de serie toda una clase de bugs:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Structs y protocolos</span><span class="dots">···</span>
:::

```
// el struct: la caja que guarda datos
struct Record {
    var id = UUID()
    var amount: Double
    var category: String
    var date: Date

    // el struct trae de serie su "memberwise initializer": se puede crear directamente
}
let r = Record(amount: 25.5, category: "comida", date: Date())

// protocolo: el contrato de "qué capacidades debe tener"
protocol Identifiable {
    var id: UUID { get }
}
struct Record: Identifiable { ... }   // adoptar el protocolo = comprometerse a cumplir sus requisitos
```
:::

En SwiftUI casi todo es un struct (View es un protocolo). No pasa nada si ahora no lo pillas: en el capítulo 62 lo verás todos los días. En el mundo de Swift, abraza primero el struct.

#### 5. Tarjeta de sintaxis de referencia para quienes empiezan de cero

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Qué quieres hacer</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Cómo se escribe</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Definir constantes/variables</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">let x = 1</code> / <code class="inline">var x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Interpolación de cadenas</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"Hola, \(name)"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Definir funciones</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">func nombre(parametro: Tipo) -> TipoDeRetorno { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Condicional</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if condicion { ... } else { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Recorrer (bucle)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">for x in array { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Desempaquetado seguro</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if let x = valorOpcional { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Valor por defecto</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">x ?? valorPorDefecto</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Definir structs</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">struct X { var a: Int; var b: String }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Closures</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">{ $0 * 2 }</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Tarjeta de referencia rápida de Swift (edición principiante)

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Manos a la obra: juega 15 minutos con Swift en Playgrounds

{class="mt-1"}
Si tienes Mac, abre Xcode → Playground; si no, usa Swift Playgrounds en el iPad o el playground web. Ejecuta cada bloque de código de este capítulo, cambia números y textos, y provoca unos errores a propósito para ver cómo te avisa Xcode. Estos 15 minutos de «primero jugar, luego aprender» te harán el doble de fácil arrancar en el capítulo 62.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumen del capítulo

- Prioriza let y usa var con cuidado; los tipos se infieren solos, aunque también puedes declararlos tras los dos puntos
- Los opcionales son el alma de Swift: lo que puede estar vacío hay que manejarlo; if let y ?? son tu amuleto, y ! es una operación de alto riesgo
- Las llamadas a funciones llevan el nombre de los parámetros; un closure es una función sin nombre, y en SwiftUI está por todas partes
- Prioriza struct y cumple protocolos; en SwiftUI casi todo es un struct
- Con el 20 % de la sintaxis haces el 80 % del trabajo: primero úsalo, después domínalo
:::
