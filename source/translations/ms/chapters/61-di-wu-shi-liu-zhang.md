---
id: di-wu-shi-liu-zhang
num: 56
part: an-zhuo-kai-fa-pian
nav: Bab 56: Penghalusan dan Penerbitan—Menerbitkan di Google Play
toc: default
kind: chapter
---

### Bab 56: Pengilatan dan Penerbitan — Ujian, Penyahpepijatan dan Penerbitan di Google Play

{class="chapter-intro mb-4"}
Aplikasi sudah siap dibuat, kemudian? Bab ini menjawab tiga perkara 'dari boleh berjalan' ke 'boleh dihantar': bagaimana menyahpepijat dengan cekap untuk mencari bug, bagaimana menulis ujian untuk mengelakkan regresi, dan bagaimana menghantar aplikasi ke Google Play untuk dimuat turun oleh seluruh dunia. Menerbitkan bukan sekadar upacara formal — ia titik peralihan yang menukarkan sebuah karya menjadi produk.

#### 1. Tiga Senjata Penyahpepijatan: Logcat, Breakpoint, Pemeriksa UI

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Alat</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Untuk apa</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Cara guna</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Logcat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lihat log sistem atau log yang anda tulis sendiri</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Dalam kod tulis Log.d("TAG","nilai=$x"), kemudian tapis panel dengan mencari TAG</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Debug dengan breakpoint</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Buat program berhenti pada baris tertentu untuk melihat nilai pemboleh ubah</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Klik di sebelah nombor baris untuk munculkan titik merah, jalankan dalam mod Debug, dan menelusuri langkah demi langkah</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Layout Inspector</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lihat struktur antara muka semasa aplikasi berjalan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menu Tools → Layout Inspector, lihat pepohon komponen secara masa nyata</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Tiga senjata utama debugging

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Petua: cara membaca mesej ralat?

{class="mt-1"}
Selepas aplikasi ranap, Logcat akan memaparkan stacktrace berwarna merah. Cari dari bawah ke atas baris pertama yang bermula dengan nama pakej anda sendiri (contohnya com.example.yourapp) — baris itu biasanya lokasi 'kejadian'. Lihat dahulu "jenis Exception" (penunjuk kosong? ralat penukaran jenis?), kemudian lihat "at ... fail anda:nombor baris". Cara ini boleh menyelesaikan 80% daripada ranapan.
:::

#### 2. Ujian: beri 'insurans' kepada kod anda

Ujian manual tidak boleh diharap — anda membaiki satu fungsi, fungsi lain rosak secara senyap. Ujian ialah 'ubat penyesalan' dan sekali gus 'baju kebal'. Ujian Android terbahagi kepada tiga lapisan; sebagai pemula, kuasai dahulu lapisan pertama:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Lapisan</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Apa yang diuji</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Diletakkan di mana</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Kelajuan</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ujian unit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Logik tulen (pengiraan, pengesahan)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">app/src/test/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Beberapa saat</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ujian instrumentasi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tingkah laku antara muka pada peranti sebenar</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">app/src/androidTest/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Beberapa minit</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ujian manual</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pengalaman dan rasa sebenar manusia</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">——</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sentiasa diperlukan</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Tiga lapisan ujian

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Contoh ujian unit</span><span class="dots">···</span>
:::

```
// Pisahkan logik "tukar rentetan jumlah kepada nombor" menjadi fungsi tulen
fun parseAmount(input: String): Double? {
    val v = input.trim().toDoubleOrNull()
    return if (v != null && v > 0) v else null
}

// Uji dia (JUnit4)
@Test
fun emptyInputReturnsNull() {
    assertEquals(null, parseAmount(""))
}
@Test
fun negativeReturnsNull() {
    assertEquals(null, parseAmount("-5"))
}
@Test
fun normalValueParses() {
    assertEquals(12.5, parseAmount("12.5"))
}
```
:::

Pengesahan jumlah wang dan pengiraan statistik dalam buku perakaunan patut dilindungi oleh ujian unit. Jalankan ujian: klik kanan folder test → Run. Jika semuanya hijau, anda boleh mengubah kod dengan tenang.

#### 3. Tandatangan dan bungkusan: 'cop rasmi' untuk aplikasi anda

Android mewajibkan semua pakej pemasangan ditandatangani — seperti cop rasmi yang membuktikan "pakej ini datang daripada saya dan tidak diubah suai". Semasa debug, Android Studio secara automatik menggunakan tandatangan debug; untuk penerbitan, anda perlu tandatangan release sendiri. Prosedurnya:

1. Menu Build → Generate Signed Bundle / APK;
2. Cipta fail keystore (stor kunci) — tetapkan kata laluan dan simpan dengan selamat;
3. Pilih format release + AAB, dan binaan siap.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Amaran penting: keystore hilang = aplikasi hilang

{class="mt-1"}
Selepas aplikasi diterbitkan, setiap kemas kini mesti menggunakan tandatangan yang sama, jika tidak kedai akan menolak kemas kini tersebut. Sekali fail keystore dan kata laluannya hilang, anda hanya boleh mencipta aplikasi baharu dan menerbitkannya semula — pengguna lama semuanya terputus sambungan. Pastikan anda membuat sandaran keystore dan kata laluannya di tempat yang selamat (storan awan disulitkan + buku nota). Ini antara pengajaran paling mahal bagi pembangun Android.
:::

#### 4. Proses penuh menerbitkan di Google Play

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> Daftar akaun pembangun</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-invoice mr-1"></i> Menyiapkan bahan kedai</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-box mr-1"></i> Muat naik AAB</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-clipboard-list mr-1"></i> Isi jadual keselamatan data</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> Semakan (beberapa jam~beberapa hari)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-party-horn mr-1"></i> Naik ke kedai</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Rajah 6: Enam langkah menerbitkan di Google Play
:::

- Pendaftaran: yuran pendaftaran sekali bayar 25 dolar AS, memerlukan akaun Google yang boleh digunakan;
- Bahan: ikon aplikasi (512×512), tangkapan skrin (sekurang-kurangnya 2 keping), penerangan fungsi, pautan dasar privasi (wajib jika ada data dikumpul);
- Borang keselamatan data: isytiharkan dengan jujur data apa yang dikumpul — buku perakaunan yang tidak bersambung ke internet boleh menanda "sifar pengumpulan";
- Semakan: akaun baharu yang menerbitkan buat kali pertama kerap melalui semakan manusia, dari beberapa jam hingga beberapa hari; jika ditolak, baiki mengikut ulasan yang diberikan.

Perhatian bagi pengguna di China: Google Play memerlukan persekitaran rangkaian khas, dan pengedaran di tanah besar China biasanya melalui kedai tempatan (Huawei, Xiaomi, Yingyongbao dan sebagainya). Prosedur menerbitkan di kedai tempatan serupa, tetapi setiap kedai mempunyai citarasa semakan sendiri — AAB/APK yang sama boleh diedarkan ke banyak kedai. Untuk permulaan, berjaya melalui satu kedai sahaja sudah kemenangan.

#### 5. Cara menyediakan bahan kedai: tanggapan pertama menentukan muat turun

Halaman kedai ialah etalase yang dilihat pengguna ketika "melayari kedai". Tiga bahan menentukan tanggapan pertama:

- Ikon: 512×512, jangan guna tangkapan skrin sekadar lepas. Jika tiada kemahiran reka bentuk, gunakan alat AI untuk menjana bentuk geometri ringkas; ia hanya layak jika masih dikenali sekilas pandang walaupun diperkecil pada skrin utama telefon;
- Tangkapan skrin: sekurang-kurangnya 2 keping, lebih baik 4-6 keping, memaparkan senario fungsi paling teras; setiap satu disertakan satu ayat mudah difahami ("Catat satu entri dalam se saat" sepuluh kali lebih baik daripada "Penyelesaian perakaunan yang cekap");
- Penerangan: ayat pertama mesti menjelaskan "apa ini + untuk siapa"; jangan menimbun "paling profesional, paling hebat" — keutamaan carian kedai terutamanya bergantung pada kata kunci dan penukaran muat turun; kejujuran lebih berkesan daripada pembesaran berlebihan.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Petua: buat perbandingan A/B dengan aplikasi sejenis

{class="mt-1"}
Sebelum menerbitkan, layari sepuluh teratas aplikasi sejenis di kedai dan bandingkan tangkapan skrin: apakah gaya ikon mereka? Apakah jualan unik dalam tangkapan skrin? Bagaimana tajuk ditulis? Meniru bukan menjiplak — pelajari coraknya, gantikan dengan kandungan anda sendiri. Ini pelajaran terpantas untuk memulakan semua produk.
:::

#### 6. Senarai semak pengoptimuman prestasi dan laporan ranapan

Sebelum aplikasi diterbitkan, dua perkara ini berbaloi diberikan masing-masing separuh jam:

##### 1. Empat semakan prestasi

1. Gunakan LazyColumn untuk senarai: jangan sesekali menyusun senarai panjang dengan Column — lazy loading ialah pelajaran pertama prestasi Android;
2. Jangan terus gunakan imej asal: gunakan pustaka imej Coil untuk menskala dan menge-cache secara automatik; satu imej asal 5MB sudah cukup untuk menyekat telefon kelas bawah;
3. Elakkan kerja berat pada benang utama: pangkalan data, rangkaian dan fail besar dilakukan dalam coroutine;
4. Ukur dengan Profiler: penganalisis prestasi terbina dalam Android Studio boleh melihat memori, CPU dan penggunaan bateri — ukur dahulu, kemudian optima; jangan bergantung pada perasaan.

##### 2. Laporan ranapan

Aplikasi tidak ranap semasa anda menguji tidak bermakna ia tidak akan ranap pada telefon pengguna. Sebelum menerbitkan, integrasikan Firebase Crashlytics (rasmi Google, percuma): dengan beberapa baris konfigurasi, apabila pengguna mengalami ranapan, stacktrace dihantar secara automatik, dan anda boleh melihat dalam papan pemuka "model peranti mana, versi mana, ranap di baris mana". Menerbitkan tanpa pemantauan ranapan bagaikan memandu sambil memejamkan mata.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Praktik: "serahkan" buku perakaunan anda sekali

{class="mt-1"}
① Tambahkan 3 ujian unit untuk logik seperti parseAmount; ② gunakan Logcat untuk menangkap sendiri satu ranapan yang anda cipta dan membaikinya; ③ jana APK bertanda tangan release dan hantar kepada rakan untuk dipasang (barulah ada rasa "karya siap"); ④ jika ada kelapangan, daftar akaun pembangun dan benar-benar hantar buku perakaunan untuk diterbitkan. Tiga yang pertama boleh siap malam ini juga.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan bab ini

- Tiga senjata debugging: Logcat untuk log, breakpoint untuk pemboleh ubah, Layout Inspector untuk antara muka
- Membaca ranapan: cari dari bawah ke atas baris pertama yang mengandungi nama pakej anda
- Tiga lapisan ujian: unit (saat, pelajari ini dahulu)/instrumentasi/manual
- Penerbitan wajib bertanda tangan: sandarkan keystore dan kata laluan; jika hilang, aplikasi "bertukar tuan"
- Enam langkah menerbitkan: pendaftaran → bahan → muat naik AAB → borang keselamatan data → semakan → diterbitkan
:::
