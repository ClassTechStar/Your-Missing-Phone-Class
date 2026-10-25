---
id: di-san-shi-jiu-zhang
num: 39
part: ai-biancheng-pian
nav: Bab 39: Kejuruteraan Konteks—Memastikan AI Memahami Niat Anda
toc: default
kind: chapter
---

### Bab 39: Kejuruteraan konteks - membuat AI memahami niat anda

{class="chapter-intro mb-4"}
Pernahkah anda mengalami ini: bertukar kepada tetingkap perbualan baharu, dan AI seperti hilang ingatan, lupa segala keadaan asas projek anda? Ini bukan AI sengaja menyakitkan hati anda, tetapi ia memang "pelupa" dari asal. Bab ini mengajar anda memasang satu "sistem ingatan jangka panjang" untuk AI, dan sekali gus mengenali salah satu paradigma pembangunan paling popular 2026 - pembangunan didorong spesifikasi.

#### 1. Fail ingatan projek: "ingatan jangka panjang" AI

Model AI mempunyai satu had asas: ingatannya bersifat "jangka pendek". Setiap kali perbualan bermula, pengetahuan AI tentang projek anda ialah sifar. Anda perlu sentiasa memberitahunya dalam perbualan "kita guna React" "backend ialah Node.js" "pangkalan data ialah PostgreSQL" "gaya kod guna petikan berganda". Ini bukan sahaja tidak cekap, malah mudah tertinggal - seperti perlu melakukan orientasi semula setiap hari kepada rakan sekerja baharu.

Penyelesaiannya ialah "fail ingatan projek" - satu fail teks tulen yang diletakkan di direktori akar projek, dan alat AI akan membacanya secara automatik setiap kali perbualan bermula. Alat yang berbeza mempunyai konvensyen penamaan yang berbeza:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Alat</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Nama fail</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cursor</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.cursorrules</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Code</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">CLAUDE.md</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GitHub Copilot</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">copilot-instructions.md</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Penyelesaian generik</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">AGENTS.md</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Konvensyen penamaan fail ingatan projek bagi setiap alat

Walaupun penamaannya berbeza, prinsipnya sama: tulis maklumat yang anda mahu AI "sentiasa ingat" dalam fail ini. Fail ingatan projek yang baik patut mengandungi: gambaran keseluruhan projek (apa projek ini), timbunan teknologi (teknologi apa yang digunakan), piawaian kod (penamaan, inden, gaya komen), struktur direktori (bagaimana kod disusun), dan konvensyen pembangunan (strategi cawangan, piawaian commit, keperluan ujian). CLAUDE.md Karpathy hanya 70 baris, tetapi meliputi semua maklumat utama - ringkas tetapi lengkap.

::: div .code-block
:::inline div .code-head
<span>CLAUDE.md</span><span class="dots">···</span>
:::

```
# Projek: aplikasi perakaunan peribadi
## Ringkasan
Aplikasi perakaunan peribadi penuh untuk membantu pengguna merekod pendapatan-perbelanjaan harian.
## Teknologi
- Frontend: React + TypeScript + Tailwind CSS
- Backend: Node.js + Express + TypeScript
- Pangkalan data: SQLite (pembangunan) / PostgreSQL (pengeluaran)
- Ujian: Vitest
## Peraturan penulisan kod
- Guna petikan berganda
- Inden 2 ruang
- Nama fungsi guna camelCase
- Definisi jenis guna PascalCase
- Setiap fungsi mesti ada komen JSDoc
## Struktur direktori
/src
  /frontend  - kod frontend
  /backend   - kod backend
  /shared    - jenis dikongsi bersama
  /tests     - fail ujian
## Persetujuan pembangunan
- Mesej komit dalam bahasa Mandarin
- Fungsi baru mesti tulis ujian dahulu
- Respons API seragam dengan format { success, data, error }
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Perhatian: jangan tulisnya menjadi "dokumen keperluan kedua"

{class="mt-1"}
Perhatikan panjang fail ini - jangan tulisnya menjadi dokumen keperluan berpuluh halaman. Tujuan fail ingatan projek ialah "membolehkan AI cepat membina pemahaman latar", bukan "menerangkan setiap fungsi secara terperinci". Kekalkan ringkas, berstruktur, dan hanya tulis "apa yang AI perlu tahu".
:::

#### 2. Pembangunan didorong spesifikasi (SDD)

Spec-Driven Development (SDD, pembangunan didorong spesifikasi) ialah satu paradigma pembangunan yang semakin matang pada 2026; ide terasnya dalam satu ayat: tulis spesifikasi dahulu, kemudian tulis kod. Berbeza dengan TDD tradisional (pembangunan didorong ujian), "spesifikasi" SDD bukan sahaja kes ujian, malah merangkumi penerangan keperluan, takrif antara muka, model data dan sebagainya. AI menjana kod berdasarkan spesifikasi ini, manakala tugas manusia ialah menulis dan menyelenggara spesifikasi.

Aliran kerja SDD lima langkah:

1. Terangkan spesifikasi keperluan dengan bahasa semula jadi (tulis dalam satu fail .md);
2. Takrifkan antara muka dan struktur data (tulis dalam fail spesifikasi);
3. Biarkan AI menjana pelaksanaan kod berdasarkan spesifikasi;
4. Jalankan ujian untuk mengesahkan sama ada hasil memenuhi spesifikasi;
5. Jika tidak memenuhi, baik pulih spesifikasi atau biarkan AI membaiki kodnya.

Dalam aliran kerja ini, fail spesifikasi ialah "sumber kebenaran tunggal" - kod boleh dijana semula, tetapi spesifikasi mesti betul dahulu.

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> Menulis fail spesifikasi</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> Adakah spesifikasi sudah lengkap?</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> Lengkap</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-robot mr-1"></i> AI menjana kod daripada spesifikasi</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> Jalankan ujian untuk sahkan hasil</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-times-circle mr-1"></i> Spesifikasi tidak lengkap / ujian gagal</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-tools mr-1"></i> Masalah kod → betulkan kod; masalah spesifikasi → betulkan spesifikasi</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> Kembali ke pengesahan</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> Lulus semua → serah</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Rajah 3: Aliran kerja pembangunan didorong spesifikasi (SDD)
:::

Kelebihan SDD terletak pada: fail spesifikasi lebih stabil daripada kod. Apabila model atau alat asas berubah, fail spesifikasi anda tetap sah; anda hanya perlu membiarkan alat AI baharu menjana semula kod. Itulah sebabnya buku ini menekankan "metodologi lebih penting daripada alat" - fail spesifikasi itulah pembawa konkrit metodologi anda.

#### 3. Pengurusan tetingkap konteks

Walaupun sudah ada fail ingatan projek, anda masih akan menghadapi masalah "konteks tidak cukup" dalam perbualan. Tetingkap konteks model AI (jumlah maklumat yang boleh diproses serentak) adalah terhad. Apabila perbualan terlalu panjang atau fail yang dirujuk terlalu banyak, AI akan "lupa" maklumat awal, menyebabkan kualiti hasil menurun - seperti anda berbual dengan seorang kawan selama enam jam, dia sudah lama lupa perkara pertama yang anda katakan pada awalnya.

Strategi teras mengurus tetingkap konteks ialah "rujukan berlapis":

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Lapisan konteks</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Kandungan</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Cara pengurusan</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lapisan satu: ingatan projek</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Timbunan teknologi, spesifikasi, struktur direktori</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ditulis dalam fail seperti CLAUDE.md, dimuatkan secara automatik, tidak perlu diulang</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lapisan dua: rujukan fail</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Fail kod yang terlibat dalam tugas semasa</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Rujuk dengan tepat menggunakan simbol @, jangan tampal teks penuh ke dalam perbualan</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lapisan tiga: konteks perbualan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sejarah perbualan tugas semasa</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Buka perbualan baharu selepas menyiapkan satu tugas, elak konteks membengkak</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lapisan empat: arahan serta-merta</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Keperluan khusus langkah semasa ini</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Jelas, ringkas, bersasar, elak penerangan berjela</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Strategi pengurusan berlapis tetingkap konteks

#### 4. Perkara Penting Amalan Kejuruteraan Konteks

Kejuruteraan konteks bukan sekadar tetapan sekali sahaja, tetapi satu proses penambahbaikan berterusan. Berikut ialah beberapa perkara penting yang telah terbukti berulang kali dalam amalan:

1. Kemas kini fail memori selari dengan perkembangan projek. Apabila memperkenalkan teknologi baharu atau mengubah seni bina, kemas kini fail memori dengan segera, jangan hanya jelaskan secara sementara dalam perbualan.
2. Gunakan rujukan @ dengan bijak berbanding menampal keseluruhan teks. Kebanyakan alat pengaturcaraan AI menyokong sintaks @file atau @folder, yang menyuntik kandungan fail ke dalam konteks AI di latar belakang — lebih cekap daripada menampal secara manual dan tidak mencemarkan perbualan.
3. Perbualan perlu "pendek dan padat". Satu perbualan hanya mengurus satu tugasan atau satu ciri. Selepas selesai, buka perbualan baharu untuk yang seterusnya. Perbualan panjang bukan sahaja menghabiskan tetingkap konteks, malah boleh membuat AI "hilang tumpuan".
4. Berikan AI "melihat" hasil, bukan "menerangkan" hasil. Apabila menghadapi bug, rujuk log ralat terus kepada AI dengan @, jangan hanya terangkan dengan kata-kata sendiri "macam ada sebarang ralat". AI lebih berkesan apabila melihat maklumat asli berbanding huraian anda.
5. Mengarkib dan membersih secara berkala. Perbualan yang telah selesai dan fail sementara akan memenuhi ruang kerja. Membersihkan kandungan yang tidak berkaitan secara berkala serta mengekalkan direktori projek yang kemas juga membantu AI memahami struktur projek dengan lebih cekap.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mari praktik: Tulis satu fail memori 70 baris untuk projek anda

{class="mt-1"}
Pilih satu projek yang sedang anda buat (atau ingin buat), dan tulis satu fail CLAUDE.md: gambaran keseluruhan projek (2-3 ayat), tindanan teknologi (senaraikan), peraturan kod (3-5 perkara), struktur direktori (lukis pepohon) dan konvensyen pembangunan (2-3 perkara). Kekalkan dalam 70 baris — selepas menulis, anda akan mendapati pemahaman anda terhadap projek menjadi jauh lebih jelas.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan Bab Ini

- Memori AI bersifat "jangka pendek": setiap kali perbualan baharu bermula, pengetahuannya tentang projek ialah sifar
- Fail memori projek (CLAUDE.md dan sebagainya) ialah "memori jangka panjang" AI, dimuatkan secara automatik pada setiap perbualan
- Fail memori yang baik = gambaran keseluruhan + tindanan teknologi + peraturan + direktori + konvensyen, 70 baris sudah memadai
- Pembangunan dipacu spesifikasi (SDD): tulis spesifikasi dahulu sebelum menulis kod; spesifikasi ialah "sumber kebenaran tunggal", lebih stabil daripada kod
- Konteks diurus dalam empat lapisan: memori projek → rujukan @fail → sejarah perbualan → arahan serta-merta
- Lima perkara penting amalan: kemas kini serentak, rujukan @, perbualan pendek, beri maklumat asli, bersih secara berkala
:::
