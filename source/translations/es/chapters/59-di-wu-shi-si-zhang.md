---
id: di-wu-shi-si-zhang
num: 54
part: an-zhuo-kai-fa-pian
nav: Capítulo 54: Proyecto 1: mi app de gastos (versión local)
toc: default
kind: chapter
---

### Capítulo 54: Proyecto 1: mi app de gastos (versión local)

{class="chapter-intro mb-4"}
Bienvenido a tu primer "proyecto en serio". Esta app de gastos no se conecta a internet, pero no le falta nada: anota movimientos, muestra el historial, resume por meses y permite borrar y editar. Al terminarla habrás recorrido el ciclo completo "datos → lógica → interfaz". No corras a copiar código: primero piensa y luego actúa; ese es nuestro principio de siempre.

#### 1. Pensar los requisitos: cinco preguntas primero

Antes de poner manos a la obra, ordena la idea con las "cinco preguntas del requisito":

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Elemento</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Respuesta</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who (¿para quién?)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Para ti; también vale familia y amigos</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What (¿qué hace?)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Anotar ingresos y gastos, ver el historial, resumir por mes y por categoría</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why (¿por qué?)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Practicar + enterarte de a dónde va el dinero</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How (¿cómo?)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin + Compose + Room + MVVM, todo local y sin backend</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint (¿con qué límites?)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Terminar en una semana; soportar como mínimo Android 8; escribir con estándar de tienda aunque no se publique</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Las cinco preguntas del requisito de la app de gastos

Luego divídela en pasos pequeños donde "cada uno se pueda usar": ① montar la capa de datos con Room (guardar un movimiento); ② la pantalla de lista (ver el historial); ③ la pantalla de registro (añadir movimientos); ④ borrar y editar; ⑤ la tarjeta de resumen mensual. Con cada paso terminado, la app sigue siendo algo "que se puede usar".

#### 2. La capa de datos: que cada "apunte" tenga casa

Primero define cómo es un apunte: los campos deben bastar, pero no pidas de más:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Record.kt (entidad)</span><span class="dots">···</span>
:::

```
@Entity(tableName = "records")
data class Record(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val type: String,        // "income" ingreso | "expense" gasto
    val amount: Double,      // importe (yuan)
    val category: String,    // categoría: comida, transporte, salario…
    val note: String = "",   // nota (opcional)
    val date: String         // "2026-08-15"
)
```
:::

Añade al Dao dos consultas "para estadísticas": son el alma de la app de gastos:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · RecordDao.kt (consultas de estadísticas)</span><span class="dots">···</span>
:::

```
@Dao
interface RecordDao {
    @Query("SELECT * FROM records ORDER BY date DESC, id DESC")
    fun getAll(): Flow&lt;List&lt;Record&gt;&gt;

    @Insert
    suspend fun insert(record: Record)

    @Delete
    suspend fun delete(record: Record)

    @Query("SELECT COALESCE(SUM(amount),0) FROM records WHERE type='income' AND date LIKE :month || '%'")
    suspend fun monthIncome(month: String): Double   // month tiene el formato "2026-08"

    @Query("SELECT COALESCE(SUM(amount),0) FROM records WHERE type='expense' AND date LIKE :month || '%'")
    suspend fun monthExpense(month: String): Double
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Consejo: ¿por qué Double para el importe?

{class="mt-1"}
Las apps financieras serias usan BigDecimal o "un Int en céntimos" para esquivar los errores de coma flotante (el viejo problema de que 0,1+0,2≠0,3). Para un proyecto de práctica basta Double; si algún día montas un producto financiero de verdad, recuerda pasar a céntimos: es una trampa que pisaron incontables predecesores.
:::

#### 3. MVVM: interfaz y lógica "se separan"

¿Dejar que la interfaz toque la base de datos directamente? Funciona, pero el código de interfaz se vuelve largo y farragoso. La arquitectura MVVM reparte papeles: View (interfaz) solo dibuja, ViewModel (centro de la lógica) lleva los datos y Model (Room) guarda.

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> Vista (interfaz Compose)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> ViewModel (estado y lógica)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-database mr-1"></i> Model (capa de datos Room)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figura 5: las tres capas de MVVM: los datos fluyen en una sola dirección y ninguna capa pisa el terreno ajeno
:::

::: div .code-block
:::inline div .code-head
<span>KOTLIN · RecordViewModel.kt (esqueleto)</span><span class="dots">···</span>
:::

```
class RecordViewModel(private val dao: RecordDao) : ViewModel() {

    // convierte el Flow en un estado observable por la interfaz
    val records = dao.getAll()
        .stateIn(viewModelScope, SharingStarted.WhileSubscribed(), emptyList())

    // acciones del usuario: llamar a funciones suspend
    fun addRecord(type: String, amount: Double, category: String, note: String, date: String) {
        viewModelScope.launch {
            dao.insert(Record(type = type, amount = amount,
                category = category, note = note, date = date))
        }
    }

    fun deleteRecord(record: Record) {
        viewModelScope.launch { dao.delete(record) }
    }
}
```
:::

En la interfaz (Compose) se usa así: val vm: RecordViewModel = viewModel() y luego val list by vm.records.collectAsState(): en cuanto cambian los datos, la lista se refresca sola y tú no tocas nada. Ese es el poder de la unión de MVVM + Flow + Compose.

#### 4. La interfaz: pantalla de lista + pantalla de registro

La lista usa LazyColumn (lista de carga diferida): por muchos datos que haya, sin tirones:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Pantalla de lista de gastos (fragmento clave)</span><span class="dots">···</span>
:::

```
@Composable
fun RecordListScreen(vm: RecordViewModel) {
    val records by vm.records.collectAsState()

    Column {
        // tarjeta de resumen superior (ingresos - gastos = balance)
        SummaryCard(records)

        // lista de movimientos
        LazyColumn {
            items(records, key = { it.id }) { record -&gt;
                RecordRow(record) { vm.deleteRecord(record) }
            }
        }

        // botón flotante "apuntar gasto" → abre el diálogo de alta
        FloatingActionButton(onClick = { showAddDialog = true }) {
            Text("+")
        }
    }
}

@Composable
fun RecordRow(record: Record, onDelete: () -&gt; Unit) {
    Row(Modifier.fillMaxWidth().padding(12.dp)) {
        Text(record.category, fontWeight = FontWeight.Bold)
        Spacer(Modifier.weight(1f))
        Text(if (record.type == "income") "+${record.amount}" else "-${record.amount}",
             color = if (record.type == "income") Color(0xFF27AE60) else Color(0xFFC0392B))
    }
}
```
:::

Para registrar, lo más cómodo es un AlertDialog (cuadro de diálogo): unos campos de texto + un conmutador ingreso/gasto + un desplegable de categorías; al pulsar aceptar se llama a vm.addRecord(...).

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Atención: con la validación de entradas no seas perezoso

{class="mt-1"}
El campo del importe hay que validarlo sí o sí: corta nulos, negativos y entradas ilegales como "abc" (compruébalo con toDoubleOrNull()). Una de las causas más comunes de caídas es "tratar la entrada del usuario como si fuera un niño modelo". Recuerda: todo lo que escriba el usuario, examínalo como a un enemigo.
:::

#### 5. Editar y borrar: que los datos "entren y salgan"

Una app de gastos que solo añade y no borra muere a los tres días. Añade dos operaciones:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Borrar y editar</span><span class="dots">···</span>
:::

```
// añade dos métodos al Dao:
@Query("UPDATE records SET amount=:amount, category=:category, note=:note WHERE id=:id")
suspend fun update(id: Long, amount: Double, category: String, note: String)

@Query("DELETE FROM records WHERE id=:id")
suspend fun deleteById(id: Long)

// en la interfaz: mantener pulsado un ítem abre el menú "editar/borrar" (en Compose, DropdownMenu o AlertDialog)
// antes de borrar, conviene un diálogo de confirmación: el "borrado por accidente" es lo que más odian los usuarios de apps de gastos
```
:::

Dos reglas de detalle en la interacción: el borrado exige una segunda confirmación (por si el dedo resbala) y la edición conviene que traiga el valor original precargado (corregir una letra es más barato que reescribirlo todo). No subestimes estos dos detalles: la sensación de producto se amontona justo ahí.

#### 6. La entrega: revisión en tres capas + dos retos avanzados

Terminado el proyecto, revisa en tres capas "función → límites → arquitectura": ¿anota? ¿borra? ¿al reabrir la app siguen los datos ahí? (función); ¿se cae si introduces 0 o un negativo? ¿pierde datos al girar la pantalla? (límites); ¿interfaz y datos están revueltos? ¿hay valores clavados en el código? (arquitectura).

Aprobada la versión básica, apúntate dos "platos avanzados":

1. Filtro por mes: añade arriba un selector de mes (por ejemplo, 2026-08 ▾) y que la lista muestre solo los movimientos de ese mes;
2. Gráfico circular por categoría: usa el Canvas de Compose o mete una biblioteca ligera de gráficos para pintar "a dónde fue el dinero" en forma de quesito; con esto hecho, la app de gastos empieza a tener cara de "producto".

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Manos a la obra: termínala esta semana

{class="mt-1"}
Trabaja en el orden "capa de datos → ViewModel → pantalla de lista → pantalla de registro → tarjeta de resumen", un paso cada día. Si te atascas, pega el error tal cual a un buscador o a una IA (¿recuerdas la parte séptima, "Programación con IA en la práctica"? Al describir el problema, deja claros "comportamiento esperado, comportamiento real y pasos para reproducirlo"). Cuando la acabes, úsala una semana para anotar tus gastos: el orgullo de usar una app hecha por ti te empuja a seguir adelante.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Resumen del capítulo

- Cinco preguntas del requisito → dividir en pasos pequeños "cada uno útil" y luego actuar
- Capa de datos: entidad Record + Dao (con SQL de estadísticas por mes) + Database
- Reparto MVVM: View solo dibuja, ViewModel lleva la lógica, Model guarda
- Flow + stateIn + collectAsState: cambian los datos y la interfaz se refresca sola
- LazyColumn para la lista de carga diferida; AlertDialog para registrar
- Entrega en tres capas (función/límites/arquitectura) + retos avanzados (filtro por mes, gráfico circular por categoría)
:::
