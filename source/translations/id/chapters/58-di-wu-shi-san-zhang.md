---
id: di-wu-shi-san-zhang
num: 53
part: an-zhuo-kai-fa-pian
nav: Bab 53: Penyimpanan Data dan Permintaan Jaringan
toc: default
kind: chapter
---

### Bab 53: Penyimpanan Data dan Permintaan Jaringan

{class="chapter-intro mb-4"}
Aplikasi yang hanya bisa 'dilihat' adalah aplikasi mati; aplikasi yang bisa menyimpan data dan tersambung ke internet barulah hidup. Bab ini memperkenalkan 'trio' lapisan data Android: DataStore (menyimpan konfigurasi kecil), Room (menyimpan data terstruktur), Retrofit (berbicara dengan server), plus 'pengatur jalannya semuanya'—coroutine. Selesai bab ini, kamu bisa menulis aplikasi sungguhan yang mengingat kebiasaan pengguna dan memperbarui konten secara real-time.

#### 1. Memilih Skema Penyimpanan: Lihat Tabel Ini Dulu

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Skema</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Cocok Menyimpan Apa</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ciri</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Dipakai di Mana di Buku Ini</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DataStore</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Konfigurasi kecil-kecil (tema, saklar)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pasangan kunci-nilai, sederhana dan aman</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pengaturan aplikasi catatan keuangan Bab 54</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Data terstruktur (catatan keuangan, pengguna)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pembungkus database SQLite sungguhan, bisa dikueri</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Catatan keuangan Bab 54</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Data server (tidak disimpan, diambil lewat jaringan)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Standar de facto pustaka permintaan HTTP</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Data cuaca Bab 55</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Pembagian tugas trio data

Hafalkan pegangan ini: 'konfigurasi kecil masuk DataStore, data dalam jumlah besar masuk Room, data dari luar lewat Retrofit'. SharedPreferences yang sering muncul di tutorial lama sudah digantikan DataStore, dan penulisan SQL manual juga sudah digantikan Room—belajar langsung yang baru, jangan lewat jalan lama.

#### 2. DataStore: Menyimpan Konfigurasi Kecil

Ingin mengingat nilai-nilai kecil seperti 'mata uang yang terakhir dipilih pengguna' atau 'apakah mode gelap diaktifkan'? Pakai DataStore (versi Preferences):

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Contoh DataStore</span><span class="dots">···</span>
:::

```
val Context.dataStore by preferencesDataStore(name = "settings")

// Tulis: simpan sebuah nilai
suspend fun saveTheme(isDark: Boolean) {
    context.dataStore.edit { prefs ->
        prefs[THEME_KEY] = isDark
    }
}

// Baca: ambil nilainya (Flow otomatis memberi tahu perubahan)
val themeFlow: Flow<Boolean> = context.dataStore.data
    .map { it[THEME_KEY] ?: false }
```
:::

Perhatikan yang dikembalikan adalah Flow—aliran data yang 'mengalir'. Begitu nilai berubah, semua tempat yang mengamatinya otomatis menerima nilai baru. Konsep ini (reaktif) adalah batu fondasi Android modern, akan dipraktikkan di Bab 54.

#### 3. Room: Memberi Data 'Rumah Sungguhan'

Aplikasi catatan keuangan punya ratusan hingga ribuan catatan, dan perlu kueri statistik per kategori, per bulan—ini butuh database. Room adalah pembungkus resmi SQLite, membuat 'membuat tabel, mengambil data' menjadi senatural menulis Kotlin. Ada tiga hal:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Trio Room: Entity / Dao / Database</span><span class="dots">···</span>
:::

```
// 1. Entity: struktur tabel (satu tabel = satu data class)
@Entity(tableName = "records")
data class Record(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val amount: Double,
    val category: String,
    val note: String,
    val date: String
)

// 2. Dao: antarmuka operasi data (tambah, hapus, ubah, cari)
@Dao
interface RecordDao {
    @Query("SELECT * FROM records ORDER BY date DESC")
    fun getAll(): Flow<List<Record>>

    @Insert
    suspend fun insert(record: Record)

    @Delete
    suspend fun delete(record: Record)

    @Query("SELECT SUM(amount) FROM records WHERE category = :c")
    suspend fun sumByCategory(c: String): Double
}

// 3. Database: perakitan akhir
@Database(entities = [Record::class], version = 1)
abstract class AppDatabase : RoomDatabase() {
    abstract fun recordDao(): RecordDao
}
```
:::

Templat 'trio' ini bisa dibawa apa adanya ke proyek mana pun—cukup ganti nama kolomnya. Kueri mengembalikan Flow, antarmuka otomatis menyegarkan mengikuti data. Nikmat sekali.

#### 4. Retrofit: Berbicara dengan Server

Cuaca, berita, nilai tukar... data-data itu tidak ada di ponsel, melainkan di server orang lain. Retrofit membuat 'meminta data ke server' semudah memanggil fungsi. Tiga langkah:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Retrofit tiga langkah</span><span class="dots">···</span>
:::

```
// 1. Definisikan antarmuka: deskripsikan permintaan HTTP sebagai fungsi
interface WeatherApi {
    @GET("v1/weather")
    suspend fun getWeather(@Query("city") city: String): WeatherResponse
}

// 2. Buat instance
val api = Retrofit.Builder()
    .baseUrl("https://api.example.com/")
    .addConverterFactory(GsonConverterFactory.create())
    .build()
    .create(WeatherApi::class.java)

// 3. Panggil seperti memanggil fungsi (di dalam coroutine)
val result = api.getWeather("Beijing")
```
:::

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Awas Jebakan: Dua Hukum Besi Jaringan

{class="mt-1"}
① Permintaan jaringan sama sekali tidak boleh dilakukan di thread utama—bisa membekukan antarmuka bahkan crash (NetworkOnMainThreadException). Semua panggilan jaringan wajib ditaruh dalam coroutine (viewModelScope.launch). ② HTTP teks terbuka dimatikan secara bawaan: sejak Android 9 wajib HTTPS. Saat pengujian kalau perlu alamat lokal http://, harus menyatakan usesCleartextTraffic secara eksplisit di Manifest—tetapi produk resmi wajib sepenuhnya HTTPS.
:::

#### 5. Parsing JSON: 'Menerjemahkan' Data Jaringan

Data yang dikembalikan server umumnya berupa JSON—rangkaian teks seperti 'kamus bersarang'. Retrofit butuh seorang 'penerjemah' untuk mengubahnya menjadi objek Kotlin. Dua skema arus utama di 2026:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Skema</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ciri</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Skenario yang Disarankan</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gson / Moshi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Skema refleksi veteran, tanpa biaya konfigurasi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Proyek kecil yang ingin cepat jalan dengan kolom tidak banyak</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">kotlinx.serialization</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Skema resmi saat kompilasi, lebih cepat dan lebih aman</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pilihan pertama proyek baru (arus utama 2026)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Dua skema parsing JSON

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Contoh kotlinx.serialization</span><span class="dots">···</span>
:::

```
// Tambahkan anotasi @Serializable ke data class
@Serializable
data class WeatherResponse(
    val weather: List<Weather>,
    val main: Main,
    val name: String
)

// Retrofit memasang Converter terkait (contoh dengan dukungan resmi Retrofit 2.11+):
// .addConverterFactory(json.asConverterFactory("application/json".toMediaType()))
```
:::

Apa pun skemanya, hukum besinya: lihat dulu JSON asli yang dikembalikan, baru definisikan kolomnya. Banyak bug 'parsing gagal' ternyata hanya karena nama kolom salah tulis atau level bersarang salah duga—cetak JSON mentahnya dan cocokkan, sepuluh detik langsung ketemu.

#### 6. Coroutine: 'Bahasa Umum' Konkurensi Android

suspend dan launch yang muncul berulang-ulang di atas berasal dari coroutine Kotlin (Coroutine)—skema konkurensi resmi Android. Bisa dipahami kasarnya: membuat operasi yang 'perlu menunggu sebentar' (jaringan, database) tidak memblokir antarmuka.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Perkenalan coroutine</span><span class="dots">···</span>
:::

```
// Menjalankan coroutine di ViewModel
viewModelScope.launch {
    val records = dao.getAll().first()  // suspend: otomatis menunggu tanpa menghambat
    // Perbarui state tampilan……
}

// Cara cepat ingat kata kunci:
// suspend   —— "aku perlu menunggu, jangan halangi yang lain"
// launch    —— "Mulai kerja!"
// viewModelScope —— "ruang kerja" yang mengikuti halaman, otomatis berhenti saat halaman dimusnahkan
```
:::

Kalau kamu pemula total, cukup ingat dulu cara pakainya; prinsip 'penangguhan dan pemulihan' di baliknya boleh digali belakangan. 90% dari yang kamu tulis dalam pengembangan harian adalah templat ini.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Praktik: Membuat Aplikasi Kecil 'Kalimat Hari Ini'

{class="mt-1"}
Cari API kutipan gratis (semacam hitokoto), pakai Retrofit untuk menarik 'kalimat hari ini', tampilkan di tengah layar, tambahkan tombol 'Ganti Kalimat' (minta ulang lewat coroutine). Lalu simpan kalimat yang disukai ke dalam 'koleksi' memakai Room. Latihan ini memakai DataStore/Room/Retrofit/coroutine semuanya—selesai mengerjakannya, Bab 7 dan 8 akan mudah seperti membalik telapak tangan.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan Bab Ini

- Pegangan: konfigurasi kecil masuk DataStore, data dalam jumlah besar masuk Room, data dari luar lewat Retrofit
- DataStore mengembalikan Flow: nilai berubah, pengamat otomatis menerima
- Trio Room: @Entity (tabel) + @Dao (operasi) + @Database (perakitan akhir), templat bisa dipakai ulang langsung
- Tiga langkah Retrofit: definisikan antarmuka → buat instance → panggil dalam coroutine
- Dua hukum besi: jaringan tidak masuk thread utama; produk resmi wajib HTTPS
- Coroutine = menunggu tanpa memblokir antarmuka; viewModelScope adalah ruang kerja khusus halaman
:::
