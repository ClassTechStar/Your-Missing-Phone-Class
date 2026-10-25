---
id: di-liu-shi-liu-zhang
num: 66
part: ios-kai-fa-pian
nav: Bab 66: Proyek 2—App Cek Cuaca (Versi Jaringan)
toc: default
kind: chapter
---

### Bab 66: Proyek 2 — App Cek Cuaca (Versi Jaringan)

{class="chapter-intro mb-4"}
Buku catatan keuangan melatih "kungfu dasar", App cuaca "menambah wawasan" — ia harus bergaul dengan internet. Dari proyek ini kamu akan belajar: mengajukan API gratis, mengurai JSON, menangani tiga status antarmuka "memuat/berhasil/gagal", serta cara menyembunyikan kunci API dengan baik. Setelah menyelesaikannya, kamu memiliki kemampuan membuat "App online" apa pun — berita, nilai tukar, penerjemah; polanya persis sama.

#### 1. Mengajukan API Cuaca Gratis

Untuk latihan pribadi, direkomendasikan OpenWeatherMap atau QWeather (HeFeng Weather) asal Tiongkok — keduanya punya kuota gratis, langsung bisa dipakai setelah mendaftar. Contoh dengan OpenWeatherMap:

1. Daftar akun → buat sebuah Key (apikey) di halaman API keys;
2. Versi gratis dapat memanggil antarmuka Current Weather: api.openweathermap.org/data/2.5/weather? q=beijing&appid=KeyKamu&units=metric;
3. Coba dulu sekali di browser untuk melihat seperti apa JSON yang dikembalikan — ini "persiapan" yang wajib sebelum menghubungkan API apa pun.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Peringatan Jebakan: Kunci Jangan Pernah Ditulis Langsung di Kode

{class="mt-1"}
API Key setara "kata sandi dompetmu"; begitu ditulis dalam kode dan di-commit ke GitHub, dalam beberapa jam ia akan diambil crawler untuk disalahgunakan. Cara benar di iOS: taruh di Config.xcconfig (file konfigurasi, sudah diabaikan gitignore), lalu dibaca ke kode lewat Info.plist. Cari "iOS xcconfig manajemen kunci" dan ikuti langkah-langkahnya.
:::

#### 2. Lapisan Jaringan: URLSession + Codable

Definisikan model sesuai JSON yang dikembalikan API terlebih dahulu, baru tulis layanannya:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Model data + service</span><span class="dots">···</span>
:::

```
// JSON: {"weather":[{"description":"Cerah"}],"main":{"temp":26.5,"humidity":40},"name":"Beijing"}
struct WeatherResponse: Codable {
    let weather: [Weather]
    let main: Main
    let name: String
}
struct Weather: Codable { let description: String }
struct Main: Codable { let temp: Double; let humidity: Int }

struct WeatherService {
    let key: String   // Dibaca dari xcconfig

    func fetchWeather(city: String) async throws -> WeatherResponse {
        var comps = URLComponents(string: "https://api.openweathermap.org/data/2.5/weather")!
        comps.queryItems = [
            URLQueryItem(name: "q", value: city),
            URLQueryItem(name: "appid", value: key),
            URLQueryItem(name: "units", value: "metric"),
            URLQueryItem(name: "lang", value: "zh_cn")
        ]
        let (data, _) = try await URLSession.shared.data(from: comps.url!)
        return try JSONDecoder().decode(WeatherResponse.self, from: data)
    }
}
```
:::

#### 3. Tiga Status Antarmuka: Memuat / Berhasil / Gagal

Jiwa App online terletak pada "manajemen status". Jaringan lambat, koneksi putus, nama kota salah ketik… setiap kondisi harus dijelaskan antarmuka kepada pengguna. Nyatakan dengan elegan menggunakan enum + switch:

::: div .code-block
:::inline div .code-head
<span>SWIFT · State tampilan</span><span class="dots">···</span>
:::

```
enum LoadState {
    case loading                  // sedang berputar
    case success(WeatherResponse) // sukses
    case error(String)            // gagal
}

@Observable
class WeatherViewModel {
    var state: LoadState = .loading
    private let service = WeatherService(key: Config.apiKey)

    func search(city: String) async {
        state = .loading
        do {
            let data = try await service.fetchWeather(city: city)
            state = .success(data)
        } catch {
            state = .error("Kota ini tidak ditemukan, coba nama lain ya?")
        }
    }
}

// Di tampilan:
switch vm.state {
case .loading: ProgressView("Memuat…")
case .success(let d): WeatherContent(data: d)
case .error(let msg): Text(msg).foregroundColor(.secondary)
}
```
:::

Pola tiga bagian loading/success/error ini adalah "templat serbaguna" antarmuka online — hafalkan dulu, nanti semua App online tinggal meniru polanya.

#### 4. Kode Antarmuka Praktis: Menggambar Cuaca

::: div .code-block
:::inline div .code-head
<span>SWIFT · Tampilan cuaca (potongan inti)</span><span class="dots">···</span>
:::

```
struct WeatherContent: View {
    let data: WeatherResponse

    var body: some View {
        VStack(spacing: 12) {
            Text(data.name)
                .font(.title.bold())
            Text("\(Int(data.main.temp))°C")
                .font(.system(size: 76, weight: .thin))
            Text(data.weather.first?.description ?? "Tidak diketahui")
                .font(.title3)
                .foregroundColor(.secondary)
            HStack(spacing: 24) {
                Label("Kelembapan \(data.main.humidity)%", systemImage: "humidity")
                Label("Terasa \(Int(data.main.temp))°C", systemImage: "thermometer")
            }
        }
        .padding()
    }
}
```
:::

Beberapa detail kecil layak dipelajari: first? mengambil elemen pertama dengan aman (daftar bisa saja kosong), ?? "Tidak diketahui" memberi teks cadangan; angka suhu berukuran 76 dengan ketebalan tipis adalah resep klasik App cuaca; Label adalah komponen resmi "ikon + teks", lebih rapi daripada merangkai HStack manual.

#### 5. Detail Interaksi dan Kota Favorit

- Kolom pencarian: modifier .searchable di bagian atas memberi interaksi pencarian bawaan sistem; saat dikirim, panggil vm.search;
- Kota favorit: simpan kota yang sering dilihat ke UserDefaults, otomatis dicari saat dibuka berikutnya;
- Tarik untuk menyegarkan: .refreshable { await vm.search(...) } selesai dalam satu baris;
- Ikon cuaca: gunakan Image(systemName:) dengan pemetaan berdasarkan deskripsi (sun.max / cloud.rain / snowflake), antarmuka langsung terasa hidup.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tips: "Kejanggalan" Nama Kota Bahasa Mandarin

{class="mt-1"}
Dukungan OpenWeatherMap untuk nama kota dalam bahasa Mandarin biasa-biasa saja; mencari "Beijing" bisa tanpa hasil sementara "beijing" normal. Untuk produk sungguhan, caranya menyertakan tabel pemetaan "nama kota → Inggris/koordinat" atau menghubungkan layanan cuaca lokal Tiongkok. Di tahap latihan, cukup dukung nama kota pinyin/Inggris — jangan dipersulit.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Praktik: Daftar Periksa Penerimaan App Cuaca

#### 6. Cara Debug Permintaan Jaringan: Print, Packet Sniffing, dan Simulasi Jaringan Lambat

Saat App online bermasalah, sembilan dari sepuluh kali penyebabnya "permintaan tidak dikirim dengan benar" atau "respons tidak diurai dengan benar". Tiga alat debug:

1. Cetak data mentah: print String(data: data, encoding: .utf8) untuk melihat JSON mentah — nama field dan tipe terlihat sekilas jelas, sepuluh kali lebih cepat daripada menebak;
2. Alat packet sniffing: Proxyman gratis di Mac / Charles open source dapat mencegat semua permintaan dan respons App, memperlihatkan lapisan jaringan sejelas foto rontgen;
3. Simulasi jaringan lemah: menu simulator Features → Network Link Conditioner (alatnya perlu diunduh dari situs pengembang) dapat mensimulasikan 3G dan latensi tinggi — menguji keluhan pengalaman "loading berputar lama".

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tips: Permintaan Tidak Lolos ATS?

{class="mt-1"}
Jika permintaan langsung error "App Transport Security" begitu dikirim, hampir pasti karena memakai alamat http:// teks polos. API resmi wajib HTTPS; untuk debug lokal buka pengecualian sementara (tambahkan NSAllowsLocalNetworking di Info.plist), dan ingat bersihkan sebelum rilis ke App Store.
:::

{class="mt-1"}
① Pencarian cuaca berjalan normal; ② saat jaringan diputus, App menampilkan error dengan anggun tanpa crash (uji dengan mematikan jaringan Mac dari simulator!); ③ memasukkan kota yang tidak ada, muncul pesan yang ramah; ④ dua kota favorit tetap ada setelah App dimulai ulang; ⑤ antarmuka tidak menyilaukan di dark mode. Lima poin lulus semua, barulah proyek ini dinyatakan lulus.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan Bab Ini

- Coba API di browser dan pahami JSON-nya dulu, baru menulis kode — "persiapan" tidak pernah merugikan
- API Key disembunyikan di xcconfig, tidak pernah masuk repositori kode
- Model Codable + URLSession async/await: begitu field cocok, JSON terurai otomatis
- Pola tiga bagian status loading/success/error adalah templat serbaguna antarmuka online
- Koneksi putus, input kosong, kota tidak ada — penanganan error adalah batas kelulusan App online
:::
