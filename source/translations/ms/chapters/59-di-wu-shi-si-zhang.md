---
id: di-wu-shi-si-zhang
num: 54
part: an-zhuo-kai-fa-pian
nav: Bab 54: Projek 1—Buku Catatan Saya (Versi Setempat)
toc: default
kind: chapter
---

### Bab 54: Projek Satu — Buku Perakaunan Saya (Versi Tempatan)

{class="chapter-intro mb-4"}
Selamat datang ke 'projek serius' pertama anda. Walaupun buku perakaunan ini tidak berhubung rangkaian, ia lengkap dari segala segi: boleh mencatat rekod, melihat senarai transaksi, statistik mengikut bulan, memadam dan mengubah. Selepas menyiapkannya, anda telah melalui sepenuhnya aliran 'data → logik → antara muka'. Jangan terburu-buru menyalin kod — fikir dahulu dengan jelas barulah bertindak; itulah prinsip kita sepanjang buku ini.

#### 1. Pemikiran Keperluan: Tanya Lima Soalan Dahulu

Sebelum bertindak, gunakan 'lima elemen keperluan' untuk menyusun idea dengan jelas:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Elemen</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Jawapan</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who (untuk siapa)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Untuk guna sendiri, keluarga dan rakan pun boleh</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What (buat apa)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Catat pendapatan & perbelanjaan, lihat senarai transaksi, ringkasan bulanan, statistik ikut kategori</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why (kenapa)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Latihan praktik + tahu ke mana wang dibelanjakan</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How (macam mana)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin + Compose + Room + MVVM, sepenuhnya tempatan, tanpa backend</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint (kekangan)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Siap dalam tempoh seminggu; sokongan minimum Android 8; walaupun tidak akan diterbitkan, tulis ikut standard penerbitan dahulu</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Lima elemen keperluan buku perakaunan

Kemudian pecahkan kepada langkah kecil 'setiap langkah boleh guna': ① bina lapisan data Room (boleh simpan satu rekod); ② halaman senarai (boleh lihat transaksi); ③ halaman input (boleh tambah rekod); ④ padam dan sunting; ⑤ kad ringkasan bulanan. Setiap kali satu langkah siap, aplikasi sentiasa 'benda yang boleh guna'.

#### 2. Lapisan Data: Memberi 'Rekod' Sebuah Rumah

Takrifkan dahulu rupa satu rekod — medan cukup guna tetapi jangan tamak:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Record.kt (entity)</span><span class="dots">···</span>
:::

```
@Entity(tableName = "records")
data class Record(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val type: String,        // "income" pendapatan | "expense" perbelanjaan
    val amount: Double,      // Jumlah (yuan)
    val category: String,    // Kategori: makanan, pengangkutan, gaji……
    val note: String = "",   // Nota (pilihan)
    val date: String         // "2026-08-15"
)
```
:::

Tambah dua pertanyaan 'untuk statistik' dalam Dao — inilah jiwa buku perakaunan:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · RecordDao.kt (pertanyaan statistik)</span><span class="dots">···</span>
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
    suspend fun monthIncome(month: String): Double   // month berbentuk "2026-08"

    @Query("SELECT COALESCE(SUM(amount),0) FROM records WHERE type='expense' AND date LIKE :month || '%'")
    suspend fun monthExpense(month: String): Double
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Petua: Kenapa Jumlah Guna Double?

{class="mt-1"}
Aplikasi kewangan yang teliti akan guna BigDecimal atau 'Int dengan unit sen' untuk mengelakkan ralat titik terapung (masalah lama 0.1+0.2≠0.3). Projek latihan guna Double sudah memadai; jika suatu hari membina produk kewangan sebenar, ingat tukar kepada unit 'sen' — inilah perangkap yang dilanggar oleh ramai pendahulu.
:::

#### 3. MVVM: Antara Muka dan Logik Diasingkan

Terus biarkan antara muka mengendalikan pangkalan data? Boleh berjalan, tetapi kod antara muka akan bercokol dan panjang. Seni bina MVVM memastikan setiap satu menjalankan tugasnya: View (antara muka) hanya melukis, ViewModel (pusat logik) mengurus data, Model (Room) mengurus penyimpanan.

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> View (paparan Compose)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> ViewModel (state dan logik)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-database mr-1"></i> Model (lapisan data Room)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Rajah 5: Struktur tiga lapis MVVM — data mengalir satu hala, setiap lapis tidak melampaui bidangnya
:::

::: div .code-block
:::inline div .code-head
<span>KOTLIN · RecordViewModel.kt (rangka)</span><span class="dots">···</span>
:::

```
class RecordViewModel(private val dao: RecordDao) : ViewModel() {

    // Menukar Flow kepada state yang boleh diperhatikan paparan
    val records = dao.getAll()
        .stateIn(viewModelScope, SharingStarted.WhileSubscribed(), emptyList())

    // Tindakan pengguna: memanggil fungsi suspend
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

Guna begini dalam antara muka (Compose): val vm: RecordViewModel = viewModel(), kemudian val list by vm.records.collectAsState() — data berubah, senarai segar semula secara automatik, anda tidak perlu buat apa-apa. Inilah kuasa gabungan MVVM + Flow + Compose.

#### 4. Antara Muka: Halaman Senarai + Halaman Input

Halaman senarai guna LazyColumn (senarai muat malas) — data banyak macam mana pun tidak tersekat:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Halaman senarai rekod (petikan teras)</span><span class="dots">···</span>
:::

```
@Composable
fun RecordListScreen(vm: RecordViewModel) {
    val records by vm.records.collectAsState()

    Column {
        // Kad ringkasan di atas (pendapatan-perbelanjaan=baki)
        SummaryCard(records)

        // Senarai urus niaga
        LazyColumn {
            items(records, key = { it.id }) { record -&gt;
                RecordRow(record) { vm.deleteRecord(record) }
            }
        }

        // Butang terapung "Catat" → paparkan dialog input
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

Input guna AlertDialog (kotak dialog) paling mudah: beberapa kotak input + suis pendapatan/perbelanjaan + juntai bawah kategori, tekan OK maka panggil vm.addRecord(...).

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Perhatian: Jangan Malas Menyemak Input

{class="mt-1"}
Kotak input jumlah mesti disemak: nilai kosong, nombor negatif, input haram seperti "abc" semuanya mesti disekat (guna toDoubleOrNull() untuk menilai). Salah satu punca paling lazim aplikasi ranap ialah 'menganggap input pengguna budak baik'. Ingat: semua yang dimasukkan pengguna mesti diperiksa seperti musuh.
:::

#### 5. Sunting dan Padam: Buat Data 'Boleh Masuk Boleh Keluar'

Buku perakaunan yang hanya boleh tambah tetapi tidak boleh padam, tiga hari sudah terkudung. Tambah dua operasi:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Padam dan sunting</span><span class="dots">···</span>
:::

```
// Tambah dua fungsi dalam Dao:
@Query("UPDATE records SET amount=:amount, category=:category, note=:note WHERE id=:id")
suspend fun update(id: Long, amount: Double, category: String, note: String)

@Query("DELETE FROM records WHERE id=:id")
suspend fun deleteById(id: Long)

// Di skrin: tekan lama item senarai untuk papar menu "sunting/padam" (Compose guna DropdownMenu atau AlertDialog)
// Sebaiknya paparkan kotak pengesahan sebelum padam—"terpadam tersilap" ialah perkara paling dibenci pengguna aplikasi perakaunan
```
:::

Dua pengalaman dalam butiran interaksi: padam mesti ada pengesahan kali kedua (mengelakkan tersalah tekan), sunting sebolehnya praisi nilai asal (mengubah satu aksara lebih jimat daripada menaip semula). Jangan pandang rendah dua butiran ini — rasa 'produk' memang dibina daripada butiran begini.

#### 6. Penerimaan: Semakan Tiga Lapis + Dua Cabaran Lanjutan

Selepas projek siap, buat penerimaan mengikut tiga lapis 'fungsi → sempadan → seni bina': boleh catat atau tidak, boleh padam atau tidak, data masih ada atau tidak selepas membuka semula aplikasi (fungsi); adakah ranap apabila jumlah dimasukkan 0 atau negatif, adakah data hilang semasa skrin dipusing (sempadan); adakah antara muka dan data bercampur, adakah medan dikodkan keras (seni bina).

Selepas lulus penerimaan versi asas, tambahkan dua 'hidangan lanjutan' untuk diri sendiri:

1. Tapisan bulanan: tambah penukar bulan di bahagian atas (contohnya 2026-08 ▾), senarai hanya memaparkan transaksi bulan semasa;
2. Carta pai kategori: guna Canvas Compose atau bawa masuk pustaka carta ringan, lukiskan 'ke mana wang dibelanjakan' menjadi carta pai — selepas siap ini, buku perakaunan sudah ada sedikit 'rupa produk'.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mari cuba: Siapkan Minggu Ini

{class="mt-1"}
Bertindak mengikut urutan 'lapisan data → ViewModel → halaman senarai → halaman input → kad ringkasan', satu langkah sehari. Kalau tersangkut, campakkan ralat itu seadanya kepada enjin carian atau AI (masih ingat Bahagian 7 'Praktik Pengaturcaraan AI'? Semasa menghuraikan masalah, jelaskan 'tingkah laku dijangka, tingkah laku sebenar, langkah mengulangi'). Selepas siap, gunakannya mencatat perbelanjaan seminggu — menggunakan aplikasi buatan sendiri, rasa pencapaian akan mendorong anda terus mara.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan Bab

- Lima elemen keperluan → pecahkan kepada langkah kecil 'setiap langkah boleh guna', barulah bertindak
- Lapisan data: entiti Record + Dao (termasuk SQL statistik bulanan) + Database
- Pembahagian MVVM: View hanya melukis, ViewModel urus logik, Model urus penyimpanan
- Flow + stateIn + collectAsState: data berubah, antara muka segar semula secara automatik
- LazyColumn senarai muat malas; AlertDialog untuk input
- Penerimaan tiga lapis (fungsi/sempadan/seni bina) + cabaran lanjutan (tapisan bulanan, carta pai kategori)
:::
