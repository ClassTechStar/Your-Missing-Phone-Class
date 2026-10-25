---
id: di-san-shi-ba-zhang
num: 38
part: ai-biancheng-pian
nav: Bab 38: Lima Prinsip Berpikir Pemrograman AI
toc: default
kind: chapter
---

### Bab 38: Lima Prinsip Berpikir Pemrograman AI

{class="chapter-intro mb-4"}
Jika buku ini hanya bisa membuat Anda mengingat satu bab, haruslah bab ini. Lima prinsip berpikir adalah jantung seluruh buku—semua bab berikutnya (konteks, kebutuhan, percakapan, kualitas) adalah pengembangan lima prinsip ini di berbagai skenario. Tenang, masing-masing tidak sulit dipahami—tetapi masing-masing layak Anda "tanamkan ke otot" lewat beberapa proyek.

Awal ceritanya menarik: saat Andrej Karpathy membuka proyeknya, ia menyertakan file CLAUDE.md hanya 70 baris yang merangkum empat prinsip inti bekerja sama dengan AI. File ini mendapatkan lebih dari 70.000 Star di GitHub, menjadi pedoman yang paling luas dikutip praktisi pemrograman AI di seluruh dunia. Empat prinsip ini bukan slogan kosong, melainkan kebiasaan berpikir yang bisa dijalankan, disaring dari praktik yang melimpah. Buku ini menambahkan prinsip kelima di atas fondasi itu—iterasi verifikasi—sehingga menjadi sistem lima prinsip yang lengkap.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mengapa file 70 baris begitu berharga?

{class="mt-1"}
70.000 Star itu apa artinya? Mayoritas proyek di GitHub tidak akan pernah mencapai angka itu seumur hidup. Sebuah file teks 70 baris bisa mendapatkannya—justru membuktikan satu hal: di era AI, yang paling langka bukan kode, melainkan kemampuan "berpikir jernih". 70 baris itu adalah versi pekat dari "berpikir jernih".
:::

#### 1. Prinsip satu: Think Before Coding (pikirkan dulu, baru menulis kode)

Ini prinsip yang paling kontra-intuitif di antara kelima. Kalau AI bisa membantu menulis kode, mengapa masih perlu "berpikir dulu"? Jawabannya sederhana: kualitas keluaran AI berkorelasi positif dengan kualitas masukan Anda. Kalau Anda sendiri belum jelas mau mengerjakan apa, jawaban AI hanya akan membuat Anda terjebak siklus "revisi terus-menerus"—yang populer disebut "AI ikut tersesat bersamamu".

"Berpikir dulu" berarti sebelum memberi instruksi kepada AI, Anda perlu menjawab tiga pertanyaan yang membentuk "segitiga berpikir" yang tidak boleh kurang satu pun:

1. Masalah apa yang saya selesaikan? (tujuan)
2. Seperti apa hasil yang saya harapkan? (standar verifikasi)
3. Batasan apa yang harus dipatuhi? (batasan)

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Dimensi berpikir</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Masukan tidak jelas (buruk)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Masukan jelas (baik)</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Definisi masalah</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bantu saya buat website</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bantu saya buat situs alat pribadi yang menampilkan 3 kartu pintasan ke alat AI</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Hasil yang diharapkan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Agak baguslah</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tata letak responsif, tema gelap, kartu punya animasi hover, bisa dipakai di ponsel</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Batasan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">(tidak disebutkan)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tanpa kerangka kerja, murni HTML+CSS+JS, deploy satu file, tidak perlu backend</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Perbandingan masukan tidak jelas dan masukan jelas untuk kebutuhan yang sama

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Catatan: berpikir dulu ≠ menulis dokumen sempurna dulu

{class="mt-1"}
"Berpikir dulu" tidak sama dengan "menulis PRD sempurna sebelum mulai". Ini proses berpikir yang cepat tetapi teratur—meluangkan 30 detik memikirkan tiga pertanyaan di atas jauh lebih efisien daripada menghabiskan 30 menit bolak-balik merevisi di percakapan. Untuk tugas kecil, tiga pertanyaan bisa sangat singkat; untuk proyek besar, kembangkan menjadi dokumen kebutuhan lengkap (lihat Bab 40).
:::

#### 2. Prinsip dua: Simplicity First (kesederhanaan di atas segalanya)

Jebakan terbesar pemrograman AI bukan "tidak bisa jadi", melainnam "terlalu banyak dikerjakan". Saat Anda berkata kepada AI "buat sistem manajemen pengguna", ia mungkin menghasilkan autentikasi, izin, peran, log audit, ekspor data—seperangkat fitur lengkap—padahal Anda mungkin hanya butuh halaman login sederhana. Over-generation adalah penyebab utama kode AI membengkak.

"Kesederhanaan di atas segalanya" menuntut Anda mengikuti prinsip "minimum viable" setiap kali memberi instruksi: wujudkan fungsi inti dengan kode sesedikit mungkin, selesaikan masalah dengan solusi paling sederhana, validasi gagasan dengan fitur paling minim. Karpathy punya peribahasa yang tajam: "Kalau Anda hanya perlu menghitung harga diskon, Anda tidak butuh mesin e-commerce."

Dalam praktiknya, "kesederhanaan di atas segalanya" berarti beberapa kebiasaan operasional konkret:

- Setiap kali hanya minta AI mewujudkan satu titik fungsi, bukan mendeskripsikan seluruh sistem sekaligus;
- Utamakan pustaka standar dan solusi sederhana, daripada memperkenalkan dependensi rumit;
- Masalah yang bisa diselesaikan dengan 50 baris kode, jangan biarkan AI menulis 500 baris;
- Saat keluaran AI melebihi lingkup yang diharapkan, beranilah berkata "potong bagian yang tidak perlu".

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Skenario</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Solusi berlebihan (hindari)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Solusi sederhana (disarankan)</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Perlu menyimpan data</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bangun basis data MySQL + ORM</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mulai dengan file JSON atau SQLite</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Perlu login pengguna</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OAuth2.0 + JWT + izin peran</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mulai dengan verifikasi kata sandi sederhana</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Perlu kerangka kerja frontend</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">React + Redux + Router</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Coba dulu HTML murni + JS bawaan</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Perlu deploy online</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Docker + CI/CD + K8s</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Jalan dulu secara lokal</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Perbandingan solusi berlebihan dan solusi sederhana untuk skenario umum

#### 3. Prinsip tiga: Surgical Changes (perubahan presisi)

Saat mengiterasi proyek yang sudah ada, setiap perubahan harus sepresisi bedah—hanya menyentuh yang perlu disentuh, tidak mengganggu yang tidak perlu. Ini terutama penting dalam pemrograman AI, karena AI punya kecenderungan "sekalian saya rapikan": Anda memintanya memperbaiki satu bug, ia mungkin ikut me-refactor separuh file.

Tuntutan inti "perubahan presisi" adalah: setiap instruksi kepada AI harus menetapkan lingkup dan batasan perubahan secara eksplisit. Katakan "hanya ubah fungsi calculate_discount" "jangan sentuh bagian lain" "pertahankan gaya kode yang ada". Saat perubahan AI melebihi lingkup yang Anda minta, segera minta ia mengembalikan bagian yang berlebihan.

Karpathy menjelaskan hal ini dengan contoh diff (perbandingan perbedaan). Misalkan Anda meminta AI menambahkan logika "harga member" pada fungsi hitung diskon keranjang belanja: keluaran yang baik hanya mengubah satu fungsi itu dan menambah beberapa baris kode; keluaran yang buruk me-refactor seluruh file—meski kode baru mungkin lebih "elegan", Anda tidak bisa memastikan ia tidak memperkenalkan bug baru. Dalam pemrograman AI, "tampak lebih baik" tidak pernah bisa menjadi alasan menyimpang dari instruksi.

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
Instruksi buruk (lingkup kabur)

{class="font-mono text-xs leading-relaxed"}
Bantu saya optimalkan logika hitung diskon proyek ini
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
Instruksi baik (lingkup ditetapkan presisi)

{class="font-mono text-xs leading-relaxed"}
Hanya ubah fungsi calculate_discount di cart.py: 1. Tambahkan logika harga member di atas diskon yang ada 2. Pengguna member mendapat diskon tambahan 10% 3. Jangan ubah tanda tangan fungsi dan fungsi lainnya 4. Pertahankan gaya penamaan variabel yang ada
:::
:::

#### 4. Prinsip empat: Goal-Driven Execution (eksekusi berbasis tujuan)

Prinsip ini menjawab pertanyaan kunci: sebaiknya Anda memberi AI instruksi "bagaimana cara" atau "apa yang harus dilakukan"? Jawaban Karpathy adalah yang kedua. Daripada memberi tahu AI "buat dulu sebuah kelas, lalu tambahkan metode, lalu tulis tes", lebih baik katakan "saya butuh alat yang bisa membaca file CSV dan menghitung jumlah nilai unik tiap kolom". Biarkan AI menentukan sendiri jalur implementasinya—Anda bertugas memverifikasi hasilnya.

Manfaat "berbasis tujuan" bersifat ganda. Bagi AI, ia mendapat ruang otonomi lebih luas—bisa memilih jalur implementasi terbaik, tidak terikat langkah antara Anda; bagi Anda, perhatian bergeser dari "bagaimana cara" ke "apakah hasilnya benar"—memang itulah tugas seorang komandan.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Catatan: berbasis tujuan ≠ membiarkan begitu saja

{class="mt-1"}
Prinsip ini menuntut Anda melakukan verifikasi ketat setelah AI mengeksekusi: apakah hasilnya memenuhi kebutuhan? Apakah kasus tepi sudah ditangani? Apakah ada over-engineering yang mencolok? Jika hasil tidak sesuai harapan, berikan umpan balik spesifik—bukan "tulis ulang", melainkan "masalahnya di sini: input daftar kosong memunculkan IndexError—tolong tambahkan pengecekan nilai kosong".
:::

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Gaya instruksi</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Contoh</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ciri hasil</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Imperatif (bagaimana cara)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"Buat dulu kelas Python bernama DataParser, tambahkan metode parse yang menerima parameter filename, baca dengan modul csv…"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AI berubah jadi juru ketik—langkah antara Anda belum tentu jalur terbaik</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Berbasis tujuan (apa yang dilakukan)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"Saya butuh alat: membaca file CSV, menghitung jumlah nilai unik tiap kolom, mengeluarkan dalam format JSON. Berikan implementasi lengkapnya."</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AI memilih sendiri jalur terbaik—Anda bertugas memverifikasi hasil</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Perbandingan instruksi imperatif dan instruksi berbasis tujuan

#### 5. Prinsip lima: Iterate and Verify (iterasi verifikasi)

Ini prinsip kelima yang ditambahkan buku ini di atas empat prinsip Karpathy. Keyakinan intinya: keluaran pertama AI hampir tidak pernah versi final. Pemrograman AI yang efektif adalah siklus iteratif "hasilkan–verifikasi–perbaiki", bukan sekali jalan "instruksi–keluaran".

"Iterasi verifikasi" bukan pasif "salah ya coba lagi", melainkan alur verifikasi yang terstruktur. Setiap kali AI memberi keluaran, verifikasi pada tiga tingkat:

- Tingkat 1 · Verifikasi fungsional: bisakah dijalankan? Input-output sudah benar?
- Tingkat 2 · Verifikasi tepi: input kosong, input terlalu panjang, input tidak wajar—bagaimana hasilnya?
- Tingkat 3 · Verifikasi arsitektur: struktur kode sudah masuk akal? Ada hard coding? Mudah dikembangkan nanti?

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-bullseye mr-1"></i> Tetapkan tujuan</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-robot mr-1"></i> AI membuat kode</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> Verifikasi fungsi</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> Lulus</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> Verifikasi batasan</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> Lulus</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-landmark mr-1"></i> Review arsitektur</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> Lulus, lanjut ke langkah berikutnya</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-times-circle mr-1"></i> Tidak lulus</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> Beri umpan balik konkret</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> Buat ulang</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Gambar 2: Siklus iterasi verifikasi pemrograman AI
:::

Kunci siklus ini ada pada langkah "memberi umpan balik spesifik". Saat verifikasi gagal, jangan berkata "salah, ulangi", tetapi "fungsi memunculkan IndexError saat input daftar kosong—tolong tambahkan pengecekan nilai kosong di baris 15". Umpan balik spesifik membuat AI bisa memperbaiki dengan tepat; umpan balik kabur hanya membuatnya menebak-nebak maksud Anda lagi.

#### 6. Harness Engineering: Agent = Model + Harness

Pada pertengahan 2026, konsep bernama Harness Engineering mulai populer di komunitas pemrograman AI. Rumus intinya sederhana:

:::inline div .quote-line .text-center .text-base .font-bold
<strong>Kemampuan Agent = kemampuan model × kualitas Harness</strong>
:::

Kemampuan model adalah batas kecerdasan otak AI; Harness adalah "lingkungan kerja" yang dibangun di sekitar model—termasuk manajemen konteks, integrasi alat, orkestrasi alur, sistem memori, dan lainnya.

Konsep ini menjelaskan kebingungan yang umum: mengapa dengan GPT-4 atau Claude yang sama, sebagian orang bisa membuat proyek memukau, sementara yang lain hanya mendapat kode biasa saja? Bedanya bukan di model, melainkan di Harness. Harness yang baik mencakup: file spesifikasi proyek yang jelas, integrasi alat yang wajar, konteks percakapan yang teratur, alur verifikasi yang matang. Model menentukan batas kecerdasan—Harness menentukan sejauh mana Anda bisa memanfaatkan batas itu.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Peribahasa magang jenius

{class="mt-1"}
Bayangkan model sebagai magang jenius—IQ sangat tinggi, tetapi kalau tidak diberi dokumen latar belakang proyek, tidak diberi tahu alat apa yang dipakai, tidak diberi tenggat dan standar verifikasi—ia juga tidak akan menghasilkan karya bagus. Harness Engineering adalah rekayasa "bagaimana membangun lingkungan kerja yang baik untuk magang jenius".
:::

Bab-bab berikutnya pada dasarnya mengajarkan cara membangun Harness yang baik: Bab 39 mengajarkan manajemen konteks (sistem memori proyek), Bab 40 mengajarkan definisi kebutuhan (PRD), Bab 43 mengajarkan teknik percakapan (berlapis Prompt), Bab 45 mengajarkan penjaminan kualitas (alur verifikasi). Kombinasi semuanya itulah Harness Anda.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Ayo praktik: bedah ide Anda berikutnya dengan "segitiga berpikir"

{class="mt-1"}
Pilih satu hal kecil yang selalu ingin Anda buat tetapi tidak pernah mulai (misalnya halaman hitung mundur, skrip pengingat minum air). Luangkan 3 menit menjawab: ① Masalah apa yang diselesaikannya? ② Seperti apa hasilnya? ③ Batasan apa yang ada (waktu, teknologi, lingkungan)? Lalu tulis jawabannya dalam satu paragraf. Selamat—Anda baru saja menyelesaikan "Think Before Coding" pertama dalam hidup Anda. Paragraf itu adalah instruksi berkualitas yang memenuhi syarat.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan bab ini

- Lima prinsip berasal dari CLAUDE.md 70 baris Karpathy (70K+ Star); buku ini menambahkan prinsip kelima "iterasi verifikasi"
- Think Before Coding: sebelum bicara, jawab tiga pertanyaan—mengerjakan apa? Seperti apa hasilnya? Apa batasannya?
- Simplicity First: jebakan terbesar AI adalah "terlalu banyak dikerjakan"—menghitung diskon tidak butuh mesin e-commerce
- Surgical Changes: ubah sepresisi bedah—tolak kecenderungan AI "sekalian saya rapikan"
- Goal-Driven Execution: katakan "apa yang dilakukan", bukan "bagaimana cara"—biarkan AI memilih jalurnya sendiri
- Iterate and Verify: tiga tingkat verifikasi (fungsional/tepi/arsitektur) + umpan balik spesifik, iterasi berkelanjutan
- Harness Engineering: kemampuan = Model × Harness—perlakukan AI sebagai "magang jenius" yang lingkungan kerjanya Anda atur
:::
