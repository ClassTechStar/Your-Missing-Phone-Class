---
id: di-wu-shi-qi-zhang
num: 57
part: an-zhuo-kai-fa-pian
nav: Bab 57: Jalan Menuju Tingkat Lanjut—Izin, Notifikasi, dan Arsitektur Modern
toc: default
kind: chapter
---

### Bab 57: Jalan Menuju Tingkat Lanjut — Izin, Notifikasi, dan Arsitektur Modern

{class="chapter-intro mb-4"}
Bisa membuat App hanyalah awal. Bab ini membahas beberapa rintangan dari "bisa membuat" menuju "membuat dengan baik": cara meminta izin dengan elegan, cara mengirim notifikasi yang tidak menyebalkan, cara menaikkan arsitektur satu tingkat, dan — di tahun 2026 — cara menulis kode Android berpasangan dengan AI. Semuanya akan segera kamu jumpai di proyek nyata.

#### 1. Izin saat runtime: Ketuk pintu dulu, baru masuk

Kamera, lokasi, kontak, notifikasi... "zona sensitif" ini wajib diminta App kepada pengguna saat berjalan (sejak Android 6). Aturannya: deklarasikan dulu (Manifest), lalu minta (di kode), dan bila pengguna menolak, turunkan fitur dengan elegan. Di Compose, yang paling praktis memakai rememberPermissionState dari pustaka resmi Accompanist:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Izin runtime (versi Compose)</span><span class="dots">···</span>
:::

```
// Deklarasikan dulu di Manifest:
// &lt;uses-permission android:name="android.permission.CAMERA" /&gt;

@Composable
fun CameraButton() {
    val permission = rememberPermissionState(
        permission = android.Manifest.permission.CAMERA
    )
    Button(onClick = {
        when {
            permission.status.isGranted -&gt; openCamera()
            permission.status.shouldShowRationale -&gt; showExplainDialog()
            else -&gt; permission.launchPermissionRequest()
        }
    }) { Text("Jepret") }
}
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Perhatian: Bagaimana kalau ditolak permanen?

{class="mt-1"}
Setelah pengguna mencentang "jangan tanya lagi", launchPermissionRequest tidak akan memunculkan dialog lagi. Saat itu, arahkan pengguna menyalakannya manual di Pengaturan sistem (lompat ke halaman pengaturan aplikasi dengan Intent) dan jelaskan di antarmuka "izin ini dipakai untuk apa". Sikap yang ramah membuat pengguna jauh lebih bersedia memberi izin — teks permintaan izin layak ditulis dengan serius.
:::

#### 2. Notifikasi: Mengucapkan hal berguna di waktu yang tepat

Notifikasi adalah saluran App menjangkau pengguna, sekaligus fitur yang paling gampang "diblokir" pengguna. Tiga aturan mengirim notifikasi: hanya kirim yang berguna, biarkan pengguna bisa mematikan, jangan ganggu tengah malam. Pemakaian dasarnya:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Mengirim notifikasi</span><span class="dots">···</span>
:::

```
// Android 13+ wajib minta izin POST_NOTIFICATIONS dulu (lihat bagian sebelumnya)

// 1. Buat channel notifikasi (wajib di Android 8+)
val channel = NotificationChannel(
    "reminder", "Pengingat", NotificationManager.IMPORTANCE_DEFAULT
)
val manager = getSystemService(NotificationManager::class.java)
manager.createNotificationChannel(channel)

// 2. Kirim notifikasi
val notification = NotificationCompat.Builder(this, "reminder")
    .setSmallIcon(R.drawable.ic_notification)
    .setContentTitle("Pengingat mencatat")
    .setContentText("Hari ini belum mencatat, lho")
    .setPriority(NotificationCompat.PRIORITY_DEFAULT)
    .build()
if (ActivityCompat.checkSelfPermission(this,
        Manifest.permission.POST_NOTIFICATIONS) == PackageManager.PERMISSION_GRANTED
) {
    manager.notify(1, notification)
}
```
:::

Tugas terjadwal (misalnya "pengingat mencatat pukul 20.00 tiap hari") gunakan WorkManager — ia "asisten penjadwal latar belakang" yang direkomendasikan resmi, menjamin tugas dieksekusi di waktu yang tepat tanpa kamu repot mengurus optimasi baterai. Untuk kebutuhan sekelas alarm, memakai ini pasti tepat.

#### 3. Arsitektur lanjutan: Dependency injection dan modularisasi

Begitu proyek membesar, dua "masalah manis" akan mendatangi kamu:

- Pembuatan objek kacau: tiap halaman membuat database dan API sendiri-sendiri — kelola semuanya dengan Hilt (framework dependency injection); "siapa butuh apa, tinggal minta, langsung disodorkan";
- Kode menumpuk jadi gunung: proyek satu modul makin lambat tiap kali diubah — pecah menjadi multi-modul (app / core / feature-xxx), tiap fitur dikembangkan dan diuji secara mandiri.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tips: Jangan over-engineering

{class="mt-1"}
Hilt dan modularisasi memang alat yang bagus, tetapi untuk proyek satu orang jangan buru-buru memakainya. Aplikasi catatan keuangan dengan satu modul + pembuatan dependensi manual sudah sangat cukup. Tunggu sampai kode melewati puluhan ribu baris, kompilasi mulai melambat, atau mulai kerja sama beberapa orang, baru masukkan sesuai kebutuhan. Alat melayani tujuan, bukan untuk dipamerkan — ini juga prinsip "kesederhanaan di atas segalanya" di buku pemrograman AI kita.
:::

#### 4. Cara bermain baru 2026: Pengembangan Android berbantuan AI

Di tahun 2026, AI sudah menyatu dalam alur pengembangan Android. Kalau ingin mempercepat, rangkaian kombinasi ini sudah sangat matang:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Tahap</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Cara AI membantu</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Tugasmu</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menulis kode</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gemini bawaan Android Studio / plugin AI pihak ketiga untuk pelengkapan dan pembuatan kode</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menjelaskan kebutuhan dengan jelas, meninjau hasilnya</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mencari referensi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Melemparkan dokumentasi resmi dan pesan error kepada AI untuk dijelaskan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Memverifikasi kesimpulan penting kembali ke dokumentasi resmi</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menulis test</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Meminta AI membuat test case menurut tiga kategori "normal / batas / tak terduga"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Memastikan test case sesuai makna bisnisnya</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Memperbaiki bug</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menempelkan stacktrace + kode terkait, AI menemukan lokasi dan memperbaiki</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Memahami perubahan, menjalankan test untuk verifikasi</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Empat skenario pengembangan Android berbantuan AI

Metodologi konkretnya — cara memberi instruksi ke AI, cara menilai hasil, cara menghindari jebakan — dibahas lengkap dalam 11 bab di Bagian 7 buku ini, "Praktik Pemrograman AI" (Bab 37-47). Sangat disarankan dibaca beriringan: sintaks Android diserahkan ke bagian ini, kiat kolaborasi dengan AI diserahkan ke Bagian 7.

#### 5. Optimasi performa dan alat debugging Compose

Menulis dengan Compose memang asyik, tetapi "rekomposisi berlebihan" juga bisa membuat tersendat. Tiga trik praktis:

- Stabilkan parameter: tambahkan @Immutable pada data class atau gunakan derivedStateOf agar perubahan state yang tak berhubungan tidak memicu rekomposisi luas;
- Ingat pakai key: items(list, key = { it.id }) membuat daftar hanya memperbarui item yang memang harus berubah saat ada penambahan/penghapusan — tanpa key, menghapus satu item bisa menggambar ulang seluruh daftar;
- Mode Compose di Layout Inspector: melihat jumlah rekomposisi tiap Composable secara waktu nyata; siapa yang sering rekomposisi terlihat jelas, dan optimasi tinggal mengikuti titik panasnya.

Selain itu, aktifkan laporan compiler Compose (Metrics) untuk menghasilkan laporan "komponen mana yang tidak stabil" — di jalan menuju tingkat lanjut, data selalu lebih andal daripada perasaan.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Praktik: Tambahkan "paket tiga serangkai" ke aplikasi catatan keuangan

{class="mt-1"}
① Tambahkan "pengingat mencatat pukul 20.00 tiap hari" ke aplikasi catatan keuangan (WorkManager + saluran notifikasi + izin notifikasi Android 13); ② ubah pembuatan database dan API menjadi injeksi Hilt; ③ coba percepat implementasi fitur "filter bulanan" dengan alat AI, lalu periksa hasilnya dengan metode penilaian tiga lapis. Setelah tiga serangkai ini selesai, proyekmu sudah tampak seperti "pasukan reguler".
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan bab

- Izin sensitif: deklarasi di Manifest + permintaan saat runtime + arahan elegan setelah ditolak
- Tiga aturan notifikasi: hanya yang berguna, bisa dimatikan, tidak mengganggu; saluran + izin dua-duanya wajib ada
- Tugas terjadwal pakai WorkManager, jangan bikin roda sendiri
- Hilt mengurus objek, modularisasi mengurus kode — proyek kecil satu orang jangan buru-buru
- Empat skenario bantuan AI: menulis kode, mencari referensi, menulis test, memperbaiki bug; metodologinya di Bagian 7 (Bab 37-47)
:::
