---
id: di-si-shi-si-zhang
num: 44
part: ai-biancheng-pian
nav: Bab 44: Praktik dari 0 ke 1—Alur Lengkap Proyek Utuh
toc: default
kind: chapter
---

### Bab 44: Praktik dari 0 ke 1 — Alur Lengkap Proyek Utuh

{class="chapter-intro mb-4"}
Teorinya sudah selesai; sekarang waktunya praktik. Bab ini bukan sekadar tutorial "tiru sambil ketik", melainkan metodologi praktik tentang "cara berpikir, cara bertanya, cara memverifikasi". Kita akan memakai tiga proyek dengan tingkat kesulitan berbeda untuk memperlihatkan proses berpikir lengkap dari kebutuhan sampai produk jadi. Apa pun alat yang kamu pakai, alur ini berlaku.

#### 1. Proyek satu: situs alat pribadi minimalis (tingkat pemula)

##### 1. Merenungkan kebutuhan

Tujuan: membuat satu halaman web situs alat pribadi yang menampilkan pintasan ke 3-4 alat kecil yang berguna. Ini proyek frontend murni, tanpa backend dan database. Yang penting bukan betapa rumitnya alatnya, melainkan merasakan alur lengkap "dari kebutuhan ke produk jadi".

Ikuti lima unsur kebutuhan: Who—dipakai untuk keperluan pribadi. What—satu halaman web yang menampilkan pintasan alat. Why—mengumpulkan alat yang sering dipakai dalam satu halaman agar mudah diakses. How—satu berkas HTML+CSS+JS, tanpa framework. Constraint—selesai dalam 30 menit, tanpa perlu deployment.

##### 2. Memberikan instruksi

Berdasarkan prinsip Think Before Coding, instruksimu harus memuat informasi yang cukup agar AI memahami tujuannya, tetapi tidak perlu menentukan setiap detail implementasi:

::: div .code-block
:::inline div .code-head
<span>Instruksi untuk AI</span><span class="dots">···</span>
:::

```
Buatkan satu halaman web situs alat pribadi dengan ketentuan:
1. HTML satu file (CSS dan JS inline), tanpa framework
2. Tema gelap, gaya minimalis modern
3. Tampilkan 4 kartu pintu masuk alat:
   - alat peringkas teks
   - alat penghitung kata
   - alat pemilih warna
   - generator kode QR
4. Tiap kartu punya ikon, judul, dan deskripsi singkat
5. Kartu punya animasi saat di-hover
6. Responsif, bisa dipakai di ponsel
7. Ada bilah judul di atas
Langsung berikan file HTML lengkap.
```
:::

##### 3. Penerimaan dan iterasi

Setelah AI memberikan kodenya, lakukan penerimaan mengikuti pemeriksaan tiga lapis dalam verifikasi iteratif. Lapis pertama, verifikasi fungsi: apakah berkasnya bisa dibuka di browser? Apakah keempat kartu tampil semua? Apakah animasi hover berjalan normal? Lapis kedua, verifikasi batas: apakah tata letak tetap benar pada ukuran layar ponsel? Apakah kartu-kartu turun baris saat jendela sangat sempit? Lapis ketiga, verifikasi arsitektur: apakah kodenya mudah dibaca? Apakah CSS sudah inline dalam satu tag style? Adakah bagian yang jelas-jelas berlebihan?

Jika kamu juga ingin mewujudkan fungsi salah satu kartu alat (bukan sekadar pintasannya), tambahkan secara bertahap—tambahkan fungsi satu alat, verifikasi, baru tambahkan yang berikutnya. Inilah penerapan nyata strategi "langkah kecil cepat".

#### 2. Proyek dua: sistem pencatatan keuangan full-stack (tingkat menengah)

##### 1. Merenungkan kebutuhan dan PRD

Tujuan: satu aplikasi pencatatan keuangan full-stack dengan frontend, backend, dan database. Proyek ini jauh lebih rumit dari yang pertama dan memerlukan metode rekayasa kebutuhan dari Bab 40.

Tulis PRD dulu. Mengikuti templat di Bagian 3 Bab 40, susun gambaran umum proyek, daftar fitur, solusi teknis, model data, dan rencana pengembangan. Pemilihan solusi teknis harus mengikuti prinsip Simplicity First—frontend memakai React tetapi tanpa state management rumit seperti Redux, backend memakai Node.js tetapi tanpa microservices, database memakai SQLite alih-alih PostgreSQL (untuk tahap pengembangan).

Rencana pengembangan dipecah menjadi 5 langkah: Langkah 1 kerangka API backend (server Express + SQLite + antarmuka CRUD); Langkah 2 halaman dasar frontend (daftar catatan + form tambah); Langkah 3 integrasi frontend-backend (panggilan API + tampilan data); Langkah 4 fitur kategori dan filter; Langkah 5 rekap bulanan dan grafik sederhana. Setiap langkah yang selesai selalu berupa "sesuatu yang bisa dipakai".

##### 2. Menyiapkan berkas memori proyek

Sebelum mulai menulis kode, buat dulu berkas memori proyek. Ini praktik inti dari rekayasa konteks—memastikan AI mengenal latar belakang proyek di awal setiap percakapan.

::: div .code-block
:::inline div .code-head
<span>CLAUDE.md</span><span class="dots">···</span>
:::

```
# Proyek: aplikasi pencatat keuangan full-stack
## Gambaran
Aplikasi pencatat keuangan pribadi, mendukung pencatatan, kategori, dan rekap bulanan.
## Teknologi
- Frontend: React + TypeScript + Vite
- Backend: Node.js + Express + TypeScript
- Database: SQLite (via better-sqlite3)
- Definisi tipe dipakai bersama frontend-backend
## Kesepakatan API
- Path dasar: /api
- Format respons: { success: boolean, data: any, error: string }
- Gaya RESTful
## Model data
Record { id, amount, type, category, note, date }
## Aturan penulisan kode
- TypeScript mode strict
- Indentasi 2 spasi
- Fungsi ada komentar JSDoc
- Komentar dan pesan commit dalam bahasa Mandarin
```
:::

##### 3. Implementasi bertahap

Ikuti rencana pengembangan; selesaikan setiap langkah dalam satu percakapan tersendiri. Berikut contoh instruksi untuk langkah pertama:

::: div .code-block
:::inline div .code-head
<span>Instruksi untuk AI (Step 1)</span><span class="dots">···</span>
:::

```
Aku perlu kerangka API backend.
Persyaratan:
1. Server Express, port 3001
2. Database SQLite, nama tabel records
3. Field tabel records:
   id (TEXT PRIMARY KEY)
   amount (REAL)
   type (TEXT: 'income'|'expense')
   category (TEXT)
   note (TEXT)
   date (TEXT: YYYY-MM-DD)
4. API CRUD:
   GET /api/records - ambil semua catatan
   POST /api/records - tambah catatan
   PUT /api/records/:id - perbarui catatan
   DELETE /api/records/:id - hapus catatan
5. Middleware penanganan error
Berikan struktur kode backend yang lengkap.
```
:::

Perhatikan ciri instruksi ini: ia hanya menjelaskan langkah saat ini (kerangka backend) tanpa mencampur kebutuhan frontend; ia secara eksplisit memuat daftar kolom dan antarmuka (memberi AI batasan yang cukup), tetapi detail implementasinya diserahkan pada AI; dan ia mengikuti prinsip Goal-Driven Execution—menyebut "apa yang dikerjakan", bukan "bagaimana mengerjakannya".

Begitu AI memberikan kodenya, langsung verifikasi: jalankan server, uji setiap antarmuka dengan curl atau Postman apakah berfungsi normal. Setelah dipastikan tidak ada masalah, buka percakapan baru untuk Langkah 2 (halaman dasar frontend). Setiap langkah mengikuti siklus "instruksi-verifikasi-percakapan baru".

#### 3. Proyek tiga: aplikasi yang diperkaya AI (tingkat mahir)

##### 1. Merancang gagasan proyek

Tujuan: satu aplikasi yang terhubung ke API model besar—misalnya "Asisten Belajar AI": pengguna memasukkan materi pelajaran, AI menghasilkan ringkasan, mengaitkan poin-poin pengetahuan, dan merekomendasikan sumber belajar. Keistimewaan proyek ini: aplikasimu sendiri yang memanggil AI, jadi kamu harus menangani masalah baru seperti pemanggilan API, rekayasa prompt, dan penanganan error.

Pelajaran terpenting dari proyek ini: ketika kamu "memakai AI untuk menulis kode yang memanggil AI", kamu harus ekstra memperhatikan rekayasa prompt. Prompt yang dipakai aplikasimu saat memanggil API model besar juga harus mengikuti prinsip yang dibahas panduan ini—jelas, ringkas, dan berorientasi tujuan.

##### 2. Poin-poin teknis kunci

Proyek ini melibatkan beberapa poin teknis yang belum kamu temui di dua proyek sebelumnya:

- Manajemen kunci API: kunci tidak boleh pernah ditulis langsung di dalam kode, kelola dengan environment variable;
- Penanganan respons streaming: jawaban model besar umumnya streaming dan perlu ditampilkan kata demi kata;
- Kontrol pemakaian token: model besar ditagih per token, jadi pemakaiannya perlu dikendalikan di level aplikasi;
- Manajemen templat prompt: fungsi berbeda memakai templat prompt berbeda, jadi perlu dikelola secara terstruktur.

Semua poin teknis ini bisa diserahkan pada AI, tetapi kamu perlu memahami "mengapa" di balik masing-masing—mengapa kunci tidak boleh ditulis langsung di kode? Mengapa respons streaming diperlukan? Mengapa pemakaian token harus dikendalikan? Dengan memahami "mengapa"-nya, kamu bisa menilai apakah solusi dari AI masuk akal.

#### 4. Daftar periksa alur praktik universal

Apa pun ukuran proyeknya, berikut daftar periksa alur praktik pemrograman AI yang universal. Setiap kali memulai proyek baru, lewati daftar ini sekali untuk memastikan tidak ada langkah kunci yang terlewat.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Tahap</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Apa yang dilakukan</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Prinsip terkait</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1. Merenungkan kebutuhan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lewati lima unsur kebutuhan, pastikan jelas apa yang mau dikerjakan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Think Before Coding</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2. Memecah kebutuhan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pecah kebutuhan besar menjadi langkah kecil yang bisa diverifikasi secara mandiri</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Simplicity First</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3. Menulis PRD</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Susun menjadi dokumen terstruktur sebagai rujukan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Goal-Driven</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">4. Menyiapkan berkas memori</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Buat CLAUDE.md atau berkas sejenis</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Harness Engineering</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">5. Implementasi bertahap</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Satu percakapan per langkah: instruksi-verifikasi-lanjut ke berikutnya</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Surgical Changes</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">6. Pengujian dan verifikasi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Uji kebenaran fungsinya langsung setelah setiap langkah selesai</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Iterate &amp; Verify</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">7. Tinjauan kode</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Periksa kewajaran arsitektur, keamanan, dan kemudahan perawatan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Iterate &amp; Verify</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">8. Iterasi dan optimalisasi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Perbaiki secara iteratif berdasarkan hasil pengujian dan tinjauan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Iterate &amp; Verify</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Daftar periksa alur praktik pemrograman AI yang universal

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mari praktik: selesaikan "Proyek Satu" minggu ini

{class="mt-1"}
Jadikan "situs alat pribadi" di Bagian 1 Bab 44 sebagai pekerjaan rumah pemrograman AI pertamamu: sisihkan 5 menit untuk melewati lima unsur, kirim instruksinya ke AI (alat apa pun boleh), lalu lakukan penerimaan dengan verifikasi tiga lapis. Selesaikan dalam 30 menit—karya pemrograman AI pertamamu pun lahir. Jangan lupa menyimpannya; ini kenang-an peralihanmu dari "pembaca" menjadi "praktisi".
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan bab ini

- Proyek satu (pemula): situs alat frontend murni—merasakan alur lengkap, selesai dalam 30 menit
- Proyek dua (menengah): sistem pencatatan keuangan full-stack—PRD + berkas memori + implementasi bertahap 5 langkah, setiap langkah "bisa dipakai"
- Proyek tiga (mahir): Asisten Belajar AI—memakai AI untuk menulis kode yang memanggil AI, perhatikan rekayasa prompt
- Delapan langkah alur universal: renungkan kebutuhan → pecah → PRD → berkas memori → implementasi bertahap → uji → tinjau → iterasi
- Setiap langkah mengikuti siklus "instruksi-verifikasi-percakapan baru"
:::
