---
id: di-liu-shi-er-zhang
num: 62
part: ios-kai-fa-pian
nav: Capítulo 62: Desarrollo de interfaces — introducción a SwiftUI
toc: default
kind: chapter
---

### Capítulo 62: Desarrollo de interfaces — introducción a SwiftUI

{class="chapter-intro mb-4"}
La interfaz es todo lo que el usuario ve. SwiftUI es el framework de interfaces declarativo que Apple lanzó en 2019: tú solo «declaras» cómo se ve la interfaz y el sistema se encarga solo de renderizarla, adaptarla al modo oscuro y ajustarla a cada pantalla. En 2026, SwiftUI es ya la opción dominante en los proyectos nuevos. En este capítulo aprenderemos a «dibujar».

#### 1. La filosofía de SwiftUI: declarativo, no imperativo

El desarrollo de interfaces de antes es «imperativo»: le ordenas al sistema paso a paso «crea un botón → ponlo en (20,30) → ponle color». SwiftUI es «declarativo»: describes directamente «en la interfaz hay un botón rojo que dice 'Tócame'», y el sistema se encarga de cómo dibujarlo y cuándo volver a dibujarlo.

::: div .code-block
:::inline div .code-head
<span>SWIFT · Primera vista SwiftUI</span><span class="dots">···</span>
:::

```
import SwiftUI

struct ContentView: View {
    var body: some View {      // body: describe "cómo es la interfaz"
        VStack {               // apilados en vertical
            Text("¡Hola, mundo!")
                .font(.largeTitle)      // modificador: título grande
            Button("Púlsame") {
                print("¡Pulsado!")
            }
            .buttonStyle(.borderedProminent)  // botón azul relleno
        }
        .padding()
    }
}
```
:::

Puntos clave: una vista = un struct que cumple el protocolo View; la propiedad body describe la interfaz; los .modificadores() se encadenan como quien se maquilla. Eso es todo el suelo firme de SwiftUI.

#### 2. Vistas básicas: texto, botones, campos de texto e imágenes

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Vista</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Para qué sirve</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ejemplo</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mostrar texto</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text("Hola")</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Botón</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button("Tócame") { acción }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Campo de texto</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField("Pista", text: $texto)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Image</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mostrar imágenes</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Image(systemName: "star.fill")</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Las cuatro vistas básicas de SwiftUI

Fíjate en Image(systemName:): Apple trae de serie la biblioteca de iconos SF Symbols (miles de iconos gratuitos); con un nombre como "star.fill" se muestra directamente una estrella rellena. Es una ventaja oculta de desarrollar en iOS: casi no necesitas buscar iconos para hacer interfaces.

#### 3. El trío de maquetación: VStack, HStack y ZStack

- VStack: apila en vertical (como hacer fila en la cantina);
- HStack: alinea en horizontal (como sentarse lado a lado);
- ZStack: superpone elementos (como cartas apiladas; ideal para insignias y capas).

::: div .code-block
:::inline div .code-head
<span>SWIFT · El trío de layouts + modificadores habituales</span><span class="dots">···</span>
:::

```
VStack(alignment: .leading, spacing: 12) {
    HStack {
        Text("Cuenta")
        Spacer()                 // espacio elástico: empuja lo de la derecha hasta el final
        Text("-25.5 yuan").foregroundColor(.red)
    }
    Divider()                    // separador
    Text("Nota: comida")
}
.padding(16)                     // margen en los cuatro lados
.background(Color(.systemGray6)) // fondo gris claro
.cornerRadius(12)                // esquinas redondeadas

// el orden de los modificadores importa: primero padding y luego background; el fondo no incluye el margen
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Ojo: el orden de los modificadores importa

{class="mt-1"}
padding(16).background(gris) y background(gris).padding(16) no dan el mismo resultado: el primero «primero deja el margen y luego pinta» (el fondo no incluye el margen) y el segundo «primero pinta y luego deja el margen» (el fondo incluye el margen). De ahí salen los «bordes blancos raros» más típicos de los principiantes. Si dudas, cambia el orden y la vista previa te dará la respuesta al instante.
:::

#### 4. Estado y binding: dar vida a la interfaz

Una interfaz estática es aburrida. La regla de SwiftUI: la interfaz refleja siempre fielmente el estado; si el estado cambia, la interfaz se redibuja sola.

::: div .code-block
:::inline div .code-head
<span>SWIFT · Contador con @State</span><span class="dots">···</span>
:::

```
struct CounterView: View {
    @State private var count = 0   // @State: si este valor cambia, hay que redibujar

    var body: some View {
        VStack {
            Text("Has pulsado \(count) veces")
            Button("Púlsame +1") {
                count += 1          // cambia el estado y la interfaz se actualiza sola
            }
        }
    }
}
```
:::

Los campos de texto usan «binding bidireccional»: el símbolo $ entrega a la vez «el valor y el derecho a modificarlo»:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Enlace bidireccional con @Binding</span><span class="dots">···</span>
:::

```
struct InputView: View {
    @State private var text = ""

    var body: some View {
        TextField("Escribe algo", text: $text)  // enlace bidireccional con $
            .textFieldStyle(.roundedBorder)
        Text("Has escrito: \(text)")   // se actualiza al instante mientras escribes
    }
}
```
:::

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hand-pointer mr-1"></i> Acción del usuario</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> Cambia el estado (count += 1)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> SwiftUI detecta el cambio</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> Redibuja la interfaz (se recalcula body)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figura 3: el flujo de datos en un solo sentido «estado → interfaz» de SwiftUI
:::

#### 5. Vista previa, tema y animación: los «extras» de SwiftUI

- Macro #Preview: añade #Preview { ContentView() } al final del archivo y el lienzo de la derecha renderiza en tiempo real: lo que ves es lo que obtienes mientras escribes código;
- Modo oscuro gratis: usa colores del sistema (Color(.systemGray6), .primary) en vez de colores fijos y el modo oscuro se adapta solo, sin escribir ni una línea más;
- Animación en una línea: withAnimation { count += 1 } o añade .animation(.default, value: count) a la vista: transiciones suaves.

::: div .code-block
:::inline div .code-head
<span>SWIFT · Animaciones en diez minutos</span><span class="dots">···</span>
:::

```
struct AnimatedHeartView: View {
    @State private var liked = false

    var body: some View {
        Button {
            withAnimation(.spring(duration: 0.4)) {
                liked.toggle()
            }
        } label: {
            Image(systemName: liked ? "heart.fill" : "heart")
                .font(.system(size: 48))
                .foregroundColor(liked ? .red : .gray)
                .scaleEffect(liked ? 1.3 : 1.0)
        }
    }
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Consejo: primero la función, luego la animación

{class="mt-1"}
El error típico del principiante es «afinar las animaciones cuando la interfaz todavía no funciona». Consigue primero que las funciones marchen y añade las animaciones al final: la animación es la guinda, la función es lo que salva del frío. Es nuestro principio de siempre: simplicidad ante todo.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Manos a la obra: crea un «botón de humor»

#### 6. Referencia rápida de modificadores: esta página a mano, la interfaz resuelta

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Qué quieres hacer</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Modificador</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Espaciado</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.padding(16)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Esquinas redondeadas</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.cornerRadius(12)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Color de fondo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.background(Color(.systemGray6))</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Fuente y tamaño</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.font(.title.bold())</code> / <code class="inline">.font(.system(size: 20))</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Color de primer plano (texto/iconos)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.foregroundColor(.red)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ocupar todo el ancho</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.frame(maxWidth: .infinity)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tamaño fijo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.frame(width:100, height: 44)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Alineación</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">VStack(alignment: .leading)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Opacidad</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.opacity(0.6)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sombra</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.shadow(radius: 5)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gesto de toque</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.onTapGesture { ... }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tipo de teclado</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.keyboardType(.decimalPad)</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Referencia rápida de los modificadores más usados de SwiftUI

No pasa nada si no los memorizas: esta página está para consultarla. Los cuatro que más se usan son los primeros: padding, esquinas redondeadas, fondo y fuente.

{class="mt-1"}
Convierte el proyecto plantilla en un cambiador de estados de ánimo: un botón que, al pulsarlo, va rotando entre 😀 feliz → 😢 triste → 😡 enfadado, cambiando el texto y el color de fondo. Pista: guarda los tres pares (texto + color) en un array, el índice en un @State y al pulsar usa (index + 1) % 3. Al acabarlo, envíaselo a tus amigos para presumir y recoge tu primera ola de «¡guau, sabes hacer apps!».
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumen del capítulo

- SwiftUI es declarativo: tú describes «cómo se ve» y el sistema dibuja y redibuja
- Vista = struct que cumple el protocolo View; body describe la interfaz; los modificadores se encadenan como maquillaje
- Las cuatro vistas básicas: Text / Button / TextField / Image; SF Symbols da iconos gratis de sobra
- El trío de maquetación: VStack en vertical, HStack en horizontal, ZStack superpone; Spacer es el espacio elástico
- @State da vida a la interfaz; $ alimenta el campo de texto con el binding bidireccional
- #Preview: lo que ves es lo que obtienes; los colores del sistema se adaptan al modo oscuro; withAnimation da efectos en una línea
:::
