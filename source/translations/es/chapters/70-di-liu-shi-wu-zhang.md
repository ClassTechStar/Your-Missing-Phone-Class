---
id: di-liu-shi-wu-zhang
num: 65
part: ios-kai-fa-pian
nav: Capítulo 65: Proyecto 1 — mi libreta de cuentas (versión local)
toc: default
kind: chapter
---

### Capítulo 65: Proyecto 1 — mi libreta de cuentas (versión local)

{class="chapter-intro mb-4"}
Bienvenido a tu primer «proyecto serio». Esta libreta de cuentas no se conecta a internet, pero tiene de todo: registra un gasto, muestra el historial, resume por mes y permite borrar y editar. Al terminarla habrás recorrido de principio a fin el flujo «datos → lógica → interfaz». No corras a copiar código: piensa primero y actúa después, como siempre.

#### 1. Pensar los requisitos: hazte cinco preguntas primero

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Elemento</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Respuesta</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who (¿para quién?)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Para ti; también vale para familia y amigos</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What (¿qué hace?)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Registrar ingresos y gastos, ver el historial, resumir por mes, estadísticas por categoría</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why (¿por qué?)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Practicar + averiguar en qué se va el dinero</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How (¿cómo?)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift + SwiftUI + SwiftData + MVVM, todo local y sin backend</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint (restricciones)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Terminarlo en una semana; soportar como mínimo iOS 17 (el requisito de SwiftData)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Los cinco elementos de los requisitos de la libreta de cuentas

Luego divídelo en pasos pequeños «cada uno utilizable por sí mismo»: ① crear la capa de datos con SwiftData (poder guardar un movimiento); ② la página de lista (ver el historial); ③ la ventana de registro (poder añadir); ④ borrar y editar; ⑤ la tarjeta del resumen mensual. Al completar cada paso, la app es algo «que se puede usar».

#### 2. La capa de datos: dar «casa» a los movimientos

Primero define cómo es un movimiento: que los campos alcancen, pero no te pases:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Record.swift (modelo)</span><span class="dots">···</span>
:::

```
import SwiftData

@Model
class Record {
    var type: String      // "income" ingreso | "expense" gasto
    var amount: Double    // importe (yuan)
    var category: String  // categoría: comida, transporte, salario…
    var note: String      // nota (opcional)
    var date: Date        // fecha del apunte

    init(type: String, amount: Double, category: String, note: String = "", date: Date = Date()) {
        self.type = type
        self.amount = amount
        self.category = category
        self.note = note
        self.date = date
    }
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Consejo: ¿por qué Double para el importe?

{class="mt-1"}
Una app financiera rigurosa usaría Decimal (decimales exactos) para evitar los errores de coma flotante (el viejo problema de 0,1+0,2≠0,3). Para un proyecto de práctica, Double basta; si algún día haces un producto financiero de verdad, acuérdate de cambiar a Decimal o a «un Int en céntimos»: es una trampa en la que han caído infinitas generaciones.
:::

#### 3. MVVM: interfaz y lógica «se separan»

¿Dejar que la interfaz maneje la base de datos directamente? Funciona, pero el código de la interfaz se vuelve largo e insoportable. La arquitectura MVVM reparte el trabajo: la View (interfaz) solo dibuja, el ViewModel (centro de la lógica) maneja los datos y el Model (SwiftData) guarda.

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> Vista (interfaz SwiftUI)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> ViewModel (centro de lógica @Observable)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-database mr-1"></i> Model (capa de datos SwiftData)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figura 4: la estructura de tres capas de MVVM — los datos fluyen en un solo sentido y cada capa respeta sus límites
:::

::: div .code-block
:::inline div .code-head
<span>SWIFT · RecordViewModel.swift (esqueleto)</span><span class="dots">···</span>
:::

```
import Observation

@Observable
class RecordViewModel {
    var records: [Record] = []
    private let context: ModelContext

    init(context: ModelContext) { self.context = context }

    func load() {
        // filtro con #Predicate de SwiftData + ordenación
        let descriptor = FetchDescriptor<Record>(
            sortBy: [SortDescriptor(\.date, order: .reverse)]
        )
        records = (try? context.fetch(descriptor)) ?? []
    }

    func add(type: String, amount: Double, category: String, note: String) {
        let r = Record(type: type, amount: amount, category: category, note: note)
        context.insert(r)
        try? context.save()
        load()                       // recarga; la interfaz se refresca
    }

    func delete(_ record: Record) {
        context.delete(record)
        try? context.save()
        load()
    }
}
```
:::

En la interfaz escribes @State private var vm = RecordViewModel(...) y renderizas la lista con vm.records directamente: en cuanto cambian los datos, la interfaz se refresca sola.

#### 4. La interfaz: página de lista + ventana de registro

::: div .code-block
:::inline div .code-head
<span>SWIFT · Pantalla de lista de gastos (fragmento clave)</span><span class="dots">···</span>
:::

```
struct RecordListView: View {
    @State private var vm: RecordViewModel
    @State private var showAdd = false

    var body: some View {
        NavigationStack {
            List {
                Section("Balance del mes") {          // tarjeta de resumen
                    SummaryRow(records: vm.records)
                }
                Section("Movimientos") {
                    ForEach(vm.records) { r in
                        RecordRow(record: r)
                    }
                    .onDelete { idx in
                        idx.forEach { vm.delete(vm.records[$0]) }
                    }
                }
            }
            .navigationTitle("Mi libro de cuentas")
            .toolbar {
                Button { showAdd = true } label: {
                    Image(systemName: "plus")
                }
            }
            .sheet(isPresented: $showAdd) {
                AddRecordView(vm: vm)          // diálogo de alta
            }
        }
    }
}
```
:::

Claves de la ventana de registro: para el importe, teclado .keyboardType(.decimalPad) (teclado numérico); para ingreso/gasto, un control segmentado (Picker); la categoría, con un menú; al pulsar «Guardar», llama a vm.add(...) y cierra con dismiss().

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Ojo: no seas perezoso con la validación

{class="mt-1"}
El campo del importe hay que validarlo sí o sí: valores vacíos, negativos o entradas ilegales como "abc" se bloquean (compruébalo con Double(text), que devuelve nil si falla). Una de las causas más comunes de que una app se cuelgue es «tomar la entrada del usuario por una niña bien». Recuerda: todo lo que escriba el usuario, revísalo como si fuera un enemigo.
:::

#### 5. Editar, borrar y resumir

- Borrar: .onDelete de List para deslizar y borrar + ventana de confirmación (borrar por equivocación es lo que más odian los usuarios de apps de cuentas);
- Editar: al tocar una fila se abre la ventana de edición con los valores ya puestos (corregir una letra es más cómodo que escribirlo todo de nuevo);
- Resumir: con filter + reduce calculas «ingresos / gastos / saldo del mes» y lo muestra la tarjeta de arriba:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Cálculo del resumen mensual</span><span class="dots">···</span>
:::

```
func monthSummary(_ records: [Record]) -> (income: Double, expense: Double) {
    let cal = Calendar.current
    let monthRecords = records.filter {
        cal.isDate($0.date, equalTo: Date(), toGranularity: .month)
    }
    let income = monthRecords
        .filter { $0.type == "income" }
        .reduce(0) { $0 + $1.amount }
    let expense = monthRecords
        .filter { $0.type == "expense" }
        .reduce(0) { $0 + $1.amount }
    return (income, expense)
}
```
:::

#### 6. Aceptación: tres capas de revisión + dos retos avanzados

Al acabar el proyecto, revísalo por tres capas «función → límites → arquitectura»: ¿se puede registrar y borrar?, ¿los datos siguen ahí al reiniciar la app? (función); ¿se cuelga al meter 0 o un número negativo en el importe? (límites); ¿la interfaz y los datos están revueltos?, ¿hay valores incrustados en el código? (arquitectura).

Cuando la versión básica pase la revisión, sírvete dos «platos avanzados»:

1. Estadísticas por categoría: añade una pestaña «Estadísticas» y usa Swift Charts para dibujar los gastos por categoría en gráfico de tarta o de barras: es la biblioteca oficial de Apple y con unas pocas líneas ya tienes el gráfico;
2. Sincronización con iCloud: activarla en SwiftData solo requiere configurar unos ajustes: la libreta se sincroniza sola entre iPhone e iPad y de golpe todo se ve «pro».

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Manos a la obra: termínala esta semana

{class="mt-1"}
Trabaja en el orden «capa de datos → ViewModel → página de lista → ventana de registro → tarjeta de resumen», un paso por día. Si te atascas, tira el mensaje de error tal cual al buscador o a la IA (¿recuerdas la séptima parte, «Práctica de programación con IA»? Al describir el problema, aclara «comportamiento esperado, comportamiento real y pasos para reproducirlo»). Al acabarla, úsala una semana para anotar gastos: usar una app hecha por ti mismo te empuja a seguir adelante.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumen del capítulo

- Los cinco elementos de los requisitos → dividirlos en pasos pequeños «cada uno utilizable» y luego ponerse manos a la obra
- Capa de datos: modelo con @Model + contenedor modelContainer + consultas con FetchDescriptor
- Reparto MVVM: la View solo dibuja, el ViewModel @Observable lleva la lógica y SwiftData guarda
- Interfaz: List + Section + toolbar + ventana de registro con sheet
- Revisión en tres capas (función/límites/arquitectura) + retos avanzados (Swift Charts, sincronización con iCloud)
:::
