---
id: di-liu-shi-si-zhang
num: 64
part: ios-kai-fa-pian
nav: Bab 64: Penyimpanan Data dan Permintaan Jaringan
toc: default
kind: chapter
---

### Bab 64: Penyimpanan Data dan Permintaan Jaringan

{class="chapter-intro mb-4"}
App yang hanya bisa "dilihat" itu mati; App yang bisa menyimpan data dan terhubung ke internet barulah hidup. Bab ini memperkenalkan "trio" lapisan data iOS: UserDefaults (menyimpan konfigurasi kecil), SwiftData (menyimpan data terstruktur), URLSession (berbicara dengan server), ditambah Codable untuk mengurai JSON serta async/await yang modern. Setelah bab ini, kamu bisa menulis App sungguhan yang mengingat kebiasaan pengguna dan memperbarui konten secara real-time.

#### 1. Cara Memilih Skema Penyimpanan: Lihat Dulu Tabel Ini

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Skema</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Cocok untuk menyimpan apa</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ciri</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Dipakai di mana di buku ini</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UserDefaults</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Konfigurasi kecil-kecil (sakelar, preferensi)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pasangan kunci-nilai, sederhana dan langsung</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pengaturan Bab 65, kota favorit Bab 66</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftData</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Data terstruktur (catatan keuangan, rekaman)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pembungkus basis data resmi, dideklarasikan cukup @Model satu baris</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Catatan keuangan Bab 65</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">URLSession</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">(tidak disimpan, diambil lewat internet) Data server</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Framework jaringan bawaan sistem, tanpa dependensi pihak ketiga</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Data cuaca Bab 66</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Pembagian tugas trio data

Hafalkan jembatan keledai ini: "konfigurasi kecil masuk UserDefaults, data dalam jumlah besar masuk SwiftData, data dari luar lewat URLSession". Core Data di tutorial lama tetap bisa dipakai (SwiftData adalah wajah modernnya), sedangkan SQLite tulis manual hampir tidak perlu disentuh — belajar langsung yang baru, jangan ambil jalan lama.

#### 2. UserDefaults: Menyimpan Konfigurasi Kecil

::: div .code-block
:::inline div .code-head
<span>SWIFT · Contoh UserDefaults</span><span class="dots">···</span>
:::

```
// Tulis: simpan sebuah nilai
UserDefaults.standard.set(true, forKey: "isDarkMode")
UserDefaults.standard.set("Beijing", forKey: "favoriteCity")

// Baca: ambil nilainya (kalau tidak ada, kembalikan nilai default)
let isDark = UserDefaults.standard.bool(forKey: "isDarkMode")
let city = UserDefaults.standard.string(forKey: "favoriteCity") ?? "Beijing"

// Hapus: buang satu key
UserDefaults.standard.removeObject(forKey: "isDarkMode")
```
:::

Ingat, ia hanya cocok untuk konfigurasi kecil yang berserakan — puluhan hingga ratusan rekaman serahkan ke SwiftData; jangan menjadikan UserDefaults sebagai basis data (akan memperlambat proses startup dan menyulitkan pencarian).

#### 3. SwiftData: Memberi Data "Rumah yang Sesungguhnya"

SwiftData adalah solusi basis data resmi sejak iOS 17, yang menyederhanakan "membuat tabel, menambah, menghapus, mengubah, mencari" hingga ekstrem — cukup satu anotasi @Model, kelas data langsung menjadi tabel basis data:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Contoh SwiftData</span><span class="dots">···</span>
:::

```
import SwiftData

// 1. @Model: kelas ini otomatis menjadi "tabel"
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

// 2. Pasang kontainer di titik masuk aplikasi
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .modelContainer(for: Record.self)   // database siap
    }
}

// 3. Di view pakai @Query untuk baca, @Environment untuk tulis
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
        try? context.save()   // tulis ke disk
    }
}
```
:::

Templat "@Model + modelContainer + @Query" ini bisa dipindahkan apa adanya ke proyek mana pun milikmu — cukup ganti nama fieldnya. Begitu data berubah, @Query otomatis menyegarkan antarmuka; kenyamanannya luar biasa.

#### 4. Codable: "Menerjemahkan" JSON

Data dari server sebagian besar berupa teks JSON. Protokol Codable di Swift membuat konversi "JSON ⇄ struct" terjadi otomatis — begitu nama field cocok, sihirnya langsung bekerja:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Mengurai JSON dengan Codable</span><span class="dots">···</span>
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

// String JSON → struct
let decoder = JSONDecoder()
let data = jsonString.data(using: .utf8)!
let result = try decoder.decode(WeatherResponse.self, from: data)
print(result.weather[0].description)   // "Cerah"
```
:::

Aturan besi: lihat dulu JSON asli yang dikembalikan, baru definisikan field. Banyak bug "gagal parsing" penyebabnya nama field salah tulis atau tipe salah tebak (server mengirim string "26.5", kamu mendeklarasikannya sebagai Double) — cetak JSON mentahnya untuk dibandingkan, masalah ketemu dalam sepuluh detik.

#### 5. URLSession + async/await: Berbicara dengan Server

Untuk koneksi internet, iOS memakai URLSession bawaan sistem; dikombinasikan dengan async/await Swift (fungsi asinkron), "menunggu jaringan" terasa senatural "menunggu paket kiriman":

::: div .code-block
:::inline div .code-head
<span>SWIFT · URLSession + async/await</span><span class="dots">···</span>
:::

```
struct WeatherService {
    // Fungsi async: async artinya "aku perlu menunggu", throws artinya "bisa gagal"
    func fetchWeather(city: String) async throws -> WeatherResponse {
        let url = URL(string:
            "https://api.example.com/weather?city=\(city)")!
        let (data, _) = try await URLSession.shared.data(from: url)
        return try JSONDecoder().decode(WeatherResponse.self, from: data)
    }
}

// Titik pemanggilan (di dalam .task):
.task {
    do {
        let weather = try await service.fetchWeather(city: "Beijing")
        // Perbarui tampilan……
    } catch {
        print("Terjadi kesalahan: \(error)")
    }
}
```
:::

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Peringatan Jebakan: Dua Aturan Besi Jaringan

{class="mt-1"}
① Akses internet wajib async/await, jangan pernah memblokir thread utama — antarmuka yang macet adalah pengalaman selevel crash. Structured concurrency di Swift membuat hal ini terasa alami, tapi jangan lupakan try await dan do/catch. ② ATS secara bawaan melarang HTTP teks polos: iOS mewajibkan HTTPS. Saat menguji layanan http:// lokal, perlu membuka pengecualian sementara di Info.plist (NSAppTransportSecurity), tetapi produk resmi wajib sepenuhnya lewat HTTPS — pemeriksaan App Store juga mengawasi hal ini.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Praktik: Membuat Aplikasi Kecil "Kalimat Harian"

#### 6. Kesalahan Jaringan Juga Perlu "Diklasifikasi": Jangan Buang Semua Error ke Pengguna

Koneksi putus, timeout, 404, server 500… kesalahan yang berbeda butuh pesan yang berbeda pula untuk pengguna:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Penanganan error berjenjang</span><span class="dots">···</span>
:::

```
func friendlyMessage(_ error: Error) -> String {
    if let urlError = error as? URLError {
        switch urlError.code {
        case .notConnectedToInternet: return "Koneksi terputus, cek dulu ya?"
        case .timedOut:               return "Permintaan habis waktu, coba lagi nanti ya?"
        case .cannotFindHost:         return "Server tidak ditemukan"
        default:                      return "Ada masalah jaringan: \(urlError.code)"
        }
    }
    if let d = error as? DecodingError {
        return "Format data tidak cocok (mungkin API-nya berubah)"
    }
    return "Terjadi kesalahan: \(error.localizedDescription)"
}
```
:::

Tunjukkan "bahasa manusia" kepada pengguna, dan "teks asli" untuk log (print error secara lengkap). Jangan melempar tulisan Inggris rumit dari error.localizedDescription langsung ke pengguna — rasa produk justru tersembunyi di detail seperti ini.

{class="mt-1"}
Cari API kutipan gratis (misalnya hitokoto dan sejenisnya), gunakan URLSession + async/await untuk mengambil "kalimat harian", tampilkan di tengah layar, dan tambahkan tombol "Ganti kalimat". Lalu simpan kalimat favorit ke "koleksi" dengan SwiftData. Latihan ini memakai UserDefaults/SwiftData/Codable/URLSession semuanya sekaligus — setelah menyelesaikannya, Bab 7 dan 8 akan terasa seperti makan hidangan ringan.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan Bab Ini

- Jembatan keledai: konfigurasi kecil masuk UserDefaults, data dalam jumlah besar masuk SwiftData, data dari luar lewat URLSession
- Tiga jurus SwiftData: @Model mendeklarasikan tabel, modelContainer memasang kontainer, @Query untuk membaca + context.insert untuk menulis
- Codable otomatis "menerjemahkan" JSON: begitu field cocok, sihirnya bekerja
- URLSession + async/await: mengakses internet seperti menunggu paket; do/catch menangani kegagalan
- Dua aturan besi: jangan blokir thread utama; produk resmi wajib HTTPS (ATS)
:::
