---
id: di-si-shi-wu-zhang
num: 45
part: ai-biancheng-pian
nav: Bab 45: Jaminan Kualitas—Membuat Kode AI Lebih Andal
toc: default
kind: chapter
---

### Bab 45: Jaminan Kualitas — Membuat Kode Buatan AI Menjadi Andal

{class="chapter-intro mb-4"}
Kode buatan AI punya satu ciri: biasanya "kelihatannya benar"—penamaan variabel rapi, komentar lengkap, logika jernih. Tapi "kelihatannya benar" tidak sama dengan "benar sungguhan". Masalah yang tersembunyi dalam kode AI sering lebih sulit ditemukan daripada dalam kode tulisan tangan, karena kualitas permukaannya terlalu tinggi sehingga mudah membuat orang lengah. Bab ini mengajarkan cara membangun sistem jaminan kualitas yang efektif untuk kode AI—dengan tiga lini pertahanan (pengujian, tinjauan, dan kontrol versi), "kelihatannya benar" diubah menjadi "benar sungguhan".

#### 1. Berbasis pengujian: minta AI menulis pengujian

Pengujian adalah lini pertahanan pertama jaminan kualitas pemrograman AI. Kabar baiknya: meminta AI menulis pengujian lebih mudah dan lebih andal daripada memintanya menulis kode fitur—karena perilaku yang diharapkan dari pengujian sudah jelas, sehingga kode "kelihatannya benar tapi sebenarnya salah" jarang muncul.

Alur pemrograman AI berbasis pengujian: minta AI menulis kode fitur dulu, setelah fungsi dasarnya terverifikasi, langsung minta ia menulis kasus uji. Kasus uji harus mencakup jalur normal, kasus batas, dan kasus pengecualian. Setelah itu minta AI mengoreksi kode fitur berdasarkan umpan balik pengujian. Keunggulan alur ini: begitu pengujian selesai ditulis, ia menjadi alat verifikasi yang terus-menerus—setiap perubahan berikutnya bisa dipastikan tidak menimbulkan regresi cukup dengan menjalankan pengujian.

::: div .code-block
:::inline div .code-head
<span>Instruksi untuk AI: menulis test</span><span class="dots">···</span>
:::

```
Tulis unit test untuk fungsi calculate_discount.
Kasus uji harus mencakup:
1. Jalur normal:
   - barang 100 yuan diskon 20% -> 80
   - barang 200 yuan diskon 50% -> 100
2. Kasus batas:
   - barang 0 yuan diskon 20% -> 0
   - barang 100 yuan tanpa diskon -> 100 (tidak didiskon)
   - barang 100 yuan diskon 0% -> 100 (harga penuh)
3. Kasus abnormal:
   - harga negatif -> harus melempar error
   - rasio diskon > 1 -> harus melempar error
   - input bukan angka -> Harus melempar error
Pakai framework Vitest, berikan file test yang lengkap.
```
:::

Perhatikan ciri instruksi ini: ia secara eksplisit menyebutkan tiga jenis kasus uji (normal, batas, pengecualian), tidak memberi AI ruang untuk "menguji pilih-pilih". AI kadang hanya menulis pengujian jalur normal agar "cepat selesai"; menyebutkan semua kategori secara eksplisit mencegah masalah ini.

#### 2. Teknik tinjauan kode

Meskipun sudah ada cakupan pengujian, kamu tetap perlu meninjau secara manual kode hasil AI. Tinjauan kode bukan membaca baris demi baris—itu terlalu memakan waktu dan terlalu bergantung pada kemampuan pemrogramanmu. Tinjauan kode AI yang efektif sebaiknya fokus pada dimensi-dimensi kunci berikut:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Dimensi tinjauan</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Yang diperhatikan</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Masalah yang sering muncul</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Keamanan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Validasi input, penanganan kunci, perlindungan dari injeksi SQL</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AI sering lupa memvalidasi input, kunci ditulis langsung di dalam kode</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Penanganan error</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apakah pengecualian ditangkap, apakah pesan errornya masuk akal</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AI suka memakai blok catch kosong atau hanya console.log</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kinerja</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Adakah masalah kinerja yang jelas, seperti kueri N+1 atau perulangan tanpa henti</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AI kadang menulis algoritma berkompleksitas O(n²)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kemudahan perawatan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apakah struktur kode jernih, apakah penamaannya bermakna</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AI sesekali menghasilkan kode yang terlalu abstrak</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Manajemen dependensi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apakah dependensi yang diimpor benar-benar diperlukan, apakah versinya jelas</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AI cenderung mengimpor pustaka yang tidak perlu</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Dimensi kunci tinjauan kode AI

Saat meninjau, kamu tidak harus memeriksa semuanya sendiri—minta AI membantu melakukan putaran tinjauan pertama. Instruksinya misalnya: "Tinjau keamanan, penanganan error, dan kinerja kode ini, tunjukkan potensi masalahnya." Kemampuan AI meninjau kodenya sendiri terus meningkat; meskipun belum bisa menggantikan tinjauan manual sepenuhnya, ia dapat menyaring sebagian besar masalah yang mencolok.

#### 3. Kontrol versi: peran Git dalam pemrograman AI

Peran Git dalam pemrograman AI lebih penting daripada dalam pemrograman tradisional. Karena setiap perubahan AI bisa menimbulkan perubahan yang tak terduga, kamu butuh satu "obat penyesalan" yang andal—kontrol versi itulah obat penyesalannya.

Praktik terbaik Git dalam pemrograman AI adalah "commit sering, maju bertahap kecil". Setiap satu titik fitur yang bisa diverifikasi selesai, langsung commit. Dengan begitu, saat salah satu perubahan AI bermasalah, kamu bisa mundur tepat ke keadaan terakhir yang masih berfungsi, tanpa harus membuang seluruh pekerjaan.

Trik praktis lainnya adalah "isolasi cabang". Untuk perubahan AI yang hasilnya belum pasti (misalnya restrukturisasi besar), buat dulu cabang baru untuk mengerjakannya. Jika hasilnya memuaskan, gabungkan kembali ke cabang utama; jika tidak, langsung hapus cabangnya tanpa mengganggu cabang utama. Ini jauh lebih aman daripada memodifikasi berulang-ulang di cabang utama.

1. Sebelum setiap perubahan AI, pastikan area kerja bersih (tidak ada perubahan yang belum di-commit). Dengan begitu, jika hasil perubahan AI tidak memuaskan, kamu bisa cepat mengembalikannya dengan git checkout .
2. Setelah setiap perubahan AI terverifikasi lolos, langsung commit. Pesan commit menjelaskan apa yang diubah kali ini, misalnya "feat: menambahkan fitur registrasi pengguna".
3. Untuk restrukturisasi besar, buat cabang dulu: git checkout -b refactor/auth-system. Selesaikan perubahan di cabang itu, dan gabungkan setelah pengujian lolos.
4. Biasakan melihat diff. Setelah setiap perubahan AI, gunakan git diff untuk melihat persis apa yang berubah. Ini tidak hanya membantumu menemukan masalah, tetapi juga membantumu belajar dari kodenya.

#### 4. Jebakan umum dan panduan menghindarinya

Ada beberapa jebakan yang muncul berulang kali dalam pemrograman AI dan hampir semua pemula pernah menginjaknya. Mengetahuinya sejak awal akan menghemat banyak putaran salah jalanmu.

##### 1. Jebakan pertama: jebakan kepercayaan

"Kode buatan AI kelihatan sangat profesional, pasti tidak ada masalah, kan?"—inilah jebakan paling berbahaya. Kode yang dihasilkan AI sangat rapi di permukaan—penamaannya baku, komentarnya lengkap, strukturnya jernih—"kesan profesional di permukaan" semacam ini membuat orang lengah. Tapi kerapian permukaan tidak berarti logikanya benar. Penawarnya: selalu verifikasi lewat pengujian, jangan menilai dari "kelihatannya benar atau tidak".

##### 2. Jebakan kedua: jebakan pembengkakan

"Kalau AI bisa membantu menulis kode, kenapa tidak sekaligus membuat fiturnya lengkap?"—ini akan memunculkan pembengkakan kode. AI sangat pandai "memberi lebih": kamu minta satu halaman login, ia menyerahkan satu sistem manajemen pengguna yang lengkap. Fitur-fitur berlebih tidak hanya menambah kompleksitas, tetapi juga menambah peluang munculnya bug. Penawarnya: patuhi prinsip Simplicity First secara ketat, dan tegaskan kepada AI "cukup fitur ini saja, jangan tambahkan apa pun".

##### 3. Jebakan ketiga: jebakan pemahaman

"AI pasti paham maksud saya, kan?"—belum tentu. Kemampuan pemahaman AI memang kuat, tetapi terhadap kebutuhan yang samar ia tetap akan "menebak". Ketika tebakannya meleset, kode yang dihasilkan pun salah. Yang lebih merepotkan, kode yang salah tebak itu biasanya "kelihatan sangat masuk akal", membuatmu mengira ia paham. Penawarnya: berikan detail spesifik yang cukup dalam instruksimu, kurangi ruang bagi AI untuk "menebak".

##### 4. Jebakan keempat: jebakan konteks

"Saya sudah bilang di percakapan sebelumnya, AI pasti masih ingat, kan?"—kemungkinan besar tidak ingat. Seiring percakapan memanjang atau sesi baru dibuka, AI akan kehilangan konteks awal. Kalau satu batasan penting tidak dituliskan ke berkas memori proyek, kemungkinan besar ia terabaikan pada perubahan-perubahan berikutnya. Penawarnya: tuliskan batasan kunci ke berkas memori proyek, jangan mengandalkan ingatan percakapan.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Ringkasan empat jebakan utama

{class="mt-1"}
Jebakan kepercayaan—jangan percaya yang "kelihatannya benar"; jebakan pembengkakan—AI suka "memberi lebih"; jebakan pemahaman—kebutuhan yang samar akan ia "tebak"; jebakan konteks—ingatan percakapan pasti "lupa". Penawarnya masing-masing: verifikasi lewat pengujian, buang yang berlebihan, beri detail secukupnya, tulis ke berkas memori.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mari praktik: bangun tiga lini pertahanan untuk proyekmu

{class="mt-1"}
Jika kamu sudah mulai mengerjakan Proyek Satu (situs alat): ① minta AI menulis tiga jenis kasus uji untuk fungsi inti; ② tinjau kodenya menurut lima dimensi (keamanan/penanganan error/kinerja/kemudahan perawatan/dependensi); ③ inisialisasi proyek dengan git dan lakukan commit pertama. Begitu tiga lini pertahanannya lengkap, proyekmu barulah benar-benar menjadi milikmu.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan bab ini

- Kode AI "kelihatannya benar" ≠ "benar sungguhan"—kualitas permukaan yang terlalu tinggi justru membuat orang lengah
- Minta AI menulis pengujian: sebutkan eksplisit tiga kategori kasus (normal/batas/pengecualian) agar tidak terjadi "pengujian pilih-pilih"
- Lima dimensi tinjauan: keamanan, penanganan error, kinerja, kemudahan perawatan, manajemen dependensi
- Git adalah "obat penyesalan": commit sering, maju bertahap kecil, isolasi cabang, sering lihat diff
- Empat jebakan utama: kepercayaan (verifikasi lewat pengujian), pembengkakan (buang yang berlebihan), pemahaman (beri detail secukupnya), konteks (tulis ke berkas memori)
:::
