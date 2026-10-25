---
id: di-si-shi-er-zhang
num: 42
part: ai-biancheng-pian
nav: Bab 42: Panorama Model Besar dan Praktik API
toc: default
kind: chapter
---

### Bab 42: Panorama Model Besar dan Praktik API

{class="chapter-intro mb-4"}
Beberapa bab sebelumnya membahas "cara berkolaborasi dengan AI"; bab ini menjawab pertanyaan yang lebih mendasar: "AI mana yang dipakai? Bagaimana memakainya?" Lanskap model besar per Agustus 2026 sudah sangat kaya — di ranah internasional GPT, Claude, dan Gemini bersaing sebagai tiga raksasa; di Tiongkok DeepSeek, Tongyi Qianwen, GLM, Kimi, dan Doubao bermekaran. Setiap model punya karakter dan keahlian khasnya masing-masing: memilih yang tepat membuat pekerjaan jauh lebih efisien, memilih yang salah membuat pekerjaan terasa dua kali berat. Bab ini tidak hanya memperkenalkan model-model tersebut, tetapi juga mengajarkan cara menghubungkannya ke aplikasimu melalui API, serta cara memilih Token Plan (paket kuota) yang sesuai dengan kebutuhanmu.

#### 1. Model Besar Internasional Utama: Format Tiga Raksasa

Pasar model besar internasional per Agustus 2026 membentuk format tiga raksasa: OpenAI (seri GPT), Anthropic (seri Claude), dan Google (seri Gemini). Masing-masing punya karakter khas yang menonjol — mari kita kenali satu per satu.

##### 1. Seri OpenAI GPT-5.6: Jagoan Serba Bisa yang Seimbang

OpenAI adalah pembuka gelombang model besar, dan seri GPT hingga kini tetap menjadi model yang paling banyak digunakan di dunia. Seri GPT-5.6 yang dirilis Juli 2026 memakai strategi tiga segmen: varian flagship GPT-5.6 Sol untuk kebutuhan reasoning kelas atas, varian seimbang GPT-5.6 Terra untuk pengembangan harian, dan varian ringan GPT-5.6 Luna untuk skenario konkurensi tinggi dengan biaya rendah. Ketiga model berbagi jendela konteks 1,05 juta Token, dan semuanya mendukung input gambar, function calling, serta output terstruktur.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Model</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Segmen</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Input (per juta Token)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Output (per juta Token)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Jendela Konteks</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GPT-5.6 Sol</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Flagship reasoning</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$5,00 (≈36 yuan)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$30,00 (≈217 yuan)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1,05 juta Token</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GPT-5.6 Terra</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Seimbang untuk harian</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$2,50 (≈18 yuan)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$15,00 (≈109 yuan)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1,05 juta Token</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GPT-5.6 Luna</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ringan, biaya rendah</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$1,00 (≈7 yuan)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$6,00 (≈44 yuan)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1,05 juta Token</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Harga seri OpenAI GPT-5.6 (Agustus 2026)

Keunggulan inti seri GPT ada pada "keseimbangan" — reasoning, pemrograman, penulisan, multimodal, tidak ada kelemahan yang mencolok. Ditambah ekosistem plugin dan komunitas pengembang OpenAI yang sangat besar, dokumentasi adaptasi dan toolchain-nya paling lengkap. Untuk skenario "bingung mau pilih apa", GPT adalah jawaban default yang "dipilih sambil memejamkan mata pun tidak akan salah". Namun kelemahannya: akses dari Tiongkok membutuhkan jaringan khusus, ungkapan bahasa Tionghoanya kadang terasa "berbau terjemahan", dan harga API-nya berada di level menengah ke atas.

::: div .success-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Kabar Baik

{class="mt-1"}
Pada Agustus 2026 OpenAI mengumumkan bahwa model default pengguna gratis dinaikkan menjadi GPT-5.6 Luna dan membuka obrolan teks tanpa batas. Artinya, kamu bisa merasakan kemampuan dasar GPT tanpa biaya, dan hanya perlu membayar saat butuh reasoning yang lebih kuat atau pemanggilan API.
:::

##### 2. Seri Anthropic Claude: Puncak Pemrograman dan Ketelitian

Kalau GPT adalah pemain serba bisa, maka Claude adalah "puncaknya" bidang pemrograman. Seri Claude dari Anthropic secara konsisten memimpin dengan selisih jauh di SWE-bench (benchmark rekayasa perangkat lunak), dengan kualitas pembuatan kode dan kemampuan mewujudkan proyek tingkat engineering terbaik di industrinya. Lebih istimewa lagi, tingkat halusinasi Claude (probabilitas menghasilkan informasi palsu) adalah yang terendah di antara semua model, hanya sekitar 1% — menjadikannya sangat cocok untuk skenario berpresisi tinggi seperti akademik dan hukum.

Jurus andalan Claude yang lain adalah konteks super panjang: mendukung jendela konteks 1 juta Token, mampu "membaca habis" kontrak setebal ratusan halaman atau satu basis kode penuh dalam sekali jalan tanpa kelewat satu pun detailnya. Hal ini nyaris tak tergantikan untuk skenario seperti refaktorasi kode dan analisis dokumen panjang. Claude Code sebagai alat pemrograman AI terminal telah mencapai pendapatan tahunan 2,5 miliar dolar AS per pertengahan 2026 — bukti paling kuat bahwa kemampuan pemrograman Claude paling diakui.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Model</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Segmen</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Input (per juta Token)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Output (per juta Token)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Jendela Konteks</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Fable 5</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Varian flagship</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$10,00 (≈72 yuan)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$50,00 (≈362 yuan)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1 juta Token</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Opus 4.8</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Varian profesional</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$5,00 (≈36 yuan)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$25,00 (≈181 yuan)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1 juta Token</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Sonnet 5</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Varian hemat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$2,00 (≈14 yuan)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$10,00 (≈72 yuan)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1 juta Token</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Harga seri Anthropic Claude (Agustus 2026; Sonnet 5 dengan harga promo)

Kelemahan Claude ada pada harga — harga output Fable 5 adalah yang termahal di antara semua model, 50 dolar AS per juta Token. Kemampuan multimodalnya (pemahaman gambar dan video) juga relatif lemah. Bagi pengembang individu dengan anggaran terbatas, Sonnet 5 selama periode promo menawarkan value yang sangat menonjol.

##### 3. Seri Google Gemini: Raja Multimodal

Seri Gemini dari Google pada 2026 telah beriterasi hingga versi 3.1 Pro. Jurus andalan terbesar Gemini adalah multimodal native — analisis teks dan gambar yang presisi, pengenalan tabel OCR tanpa kesalahan, ekstraksi frame video yang efisien, ditambah dukungan analisis mendalam untuk audio dan video. Ia terikat erat dengan ekosistem Google (pencarian, surel, layanan cloud) dan menonjol dalam pencarian informasi real-time serta pemahaman lintas modal. Gemini juga mendukung input konteks super panjang hingga 2 juta Token, menjadikannya model dengan jendela konteks terbesar saat ini.

Gemini diposisikan sebagai "pilihan utama untuk reasoning ilmiah dan skenario multimodal". Kalau proyekmu melibatkan analisis gambar dalam jumlah besar, pemahaman video, atau komputasi ilmiah, Gemini nyaris tanpa lawan. Namun dalam pembuatan kode murni teks ia sedikit kalah dari Claude, dan ungkapan bahasa Tionghoanya tidak senatural model buatan Tiongkok.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Aspek</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">GPT-5.6</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Claude Fable 5</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Gemini 3.1 Pro</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Skor Keseluruhan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">94.8</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">95.0</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">92.1</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kemampuan Pemrograman (SWE-bench)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">74.9%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">64.3% (Pro)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sedang</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Jendela Konteks</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1,05 juta Token</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1 juta Token</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2 juta Token</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kemampuan Multimodal</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Seimbang</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Relatif lemah</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Terkuat</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tingkat Halusinasi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Relatif rendah</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Terendah (sekitar 1%)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Relatif rendah</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Aksesibilitas di Tiongkok</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Perlu jaringan khusus</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Perlu jaringan khusus</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Perlu jaringan khusus</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ekosistem API</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Paling lengkap</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sedang berkembang</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Terikat ekosistem Google</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Perbandingan horizontal tiga model internasional (Agustus 2026)

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Catatan: Hambatan Nyata Penggunaan di Tiongkok

{class="mt-1"}
Bagi pengembang di Tiongkok, hambatan utama GPT, Claude, dan Gemini adalah akses jaringan. Meski bisa digunakan secara tidak langsung lewat proxy Azure, platform agregator API, dan cara-cara lain, stabilitas dan kepatuhan regulasinya perlu kamu nilai sendiri. Jika proyekmu menuntut keamanan data yang ketat, sebaiknya prioritaskan model buatan Tiongkok.
:::

#### 2. Model Besar Utama Buatan Tiongkok: Bermekaran

Model besar buatan Tiongkok tahun 2026 sudah berubah dari "pengejar" menjadi "penanding", bahkan "pemimpin" di beberapa bidang. Berbeda dengan kontroversi "ganti kulit" (membungkus model luar negeri) tahun 2023, model flagship buatan Tiongkok 2026 dalam hal reasoning logis, pembuatan kode, dan pemahaman bahasa Tionghoa telah setara dengan model internasional kelas atas, dengan selisih yang menyusut hingga di bawah 5%. Lebih penting lagi, model buatan Tiongkok punya keunggulan yang tak tergantikan pada skenario bahasa Tionghoa, biaya, dan deployment yang sesuai regulasi.

##### 1. DeepSeek V4: Raja Value

DeepSeek adalah fenomena di antara model besar buatan Tiongkok. Awal 2025, DeepSeek-V3 mengguncang pasar dengan posisi "seperssepuluh harga GPT tetapi kemampuan setara", dan oleh kalangan industri dijuluki "garis penentu model AI umum" — yang lebih murah tak sebagus ia, yang lebih mahal tak sekelimpahan ia. Per Agustus 2026, versi resmi DeepSeek V4-Pro dirilis: arsitektur MoE dengan 1,6 triliun parameter, sekitar 49B di antaranya aktif, mendukung konteks 1 juta tanpa kehilangan informasi, dan value-nya untuk kode secara luas dianggap puncak dunia.

DeepSeek V4 melompat jauh dalam kemampuan Agent — benchmark DeepSWE melonjak dari 12,8 ke 62,7 (+390%), dan NL2Repo naik dari 38,5 ke 61,5. API-nya kini menambahkan dukungan dua protokol, Responses API dan Anthropic API, dan telah kompatibel dengan alat pemrograman utama seperti Codex dan Claude Code. Artinya, kamu bisa mengganti API Claude dengan API DeepSeek di dalam Claude Code — biaya turun berkali lipat, sementara pengalamannya nyaris sama.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Model</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Segmen</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Input (per juta Token)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Output (per juta Token)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Jendela Konteks</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DeepSeek V4 Pro</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Flagship reasoning</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3 yuan (≈US$0,43)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">6 yuan (≈US$0,87)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1 juta Token</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DeepSeek V4 Flash</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ringan dan cepat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1 yuan (≈US$0,14)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2 yuan (≈US$0,28)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1 juta Token</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Harga seri DeepSeek V4 (Agustus 2026; harga promo)

Perbandingan harga: untuk input 1 juta Token + output 1 juta Token, DeepSeek V4 Flash menghabiskan sekitar 0,42 dolar AS, GPT-5.6 Sol sekitar 35 dolar AS, dan Claude Fable 5 sekitar 60 dolar AS. Selisihnya mencapai 80-140 kali lipat.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Waspada Jebakan: DeepSeek Akan Naik Harga

{class="mt-1"}
Pihak resmi DeepSeek telah mengumumkan pada 6 Agustus 2026 "rencana menaikkan harga API secara besar-besaran dalam waktu dekat"; harga promonya kemungkinan tidak akan bertahan lama. Sejumlah media memberitakan kenaikannya bisa mencapai 30 kali lipat; hingga 14 Agustus pihak resmi belum mengumumkan skema harga finalnya. Selain itu, versi resmi DeepSeek V4 memperkenalkan mekanisme harga puncak-lembah — harga pemanggilan pada jam sibuk langsung menjadi dua kali lipat. Disarankan memantau pengumuman resmi untuk mendapatkan harga terbaru.
:::

##### 2. Tongyi Qianwen Qwen3.7 Max: Pilihan Enterprise dari Alibaba Cloud

Seri Tongyi Qianwen (Qwen) dari Alibaba Cloud bertumpu pada ekosistem Alibaba Cloud dengan keunggulan alami dalam deployment tingkat enterprise. Qwen3.7 Max yang rilis Juli 2026 adalah flagship saat ini: model dens dengan 235B parameter, konteks native 256K, dapat diperluas hingga 1M. Keunggulan inti Qwen: ekosistem open source yang matang (seluruh seri dari 7B hingga 235B open source), pemahaman skenario bahasa Tionghoa yang presisi, serta integrasi mendalam dengan infrastruktur Alibaba Cloud.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Model</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Harga Output (per juta Token)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Skenario Penggunaan</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">qwen-turbo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">0,6 yuan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tanya jawab sederhana, klasifikasi teks, konkurensi tinggi</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">qwen-long</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2,0 yuan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pemrosesan konteks super panjang 10M</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">qwen3.7-flash</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">7,2 yuan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Percakapan umum, pembuatan konten</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">qwen3.7-plus</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">12,0 yuan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Multimodal (gambar + video), penulisan kreatif bahasa Tionghoa</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">qwen3.7-max</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">36,0 yuan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kemampuan bahasa Tionghoa kelas flagship, tugas kompleks</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Harga bertingkat seri Tongyi Qianwen Qwen (Agustus 2026)

Harga Qwen memakai strategi bertingkat — dari qwen-turbo yang sangat murah (output 0,6 yuan per juta Token) hingga flagship qwen3.7-max (output 36 yuan per juta Token), mencakup seluruh kebutuhan dari tanya jawab ringan hingga reasoning kompleks. Bagi perusahaan yang sudah memakai Alibaba Cloud, Qwen adalah pilihan integrasi yang paling praktis.

##### 3. Zhipu GLM-5.1: No. 1 SWE-bench Buatan Tiongkok

Seri GLM dari Zhipu AI berkinera cemerlang pada 2026. GLM-5.1 meraih peringkat nomor satu buatan Tiongkok di SWE-bench: arsitektur hibrida MoE-dens 744B dengan dukungan konteks 1 juta. Keunikannya adalah pemahaman semantik bahasa Tionghoa yang presisi serta dukungan deployment privat yang patuh regulasi di Tiongkok — hal yang sangat penting untuk sektor keuangan dan pemerintahan yang menuntut keamanan data tinggi. Harga GLM-5.1 adalah 6 yuan untuk input dan 24 yuan untuk output per juta Token, berada di level menengah model buatan Tiongkok.

##### 4. Kimi K3: Raja Teks Super Panjang

Seri Kimi dari Moonshot AI terkenal dengan kemampuan pemrosesan teks super panjang. Kimi K3 yang dirilis Juli 2026 memiliki 2,8 triliun parameter dan masuk jajaran teratas dunia dalam berbagai evaluasi tugas kompleks. Skenario inti Kimi adalah analisis basis kode panjang dan retrieval-augmented untuk dokumen panjang — ia mampu memproses teks satu buku penuh atau kode satu proyek utuh, serta unggul dalam tugas pencarian bergaya "mencari jarum di tumpukan jerami". Harga Kimi relatif tinggi (output sekitar 12-20 yuan per juta Token), tetapi value-nya untuk skenario teks panjang tak tertandingi.

##### 5. Doubao: Sang Serba Bisa dari ByteDance

Seri Doubao dari ByteDance tampil stabil pada 2026. Doubao Seed 2.1 Pro adalah model flagship Volcengine dengan konteks 256K, secara keseluruhan stabil dalam uji coba nyata, dengan pengalaman yang menonjol untuk skenario bahasa Tionghoa. Keunggulan Doubao: bonus Token gratis berlimpah begitu mendaftar, integrasi ekosistem Volcengine yang lengkap, dan harga yang termasuk salah satu yang termurah di Tiongkok. Bagi pemula yang ingin cepat mencoba pemrograman AI, Doubao adalah pilihan masuk tanpa hambatan.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Aspek</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">DeepSeek V4</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Qwen3.7 Max</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">GLM-5.1</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Kimi K3</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Doubao 2.1 Pro</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Skor Keseluruhan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">87.5</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">89.7</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">90.5</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">88+</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">85+</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kemampuan Pemrograman</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sangat kuat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kuat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">No. 1 SWE di Tiongkok</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kuat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Atas rata-rata</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pemahaman Bahasa Tionghoa</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bagus</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bagus</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Akurat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bagus</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bagus</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Jendela Konteks</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1 juta</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">256K-1M</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1 juta</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Super panjang</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">256K</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Harga Output (yuan/M)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">6</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">36</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">24</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">12-20</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">30</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Open Source</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lisensi MIT</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Seluruh seri open source</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sebagian open source</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tertutup</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tertutup</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Deployment Privat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Didukung</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Didukung</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Didukung</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tidak didukung</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tidak didukung</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Perbandingan horizontal lima model besar buatan Tiongkok (Agustus 2026)

Satu tren penting: "kesan ketinggalan generasi" antara model buatan Tiongkok dan GPT/Claude telah lenyap. Dalam reasoning logis dan kompetisi matematika, selisih skor flagship buatan Tiongkok dengan GPT-5 umumnya hanya satu digit. Dalam berpikir arsitektur sistematis dan reasoning engineering yang kompleks, Claude masih memimpin — ia mampu memberikan solusi arsitektur yang lebih "berjiwa", sementara model buatan Tiongkok kadang tampak "kaku mengikuti aturan". Namun pada skenario bahasa Tionghoa, kendali biaya, dan deployment sesuai regulasi, model buatan Tiongkok memiliki keunggulan yang dominan.

::: div .figure
```html
<svg style="max-width:100%;height:auto" width="620" height="290" viewBox="0 0 620 290" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="620" height="290" fill="#ffffff" rx="8"/>
      <line x1="70" y1="230" x2="590" y2="230" stroke="#9ca3af" stroke-width="1.5"/>
      <line x1="70" y1="230" x2="70" y2="20" stroke="#9ca3af" stroke-width="1.5"/>
      <line x1="70" y1="60" x2="590" y2="60" stroke="#e5e7eb" stroke-width="1" stroke-dasharray="4,4"/>
      <line x1="70" y1="116" x2="590" y2="116" stroke="#e5e7eb" stroke-width="1" stroke-dasharray="4,4"/>
      <line x1="70" y1="173" x2="590" y2="173" stroke="#e5e7eb" stroke-width="1" stroke-dasharray="4,4"/>
      <text x="62" y="234" font-size="10" fill="#6b7280" text-anchor="end">0</text>
      <text x="62" y="120" font-size="10" fill="#6b7280" text-anchor="end">50</text>
      <text x="62" y="64" font-size="10" fill="#6b7280" text-anchor="end">100</text>
      <text x="340" y="262" font-size="10.5" fill="#374151" text-anchor="middle">Harga output (yuan/juta Token)</text>
      <!-- bars: price -->
      <rect x="95" y="218" width="60" height="12" fill="#4f46e5"/><text x="125" y="212" font-size="9" fill="#374151" text-anchor="middle">6</text><text x="125" y="248" font-size="9.5" fill="#374151" text-anchor="middle">DeepSeek</text>
      <rect x="195" y="146" width="60" height="84" fill="#4f46e5"/><text x="225" y="140" font-size="9" fill="#374151" text-anchor="middle">36</text><text x="225" y="248" font-size="9.5" fill="#374151" text-anchor="middle">Qwen</text>
      <rect x="295" y="182" width="60" height="48" fill="#4f46e5"/><text x="325" y="176" font-size="9" fill="#374151" text-anchor="middle">24</text><text x="325" y="248" font-size="9.5" fill="#374151" text-anchor="middle">GLM</text>
      <rect x="395" y="200" width="60" height="30" fill="#4f46e5"/><text x="425" y="194" font-size="9" fill="#374151" text-anchor="middle">16</text><text x="425" y="248" font-size="9.5" fill="#374151" text-anchor="middle">Kimi</text>
      <rect x="495" y="170" width="60" height="60" fill="#4f46e5"/><text x="525" y="164" font-size="9" fill="#374151" text-anchor="middle">30</text><text x="525" y="248" font-size="9.5" fill="#374151" text-anchor="middle">Doubao</text>
      <!-- scores -->
      <circle cx="125" cy="118" r="5" fill="#d4a017"/><text x="140" y="114" font-size="9" fill="#78350f">87.5</text>
      <circle cx="225" cy="110" r="5" fill="#d4a017"/><text x="240" y="106" font-size="9" fill="#78350f">89.7</text>
      <circle cx="325" cy="105" r="5" fill="#d4a017"/><text x="340" y="101" font-size="9" fill="#78350f">90.5</text>
      <circle cx="425" cy="112" r="5" fill="#d4a017"/><text x="440" y="108" font-size="9" fill="#78350f">88+</text>
      <circle cx="525" cy="116" r="5" fill="#d4a017"/><text x="540" y="112" font-size="9" fill="#78350f">85+</text>
      <rect x="90" y="30" width="12" height="12" fill="#4f46e5"/><text x="108" y="41" font-size="9.5" fill="#374151">Harga output (makin rendah makin baik)</text>
      <circle cx="170" cy="36" r="5" fill="#d4a017"/><text x="182" y="40" font-size="9.5" fill="#374151">Skor gabungan (makin tinggi makin baik)</text>
    </svg>
```

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Gambar 4: Perbandingan harga dan performa lima model (semakin murah harga semakin baik, semakin tinggi skor semakin baik)
:::

#### 3. Kerangka Keputusan Memilih Model

Setelah mengenal karakteristik tiap model, bagaimana memilih model untuk proyekmu? Berikan padamu satu "metode keputusan empat pertanyaan" — jawab empat pertanyaan, dan model yang paling cocok untukmu langsung terkunci.

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-globe mr-1"></i> Proyek Anda dipasang di dalam negeri (Tiongkok) atau internasional?</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">Lokal → pilih model dalam negeri</span><span class="text-gray-400 mx-1">│</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">Internasional → boleh pilih model luar</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-laptop-code mr-1"></i> Tugas utamanya coding atau lainnya?</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">Coding → Claude atau DeepSeek</span><span class="text-gray-400 mx-1">│</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center">Lainnya → lanjut menilai</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-book mr-1"></i> Butuh konteks super panjang (&gt;500K Token)?</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">Perlu → Gemini atau Kimi</span><span class="text-gray-400 mx-1">│</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center">Tidak perlu → lanjut menilai</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-coins mr-1"></i> Anggaran ketat?</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">Sensitif → DeepSeek atau Qwen-turbo</span><span class="text-gray-400 mx-1">│</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">Tidak sensitif → GPT-5.6 atau Claude</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Gambar 5: Metode Keputusan Empat Pertanyaan untuk Memilih Model Besar
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tips: Strategi Kombinasi

{class="mt-1"}
Metode ini bukan ajaran mati — banyak skenario justru membutuhkan kombinasi beberapa model. Satu strategi kombinasi yang umum: pakai DeepSeek atau Qwen untuk pengembangan harian (biaya murah, bahasa Tionghoa bagus), Claude untuk desain arsitektur krusial (reasoning kuat, halusinasi rendah), dan Gemini untuk analisis multimodal (pemrosesan gambar dan video). Ganti model sesuai kebutuhan, jangan "satu model dipakai sampai mati".
:::

#### 4. Dasar-Dasar Panggilan API: Menghubungkan Model Besar dari Nol

Banyak tutorial pemrograman AI hanya mengajarkan cara memakai antarmuka obrolan, tetapi "pemrograman AI" yang sesungguhnya — membuat aplikasimu memanggil model besar — membutuhkan API. API (Application Programming Interface, antarmuka pemrograman aplikasi) adalah protokol komunikasi antar program. Melalui API, kode kamu bisa memanggil kemampuan model besar seperti memanggil sebuah fungsi.

##### 1. Apa Itu Token

Sebelum mengenal API, kamu wajib memahami dulu konsep "Token". Token adalah satuan dasar penagihan model besar; bisa dipahami sebagai "satuan baca dan tulis AI". Satu Token kira-kira setara dengan 0,75 kata bahasa Inggris (4 karakter), atau 0,5-1 aksara Tionghoa. Satu teks Tionghoa sepanjang 1000 karakter mengonsumsi sekitar 1500-2000 Token.

Token bukan jumlah kata dan bukan pula jumlah karakter. Model besar memakai tokenizer khusus untuk memotong teks menjadi Token. Kata yang sama bisa memiliki jumlah Token berbeda di tiap model — misalnya "kecerdasan buatan" dalam bahasa Tionghoa mungkin 3 Token di GPT tetapi 2 Token di DeepSeek. API kebanyakan model mengembalikan jumlah Token yang benar-benar terpakai, dan kamu bisa melihatnya di respons API.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Perkiraan Cepat Biaya Token

{class="mt-1"}
1 juta karakter teks Tionghoa kira-kira setara 1,5 juta Token. Memproses input 1 juta karakter + output 1 juta karakter dengan DeepSeek V4 Flash berbiaya sekitar 0,42 dolar AS (sekitar 3 yuan); dengan Claude Fable 5 untuk jumlah yang sama berbiaya sekitar 60 dolar AS (sekitar 434 yuan). Inilah alasan pemilihan model berdampak langsung pada biaya proyekmu.
:::

##### 2. Mendapatkan API Key

Langkah pertama memakai API model besar adalah mendapatkan API Key — serangkaian kunci untuk autentikasi identitas. Setiap penyedia model punya platform API sendiri; kamu perlu mendaftar akun dan membuat API Key. Berikut pintu masuk platform API model-model utama beserta proses mendapatkannya:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Model</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Platform API</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Proses Mendapatkan</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Kuota Gratis</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DeepSeek</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">platform.deepseek.com</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Daftar → Verifikasi identitas → Buat API Key</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kuota bonus pengguna baru</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tongyi Qianwen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">bailian.aliyun.com (platform Bailian)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Login akun Alibaba Cloud → Aktifkan layanan → Buat Key</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Uji coba gratis pengguna baru</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Zhipu GLM</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">open.bigmodel.cn</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Daftar → Verifikasi identitas → Buat API Key</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kuota bonus pengguna baru</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kimi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">platform.moonshot.cn</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Daftar → Verifikasi identitas → Buat API Key</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kuota gratis terbatas</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Doubao</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">volcengine.com (Volcengine)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Daftar → Aktifkan layanan Ark → Buat API Key</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bonus Token berlimpah saat mendaftar</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OpenAI GPT</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">platform.openai.com</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Daftar → Hubungkan kartu kredit → Buat API Key</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tanpa kuota gratis (berbayar)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Anthropic Claude</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">console.anthropic.com</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Daftar → Hubungkan kartu → Buat API Key</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kuota kecil untuk pengguna baru</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Platform API model utama dan cara mendapatkan Key (Agustus 2026)

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Peringatan Keamanan: API Key = Kata Sandi Dompetmu

{class="mt-1"}
API Key setara dengan kata sandi dompetmu — siapa pun yang mendapatkan Key bisa memakai kuotamu untuk memanggil model. Karena itu: jangan pernah menuliskan API Key di dalam kode (kelola dengan environment variable); jangan pernah meng-commit kode yang berisi Key ke repositori Git publik; jangan pernah membagikan tangkapan layar yang memuat Key di media sosial. Jika Key bocor, segera hapus di platform dan buat yang baru.
:::

##### 3. Panggilan API Pertama

Setelah mendapatkan API Key, kamu bisa memanggil API model besar dengan bahasa pemrograman apa pun. Berikut contoh pemanggilan paling sederhana dengan Python — mengirim satu pesan ke DeepSeek dan menerima balasannya.

::: div .code-block
:::inline div .code-head
<span>PYTHON · Panggilan API pertama</span><span class="dots">···</span>
:::

```
# Pasang SDK: pip install openai
# DeepSeek kompatibel dengan format OpenAI SDK, bisa langsung dipakai
from openai import OpenAI
import os

# 1. Buat client (API Key dibaca dari environment variable)
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

# 2. Kirim permintaan
response = client.chat.completions.create(
    model="deepseek-chat",  # pilih model
    messages=[
        {"role": "system", "content": "Kamu asisten coding Python."},
        {"role": "user", "content": "Buatkan fungsi quick sort."}
    ]
)

# 3. Ambil balasan
print(response.choices[0].message.content)

# 4. Lihat pemakaian Token
print(f"Token masuk: {response.usage.prompt_tokens}")
print(f"Token keluar: {response.usage.completion_tokens}")
print(f"Total Token: {response.usage.total_tokens}")
```
:::

Logika inti kode ini: buat client (membawa API Key dan alamat model) → susun daftar pesan (system menentukan peran, user adalah input pengguna) → kirim permintaan → terima balasan. Pola ini berlaku hampir untuk semua model yang kompatibel dengan format OpenAI — cukup ganti api_key dan base_url untuk beralih model. Inilah alasan banyak model buatan Tiongkok memilih kompatibel dengan format OpenAI SDK: pengembang cukup mengubah dua baris kode untuk berganti model, biaya migrasinya sangat rendah.

Berikut perbedaan kode saat beralih ke model lain — perhatikan, hanya dua baris yang perlu diubah:

::: div .code-block
:::inline div .code-head
<span>PYTHON · Ganti model cukup ubah dua baris</span><span class="dots">···</span>
:::

```
# DeepSeek
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)
# model="deepseek-chat"

# Qwen (platform Bailian)
client = OpenAI(
    api_key=os.environ.get("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)
# model="qwen-plus"

# Zhipu GLM
client = OpenAI(
    api_key=os.environ.get("GLM_API_KEY"),
    base_url="https://open.bigmodel.cn/api/paas/v4"
)
# model="glm-4"

# OpenAI GPT
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    # base_url cukup pakai nilai default
)
# model="gpt-5.6-terra"
```
:::

##### 4. Menangani Respons Streaming

Dalam aplikasi nyata, kamu biasanya tidak ingin menunggu AI menyelesaikan seluruh isinya sebelum ditampilkan sekaligus — itu membuat pengguna menunggu terlalu lama. Respons streaming (Streaming) memungkinkanmu menampilkan teks kata demi kata bersamaan dengan proses pembuatan oleh AI, meningkatkan pengalaman pengguna secara drastis. Seperti mesin tik, huruf-huruf muncul satu per satu, dan rasanya benar-benar berbeda bagi pengguna.

::: div .code-block
:::inline div .code-head
<span>PYTHON · Respons streaming</span><span class="dots">···</span>
:::

```
# Respons streaming: keluar per karakter
stream = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "user", "content": "Buatkan tutorial bubble sort dengan Python"}
    ],
    stream=True  # aktifkan streaming
)

# terima per blok lalu cetak
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="", flush=True)
# hasilnya muncul per karakter seperti mesin tik
```
:::

#### 5. Panduan Membeli Token Plan

Sebagian besar penyedia model punya dua cara penagihan: bayar sesuai pemakaian (Pay-as-you-go) dan langganan paket (Token Plan / Subscription). Memahami perbedaan keduanya bisa membantumu menekan biaya penggunaan secara signifikan.

##### 1. Bayar per Pemakaian vs Langganan Paket

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Aspek</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Bayar per pemakaian (Pay-as-you-go)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Langganan paket (Subscription)</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cara Penagihan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bayar sesuai jumlah Token yang dipakai</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bayar di muka dengan biaya tetap, dapatkan kuota</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Skenario yang Cocok</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pemakaian tidak stabil, pemanggilan sesekali</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pemakaian stabil, pemanggilan frekuensi tinggi</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Keunggulan Harga</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Harga standar</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">20%-50% lebih murah daripada bayar per pemakaian</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Fleksibilitas</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bisa dipakai kapan saja, tanpa komitmen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Perlu bayar di muka; kuota yang kedaluwarsa bisa hangus</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Penanganan Kelebihan Kuota</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Otomatis ditagih per pemakaian</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Setelah kuota habis, beralih ke bayar per pemakaian</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Contoh Platform</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Platform API resmi masing-masing model</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OpenAI Plus/Pro, Claude Pro, Cursor Pro</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Perbandingan dua cara penagihan

Untuk pemula, sebaiknya mulai dari bayar per pemakaian — tanpa perlu bayar di muka, pakai seberapa banyak bayar seberapa banyak. Setelah volume pemakaian bulananmu stabil di satu level (misalnya di atas 50 yuan per bulan), barulah pertimbangkan beralih ke langganan paket untuk mendapatkan harga satuan yang lebih murah.

##### 2. Ikhtisar Paket Langganan Utama

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Paket</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Biaya Bulanan</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Yang Termasuk</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Cocok Untuk</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ChatGPT Free</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gratis</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Obrolan teks tanpa batas dengan GPT-5.6 Luna</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mencoba dari nol</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ChatGPT Plus</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$20/bulan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GPT-5.6 Sol, pembuatan gambar, analisis data, akses plugin</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pengguna menengah</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ChatGPT Pro</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$200/bulan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pakai semua model tanpa batas, akses prioritas ke fitur baru</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pengguna profesional berat</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Free</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gratis</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Obrolan Claude dengan jumlah terbatas</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mencoba dari nol</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Pro</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$20/bulan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pakai Claude tanpa batas, akses prioritas ke model baru</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pengembang yang coding</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cursor Free</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gratis</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pelengkapan dan obrolan AI dengan jumlah terbatas</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Coba-coba pemula</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cursor Pro</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$20/bulan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pelengkapan AI tanpa batas, 500 permintaan premium per bulan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pengembang sehari-hari</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cursor Business</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$40/bulan/orang</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kolaborasi tim, panel admin, mode privasi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Penggunaan tim</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Paket langganan alat AI utama (Agustus 2026)

Skema langganan model dalam negeri (Tiongkok) sedikit berbeda. DeepSeek terutama memakai bayar per pemakaian tanpa paket langganan bulanan — kamu mengisi saldo dan biaya dipotong sesuai pemakaian nyata. Tongyi Qianwen menyediakan paket sumber daya prabayar di platform Bailian (membeli kuota Token tertentu dengan harga diskon). Doubao di Volcengine juga punya skema prabayar serupa. Bagi pengembang di Tiongkok, kombinasi paling hemat biasanya: DeepSeek bayar per pemakaian (pengembangan harian) + kuota gratis Doubao (uji coba).

##### 3. Platform Agregator API

Jika kamu perlu memakai beberapa model sekaligus, platform agregator API adalah pilihan yang praktis. Platform agregator memberikan satu API Key terpadu sehingga kamu bisa memanggil puluhan model dari seluruh dunia tanpa harus mendaftar di tiap platform.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Platform</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Keunggulan</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Keunggulan Harga</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Skenario yang Cocok</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OpenRouter (openrouter.ai)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Platform agregator internasional; satu Key untuk memanggil model dari seluruh dunia</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Harga transparan, bisa membandingkan harga real-time</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Perlu beralih secara fleksibel antar banyak model luar negeri</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SiliconFlow (siliconflow.cn)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Platform agregator Tiongkok, menyediakan API berbagai model buatan Tiongkok</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">20%-30% lebih murah daripada harga resmi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pengembang di Tiongkok yang ingin membandingkan harga antar model</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Azure OpenAI (proxy Microsoft)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">API OpenAI via proxy Microsoft Azure</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Batch API bisa setengah harga</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Panggilan OpenAI tingkat enterprise, tugas asinkron bervolume besar</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Baidu Qianfan (qianfan.baidubce.com)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Platform AI Cloud Baidu, menyediakan model seperti Wenxin (ERNIE)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kuota gratis untuk pengguna baru</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pengguna ekosistem Baidu</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Platform agregator API populer (Agustus 2026)

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Peringatan jebakan: jangan beli "Key bersama"

{class="mt-1"}
Jangan membeli yang namanya "API Key bersama" di platform seperti Taobao atau Xianyu—Key semacam ini biasanya berasal dari sumber yang tidak jelas, bisa kapan saja diblokir, dan berisiko membocorkan data. Selalu dapatkan API Key melalui platform resmi atau platform agregator yang kredibel.
:::

##### 4. Strategi optimasi biaya

Memilih model yang tepat hanyalah langkah pertama; cara "memakainya secara hemat" sama pentingnya. Berikut beberapa strategi optimasi biaya yang sudah teruji di praktik:

1. Manfaatkan cache hit. Banyak model menyediakan fitur "cache"—ketika permintaanmu memuat konten yang sudah pernah diproses sebelumnya (seperti system prompt), bagian itu hanya ditagih dengan harga sangat rendah. Harga cache hit DeepSeek hanya 1/60 dari harga normal. Letakkan system prompt yang tetap di awal daftar pesan agar cache hit maksimal.
2. Routing berjenjang—pakai model murah untuk tugas sederhana dan model mahal untuk tugas kompleks. Misalnya, pakai DeepSeek V4 Flash untuk klasifikasi teks (output 2 yuan/juta token) dan Claude untuk desain arsitektur (output 181 yuan/juta token). Sekitar 80% panggilan dalam satu proyek bisa memakai model murah.
3. Batasi panjang output. API ditagih berdasarkan token output; semakin panjang, semakin mahal. Pada skenario yang tidak butuh penjelasan panjang lebar, atur parameter max_tokens untuk membatasi panjang output agar AI tidak "terlalu banyak basa-basi".
4. Gunakan Batch API untuk tugas non-real-time. Jika kamu punya banyak tugas yang tidak butuh respons seketika (misalnya pelabelan data massal atau ringkasan dokumen), Batch API memberikan diskon 50%. OpenAI dan Azure sama-sama menyediakan fitur ini.
5. Pantau pemakaian token. Sebagian besar platform API menyediakan dasbor statistik pemakaian. Periksa berkala distribusi pemakaiannya, cari panggilan yang paling boros token, lalu optimalkan secara terarah. Satu penyesuaian kecil pada prompt (misalnya mengganti "jelaskan secara rinci" dengan "jelaskan dalam 3 kalimat") bisa menghemat 50% token.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Strategi optimasi</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Penghematan</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Tingkat kesulitan</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Keterangan</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cache hit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Hingga 98%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Rendah</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Letakkan konten yang tetap di awal pesan</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Routing berjenjang</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">50%-80%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sedang</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Model murah untuk tugas sederhana</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Batasi panjang output</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">30%-60%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Rendah</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Atur parameter max_tokens</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Batch API</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">50%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Rendah</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Batch untuk tugas non-real-time</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Optimasi prompt</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">20%-50%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sedang</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Padatkan prompt, kurangi bagian berlebih</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Strategi optimasi biaya dan hasilnya (Agustus 2026)

#### 6. Praktik: menghubungkan API model besar ke proyek

Mari akhiri bab ini dengan satu praktik lengkap—membuat "Generator Ringkasan AI": pengguna memasukkan sepotong teks panjang, lalu program memanggil API model besar untuk menghasilkan ringkasan. Praktik ini memperlihatkan alur lengkap pemanggilan API: konfigurasi lingkungan, pemanggilan API, penanganan error, dan kontrol biaya.

::: div .code-block
:::inline div .code-head
<span>PYTHON · ai_summarizer.py</span><span class="dots">···</span>
:::

```
# ai_summarizer.py - peringkas teks AI
import os
from openai import OpenAI

# 1. Konfigurasi (baca API Key dari environment variable, jangan pernah hardcode)
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

def summarize(text: str, max_length: int = 200) -> dict:
    """Meringkas teks

    Args:
        text: teks asli yang akan diringkas
        max_length: panjang ringkasan maksimum (jumlah Token)

    Returns:
        dict: berisi ringkasan dan info pemakaian Token
    """
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {
                    "role": "system",
                    "content": "Kamu adalah generator ringkasan."
                               "Rangkum teks yang diberikan pengguna secara ringkas."
                               "Ringkasan tidak lebih dari 3 kalimat."
                },
                {
                    "role": "user",
                    "content": f"Ringkas teks berikut:\n\n{text}"
                }
            ],
            max_tokens=max_length,  # batasi panjang keluaran
            temperature=0.3  # suhu rendah=lebih stabil
        )

        return {
            "success": True,
            "summary": response.choices[0].message.content,
            "input_tokens": response.usage.prompt_tokens,
            "output_tokens": response.usage.completion_tokens,
            "total_tokens": response.usage.total_tokens
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

# 2. Contoh pemakaian
if __name__ == "__main__":
    long_text = """
    (tempel teks panjang di sini...)
    """

    result = summarize(long_text)

    if result["success"]:
        print(f"Ringkasan: {result['summary']}")
        print(f"Token terpakai: {result['total_tokens']}")
        # estimasi biaya: DeepSeek V4 Flash
        cost = result['total_tokens'] * 0.000004  # sekitar 0.4 sen per seribu Token
        print(f"Estimasi biaya: {cost:.4f} yuan")
    else:
        print(f"Terjadi kesalahan: {result['error']}")
```
:::

Kode ini mencerminkan beberapa praktik terbaik pemanggilan API: API Key dibaca lewat environment variable, tidak pernah ditulis langsung di dalam kode; fungsi dilengkapi dokumentasi dan type hint yang jelas; max_tokens diatur untuk membatasi panjang output; temperature diatur rendah (0.3) agar output lebih stabil; penanganan error lengkap; dan informasi konsumsi token dikembalikan untuk pelacakan biaya. Saat kamu memakai AI untuk menulis kode ini, sampaikan saja persyaratan-persyaratan tersebut—AI sepenuhnya mampu mewujudkannya untukmu.

:::inline div .quote-line
Pelajaran terakhir bab ini: model adalah "amunisi", metodologi adalah "taktik". Memilih amunisi yang tepat membuat pertempuran lebih lancar, tetapi tanpa taktik yang baik, amunisi sebanyak apa pun tak akan menang. Setelah mengenal karakter tiap model dan cara memakai API, Anda punya "gudang amunisi" yang cukup—tetapi bagaimana memenangkan pertempurannya tetap bergantung pada metodologi berpikir yang dipelajari di bab-bab sebelumnya.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mari praktik: buat panggilan API pertamamu berhasil

{class="mt-1"}
Daftar di satu platform model dalam negeri (disarankan DeepSeek atau Zhipu—keduanya memberi kuota gratis bagi pengguna baru), buat API Key, tuliskan ke environment variable sistem (bukan ke dalam kode!), lalu jalankan kode "panggilan API pertama" di atas. Pada saat jawaban AI berhasil tercetak, kamu sudah melewati garis batas antara "memakai AI" dan "membangun aplikasi AI".
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan bab ini

- Tiga raksasa internasional: GPT-5.6 (seimbang dan serba bisa), Claude (puncak kemampuan coding + tingkat halusinasi hanya 1%), Gemini (raja multimodal + konteks 2 juta)
- Lima raksasa dalam negeri: DeepSeek V4 (raja value for money, perhatikan pengumuman kenaikan harga), Qwen3.7 (kelas enterprise), GLM-5.1 (nomor satu dalam negeri untuk SWE), Kimi K3 (teks super panjang), Doubao (gratis untuk pemula)
- Metode keputusan empat pertanyaan: di-deploy di mana? untuk coding atau lainnya? butuh konteks super panjang? sensitif terhadap anggaran?
- Token adalah satuan penagihan: 1 karakter Mandarin sekitar 1,5-2 token; 1 juta karakter sekitar 1,5 juta token
- API Key = sandi dompetmu: kelola lewat environment variable, jangan pernah ditulis langsung di kode, jangan diunggah ke Git
- Model dalam negeri umumnya kompatibel dengan OpenAI SDK: mengganti model cukup dengan mengubah dua baris, api_key dan base_url
- Lima cara hemat: cache hit, routing berjenjang, batasi output, Batch API, pantau pemakaian
:::
