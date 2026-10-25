---
id: di-san-shi-jiu-zhang
num: 39
part: ai-biancheng-pian
nav: Bab 39: Context Engineering—Membuat AI Memahami Niatmu
toc: default
kind: chapter
---

### Bab 39: Rekayasa Konteks—Membuat AI Memahami Maksud Anda

{class="chapter-intro mb-4"}
Pernah mengalami ini: ganti jendela percakapan baru, AI seperti lupa ingatan—semua dasar proyek Anda hilang dari kepalanya? Ini bukan AI sengaja menyebalkan—memang ia "pelupa" sejak lahir. Bab ini mengajarkan cara memasang "sistem memori jangka panjang" untuk AI, sekaligus mengenalkan salah satu paradigma pengembangan paling populer pada 2026—spec-driven development.

#### 1. File memori proyek: "memori jangka panjang" AI

Model AI punya keterbatasan mendasar: memorinya "jangka pendek". Setiap kali percakapan dimulai, pengetahuan AI tentang proyek Anda adalah nol. Anda harus terus-menerus memberi tahu "kami memakai React" "backend-nya Node.js" "databasenya PostgreSQL" "gaya kode pakai tanda kutip ganda". Ini tidak hanya tidak efisien, tetapi juga mudah terlewat—seperti setiap hari harus melatih karyawan baru dari awal.

Solusinya adalah "file memori proyek"—sebuah file teks biasa di root proyek yang dibaca otomatis oleh alat AI setiap kali percakapan dimulai. Tiap alat punya konvensi penamaan berbeda:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Alat</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Nama file</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cursor</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.cursorrules</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Code</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">CLAUDE.md</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GitHub Copilot</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">copilot-instructions.md</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Solusi umum</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">AGENTS.md</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Konvensi penamaan file memori proyek berbagai alat

Meski namanya berbeda, prinsipnya sama: tulis informasi yang ingin Anda "selalu ingatkan" kepada AI di file ini. File memori proyek yang baik seharusnya memuat: ikhtisar proyek (proyek apa ini), stack teknologi (teknologi apa yang dipakai), standar kode (penamaan, indentasi, gaya komentar), struktur direktori (bagaimana kode diorganisasi), konvensi pengembangan (strategi branching, standar commit, tuntutan pengujian). CLAUDE.md Karpathy hanya 70 baris—tetapi mencakup semua informasi kunci: ringkas namun lengkap.

::: div .code-block
:::inline div .code-head
<span>CLAUDE.md</span><span class="dots">···</span>
:::

```
# Proyek: aplikasi pencatat keuangan pribadi
## Gambaran
Aplikasi pencatat keuangan pribadi full-stack untuk membantu pengguna mencatat pemasukan-pengeluaran harian.
## Teknologi
- Frontend: React + TypeScript + Tailwind CSS
- Backend: Node.js + Express + TypeScript
- Database: SQLite (pengembangan) / PostgreSQL (produksi)
- Testing: Vitest
## Aturan penulisan kode
- Pakai tanda kutip ganda
- Indentasi 2 spasi
- Nama fungsi pakai camelCase
- Definisi tipe pakai PascalCase
- Setiap fungsi wajib ada komentar JSDoc
## Struktur direktori
/src
  /frontend  - kode frontend
  /backend   - kode backend
  /shared    - tipe yang dipakai bersama
  /tests     - file pengujian
## Kesepakatan pengembangan
- Pesan commit dalam bahasa Mandarin
- Fitur baru wajib tulis test dulu
- Respons API seragam dengan format { success, data, error }
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Catatan: jangan ditulis jadi "dokumen kebutuhan kedua"

{class="mt-1"}
Perhatikan panjang file ini—jangan sampai menjadi dokumen kebutuhan puluhan halaman. Tujuan file memori proyek adalah "membangun latar belakang pemahaman AI dengan cepat", bukan "mendeskripsikan setiap fitur secara detail". Jaga tetap ringkas, terstruktur, dan hanya tulis "yang perlu diketahui AI".
:::

#### 2. Spec-Driven Development (SDD)

Spec-Driven Development (SDD, pengembangan berbasis spesifikasi) adalah paradigma pengembangan yang mulai matang pada 2026—inti idenya satu kalimat: tulis spesifikasi dulu, baru tulis kode. Berbeda dengan TDD (test-driven development) tradisional, "spesifikasi" SDD tidak hanya kasus uji, tetapi juga deskripsi kebutuhan, definisi antarmuka, model data, dan lainnya. AI menghasilkan kode berdasarkan spesifikasi ini—tugas manusia adalah menulis dan memelihara spesifikasinya.

Alur kerja SDD dalam lima langkah:

1. Deskripsikan spesifikasi kebutuhan dalam bahasa alami (tulis di file .md);
2. Definisikan antarmuka dan struktur data (tulis di file spesifikasi);
3. Biarkan AI menghasilkan implementasi kode berdasarkan spesifikasi;
4. Jalankan tes untuk memverifikasi apakah keluaran sesuai spesifikasi;
5. Jika tidak sesuai, perbaiki spesifikasinya atau minta AI memperbaiki kodenya.

Dalam alur ini, file spesifikasi adalah "sumber kebenaran tunggal"—kode bisa dibuat ulang, tetapi spesifikasi harus lebih dulu benar.

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> Menulis file spesifikasi</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> Apakah spesifikasi sudah lengkap?</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> Lengkap</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-robot mr-1"></i> AI membuat kode dari spesifikasi</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> Jalankan test untuk memverifikasi hasil</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-times-circle mr-1"></i> Spesifikasi belum lengkap / test gagal</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-tools mr-1"></i> Masalah kode → perbaiki kode; masalah spesifikasi → perbaiki spesifikasi</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> Kembali ke verifikasi</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> Lulus semua → serahkan</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Gambar 3: Alur kerja Spec-Driven Development (SDD)
:::

Keunggulan SDD: file spesifikasi lebih stabil daripada kode. Saat model dasar atau alat berubah, file spesifikasi Anda tetap berlaku—cukup minta alat AI baru menghasilkan ulang kodenya. Inilah sebabnya buku ini menekankan "metodologi lebih penting daripada alat"—file spesifikasi adalah wujud nyata metodologi Anda.

#### 3. Manajemen jendela konteks

Meski sudah punya file memori proyek, Anda tetap akan menghadapi masalah "konteks tidak cukup" di percakapan. Jendela konteks model AI (jumlah informasi yang bisa diproses sekaligus) itu terbatas. Saat percakapan terlalu panjang dan file yang dirujuk terlalu banyak, AI akan "melupakan" informasi awal—kualitas keluaran pun menurun. Ibarat Anda ngobrol dengan teman selama enam jam—ia sudah lupa apa yang Anda katakan di awal.

Strategi inti manajemen jendela konteks adalah "rujukan berlapis":

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Tingkat konteks</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Isi</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Cara mengelola</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lapis 1: memori proyek</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Stack teknologi, standar, struktur direktori</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tulis di file seperti CLAUDE.md—dimuat otomatis, tidak perlu diulang</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lapis 2: rujukan file</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">File kode yang terlibat tugas saat ini</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Rujuk presisi dengan simbol @—jangan tempel seluruh isi ke percakapan</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lapis 3: konteks percakapan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Riwayat percakapan tugas saat ini</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Setelah satu tugas selesai, buka percakapan baru—hindari konteks membengkak</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lapis 4: instruksi sesaat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tuntutan spesifik langkah saat ini</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Jelas, ringkas, terarah—hindari deskripsi bertele-tele</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Strategi manajemen berlapis untuk jendela konteks

#### 4. Poin Praktis Rekayasa Konteks

Rekayasa konteks bukan pengaturan sekali jadi, melainkan proses penyempurnaan yang berkelanjutan. Berikut beberapa poin yang telah teruji berulang kali dalam praktik:

1. Perbarui file memori secara sinkron seiring berkembangnya proyek. Saat memperkenalkan teknologi baru atau mengubah arsitektur, segera perbarui file memorinya, jangan hanya menjelaskannya dadakan di percakapan.
2. Manfaatkan referensi @ daripada menempel seluruh teks. Sebagian besar alat pemrograman AI mendukung sintaks @file atau @folder, yang menyuntikkan isi file ke konteks AI di latar belakang — lebih efisien daripada menempel manual dan tidak mencemari percakapan.
3. Buat percakapan yang "singkat dan padat". Satu percakapan hanya menangani satu tugas atau satu fitur. Setelah selesai, buka percakapan baru untuk tugas berikutnya. Percakapan yang panjang tidak hanya menguras jendela konteks, tetapi juga membuat AI "terpecah fokus".
4. Tunjukkan hasilnya kepada AI, jangan sekadar "mendeskripsikan" hasilnya. Saat menemukan bug, langsung rujuk log errornya dengan @ kepada AI, bukan mendeskripsikannya dengan kata-kata sendiri seperti "sepertinya ada error begitu". AI jauh lebih efektif melihat informasi mentah daripada menerima parafrase dari kamu.
5. Bersihkan dan arsipkan secara berkala. Percakapan yang sudah selesai dan file sementara memakan ruang kerja. Rutin membersihkan konten yang tidak relevan dan menjaga kerapian direktori proyek juga membantu AI memahami struktur proyek dengan lebih efisien.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Praktik Yuk: Tulis File Memori 70 Baris untuk Proyekmu

{class="mt-1"}
Pilih satu proyek yang sedang (atau akan) kamu kerjakan, lalu tulis sebuah CLAUDE.md: gambaran umum proyek (2-3 kalimat), tech stack (daftar saja), aturan kode (3-5 poin), struktur direktori (gambar diagram pohonnya), dan konvensi pengembangan (2-3 poin). Batasi maksimal 70 baris — setelah menulisnya, kamu akan sadar pemahamanmu tentang proyek menjadi jauh lebih jelas.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan Bab Ini

- Memori AI itu "jangka pendek": setiap percakapan baru, pengetahuannya tentang proyek kembali nol
- File memori proyek (CLAUDE.md dan sejenisnya) adalah "memori jangka panjang" AI, dimuat otomatis di setiap percakapan
- File memori yang baik = gambaran umum + tech stack + aturan + struktur direktori + konvensi, cukup 70 baris
- SDD (pengembangan berbasis spesifikasi): tulis spesifikasi dulu baru kodenya; spesifikasi adalah "sumber kebenaran tunggal" yang lebih stabil daripada kode
- Konteks dikelola dalam empat lapis: memori proyek → referensi @file → riwayat percakapan → instruksi langsung
- Lima poin praktis: perbarui secara sinkron, rujuk dengan @, percakapan singkat, berikan info mentah, bersihkan secara berkala
:::
