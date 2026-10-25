---
id: di-liu-shi-ba-zhang
num: 68
part: ios-kai-fa-pian
nav: Bab 68: Jalan Lanjutan—Kebenaran, Notifikasi dan Seni Bina Moden
toc: default
kind: chapter
---

### Bab 68: Jalan Lanjutan — Keizinan, Pemberitahuan dan Seni Bina Moden

{class="chapter-intro mb-4"}
Dapat membuat App hanyalah permulaan. Bab ini membincangkan beberapa halangan dari 'boleh membuat' kepada 'membuat dengan baik': cara memohon keizinan dengan anggun, cara menghantar pemberitahuan tanpa membosankan, cara menaikkan seni bina ke satu peringkat lagi, dan — pada 2026 — cara berpasangan dengan AI untuk menulis kod iOS. Setiap satu daripadanya pasti anda jumpai segera dalam projek sebenar.

#### 1. Keizinan: ketuk pintu dahulu, barulah masuk

Kamera, lokasi, kenalan, pemberitahuan… bagi 'kawasan sensitif' ini, iOS menuntut App memohon melalui pop timbul kepada pengguna semasa digunakan. Peraturannya tiga langkah 'isytihar + mohon + degradasi anggun':

::: div .code-block
:::inline div .code-head
<span>SWIFT · Permohonan kebenaran (contoh lokasi)</span><span class="dots">···</span>
:::

```
// 1. Isytiharkan teks kegunaan dalam Info.plist (kalau tidak, aplikasi terus runtuh!)
// Privacy - Location When In Use Usage Description: "Digunakan untuk melihat cuaca di bandar anda"

// 2. Minta kebenaran semasa guna
import CoreLocation

@Observable
class LocationModel {
    private let manager = CLLocationManager()

    func request() {
        switch manager.authorizationStatus {
        case .notDetermined: manager.requestWhenInUseAuthorization()
        case .denied, .restricted: /* Pandu ke tetapan */
        default: /* Kebenaran diberi, teruskan! */
        }
    }
}

// 3. Jika ditolak, tangani dengan anggun: papar mesej + pandu ke tetapan
// UIApplication.shared.open(URL(string: UIApplication.openSettingsURLString)!)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Perhatian: keizinan iOS 'sekali sahaja'

{class="mt-1"}
Pop timbul keizinan iOS hanya muncul sekali — selepas pengguna menolak, ia tidak akan muncul lagi. Jadi: pilih masa memohon pada 'detik pengguna betul-betul hendak menggunakannya' (bukan memunculkan segalanya sebaik sahaja App dimulakan), dan teksnya menerangkan kegunaan. Panduan antara muka selepas ditolak ('buka lokasi dalam Tetapan') ialah keperluan standard; jangan biarkan pengguna terjebak di jalan buntu.
:::

#### 2. Pemberitahuan: menyampaikan perkara berguna pada masa yang betul

Pemberitahuan ialah saluran App menghubungi pengguna, dan juga fungsi yang paling mudah 'disenarai hitam' oleh pengguna. iOS menggunakan rangka kerja UserNotifications; tiga disiplin menghantar pemberitahuan: hanya hantar yang berguna, biarkan pengguna boleh mematikannya, dan jangan mengganggu tengah malam. Kegunaan asasnya:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Pemberitahuan setempat</span><span class="dots">···</span>
:::

```
import UserNotifications

// 1. Minta kebenaran pemberitahuan (popup sekali)
UNUserNotificationCenter.current()
    .requestAuthorization(options: [.alert, .sound, .badge]) { granted, _ in
        print(granted ? "Diberi kebenaran" : "Ditolak")
    }

// 2. Menjadualkan "setiap hari 20:00 peringatan merekod"
func scheduleDailyReminder() {
    let content = UNMutableNotificationContent()
    content.title = "Peringatan merekod"
    content.body = "Hari ini belum merekod lagi"
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

Perhatian: keizinan pemberitahuan iOS juga 'hanya muncul sekali', dan pengguna boleh mematikannya bila-bila masa dalam tetapan sistem — nilai kandungan pemberitahuan menjadi sangat penting; sekali menghantar secara berlebihan mungkin membuat anda kehilangan pengguna selamanya.

#### 3. Seni bina lanjutan: pendalaman MVVM dan kebolehujian

Bab 65 sudah menggunakan MVVM; di sini ditambah tiga poin lanjutan:

- Abstraksi protokol: jadikan ViewModel bergantung pada protokol (protocol) dan bukannya kelas konkrit — semasa menguji boleh disuntik 'sumber data palsu'; inilah asas kebolehujian;
- Tanggungjawab tunggal: satu ViewModel hanya mengurus satu perkara (yang mengurus rekod kewangan tidak mengurus cuaca); apabila fungsi bertambah, pecahkan;
- Jangan reka bentuk berlebihan: untuk projek kecil seorang diri, 'kelas @Observable + abstraksi protokol' sudah memadai. Seni bina berat seperti VIPER dan Clean Architecture, tunggulah sehingga pasukan dan kerumitan datang mencari — alat berkhidmat untuk matlamat, bukan untuk pameran.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Petua: 'dividen ekosistem' SwiftUI

{class="mt-1"}
Ekosistem iOS juga mempunyai dua 'istimewa tiada ganti' yang lanjutan: widget (WidgetKit) membolehkan pengguna melihat maklumat tanpa membuka App ('belanja bulan ini' buku rekod perbelanjaan boleh diletakkan di skrin utama), dan Shortcut (App Intents) membolehkan pengguna memanggil fungsi anda melalui Siri atau automasi. Kedua-duanya mempunyai rangka kerja rasmi, kos permulaan tidak tinggi, tetapi sumbangannya kepada pengalaman pengguna sangat besar — patut diutamakan untuk dibuka dalam perjalanan lanjutan.
:::

#### 4. Cara baharu 2026: pembangunan iOS dibantu AI

Pada 2026, AI sudah menyatu secara mendalam dalam aliran kerja pembangunan Apple. Jika mahu mempercepatkan kerja, gabungan ini sudah sangat matang:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Peringkat</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Cara AI membantu</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Tanggungjawab anda</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menulis kod</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pelengkap kod terbina dalam Xcode + penjanaan melalui plugin AI pihak ketiga</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Huraikan keperluan dengan jelas, semak hasilnya</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mencari maklumat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Berikan dokumen rasmi dan mesej ralat kepada AI untuk ditafsirkan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menyemak kesimpulan penting semula dengan dokumen rasmi</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menulis ujian</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Meminta AI menjana kes ujian XCTest mengikut tiga kategori 'biasa/sempadan/luar jangka'</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Memastikan kes ujian sepadan dengan logik perniagaan</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Membaiki bug</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Melekatkan log ranap + kod berkaitan, AI mengenal pasti dan membaiki</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Memahami perubahan, jalankan ujian untuk mengesahkan</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Empat senario pembangunan iOS dibantu AI

Metodologi khusus — cara memberi arahan kepada AI, cara menerima hasil, cara mengelak perangkap — keseluruhan 11 bab terdapat dalam Bahagian 7 buku ini 'Praktik Pengekodan AI' (Bab 37-47); sangat disyorkan dibaca bersama: sintaks Swift diserahkan kepada bahagian ini, manakala ilmu kerjasama dengan AI diserahkan kepada Bahagian 7.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Praktik: Tambah 'tiga serangkai' pada buku rekod perbelanjaan

#### 5. Perkara penting keserentakan Swift: @MainActor dan Task

Sistem keserentakan Swift 6 mempunyai dua peraturan yang wajib difahami pemula:

- Antara muka hanya boleh dikemas kini pada urutan utama: view SwiftUI secara lalai ialah @MainActor, jadi selepas panggilan balik rangkaian kembali ke urutan utama barulah ubah state (dengan await MainActor.run { ... } atau tandakan ViewModel sebagai @MainActor);
- Tugas tak segerak diurus dengan Task: modifier .task { } bermula secara automatik apabila view muncul dan dibatalkan secara automatik apabila hilang — inilah cara standard memulakan kerja tak segerak dalam SwiftUI; jangan menulis Task sewenang-wenangnya dalam body.

::: div .code-block
:::inline div .code-head
<span>SWIFT · Corak async piawai</span><span class="dots">···</span>
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
        .task {                       // Mula bila muncul, batal bila hilang
            await vm.search(city: "Beijing")
        }
    }
}
```
:::

Di sebalik dua peraturan ini ialah reka bentuk 'keselamatan perlumbaan data' Swift 6 — pengkompil terus memberi ralat apabila anda tersilap menulis, bukannya mendapati selepas App ranap. Ralat pengkompil bukan cari pasal; ia menahan tembakan untuk anda.

{class="mt-1"}
(1) Tambah 'peringatan merekod pada pukul 20:00 setiap hari' kepada buku rekod perbelanjaan (keizinan pemberitahuan + pemberitahuan tempatan); (2) tukar sumber data ViewModel kepada abstraksi protokol, dan tulis satu ujian unit yang menyuntik data palsu; (3) tambah satu widget skrin utama 'belanja bulan ini'. Selepas tiga serangkai ini siap, projek anda akan kelihatan seperti 'askar regular'.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan bab ini

- Tiga langkah keizinan: isytihar dalam Info.plist (tertinggal pasti ranap), mohon semasa digunakan, selepas ditolak pandu ke Tetapan
- Pop timbul keizinan iOS hanya muncul sekali: pilih masa pada 'detik betul-betul hendak guna', tulis kegunaan dengan jelas dalam teks
- Tiga disiplin pemberitahuan: hanya hantar yang berguna, boleh dimatikan, tidak mengganggu; rangka kerja UserNotifications
- MVVM lanjutan: abstraksi protokol (boleh diuji), tanggungjawab tunggal, jangan reka bentuk berlebihan
- Dividen ekosistem: widget WidgetKit + Shortcut App Intents
- Empat senario bantuan AI: menulis kod, mencari maklumat, menulis ujian, membaiki bug; metodologi lihat Bahagian 7 (Bab 37-47)
:::
