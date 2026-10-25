---
id: di-liu-shi-si-zhang
num: 64
part: ios-kai-fa-pian
nav: Bab 64: Penyimpanan Data dan Permintaan Rangkaian
toc: default
kind: chapter
---

### Bab 64: Penyimpanan Data dan Permintaan Rangkaian

{class="chapter-intro mb-4"}
App yang hanya boleh 'dilihat' ialah App mati; App yang boleh menyimpan data dan menyambung internet barulah hidup. Bab ini mengenalkan 'tiga serangkai' lapisan data iOS: UserDefaults (simpan tetapan kecil), SwiftData (simpan data berstruktur), URLSession (berbual dengan pelayan), ditambah Codable untuk menghurai JSON dan async/await yang moden. Selepas bab ini, anda boleh menulis App sebenar yang mengingati tabiat pengguna dan mengemas kini kandungan secara masa nyata.

#### 1. Cara memilih kaedah penyimpanan: lihat jadual ini dahulu

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Kaedah</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Sesuai menyimpan apa</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ciri</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Digunakan di mana dalam buku ini</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UserDefaults</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tetapan berselerak (suis, keutamaan)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pasangan kunci-nilai, ringkas dan terus</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tetapan Bab 65, bandar kegemaran Bab 66</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftData</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Data berstruktur (rekod akaun, catatan)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pembalut pangkalan data rasmi, diisytihar dengan satu baris @Model</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Rekod akaun Bab 65</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">URLSession</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">(Tidak disimpan, diambil melalui internet) data pelayan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Rangka kerja rangkaian terbina dalam sistem, tiada pergantungan pihak ketiga</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Data cuaca Bab 66</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Pembahagian tugas tiga serangkai data

Hafal satu rumus: 'tetapan kecil masuk UserDefaults, data beramai-ramai masuk SwiftData, data dari luar guna URLSession'. Core Data dalam tutorial lama masih boleh digunakan (SwiftData ialah jubah modennya), manakala SQLite tulisan tangan hampir tidak perlu disentuh — belajar terus yang baharu, jangan ikut jalan lama.

#### 2. UserDefaults: simpan tetapan kecil

::: div .code-block
:::inline div .code-head
<span>SWIFT · Contoh UserDefaults</span><span class="dots">···</span>
:::

```
// Tulis: simpan satu nilai
UserDefaults.standard.set(true, forKey: "isDarkMode")
UserDefaults.standard.set("Beijing", forKey: "favoriteCity")

// Baca: ambil nilainya (jika tiada, pulangkan nilai lalai)
let isDark = UserDefaults.standard.bool(forKey: "isDarkMode")
let city = UserDefaults.standard.string(forKey: "favoriteCity") ?? "Beijing"

// Padam: buang satu kunci
UserDefaults.standard.removeObject(forKey: "isDarkMode")
```
:::

Perhatikan ia hanya sesuai untuk tetapan kecil yang berselerak — rekod berpuluhan hingga beratus-ratus serahkan kepada SwiftData; jangan gunakan UserDefaults sebagai pangkalan data (melambatkan permulaan dan sukar dibuat pertanyaan).

#### 3. SwiftData: berikan data 'rumah sebenar'

SwiftData ialah penyelesaian pangkalan data rasmi mulai iOS 17, memudahkan 'bina jadual, tambah-padam-ubah-cari' hingga ke tahap maksimum — satu anotasi @Model sahaja, kelas data bertukar menjadi jadual pangkalan data:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Contoh SwiftData</span><span class="dots">···</span>
:::

```
import SwiftData

// 1. @Model: kelas ini menjadi "jadual" secara automatik
@Model
class Record {
    var amount: Double
    var category: String
    var note: String
    var date: Date

    init(amount: Double, category: String, note: String, date: Date) {
        self.amount = amount
        self.category = category
        self.note = note
        self.date = date
    }
}

// 2. Pasang bekas di pintu masuk aplikasi
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .modelContainer(for: Record.self)   // pangkalan data sedia
    }
}

// 3. Dalam view guna @Query untuk baca, @Environment untuk tulis
struct RecordListView: View {
    @Query(sort: \Record.date, order: .reverse) var records: [Record]
    @Environment(\.modelContext) private var context

    var body: some View {
        List(records) { r in
            Text("\(r.category) \(r.amount) yuan")
        }
    }

    func add(amount: Double, category: String) {
        let r = Record(amount: amount, category: category, note: "", date: Date())
        context.insert(r)     // simpan
        try? context.save()   // tulis ke cakera
    }
}
```
:::

Templat '@Model + modelContainer + @Query' ini boleh dibawa masuk ke mana-mana projek anda seadanya — cukup tukar nama medan. Data berubah, @Query menyegarkan antara muka secara automatik; sungguh menakjubkan.

#### 4. Codable: 'menerjemahkan' JSON

Kebanyakan data pelayan ialah teks JSON. Protokol Codable Swift menjadikan penukaran 'JSON ⇄ struktur' berlaku secara automatik — nama medan sepadan, sihirnya berkesan:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Menghurai JSON dengan Codable</span><span class="dots">···</span>
:::

```
// JSON: {"name":"Beijing","main":{"temp":26.5},"weather":[{"description":"Cerah"}]}
struct WeatherResponse: Codable {
    let name: String
    let main: Main
    let weather: [Weather]
}
struct Main: Codable { let temp: Double }
struct Weather: Codable { let description: String }

// Rentetan JSON → struct
let decoder = JSONDecoder()
let data = jsonString.data(using: .utf8)!
let result = try decoder.decode(WeatherResponse.self, from: data)
print(result.weather[0].description)   // "Cerah"
```
:::

Peraturan besi: lihat dahulu JSON yang benar-benar dikembalikan, barulah takrifkan medan. Banyak bug 'gagal menghurai' berpunca daripada nama medan tersalah taip atau jenis tersalah teka (pelayan menghantar rentetan "26.5", anda mengisytiharkan sebagai Double) — cetak JSON mentah untuk dibandingkan, masalah dapat dikenal pasti dalam sepuluh saat.

#### 5. URLSession + async/await: berbual dengan pelayan

Sambungan internet iOS guna URLSession terbina dalam sistem, digandingkan dengan async/await Swift (fungsi tak segerak), maka 'menunggu rangkaian' menjadi semula jadi seperti 'menunggu bungkusan':

::: div .code-block
:::inline div .code-head
<span>SWIFT · URLSession + async/await</span><span class="dots">···</span>
:::

```
struct WeatherService {
    // Fungsi async: async bermaksud "aku perlu tunggu sebentar", throws bermaksud "mungkin gagal"
    func fetchWeather(city: String) async throws -> WeatherResponse {
        let url = URL(string:
            "https://api.example.com/weather?city=\(city)")!
        let (data, _) = try await URLSession.shared.data(from: url)
        return try JSONDecoder().decode(WeatherResponse.self, from: data)
    }
}

// Titik panggilan (dalam .task):
.task {
    do {
        let weather = try await service.fetchWeather(city: "Beijing")
        // Kemas kini paparan……
    } catch {
        print("Berlaku ralat: \(error)")
    }
}
```
:::

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Amaran: dua peraturan besi rangkaian

{class="mt-1"}
(1) Sambungan internet mesti async/await, jangan sekali-kali menyekat urutan utama — antara muka tersekat ialah pengalaman tahap ranap. Keserentakan berstruktur Swift menjadikannya semula jadi, tetapi jangan lupa try await dan do/catch. (2) ATS secara lalai melarang HTTP jelas: iOS menuntut HTTPS. Semasa menguji perkhidmatan http:// tempatan, perlu buka pengecualian sementara dalam Info.plist (NSAppTransportSecurity), tetapi produk rasmi mesti sepenuhnya HTTPS — semakan Apple juga memantau perkara ini.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Praktik: Bina aplikasi kecil 'ayat harian'

#### 6. Ralat rangkaian juga perlu 'dikelaskan': jangan campak semua ralat kepada pengguna

Tiada internet, tamat masa, 404, pelayan 500… ralat yang berbeza, mesej yang patut dilihat pengguna juga berbeza:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Pengendalian ralat bertingkat</span><span class="dots">···</span>
:::

```
func friendlyMessage(_ error: Error) -> String {
    if let urlError = error as? URLError {
        switch urlError.code {
        case .notConnectedToInternet: return "Sambungan terputus, semak dulu ya?"
        case .timedOut:               return "Permintaan tamat masa, cuba lagi nanti ya?"
        case .cannotFindHost:         return "Pelayar tidak dijumpai"
        default:                      return "Ada masalah rangkaian: \(urlError.code)"
        }
    }
    if let d = error as? DecodingError {
        return "Format data tidak sepadan (mungkin API sudah berubah)"
    }
    return "Berlaku ralat: \(error.localizedDescription)"
}
```
:::

Tunjukkan 'bahasa manusia' kepada pengguna, dan 'teks asal' kepada log (print ralat penuh). Jangan campakkan teks Inggeris yang mengerikan daripada error.localizedDescription terus kepada pengguna — rasa produk tersembunyi dalam butiran begini.

{class="mt-1"}
Cari API petikan percuma (seperti hitokoto), guna URLSession + async/await untuk menarik 'ayat harian', paparkan di tengah skrin, dan tambahkan butang 'Tukar ayat'. Kemudian simpan ayat kegemaran ke dalam 'Kegemaran' dengan SwiftData. Latihan ini menggunakan UserDefaults/SwiftData/Codable/URLSession semuanya sekali — selepas menyiapkannya, Bab 7 dan 8 menjadi perkara mudah.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan bab ini

- Rumus: tetapan kecil masuk UserDefaults, data beramai-ramai masuk SwiftData, data dari luar guna URLSession
- Tiga langkah SwiftData: @Model isytihar jadual, modelContainer pasang bekas, @Query baca + context.insert tulis
- Codable 'menerjemahkan' JSON secara automatik: medan sepadan, sihirnya berkesan
- URLSession + async/await: bersambung internet seperti menunggu bungkusan; do/catch mengendalikan kegagalan
- Dua peraturan besi: jangan sekat urutan utama; produk rasmi mesti HTTPS (ATS)
:::
