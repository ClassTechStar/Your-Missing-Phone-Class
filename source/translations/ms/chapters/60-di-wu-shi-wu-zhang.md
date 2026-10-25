---
id: di-wu-shi-wu-zhang
num: 55
part: an-zhuo-kai-fa-pian
nav: Bab 55: Projek 2—App Semakan Cuaca (Versi Rangkaian)
toc: default
kind: chapter
---

### Bab 55: Projek Dua — Aplikasi Semakan Cuaca (Versi Rangkaian)

{class="chapter-intro mb-4"}
Buku perakaunan ialah 'melatih kungfu dalaman', aplikasi cuaca ialah 'melihat dunia luar' — ia perlu berurusan dengan internet. Dalam projek ini anda akan belajar: memohon API percuma, menghurai JSON, mengendalikan tiga keadaan antara muka 'sedang memuatkan/berjaya/gagal', serta cara menyembunyikan kunci API dengan baik. Selepas menyiapkannya, anda sudah memiliki kebolehan membina apa-apa 'aplikasi berhubung rangkaian' — berita, kadar pertukaran, terjemahan; caranya sama persis.

#### 1. Memohon API Cuaca Percuma

Untuk latihan peribadi, disyorkan OpenWeatherMap atau QWeather dari China — kedua-duanya ada kuota percuma, daftar sahaja terus boleh guna. Contoh dengan OpenWeatherMap:

1. Daftar akaun → jana satu Key (apikey) di halaman API keys;
2. Versi percuma boleh memanggil antara muka Current Weather (cuaca semasa): api.openweathermap.org/data/2.5/weather? q=beijing&appid=KeyAnda&units=metric;
3. Cuba sekali dahulu dalam pelayar, lihat rupa JSON yang dipulangkan — ini 'pra-belajar' yang wajib dilakukan sebelum menyambung apa-apa API.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Amaran Perangkap: Kunci Sama Sekali Jangan Ditulis Terus dalam Kod

{class="mt-1"}
API Key setara 'kata laluan dompet anda'; sekali ditulis dalam kod dan dimasukkan ke GitHub, dalam beberapa jam ia akan diimbas dan disalahgunakan oleh perayap. Cara betul: letakkan dalam local.properties (fail ini sudah diabaikan oleh gitignore), kemudian baca ke dalam kod melalui buildConfig Gradle. Cari 'amalan terbaik menyembunyikan API Key Android' dan ubah mengikut arahan.
:::

#### 2. Lapisan Rangkaian: Retrofit + Penghuraian JSON

Takrifkan dahulu 'model data' ikut JSON yang dipulangkan API; medan yang tidak sepadan abaikan sahaja:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Model data + antara muka</span><span class="dots">···</span>
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

Gson akan memasukkan JSON ke dalam data class ini secara automatik — nama medan sepadan, sihir berlaku sendiri.

#### 3. Tiga Keadaan Antara Muka: Memuatkan / Berjaya / Gagal

Jiwa aplikasi berhubung rangkaian terletak pada 'pengurusan keadaan'. Rangkaian perlahan, tiada rangkaian, nama bandar tersilap taip… setiap situasi antara muka mesti memberi penjelasan kepada pengguna. Guna satu sealed class (kelas termeterai) untuk mewakilinya dengan anggun:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · State paparan</span><span class="dots">···</span>
:::

```
sealed class UiState {
    object Loading : UiState()                    // sedang berpusing
    data class Success(val data: WeatherResponse) : UiState()  // berjaya
    data class Error(val message: String) : UiState()          // gagal
}

// Dalam ViewModel:
fun search(city: String) {
    viewModelScope.launch {
        _state.value = UiState.Loading
        _state.value = try {
            UiState.Success(api.getWeather(city))
        } catch (e: Exception) {
            UiState.Error("Bandar ini tidak dijumpai, cuba nama lain ya?")
        }
    }
}

// Dalam paparan:
when (val s = state) {
    is UiState.Loading -&gt; CircularProgressIndicator()   // berpusing
    is UiState.Success -&gt; WeatherContent(s.data)        // papar
    is UiState.Error -&gt; Text(s.message)                 // papar ralat
}
```
:::

Corak tiga bahagian Loading/Success/Error ini ialah 'templat serba guna' antara muka berhubung rangkaian; hafalkan dahulu, kelak semua aplikasi berhubung rangkaian tinggal menirunya.

#### 4. Kod Antara Muka Amali: Melukis Cuaca

Keadaan sudah ada, antara muka berbentuk begini (cekak utama):

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Paparan cuaca (petikan teras)</span><span class="dots">···</span>
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

Beberapa butiran kecil berbaloi dipelajari: firstOrNull() mengambil elemen pertama dengan selamat (senarai mungkin kosong), ?: "Tidak diketahui" memberi teks sandaran — prinsip keselamatan null turun terpakai dalam antara muka. Suhu guna saiz huruf besar 72.sp untuk mengisi ruang, berat fon 'Light' menjadikan nombor nampak anggun; inilah resipi klasik aplikasi jenis cuaca.

#### 5. Butiran Antara Muka dan Interaksi

- Kotak carian: TextField di bahagian atas, taip nama bandar dan tekan cari (tetapkan tindakan 'Cari' pada papan kekunci, tekan enter terus carian berjalan);
- Kad cuaca: suhu huruf besar (26.5°), huraian cuaca (Cerah), kelembapan, nama bandar;
- Bandar kegemaran: simpan bandar yang kerap dilihat ke dalam DataStore, buka lain kali terus disemak secara automatik — sambil itu ulangkaji Bab 6;
- Segar semula tarik ke bawah: dalam Compose guna PullToRefreshBox (disediakan Material 3), rasa sentuh terus terasa 'profesional'.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Petua: Imej Menghidupkan Antara Muka

{class="mt-1"}
Sediakan satu emoji atau ikon (☀️🌧️❄️) untuk setiap jenis cuaca, petakan dengan when(description) — tiga baris kod, rasa 'suasana' antara muka berlipat ganda. Boleh juga memuatkan pustaka ikon cuaca pihak ketiga, tetapi pada peringkat latihan emoji sudah memadai.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mari cuba: Senarai Semak Penerimaan Aplikasi Cuaca

{class="mt-1"}
① Carian biasa memaparkan cuaca; ② putuskan rangkaian, aplikasi memberi ralat dengan anggun tanpa ranap (hidupkan mod kapal terbang untuk menguji!); ③ masukkan bandar yang tidak wujud, mesej tetap mesra; ④ kegemarkan dua bandar, buka semula aplikasi masih ada; ⑤ pusing skrin, keadaan tidak hilang. Lima syarat lulus semua, projek ini barulah boleh bergraduat.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan Bab

- Cuba API dalam pelayar dahulu, fahami JSON, barulah tulis kod — 'pra-belajar' tidak pernah rugi
- API Key disembunyikan dalam local.properties, sama sekali tidak masuk repositori kod
- Antara muka Retrofit + data class: medan sepadan, JSON dihurai secara automatik
- Keadaan tiga bahagian Loading/Success/Error ialah penyelesaian serba guna antara muka berhubung rangkaian
- Tiada rangkaian, input kosong, bandar tidak wujud — pengendalian ralat ialah garis lulus aplikasi berhubung rangkaian
:::
