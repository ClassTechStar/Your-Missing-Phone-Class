---
id: di-wu-shi-si-zhang
num: 54
part: an-zhuo-kai-fa-pian
nav: Capitolo 54: Progetto 1 — Il mio registro delle spese (versione locale)
toc: default
kind: chapter
---

### Capitolo 54: Progetto 1 — il mio registro delle spese (versione locale)

{class="chapter-intro mb-4"}
Benvenuto nel tuo primo «progetto serio». Questo registro delle spese, pur senza andare in rete, ha tutto l'occorrente: registra una voce, mostra i movimenti, fa i riepiloghi mensili, permette di cancellare e modificare. Completandolo avrai percorso per intero il flusso «dati → logica → interfaccia». Non avere fretta di copiare il codice — prima pensa bene, poi metti le mani: è il nostro principio di sempre.

#### 1. Pensare ai requisiti: prima poni cinque domande

Prima di iniziare, metti ordine nelle idee con i «cinque elementi dei requisiti»:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Elemento</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Risposta</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who (per chi è)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Per me; va benissimo anche per famiglia e amici</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What (cosa fa)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Registra entrate e uscite, mostra i movimenti, riepiloga per mese, statistiche per categoria</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why (perché)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Fare pratica + capire dove vanno a finire i soldi</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How (come)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin + Compose + Room + MVVM, tutto in locale senza backend</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint (vincoli)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pronto in una settimana; supporto minimo Android 8; anche se non si pubblica, si scrive con standard da pubblicazione</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
I cinque elementi dei requisiti del registro delle spese

Poi scompone il lavoro in piccoli passi, ciascuno «già utilizzabile»: ① crea il livello dati con Room (salva una voce); ② la schermata elenco (vedi i movimenti); ③ la schermata d'inserimento (aggiungi una voce); ④ cancella e modifica; ⑤ la scheda di riepilogo mensile. A ogni passo completato l'app resta un «oggetto che funziona».

#### 2. Il livello dati: dare alle «voci» una casa

Prima definisci com'è fatta una voce — campi sufficienti, senza ingolosirsi:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Record.kt (entità)</span><span class="dots">···</span>
:::

```
@Entity(tableName = "records")
data class Record(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val type: String,        // "income" entrata | "expense" uscita
    val amount: Double,      // importo (in yuan)
    val category: String,    // categoria: pasti, trasporti, stipendio…
    val note: String = "",   // nota (facoltativa)
    val date: String         // "2026-08-15"
)
```
:::

Nel Dao aggiungi due query «di statistica» — sono l'anima del registro delle spese:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · RecordDao.kt (query aggregate)</span><span class="dots">···</span>
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
    suspend fun monthIncome(month: String): Double   // month nella forma "2026-08"

    @Query("SELECT COALESCE(SUM(amount),0) FROM records WHERE type='expense' AND date LIKE :month || '%'")
    suspend fun monthExpense(month: String): Double
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Consiglio: perché l'importo è un Double?

{class="mt-1"}
Le app finanziarie rigorose usano BigDecimal o «un Int in centesimi» per evitare gli errori della virgola mobile (il vecchio problema 0,1+0,2≠0,3). Per un progetto di esercizio il Double basta; se un giorno fai un prodotto finanziario vero, ricordati di passare ai «centesimi» come unità — è una trappola su cui sono inciampati innumerevoli predecessori.
:::

#### 3. MVVM: interfaccia e logica «vanno a vivere separate»

Far operare l'interfaccia direttamente sul database? Funziona, ma il codice dell'interfaccia diventa lungo e intrattabile. L'architettura MVVM ripartisce i ruoli: la View (interfaccia) si occupa solo di disegnare, il ViewModel (centro della logica) dei dati, il Model (Room) dell'archiviazione.

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> View (interfaccia Compose)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> ViewModel (stato e logica)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-database mr-1"></i> Model (livello dati Room)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Figura 5: la struttura a tre livelli di MVVM — i dati fluiscono a senso unico, nessun livello invade gli altri
:::

::: div .code-block
:::inline div .code-head
<span>KOTLIN · RecordViewModel.kt (scheletro)</span><span class="dots">···</span>
:::

```
class RecordViewModel(private val dao: RecordDao) : ViewModel() {

    // Trasforma il Flow in uno stato osservabile dall'interfaccia
    val records = dao.getAll()
        .stateIn(viewModelScope, SharingStarted.WhileSubscribed(), emptyList())

    // Azioni dell'utente: chiama le funzioni suspend
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

Nell'interfaccia (Compose) si usa così: val vm: RecordViewModel = viewModel(), poi val list by vm.records.collectAsState() — appena i dati cambiano, l'elenco si aggiorna da solo e tu non muovi un dito. È la forza del tridente MVVM + Flow + Compose.

#### 4. L'interfaccia: schermata elenco + schermata d'inserimento

La schermata elenco usa LazyColumn (elenco a caricamento pigro) — qualunque sia la mole di dati non si inceppa:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Schermata elenco spese (brano essenziale)</span><span class="dots">···</span>
:::

```
@Composable
fun RecordListScreen(vm: RecordViewModel) {
    val records by vm.records.collectAsState()

    Column {
        // card riepilogo in alto (entrate - uscite = saldo)
        SummaryCard(records)

        // elenco movimenti
        LazyColumn {
            items(records, key = { it.id }) { record -&gt;
                RecordRow(record) { vm.deleteRecord(record) }
            }
        }

        // pulsante flottante "aggiungi voce" → apre la finestra di inserimento
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

Per l'inserimento la via più comoda è AlertDialog (finestra di dialogo): qualche campo di input + l'interruttore entrata/uscita + il menù a tendina delle categorie; al colpo su «Conferma» chiami vm.addRecord(...).

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Attenzione: con la validazione dell'input non essere pigro

{class="mt-1"}
Il campo dell'importo va validato sempre: valori vuoti, negativi, input illegale come "abc" — tutto va fermato (controlla con toDoubleOrNull()). Una delle cause più comuni di crash è «prendere l'input dell'utente per un bambino educato». Ricorda: tutto ciò che l'utente digita va ispezionato come se venisse da un nemico.
:::

#### 5. Modifica ed eliminazione: i dati devono «poter entrare e uscire»

Un registro che sa solo aggiungere e non cancellare si rovina in tre giorni. Aggiungi due operazioni:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Eliminare e modificare</span><span class="dots">···</span>
:::

```
// Aggiungi due metodi al Dao:
@Query("UPDATE records SET amount=:amount, category=:category, note=:note WHERE id=:id")
suspend fun update(id: Long, amount: Double, category: String, note: String)

@Query("DELETE FROM records WHERE id=:id")
suspend fun deleteById(id: Long)

// Nell'interfaccia: una pressione lunga sull'elemento apre il menu "modifica/elimina" (in Compose usa DropdownMenu o AlertDialog)
// Meglio mostrare una conferma prima di eliminare — l'eliminazione accidentale è ciò che gli utenti delle app di spese odiano di più
```
:::

Due regole d'esperienza sui dettagli d'interazione: l'eliminazione vuole una conferma in due tempi (per evitare tocchi di troppo), la modifica meglio se precompila i valori originali (correggere un carattere è più comodo che ridigitare tutto). Non sottovalutare questi dettagli — il «sapore di prodotto vero» è costruito proprio con dettagli così.

#### 6. Collaudo: tre livelli di controllo + due sfide avanzate

Finito il progetto, collauda su tre livelli «funzione → casi limite → architettura»: registra? cancella? riaprendo l'app i dati ci sono ancora? (funzione); crasha se l'importo è 0 o negativo? la rotazione dello schermo perde dati? (casi limite); interfaccia e dati sono mescolati? i campi sono scritti fissi nel codice? (architettura).

Superato il collaudo della versione base, aggiungiti due «portate avanzate»:

1. Filtro mensile: in cima aggiungi il cambio di mese (per esempio 2026-08 ▾) e l'elenco mostra solo i movimenti del mese in corso;
2. Grafico a torta per categoria: usa il Canvas di Compose o aggiungi una libreria di grafici leggera per disegnare «dove vanno a finire i soldi» in un grafico a torta — fatto questo, il registro comincia ad avere un «aspetto da prodotto».

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mani all'opera: finiscilo entro questa settimana

{class="mt-1"}
Lavora nell'ordine «livello dati → ViewModel → schermata elenco → schermata d'inserimento → scheda di riepilogo», un passo al giorno. Se ti blocchi, consegna l'errore così com'è al motore di ricerca o all'AI (ricordi la parte 7, «Coding con l'AI»? Quando descrivi il problema, chiarisci «comportamento atteso, comportamento reale, passi per riprodurlo»). Quando è pronto, tieni i conti per una settimana con lui — usare un'app fatta da te ti dà una spinta di orgoglio che ti porta avanti.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Riepilogo del capitolo

- Cinque elementi dei requisiti → scomposti in piccoli passi «ciascuno già utilizzabile», poi si mette mano al codice
- Livello dati: entità Record + Dao (con SQL di statistica mensile) + Database
- La divisione MVVM: la View disegna soltanto, il ViewModel tiene la logica, il Model tiene l'archivio
- Flow + stateIn + collectAsState: appena i dati cambiano, l'interfaccia si aggiorna da sola
- LazyColumn per l'elenco a caricamento pigro; AlertDialog per l'inserimento
- Collaudo a tre livelli (funzione/casi limite/architettura) + sfide avanzate (filtro mensile, grafico a torta per categoria)
:::
