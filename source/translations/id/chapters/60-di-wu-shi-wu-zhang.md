---
id: di-wu-shi-wu-zhang
num: 55
part: an-zhuo-kai-fa-pian
nav: Bab 55: Proyek 2—App Cek Cuaca (Versi Jaringan)
toc: default
kind: chapter
---

### Bab 55: Proyek 2—Aplikasi Cek Cuaca (Versi Jaringan)

{class="chapter-intro mb-4"}
Aplikasi catatan keuangan melatih 'kekuatan dasar', aplikasi cuaca 'memperluas wawasan'—ia harus bergaul dengan internet. Di proyek ini kamu belajar: mendaftar API gratis, parsing JSON, menangani tiga keadaan antarmuka 'memuat/berhasil/gagal', serta cara menyembunyikan kunci API dengan baik. Setelah selesai, kamu punya kemampuan membuat aplikasi 'terhubung internet' apa pun—berita, nilai tukar, terjemahan, polanya persis sama.

#### 1. Mendaftar API Cuaca Gratis

Untuk latihan pribadi, disarankan OpenWeatherMap atau QWeather—keduanya punya kuota gratis, langsung bisa dipakai setelah mendaftar. Contoh dengan OpenWeatherMap:

1. Daftar akun → buat satu Key (apikey) di halaman API keys;
2. Versi gratis bisa memanggil antarmuka Current Weather (cuaca saat ini): api.openweathermap.org/data/2.5/weather? q=beijing&appid=KeyAnda&units=metric;
3. Coba dulu sekali di peramban, lihat seperti apa bentuk JSON yang dikembalikan—ini 'pralatihan' yang wajib dilakukan sebelum menyambung API apa pun.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Awas Jebakan: Kunci API Dilarang Keras Ditulis Langsung di Kode

{class="mt-1"}
API Key setara 'kata sandi dompet'-mu; begitu ditulis di kode dan dikomit ke GitHub, dalam beberapa jam akan diambil crawler dan disalahgunakan. Cara yang benar: taruh di local.properties (berkas ini sudah diabaikan oleh gitignore), lalu bacakan ke kode lewat buildConfig Gradle. Cari 'praktik terbaik menyembunyikan API Key di Android' dan ikuti petunjuknya.
:::

#### 2. Lapisan Jaringan: Retrofit + Parsing JSON

Pertama definisikan 'model data' sesuai JSON yang dikembalikan API; kolom yang tidak cocok abaikan saja:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Model data + antarmuka</span><span class="dots">···</span>
:::

```
// JSON: {"weather":[{"description":"Cerah"}],"main":{"temp":26.5,"humidity":40},"name":"Beijing"}
data class WeatherResponse(
    val weather: List&lt;Weather&gt;,
    val main: Main,
    val name: String
)
data class Weather(val description: String)
data class Main(val temp: Double, val humidity: Int)

interface WeatherApi {
    @GET("data/2.5/weather")
    suspend fun getWeather(
        @Query("q") city: String,
        @Query("appid") key: String,
        @Query("units") metric: String = "metric",
        @Query("lang") lang: String = "zh_cn"
    ): WeatherResponse
}
```
:::

Gson otomatis memasukkan JSON ke data class ini—nama kolomnya cocok, sihir terjadi sendiri.

#### 3. Tiga Keadaan Antarmuka: Memuat / Berhasil / Gagal

Jiwa aplikasi terhubung internet ada pada 'manajemen status'. Jaringan lambat, koneksi putus, nama kota salah ketik... setiap keadaan antarmukanya harus memberi kabar ke pengguna. Nyatakan dengan elegan memakai sealed class (kelas tertutup):

::: div .code-block
:::inline div .code-head
<span>KOTLIN · State tampilan</span><span class="dots">···</span>
:::

```
sealed class UiState {
    object Loading : UiState()                    // sedang berputar
    data class Success(val data: WeatherResponse) : UiState()  // sukses
    data class Error(val message: String) : UiState()          // gagal
}

// Di ViewModel:
fun search(city: String) {
    viewModelScope.launch {
        _state.value = UiState.Loading
        _state.value = try {
            UiState.Success(api.getWeather(city))
        } catch (e: Exception) {
            UiState.Error("Kota ini tidak ditemukan, coba nama lain ya?")
        }
    }
}

// Di tampilan:
when (val s = state) {
    is UiState.Loading -&gt; CircularProgressIndicator()   // berputar
    is UiState.Success -&gt; WeatherContent(s.data)        // tampilkan
    is UiState.Error -&gt; Text(s.message)                 // tampilkan error
}
```
:::

Pola tiga bagian Loading/Success/Error ini adalah 'templat serbaguna' antarmuka jaringan; hafalkan dulu, nanti semua aplikasi jaringan tinggal meniru polanya.

#### 4. Kode Antarmuka Praktis: Menggambar Cuaca

State-nya sudah ada, antarmukanya seperti ini (potongan kuncinya):

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Tampilan cuaca (potongan inti)</span><span class="dots">···</span>
:::

```
@Composable
fun WeatherContent(data: WeatherResponse) {
    Column(
        Modifier.fillMaxSize().padding(24.dp),
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Text(data.name, fontSize = 28.sp, fontWeight = FontWeight.Bold)
        Text(
            "${data.main.temp}°C",
            fontSize = 72.sp,
            fontWeight = FontWeight.Light
        )
        Text(
            data.weather.firstOrNull()?.description ?: "Tidak diketahui",
            fontSize = 20.sp,
            color = Color.Gray
        )
        Spacer(Modifier.height(16.dp))
        Row {
            Text("💧 Kelembapan ${data.main.humidity}%")
            Spacer(Modifier.width(24.dp))
            Text("🌡️ Terasa ${data.main.temp}°C")
        }
    }
}
```
:::

Beberapa detail kecil layak dipelajari: firstOrNull() mengambil elemen pertama dengan aman (daftarnya bisa kosong), ?: "Tidak diketahui" memberi teks cadangan—prinsip null safety juga berlaku di antarmuka. Suhu memakai ukuran huruf besar 72.sp agar menguasai tampilan, dan ketebalan 'Light' membuat angkanya terlihat elegan—ini resep klasik aplikasi cuaca.

#### 5. Detail Antarmuka dan Interaksi

- Kolom pencarian: TextField di bagian atas, ketik nama kota lalu tekan cari (atur aksi 'cari' di keyboard, tekan enter langsung mencari);
- Kartu cuaca: suhu huruf besar (26.5°), deskripsi cuaca (cerah), kelembapan, nama kota;
- Kota favorit: simpan kota yang sering dilihat ke DataStore, otomatis dicek saat dibuka berikutnya—sekalian mengulang Bab 6;
- Tarik untuk menyegarkan: di Compose pakai PullToRefreshBox (disediakan Material 3), rasanya langsung 'profesional'.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tips: Gambar Membuat Antarmuka Hidup

{class="mt-1"}
Beri satu emoji atau ikon untuk tiap jenis cuaca (☀️🌧️❄️), petakan dengan when(description)—tiga baris kode, kehangatan antarmuka berlipat. Bisa juga memuat pustaka ikon cuaca pihak ketiga, tapi di tahap latihan emoji sudah cukup.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Praktik: Daftar Periksa Serah Terima Aplikasi Cuaca

{class="mt-1"}
① Pencarian cuaca normal berhasil; ② putuskan jaringan, aplikasi memberi error dengan anggun tanpa crash (uji dengan mode pesawat!); ③ ketik kota yang tidak ada, pesannya ramah; ④ simpan dua kota favorit, buka ulang aplikasi masih ada; ⑤ putar layar tidak menghilangkan state. Lolos kelima-nya, proyek ini baru resmi lulus.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan Bab Ini

- Coba API di peramban dulu, pahami JSON-nya, baru tulis kode—'pralatihan' tidak pernah merugikan
- Sembunyikan API Key di local.properties, dilarang keras masuk repositori kode
- Antarmuka Retrofit + data class: kolomnya cocok, JSON terurai otomatis
- Keadaan tiga bagian Loading/Success/Error adalah obat serbaguna antarmuka jaringan
- Jaringan putus, input kosong, kota tidak ada—penanganan error adalah garis lulus aplikasi jaringan
:::
