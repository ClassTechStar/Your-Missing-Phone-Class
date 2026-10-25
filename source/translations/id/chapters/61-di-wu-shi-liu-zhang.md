---
id: di-wu-shi-liu-zhang
num: 56
part: an-zhuo-kai-fa-pian
nav: Bab 56: Memoles dan Menerbitkan—Masuk ke Google Play
toc: default
kind: chapter
---

### Bab 56: Pemolesan dan Rilis—Menguji, Men-debug, dan Naik ke Google Play

{class="chapter-intro mb-4"}
Aplikasinya sudah jadi, terus? Bab ini menjawab tiga hal untuk berpindah dari 'bisa jalan' ke 'bisa diserahkan': cara men-debug untuk menemukan bug secara efisien, cara menulis pengujian untuk mencegah regresi, dan cara mengirim aplikasi ke Google Play agar diunduh orang seluruh dunia. Naik toko bukan sekadar seremoni—itulah garis batas yang mengubah sebuah karya menjadi produk.

#### 1. Tiga Jurus Debugging: Logcat, Breakpoint, Inspektur UI

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Alat</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Fungsinya Apa</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Cara memakainya</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Logcat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Melihat log sistem / log yang kamu tulis sendiri</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Di kode tulis Log.d("TAG","nilai=$x"), lalu cari TAG di panel untuk memfilter</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Debug dengan breakpoint</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Membuat program berhenti di baris tertentu untuk melihat nilai variabel</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Klik di samping nomor baris hingga muncul titik merah, jalankan dalam mode Debug, lalu eksekusi baris demi baris</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Layout Inspector</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Melihat struktur tampilan yang sedang berjalan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menu Tools → Layout Inspector, melihat pohon komponen secara waktu nyata</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Tiga jurus andalan debugging

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tips: Cara membaca pesan error

{class="mt-1"}
Setelah crash, Logcat akan menampilkan stacktrace merah. Cari dari bawah ke atas baris pertama yang diawali nama paketmu sendiri (misalnya com.example.yourapp) — baris itulah biasanya lokasi kejadian. Periksa dulu "jenis Exception"-nya (null pointer? salah konversi tipe?), lalu lihat "at ... filemu:nomorbaris". Trik ini menyelesaikan 80% crash.
:::

#### 2. Pengujian: Memberi "asuransi" pada kode

Pengujian manual tidak bisa diandalkan — perbaiki satu fitur, fitur lain diam-diam rusak. Test adalah "obat penyesalan" sekaligus "rompi anti peluru". Test Android terbagi tiga lapis; pemula cukup kuasai lapis pertama dulu:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Lapisan</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Menguji apa</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Diletakkan di mana</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Kecepatan</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Unit test</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Logika murni (perhitungan, validasi)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">app/src/test/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Hitungan detik</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Instrumented test</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Perilaku antarmuka di perangkat asli</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">app/src/androidTest/</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Hitungan menit</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pengujian manual</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Rasa dan pengalaman manusia sungguhan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">——</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Selalu diperlukan</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Tiga lapis pengujian

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Contoh unit test</span><span class="dots">···</span>
:::

```
// Pisahkan logika "mengubah teks nominal menjadi angka" menjadi fungsi murni
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

Validasi nominal dan perhitungan statistik di aplikasi catatan keuangan semuanya harus dilindungi unit test. Menjalankan test: klik kanan folder test → Run. Semua hijau berarti lulus, dan kamu bisa mengubah kode dengan tenang.

#### 3. Menandatangani dan mengemas: Memberi "stempel" pada App

Android mewajibkan semua paket instalasi ditandatangani — seperti mencap cap resmi yang membuktikan "paket ini keluaran saya dan tidak diubah orang". Saat debugging, Android Studio otomatis memakai tanda tangan debug; untuk rilis kamu harus memakai tanda tangan release sendiri. Prosesnya:

1. Menu Build → Generate Signed Bundle / APK;
2. Buat file keystore (gudang kunci) — atur kata sandinya dan simpan dengan baik;
3. Pilih format release + AAB, dan build selesai.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Peringatan jebakan: keystore hilang = App hilang

{class="mt-1"}
Setelah tayang, pembaruan App wajib memakai tanda tangan yang sama, jika tidak toko akan menolak pembaruannya. Begitu file keystore dan kata sandinya hilang, kamu hanya bisa membuat aplikasi baru dan mengunggah ulang dari nol — pengguna lama tidak bisa terhubung sama sekali. Pastikan mencadangkan keystore dan kata sandi di tempat yang aman (cloud drive terenkripsi + aplikasi catatan); ini salah satu pelajaran paling mahal bagi pengembang Android.
:::

#### 4. Alur lengkap tayang di Google Play

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> Mendaftar akun developer</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-invoice mr-1"></i> Menyiapkan materi store</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-box mr-1"></i> Unggah AAB</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-clipboard-list mr-1"></i> Isi tabel keamanan data</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> Review (berjam-jam sampai berhari-hari)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-party-horn mr-1"></i> Rilis di store</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Gambar 6: Enam langkah tayang di Google Play
:::

- Pendaftaran: biaya pendaftaran sekali bayar 25 dolar AS, perlu akun Google yang bisa dipakai;
- Aset: ikon aplikasi (512×512), tangkapan layar (minimal 2), deskripsi fitur, tautan kebijakan privasi (wajib bila mengumpulkan data);
- Formulir keamanan data: nyatakan dengan jujur data apa saja yang dikumpulkan — aplikasi catatan keuangan tanpa koneksi internet bisa "nol pengumpulan";
- Peninjauan: unggahan pertama akun baru sering ditinjau manusia, durasinya berkisar beberapa jam hingga beberapa hari; kalau ditolak, perbaiki sesuai masukannya.

Catatan untuk pengguna di Tiongkok: Google Play membutuhkan lingkungan jaringan khusus, dan distribusi di Tiongkok daratan biasanya lewat toko lokal (Huawei, Xiaomi, Yingyongbao, dll.). Proses tayang di toko lokal serupa, tetapi tiap toko punya selera peninjauannya sendiri — satu AAB/APK yang sama bisa didistribusikan ke banyak toko. Untuk latihan, berhasil menuntaskan satu toko saja sudah kemenangan.

#### 5. Menyiapkan aset toko: Kesan pertama adalah jumlah unduhan

Halaman toko adalah etalase yang dilihat pengguna saat "berkeliling di toko". Tiga aset menentukan kesan pertama:

- Ikon: 512×512, jangan asal pakai tangkapan layar. Kalau tidak punya kemampuan desain, pakai alat AI untuk membuat bentuk geometris sederhana; baru memenuhi syarat jika ikon tetap dikenali sekali lihat setelah diperkecil di layar utama ponsel;
- Tangkapan layar: minimal 2, sebaiknya 4-6, menampilkan skenario fitur paling inti; tiap gambar diberi satu kalimat bahasa sehari-hari ("catat satu catatan dalam sekejap" sepuluh kali lebih baik daripada "solusi pencatatan keuangan yang efisien");
- Deskripsi: kalimat pertama harus menjelaskan "ini apa + untuk siapa"; jangan menumpuk kata "paling profesional, paling hebat" — bobot pencarian toko utamanya melihat kata kunci dan konversi unduhan; kejujuran lebih efektif daripada bombastis.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tips: Lihat-lihat sejawat (A/B)

{class="mt-1"}
Sebelum tayang, kelilingi sepuluh besar App sejenis di toko dan bandingkan lewat tangkapan layar: gaya ikon mereka seperti apa? Titik jual apa yang ditonjolkan tangkapan layarnya? Bagaimana judulnya ditulis? Meniru bukan mencontek — pelajari polanya, ganti dengan kontenmu sendiri; ini pelajaran tercepat untuk cold start semua produk.
:::

#### 6. Daftar singkat optimasi performa dan pelaporan crash

Sebelum App tayang, dua hal ini layak masing-masing diberi setengah jam:

##### 1. Empat butir pemeriksaan performa

1. Gunakan LazyColumn untuk daftar: jangan pernah menyusun daftar panjang dengan Column paksa — lazy loading adalah pelajaran pertama performa Android;
2. Jangan memuat gambar asli mentah-mentah: pakai pustaka gambar Coil untuk memperkecil dan menyimpan cache otomatis; satu gambar asli 5MB cukup membuat ponsel kelas bawah tersendat habis;
3. Hindari kerja berat di thread utama: database, jaringan, dan file besar kerjakan di dalam coroutine;
4. Ukur dengan Profiler: profiler bawaan Android Studio bisa memantau memori, CPU, dan konsumsi baterai — ukur dulu, baru optimasi, jangan pakai perasaan.

##### 2. Pelaporan crash

Tidak crash saat kamu menguji bukan berarti tidak crash di ponsel pengguna. Sebelum tayang, integrasikan Firebase Crashlytics (resmi dari Google, gratis): hanya beberapa baris konfigurasi; saat pengguna mengalami crash, stacktrace otomatis terlaporkan, dan di dashboard kamu bisa melihat "model mana, versi berapa, crash di baris mana". Tayang tanpa pemantauan crash sama dengan menyetir dengan mata terpejam.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Praktik: "Serahkan" aplikasi catatan keuanganmu sekali

{class="mt-1"}
① Tambahkan 3 unit test untuk logika seperti parseAmount; ② gunakan Logcat untuk menangkap sendiri satu crash buatanmu lalu perbaiki; ③ hasilkan satu APK bertanda tangan release dan kirim ke teman untuk dipasang (di sinilah "rasa karya" terasa); ④ kalau masih ada tenaga, daftar akun pengembang dan benar-benar ajukan aplikasi catatan keuanganmu untuk tayang. Tiga butir pertama bisa selesai malam ini.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan bab

- Tiga jurus debugging: Logcat melihat log, breakpoint melihat variabel, Layout Inspector melihat tampilan
- Membaca crash: dari stacktrace, cari dari bawah ke atas baris pertama yang memuat nama paketmu sendiri
- Tiga lapis pengujian: unit (hitungan detik, pelajari ini dulu) / instrumented / manual
- Rilis wajib ditandatangani: cadangkan baik-baik keystore dan kata sandi; hilang berarti App "berganti orang"
- Enam langkah tayang: daftar → aset → unggah AAB → formulir keamanan data → peninjauan → tayang
:::
