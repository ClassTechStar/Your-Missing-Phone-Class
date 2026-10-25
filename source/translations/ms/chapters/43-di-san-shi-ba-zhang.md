---
id: di-san-shi-ba-zhang
num: 38
part: ai-biancheng-pian
nav: Bab 38: Lima Prinsip Pemikiran Pengaturcaraan AI
toc: default
kind: chapter
---

### Bab 38: Lima prinsip pemikiran pengaturcaraan AI

{class="chapter-intro mb-4"}
Jika buku ini hanya mampu membuat anda mengingati satu bab, ia mesti bab ini. Lima prinsip pemikiran ialah jantung seluruh buku; semua bab seterusnya - konteks, keperluan, dialog, kualiti - ialah pengembangan lima prinsip ini dalam pelbagai senario. Jangan risau, setiap satu tidak sukar difahami, tetapi setiap satu patut anda "tumbuhkan ke dalam otot" melalui beberapa projek.

Titik permulaan kisah ini menarik: ketika membuka sumber projeknya, Andrej Karpathy menyertakan satu fail CLAUDE.md yang hanya 70 baris, merumuskan empat prinsip teras kerjasama dengan AI. Fail ini memperoleh lebih 70,000 Star di GitHub, menjadi panduan yang paling meluas dipetik oleh pengamal pengaturcaraan AI di seluruh dunia. Empat prinsip ini bukan slogan kosong, tetapi tabiat berfikir yang boleh dilaksanakan, disuling daripada banyak amalan. Buku ini menambah prinsip kelima di atas asasnya - iterasi dan pengesahan - membentuk sistem lima prinsip yang lengkap.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mengapa fail 70 baris begitu bernilai?

{class="mt-1"}
Apakah makna 70,000 Star? Sebahagian besar projek di GitHub seumur hidupnya tidak akan capai angka itu. Satu fail teks 70 baris dapat memperolehnya, justru membuktikan satu perkara: pada era AI, yang paling langka bukan kod, tetapi kebolehan "memikirkan dengan jelas". 70 baris ini ialah versi termampat daripada "memikirkan dengan jelas".
:::

#### 1. Prinsip satu: Think Before Coding (berfikir dahulu, kemudian mengekod)

Ini prinsip yang paling melawan intuisi antara lima prinsip. Memandangkan AI boleh membantu kita menulis kod, mengapa masih perlu "berfikir dahulu"? Jawapannya mudah: kualiti hasil AI berkorelasi positif dengan kualiti input anda. Jika anda sendiri tidak jelas tentang apa yang hendak dibuat, jawapan AI hanya akan menyebabkan anda terjebak dalam kitaran "baik pulang berulang-ulang" tanpa henti - digelar "AI sesat bersama-sama dengan anda".

"Berfikir dahulu" bermaksud sebelum memberi arahan kepada AI, anda perlu menjawab tiga soalan; ketiga-tiganya membentuk satu "segi tiga pemikiran" yang tiada satu pun boleh diketepikan:

1. Masalah apa yang saya hendak selesaikan? (matlamat)
2. Bagaimana rupa hasil yang saya harapkan? (piawaian penerimaan)
3. Apakah kekangan yang perlu dipatuhi? (sempadan)

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Dimensi pemikiran</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Input kabur (buruk)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Input jelas (baik)</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Takrif masalah</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bantu saya buat satu laman web</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bantu saya buat satu laman alat peribadi yang memaparkan 3 kad pintasan masuk untuk alat kecil AI</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Hasil yang diharapkan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Nampak cantik sikit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Susun atur responsif, tema gelap, kad mempunyai animasi hover, boleh digunakan pada peranti mudah alih</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kekangan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">(Tidak dinyatakan)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tanpa rangka kerja, tulen HTML+CSS+JS, pelaksanaan satu fail, tidak perlukan backend</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Perbandingan input kabur dan input jelas bagi keperluan yang sama

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Perhatian: berfikir dahulu bukan bermakna menulis dokumen sempurna dahulu

{class="mt-1"}
"Berfikir dahulu" tidak sama dengan "tulis satu PRD yang sempurna dahulu baru bermula". Ia satu proses berfikir yang pantas tetapi tersusun - meluangkan 30 saat memikirkan tiga soalan di atas dengan jelas jauh lebih cekap daripada meluangkan 30 minit membaiki berulang kali dalam perbualan. Untuk tugas kecil, tiga soalan itu boleh jadi sangat ringkas; untuk projek besar, ia boleh dikembangkan menjadi dokumen keperluan lengkap (lihat Bab 40 untuk butiran).
:::

#### 2. Prinsip dua: Simplicity First (utamakan kesederhanaan)

Perangkap terbesar pengaturcaraan AI bukan "tidak dapat dibuat", tetapi "terlalu banyak dibuat". Apabila anda katakan kepada AI "buat satu sistem pengurusan pengguna", ia mungkin menjana satu set fungsi lengkap - pengesahan, kebenaran, peranan, log audit, eksport data dan sebagainya - sedangkan anda kini mungkin hanya perlukan satu halaman log masuk yang mudah. Penjanaan berlebihan ialah sebab utama kod AI membengkak.

"Utamakan kesederhanaan" menuntut anda mengikuti prinsip "minimum boleh laku" setiap kali memberi arahan: gunakan kod paling sedikit untuk melaksanakan fungsi teras, gunakan penyelesaian paling mudah untuk menyelesaikan masalah, gunakan fungsi paling sedikit untuk mengesahkan idea. Karpathy ada satu perumpamaan yang tajam: "Jika anda perlu mengira satu harga diskaun, anda tidak memerlukan enjin e-dagang."

Dalam amalan, "utamakan kesederhanaan" bermaksud beberapa tabiat operasi yang konkrit:

- Setiap kali hanya biarkan AI melaksanakan satu titik fungsi, bukannya menerangkan keseluruhan sistem sekali gus;
- Utamakan pustaka standard dan penyelesaian mudah, bukannya memperkenalkan kebergantungan yang rumit;
- Masalah yang boleh diselesaikan dengan 50 baris kod, jangan biarkan AI menulis 500 baris;
- Apabila hasil AI melampaui jangkaan, beranilah memberitahunya "potong bahagian yang berlebihan".

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Senario</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Penyelesaian berlebihan (elakkan)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Penyelesaian mudah (disyorkan)</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Perlu menyimpan data</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Membina pangkalan data MySQL + ORM</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Guna fail JSON atau SQLite dahulu</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Perlu log masuk pengguna</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OAuth2.0 + JWT + kebenaran peranan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Buat pengesahan kata laluan mudah dahulu</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Perlu rangka kerja frontend</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">React + Redux + Router</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cuba HTML tulen + JS natif dahulu</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Perlu pelaksanaan ke atas talian</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Docker + CI/CD + K8s</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pastikan berjalan di tempatan dahulu</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Perbandingan penyelesaian berlebihan dan penyelesaian mudah bagi senario biasa

#### 3. Prinsip tiga: Surgical Changes (pindaan yang tepat)

Apabila anda mengiterasi satu projek sedia ada, setiap pindaan patut tepat seperti pembedahan - hanya sentuh bahagian yang patut disentuh, jangan ganggu yang tidak patut. Perkara ini amat penting dalam pengaturcaraan AI, kerana AI ada kecenderungan "sambil lewa membaikit sedikit": anda menyuruhnya membaiki satu bug, ia mungkin sambil itu merestrukturkan separuh fail.

Tuntutan teras "pindaan yang tepat" ialah: setiap arahan kepada AI mesti menyatakan dengan jelas skop dan sempadan pindaan. Beritahunya "hanya pinda fungsi calculate_discount" "jangan sentuh bahagian lain" "kekalkan gaya kod sedia ada". Apabila pindaan AI melampaui skop yang anda minta, minta segera ia mengembalikan bahagian berlebihan.

Karpathy menjelaskan perkara ini dengan satu contoh diff (perbandingan perbezaan). Katakan anda meminta AI menambah logik "harga ahli" pada fungsi pengiraan diskaun troli beli-belah: hasil yang baik ialah hanya meminda fungsi itu dan menambah beberapa baris kod; hasil yang buruk ialah merestrukturkan keseluruhan fail - walaupun kod baharu mungkin lebih "anggun", anda tidak dapat pasti sama ada ia memperkenalkan bug baharu. Dalam pengaturcaraan AI, "nampak lebih baik" tidak pernah boleh menjadi alasan untuk menyeleweng daripada arahan.

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
Arahan kurang baik (skop kabur)

{class="font-mono text-xs leading-relaxed"}
Bantu saya optimumkan logik pengiraan diskaun projek ini
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
Arahan yang baik (skop dinyatakan dengan tepat)

{class="font-mono text-xs leading-relaxed"}
Hanya pinda fungsi calculate_discount dalam cart.py: 1. Tambahkan logik harga ahli di atas diskaun sedia ada 2. Pengguna ahli menikmati diskaun tambahan 10% 3. Jangan pinda tandatangan fungsi dan fungsi lain 4. Kekalkan gaya penamaan pemboleh ubah sedia ada
:::
:::

#### 4. Prinsip empat: Goal-Driven Execution (pelaksanaan didorong matlamat)

Prinsip ini menjawab satu soalan utama: patutkah anda memberi AI arahan "bagaimana melakukannya" atau arahan "apa yang perlu dilakukan"? Jawapan Karpathy ialah yang kedua. Daripada memberitahu AI "cipta satu kelas dahulu, kemudian tambah kaedah, kemudian tulis ujian", lebih baik beritahunya "saya perlukan satu alat yang boleh menghurai fail CSV dan mengira bilangan nilai unik setiap lajur". Biarkan AI menentukan sendiri laluan pelaksanaan, dan anda bertanggungjawab menerima hasilnya.

Kebaikan "didorong matlamat" adalah dua hala. Bagi AI, ia mendapat ruang autonomi lebih besar, boleh memilih laluan pelaksanaan paling optimum, bukannya terikat dengan langkah pertengahan anda; bagi anda, anda mengalihkan perhatian daripada "bagaimana melakukannya" kepada "betulkah hasilnya" - inilah yang patut dilakukan oleh konduktor.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Perhatian: didorong matlamat bukan bermakna membiarkan begitu sahaja

{class="mt-1"}
Ia memerlukan anda melakukan penerimaan hasil yang ketat selepas AI melaksanakan: adakah hasil memenuhi keperluan? Adakah kes sempadan telah dikendalikan? Adakah terdapat reka bentuk berlebihan yang ketara? Jika hasil tidak memenuhi jangkaan, berikan maklum balas yang konkrit - bukan "tulis semula", tetapi "masalah di sini ialah input senarai kosong akan melaporkan IndexError, sila pinda dengan menambah semakan nilai kosong".
:::

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Gaya arahan</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Contoh</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ciri hasil</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Arahan memerintah (bagaimana melakukannya)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"Cipta dahulu satu kelas Python bernama DataParser, tambah satu kaedah parse yang menerima parameter filename, gunakan modul csv untuk membaca..."</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AI bertukar menjadi jurutaip, langkah pertengahan anda mungkin bukan laluan paling optimum</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gaya matlamat (apa yang dilakukan)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"Saya perlukan satu alat: baca fail CSV, kira bilangan nilai unik setiap lajur, output dalam format JSON. Sila berikan pelaksanaan lengkap."</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AI memilih sendiri laluan paling optimum, anda bertanggungjawab menerima hasil</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Perbandingan arahan memerintah dan arahan gaya matlamat

#### 5. Prinsip lima: Iterate and Verify (iterasi dan pengesahan)

Ini prinsip kelima yang ditambah oleh buku ini di atas empat prinsip Karpathy. Kepercayaan terasnya ialah: hasil pertama AI hampir selalu bukan versi akhir. Pengaturcaraan AI yang berkesan ialah satu kitaran iteratif "jana-sahkan-baiki", bukan sekali "arahan-hasil".

"Iterasi dan pengesahan" bukan "cuba lagi kalau salah" secara pasif, tetapi satu proses pengesahan yang berstruktur. Setiap kali AI memberikan hasil, sahkan mengikut tiga peringkat:

- Peringkat satu - pengesahan fungsi: bolehkah ia berjalan? Betulkah input dan output?
- Peringkat dua - pengesahan sempadan: apa berlaku dengan input kosong, input terlalu panjang, input luar biasa?
- Peringkat tiga - pengesahan seni bina: adakah struktur kod munasabah? Adakah ada hardcode? Adakah mudah untuk pengembangan seterusnya?

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-bullseye mr-1"></i> Takrifkan matlamat</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-robot mr-1"></i> AI menjana kod</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> Pengesahan fungsi</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> Lulus</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> Pengesahan sempadan</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> Lulus</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-landmark mr-1"></i> Semakan seni bina</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-check-circle mr-1"></i> Lulus, teruskan ke langkah seterusnya</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-red-500 bg-red-50 text-red-900 dark:bg-red-950 dark:text-red-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-times-circle mr-1"></i> Tidak lulus</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> Berikan maklum balas khusus</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> Jana semula</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Rajah 2: Kitaran iterasi dan pengesahan pengaturcaraan AI
:::

Kunci kitaran ini terletak pada langkah "memberi maklum balas konkrit". Apabila pengesahan gagal, jangan katakan "salah, buat semula", sebaliknya katakan "fungsi melaporkan IndexError apabila input senarai kosong, sila tambah semakan nilai kosong pada baris 15". Maklum balas konkrit membolehkan AI membaiki dengan tepat; maklum balas kabur hanya menyebabkannya meneka semula niat anda.

#### 6. Harness Engineering: Agent = Model + Harness

Menjelang pertengahan 2026, satu konsep bernama Harness Engineering mula popular dalam komuniti pengaturcaraan AI. Rumus terasnya sangat mudah:

:::inline div .quote-line .text-center .text-base .font-bold
<strong>Keupayaan Agent = keupayaan model × kualiti Harness</strong>
:::

Keupayaan model ialah had kecerdasan otak AI; Harness ialah "persekitaran kerja" yang dibina mengelilingi model - merangkumi pengurusan konteks, integrasi alat, orkestrasi aliran kerja, sistem ingatan dan sebagainya.

Konsep ini menjelaskan satu kekeliruan yang biasa: mengapa dengan GPT-4 atau Claude yang sama, ada orang dapat menghasilkan projek yang mengagumkan, ada yang hanya memperoleh kod biasa-biasa? Bezanya bukan pada model, tetapi pada Harness. Harness yang baik merangkumi: fail spesifikasi projek yang jelas, integrasi alat yang munasabah, konteks perbualan yang tersusun, dan proses pengesahan yang lengkap. Model menentukan had kecerdasan, manakala Harness menentukan sejauh mana anda dapat memanfaatkan had itu.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Perumpamaan pelatih cemerlang

{class="mt-1"}
Bayangkan model sebagai seorang pelatih yang sangat pintar - IQ tinggi, tetapi jika anda tidak memberinya dokumen latar projek, tidak memberitahunya alat mana yang digunakan, tidak menetapkan tarikh akhir dan piawaian penerimaan, dia juga tidak dapat menghasilkan kerja yang baik. Harness Engineering ialah kejuruteraan "bagaimana membina persekitaran kerja yang baik untuk pelatih pintar itu".
:::

Bab-bab seterusnya dalam buku ini, pada hakikatnya semuanya mengajar anda bagaimana membina Harness yang baik: Bab 39 mengajar anda mengurus konteks (sistem ingatan projek), Bab 40 mengajar anda menakrifkan keperluan (PRD), Bab 43 mengajar anda teknik dialog (pelapisan Prompt), Bab 45 mengajar anda jaminan kualiti (proses pengesahan). Gabungan semuanya itulah Harness anda.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mari praktik: huraikan idea seterusnya anda dengan "segi tiga pemikiran"

{class="mt-1"}
Pilih satu benda kecil yang anda sentiasa mahu buat tetapi belum mula (contohnya satu laman web kira hari unduran, satu skrip peringatan minum air). Luangkan 3 minit untuk menjawab: (1) Masalah apa yang ia selesaikan? (2) Bagaimana rupanya apabila siap? (3) Apakah kekangannya (masa, teknologi, persekitaran)? Kemudian tulis jawapan itu menjadi satu perenggan. Tahniah, anda telah menyiapkan "Think Before Coding" pertama dalam hidup anda - perenggan itu sendiri ialah satu arahan berkualiti tinggi yang memenuhi syarat.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan bab ini

- Lima prinsip berpunca daripada CLAUDE.md 70 baris Karpathy (70K+ Star); buku ini menambah prinsip kelima "iterasi dan pengesahan"
- Think Before Coding: jawab tiga soalan sebelum bercakap - apa yang dibuat? Bagaimana rupanya hasilnya? Apakah kekangannya?
- Simplicity First: perangkap terbesar AI ialah "terlalu banyak dibuat" - mengira diskaun tidak perlukan enjin e-dagang
- Surgical Changes: pinda dengan tepat seperti pembedahan, tolak "sambil lewa membaikit" ala AI
- Goal-Driven Execution: katakan "apa yang dilakukan", bukan "bagaimana melakukannya", biarkan AI memilih laluan sendiri
- Iterate and Verify: pengesahan tiga peringkat (fungsi/sempadan/seni bina) + maklum balas konkrit, iterasi berterusan
- Harness Engineering: kebolehan = model x Harness, layani AI sebagai "pelatih pintar" dengan mengurus persekitarannya
:::
