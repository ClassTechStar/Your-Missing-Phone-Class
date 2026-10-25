---
id: di-wu-shi-er-zhang
num: 52
part: an-zhuo-kai-fa-pian
nav: Bab 52: Empat Komponen Utama dan Kitaran Hidup Activity
toc: default
kind: chapter
---

### Bab 52: Empat Komponen dan Kitaran Hayat Activity

{class="chapter-intro mb-4"}
Jika Compose ialah 'wajah' aplikasi, bab ini pula bercakap tentang 'rangka' aplikasi. Sistem Android ada empat komponen asas; semua aplikasi dibina daripadanya; dan yang paling penting, Activity, mempunyai satu 'rajah kitaran hayat' yang wajib terpahat dalam kepala setiap pembangun Android. Selepas bab ini, anda akan memahami teka-teki abadi seperti 'kenapa bila masuk latar belakang dan kembali semula, keadaan aplikasi saya hilang'.

#### 1. Empat Komponen: 'Tiang Seri' Android

Android secara rasmi mentakrifkan empat komponen asas, masing-masing bertanggungjawab atas satu jenis kerja:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Komponen</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Tanggungjawab</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ibaratnya</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Activity</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Satu antara muka yang boleh dilihat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pemuka kedai — boleh dilihat dan boleh berinteraksi oleh pengguna</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Service</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">'Pekerja halimunan' yang bekerja di latar belakang</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pekerja gudang — memainkan muzik, memuat turun fail, tidak perlukan antara muka</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">BroadcastReceiver</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menerima siaran sistem</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Rumah pengawal — 'pembesar suara' yang menyiarkan 'bateri habis', 'rangkaian terputus'</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ContentProvider</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Berkongsi data merentas aplikasi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kabinet fail awam — contohnya berkongsi kenalan dengan aplikasi lain</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Sekilas pandang empat komponen Android

Pada peringkat pemula, 95% masa anda dihabiskan berurusan dengan Activity; Service dan BroadcastReceiver digunakan semasa memainkan muzik atau menghantar pemberitahuan; ContentProvider paling jarang digunakan (sistem sudah membungkus data yang lazim). Juga perhatikan: keempat-empat komponen mesti 'mendaftar' dalam AndroidManifest.xml; tanpa pendaftaran, sistem tidak jumpa mereka.

#### 2. Kitaran Hayat Activity: 'Peta Harta Karun' Pertama Pembangunan Android

Aplikasi pada telefon boleh terganggu bila-bila masa: panggilan telefon masuk, pengguna bertukar ke WeChat untuk membalas mesej, memori sistem tidak cukup lalu mematikan anda… Sepanjang hayat Activity, ia melawati rajah ini secara berulang:

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onCreate (lahir: pemulaan)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onStart (sudah kelihatan)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">onResume (aktif di hadapan)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center">onPause (sebahagian tertutup)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center">onStop (langsung tidak kelihatan)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center">onDestroy (dimusnahkan)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center">🔁 onRestart / onStart / onResume: kembali ke hadapan melalui jalan yang sama</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Rajah 4: Kitaran hayat Activity (arah ke hadapan: baris atas lahir → baris bawah keluar; semasa kembali, berbalik melalui jalan asal)
:::

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Panggil balik</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Bila dicetuskan</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Kegunaan biasa</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onCreate</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Semasa Activity dicipta (sekali)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Memuatkan antara muka, memulakan data</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onStart</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Antara muka menjadi kelihatan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Memulakan beberapa logik ringan</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onResume</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mendapat fokus, boleh berinteraksi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Memulakan animasi, menyambung semula main balik</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onPause</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Dilindungi sebahagian / sejurus bertukar pergi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Jeda animasi, simpan draf</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onStop</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sama sekali tidak kelihatan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Melepaskan sumber berat, menjeda muat turun</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onDestroy</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sebelum dimusnahkan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pembersihan terakhir</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Kegunaan biasa enam panggil balik kitaran hayat

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Amaran Perangkap: Memusingkan Skrin Akan 'Membunuh' Activity

{class="mt-1"}
Adegan terjebak paling klasik pemula: aplikasi dipusingkan sedikit, semua teks dalam kotak input hilang. Punca: memusingkan skrin secara lalai akan memusnahkan dan mencipta semula Activity (melalui sekali onDestroy → onCreate). Penyelesaian: guna rememberSaveable untuk menyimpan keadaan (pengganti remember dalam Compose); ia akan mengembalikan nilai secara automatik semasa dibina semula. Akan digunakan berulang kali dalam Bab 6 dan 7.
:::

#### 3. Intent: 'Tiket Perjalanan' Masuk Keluar Aplikasi

Intent (niat) ialah 'tiket' komunikasi antara komponen. Mahu melompat dari satu halaman ke halaman lain, atau membuka pelayar, atau membangkitkan kamera, semuanya perlu 'beli tiket dan naik':

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Berpindah dengan Intent</span><span class="dots">···</span>
:::

```
// Cara satu: Intent eksplisit—nyatakan halaman destinasi dengan jelas
val intent = Intent(this, DetailActivity::class.java)
intent.putExtra("name", "Zhang San")     // Seperti menitipkan "bagasi" dalam kenderaan (data)
startActivity(intent)

// Cara dua: Intent implisit—cukup sebut mahu buat apa, sistem carikan pelakunya
val web = Intent(Intent.ACTION_VIEW, Uri.parse("https://developer.android.com"))
startActivity(web)   // Sistem akan buka pelayar/atau minta anda pilih
```
:::

Kedua-dua cara ada kegunaan masing-masing: eksplisit untuk lompatan halaman di dalam aplikasi sendiri; implisit untuk memanggil kebolehan sistem atau aplikasi lain (membuka laman web, membuat panggilan, berkongsi). Dalam projek Compose, dalam Composable gunakan LocalContext.current untuk mendapatkan Context maka boleh startActivity.

#### 4. Berbilang Halaman dan Navigasi

Aplikasi sebenar semuanya ada berbilang halaman. Penyelesaian navigasi yang disyorkan secara rasmi untuk Compose ialah Navigation Compose (pustaka kebergantungan androidx.navigation):

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Rangka Navigation Compose</span><span class="dots">···</span>
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

// Berpindah halaman dalam halaman:
navController.navigate("detail/Zhang San")     // dengan parameter
navController.popBackStack()              // kembali ke halaman sebelumnya
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Petua: Kalau Halaman Makin Banyak Macam Mana?

{class="mt-1"}
Apabila projek membesar, kumpulkan semua laluan halaman dalam satu fail (contohnya AppNavGraph.kt) untuk diurus secara pusat; jangan biarkan logik 'pergi ke mana' berselerak merentas halaman. Ini langkah pertama dari 'boleh berjalan' ke 'boleh diselenggara'.
:::

#### 5. Sambil Membiasa Diri: Apa Itu Fragment (dan Kenapa Buku Ini Tidak Mengajarnya)

Semasa merujuk tutorial lama, anda pasti akan bertemu Fragment — ia 'cekak antara muka boleh guna semula' dalam Activity, wira utama dalam seni bina berbilang halaman lama. Tetapi di era Compose, halaman cukup menggunakan fungsi Composable + laluan Navigation, dan pihak rasmi pun sudah melemahkan kedudukan Fragment. Maka buku ini tidak memasukkannya ke dalam laluan utama.

Cadangan untuk anda: projek baharu jangan aktif menggunakan Fragment; tetapi semasa membaca kod lama atau apabila ditanya dalam temu duga, tahu bahawa ia 'cekak antara muka yang disarang dalam Activity' sudah memadai. Sumber pembelajaran sentiasa utamakan yang selepas 2023 — 'kalendar lama' tindanan teknologi Android berubah lebih pantas daripada disangka.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mari cuba: Beri Pengira Itu 'Ingatan'

{class="mt-1"}
Ubah suai pengira Bab 51: ① tukar remember kepada rememberSaveable, pusingkan skrin dan sahkan nombor masih ada; ② tambah butang 'Tentang', guna Navigation untuk pergi ke halaman kedua yang memaparkan nombor versi; ③ cetak log (Log.d) dalam onCreate/onPause kedua-dua halaman, dan perhatikan susunan panggilan kitaran hayat dengan Logcat. Selepas tiga langkah ini, kitaran hayat bukan lagi teori di atas kertas.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan Bab

- Empat komponen: Activity (pemuka), Service (latar belakang), BroadcastReceiver (pembesar suara), ContentProvider (kabinet fail)
- Enam panggil balik kitaran hayat: onCreate → onStart → onResume → onPause → onStop → onDestroy
- Memusingkan skrin memusnahkan dan membina semula Activity: guna rememberSaveable untuk menyelamatkan keadaan
- Intent ialah 'tiket': eksplisit melompat halaman sendiri, implisit memanggil kebolehan sistem
- Berbilang halaman guna Navigation Compose: laluan NavHost + composable
:::
