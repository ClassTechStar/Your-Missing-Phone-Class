---
id: di-wu-shi-san-zhang
num: 53
part: an-zhuo-kai-fa-pian
nav: Bab 53: Penyimpanan Data dan Permintaan Rangkaian
toc: default
kind: chapter
---

### Bab 53: Penyimpanan Data dan Permintaan Rangkaian

{class="chapter-intro mb-4"}
Aplikasi yang hanya boleh 'dilihat' ialah aplikasi mati; aplikasi yang boleh menyimpan data dan menyambung rangkaian barulah hidup. Bab ini memperkenalkan 'set tiga' lapisan data Android: DataStore (menyimpan konfigurasi kecil), Room (menyimpan data berstruktur), Retrofit (berbual dengan pelayan), ditambah 'penyelaras utama' mereka — korutin. Selepas bab ini, anda boleh menulis aplikasi sebenar yang mengingati tabiat pengguna dan mengemas kini kandungan secara masa nyata.

#### 1. Macam Mana Memilih Penyelesaian Penyimpanan: Lihat Jadual Ini Dahulu

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Penyelesaian</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Sesuai menyimpan apa</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ciri</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Diguna di mana dalam buku ini</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DataStore</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Konfigurasi berselerak (tema, suis)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pasangan kunci-nilai; mudah dan selamat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tetapan buku perakaunan Bab 54</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Data berstruktur (akaun, pengguna)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pembungkus pangkalan data SQLite sebenar, boleh buat pertanyaan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Rekod akaun Bab 54</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">(Tidak disimpan, diambil melalui rangkaian) data pelayan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Piawaian de facto pustaka permintaan HTTP</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Data cuaca Bab 55</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Pembahagian tugas set tiga data

Hafal satu rumus: 'konfigurasi kecil masuk DataStore, data berkelompok masuk Room, data luar guna Retrofit'. SharedPreferences yang kerap muncul dalam tutorial lama sudah digantikan oleh DataStore, dan penulisan SQL SQLite secara manual juga sudah digantikan oleh Room — belajar terus yang baharu, jangan ikut jalan lama.

#### 2. DataStore: Menyimpan Sedikit Konfigurasi Kecil

Mahu mengingati nilai berselerak seperti 'mata wang yang dipilih pengguna kali terakhir' atau 'mod gelap diaktifkan atau tidak', guna DataStore (versi Preferences):

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Contoh DataStore</span><span class="dots">···</span>
:::

```
val Context.dataStore by preferencesDataStore(name = "settings")

// Tulis: simpan satu nilai
suspend fun saveTheme(isDark: Boolean) {
    context.dataStore.edit { prefs ->
        prefs[THEME_KEY] = isDark
    }
}

// Baca: ambil nilainya (Flow memberitahu perubahan secara automatik)
val themeFlow: Flow<Boolean> = context.dataStore.data
    .map { it[THEME_KEY] ?: false }
```
:::

Perhatikan yang dipulangkan ialah Flow — satu aliran data yang 'mengalir'. Sebaik sahaja nilai berubah, semua tempat yang memerhatinya akan menerima nilai baharu secara automatik. Konsep ini (reaktif) ialah batu asas Android moden, akan dipraktikkan dalam Bab 54.

#### 3. Room: Memberi Data 'Rumah Sebenar'

Buku perakaunan ada ratusan hingga ribuan rekod, malah perlu pertanyaan dan statistik mengikut kategori dan bulan — ini memerlukan pangkalan data. Room ialah pembungkus rasmi SQLite, menjadikan 'membina jadual, membuat pertanyaan data' semula jadi seperti menulis Kotlin. Tiga benda:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Set tiga Room: Entity / Dao / Database</span><span class="dots">···</span>
:::

```
// 1. Entity: struktur jadual (satu jadual = satu data class)
@Entity(tableName = "records")
data class Record(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val amount: Double,
    val category: String,
    val note: String,
    val date: String
)

// 2. Dao: antara muka operasi data (tambah, padam, ubah, cari)
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

// 3. Database: pemasangan akhir
@Database(entities = [Record::class], version = 1)
abstract class AppDatabase : RoomDatabase() {
    abstract fun recordDao(): RecordDao
}
```
:::

Templat 'set tiga' ini boleh dipindahkan terus ke mana-mana projek anda — tukar nama medan sahaja. Pertanyaan memulangkan Flow, antara muka segar semula mengikut data secara automatik; nikmatnya tidak terkata.

#### 4. Retrofit: Berbual dengan Pelayan

Cuaca, berita, kadar pertukaran… data-data ini tiada dalam telefon, tetapi di pelayan orang lain. Retrofit menjadikan 'meminta data daripada pelayan' semudah memanggil fungsi. Tiga langkah:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Retrofit tiga langkah</span><span class="dots">···</span>
:::

```
// 1. Takrifkan antara muka: gambarkan permintaan HTTP sebagai fungsi
interface WeatherApi {
    @GET("v1/weather")
    suspend fun getWeather(@Query("city") city: String): WeatherResponse
}

// 2. Cipta instance
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
Amaran Perangkap: Dua Hukum Besi Rangkaian

{class="mt-1"}
① Permintaan rangkaian sama sekali tidak boleh dibuat pada utas utama — akan menyekat antara muka malah meranap (NetworkOnMainThreadException). Semua panggilan rangkaian mesti diletakkan dalam korutin (viewModelScope.launch). ② HTTP berjelas dilarang secara lalai: mulai Android 9, HTTPS diwajibkan. Semasa menguji jika perlu guna alamat tempatan http://, perlu mengisytiharkan usesCleartextTraffic secara jelas dalam Manifest — tetapi produk sebenar mesti sepenuhnya HTTPS.
:::

#### 5. Penghuraian JSON: 'Menterjemah' Data Rangkaian

Data yang dipulangkan pelayan kebanyakannya JSON — rentetan teks seperti 'kamus tersarang'. Retrofit memerlukan seorang 'penterjemah' untuk menukarkannya kepada objek Kotlin. Dua penyelesaian arus perdana 2026:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Penyelesaian</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ciri</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Senario disyorkan</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gson / Moshi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Penyelesaian refleksi veteran; kos sifar untuk konfigurasi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Projek kecil yang mahu bermula pantas, medan tidak banyak</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">kotlinx.serialization</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Penyelesaian semasa kompilasi rasmi; lebih pantas dan selamat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pilihan utama projek baharu (arus perdana 2026)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Dua penyelesaian penghuraian JSON

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Contoh kotlinx.serialization</span><span class="dots">···</span>
:::

```
// Tambah anotasi @Serializable pada data class
@Serializable
data class WeatherResponse(
    val weather: List<Weather>,
    val main: Main,
    val name: String
)

// Retrofit memasang Converter berkenaan (contoh dengan sokongan rasmi Retrofit 2.11+):
// .addConverterFactory(json.asConverterFactory("application/json".toMediaType()))
```
:::

Apa pun penyelesaiannya, hukum besinya ialah: lihat dahulu JSON sebenar yang dipulangkan, barulah takrifkan medan. Banyak pepijat 'penghuraian gagal' berpunca daripada nama medan tersilap atau tahap penyarangan tersalah jangka — cetak JSON mentah dan bandingkan; sepuluh saat dapat dikesan.

#### 6. Korutin: 'Bahasa Perantaraan' Keserentakan Android

suspend dan launch yang berulang di atas datang daripada korutin Kotlin (Coroutine) — penyelesaian keserentakan rasmi Android. Anda boleh memahaminya secara kasar: memastikan operasi yang 'perlu menunggu sebentar' (rangkaian, pangkalan data) tidak menyekat antara muka.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Pengenalan coroutine</span><span class="dots">···</span>
:::

```
// Memulakan coroutine dalam ViewModel
viewModelScope.launch {
    val records = dao.getAll().first()  // suspend: menunggu secara automatik tanpa menghalang
    // Kemas kini state paparan……
}

// Jembalitan kata kunci:
// suspend   —— "aku perlu tunggu, jangan halangi orang lain"
// launch    —— "Mula kerja!"
// viewModelScope —— "ruang kerja" yang mengikut halaman, berhenti sendiri apabila halaman dimusnahkan
```
:::

Untuk yang sifar asas, cukup ingat cara guna dahulu; prinsip 'gantung dan sambung semula' di sebaliknya boleh dikaji lebih dalam kemudian. 90% daripada apa yang anda tulis dalam pembangunan harian ialah templat ini.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mari cuba: Buat Aplikasi Kecil 'Satu Ayat Sehari'

{class="mt-1"}
Cari satu API petikan percuma (contohnya hitokoto dan seumpamanya), guna Retrofit untuk menarik 'satu ayat sehari', paparkan di tengah skrin, tambah butang 'Tukar ayat' (minta semula dalam korutin). Kemudian simpan ayat yang digemari ke dalam 'kegemaran' dengan Room. Latihan ini menggunakan DataStore/Room/Retrofit/korutin semuanya sekali habis — selepas menyiapkannya, Bab 7 dan 8 cuma makanan ringan.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan Bab

- Rumus: konfigurasi kecil masuk DataStore, data berkelompok masuk Room, data luar guna Retrofit
- DataStore memulangkan Flow: nilai berubah, pemerhati terus menerimanya secara automatik
- Set tiga Room: @Entity (jadual) + @Dao (operasi) + @Database (pemasangan akhir), templat boleh diguna semula terus
- Tiga langkah Retrofit: takrif antara muka → cipta contoh → panggil dalam korutin
- Dua hukum besi: rangkaian tidak masuk utas utama; produk sebenar mesti HTTPS
- Korutin = menunggu tanpa menyekat antara muka; viewModelScope ialah bengkel khusus halaman
:::
