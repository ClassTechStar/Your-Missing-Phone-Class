---
id: di-liu-shi-zhang
num: 60
part: ios-kai-fa-pian
nav: Bab 60: Menyiapkan Lingkungan Pengembangan—Xcode dan Proyek Pertama
toc: default
kind: chapter
---

### Bab 60: Menyiapkan Lingkungan Pengembangan — Xcode dan Proyek Pertama

{class="chapter-intro mb-4"}
Ingin bekerja bagus, tajamkan dulu alatnya. Di bab ini kita menata "dapur": memasang Xcode, menjalankan Simulator sampai jalan, membuat proyek iOS pertama dalam hidupmu, lalu membongkar struktur proyeknya sampai jelas. Setelah lingkungan siap, kamu akan pertama kali melihat kode tulisanmu menjadi tombol yang bisa ditekan — momen ini bagi banyak orang diingat seumur hidup.

#### 1. Siapkan sebuah Mac

Syaratnya dulu: pengembangan iOS harus dilakukan di macOS. Kalau belum punya Mac, pilihannya tiga: beli satu (Mac mini atau MacBook Air bekas pun cukup), sewa Mac cloud untuk jangka pendek, atau baca dulu Bagian 8 "Praktik Pengembangan Android" (bisa dikerjakan di Windows).

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Butir spesifikasi</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Kebutuhan minimum</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Batas nyaman (direkomendasikan)</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Chip</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple Silicon (M1 ke atas)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">M2 atau lebih baru</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Memori</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">8GB</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">16GB</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Disk</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sediakan 40GB+ (badan Xcode sendiri gemuk)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mulai dari 256GB</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sistem</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">macOS terbaru</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Biarkan pembaruan otomatis menyala</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Referensi konfigurasi Mac untuk pengembangan (Agustus 2026)

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tips: Tanpa Mac pun bisa belajar bahasanya dulu

{class="mt-1"}
Swift Playgrounds yang gratis di iPad bisa dipakai mempelajari dasar bahasa Swift (tanpa Mac); bahkan bisa dipasang di iPhone. Mainkan dulu materi bahasa Bab 61 di Playgrounds sampai cair, begitu Mac tiba langsung melesat. "Mengasah parang tak menunda menebang kayu" — maksudnya persis itu.
:::

#### 2. Memasang Xcode

Xcode adalah lingkungan pengembangan terintegrasi resmi Apple, gratis. Terpasang dalam tiga langkah:

1. Di Mac buka App Store, cari "Xcode", tekan pasang — perhatikan ukurannya beberapa GB, pilih waktu dengan jaringan bagus;
2. Setelah terpasang, saat pertama dijalankan: setujui perjanjian, tunggu komponen selesai terpasang (otomatis);
3. Menu Xcode → Settings → Locations, pastikan Command Line Tools sudah terpilih — alat baris perintah adalah prasyarat banyak skrip dan alat pihak ketiga.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Perhatian: "Permainan pencocokan" versi dan sistem

{class="mt-1"}
Xcode baru kerap menuntut macOS terbaru, sedangkan Mac lama bisa tertahan di versi tua. Saat tayang ke App Store, Apple menuntut build dengan Xcode yang lebih baru (biasanya diberi masa tenggang). Jadi jangan menunda pembaruan sistem terlalu lama — pengembang iOS adalah kelompok yang paling rajin "mengejar versi baru".
:::

#### 3. Membuat proyek pertamamu

Buka Xcode → Create New Project → pilih iOS → template App, lalu isi:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Butir konfigurasi</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Diisi apa</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Keterangan</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Product Name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstApp</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Nama aplikasi</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Team</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple ID kamu (gratis)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Dipakai untuk penandatanganan; akun pribadi cukup</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Organization Identifier</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">com.example</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Digabung dengan Product Name menjadi pengenal paket</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Interface</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Framework jalur utama buku ini</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Language</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tak perlu dijelaskan</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Lima hal yang diisi saat membuat proyek

Setelah menekan Create, Xcode menghasilkan proyek yang bisa langsung dijalankan. Pilih satu Simulator di pojok kiri atas (misalnya iPhone 17), tekan ▶ untuk menjalankan — beberapa detik kemudian, di layar Simulator muncul jendela bertuliskan "Hello, world!". App iOS pertamamu telah lahir.

#### 4. Bedah struktur proyek: Tiap file berfungsi apa

Panel kiri adalah project navigator; pemula cukup mengenal ini:

::: div .figure
```html
<svg style="max-width:100%;height:auto" width="600" height="290" viewBox="0 0 600 290" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="600" height="290" fill="#fafafa" rx="8"/>
      <text x="20" y="28" font-size="13" font-weight="bold" fill="#111827">MyFirstApp/ direktori akar proyek</text>
      <rect x="30" y="42" width="540" height="225" fill="#ffffff" stroke="#d1d5db" rx="6"/>
      <rect x="45" y="56" width="250" height="196" fill="#eef2ff" rx="5"/>
      <text x="56" y="78" font-size="11" fill="#1e1b4b" font-weight="bold">MyFirstApp/ (direktori kode)</text>
      <text x="66" y="100" font-size="10" fill="#374151">├ MyFirstAppApp.swift  ← pintu masuk program</text>
      <text x="66" y="120" font-size="10" fill="#374151">├ ContentView.swift  ← tampilan utama</text>
      <text x="66" y="140" font-size="10" fill="#374151">└ Assets.xcassets  ← ikon, gambar, warna</text>
      <text x="56" y="166" font-size="10" fill="#6b7280">(semua file baru diletakkan di direktori ini)</text>
      <text x="56" y="196" font-size="10" fill="#1e1b4b" font-weight="bold">Tab Info / Info.plist</text>
      <text x="66" y="216" font-size="10" fill="#6b7280">Deklarasi aplikasi: nama, izin, pengaturan</text>
      <rect x="310" y="56" width="245" height="196" fill="#f0fdf4" rx="5"/>
      <text x="321" y="78" font-size="11" fill="#065f46" font-weight="bold">Posisi penting lainnya</text>
      <text x="331" y="100" font-size="10" fill="#374151">📁 Preview Content/  ← materi pratinjau</text>
      <text x="331" y="122" font-size="10" fill="#374151"><i class="fas fa-bullseye mr-1"></i> Pengaturan Target (ikon proyek biru)</text>
      <text x="331" y="142" font-size="10" fill="#6b7280">— nomor versi, sistem minimum, dan tanda tangan ada di sini</text>
      <text x="331" y="168" font-size="10" fill="#374151"><i class="fas fa-flask mr-1"></i> MyFirstAppTests/  ← unit test</text>
      <text x="331" y="188" font-size="10" fill="#374151">📱 MyFirstAppUITests/ ← test tampilan</text>
      <text x="331" y="216" font-size="10" fill="#9ca3af">(template test sudah dibuat, dipakai di Bab 67)</text>
    </svg>
```

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Gambar 2: Struktur proyek Xcode yang wajib dipahami pemula
:::

- MyFirstAppApp.swift: pintu masuk program; di SwiftUI isinya hanya beberapa baris — "nyalakan, lalu tampilkan layar utama";
- ContentView.swift: tampilan layar utama; semua yang kamu lihat sekarang ada di sini;
- Assets.xcassets: gudang aset — ikon, gambar, dan warna ditaruh di sini;
- Pengaturan Target: tekan ikon proyek biru di kiri untuk masuk; nomor versi, versi iOS minimum, dan penandatanganan semuanya ada di dalamnya. Nama tampilan App dan ikon juga diatur di sini.

#### 5. Trik efisiensi Xcode: Lima "cheat shortcut" untuk pemula

Kalau lima ini sudah terbiasa, kamu akan tampak "sangat profesional":

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Aksi</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Shortcut</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Fungsi</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Jalankan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘R</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kompilasi dan langsung berjalan</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Membuka/mengalihkan pratinjau kanvas</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌥⌘↩</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sakelar pratinjau langsung (WYSIWYG)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Merapikan indentasi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌃I</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Merapikan otomatis indentasi kode yang dipilih</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Membuka file dengan cepat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘O</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ketik nama file, terbuka dalam sekejap (paling sering dipakai!)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Memberi/menghapus komentar</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mematikan/menyalakan kode sepintas saat debugging</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Shortcut Xcode paling sering dipakai (paket lima pemula)

Dua bonus tersembunyi lainnya: menjalankan beberapa Simulator sekaligus (iPhone dan iPad jalan bersamaan untuk membandingkan tata letak) dan pustaka potongan kode (tarik beberapa baris kode yang sering dipakai ke panel Snippets di kanan, nanti tinggal sisipkan sekali tekan) — pakai dulu alat efisiensinya, kecekatan tangan otomatis naik.

#### 6. Debug di perangkat asli: Memasang App ke iPhone-mu

Simulator memang nyaman, tetapi perangkat asli adalah garis finisnya. Dengan Apple ID gratis pun bisa debug di perangkat asli:

1. Sambungkan iPhone dengan kabel data (atau debug nirkabel lewat Wi-Fi yang sama);
2. Pada daftar perangkat di bagian atas Xcode pilih ponselmu; pertama kali akan diminta masuk Apple ID dan penandatanganan dikonfigurasi otomatis;
3. Di iPhone buka [Pengaturan] → [Umum] → [VPN & Manajemen Perangkat] → percayai sertifikat pengembangmu;
4. Tekan ▶, dan App terpasang di perangkat asli.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Perhatian: "Batasan tujuh hari" akun gratis

{class="mt-1"}
App bertanda tangan Apple ID gratis akan kedaluwarsa setelah 7 hari (jalankan ulang sekali untuk memperpanjang). Ini mekanisme anti penyalahgunaan Apple dan untuk tahap belajar sepenuhnya cukup; akun pengembang berbayar (99 dolar AS/tahun) tak punya batasan ini — dibahas rinci di Bab 67.
:::

#### 7. Uji coba pertama + Pertolongan pertama error umum

Buka ContentView.swift, ganti tulisan di dalam Text("Hello, world!") dengan namamu, tekan ⌘R untuk menjalankan ulang — beberapa detik kemudian namamu tampil di Simulator. Selamat, kamu baru saja menuntaskan siklus lengkap pertamamu "ubah kode → kompilasi → pasang → jalankan".

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Gejala error</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Penyebab umum</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Obatnya</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Error Signing</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Team belum dipilih, sertifikat kedaluwarsa</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Di Target → Signing centang akunmu; akun gratis tinggal jalankan ulang sekali</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Simulator layar hitam / tak mau terbuka</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Image Simulator rusak</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menu Device → Erase All Content; atau hapus lalu tambahkan ulang Simulator</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Unduhan Xcode lambat / gagal terpasang</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Koneksi App Store tidak stabil</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ganti waktu; atau unduh paket offline .xip dari situs pengembang Apple</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Tabel pertolongan pertama error lingkungan pemula

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Praktik: Tuntaskan daftar "ritual pengembangan"mu

{class="mt-1"}
① Pasang Xcode dan jalankan Simulator sampai jalan; ② jalankan App-mu sekali di perangkat asli dan simpan tangkapan layarnya sebagai kenangan; ③ ganti tulisan Hello dengan namamu; ④ ubah nama tampilan App menjadi "App Pertamaku" di pengaturan Target. Setelah empat langkah ini selesai, kamu resmi menjadi orang yang punya karya.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan bab

- Syarat mutlak: Mac + Xcode; tanpa Mac, belajar bahasanya dulu lewat Swift Playgrounds di iPad
- Xcode dipasang dari App Store; versi baru menuntut sistem baru, jangan tunda pembaruan
- Lima unsur proyek baru: nama, Team, pengenal organisasi, SwiftUI, Swift
- Jurus hafalan proyek: semua kode ada di folder MyFirstApp/; pengaturan Target mengurus versi dan penandatanganan
- Debug perangkat asli dengan Apple ID gratis punya batas tanda tangan 7 hari; akun berbayar tak ada batasan ini
- Rutinitas pengembangan = ubah kode → ⌘R → lihat hasil, berulang terus
:::
