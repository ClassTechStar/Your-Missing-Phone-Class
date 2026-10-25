---
id: di-liu-shi-qi-zhang
num: 67
part: ios-kai-fa-pian
nav: Capítulo 67: Pulir y publicar — pruebas, depuración y salir en el App Store
toc: default
kind: chapter
---

### Capítulo 67: Pulir y publicar — pruebas, depuración y salir en el App Store

{class="chapter-intro mb-4"}
Ya tienes la app hecha, ¿y ahora qué? Este capítulo responde a las tres cosas que separan «funciona» de «se puede entregar»: cómo depurar con eficacia para cazar errores, cómo escribir pruebas para evitar regresiones y cómo subir la app al App Store para que la descargue el mundo entero. Publicar no es solo una ceremonia: es la línea que convierte una obra en producto.

#### 1. Las tres armas de la depuración: print, puntos de interrupción y vista previa

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Herramienta</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Para qué sirve</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Cómo se usa</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">print + consola</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ver los registros de ejecución</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Escribe print("valor=\(x)") en el código y mira la salida en la consola de abajo de Xcode</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Depuración con puntos de interrupción</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Detener el programa en una línea y ver el valor de las variables</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Toca junto al número de línea y sale un marcador azul; al llegar ahí la ejecución se detiene y puedes avanzar paso a paso</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Vista previa de SwiftUI + depurador</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ver la interfaz y la jerarquía de vistas en tiempo real</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lienzo de #Preview + inspector de View Hierarchy en ejecución</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Las tres armas de la depuración

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Consejo: ¿cómo se lee un cuelgue?

{class="mt-1"}
Cuando Swift se cuelga, la consola imprime "Fatal error" con su motivo y Xcode se detiene en la línea culpable y la resalta. Los cuelgues históricos en dispositivos reales se consultan en Xcode → Window → Organizer → Crashes (requiere cuenta de pago). Busca primero por «primera frase del motivo + swiftui»: solo una pregunta precisa tiene una respuesta precisa.
:::

#### 2. Pruebas: ponerle seguro al código

Probar a mano no es fiable: arreglas una función y otra se rompe a escondidas. Las pruebas son a la vez «la píldora del arrepentimiento» y «el chaleco antibalas». iOS usa el framework XCTest, con dos tipos:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Nivel</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Qué prueba</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Target</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Velocidad</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pruebas unitarias</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lógica pura (cálculos, validaciones)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstAppTests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Segundos</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pruebas de UI</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">El comportamiento real de la interfaz</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstAppUITests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Minutos</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pruebas manuales</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">La sensación y la experiencia de una persona real</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">——</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Siempre necesarias</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Niveles de pruebas en iOS (el proyecto plantilla ya trae dos Test Target)

::: div .code-block
:::inline div .code-head
<span>SWIFT · Ejemplo de prueba unitaria</span><span class="dots">···</span>
:::

```
import XCTest

// extrae a una función pura la lógica de "convertir el texto del importe en número"
func parseAmount(_ input: String) -> Double? {
    guard let v = Double(input.trimmingCharacters(in: .whitespaces)),
          v > 0 else { return nil }
    return v
}

final class AmountTests: XCTestCase {
    func testEmptyInputReturnsNil() {
        XCTAssertNil(parseAmount(""))
    }
    func testNegativeReturnsNil() {
        XCTAssertNil(parseAmount("-5"))
    }
    func testNormalValueParses() {
        XCTAssertEqual(parseAmount("12.5"), 12.5)
    }
}
```
:::

Ejecuta las pruebas con ⌘U. Con todo en verde, cambias código con tranquilidad. La validación de importes y los cálculos de resumen de la libreta merecen pruebas unitarias que los cuiden.

#### 3. Firma y empaquetado: ponerle «sello» a la app

Toda app de iOS debe estar firmada para poder instalarse: es la prueba de «este paquete viene de ti y no lo han alterado». La jerarquía:

- Fase de aprendizaje: un Apple ID gratuito + la firma automática de Xcode (Personal Team), que permite instalar en un dispositivo real y se renueva cada 7 días;
- Fase de distribución: una cuenta de desarrollador de pago (99 USD al año) emite certificados y perfiles, y solo así se publica y se instala a largo plazo.

Empaquetar: en el menú de Xcode, Product → Archive; cuando acabe la compilación, en Organizer elige Distribute App → selecciona App Store Connect → sube. El archivado debe hacerse con Generic iOS Device como destino (no el simulador): es el paso que los principiantes olvidan más.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Para evitar tropiezos: perder el certificado = dejar de poder actualizar

{class="mt-1"}
Si pierdes el certificado de firma y su clave privada, ya no podrás mandar actualizaciones de la app antigua: los usuarios solo podrán instalar una app «nueva». Haz copia de seguridad del certificado (expórtalo del llavero como .p12) y guarda bien la contraseña. Por suerte, Apple ofrece la «firma automática» y la gestión de certificados en la nube (marca Automatically manage signing en Xcode), que te ahorran la mayoría de las trampas manuales.
:::

#### 4. El proceso completo para salir en el App Store

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> Registrar cuenta de desarrollador</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-invoice mr-1"></i> Preparar material de la tienda</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-box mr-1"></i> Subir la compilación</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-clipboard-list mr-1"></i> Rellenar los datos de privacidad y revisión</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> Revisión de Apple (1-7 días)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-party-horn mr-1"></i> Publicar</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figura 5: los seis pasos para publicar en el App Store
:::

- Registro: developer.apple.com, cuenta personal a 99 USD al año;
- Material: icono (1024×1024, sin esquinas redondeadas: Apple lo recorta él solo), capturas (en los tamaños de iPhone), descripción y enlace a la política de privacidad;
- Cuestionario de privacidad: declara con verdad qué datos recoges; una libreta sin conexión puede declarar «no se recogen datos»;
- Revisión: el primer envío suele esperar de 1 a 7 días; si te rechazan, corrige punto por punto según las «notas de revisión»: los motivos de rechazo de Apple suelen venir escritos con todo detalle y basta con hacerles caso;
- TestFlight: antes de publicar, manda la versión de pruebas a tus amigos para las pruebas internas (hasta 10000 personas), recoge una ronda de comentarios y presenta oficialmente después: puro estilo profesional.

#### 5. Cómo hacer el material de la tienda: la primera impresión son las descargas

La página de la tienda es el escaparate que ve el usuario al «pasear por la tienda». Tres materiales deciden la primera impresión:

- Icono: 1024×1024, no te conformes con una captura. Si no tienes mano de diseñador, genera una figura sencilla con una herramienta de IA; solo aprueba si se reconoce de un vistazo incluso reducido en la pantalla de inicio;
- Capturas: al menos 2 juegos (en los tamaños de iPhone habituales) mostrando los escenarios más esenciales; en cada una, una frase en lenguaje humano («Anota un gasto en un segundo» vale diez veces más que «Una solución eficiente de contabilidad»);
- Descripción: la primera frase debe aclarar «qué es + para quién es»; no amontones «lo más profesional, lo más potente»: la sinceridad rinde más que la exageración.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Manos a la obra: «entrega» la libreta una vez

#### 6. Informes de cuelgues y una pequeña lista de rendimiento

Antes de publicar la app, estas dos cosas merecen media hora cada una:

##### 1. Vigilancia de cuelgues

Que no se cuelgue en tus pruebas no quiere decir que no se cuelgue en el teléfono de un usuario. Apple da informes de cuelgues gratuitos en Xcode Organizer (con cuenta de pago se ven los registros de dispositivos reales); una opción aún más cómoda es integrar un SDK de terceros (como Firebase Crashlytics). Publicar sin vigilancia de cuelgues es conducir con los ojos cerrados.

##### 2. Cuatro puntos de autochequeo del rendimiento

1. Listas con LazyVStack / List: no montes una lista larga con un VStack normal; la carga diferida es la primera lección de rendimiento;
2. No fuerces las imágenes originales: usa AsyncImage (imágenes remotas) y la caché del sistema; una imagen original de 5 MB basta para asfixiar a los modelos viejos;
3. No hagas trabajo pesado en el hilo principal: la red y los archivos grandes van con async/await;
4. Mide con Instruments: el analizador de rendimiento que trae Xcode (Time Profiler, chequeo de fugas de memoria): primero mide, luego optimiza, no vayas a corazonadas.

{class="mt-1"}
① Añade 3 pruebas unitarias a parseAmount y otras lógicas (que se pongan verdes con ⌘U); ② caza con un punto de interrupción un cuelgue provocado por ti mismo y arréglalo; ③ con Product → Archive genera un paquete y usa TestFlight para invitar a tus amigos a las pruebas internas; ④ si te sobran fuerzas, regístrate como desarrollador y presenta de verdad la libreta al App Store. Los tres primeros pasos puedes hacerlos esta misma noche.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumen del capítulo

- Las tres armas de la depuración: registros con print, puntos de interrupción, vista previa de SwiftUI e inspector de vistas
- XCTest: pruebas unitarias (⌘U) + pruebas de UI + pruebas manuales; la plantilla ya las trae
- Firma: la cuenta gratuita firma automática (renovación cada 7 días); solo la de pago permite distribuir
- Empaquetado: Generic iOS Device + Archive + Distribute; haz siempre copia del certificado
- Los seis pasos para publicar: registro → material → subida → cuestionario de privacidad → revisión → publicación; TestFlight primero, pruebas internas
:::
