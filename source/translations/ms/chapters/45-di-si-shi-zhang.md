---
id: di-si-shi-zhang
num: 40
part: ai-biancheng-pian
nav: Bab 40: Kejuruteraan Keperluan—Mengubah Idea menjadi Arahan AI
toc: default
kind: chapter
---

### Bab 40: Kejuruteraan Keperluan — Mengubah Idea Menjadi Arahan yang Boleh Dilaksanakan oleh AI

{class="chapter-intro mb-4"}
Jika kejuruteraan konteks menyelesaikan masalah "membuat AI memahami latar belakang", maka kejuruteraan keperluan menyelesaikan masalah "membuat AI tahu apa yang perlu dibuat kali ini". Inilah bahagian dalam pengaturcaraan AI yang paling menonjolkan perbezaan antara individu — alat yang sama, model yang sama, tetapi ada yang mampu menghasilkan projek yang mengagumkan, ada yang hanya menghasilkan mainan biasa-biasa. Perbezaannya sering kali bukan pada kebolehan teknikal, tetapi pada keupayaan menyatakan keperluan.

#### 1. Daripada Idea Kabur kepada Keperluan Berstruktur

Setiap projek bermula dengan satu idea yang kabur — "Saya nak buat aplikasi perakaunan", "Saya nak buat laman web peribadi", "Saya nak buat alat senarai tugasan". Idea-idea ini tiada masalah, tetapi jika anda terus menyampaikannya kepada AI, kualiti hasilnya bergantung sepenuhnya pada nasib. Matlamat kejuruteraan keperluan ialah mengubah idea kabur ini menjadi keperluan berstruktur yang boleh dilaksanakan oleh AI dengan tepat.

Berita baiknya: keperluan berstruktur tidak memerlukan anda menulis PRD setebal puluhan muka surat. Anda hanya perlu menjawab lima soalan, yang kami gelar "lima elemen keperluan":

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Elemen</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Soalan</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Contoh: Aplikasi Perakaunan</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Untuk siapa?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Penggunaan peribadi, merekod pendapatan dan perbelanjaan harian</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Buat apa?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Aplikasi yang boleh merekod setiap urus niaga pendapatan dan perbelanjaan, meringkaskan mengikut bulan dan memaparkannya secara visual</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kenapa dibuat?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ingin memahami corak perbelanjaan sendiri dan mengenal pasti perbelanjaan yang tidak perlu</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Macam mana nak buat secara kasar?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bahagian hadapan guna React, data disimpan secara tempatan dalam pelayar; bahagian belakang dan log masuk tidak dibuat dahulu</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apakah hadnya?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Dibangunkan oleh seorang sahaja, siap dalam tempoh 2 minggu, tidak perlu dilancarkan atas talian</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Lima elemen keperluan beserta contoh

Kelima-lima elemen ini tidak perlu ditulis sebagai dokumen rasmi; malah cukup dengan menyemaknya secara pantas dalam fikiran. Kuncinya ialah membentuk tabiat "fikir dengan jelas dahulu sebelum bercakap". Anda akan mendapati, apabila anda mampu menjawab kelima-lima soalan ini dengan jelas, penerangan keperluan anda secara semula jadi menjadi berstruktur.

#### 2. Seni Pelapisan Pemecahan Keperluan

Bagi projek yang lebih besar, satu penerangan keperluan tidak mencukupi. Anda perlu memecahkan keperluan besar kepada sub-keperluan kecil yang boleh disahkan secara berasingan. Proses ini dipanggil "pemecahan keperluan"; prinsip terasnya: setiap sub-keperluan harus boleh disiapkan, disahkan dan diserahkan secara berasingan.

Ambil "membuat aplikasi perakaunan peribadi" sebagai contoh; satu cara pemecahan yang munasabah ialah:

1. Melaksanakan fungsi asas perekodan pendapatan dan perbelanjaan (boleh tambah, lihat dan padam rekod);
2. Menambah fungsi kategori (melekatkan label seperti makanan atau pengangkutan pada setiap rekod);
3. Melaksanakan fungsi ringkasan bulanan (menghitung pendapatan dan perbelanjaan mengikut bulan);
4. Menambah visualisasi data (memaparkan corak perbelanjaan dengan carta).

Setiap langkah ialah satu tambahan ciri yang boleh berjalan dan disahkan secara berasingan.

:::inline div .quote-line
Hukum emas mengurai keperluan: setiap langkah selesai, projek harus berupa "benda yang boleh guna"—walaupun fungsinya kasar. Jangan sesekali biarkan projek terhenti dalam keadaan "semuanya separuh siar tetapi tak satu pun boleh guna".
:::

Cara pemecahan ini mempunyai dua kelebihan. Pertama, ia membolehkan anda sentiasa melihat kemajuan — setiap satu langkah selesai, aplikasi anda bertambah satu ciri, dan maklum balas positif ini amat penting untuk projek jangka panjang (semua orang memang perlukan rasa pencapaian). Kedua, ia menjadikan setiap tugasan AI cukup kecil, mengurangkan risiko "kefahaman AI yang tersasar" — semakin kecil tugasan, semakin tepat kefahaman AI, dan semakin tinggi kualiti hasilnya.

#### 3. Templat dan Amalan Penulisan PRD

Bagi projek yang lebih besar (contohnya, aplikasi penuh yang mempunyai bahagian hadapan dan belakang serta beberapa modul ciri), lima elemen keperluan sahaja mungkin tidak mencukupi. Pada ketika ini anda perlu menulis dokumen keperluan projek (PRD) yang lebih rasmi. Satu perkara yang mudah disalahertikan: PRD bukan ditulis untuk AI — ia ditulis untuk anda sendiri, untuk membantu anda menyusun fikiran; barulah anda dapat memberikan arahan yang lebih tepat kepada AI.

PRD yang baik tidak perlu panjang, tetapi patut mengandungi enam bahagian: gambaran keseluruhan projek (satu perenggan menjelaskan apa yang dibuat), senarai ciri (apa setiap ciri itu), pelan teknikal (tindanan teknologi yang digunakan dan seni bina kasar), model data (struktur data teras), penerangan antara muka (rupa halaman utama) dan pelan pembangunan (berapa langkah untuk siap).

::: div .code-block
:::inline div .code-head
<span>PRD.md</span><span class="dots">···</span>
:::

```
# PRD aplikasi perakaunan peribadi
## Ringkasan projek
Aplikasi perakaunan peribadi yang ringan, menyokong rekod pendapatan/perbelanjaan, kategori, ringkasan bulanan dan visualisasi data.
## Senarai fungsi
1. Rekod pendapatan/perbelanjaan: jumlah, jenis (masuk/keluar), kategori, nota, tarikh
2. Pengurusan kategori: sedia ada makanan, pengangkutan, beli-belah, hiburan, lain-lain
3. Ringkasan bulanan: jumlah pendapatan, perbelanjaan dan baki setiap bulan
4. Visualisasi perbelanjaan: carta pai menunjukkan pecahan setiap kategori
5. Eksport data: ke CSV
## Pelan teknikal
- Frontend: React + TypeScript + Tailwind CSS
- Simpanan data: localStorage (tanpa backend)
- Carta: guna Chart.js
- Binaan: Vite
## Model data
Record {
  id: string
  amount: number
  type: 'income' | 'expense'
  category: string
  note: string
  date: string  // YYYY-MM-DD
}
## Pelan pembangunan
Step 1: fungsi rekod asas (CRUD)
Step 2: pengurusan kategori
Step 3: ringkasan bulanan
Step 4: visualisasi data
Step 5: eksport data
```
:::

Perhatikan gaya penulisan PRD ini: gunakan senarai yang ringkas dan format berstruktur, bukan huraian panjang lebar. Setiap ciri mempunyai definisi yang jelas, dan model data diterangkan dengan jenis yang mudah. PRD bergaya sedemikian bukan sahaja jelas untuk anda baca sendiri; apabila diberikan kepada AI, AI juga dapat memahami setiap titik keperluan dengan tepat.

#### 4. Praktik: Proses Lengkap daripada Idea kepada Pelan

Bercakap teori sahaja kurang menarik; mari kita gunakan satu contoh lengkap untuk menghayati keseluruhan proses kejuruteraan keperluan. Katakan idea anda ialah: "Saya nak buat penjejak pembelajaran yang boleh menjejak apa yang saya pelajari setiap hari".

Langkah pertama, lalui lima elemen keperluan.

- Who (Siapa): Penggunaan peribadi.
- What (Apa): Alat yang boleh merekod kandungan pembelajaran setiap hari, menjejak tempoh pembelajaran dan mengulang kaji kemajuan pembelajaran.
- Why (Kenapa): Ingin membentuk tabiat belajar berterusan dan melihat pengumpulan diri sendiri.
- How (Bagaimana): Buat versi laman web dahulu, data disimpan secara tempatan dalam pelayar.
- Constraint (Had): Pembangunan sebagai pemula tanpa asas, ciri teras siap dalam tempoh 1 minggu.

Langkah kedua, pecahkan keperluan.

1. Langkah 1: Laksanakan fungsi "rekod entri pembelajaran" (tarikh, kandungan, tempoh);
2. Langkah 2: Tambah "statistik tempoh pembelajaran" (hari ini, jumlah kumulatif minggu ini);
3. Langkah 3: Laksanakan paparan "kalendar pembelajaran" (dipaparkan seperti carta sumbangan GitHub);
4. Langkah 4: Tambah fungsi "ulang kaji pembelajaran" (memaparkan secara rawak rekod pembelajaran suatu hari yang lalu untuk membantu mengulang kaji).

Langkah ketiga, tulis satu PRD ringkas. Tidak perlu panjang — pemecahan di atas itu sendiri sudah menjadi isi utama PRD. Susunannya menjadi satu fail .md, letakkan dalam direktori akar projek, sebagai rujukan bersama anda dan AI.

Langkah keempat, mulakan pembangunan langkah pertama. Arahan kepada AI boleh seperti ini:

::: div .code-block
:::inline div .code-head
<span>Arahan untuk AI</span><span class="dots">···</span>
:::

```
Saya perlukan fungsi pertama untuk penjejak pembelajaran—merekod sesi pembelajaran.
Pengguna boleh menambah satu rekod pembelajaran, merangkumi tarikh, kandungan pembelajaran dan tempoh (minit).
Data disimpan dalam localStorage.
Frontend guna React + TypeScript.
Berikan pelaksanaan lengkap.
```
:::

Perhatikan ciri arahan ini: ia hanya menerangkan matlamat langkah semasa (fungsi perekodan) tanpa mencampurkan ciri lain; ia menyatakan dengan jelas kekangan teknikal (React, TypeScript, localStorage); ia memberikan maklumat yang cukup supaya AI tahu "apa yang perlu dibuat" dan "cara membuatnya", tetapi pelaksanaan khusus diserahkan kepada AI. Inilah arahan pengaturcaraan AI bermutu tinggi yang telah diproses melalui kejuruteraan keperluan.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mari praktik: Tulis kad lima elemen untuk projek idaman anda

{class="mt-1"}
Pilih satu projek kecil yang sudah lama anda perah, luangkan 5 minit untuk mengisi satu kad: Who / What / Why / How / Constraint, satu ayat bagi setiap satu. Kemudian pecahkannya kepada 3-5 langkah yang "setiap satu boleh digunakan". Anda akan mendapati: selepas idea ditulis, ia berubah daripada "mimpi siang" kepada "senarai tugasan".
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan Bab Ini

- Lima elemen keperluan: Who / What / Why / How / Constraint — fikir dengan jelas sebelum bercakap
- Peraturan emas pemecahan keperluan: selepas setiap langkah selesai, projek tetap "benda yang boleh digunakan"
- PRD ditulis untuk diri sendiri: gambaran keseluruhan, senarai ciri, pelan teknikal, model data, antara muka, pelan
- Arahan yang baik = hanya menerangkan langkah semasa + kekangan yang jelas + kata "apa yang dibuat", bukan "bagaimana membuatnya"
- Templat proses lengkap: lima elemen → pemecahan → PRD → beri arahan, empat langkah
:::
