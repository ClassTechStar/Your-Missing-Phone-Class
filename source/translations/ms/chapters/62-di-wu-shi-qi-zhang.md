---
id: di-wu-shi-qi-zhang
num: 57
part: an-zhuo-kai-fa-pian
nav: Bab 57: Jalan Lanjutan—Kebenaran, Notifikasi dan Seni Bina Moden
toc: default
kind: chapter
---

### Bab 57: Jalan ke hadapan — kebenaran, pemberitahuan dan seni bina moden

{class="chapter-intro mb-4"}
Berjaya membuat aplikasi hanyalah permulaan. Bab ini membincangkan beberapa halangan daripada 'boleh buat' kepada 'buat dengan baik': cara memohon kebenaran dengan anggun, cara menghantar pemberitahuan tanpa menjengkelkan, cara menaikkan seni bina setingkat lagi, dan — pada tahun 2026 — cara bekerjasama dengan AI untuk menulis kod Android. Setiap satu akan anda temui segera dalam projek sebenar.

#### 1. Kebenaran masa jalan: ketuk pintu dahulu, kemudian masuk

Kamera, lokasi, kenalan, pemberitahuan ... 'kawasan sensitif' ini memerlukan aplikasi memohon daripada pengguna semasa berjalan (sejak Android 6). Peraturannya: isytihar dahulu (Manifest), kemudian mohon (dalam kod), dan jika pengguna menolak, nyah taraf dengan anggun. Dalam Compose, paling mudah menggunakan rememberPermissionState daripada pustaka rasmi Accompanist:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Kebenaran runtime (versi Compose)</span><span class="dots">···</span>
:::

```
// Isytiharkan dahulu dalam Manifest:
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
    }) { Text("Rakam gambar") }
}
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Perhatian: bagaimana jika ditolak secara kekal?

{class="mt-1"}
Selepas pengguna menanda "jangan tanya lagi", launchPermissionRequest tidak akan memaparkan dialog lagi. Pada ketika itu, pandu pengguna untuk mengaktifkannya secara manual dalam tetapan sistem (gunakan Intent untuk melompat ke halaman tetapan aplikasi), dan jelaskan dalam antara muka "kebenaran ini untuk apa". Sikap yang lebih mesra akan meningkatkan kesediaan pengguna memberi kebenaran — teks permohonan kebenaran patut ditulis dengan bersungguh-sungguh.
:::

#### 2. Pemberitahuan: katakan perkara berguna pada masa yang tepat

Pemberitahuan ialah saluran aplikasi menjangkau pengguna, dan juga fungsi yang paling mudah "disekat" oleh pengguna. Tiga disiplin menghantar pemberitahuan: hanya hantar yang berguna, benarkan pengguna mematikannya, dan jangan ganggu pada tengah malam. Penggunaan asas:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Hantar pemberitahuan</span><span class="dots">···</span>
:::

```
// Android 13+ wajib minta kebenaran POST_NOTIFICATIONS dahulu (lihat bahagian sebelumnya)

// 1. Cipta saluran pemberitahuan (wajib di Android 8+)
val channel = NotificationChannel(
    "reminder", "Peringatan", NotificationManager.IMPORTANCE_DEFAULT
)
val manager = getSystemService(NotificationManager::class.java)
manager.createNotificationChannel(channel)

// 2. Hantar pemberitahuan
val notification = NotificationCompat.Builder(this, "reminder")
    .setSmallIcon(R.drawable.ic_notification)
    .setContentTitle("Peringatan merekod")
    .setContentText("Hari ini belum merekod lagi")
    .setPriority(NotificationCompat.PRIORITY_DEFAULT)
    .build()
if (ActivityCompat.checkSelfPermission(this,
        Manifest.permission.POST_NOTIFICATIONS) == PackageManager.PERMISSION_GRANTED
) {
    manager.notify(1, notification)
}
```
:::

Untuk tugasan berjadual (contohnya "ingatkan mencatat pada pukul 20:00 setiap hari"), gunakan WorkManager — ia "pengurus penjadualan latar belakang" yang disyorkan secara rasmi, menjamin tugasan dilaksanakan pada masa yang sesuai tanpa anda perlu risau tentang pengoptimuman bateri. Untuk keperluan sejenis penggera, ia memang pilihan tepat.

#### 3. Seni bina lanjutan: suntikan kebergantungan dan modularisasi

Selepas projek membesar, dua "masalah manis" ini akan datang mengetuk:

- Penciptaan objek bercelaru: setiap halaman mencipta pangkalan data dan API sendiri — gunakan Hilt (rangka kerja suntikan kebergantungan) untuk mengurus secara berpusat; "sesiapa yang perlukan apa-apa, cukup minta dan ia disampaikan";
- Kod bertumpuk seperti gunung: projek satu modul makin perlahan untuk diubah — pecahkan kepada berbilang modul (app / core / feature-xxx), setiap fungsi dibangunkan dan diuji secara berasingan.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Petua: jangan reka bentuk berlebihan

{class="mt-1"}
Hilt dan modularisasi adalah alat yang baik, tetapi untuk projek seorang diri jangan tergesa menggunakannya. Buku perakaunan dengan satu modul + penciptaan kebergantungan secara manual sudah cukup. Tunggu sehingga kod melebihi beberapa puluh ribu baris, binaan mula perlahan, atau mula bekerja beramai-ramai, barulah gunakan mengikut keperluan. Alat wujud untuk mencapai matlamat, bukan untuk pamer — ini juga prinsip "kesederhanaan di atas segalanya" dalam buku pengaturcaraan AI kita.
:::

#### 4. Cara baharu pada 2026: pembangunan Android dibantu AI

Pada tahun 2026, AI telah meresap jauh ke dalam aliran kerja pembangunan Android. Jika anda mahu lebih pantas, gabungan ini sudah sangat matang:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Peringkat</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Bagaimana AI membantu</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Tanggungjawab anda</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menulis kod</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pelengkapan dan penjanaan melalui Gemini terbina dalam Android Studio/plugin AI pihak ketiga</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Terangkan keperluan dengan jelas dan semak hasilnya</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mencari rujukan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Berikan dokumentasi rasmi dan mesej ralat kepada AI untuk ditafsir</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sahkan kesimpulan penting semula di dokumentasi rasmi</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menulis ujian</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Minta AI menjana kes ujian mengikut tiga kategori: "normal/sempadan/luar biasa"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pastikan kes ujian sepadan dengan logik sebenar aplikasi</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Membetulkan bug</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tampal stacktrace + kod berkaitan, AI mengenal pasti dan membaiki</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Fahami perubahan dan jalankan ujian untuk mengesahkan</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Empat senario pembangunan Android dibantu AI

Metodologi terperinci — cara memberi arahan kepada AI, cara menerima hasil, cara mengelakkan perangkap — dibincangkan dalam 11 bab lengkap Bahagian 7 buku ini, "Amalan Pengaturcaraan AI" (Bab 37-47). Sangat disyorkan untuk dibaca bersama: serahkan tatabahasa Android kepada bahagian ini, dan seni kerjasama AI kepada Bahagian 7.

#### 5. Pengoptimuman prestasi dan alat debug Compose

Compose menyeronokkan untuk ditulis, tetapi "rekomposisi berlebihan" juga boleh menyebabkan kelambatan. Tiga petua praktikal:

- Stabilkan parameter: tambahkan @Immutable pada data class atau gunakan derivedStateOf untuk mengelakkan perubahan status yang tidak berkaitan mencetuskan rekomposisi meluas;
- Ingat gunakan key: items(list, key = { it.id }) memastikan hanya item yang sepatutnya berubah apabila senarai ditambah atau dibuang — tanpa key, membuang satu item mungkin melukis semula keseluruhan senarai;
- Mod Compose dalam Layout Inspector: lihat secara masa nyata bilangan rekomposisi setiap Composable; yang kerap berekomposisi jelas sekilas pandang — optima mengikut titik panas tersebut.

Selain itu, aktifkan laporan pengkompil Compose (Metrics) untuk menjana laporan "komponen mana yang tidak stabil" — dalam perjalanan lanjutan, data sentiasa lebih dipercayai daripada perasaan.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Praktik: tambahkan "tiga serangkai" pada buku perakaunan

{class="mt-1"}
① Tambahkan "peringatan mencatat pada pukul 20:00 setiap hari" pada buku perakaunan (WorkManager + saluran pemberitahuan + kebenaran pemberitahuan Android 13); ② ubah penciptaan pangkalan data dan API kepada suntikan Hilt; ③ cuba gunakan alat AI untuk mempercepat pelaksanaan fungsi "penapis bulanan", kemudian semak hasilnya dengan kaedah penerimaan tiga lapisan. Selepas tiga serangkai ini siap, projek anda sudah kelihatan seperti keluaran profesional.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan bab ini

- Kebenaran sensitif: isytihar dalam Manifest + mohon semasa jalan + pandu dengan anggun selepas ditolak
- Tiga disiplin pemberitahuan: hanya yang berguna, boleh dimatikan, tidak mengganggu; saluran + kebenaran, kedua-duanya wajib ada
- Gunakan WorkManager untuk tugasan berjadual, jangan cipta roda sendiri
- Hilt mengurus objek, modularisasi mengurus kod — untuk projek kecil seorang diri, jangan tergesa menggunakannya
- Empat senario bantuan AI: menulis kod, mencari rujukan, menulis ujian, membetulkan bug; metodologi dalam Bahagian 7 (Bab 37-47)
:::
