---
id: di-wu-shi-si-zhang
num: 54
part: an-zhuo-kai-fa-pian
nav: Bab 54: Proyek 1—Aplikasi Pembukuan Saya (Versi Lokal)
toc: default
kind: chapter
---

### Bab 54: Proyek 1—Aplikasi Catatan Keuangan Saya (Versi Lokal)

{class="chapter-intro mb-4"}
Selamat datang di 'proyek serius' pertamamu. Aplikasi catatan keuangan ini walau tidak terhubung internet, isinya lengkap: bisa mencatat pemasukan-pengeluaran, melihat riwayat, statistik per bulan, menghapus dan mengubah. Selesai mengerjakannya, kamu sudah menjalani alur lengkap 'data → logika → antarmuka'. Jangan buru-buru menyalin kode—pikirkan dulu baru bekerja, itu prinsip kita selama ini.

#### 1. Memikirkan Kebutuhan: Tanya Lima Pertanyaan Dulu

Sebelum mulai bekerja, gunakan 'lima unsur kebutuhan' untuk merapikan idemu:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Unsur</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Jawaban</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who (untuk siapa)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Untuk sendiri, boleh juga keluarga dan teman</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What (membuat apa)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mencatat pemasukan-pengeluaran, melihat riwayat, rekap per bulan, statistik per kategori</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why (kenapa)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Latihan + tahu uang habis ke mana</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How (bagaimana)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin + Compose + Room + MVVM, murni lokal tanpa backend</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint (batasan)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Selesai dalam seminggu; dukung minimal Android 8; walau tidak naik toko, tulis dengan standar naik toko</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Lima unsur kebutuhan aplikasi catatan keuangan

Lalu pecah menjadi langkah-langkah kecil yang 'setiap langkahnya bisa dipakai': ① bangun lapisan data Room (bisa menyimpan satu catatan); ② halaman daftar (bisa melihat riwayat); ③ halaman input (bisa menambah catatan); ④ hapus dan ubah; ⑤ kartu rekap bulanan. Setiap langkah selesai, aplikasinya selalu 'sesuatu yang bisa dipakai'.

#### 2. Lapisan Data: Memberi 'Catatan Keuangan' Sebuah Rumah

Pertama definisikan seperti apa bentuk satu catatan—kolomnya cukup untuk kebutuhan tapi jangan serakah:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Record.kt (entity)</span><span class="dots">···</span>
:::

```
@Entity(tableName = "records")
data class Record(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val type: String,        // "income" pemasukan | "expense" pengeluaran
    val amount: Double,      // Nominal (yuan)
    val category: String,    // Kategori: makan, transportasi, gaji……
    val note: String = "",   // Catatan (opsional)
    val date: String         // "2026-08-15"
)
```
:::

Di Dao tambahkan dua kueri 'untuk statistik'—inilah jiwa aplikasi catatan keuangan:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · RecordDao.kt (query statistik)</span><span class="dots">···</span>
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
Tips: Kenapa Nominalnya Pakai Double?

{class="mt-1"}
Aplikasi finansial yang serius akan memakai BigDecimal atau 'Int dengan satuan sen' untuk menghindari galat floating point (masalah lama 0.1+0.2≠0.3). Untuk proyek latihan, Double sudah cukup; kalau suatu hari membuat produk finansial sungguhan, ingat ganti dengan satuan 'sen'—jebakan yang sudah banyak dilewati para pendahulu.
:::

#### 3. MVVM: Antarmuka dan Logika 'Pisah Rumah'

Biar antarmuka langsung mengoperasikan database? Bisa jalan, tapi kode antarmukanya akan panjang lebar dan berantakan. Arsitektur MVVM membuat tiap pihak menjalankan tugasnya: View (antarmuka) hanya menggambar, ViewModel (pusat logika) mengurus data, Model (Room) mengurus penyimpanan.

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> View (tampilan Compose)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> ViewModel (state dan logika)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-database mr-1"></i> Model (lapisan data Room)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Gambar 5: Struktur tiga lapis MVVM—data mengalir satu arah, tiap lapis tidak melintasi batas
:::

::: div .code-block
:::inline div .code-head
<span>KOTLIN · RecordViewModel.kt (kerangka)</span><span class="dots">···</span>
:::

```
class RecordViewModel(private val dao: RecordDao) : ViewModel() {

    // Mengubah Flow menjadi state yang bisa diamati tampilan
    val records = dao.getAll()
        .stateIn(viewModelScope, SharingStarted.WhileSubscribed(), emptyList())

    // Aksi pengguna: memanggil fungsi suspend
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

Di antarmuka (Compose) dipakai begini: val vm: RecordViewModel = viewModel(), lalu val list by vm.records.collectAsState()—begitu data berubah, daftar otomatis menyegarkan, kamu tidak perlu berbuat apa-apa. Inilah kekuatan gabungan MVVM + Flow + Compose.

#### 4. Antarmuka: Halaman Daftar + Halaman Input

Halaman daftar memakai LazyColumn (daftar lazy-loading)—datanya sebanyak apa pun tidak akan patah-patah:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Halaman daftar pencatatan (potongan inti)</span><span class="dots">···</span>
:::

```
@Composable
fun RecordListScreen(vm: RecordViewModel) {
    val records by vm.records.collectAsState()

    Column {
        // Kartu rekap di atas (pemasukan-pengeluaran=saldo)
        SummaryCard(records)

        // Daftar mutasi
        LazyColumn {
            items(records, key = { it.id }) { record -&gt;
                RecordRow(record) { vm.deleteRecord(record) }
            }
        }

        // Tombol melayang "Catat" → memunculkan dialog input
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

Untuk input, paling praktis memakai AlertDialog (dialog): beberapa kolom input + saklar pemasukan/pengeluaran + dropdown kategori, tekan OK lalu panggil vm.addRecord(...).

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Perhatian: Jangan Malas Memvalidasi Input

{class="mt-1"}
Kolom input nominal wajib divalidasi: nilai kosong, angka negatif, input tak sah seperti 'abc' semuanya harus ditahan (pakai toDoubleOrNull() untuk memeriksa). Salah satu penyebab paling umum aplikasi crash adalah 'menganggap input pengguna selalu anak baik'. Ingat: semua input pengguna harus diperlakukan seperti musuh yang diperiksa.
:::

#### 5. Ubah dan Hapus: Agar Data 'Bisa Masuk Bisa Keluar'

Aplikasi catatan keuangan yang hanya bisa menambah tapi tidak bisa menghapus, tiga hari langsung tidak terpakai. Tambahkan dua operasi ini:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Hapus dan edit</span><span class="dots">···</span>
:::

```
// Tambahkan dua fungsi di Dao:
@Query("UPDATE records SET amount=:amount, category=:category, note=:note WHERE id=:id")
suspend fun update(id: Long, amount: Double, category: String, note: String)

@Query("DELETE FROM records WHERE id=:id")
suspend fun deleteById(id: Long)

// Di layar: tekan lama item daftar untuk memunculkan menu "edit/hapus" (Compose pakai DropdownMenu atau AlertDialog)
// Sebaiknya munculkan dialog konfirmasi sebelum menghapus—"terhapus tak sengaja" adalah hal paling dibenci pengguna aplikasi catatan keuangan
```
:::

Dua pengalaman soal detail interaksi: hapus wajib konfirmasi dua kali (mencegah jari selip), ubah sebisa mungkin sudah terisi nilai lama (mengubah satu kata lebih hemat daripada mengetik ulang). Jangan remehkan dua detail ini—rasa 'produk' memang ditumpuk dari detail-detail begini.

#### 6. Serah Terima: Pemeriksaan Tiga Lapis + Dua Tantangan Lanjutan

Setelah proyek selesai, lakukan serah terima tiga lapis 'fungsi → batas → arsitektur': bisa mencatat tidak, bisa menghapus tidak, data masih ada tidak setelah aplikasi dibuka ulang (fungsi); apakah crash saat nominal diisi 0 atau negatif, apakah data hilang saat layar diputar (batas); apakah antarmuka dan data tercampur, apakah ada kolom yang ditulis mati (arsitektur).

Setelah versi dasar lolos serah terima, beri dirimu dua 'hidangan lanjutan':

1. Filter bulanan: tambahkan sakelar bulan di bagian atas (misalnya 2026-08 ▾), daftar hanya menampilkan riwayat bulan itu;
2. Diagram lingkaran kategori: pakai Canvas milik Compose atau pustaka grafik ringan, gambar 'uang habis ke mana' sebagai diagram lingkaran—setelah jadi ini, aplikasi catatan keuanganmu mulai terasa seperti 'produk'.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Praktik: Selesaikan Minggu Ini

{class="mt-1"}
Bekerja dengan urutan 'lapisan data → ViewModel → halaman daftar → halaman input → kartu rekap', satu langkah per hari. Kalau macet, lempar errornya apa adanya ke mesin pencari atau AI (masih ingat Bagian 7 'Praktik Pemrograman AI'? Saat menjelaskan masalah, sebutkan dengan jelas 'perilaku yang diharapkan, perilaku nyata, langkah reproduksi'). Setelah selesai, pakai untuk mencatat keuangan selama seminggu—memakai aplikasi buatan sendiri, rasa bangganya akan mendorongmu terus melangkah.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan Bab Ini

- Lima unsur kebutuhan → pecah menjadi langkah kecil 'setiap langkah bisa dipakai', baru mulai bekerja
- Lapisan data: entitas Record + Dao (termasuk SQL statistik bulanan) + Database
- Pembagian tugas MVVM: View hanya menggambar, ViewModel mengurus logika, Model mengurus penyimpanan
- Flow + stateIn + collectAsState: begitu data berubah, antarmuka otomatis menyegarkan
- LazyColumn daftar lazy-loading; AlertDialog untuk input
- Serah terima tiga lapis (fungsi/batas/arsitektur) + tantangan lanjutan (filter bulanan, diagram lingkaran kategori)
:::
