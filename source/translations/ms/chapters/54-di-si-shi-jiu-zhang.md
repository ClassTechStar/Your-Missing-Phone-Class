---
id: di-si-shi-jiu-zhang
num: 49
part: an-zhuo-kai-fa-pian
nav: Bab 49: Menyediakan Persekitaran Pembangunan—Android Studio dan Projek Pertama
toc: default
kind: chapter
---

### Bab 49: Membina Persekitaran Pembangunan — Android Studio dan Projek Pertama

{class="chapter-intro mb-4"}
Ingin membuat kerja dengan baik, tajamkan dahulu peralatan anda. Dalam bab ini kita 'memasang dapur': memasang Android Studio, menjayakan emulator, mencipta projek Android pertama dalam hidup anda, kemudian membongkar struktur projek untuk difahami dengan jelas. Selepas persekitaran siap dipasang, anda buat pertama kalinya akan melihat kod yang anda tulis bertukar menjadi butang yang boleh ditekan — detik ini, ramai orang ingat seumur hidup.

#### 1. Memasang Android Studio

Android Studio ialah persekitaran pembangunan bersepadu (IDE) rasmi Google, percuma, dengan pakej fungsi lengkap: menulis kod, melihat pratonton antara muka, menyahpepijat, membungkus — semuanya di dalamnya. Empat langkah pemasangan:

1. Buka laman rasmi developer.android.com/studio dan muat turun versi stabil terkini (pada Ogos 2026, versi selepas Narwhal; ada untuk Windows/Mac/Linux);
2. Jalankan pemasang, klik 'Seterusnya' dari mula hingga akhir — pembimbing pemasangan akan membawa Android SDK dan komponen emulator secara automatik;
3. Semasa dilancarkan buat kali pertama, muat turun komponen SDK mengikut arahan (cukup guna pilihan lalai; mungkin mengambil masa beberapa minit dan beberapa GB ruang);
4. Selepas selesai, anda akan melihat halaman alu-aluan — tahniah, 'dapur' sudah siap.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Perhatian: Fahami Keperluan Perkakasan

{class="mt-1"}
Android Studio ialah 'pemakan memori': disyorkan sekurang-kurangnya 16GB RAM (8GB pun boleh berjalan, tetapi emulator agak tersekat apabila dibuka), sediakan ruang cakera melebihi 20GB, dan CPU mesti menyokong virtualisasi (aktifkan VT-x/AMD-V dalam BIOS). Jika komputer anda memang tua, boleh guna 'penyahpepijatan peranti sebenar' sebagai ganti emulator (diterangkan dalam Bahagian 4 bab ini); pengalamannya malah lebih lancar.
:::

#### 2. Mencipta Projek Pertama Anda

Di halaman alu-aluan, klik New Project, pilih templat Empty Activity (templat paling bersih untuk pemula), kemudian isi tiga perkara:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Item konfigurasi</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Apa diisi</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Penerangan</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">My First App</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Nama aplikasi, dipaparkan pada skrin utama telefon</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Package name</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">com.example.myfirstapp</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pengenal unik sejagat; lazimnya 'domain terbalik', ikut lalai dahulu</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Minimum SDK</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">API 26(Android 8.0)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Versi sokongan minimum, meliputi 95%+ peranti</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Tiga perkara yang perlu diisi semasa mencipta projek

Selepas klik Finish, Android Studio akan memuat turun kebergantungan dan membina projek secara automatik dengan Gradle (kali pertama perlu menunggu beberapa minit; selepas itu jauh lebih pantas). Setelah siap dibina, anda mempunyai apl yang boleh berjalan — walaupun ia buat sementara hanya memaparkan satu baris "Hello Android!".

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Petua: Selok-belok Nama Pakej

{class="mt-1"}
Nama pakej (package name) seperti 'nombor kad pengenalan' aplikasi; tidak boleh berulang di seluruh dunia, dan tidak boleh diubah selepas diterbitkan. Untuk latihan peribadi, com.example.xxx sudah memadai; produk sebenar mesti diganti dengan domain terbalik anda sendiri (contohnya com.nama.anda.namaaplikasi). Jangan terbitkan dengan com.example — kedai akan menolaknya.
:::

#### 3. Menjalankannya: Emulator dan Peranti Sebenar

Kod sudah siap ditulis, kena cari 'telefon' untuk menjalankannya. Anda ada dua pilihan:

##### 1. Emulator

Emulator ialah telefon Android yang dimayakan di dalam komputer. Dalam Android Studio, buka Device Manager → Create Device, pilih satu peranti (disyorkan siri Pixel) → pilih satu imej sistem (yang membawa Google APIs) → muat turun → mula. Kemudian tekan segi tiga hijau Run pada bar alat; beberapa saat kemudian, apl anda akan muncul pada skrin 'telefon' itu.

##### 2. Penyahpepijatan peranti sebenar (lebih disyorkan)

Peranti sebenar sentiasa menjadi persekitaran ujian paling sebenar — rasa geseran semasa meluncur, rangkaian sebenar, sensor sebenar; emulator tidak dapat menandinginya. Penyahpepijatan peranti Android sebenar sangat mudah:

1. Pada telefon, buka [Tetapan] → [Mengenai Telefon], ketik 'Nombor Binaan' 7 kali berturut-turut untuk mengaktifkan 'Pilihan Pembangun';
2. Dalam [Pilihan Pembangun], aktifkan Penyahpepijatan USB;
3. Sambungkan telefon ke komputer dengan kabel data, dan pada tetingkap timbul telefon pilih 'Benarkan penyahpepijatan USB';
4. Kembali ke Android Studio; telefon anda akan muncul dalam senarai juntai bawah peranti pada bar alat, kemudian tekan Run.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Amaran Perangkap: Jangan Biarkan Penyahpepijatan USB Sentiasa Aktif

{class="mt-1"}
Penyahpepijatan USB umpama membuka 'pintu belakang' kepada komputer. Semasa mengecas di tempat awam atau menyambung kepada komputer yang tidak dipercayai, pastikan anda mematikan Penyahpepijatan USB untuk menghalang orang lain membaca data anda melaluinya. Matikan terus selepas selesai membangun — jadikan tabiat.
:::

#### 4. Membongkar Struktur Projek: Apa Fungsi Setiap Fail

Kali pertama membuka projek, pepohon fail di sebelah kiri mungkin membuatkan anda pening. Jangan panik; dalam pembangunan harian, 90% masa anda hanya berurusan dengan beberapa yang berikut:

::: div .figure
```html
<svg style="max-width:100%;height:auto" width="600" height="300" viewBox="0 0 600 300" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="600" height="300" fill="#fafafa" rx="8"/>
      <text x="20" y="30" font-size="13" font-weight="bold" fill="#111827">MyFirstApp/ direktori akar projek</text>
      <rect x="30" y="45" width="540" height="230" fill="#ffffff" stroke="#d1d5db" rx="6"/>
      <text x="45" y="70" font-size="11" fill="#4f46e5" font-weight="bold">app/ ← tempat anda menulis kod</text>
      <rect x="60" y="82" width="240" height="178" fill="#eef2ff" rx="5"/>
      <text x="70" y="102" font-size="10" fill="#1e1b4b" font-weight="bold">src/main/</text>
      <text x="80" y="120" font-size="10" fill="#374151">├ java/…/MainActivity.kt  ← kod logik</text>
      <text x="80" y="138" font-size="10" fill="#374151">├ res/  ← sumber (imej, teks, warna)</text>
      <text x="80" y="156" font-size="10" fill="#374151">└ AndroidManifest.xml  ← "surat beranak" aplikasi</text>
      <text x="70" y="180" font-size="10" fill="#1e1b4b" font-weight="bold">build.gradle.kts</text>
      <text x="80" y="198" font-size="10" fill="#6b7280">Isytiharkan pustaka yang digunakan (versi SDK, Compose dll.)</text>
      <text x="70" y="222" font-size="10" fill="#1e1b4b" font-weight="bold">src/androidTest/ dan test/</text>
      <text x="80" y="240" font-size="10" fill="#6b7280">Kod ujian automatik (guna di Bab 56)</text>
      <rect x="320" y="82" width="230" height="178" fill="#f0fdf4" rx="5"/>
      <text x="330" y="102" font-size="10" fill="#065f46" font-weight="bold">Fail lain dalam direktori akar</text>
      <text x="340" y="122" font-size="10" fill="#374151">gradle/ + gradlew.bat  ← skrip binaan</text>
      <text x="340" y="142" font-size="10" fill="#374151">settings.gradle.kts  ← tetapan projek</text>
      <text x="340" y="162" font-size="10" fill="#6b7280">(kata azam orang baru: sentuh direktori app/ sahaja </text>
      <text x="340" y="180" font-size="10" fill="#6b7280">yang selebihnya anggap dulu "kotak hitam", jangan diusik)</text>
      <text x="340" y="208" font-size="10" fill="#9ca3af">.gitignore  ← senarai diabaikan kawalan versi</text>
    </svg>
```

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Rajah 2: Struktur projek yang wajib difahami pemula (rumus: sentuh hanya direktori app/)
:::

- MainActivity.kt: 'Pintu gerbang' aplikasi. Apabila pengguna mengetik ikon, inilah yang pertama dibangunkan. Dalam templat masa kini, ia bertanggungjawab memaparkan "Hello Android!".
- AndroidManifest.xml: 'Buku daftar' aplikasi — mengisytiharkan nama aplikasi ini, ikon yang mana, halaman apa yang ada, dan kebenaran apa yang diperlukan (kamera, lokasi dan sebagainya).
- Direktori res/: gudang sumber, menyimpan imej, ikon, rentetan, warna. Meletakkan teks dalam fail sumber dan bukannya menulis terus dalam kod ialah tabiat baik pembangunan Android (mudah untuk tukar bahasa, tukar tema).
- build.gradle.kts: resipi binaan — mengisytiharkan versi sokongan minimum dan pustaka kebergantungan (contohnya Compose).

#### 5. Uji Kemahiran: Gantikan 'Hello' dengan Nama Anda

Buka MainActivity.kt dan anda akan melihat kod yang dijana oleh templat Compose. Cari baris Text("Hello Android!"), gantikan teks dalam tanda petik dengan nama anda, contohnya Text("Hai, Ali! Ini aplikasi pertama saya"), kemudian tekan Ctrl+R (Cmd+R pada Mac) untuk menjalankan semula. Beberapa saat kemudian, nama anda terpamer pada emulator.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · MainActivity.kt (ubah baris ini)</span><span class="dots">···</span>
:::

```
setContent {
    MyFirstAppTheme {
        Surface(modifier = Modifier.fillMaxSize()) {
            // ▼ Tukar bahagian ini kepada teks anda sendiri
            Text("Hai, Zhang San! Ini aplikasi pertama saya")
        }
    }
}
```
:::

Tahniah, anda telah melengkapkan satu kitaran penuh 'ubah kod → bina → pasang → jalankan'. Kitaran inilah rutin pembangunan harian anda pada masa hadapan. Sementara masih hangat, cuba ubah sesuatu yang lain: besarkan saiz fon, tukar warna — bab seterusnya kita akan belajar bagaimana 'sihir' ini datang.

#### 6. Pertolongan Cemas Ralat Biasa: 'Bilik Kecemasan' Dua Minggu Pertama Pemula

Pada peringkat penyediaan persekitaran dan binaan pertama, anda berkemungkinan besar menghadapi tiga ralat berikut. Jangan panik; semuanya ada penawar:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Gejala ralat</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Punca biasa</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Penawar</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gradle sync failed / muat turun kebergantungan lambat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Akses rangkaian ke repositori tidak lancar</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Konfigurasikan repositori cermin tempatan untuk Gradle (cermin maven Aliyun/Tencent Cloud), cari 'gradle mirror tempatan' di internet dan ubah mengikut arahan</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Komponen SDK tidak lengkap</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Muat turun SDK dilangkau semasa pemasangan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Settings → SDK Manager untuk memasang platform dan alat yang kurang</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Emulator gagal dimulakan / skrin hitam</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Virtualisasi tidak diaktifkan; imej rosak</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Aktifkan VT-x/AMD-V dalam BIOS; padam emulator dan bina semula; atau guna terus penyahpepijatan peranti sebenar</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Jadual pertolongan cemas ralat persekitaran untuk pemula

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Petua: Metodologi Mencari Ralat

{class="mt-1"}
Baris pertama mesej ralat paling bernilai — salinkan apa adanya ke dalam enjin carian, tambah kata kunci "android studio". Jangan cari soalan umum seperti "kenapa saya tidak boleh pasang persekitaran", cari ralat spesifik seperti "Gradle sync failed: Could not resolve com.android.tools.build". Soalan yang tepat barulah menghasilkan jawapan yang tepat.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mari cuba: Lengkapkan senarai 'ritual pembangun' anda

{class="mt-1"}
① Pasang Android Studio dan jayakan emulator; ② jalankan aplikasi anda sekali pada peranti sebenar dan simpan tangkapan skrin sebagai kenangan; ③ ubah teks Hello kepada nama anda; ④ mampatkan projek sebagai arkib simpanan. Selepas melengkapkan empat langkah ini, anda boleh mengumumkan di media sosial: saya kini juga seorang pembangun Android (tangkapan skrin sebagai bukti).
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan Bab

- Android Studio = IDE rasmi percuma; disyorkan 16GB RAM + 20GB cakera + aktifkan virtualisasi
- Tiga elemen projek baharu: nama, nama pakej (unik sejagat, jangan terbitkan dengan com.example), SDK minimum (mulai API 26)
- Dua cara menjalankan: emulator (telefon maya dalam komputer) dan peranti sebenar (aktifkan penyahpepijatan USB, ingat matikan selepas guna)
- Rumus projek: sentuh hanya direktori app/ — MainActivity.kt ialah pintu gerbang, Manifest ialah buku daftar, res/ ialah gudang sumber
- Rutin pembangunan = ubah kod → Run → lihat hasil, berulang-ulang
:::
