---
id: di-si-shi-jiu-zhang
num: 49
part: an-zhuo-kai-fa-pian
nav: Bab 49: Menyiapkan Lingkungan Pengembangan—Android Studio dan Proyek Pertama
toc: default
kind: chapter
---

### Bab 49: Menyiapkan Lingkungan Pengembangan—Android Studio dan Proyek Pertama

{class="chapter-intro mb-4"}
Ada pepatah: untuk bekerja dengan baik, tajamkan dulu alatmu. Di bab ini kita menyiapkan 'dapurnya': memasang Android Studio, menjalankan emulator, membuat proyek Android pertama dalam hidupmu, lalu membongkar struktur proyeknya sampai benar-benar paham. Setelah lingkungan siap, untuk pertama kalinya kamu akan melihat kode tulisanmu berubah menjadi tombol yang bisa ditekan—momen yang oleh banyak orang diingat seumur hidup.

#### 1. Memasang Android Studio

Android Studio adalah lingkungan pengembangan terpadu (IDE) resmi dari Google, gratis, dan fiturnya lengkap: menulis kode, melihat pratinjau tampilan, debugging, sampai mengemas aplikasi semuanya di dalamnya. Pemasangannya empat langkah:

1. Buka situs resmi developer.android.com/studio, unduh versi stabil terbaru (per Agustus 2026: versi setelah Narwhal; tersedia untuk Windows/Mac/Linux);
2. Jalankan berkas pemasangannya, tinggal klik 'Berikutnya' terus—wizard instalasi otomatis menyertakan Android SDK dan komponen emulator;
3. Saat dijalankan pertama kali, unduh komponen SDK sesuai petunjuk (cukup pakai pilihan bawaan; butuh beberapa menit dan beberapa GB ruang);
4. Setelah selesai kamu akan melihat halaman selamat datang—selamat, 'dapurnya' sudah terpasang.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Perhatian: Ketahui Persyaratan Perangkat Keras

{class="mt-1"}
Android Studio adalah 'pemakan memori': disarankan RAM minimal 16 GB (8 GB masih bisa jalan, tapi emulatornya agak tersendat saat dibuka), sediakan ruang disk lebih dari 20 GB, dan CPU yang mendukung virtualisasi (aktifkan VT-x/AMD-V di BIOS). Kalau komputermu memang tua, gunakan 'debugging ponsel asli' menggantikan emulator (dibahas di bagian 4 bab ini)—justru lebih lancar.
:::

#### 2. Membuat Proyek Pertamamu

Di halaman selamat datang klik New Project, pilih templat Empty Activity (templat paling bersih untuk pemula), lalu isi tiga hal:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Item Konfigurasi</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Isi Dengan Apa</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Keterangan</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">My First App</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Nama aplikasi, ditampilkan di layar utama ponsel</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Package name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">com.example.myfirstapp</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Identitas unik global; kebiasaannya 'domain dibalik', ikuti nilai bawaan dulu</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Minimum SDK</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">API 26(Android 8.0)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Versi minimum yang didukung, mencakup 95%+ perangkat</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Tiga hal yang diisi saat membuat proyek

Setelah klik Finish, Android Studio akan otomatis mengunduh dependensi dan membangun proyek dengan Gradle (pertama kali perlu menunggu beberapa menit, setelah itu jauh lebih cepat). Begitu build selesai, kamu punya aplikasi yang bisa jalan—walau untuk sekarang hanya menampilkan tulisan 'Hello Android!'.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tips: Seluk-Beluk Nama Paket

{class="mt-1"}
Nama paket (package name) ibarat 'nomor identitas' aplikasi; tidak boleh ada yang sama di seluruh dunia, dan setelah naik toko tidak bisa diubah lagi. Untuk latihan pribadi, com.example.xxx sudah cukup; produk resmi harus diganti dengan domainmu sendiri yang dibalik (misalnya com.namamu.namaaplikasi). Jangan pernah naik toko dengan com.example—toko akan menolaknya.
:::

#### 3. Menjalankannya: Emulator dan Ponsel Asli

Kode sudah ditulis, sekarang butuh 'ponsel' untuk menjalankannya. Kamu punya dua pilihan:

##### 1. Emulator

Emulator adalah ponsel Android yang divirtualisasi di dalam komputer. Di Android Studio buka Device Manager → Create Device, pilih satu perangkat (disarankan seri Pixel) → pilih citra sistem (yang ada Google APIs-nya) → unduh → jalankan. Lalu klik segitiga hijau Run di toolbar; beberapa detik kemudian aplikasimu muncul di layar 'ponsel' itu.

##### 2. Debugging Ponsel Asli (Lebih Disarankan)

Ponsel asli selalu jadi lingkungan uji paling nyata—rasa gesekannya, jaringannya, sensor aslinya, tidak ada yang bisa ditandingi emulator. Debugging dengan ponsel Android asli itu mudah:

1. Di ponsel buka [Pengaturan] → [Tentang Ponsel], ketuk 'Nomor Versi' 7 kali berturut-turut untuk mengaktifkan 'Opsi Pengembang';
2. Di [Opsi Pengembang], aktifkan USB Debugging;
3. Sambungkan ponsel ke komputer dengan kabel data; saat ponsel memunculkan popup, pilih 'Izinkan USB Debugging';
4. Kembali ke Android Studio, ponselmu akan muncul di daftar perangkat di toolbar, lalu klik Run.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Awas Jebakan: Jangan Biarkan USB Debugging Menyala Terus

{class="mt-1"}
USB Debugging ibarat membuka 'pintu belakang' bagi komputer. Saat mengisi daya di tempat umum atau menyambung ke komputer yang tidak dipercaya, wajib mematikan USB Debugging agar orang lain tidak bisa membaca datamu lewat jalur itu. Biasakan mematikannya setelah selesai dipakai untuk pengembangan.
:::

#### 4. Bedah Struktur Proyek: Untuk Apa Saja Tiap Berkas

Pertama kali membuka proyek, pohon berkas di sebelah kiri bisa membuatmu pusing. Tenang, 90% waktumu dalam pengembangan sehari-hari hanya berurusan dengan beberapa hal berikut:

::: div .figure
```html
<svg style="max-width:100%;height:auto" width="600" height="300" viewBox="0 0 600 300" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="600" height="300" fill="#fafafa" rx="8"/>
      <text x="20" y="30" font-size="13" font-weight="bold" fill="#111827">MyFirstApp/ direktori akar proyek</text>
      <rect x="30" y="45" width="540" height="230" fill="#ffffff" stroke="#d1d5db" rx="6"/>
      <text x="45" y="70" font-size="11" fill="#4f46e5" font-weight="bold">app/ ← tempat Anda menulis kode</text>
      <rect x="60" y="82" width="240" height="178" fill="#eef2ff" rx="5"/>
      <text x="70" y="102" font-size="10" fill="#1e1b4b" font-weight="bold">src/main/</text>
      <text x="80" y="120" font-size="10" fill="#374151">├ java/…/MainActivity.kt  ← kode logika</text>
      <text x="80" y="138" font-size="10" fill="#374151">├ res/  ← resource (gambar, teks, warna)</text>
      <text x="80" y="156" font-size="10" fill="#374151">└ AndroidManifest.xml  ← "akta lahir" aplikasi</text>
      <text x="70" y="180" font-size="10" fill="#1e1b4b" font-weight="bold">build.gradle.kts</text>
      <text x="80" y="198" font-size="10" fill="#6b7280">Deklarasikan library yang dipakai (versi SDK, Compose dll.)</text>
      <text x="70" y="222" font-size="10" fill="#1e1b4b" font-weight="bold">src/androidTest/ dan test/</text>
      <text x="80" y="240" font-size="10" fill="#6b7280">Kode test otomatis (dipakai di Bab 56)</text>
      <rect x="320" y="82" width="230" height="178" fill="#f0fdf4" rx="5"/>
      <text x="330" y="102" font-size="10" fill="#065f46" font-weight="bold">File lain di direktori akar</text>
      <text x="340" y="122" font-size="10" fill="#374151">gradle/ + gradlew.bat  ← skrip build</text>
      <text x="340" y="142" font-size="10" fill="#374151">settings.gradle.kts  ← pengaturan proyek</text>
      <text x="340" y="162" font-size="10" fill="#6b7280">(ngomongannya untuk pemula: cukup sentuh direktori app/ </text>
      <text x="340" y="180" font-size="10" fill="#6b7280">sisanya anggap dulu "kotak hitam", jangan diutak-atik)</text>
      <text x="340" y="208" font-size="10" fill="#9ca3af">.gitignore  ← daftar yang diabaikan version control</text>
    </svg>
```

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Gambar 2: Struktur proyek yang wajib dipahami pemula (pegangan: sentuh saja direktori app/)
:::

- MainActivity.kt: 'pintu gerbang' aplikasi. Saat pengguna mengetuk ikonnya, inilah yang pertama dibangunkan. Di templat sekarang, ia bertugas menampilkan 'Hello Android!'.
- AndroidManifest.xml: 'buku keluarga' aplikasi—menyatakan aplikasi ini bernama apa, ikonnya yang mana, ada halaman apa saja, dan izin apa saja yang dipakai (kamera, lokasi, dst.).
- Direktori res/: gudang sumber daya, menyimpan gambar, ikon, teks, warna. Menaruh teks di berkas sumber daya alih-alih menulisnya mati di kode adalah kebiasaan baik pengembangan Android (memudahkan ganti bahasa, ganti tema).
- build.gradle.kts: resep build—menyatakan versi minimum yang didukung dan pustaka apa saja yang dipakai (misalnya Compose).

#### 5. Coba-Coba: Ganti 'Hello' dengan Namamu

Buka MainActivity.kt, kamu akan melihat kode yang dihasilkan templat Compose. Temukan baris Text("Hello Android!") dan ganti teks di dalam tanda kutip dengan namamu, misalnya Text("Halo, Budi! Ini aplikasi pertamaku"), lalu tekan Ctrl+R (di Mac Cmd+R) untuk menjalankan ulang. Beberapa detik kemudian namamu tampil di emulator.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · MainActivity.kt (ubah baris ini)</span><span class="dots">···</span>
:::

```
setContent {
    MyFirstAppTheme {
        Surface(modifier = Modifier.fillMaxSize()) {
            // ▼ Ubah bagian ini menjadi teks Anda sendiri
            Text("Halo, Zhang San! Ini aplikasi pertamaku")
        }
    }
}
```
:::

Selamat, kamu baru saja menyelesaikan satu siklus lengkap 'ubah kode → kompilasi → pasang → jalankan'. Siklus inilah rutinitas pengembangan untuk setiap hari ke depan. Sekalian saja coba ubah yang lain: perbesar ukuran huruf, ganti warna—bab berikutnya kita akan belajar dari mana semua 'sihir' itu berasal.

#### 6. Pertolongan Pertama Error Umum: 'Ruang Gawat Darurat' Dua Pekan Pertama Pemula

Pada tahap penyiapan lingkungan dan build pertama, kemungkinan besar kamu akan menemui tiga error berikut. Tenang, semuanya ada penawarnya:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Gejala Error</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Penyebab Umum</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Penawarnya</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gradle sync failed / unduhan dependensi lambat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Akses jaringan ke repositori tidak lancar</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Konfigurasikan mirror repositori yang lebih cepat untuk Gradle (misalnya mirror maven Alibaba Cloud/Tencent Cloud), cari 'gradle mirror' di internet lalu ikuti petunjuknya</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Komponen SDK kurang</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Unduhan SDK terlewat saat instalasi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lengkapi platform dan alat yang kurang lewat Settings → SDK Manager</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Emulator gagal jalan / layar hitam</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Virtualisasi belum aktif, citra rusak</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Aktifkan VT-x/AMD-V di BIOS; hapus emulator lalu buat ulang; atau langsung pakai debugging ponsel asli</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Tabel pertolongan pertama error lingkungan untuk pemula

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tips: Metode Mencari Error

{class="mt-1"}
Baris pertama pesan error paling bernilai—salin persis ke mesin pencari, tambahkan kata kunci 'android studio'. Jangan mencari pertanyaan yang terlalu umum seperti 'kenapa environment saya gagal terpasang'; cari error yang spesifik seperti 'Gradle sync failed: Could not resolve com.android.tools.build'. Pertanyaan yang presisi baru menghasilkan jawaban yang presisi.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Praktik: Selesaikan Daftar 'Ritual Peresmian' Pengembangmu

{class="mt-1"}
① Pasang Android Studio dan berhasil menjalankan emulator; ② jalankan aplikasimu sendiri sekali di ponsel asli dan simpan tangkapan layarnya; ③ ubah teks Hello menjadi namamu; ④ arsipkan proyeknya dalam bentuk zip. Selesai empat langkah ini, kamu berhak mengumumkan di media sosial: aku juga pengembang Android sekarang (bukti tangkapan layar).
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan Bab Ini

- Android Studio = IDE resmi gratis; disarankan RAM 16 GB + disk 20 GB + aktifkan virtualisasi
- Tiga unsur proyek baru: nama, nama paket (unik global, jangan naik toko dengan com.example), SDK minimum (mulai API 26)
- Dua cara menjalankan: emulator (ponsel virtual di komputer) dan ponsel asli (aktifkan USB Debugging, ingat dimatikan setelah pakai)
- Pegangan proyek: sentuh saja direktori app/—MainActivity.kt pintu gerbang, Manifest buku keluarga, res/ gudang sumber daya
- Rutinitas pengembangan = ubah kode → Run → lihat hasilnya, berulang-ulang
:::
