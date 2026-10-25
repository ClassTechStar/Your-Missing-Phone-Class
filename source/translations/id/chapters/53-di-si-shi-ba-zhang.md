---
id: di-si-shi-ba-zhang
num: 48
part: an-zhuo-kai-fa-pian
nav: Bab 48: Mengenal Android—Dari Sistem Operasi hingga Ekosistem Pengembangan
toc: default
kind: chapter
---

### Bab 48: Mengenal Android — Dari Sistem Operasi hingga Ekosistem Pengembangan

{class="chapter-intro mb-4"}
Selamat atas keputusan ini—dari "orang yang memakai ponsel" menjadi "orang yang membuat aplikasi ponsel". Sebelum mulai praktik, mari kita buka petanya dulu: dari mana Android berasal? Mengapa pengembang di seluruh dunia rajin membuat aplikasi untuknya? Apa saja yang terjadi dari jari menyentuh keyboard sampai aplikasinya ada di ponsel pengguna?

#### 1. Silsilah Android: dari "robot kecil" menjadi "sistem terbesar di dunia"

Kisah Android dimulai pada 2003—seorang insinyur bernama Andy Rubin mendirikan perusahaan Android dengan tujuan yang sederhana: membuat sistem operasi pintar yang "lebih paham kamera". Kemudian Google mengakuisisinya pada 2005, pada 2007 bersama puluhan vendor mendirikan Open Handset Alliance (OHA), dan pada September 2008 ponsel Android pertama, HTC Dream (G1), resmi dijual.

Cerita setelahnya sudah kamu tahu: sampai 2026, Android adalah sistem operasi mobile dengan pangsa pasar terbesar di dunia, dengan jumlah perangkat aktif dihitung dalam miliaran. Ponselmu, kotak TV, layar besar di mobil, jam pintarmu—kemungkinan besar semuanya menjalankan Android. Apa artinya? Artinya setiap baris kode yang kamu tulis berpeluang dipakai oleh paling banyak orang di dunia.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tips: gen open source Android

{class="mt-1"}
Kode inti Android (AOSP, Android Open Source Project) bersifat open source—vendor mana pun bebas mengambilnya, memodifikasinya, dan menyesuaikannya. Karena itu ada MIUI milik Xiaomi (sekarang bernama HyperOS), lapisan kompatibilitas HarmonyOS milik Huawei, dan One UI milik Samsung. Ini kabar baik bagi pengembang: yang kamu pelajari adalah "pengembangan Android", bukan "pengembangan merek tertentu"—satu keahlian, berlaku di semua merek.
:::

Evolusi nomor versinya juga menarik: mulai dari Cupcake (kue cup) di versi 1.5, setiap versi besar dinamai dengan nama makanan penutup—Donut, Eclair, Frozen Yogurt, Gingerbread... sampai Android 10 pada 2019 akhirnya berganti menjadi angka murni. Per Agustus 2026, versi resmi terbaru adalah Android 17, sementara "versi dukungan minimum" yang benar-benar perlu kamu pedulikan saat mengembangkan biasanya dipatok aplikasi populer antara Android 8 (API 26) dan Android 10 (API 29)—mendukung perangkat beberapa tahun lalu membuat cakupan penggunamu cukup besar.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Versi</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Kode nama/tahun</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Hal penting bagi pengembang</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 8 (API 26)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Oreo · 2017</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kanal notifikasi, pembatasan latar belakang—batas minimum banyak perangkat lama</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 10 (API 29)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2019</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Munculnya penyimpanan terpartisi (scoped storage), aturan akses berkas berubah besar</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 12 (API 31)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2021</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Material You dengan warna dinamis, tampilan antarmuka terdongkrak besar</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 13 (API 33)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2022</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Izin notifikasi saat runtime, dialog bertanya "boleh mengirim notifikasi atau tidak"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 14-15 (API 34-35)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2023-2024</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gestur kembali prediktif, halaman 16KB, privasi makin ketat</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 16-17 (API 36-37)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2025-2026</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ritme versi minor lebih cepat, integrasi kemampuan AI (seperti ekstensi Gemini)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Sejarah singkat versi Android (per Agustus 2026, hal yang paling diperhatikan saat pengembangan)

#### 2. Menulis dengan bahasa apa: Java atau Kotlin?

Dalam sejarah pengembangan Android ada dua bahasa utama. Java adalah "bapak pendiri"—dipakai sejak Android pertama lahir; Kotlin adalah "warga kelas satu" yang ditunjuk Google pada 2017, dan sejak 2019 posisi resminya "Kotlin dulu" (Kotlin-first). Menjelang 2026, hampir semua proyek baru memakai Kotlin, dan proyek-proyek lama pun sebagian besar sedang bermigrasi.

Kata jujur saja: kalau kamu benar-benar tanpa dasar, langsung belajar Kotlin, jangan mundur ke Java. Ada tiga alasan: pertama, jumlah kode Kotlin 30%-40% lebih sedikit daripada Java (fungsi yang sama, Kotlin lebih pendek dan jernih); kedua, Kotlin secara bawaan mencegah "null pointer", mimpi buruk para pemula; ketiga, semua tutorial modern, dokumentasi resmi, dan alat pemrograman AI (masih ingat buku pemrograman AI kita?) menjadikan Kotlin sebagai standar. Java hanya akan kamu temui saat merawat proyek lama atau membaca kode lama.

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
Gaya Java (versi bertele-tele)

{class="font-mono text-xs leading-relaxed"}
public class MainActivity extends Activity {<br>&nbsp;&nbsp;@Override<br>&nbsp;&nbsp;protected void onCreate(Bundle b) {<br>&nbsp;&nbsp;&nbsp;&nbsp; super.onCreate(b);<br>&nbsp;&nbsp;&nbsp;&nbsp; setContentView(R.layout.activity);<br>&nbsp;&nbsp;}<br>}
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
Gaya Kotlin (versi ringkas)

{class="font-mono text-xs leading-relaxed"}
class MainActivity : ComponentActivity() {<br>&nbsp;&nbsp;override fun onCreate(b: Bundle?) {<br>&nbsp;&nbsp;&nbsp;&nbsp; super.onCreate(b)<br>&nbsp;&nbsp;&nbsp;&nbsp;setContent { App() }<br>&nbsp;&nbsp;}<br>}
:::
:::

Untuk hal yang sama, Kotlin menghemat banyak kurung kurawal dan tulisan boilerplate. Bab 50 nanti kita pelajari resmi; untuk sekarang cukup ingat: "bahasa nasional" pengembangan Android bernama Kotlin.

#### 3. Bagaimana sebuah App lahir?

Banyak orang mengira "mengembangkan App" itu membuka komputer lalu mengetik kode sekuat hati. Nyatanya, dari ide sampai berada di ponsel pengguna, sebuah App menempuh lini produksi kurang lebih seperti ini:

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-lightbulb mr-1"></i> Ide</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center">📐 Desain (tampilan+fungsi)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-keyboard mr-1"></i> Menulis kode</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hammer mr-1"></i> Kompilasi dan kemas (APK/AAB)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> Pengujian (emulator+perangkat nyata)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-rocket mr-1"></i> Rilis (store/paket instalasi)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Gambar 1: Alur lengkap sebuah App Android dari ide hingga rilis di toko
:::

Ada dua konsep dalam alur ini yang harus kamu kenal sekarang:

- APK: format paket instalasi aplikasi Android (.apk), bisa langsung dipasang ke ponsel dengan sekali klik, seperti .exe di Windows. Untuk pengujian sendiri atau sekadar membagikan ke teman, pakailah ini.
- AAB: Android App Bundle (.aab), "format pengemasan premium" untuk rilis di Google Play. Toko akan memotongnya secara dinamis sesuai model ponsel pengguna sehingga paket yang diunduh tiap orang lebih kecil. Tidak bisa dipasang sendiri, hanya bisa diserahkan ke toko.

Selain itu kamu akan terus mendengar satu istilah: SDK (Software Development Kit, perangkat lunak pengembangan). Inilah satu set "perlengkapan pengembangan" lengkap dari Android resmi—mencakup pustaka API berbagai versi, alat debugging, citra emulator, dan sebagainya. Kelas-kelas seperti Activity dan Button yang kamu panggil saat menulis kode semuanya berasal dari SDK.

#### 4. Peta penuh tumpukan teknologi Android: "daftar senjata"-mu

Sebelum belajar resmi, kenali dulu konfigurasi standar proyek Android populer tahun 2026—tidak masalah kalau daftar ini belum kamu pahami sekarang; kembali lagi setelah selesai membaca buku ini, semuanya akan terasa jernih:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Lapisan</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Pilihan populer (2026)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Untuk apa</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bahasa</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin 2.x</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bahasa untuk menulis logika</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Antarmuka</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Jetpack Compose + Material 3</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menggambar antarmuka lewat kode (jalur utama buku ini)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Arsitektur</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MVVM + ViewModel</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Memisahkan antarmuka dan logika agar kode tidak berantakan</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Penyimpanan data</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room (database) + DataStore (konfigurasi)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menyimpan data ke dalam ponsel</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Jaringan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit + OkHttp + coroutine Kotlin</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Berbicara dengan server</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Alat build</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gradle + Kotlin DSL</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mengubah kode menjadi paket instalasi</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lingkungan pengembangan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android Studio</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">IDE "paket lengkap" resmi Google</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Sekilas tumpukan teknologi Android populer tahun 2026

Jangan gentar oleh rangkaian istilah berbahasa Inggris ini. Semuanya seperti panci dan wajan di dapur—untuk sekarang kamu cukup tahu "memasak harus masuk dapur"; cara memakai masing-masing akan kita bedah satu per satu di bab-bab berikutnya. Kabar baiknya: saat membuat proyek baru, Android Studio otomatis menyiapkan seluruh rangkaian ini untukmu, dan kamu tinggal memasak.

#### 5. Android vs iOS: "pelajaran memilih kubu" pertama bagi pengembang

Mungkin kamu sedang memegang perangkat Android dan Apple sekaligus. Sebagai pengembang, perbedaan pengalaman kedua sisi patut dipahami sejak awal—bukan menentukan sikap "mana yang lebih baik", melainkan menghitung secara realistis "sisi mana yang lebih cocok untukmu memulai":

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Aspek</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Pengembangan Android</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Pengembangan iOS</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Komputer pengembangan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Windows / Mac / Linux semuanya bisa</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Wajib Mac (Xcode eksklusif)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Alat pengembangan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android Studio (gratis)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode (gratis) + biaya tahunan rilis 99 dolar AS</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tinjauan rilis di toko</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Longgar, beberapa jam hingga beberapa hari</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ketat, 1-7 hari adalah hal biasa</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pasang dan coba di perangkat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">APK bisa dibagikan dan dipasang dengan bebas</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Distribusi dibatasi; pengujian butuh penandatanganan/TestFlight</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lingkungan pendapatan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Terutama iklan/kanal lokal</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kebiasaan membayar pembelian dalam aplikasi (in-app purchase) di App Store lebih baik</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Biaya belajar</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Konsepnya lebih banyak (empat komponen utama, dll.)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ekosistem tertutup tapi sistemnya seragam, dokumentasinya prima</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Perbandingan jalur pengembangan Android vs iOS (Agustus 2026)

Jujur saja: kalau komputermu bukan Mac, soal ini tidak perlu dipikirkan lagi—Android adalah satu-satunya pilihan. Kalau kamu punya Mac, Bagian 8 dan Bagian 9 buku ini bisa dibaca berdampingan karena pola pikirnya saling terkait; setelah menguasai salah satunya, mempelajari yang lain akan jauh lebih cepat.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Praktik: Lihat 'Android' di Dalam Ponselmu

{class="mt-1"}
Buka [Pengaturan] → [Tentang Ponsel] (atau 'Tentang Perangkat') di ponselmu, cari baris 'Versi Android'—ketuk baris itu beberapa kali berturut-turut, kamu bahkan bisa memunculkan permainan easter egg bawaan sistem. Catat nomor versimu, lalu cocokkan dengan tabel versi di atas untuk melihat generasinya. Ponselmu adalah 'perangkat uji' pertamamu.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan Bab Ini

- Android lahir tahun 2008; pada 2026 ia adalah sistem mobile dengan pangsa pasar terbesar di dunia, dengan perangkat aktif mencapai miliaran
- Versi resmi terbaru Android 17; aplikasi populer mendukung minimal Android 8-10 agar cakupan penggunanya cukup besar
- Proyek baru selalu pakai Kotlin: kode hemat 30%+, bebas null pointer, pilihan resmi Google
- APK dipasang sendiri, AAB untuk toko aplikasi; SDK adalah paket peralatan pengembangan resmi
- Tumpukan teknologi standar 2026: Kotlin + Compose + MVVM + Room + Retrofit + Gradle + Android Studio
:::
