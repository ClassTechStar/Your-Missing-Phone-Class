---
id: di-wu-shi-ba-zhang
num: 58
part: an-zhuo-kai-fa-pian
nav: Bab 58: Manual Rujukan Pantas dan Sumber
toc: default
kind: chapter
---

### Bab 58: Manual rujukan pantas dan sumber

{class="chapter-intro mb-4"}
Bab ini ialah manual rujukan pantas yang boleh digunakan secara berasingan. Apabila anda lupa sesuatu sintaks atau perlu membuat keputusan pantas, terus rujuk sini. Disyorkan untuk menjadikannya "kad saku": rujukan pantas kod biasa, soalan lazim, sumber pembelajaran — tiada halaman tertinggal.

#### 1. Kad rujukan pantas kod biasa

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Apa yang mahu dibuat</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Kod utama</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ingat satu keadaan boleh ubah</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">var x by remember { mutableStateOf(nilaiAwal) }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Keadaan tidak hilang apabila skrin diputar</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">rememberSaveable { mutableStateOf(nilaiAwal) }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Susunan menegak/melintang</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Column { }</code> / <code class="inline">Row { }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Senarai muat lambat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">LazyColumn { items(senarai) { ... } }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Navigasi antara halaman</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">navController.navigate("laluan")</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kerja menunggu dilakukan dalam coroutine</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">viewModelScope.launch { ... }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Memerhatikan aliran data</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">val list by flow.collectAsState()</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Simpan konfigurasi kecil</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">context.dataStore.edit { it[KEY] = nilai }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Simpan data berstruktur</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tiga serangkai Room: @Entity / @Dao / @Database</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ambil data melalui rangkaian</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Antara muka Retrofit + fungsi suspend</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Hantar pemberitahuan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">NotificationChannel + NotificationCompat.Builder</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tulis log</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Log.d("TAG", "message")</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Kad rujukan pantas pembangunan Android (edisi Ogos 2026)

#### 2. Soalan lazim (FAQ)

S1: Saya langsung tiada asas pengaturcaraan, berapa lama untuk belajar pembangunan Android?

Ikuti laluan buku ini: minggu 1-2 pasang persekitaran dan belajar asas Kotlin; minggu 3-4 belajar Compose untuk membina antara muka; minggu 5-6 siapkan projek buku perakaunan; minggu 7-8 habiskan projek cuaca. Dua bulan, daripada sifar kepada mampu membuat aplikasi kecil secara berasingan. Syaratnya: dedikasikan 1-2 jam sehari, dan taip kod dengan tangan, bukan sekadar membaca.

S2: Adakah Java masih perlu dipelajari?

Tidak perlu. Projek baharu, tutorial baharu dan jawatan baharu pada asasnya semuanya menggunakan Kotlin. Anda hanya akan bertemu banyak Java apabila "menyelenggara projek lama berumur sepuluh tahun". Selepas menguasai Kotlin, jika kerja memerlukannya, menambah Java akan cepat — kedua-duanya berkongsi ekosistem mesin maya yang sama.

S3: Emulator atau peranti sebenar?

Emulator memang mudah untuk debug semasa pembangunan (snapshot, pelbagai model), tetapi penerimaan akhir mesti melalui peranti sebenar — sentuhan, prestasi, rangkaian sebenar, penderia, semuanya tidak boleh digantikan oleh emulator. Jika berkemampuan, membeli satu peranti sebenar kelas pertengahan sebagai peranti ujian ialah pelaburan paling berbaloi.

S4: Senangkah mendapat kerja dalam pembangunan Android?

Keadaan pasaran 2026: jawatan peringkat permulaan yang sekadar "boleh tulis antara muka" sangat kompetitif, tetapi pembangun yang "faham Kotlin + mahir seni bina + ada karya yang telah diterbitkan" masih dicari-cari. Untuk anda yang masih belajar, resume terbaik ialah aplikasi buatan sendiri yang ada di kedai.

S5: Apa yang perlu dibuat jika terkandas kerana ralat?

Tiga langkah emas: ① salin baris pertama ralat dan cari seadanya di StackOverflow/mesin carian; ② semak halaman berkaitan dalam dokumentasi rasmi; ③ jika masih gagal, bungkus "tingkah laku diharapkan + gejala sebenar + teks penuh ralat + kod berkaitan" dan hantar kepada AI atau komuniti untuk bertanya. Sebahagian besar masalah selesai pada langkah pertama.

#### 3. Sumber pembelajaran disyorkan

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Jenis</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Sumber</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Sebab disyorkan</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Rasmi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">developer.android.com</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Dokumentasi rasmi Android, semua tutorial Compose/Kotlin ada di dalamnya, rujukan paling sahih</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Rasmi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Laman rasmi Kotlin (kotlinlang.org)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Dokumentasi rasmi bahasa + tapak latihan dalam talian</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Rasmi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Google Codelabs</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kursus latihan langkah demi langkah dengan bimbingan penuh, sangat mesra pemula</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Komuniti</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Stack Overflow (tag android)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Stesen pertama meminta bantuan untuk ralat</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Komuniti</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Juejin / CSDN (zon Android)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Banyak artikel praktikal berbahasa Cina; berhati-hati membezakan yang baharu dan lama (semak tarikh dahulu)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Video</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Saluran rasmi Google Developers</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Penerangan teknologi baharu daripada persidangan pembangun setiap tahun</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Temahan buku</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bahagian 7 "Amalan Pengaturcaraan AI" (Bab 37-47)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Panduan lengkap menggunakan AI untuk pembangunan Android</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Senarai sumber pembelajaran pembangunan Android (Ogos 2026)

#### 4. Rujukan pantas arahan Gradle biasa

Biasanya klik butang sudah cukup, tetapi baris arahan kadangkala lebih cekap (terutamanya apabila digandingkan dengan alat AI atau talian paip CI):

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Arahan</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Fungsi</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">./gradlew assembleDebug</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bina APK versi debug (pada Windows, buang ./)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">./gradlew assembleRelease</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bina versi release (perlu persiapan tandatangan)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">./gradlew test</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Jalankan semua ujian unit</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">./gradlew lint</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Semakan statik: cari bug berpotensi dan gaya kod yang tidak menepati piawaian</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">./gradlew clean</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kosongkan hasil binaan (versi kompilasi daripada "petua mulakan semula")</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">./gradlew :app:dependencies</code></td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lihat pepohon kebergantungan (alat ampuh mengesan konflik versi)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Rujukan pantas arahan Gradle biasa

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Petua: jika binaan bermasalah, jalankan clean dahulu

{class="mt-1"}
Peristiwa misteri "semalam boleh jalan, hari ini tiba-tiba tidak" — enam atau tujuh daripada sepuluh kali disebabkan cache binaan bercelaru. Jalankan ./gradlew clean kemudian bina semula; ini boleh menyembuhkan lebih separuh masalah "misteri". Jika masih tidak boleh, mulakan semula Android Studio — petua ini paling berkesan digandingkan dengan File → Invalidate Caches.
:::

#### 5. Penutup: daripada aplikasi pertama ke aplikasi ke-N

Bila dilihat semula, anda daripada "tidak tahu apa itu Activity" kepada memasang persekitaran, menguasai Kotlin, melukis antara muka dengan Compose, menyambungkan aplikasi kepada pangkalan data dan rangkaian, kemudian menguji, membungkus dan menerbitkan — di laluan ini, anda telah menamatkan bahagian paling sukar daripada perjalanan sifar ke satu.

Dunia teknologi berubah sangat pantas: rangka kerja akan dinaik taraf, alat akan berganti, AI akan mengambil alih lebih banyak kerja "menaip papan kekunci". Tetapi ada satu perkara yang tidak akan lapuk: kebolehan anda menguraikan idea yang kabar kepada langkah-langkah yang jelas, kemudian melaksanakannya langkah demi langkah. Alat ialah pengganda, pemikiran ialah asas. Pengganda boleh diganti, tetapi asas tidak boleh digoyang.

:::inline div .quote-line
Anda bukan lagi sekadar "orang yang mahir guna telefon". Anda boleh mengubah idea dalam kepala menjadi aplikasi yang benar-benar berjalan pada ratusan juta peranti Android. Mulai hari ini, berkarya dengan papan kekunci—itulah romantisme pembangun Android.
:::

#### Rujukan

{class="list-decimal pl-6 mb-3 space-y-1 text-xs text-gray-500"}
1. Android Developers. (2026). Android Developer Guides and Jetpack Compose Documentation. developer.android.com.
2. Kotlin Foundation. (2026). Kotlin Language Documentation. kotlinlang.org.
3. Android Open Source Project. (2026). Android Platform Version History and API Levels.
4. Google Play. (2026). Play Console Help: Publishing and App Signing.
5. AndroidX Release Notes. (2026). Room / DataStore / Navigation / WorkManager releases.
6. Square. (2026). Retrofit Documentation. github.com/square/retrofit.
