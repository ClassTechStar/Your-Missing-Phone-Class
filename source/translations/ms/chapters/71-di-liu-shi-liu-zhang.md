---
id: di-liu-shi-liu-zhang
num: 66
part: ios-kai-fa-pian
nav: Bab 66: Projek 2—App Semakan Cuaca (Versi Rangkaian)
toc: default
kind: chapter
---

### Bab 66: Projek 2 — App Carian Cuaca (Versi Rangkaian)

{class="chapter-intro mb-4"}
Buku rekod perbelanjaan ialah 'latihan dalaman', App cuaca ialah 'melihat dunia luar' — ia perlu berurusan dengan internet. Dalam projek ini anda belajar: memohon API percuma, menghurai JSON, mengendalikan tiga state antara muka 'memuatkan/berjaya/gagal', serta cara menyembunyikan kunci API dengan baik. Selepas menyiapkannya, anda mempunyai keupayaan membuat sebarang 'App rangkaian' — berita, kadar pertukaran, penterjemah; caranya serupa sahaja.

#### 1. Memohon API cuaca percuma

Untuk latihan individu, disyorkan OpenWeatherMap atau QWeather (perkhidmatan China) — kedua-duanya menawarkan kuota percuma, boleh digunakan sebaik sahaja mendaftar. Contoh dengan OpenWeatherMap:

1. Daftar akaun → jana satu kunci (apikey) pada halaman API keys;
2. Versi percuma boleh memanggil antara muka Current Weather: api.openweathermap.org/data/2.5/weather? q=beijing&appid=kunciAnda&units=metric;
3. Cuba dahulu sekali dalam pelayar untuk melihat bentuk JSON yang dikembalikan — inilah 'persiapan' yang wajib sebelum menyambung sebarang API.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Amaran: kunci jangan sekali-kali ditulis tetap dalam kod

{class="mt-1"}
Kunci API setara dengan 'kata laluan dompet' anda; sebaik sahaja ditulis dalam kod dan dimuat naik ke GitHub, ia akan diimbas oleh bot perayau dalam beberapa jam lalu disalahguna. Cara betul di iOS: letakkan dalam Config.xcconfig (fail tetapan, sudah diabaikan oleh gitignore) dan baca ke dalam kod melalui Info.plist. Cari 'iOS xcconfig mengurus kunci' dan ikut langkahnya.
:::

#### 2. Lapisan rangkaian: URLSession + Codable

Takrifkan dahulu model mengikut JSON yang dikembalikan oleh API, kemudian tulis perkhidmatan:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Model data + servis</span><span class="dots">···</span>
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

#### 3. Tiga state antara muka: memuatkan / berjaya / gagal

Jiwa App rangkaian terletak pada 'pengurusan state'. Rangkaian lambat, tiada sambungan, nama bandar salah taip… setiap keadaan perlu diberitahu kepada pengguna melalui antara muka. Guna enum + switch untuk menyatakannya dengan anggun:

::: div .code-block
:::inline div .code-head
<span>SWIFT · State paparan</span><span class="dots">···</span>
:::

```
enum LoadState {
    case loading                  // sedang berpusing
    case success(WeatherResponse) // berjaya
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
            state = .error("Bandar ini tidak dijumpai, cuba nama lain ya?")
        }
    }
}

// Dalam paparan:
switch vm.state {
case .loading: ProgressView("Memuatkan…")
case .success(let d): WeatherContent(data: d)
case .error(let msg): Text(msg).foregroundColor(.secondary)
}
```
:::

Corak tiga peringkat loading/success/error ini ialah 'templat serbaguna' antara muka rangkaian; hafalkan dahulu, kemudian semua App rangkaian pada masa hadapan boleh ditiru dengan cara yang sama.

#### 4. Kod antara muka praktikal: memaparkan cuaca

::: div .code-block
:::inline div .code-head
<span>SWIFT · Paparan cuaca (petikan teras)</span><span class="dots">···</span>
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

Beberapa butiran kecil wajar dipelajari: first? mengambil elemen pertama dengan selamat (senarai mungkin kosong), ?? "Tidak diketahui" sebagai teks sandaran; angka suhu dengan fon nipis bersaiz 76 ialah resipi klasik App cuaca; Label ialah komponen rasmi 'ikon + teks', lebih teratur daripada menyusun HStack sendiri.

#### 5. Butiran interaksi dan bandar kegemaran

- Kotak carian: modifier .searchable di bahagian atas, interaksi carian terbina dalam sistem, semasa dihantar memanggil vm.search;
- Bandar kegemaran: simpan bandar yang kerap dilihat ke dalam UserDefaults, dibuka kali seterusnya carian dibuat secara automatik;
- Segar semula dengan leret ke bawah: .refreshable { await vm.search(...) } selesai dalam satu baris;
- Ikon cuaca: guna Image(systemName:) untuk memetakan mengikut huraian (sun.max / cloud.rain / snowflake), antara muka terus menjadi hidup.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Petua: 'isunya' nama bandar dalam tulisan Cina

{class="mt-1"}
Sokongan OpenWeatherMap terhadap nama bandar dalam tulisan Cina hanya sederhana; mencari nama bandar dalam tulisan Cina mungkin tiada hasil sedangkan "beijing" berfungsi normal. Pendekatan produk sebenar ialah membina jadual pemetaan 'nama bandar → Inggeris/koordinat' terbina dalam, atau menyambung perkhidmatan cuaca tempatan China. Untuk peringkat latihan, sokongan nama bandar dalam pinyin/Inggeris sudah memadai; jangan memaksa.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Praktik: Senarai semak penerimaan App cuaca

#### 6. Cara menyahpepiat permintaan rangkaian: cetakan, pemeriksaan paket dan simulasi rangkaian perlahan

App rangkaian bermasalah, sembilan daripada sepuluh berpunca daripada 'permintaan tidak dihantar dengan betul' atau 'tindak balas tidak dihurai dengan betul'. Tiga kaedah penyahpepijatan:

1. Cetak data mentah: cetak String(data: data, encoding: .utf8) untuk melihat JSON mentah — nama medan dan jenis kelihatan jelas sekali pandang, sepuluh kali lebih pantas daripada meneka;
2. Alat pemeriksaan paket: Proxyman yang percuma di Mac / Charles sumber terbuka boleh memerangkap semua permintaan dan tindak balas App, memaparkan lapisan rangkaian dengan jelas seperti sinar-X;
3. Simulasi rangkaian lemah: menu simulator Features → Network Link Conditioner (alat perlu dimuat turun dari tapak web pembangun), boleh mensimulasikan 3G dan kependaman tinggi — mengesan masalah pengalaman 'berputar lama tanpa hasil'.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Petua: Permintaan tidak lulus ATS?

{class="mt-1"}
Jika permintaan sebaik sahaja dihantar terus memberi ralat 'App Transport Security', kebanyakannya kerana menggunakan alamat http:// yang jelas. Antara muka rasmi mesti HTTPS; semasa menyahpepiat secara tempatan, buka pengecualian sementara (tambah NSAllowsLocalNetworking dalam Info.plist), dan ingat membersihkannya sebelum muat naik.
:::

{class="mt-1"}
(1) Carian cuaca berfungsi normal; (2) putuskan sambungan internet, App memberi ralat dengan anggun tanpa ranap (uji dengan mematikan rangkaian Mac dalam simulator!); (3) masukkan nama bandar yang tidak wujud, mesej dipaparkan dengan mesra; (4) kegemarkan dua bandar, masih ada selepas App dimulakan semula; (5) antara muka tidak menyilaukan dalam mod gelap. Kelima-limanya lulus, barulah projek ini dikira tamat.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan bab ini

- Cuba API dalam pelayar dan fahami JSON dahulu, barulah menulis kod — 'persiapan' tidak pernah merugikan
- Sembunyikan kunci API dalam xcconfig, jangan sekali-kali masuk repositori kod
- Model Codable + URLSession async/await: medan sepadan, JSON dihurai secara automatik
- Corak tiga peringkat state loading/success/error ialah templat serbaguna antara muka rangkaian
- Tiada internet, input kosong, bandar tidak wujud — pengendalian ralat ialah garis lulus App rangkaian
:::
