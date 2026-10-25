---
id: di-liu-shi-zhang
num: 60
part: ios-kai-fa-pian
nav: Bab 60: Menyediakan Persekitaran Pembangunan—Xcode dan Projek Pertama
toc: default
kind: chapter
---

### Bab 60: Menyiapkan persekitaran pembangunan — Xcode dan projek pertama

{class="chapter-intro mb-4"}
Untuk kerja yang baik, pertajam dahulu alatnya. Dalam bab ini kita "menyiapkan dapur": memasang Xcode, memastikan simulator berjalan, mencipta projek iOS pertama dalam hidup anda, kemudian mengurai struktur projek sehingga jelas. Selepas persekitaran siap, anda akan buat pertama kali melihat kod yang anda tulis menjadi butang yang boleh ditekan — detik ini, ramai orang ingat seumur hidup.

#### 1. Sediakan sebuah Mac

Syarat dahulu: pembangunan iOS mesti dilakukan pada macOS. Jika anda tidak mempunyai Mac, ada tiga pilihan: beli satu (walaupun Mac mini atau MacBook Air terpakai pun cukup), sewa Mac awan untuk jangka pendek, atau baca dahulu Bahagian 8 "Amalan Pembangunan Android" (boleh dilakukan pada Windows).

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Perkara konfigurasi</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Keperluan minimum</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Tahap selesa (disyorkan)</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cip</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple Silicon (M1 ke atas)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">M2 atau lebih baharu</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Memori</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">8GB</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">16GB</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cakera</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ruang 40GB+ (Xcode sendiri sangat besar)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bermula 256GB</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sistem</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">macOS terkini</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kekalkan kemas kini automatik</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Rujukan konfigurasi mesin pembangunan Mac (Ogos 2026)

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Petua: boleh belajar bahasa dahulu walaupun tiada Mac

{class="mt-1"}
Swift Playgrounds yang percuma di iPad boleh mengajar asas bahasa Swift (tanpa Mac); malah boleh dipasang di iPhone juga. Kuasai dahulu pengetahuan bahasa Bab 61 dalam Playgrounds; apabila mendapat Mac, anda terus meluncur. "Mengasah kapak tidak melambatkan menebang kayu" — itulah maksudnya.
:::

#### 2. Memasang Xcode

Xcode ialah persekitaran pembangunan bersepadu rasmi Apple, percuma. Tiga langkah untuk memasang:

1. Di Mac, buka App Store, cari "Xcode", tekan pasang — ingat, saiznya beberapa GB, pilih waktu yang rangkaiannya laju;
2. Selepas terpasang, lancarkan buat kali pertama, setuju dengan perjanjian dan biar komponen selesai dipasang (berlaku secara automatik);
3. Menu Xcode → Settings → Locations, pastikan Command Line Tools telah dipilih — alat baris arahan ialah prasyarat bagi banyak skrip dan alat pihak ketiga.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Perhatian: "permainan padanan" antara versi dan sistem

{class="mt-1"}
Xcode baharu kerap menuntut macOS terkini, manakala Mac lama akan terkandas pada versi lama. Semasa menerbitkan ke App Store, Apple menuntut binaan dengan Xcode yang lebih baharu (biasanya diberikan tempoh tangguh). Jadi jangan tangguh kemas kini sistem terlalu lama — pembangun iOS antara kumpulan yang paling rajin mengejar versi baharu.
:::

#### 3. Mencipta projek pertama anda

Buka Xcode → Create New Project → pilih iOS → templat App, kemudian isi:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Perkara konfigurasi</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Apa yang diisi</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Penjelasan</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Product Name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstApp</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Nama aplikasi</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Team</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple ID anda (percuma)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Untuk tandatangan, akaun peribadi sudah cukup</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Organization Identifier</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">com.example</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Digabung dengan Product Name menjadi pengenal pakej</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Interface</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Rangka kerja garis utama buku ini</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Language</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tak perlu dijelaskan</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Lima perkara yang diisi semasa mencipta projek

Selepas menekan Create, Xcode akan menjana projek yang boleh terus dijalankan. Pilih satu simulator di penjuru kiri atas (contohnya iPhone 17), tekan ▶ untuk menjalankan — beberapa saat kemudian, di skrin simulator muncul satu tetingkap bertulis "Hello, world!". Aplikasi iOS pertama anda telah dilahirkan.

#### 4. Mengurai struktur projek: apa fungsi setiap fail

Di sebelah kiri ialah navigator projek; pemula hanya perlu mengenali beberapa ini:

::: div .figure
```html
<svg style="max-width:100%;height:auto" width="600" height="290" viewBox="0 0 600 290" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="600" height="290" fill="#fafafa" rx="8"/>
      <text x="20" y="28" font-size="13" font-weight="bold" fill="#111827">MyFirstApp/ direktori akar projek</text>
      <rect x="30" y="42" width="540" height="225" fill="#ffffff" stroke="#d1d5db" rx="6"/>
      <rect x="45" y="56" width="250" height="196" fill="#eef2ff" rx="5"/>
      <text x="56" y="78" font-size="11" fill="#1e1b4b" font-weight="bold">MyFirstApp/ (direktori kod)</text>
      <text x="66" y="100" font-size="10" fill="#374151">├ MyFirstAppApp.swift  ← pintu masuk program</text>
      <text x="66" y="120" font-size="10" fill="#374151">├ ContentView.swift  ← antara muka utama</text>
      <text x="66" y="140" font-size="10" fill="#374151">└ Assets.xcassets  ← ikon, imej, warna</text>
      <text x="56" y="166" font-size="10" fill="#6b7280">(semua fail baru letak dalam direktori ini)</text>
      <text x="56" y="196" font-size="10" fill="#1e1b4b" font-weight="bold">Tab Info / Info.plist</text>
      <text x="66" y="216" font-size="10" fill="#6b7280">Pengisytiharan aplikasi: nama, kebenaran, tetapan</text>
      <rect x="310" y="56" width="245" height="196" fill="#f0fdf4" rx="5"/>
      <text x="321" y="78" font-size="11" fill="#065f46" font-weight="bold">Kedudukan penting lain</text>
      <text x="331" y="100" font-size="10" fill="#374151">📁 Preview Content/  ← bahan pratonton</text>
      <text x="331" y="122" font-size="10" fill="#374151"><i class="fas fa-bullseye mr-1"></i> Tetapan Target (ikon projek biru)</text>
      <text x="331" y="142" font-size="10" fill="#6b7280">— nombor versi, sistem minimum dan tandatangan semua di sini</text>
      <text x="331" y="168" font-size="10" fill="#374151"><i class="fas fa-flask mr-1"></i> MyFirstAppTests/  ← ujian unit</text>
      <text x="331" y="188" font-size="10" fill="#374151">📱 MyFirstAppUITests/ ← ujian paparan</text>
      <text x="331" y="216" font-size="10" fill="#9ca3af">(templat ujian sudah dijana, guna di Bab 67)</text>
    </svg>
```

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Rajah 2: Struktur projek Xcode yang wajib difahami pemula
:::

- MyFirstAppApp.swift: pintu masuk program; dalam SwiftUI ia hanya beberapa baris — "mula, kemudian paparkan antara muka utama";
- ContentView.swift: paparan antara muka utama; semua yang anda lihat sekarang ada di sini;
- Assets.xcassets: gudang sumber — ikon, imej dan warna diletakkan di sini;
- Tetapan Target: tekan ikon projek biru di sebelah kiri untuk masuk; nombor versi, versi iOS minimum dan tandatangan semuanya di dalamnya. Nama paparan aplikasi dan ikon juga dikonfigur di sini.

#### 5. Petua kecekapan Xcode: lima "senjata rahsia pintasan" pemula

Kuasai yang berikut, dan anda akan kelihatan "sangat profesional":

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Tindakan</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Pintasan</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Fungsi</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menjalankan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘R</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kompil dan jalankan</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Buka/tukar pratonton kanvas</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌥⌘↩</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Suis "apa yang dilihat itulah yang diperoleh"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Format inden</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌃I</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menyusun inden kod yang dipilih secara automatik</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Buka fail dengan pantas</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘O</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Taip nama fail, terbuka serta-merta (paling kerap digunakan!)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Komen/nyahkomen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Hidup/matikan kod dengan pantas semasa debug</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Pintasan papan kekunci Xcode yang kerap digunakan (lima serangkai pemula)

Dua faedah tersembunyi lagi: menjalankan beberapa simulator serentak (jalankan iPhone dan iPad pada masa yang sama untuk membandingkan susun atur) dan pustaka petikan kod (seret beberapa baris kod biasa ke panel Snippets di sebelah kanan, lain kali sisipkan dengan satu tekanan) — gunakan dahulu alat kecekapan ini, dan kemahiran tangan akan datang dengan sendirinya.

#### 6. Debug pada peranti sebenar: memasang aplikasi ke dalam iPhone anda

Walaupun simulator bagus, peranti sebenar tetap destinasi akhir. Dengan Apple ID percuma pun boleh debug pada peranti sebenar:

1. Sambungkan iPhone dengan kabel data (atau debug secara wayarles melalui Wi-Fi yang sama);
2. Dalam senarai peranti di bahagian atas Xcode, pilih telefon anda; kali pertama akan diminta log masuk Apple ID dan tandatangan dikonfigur secara automatik;
3. Di iPhone, [Tetapan] → [Am] → [VPN & Pengurusan Peranti] → percayai sijil pembangun anda;
4. Tekan ▶, dan aplikasi terpasang pada peranti sebenar.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Perhatian: "had tujuh hari" akaun percuma

{class="mt-1"}
Aplikasi yang ditandatangani dengan Apple ID percuma akan luput selepas 7 hari (jalankan semula sekali untuk memperbaharui). Ini mekanisme cegah penyalahgunaan Apple; untuk peringkat pembelajaran ia sudah cukup; akaun pembangun berbayar (99 dolar AS setahun) tiada had ini, diterangkan terperinci dalam Bab 67.
:::

#### 7. Ujian kemahiran pertama + pertolongan cemas ralat biasa

Buka ContentView.swift, tukar teks dalam Text("Hello, world!") kepada nama anda, tekan ⌘R untuk menjalankan semula — beberapa saat kemudian nama anda dipaparkan pada simulator. Tahniah, anda telah menamatkan pusingan penuh pertama "ubah kod → kompil → pasang → jalankan".

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Gejala ralat</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Punca biasa</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Penawar</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ralat Signing</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Team tidak dipilih, sijil luput</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Dalam Target → Signing, tandakan akaun anda; untuk akaun percuma, jalankan semula sekali</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Skrin simulator hitam/tidak boleh dibuka</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Imej rosak</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menu Device → Erase All Content; atau padam dan tambah semula simulator</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Muat turun Xcode perlahan/gagal dipasang</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Rangkaian App Store tidak stabil</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tukar waktu; atau muat turun pakej luar talian .xip dari laman pembangun Apple</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Jadual pertolongan cemas ralat persekitaran untuk pemula

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Praktik: lengkapkan senarai "ritual pembangunan" anda

{class="mt-1"}
① Pasang Xcode dan pastikan simulator berjalan; ② jalankan aplikasi anda sekali pada peranti sebenar dan simpan tangkapan skrin sebagai kenangan; ③ tukar teks Hello kepada nama anda; ④ dalam tetapan Target, tukar nama paparan aplikasi kepada "Aplikasi Pertama Saya". Selepas empat langkah ini, anda sudah ialah orang yang berkarya.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan bab ini

- Syarat wajib: Mac + Xcode; tiada Mac? Belajar bahasa dahulu dengan Swift Playgrounds di iPad
- Xcode dipasang dari App Store; versi baharu menuntut sistem baharu, jangan tangguh kemas kini
- Lima unsur projek baharu: nama, Team, pengenal organisasi, SwiftUI, Swift
- Petua projek: semua kod dalam direktori MyFirstApp/; tetapan Target mengurus versi dan tandatangan
- Debug peranti sebenar dengan Apple ID percuma ada had tandatangan 7 hari; akaun berbayar tiada had ini
- Rutinan pembangunan = ubah kod → ⌘R → lihat hasil, berulang-ulang
:::
