---
id: di-si-shi-zhang
num: 40
part: ai-biancheng-pian
nav: Bab 40: Requirements Engineering—Mengubah Ide Menjadi Instruksi AI
toc: default
kind: chapter
---

### Bab 40: Rekayasa Kebutuhan — Mengubah Ide Menjadi Instruksi yang Bisa Dieksekusi AI

{class="chapter-intro mb-4"}
Jika rekayasa konteks menjawab "membuat AI memahami latar belakang", maka rekayasa kebutuhan menjawab "membuat AI tahu apa yang spesifik harus dikerjakan kali ini". Inilah bagian dari pemrograman AI yang paling menunjukkan perbedaan antar manusia — dengan alat yang sama dan model yang sama, ada yang bisa membuat proyek yang menakjubkan, ada pula yang hanya mampu membuat mainan biasa-biasa saja. Perbedaannya seringkali bukan pada kemampuan teknis, melainkan pada kemampuan mengungkapkan kebutuhan.

#### 1. Dari Ide Kabur ke Kebutuhan Terstruktur

Setiap proyek dimulai dari ide yang masih kabur — "aku ingin membuat aplikasi pencatat keuangan", "aku ingin punya situs web pribadi", "aku ingin membuat alat daftar tugas". Ide-ide seperti itu tidak ada masalah, tetapi kalau langsung dilempar ke AI, kualitas hasilnya sepenuhnya tergantung keberuntungan. Tujuan rekayasa kebutuhan adalah mengubah ide kabur itu menjadi kebutuhan terstruktur yang bisa dieksekusi AI secara presisi.

Kabar baiknya: kebutuhan terstruktur tidak mengharuskanmu menulis PRD setebal puluhan halaman. Kamu hanya perlu menjawab lima pertanyaan, yang kita sebut "Lima Elemen Kebutuhan":

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Elemen</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Pertanyaan</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Contoh: Aplikasi Pencatat Keuangan</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Untuk siapa?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Penggunaan pribadi, mencatat pemasukan-pengeluaran harian</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apa yang dibuat?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Aplikasi yang bisa mencatat setiap transaksi, merangkum per bulan, dan menampilkannya secara visual</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mengapa dibuat?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ingin memahami pola pengeluaran dan menemukan belanja yang tidak perlu</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bagaimana kira-kira caranya?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Frontend pakai React, data disimpan lokal di browser, backend dan login dulu tidak usah dibuat</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apa batasannya?</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Dikembangkan sendirian, selesai dalam 2 minggu, tidak perlu deployment ke produksi</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Lima Elemen Kebutuhan beserta contohnya

Kelima elemen ini tidak perlu ditulis sebagai dokumen resmi; cukup bahkan hanya dilalui cepat di kepala. Kuncinya adalah membiasakan diri "berpikir jernih dulu sebelum bicara". Kamu akan menemukan bahwa saat bisa menjawab kelima pertanyaan ini dengan jelas, deskripsi kebutuhanmu otomatis menjadi terstruktur.

#### 2. Seni Memecah Kebutuhan Secara Bertingkat

Untuk proyek yang lebih besar, satu deskripsi kebutuhan saja tidak cukup. Kamu perlu memecah kebutuhan besar menjadi sub-kebutuhan yang kecil dan bisa diverifikasi secara mandiri. Proses ini disebut "pemecahan kebutuhan", dengan prinsip inti: setiap sub-kebutuhan harus bisa diselesaikan, diverifikasi, dan diserahkan secara mandiri.

Ambil contoh "membuat aplikasi pencatat keuangan pribadi"; cara memecah yang masuk akal adalah:

1. Membuat fungsi dasar pencatatan pemasukan-pengeluaran (bisa menambah, melihat, dan menghapus catatan);
2. Menambahkan fungsi kategori (menempelkan label seperti makanan, transportasi, dan lainnya pada tiap catatan);
3. Membuat fungsi ringkasan bulanan (menghitung pemasukan-pengeluaran per bulan);
4. Menambahkan visualisasi data (menampilkan pola pengeluaran dalam bentuk grafik).

Setiap langkah adalah penambahan fitur yang bisa dijalankan dan diverifikasi secara mandiri.

:::inline div .quote-line
Aturan emas merinci kebutuhan: setiap langkah selesai, proyek harus berupa "sesuatu yang bisa dipakai"—sekalipun fiturnya masih sederhana. Jangan pernah membiarkan proyek terjebak dalam kondisi "semuanya setengah jadi tetapi tak ada yang bisa dipakai".
:::

Cara memecah seperti ini punya dua keuntungan. Pertama, kamu selalu bisa melihat kemajuan — setiap satu langkah selesai, aplikasimu bertambah satu fitur; umpan balik positif seperti ini sangat penting untuk proyek jangka panjang (semua orang memang butuh rasa pencapaian). Kedua, setiap tugas AI menjadi cukup kecil sehingga risiko "AI salah paham" menurun — semakin kecil tugasnya, semakin akurat pemahaman AI dan semakin tinggi kualitas hasilnya.

#### 3. Template Penulisan PRD dan Praktiknya

Untuk proyek yang lebih besar (misalnya aplikasi full-stack dengan frontend, backend, dan beberapa modul fitur), Lima Elemen Kebutuhan saja mungkin belum cukup. Pada saat itu kamu perlu menulis dokumen kebutuhan proyek (PRD) yang lebih formal. Satu hal yang sering disalahpahami: PRD bukan ditulis untuk dibaca AI — ia ditulis untuk dirimu sendiri, untuk membantumu merapikan alur pikir; baru setelah itu kamu bisa memberikan instruksi yang lebih presisi kepada AI.

PRD yang baik tidak perlu panjang, tetapi harus memuat enam bagian: gambaran umum proyek (satu paragraf yang menjelaskan apa yang dibuat), daftar fitur (apa isi setiap fitur), rencana teknis (tech stack dan arsitektur kira-kira seperti apa), model data (struktur data inti), deskripsi antarmuka (seperti apa tampilan halaman-halaman utama), dan rencana pengembangan (selesai dalam beberapa tahap apa saja).

::: div .code-block
:::inline div .code-head
<span>PRD.md</span><span class="dots">···</span>
:::

```
# PRD aplikasi pencatat keuangan pribadi
## Gambaran proyek
Aplikasi pencatat keuangan pribadi yang ringan, mendukung pencatatan pemasukan/pengeluaran, kategori, rekap bulanan, dan visualisasi data.
## Daftar fitur
1. Catat pemasukan/pengeluaran: nominal, jenis (masuk/keluar), kategori, catatan, tanggal
2. Kelola kategori: sudah disiapkan makan, transportasi, belanja, hiburan, lainnya
3. Rekap bulanan: total pemasukan, pengeluaran, dan saldo per bulan
4. Visualisasi pengeluaran: diagram lingkaran menampilkan proporsi tiap kategori
5. Ekspor data: ke CSV
## Rencana teknis
- Frontend: React + TypeScript + Tailwind CSS
- Penyimpanan data: localStorage (tanpa backend)
- Grafik: pakai Chart.js
- Build: Vite
## Model data
Record {
  id: string
  amount: number
  type: 'income' | 'expense'
  category: string
  note: string
  date: string  // YYYY-MM-DD
}
## Rencana pengembangan
Step 1: fitur pencatatan dasar (CRUD)
Step 2: kelola kategori
Step 3: rekap bulanan
Step 4: visualisasi data
Step 5: ekspor data
```
:::

Perhatikan gaya penulisan PRD seperti ini: gunakan poin-poin ringkas dan format terstruktur, bukan uraian panjang lebar. Setiap fitur punya definisi yang jelas, dan model data dideskripsikan dengan tipe sederhana. PRD dengan gaya seperti ini tidak hanya mudah kamu baca sendiri; saat diberikan kepada AI, AI pun bisa memahami setiap butir kebutuhan dengan presisi.

#### 4. Praktik: Simulasi Lengkap dari Ide ke Solusi

Teori saja kurang seru; mari kita lewati seluruh proses rekayasa kebutuhan dengan satu contoh lengkap. Misalkan idemu adalah: "aku ingin membuat pelacak belajar yang bisa merekam apa saja yang aku pelajari setiap hari".

Langkah pertama, telusuri Lima Elemen Kebutuhan satu per satu.

- Who: penggunaan pribadi.
- What: alat yang bisa mencatat materi belajar setiap hari, melacak durasi belajar, dan meninjau kemajuan belajar.
- Why: ingin membangun kebiasaan belajar berkelanjutan dan melihat akumulasi hasil.
- How: buat versi web dulu, data disimpan lokal di browser.
- Constraint: pengembangan tanpa dasar pemrograman, fitur inti selesai dalam 1 minggu.

Langkah kedua, pecah kebutuhannya.

1. Langkah 1: buat fitur "catat entri belajar" (tanggal, materi, durasi);
2. Langkah 2: tambahkan "statistik durasi belajar" (hari ini, total minggu ini);
3. Langkah 3: buat tampilan "kalender belajar" (ditampilkan seperti graf kontribusi GitHub);
4. Langkah 4: tambahkan fitur "tinjauan belajar" (menampilkan catatan belajar dari suatu hari di masa lalu secara acak, untuk membantu mengulang pelajaran).

Langkah ketiga, tulis PRD singkat. Tidak perlu panjang — pemecahan di atas sendiri sudah membentuk isi utama PRD. Rapikan menjadi satu file .md, letakkan di direktori akar proyek, sebagai referensi bersama antara kamu dan AI.

Langkah keempat, mulai kembangkan langkah pertama. Instruksi untuk AI bisa seperti ini:

::: div .code-block
:::inline div .code-head
<span>Instruksi untuk AI</span><span class="dots">···</span>
:::

```
Aku butuh fitur pertama untuk pelacak belajar—mencatat sesi belajar.
Pengguna bisa menambahkan satu catatan belajar berisi tanggal, materi yang dipelajari, dan durasi (menit).
Data disimpan di localStorage.
Frontend pakai React + TypeScript.
Berikan implementasi lengkap.
```
:::

Perhatikan ciri instruksi ini: ia hanya mendeskripsikan target langkah saat ini (fitur pencatatan) tanpa mencampur fitur lain; ia memperjelas batasan teknis (React, TypeScript, localStorage); ia memberikan informasi yang cukup agar AI tahu "apa yang dibuat" dan "bagaimana kira-kira caranya", sementara implementasi detailnya diserahkan pada AI. Inilah instruksi pemrograman AI berkualitas tinggi yang telah melewati proses rekayasa kebutuhan.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Praktik Yuk: Tulis Kartu Lima Elemen untuk Proyek Favoritmu

{class="mt-1"}
Pilih satu proyek kecil yang sudah lama kamu pikirkan, luangkan 5 menit untuk mengisi satu kartu: Who / What / Why / How / Constraint, masing-masing satu kalimat. Lalu pecah menjadi 3-5 langkah yang "setiap langkahnya langsung bisa dipakai". Kamu akan menemukan: setelah idemu dituliskan, ia berubah dari "lamunan" menjadi "daftar tugas".
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan Bab Ini

- Lima Elemen Kebutuhan: Who / What / Why / How / Constraint — pikirkan dulu dengan jelas baru bicara
- Aturan emas pemecahan kebutuhan: setelah setiap langkah selesai, proyek selalu berupa "sesuatu yang bisa dipakai"
- PRD ditulis untuk dirimu sendiri: gambaran umum, daftar fitur, rencana teknis, model data, antarmuka, jadwal
- Instruksi bagus = hanya mendeskripsikan langkah saat ini + batasan yang jelas + menyebut "apa yang dibuat" tanpa "bagaimana caranya"
- Template simulasi lengkap: lima elemen → pemecahan → PRD → instruksi, empat langkah
:::
