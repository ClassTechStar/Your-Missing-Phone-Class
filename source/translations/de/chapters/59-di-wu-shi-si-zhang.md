---
id: di-wu-shi-si-zhang
num: 54
part: an-zhuo-kai-fa-pian
nav: Kapitel 54: Projekt 1 – mein Haushaltsbuch (Lokalversion)
toc: default
kind: chapter
---

### Kapitel 54: Projekt 1 – Mein Haushaltsbuch (Lokalversion)

{class="chapter-intro mb-4"}
Willkommen bei deinem ersten "richtigen Projekt". Dieses Haushaltsbuch geht zwar nicht ins Netz, aber es hat alles, was dazugehört: eine Buchung erfassen, den Verlauf ansehen, monatliche Auswertungen, Löschen und Ändern. Wenn du fertig bist, hast du den kompletten Ablauf "Daten → Logik → Oberfläche" einmal durchlaufen. Und: Nicht sofort den Code abschreiben – erst klar denken, dann anpacken. Das ist unser Prinzip von Anfang an.

#### 1. Über die Anforderungen nachdenken: erst fünf Fragen stellen

Bevor du loslegst, sortiere deine Idee mit den "fünf Anforderungsfragen":

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Frage</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Antwort</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who (für wen?)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Für dich selbst, auch für Familie und Freunde</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What (was?)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Einnahmen und Ausgaben erfassen, Verlauf ansehen, monatliche Summen, Auswertung nach Kategorien</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why (warum?)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Übung + herausfinden, wohin das Geld fließt</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How (wie?)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin + Compose + Room + MVVM, rein lokal ohne Backend</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint (Rahmenbedingung)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">In einer Woche fertig; mindestens Android 8 unterstützen; auch ohne Store-Veröffentlichung nach Store-Maßstab schreiben</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Die fünf Anforderungsfragen des Haushaltsbuchs

Dann zerlegst du es in kleine Schritte, von denen jeder einzeln "benutzbar" ist: ① Room-Datenschicht bauen (eine Buchung speichern können); ② Listenseite (Verlauf ansehen können); ③ Erfassungsseite (Buchung hinzufügen können); ④ Löschen und Bearbeiten; ⑤ Monats-Karte. Nach jedem Schritt ist die App ein "brauchbares Ding".

#### 2. Die Datenschicht: Den "Buchungen" ein Zuhause geben

Definiere zuerst, wie eine Buchung aussieht – die Felder sollen reichen, aber nicht gierig sein:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Record.kt (Entität)</span><span class="dots">···</span>
:::

```
@Entity(tableName = "records")
data class Record(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val type: String,        // "income" Einnahme | "expense" Ausgabe
    val amount: Double,      // Betrag (Yuan)
    val category: String,    // Kategorie: Essen, Verkehr, Gehalt …
    val note: String = "",   // Notiz (optional)
    val date: String         // "2026-08-15"
)
```
:::

In den Dao kommen zwei "Statistik-Abfragen" – sie sind die Seele des Haushaltsbuchs:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · RecordDao.kt (Statistik-Abfragen)</span><span class="dots">···</span>
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
    suspend fun monthIncome(month: String): Double   // month hat das Format "2026-08"

    @Query("SELECT COALESCE(SUM(amount),0) FROM records WHERE type='expense' AND date LIKE :month || '%'")
    suspend fun monthExpense(month: String): Double
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tipp: Warum Double für Beträge?

{class="mt-1"}
Seriöse Finanz-Apps nutzen BigDecimal oder "Int in Cent", um Rundungsfehler zu vermeiden (das alte Problem 0,1+0,2≠0,3). Für ein Übungsprojekt reicht Double völlig; baust du eines Tages ein echtes Finanzprodukt, rechne in Cent – eine Falle, in die unzählige Vorgänger getreten sind.
:::

#### 3. MVVM: Oberfläche und Logik ziehen getrennte Wege

Die Oberfläche direkt auf die Datenbank zugreifen lassen? Läuft zwar – aber der Oberflächen-Code wird lang und furchtbar. Die MVVM-Architektur lässt jeden seine Rolle spielen: View (Oberfläche) zeichnet nur, ViewModel (Logikzentrale) verwaltet die Daten, Model (Room) kümmert sich um die Speicherung.

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> View (Compose-Oberfläche)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> ViewModel (Zustand und Logik)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-database mr-1"></i> Model (Datenlayer mit Room)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Abbildung 5: Die drei MVVM-Schichten – Daten fließen in eine Richtung, keine Schicht greift über
:::

::: div .code-block
:::inline div .code-head
<span>KOTLIN · RecordViewModel.kt (Grundgerüst)</span><span class="dots">···</span>
:::

```
class RecordViewModel(private val dao: RecordDao) : ViewModel() {

    // wandelt den Flow in einen von der UI beobachtbaren Zustand
    val records = dao.getAll()
        .stateIn(viewModelScope, SharingStarted.WhileSubscribed(), emptyList())

    // Nutzeraktionen: suspend-Funktionen aufrufen
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

In der Oberfläche (Compose) so: val vm: RecordViewModel = viewModel(), dann val list by vm.records.collectAsState() – sobald sich die Daten ändern, aktualisiert sich die Liste von selbst, du musst nichts tun. Das ist die geballte Kraft von MVVM + Flow + Compose.

#### 4. Oberfläche: Listenseite + Erfassungsseite

Für die Listenseite nimm LazyColumn (träge ladende Liste) – selbst bei riesigen Datenmengen ruckelt nichts:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Ausgabenlisten-Ansicht (Kernauszug)</span><span class="dots">···</span>
:::

```
@Composable
fun RecordListScreen(vm: RecordViewModel) {
    val records by vm.records.collectAsState()

    Column {
        // oben die Zusammenfassungs-Karte (Einnahmen - Ausgaben = Saldo)
        SummaryCard(records)

        // Liste der Buchungen
        LazyColumn {
            items(records, key = { it.id }) { record -&gt;
                RecordRow(record) { vm.deleteRecord(record) }
            }
        }

        // schwebender Button "Ausgabe erfassen" → öffnet den Eingabedialog
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

Zum Erfassen ist ein AlertDialog am bequemsten: ein paar Eingabefelder + Umschalter Einnahme/Ausgabe + Kategorie-Dropdown, und bei "OK" rufst du vm.addRecord(...) auf.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Achtung: Bei der Eingabeprüfung nicht faulenzen

{class="mt-1"}
Das Betragsfeld musst du unbedingt prüfen: Leere Werte, Negativeingaben, "abc" und Ähnliches sind abzufangen (mit toDoubleOrNull() prüfen). Einer der häufigsten Gründe für App-Abstürze ist, "die Eingaben des Nutzers für brav zu halten". Merke: Behandle alles, was Nutzer eintippen, wie etwas, das du feindlich prüfen musst.
:::

#### 5. Bearbeiten und Löschen: Daten müssen "rein und raus" können

Ein Haushaltsbuch, das nur hinzufügen kann, ist nach drei Tagen unbrauchbar. Zwei Operationen noch:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Löschen und Bearbeiten</span><span class="dots">···</span>
:::

```
// zwei Methoden im Dao ergänzen:
@Query("UPDATE records SET amount=:amount, category=:category, note=:note WHERE id=:id")
suspend fun update(id: Long, amount: Double, category: String, note: String)

@Query("DELETE FROM records WHERE id=:id")
suspend fun deleteById(id: Long)

// in der Oberfläche: langes Tippen auf einen Eintrag öffnet das Menü "Bearbeiten/Löschen" (in Compose: DropdownMenu oder AlertDialog)
// vor dem Löschen besser einen Bestätigungsdialog: "versehentliches Löschen" ist, was Nutzer von Ausgaben-Apps am meisten hassen
```
:::

Zwei Erfahrungsregeln für die Bedienung: Beim Löschen immer eine zweite Bestätigung (gegen Versehen), beim Bearbeiten möglichst die Originalwerte voreintragen (ein Zeichen ändern ist leichter als alles neu tippen). Unterschätz diese Details nicht – "Produktgefühl" besteht genau aus solchen Details.

#### 6. Abnahme: drei Prüfebenen + zwei Fortgeschrittenen-Herausforderungen

Wenn das Projekt fertig ist, nimm die Abnahme in drei Ebenen vor: "Funktion → Grenzfälle → Architektur": Kannst du erfassen? Löschen? Sind die Daten nach einem Neustart noch da (Funktion)? Stürzt die App bei Betrag 0 oder negativ ab? Gehen bei einer Bildschirmdrehung Daten verloren (Grenzfälle)? Sind Oberfläche und Daten sauber getrennt, sind Felder hart kodiert (Architektur)?

Nach bestandener Basis-Abnahme gönn dir zwei "Fortgeschrittenen-Gerichte":

1. Monatsfilter: oben einen Monatswechsel ergänzen (z. B. 2026-08 ▾), die Liste zeigt nur den Verlauf des jeweiligen Monats;
2. Kreisdiagramm nach Kategorien: mit Composes Canvas oder einer leichten Chart-Bibliothek "wohin das Geld fließt" als Tortendiagramm zeichnen – danach sieht das Haushaltsbuch schon richtig nach Produkt aus.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Selbst ausprobieren: Diese Woche fertigstellen

{class="mt-1"}
Arbeite in der Reihenfolge "Datenschicht → ViewModel → Listenseite → Erfassungsseite → Auswertungskarte", jeden Tag ein Schritt. Wenn du festhängst, wirf die Fehlermeldung wörtlich in die Suchmaschine oder an eine KI (erinnerst du dich an Teil 7, "AI-Programmierung in der Praxis"? Beschreibe das Problem mit "erwartetes Verhalten, tatsächliches Verhalten, Schritte zur Reproduktion"). Wenn du fertig bist, führe eine Woche lang damit Buch – eine selbstgebaute App im eigenen Einsatz gibt dir Schwung für den weiteren Weg.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Zusammenfassung des Kapitels

- Fünf Anforderungsfragen → zerlegen in Schritte, von denen jeder einzeln funktioniert – dann loslegen
- Datenschicht: Record-Entity + Dao (inkl. SQL für Monatsstatistik) + Database
- MVVM-Arbeitsteilung: View zeichnet nur, ViewModel steuert die Logik, Model verwaltet die Speicherung
- Flow + stateIn + collectAsState: Daten ändern sich, die Oberfläche aktualisiert sich automatisch
- LazyColumn als träge ladende Liste; AlertDialog für die Erfassung
- Abnahme in drei Ebenen (Funktion/Grenzfälle/Architektur) + Zusatzaufgaben (Monatsfilter, Kreisdiagramm)
:::
