---
id: di-wu-shi-er-zhang
num: 52
part: an-zhuo-kai-fa-pian
nav: Bab 52: Empat Komponen Utama dan Siklus Hidup Activity
toc: default
kind: chapter
---

### Bab 52: Empat Komponen Utama dan Siklus Hidup Activity

{class="chapter-intro mb-4"}
Kalau Compose adalah 'wajah' aplikasi, bab ini membahas 'kerangka'-nya. Android punya empat komponen dasar; semua aplikasi tersusun daripadanya. Dan yang terpenting, Activity memiliki 'peta siklus hidup' yang wajib terpatri di kepala setiap pengembang Android. Selesai bab ini, kamu bisa memahami teka-teki abadi seperti 'kenapa setelah pindah ke latar belakang lalu kembali, state aplikasiku hilang'.

#### 1. Empat Komponen Utama: 'Tiang Utama' Android

Android secara resmi mendefinisikan empat komponen dasar, masing-masing bertanggung jawab atas satu jenis pekerjaan:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Komponen</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Tugasnya</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ibaratnya</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Activity</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Satu antarmuka yang terlihat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Etalase toko—bisa dilihat dan bisa diajak berinteraksi oleh pengguna</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Service</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">'Orang tak terlihat' yang bekerja di belakang layar</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pekerja gudang—memutar musik, mengunduh berkas, tanpa perlu antarmuka</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">BroadcastReceiver</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menerima siaran sistem</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ruang penjaga—'pengeras suara' yang meneriakkan 'baterai mau habis', 'jaringan putus'</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ContentProvider</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Berbagi data antar aplikasi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lemari arsip umum—misalnya membagikan kontak ke aplikasi lain</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Sekilas empat komponen utama Android

Di fase pemula, 95% waktumu berkutat dengan Activity; Service dan BroadcastReceiver dipakai saat memutar musik atau mengirim push notification; ContentProvider paling jarang dipakai (data yang umum sudah dibungkus rapi oleh sistem). Catatan lagi: keempat komponen utama wajib 'mendaftar' di AndroidManifest.xml; kalau tidak terdaftar, sistem tidak akan menemukannya.

#### 2. Siklus Hidup Activity: 'Peta Harta Karun' Pertama Pengembangan Android

Aplikasi di ponsel kapan pun bisa terinterupsi: ada telepon masuk, pengguna berpindah ke WeChat untuk membalas pesan, sistem kehabisan memori lalu menutupmu... Seumur hidup Activity adalah berkeliling di peta ini:

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onCreate (lahir: inisialisasi)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onStart (sudah terlihat)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onResume (aktif di depan)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center">onPause (sebagian tertutup)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center">onStop (tidak terlihat sama sekali)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center">onDestroy (dimusnahkan)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center">🔁 onRestart / onStart / onResume: kembali ke depan lewat jalur yang sama</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Gambar 4: Siklus hidup Activity (arah maju: baris atas lahir → baris bawah pergi; saat kembali, lewat jalur yang sama secara terbalik)
:::

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Callback</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Kapan Dipicu</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Kegunaan Tipikal</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onCreate</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Saat Activity dibuat (sekali)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Memuat antarmuka, inisialisasi data</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onStart</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Antarmuka menjadi terlihat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Memulai beberapa logika ringan</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onResume</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mendapat fokus, bisa berinteraksi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Memulai animasi, melanjutkan pemutaran</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onPause</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Saat tertutup sebagian/berpindah</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menghentikan animasi, menyimpan draf</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onStop</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sama sekali tidak terlihat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Melepas sumber daya berat, menghentikan unduhan</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onDestroy</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sebelum dihancurkan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pembersihan terakhir</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Kegunaan tipikal enam callback siklus hidup

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Awas Jebakan: Memutar Layar Akan 'Membunuh' Activity

{class="mt-1"}
Adegan gagal paling klasik pemula: layar diputar, teks di kolom input hilang semua. Penyebabnya: memutar layar secara bawaan akan menghancurkan lalu membangun ulang Activity (melewati onDestroy → onCreate). Solusinya: pakai rememberSaveable untuk menyimpan state (pengganti remember di Compose), ia otomatis mengembalikan nilai saat dibangun ulang. Bab 6 dan 7 akan sering memakainya.
:::

#### 3. Intent: 'Tiket' Perjalanan di Dalam dan Luar Aplikasi

Intent (niat) adalah 'tiket' komunikasi antar komponen. Ingin berpindah dari satu halaman ke halaman lain, membuka peramban, atau memanggil kamera? Semuanya harus 'beli tiket dulu naik kereta':

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Pindah halaman dengan Intent</span><span class="dots">···</span>
:::

```
// Cara satu: Intent eksplisit—tentukan halaman tujuan secara jelas
val intent = Intent(this, DetailActivity::class.java)
intent.putExtra("name", "Zhang San")     // Seperti menitipkan "barang bawaan" di kendaraan (data)
startActivity(intent)

// Cara dua: Intent implisit—cukup bilang mau apa, sistem carikan pelakunya
val web = Intent(Intent.ACTION_VIEW, Uri.parse("https://developer.android.com"))
startActivity(web)   // Sistem akan membuka browser/atau meminta Anda memilih
```
:::

Kedua cara masing-masing punya gunanya: eksplisit untuk perpindahan halaman di dalam aplikasi sendiri; implisit untuk memanggil kemampuan sistem atau aplikasi lain (membuka web, menelepon, berbagi). Di proyek Compose, ambil Context dengan LocalContext.current di dalam Composable, lalu bisa startActivity.

#### 4. Multi-Halaman dan Navigasi

Aplikasi nyata pasti punya banyak halaman. Solusi navigasi yang direkomendasikan resmi untuk Compose adalah Navigation Compose (pustaka dependensi androidx.navigation):

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Kerangka Navigation Compose</span><span class="dots">···</span>
:::

```
val navController = rememberNavController()

NavHost(navController, startDestination = "home") {
    composable("home") { HomeScreen(navController) }
    composable("detail/{name}") { entry ->
        val name = entry.arguments?.getString("name")
        DetailScreen(name ?: "Tidak diketahui")
    }
}

// Berpindah halaman di dalam halaman:
navController.navigate("detail/Zhang San")     // dengan parameter
navController.popBackStack()              // kembali ke halaman sebelumnya
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tips: Kalau Halamannya Makin Banyak, Bagaimana?

{class="mt-1"}
Saat proyek membesar, kumpulkan semua rute halaman dalam satu berkas (misalnya AppNavGraph.kt) agar terkelola rapi; jangan biarkan logika 'pergi ke mana' tersebar di tiap halaman. Ini langkah pertama dari 'bisa jalan' menuju 'mudah dirawat'.
:::

#### 5. Sekalian Kenalan: Apa Itu Fragment (dan Kenapa Buku Ini Tidak Mengajarkannya)

Saat membaca tutorial lama kamu pasti bertemu Fragment—'potongan antarmuka yang bisa dipakai ulang' di dalam Activity, pemeran utama mutlak di arsitektur multi-halaman lama. Tetapi di era Compose, halaman cukup memakai fungsi Composable + rute Navigation, dan secara resmi posisi Fragment pun sudah dikurangi. Karena itu buku ini tidak memasukkannya ke jalur utama.

Saran untukmu: pada proyek baru jangan aktif-aktif memakai Fragment; tapi saat membaca kode lama atau ditanya saat wawancara, cukup tahu bahwa ia 'potongan antarmuka yang tertanam di dalam Activity'. Sumber belajar selalu prioritaskan yang terbit 2023 ke atas—'almanak lama' tumpukan teknologi Android ternyata lebih cepat kedaluwarsa dari yang dikira.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Praktik: Memberi 'Ingatan' pada Penghitung

{class="mt-1"}
Ubah penghitung dari Bab 51: ① ganti remember dengan rememberSaveable, putar layar dan pastikan angkanya masih ada; ② tambahkan tombol 'Tentang', pakai Navigation untuk melompat ke halaman kedua yang menampilkan nomor versi; ③ cetak log di onCreate/onPause kedua halaman (Log.d), amati urutan pemanggilan siklus hidup lewat Logcat. Setelah tiga langkah ini, siklus hidup tidak lagi sekadar teori di atas kertas.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan Bab Ini

- Empat komponen utama: Activity (etalase), Service (belakang layar), BroadcastReceiver (pengeras suara), ContentProvider (lemari arsip)
- Enam callback siklus hidup: onCreate → onStart → onResume → onPause → onStop → onDestroy
- Memutar layar menghancurkan lalu membangun ulang Activity: pakai rememberSaveable untuk menyelamatkan state
- Intent adalah 'tiket': eksplisit untuk melompat ke halaman sendiri, implisit untuk memanggil kemampuan sistem
- Multi-halaman pakai Navigation Compose: rute NavHost + composable
:::
