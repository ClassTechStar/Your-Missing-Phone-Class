---
id: di-liu-shi-ba-zhang
num: 68
part: ios-kai-fa-pian
nav: Bab 68: Jalan Menuju Tingkat Lanjut—Izin, Notifikasi, dan Arsitektur Modern
toc: default
kind: chapter
---

### Bab 68: Jalan Menuju Level Lanjut — Izin, Notifikasi, dan Arsitektur Modern

{class="chapter-intro mb-4"}
Bisa membuat App baru permulaan. Bab ini membahas beberapa rintangan dari "bisa membuat" menuju "membuat dengan baik": cara mengajukan izin dengan anggun, cara mengirim notifikasi tanpa mengganggu, cara mengangkat arsitektur satu tingkat lagi, dan — pada 2026 — cara menulis kode iOS berdua dengan AI. Semuanya adalah hal yang akan segera kamu temui di proyek nyata.

#### 1. Izin: Ketuk Pintu Dulu, Baru Masuk

Kamera, lokasi, kontak, notifikasi… untuk "zona sensitif" ini, iOS mewajibkan App memunculkan dialog permohonan kepada pengguna saat fiturnya dipakai. Aturannya tiga langkah: "deklarasi + permohonan + degradasi anggun":

::: div .code-block
:::inline div .code-head
<span>SWIFT · Permintaan izin (contoh lokasi)</span><span class="dots">···</span>
:::

```
// 1. Deklarasikan teks alasan di Info.plist (kalau tidak, aplikasi langsung crash!)
// Privacy - Location When In Use Usage Description: "Dipakai untuk melihat cuaca di kota Anda"

// 2. Minta izin saat dipakai
import CoreLocation

@Observable
class LocationModel {
    private let manager = CLLocationManager()

    func request() {
        switch manager.authorizationStatus {
        case .notDetermined: manager.requestWhenInUseAuthorization()
        case .denied, .restricted: /* Arahkan ke pengaturan */
        default: /* Sudah diizinkan, gas! */
        }
    }
}

// 3. Jika ditolak, degradasi dengan elegan: tampilkan pesan + arahkan ke pengaturan
// UIApplication.shared.open(URL(string: UIApplication.openSettingsURLString)!)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Perhatian: "Sekali Saja" Izin iOS

{class="mt-1"}
Dialog izin iOS hanya muncul satu kali — setelah pengguna menolak, tidak akan muncul lagi. Karena itu: ajukan izin pada saat "tepat ketika pengguna hendak memakainya" (bukan memunculkan segudang dialog begitu aplikasi dibuka), dan tulisannya harus menjelaskan kegunaannya. Panduan antarmuka setelah ditolak ("buka lokasi di Pengaturan") adalah fitur wajib; jangan biarkan pengguna terjebak di jalan buntu.
:::

#### 2. Notifikasi: Mengucapkan Hal Berguna di Waktu yang Tepat

Notifikasi adalah saluran App menjangkau pengguna, sekaligus fitur yang paling mudah "diblokir" oleh mereka. iOS memakai framework UserNotifications, dengan tiga disiplin mengirim notifikasi: hanya kirim yang berguna, biarkan pengguna bisa mematikan, dan jangan mengganggu tengah malam. Pemakaian dasarnya:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Notifikasi lokal</span><span class="dots">···</span>
:::

```
import UserNotifications

// 1. Minta izin notifikasi (popup sekali)
UNUserNotificationCenter.current()
    .requestAuthorization(options: [.alert, .sound, .badge]) { granted, _ in
        print(granted ? "Diizinkan" : "Ditolak")
    }

// 2. Menjadwalkan "setiap hari 20:00 pengingat mencatat"
func scheduleDailyReminder() {
    let content = UNMutableNotificationContent()
    content.title = "Pengingat mencatat"
    content.body = "Hari ini belum mencatat, lho"
    content.sound = .default

    var comps = DateComponents()
    comps.hour = 20
    let trigger = UNCalendarNotificationTrigger(dateMatching: comps, repeats: true)

    let request = UNNotificationRequest(
        identifier: "daily-reminder",
        content: content,
        trigger: trigger
    )
    UNUserNotificationCenter.current().add(request)
}
```
:::

Perhatian: izin notifikasi iOS juga "hanya muncul sekali", dan pengguna bisa mematikannya kapan saja di pengaturan sistem — karena itu rasa nilai dari isi notifikasi sangat penting; sekali berlebihan mengirim, pengguna bisa hilang selamanya.

#### 3. Arsitektur Lanjut: Mendalami MVVM dan Keterujian

Bab 65 sudah memakai MVVM; di sini ditambah tiga poin lanjutan:

- Abstraksi protokol: buat ViewModel bergantung pada protokol (protocol) alih-alih kelas konkret — saat pengujian bisa disuntik "sumber data palsu"; inilah fondasi keterujian;
- Tanggung jawab tunggal: satu ViewModel hanya mengurus satu hal (yang mencatat keuangan tidak mengurus cuaca); kalau fiturnya bertambah, pecah saja;
- Jangan over-engineering: untuk proyek kecil satu orang, "kelas @Observable + abstraksi protokol" sudah cukup. Arsitektur berat seperti VIPER atau Clean Architecture, tunggu saja sampai tim dan kompleksitas datang mengetuk — alat adalah untuk melayani tujuan, bukan untuk dipamerkan.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tips: "Bonus Ekosistem" SwiftUI

{class="mt-1"}
Ekosistem iOS masih punya dua cara bermain lanjutan yang "tak ada duanya": widget (WidgetKit) memungkinkan pengguna melihat informasi tanpa membuka App ("pengeluaran bulan ini" dari buku catatan keuangan ditaruh di layar utama), dan Pintasan (App Intents) memungkinkan pengguna memanggil fiturmu lewat Siri atau otomatisasi. Keduanya punya framework resmi dengan biaya masuk yang tidak tinggi, tetapi menambah pengalaman pengguna secara luar biasa — layak diprioritaskan untuk dibuka di jalan menuju level lanjut.
:::

#### 4. Cara Baru 2026: Pengembangan iOS Berbantuan AI

Pada 2026, AI sudah menyatu dalam alur kerja pengembangan Apple. Kalau ingin mempercepat, kombinasi berikut ini sudah sangat matang:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Tahapan</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Bagaimana AI membantu</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Tugasmu</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menulis kode</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pelengkapan kode bawaan Xcode + pembuatan lewat plugin AI pihak ketiga</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Deskripsikan kebutuhan dengan jelas, periksa hasilnya</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mencari referensi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Serahkan dokumentasi resmi dan pesan error ke AI untuk ditafsirkan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Verifikasi kesimpulan penting kembali ke dokumentasi resmi</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menulis tes</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Minta AI membuat kasus uji XCTest dalam tiga kategori "normal/batas/eksepsi"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pastikan kasus uji sesuai makna bisnis</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Memperbaiki bug</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tempelkan log crash + kode terkait, AI menemukan lokasi dan memperbaiki</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pahami perubahannya, jalankan tes untuk memverifikasi</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Empat skenario pengembangan iOS berbantuan AI

Metodologi konkretnya — cara memberi instruksi ke AI, cara menerima hasil kerja, cara menghindari jebakan — dibahas lengkap dalam 11 bab di Bagian 7 buku ini, "Praktik Pemrograman dengan AI" (Bab 37–47). Sangat disarankan membaca keduanya bersamaan: sintaks Swift diserahkan ke bagian ini, kiat kerja sama dengan AI diserahkan ke Bagian 7.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Praktik: Menambahkan "Trio" ke Buku Catatan Keuangan

#### 5. Poin Penting Concurrency Swift: @MainActor dan Task

Sistem concurrency Swift 6 punya dua aturan yang wajib dipahami pemula:

- Antarmuka hanya boleh diperbarui di thread utama: view SwiftUI secara bawaan adalah @MainActor, jadi callback jaringan harus kembali ke thread utama sebelum mengubah state (dengan await MainActor.run { ... } atau menandai ViewModel sebagai @MainActor);
- Tugas asinkron dikelola dengan Task: modifier .task { } otomatis mulai saat view muncul dan otomatis dibatalkan saat view hilang — inilah posisi standar memulai kerja asinkron di SwiftUI; jangan asal menulis Task telanjang di dalam body.

::: div .code-block
:::inline div .code-head
<span>SWIFT · Pola async standar</span><span class="dots">···</span>
:::

```
struct WeatherScreen: View {
    @State private var vm = WeatherViewModel()

    var body: some View {
        Group {
            switch vm.state {
            case .loading: ProgressView()
            case .success(let d): WeatherContent(data: d)
            case .error(let m): Text(m)
            }
        }
        .task {                       // Mulai begitu muncul, batal begitu hilang
            await vm.search(city: "Beijing")
        }
    }
}
```
:::

Di balik dua aturan ini ada desain "keamanan data race" Swift 6 — kompiler langsung memberi error saat kamu salah menulis, bukan menunggu App crash baru ketahuan. Error dari kompiler bukan mencari-cari kesalahanmu; ia menahan peluru untukmu.

{class="mt-1"}
① Tambahkan "pengingat mencatat pukul 20:00 setiap hari" ke buku catatan (izin notifikasi + notifikasi lokal); ② ubah sumber data ViewModel menjadi abstraksi protokol, dan tulis satu tes unit dengan data palsu yang disuntikkan; ③ tambahkan widget layar utama "pengeluaran bulan ini". Setelah trio ini selesai, proyekmu sudah tampak seperti "pasukan reguler".
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan Bab Ini

- Tiga langkah izin: deklarasi di Info.plist (terlewat pasti crash), minta saat dipakai, jika ditolak arahkan ke Pengaturan
- Dialog izin iOS hanya muncul sekali: pilih saat "tepat hendak dipakai", tulisannya menjelaskan kegunaan
- Tiga disiplin notifikasi: hanya kirim yang berguna, bisa dimatikan, tidak mengganggu; framework UserNotifications
- MVVM lanjutan: abstraksi protokol (bisa diuji), tanggung jawab tunggal, tidak over-engineering
- Bonus ekosistem: widget WidgetKit + Pintasan App Intents
- Empat skenario berbantuan AI: menulis kode, mencari referensi, menulis tes, memperbaiki bug; metodologinya lihat Bagian 7 (Bab 37–47)
:::
