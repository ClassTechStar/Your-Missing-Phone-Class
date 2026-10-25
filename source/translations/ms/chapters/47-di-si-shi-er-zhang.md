---
id: di-si-shi-er-zhang
num: 42
part: ai-biancheng-pian
nav: Bab 42: Panorama Model Besar dan Praktik API
toc: default
kind: chapter
---

### Bab 42: Panorama Model Bahasa Besar dan Praktik API

{class="chapter-intro mb-4"}
Bab-bab sebelum ini bercakap tentang "cara bekerjasama dengan AI"; bab ini menyelesaikan satu soalan yang lebih asas: "gunakan AI yang mana? bagaimana menggunakannya?" Landskap model bahasa besar pada Ogos 2026 sudah sangat pelbagai — di peringkat antarabangsa ada pertarungan tiga kuasa besar iaitu GPT, Claude dan Gemini; di China pula ada DeepSeek, Tongyi Qianwen, GLM, Kimi dan Doubao yang berkembang masing-masing. Setiap model mempunyai personaliti dan kepakaran tersendiri: pilih dengan tepat, kerja menjadi lebih mudah; pilih dengan salah, kerja menjadi lebih sukar. Bab ini bukan sahaja membawa anda mengenali model-model ini, malah mengajar anda cara menyambungkannya ke aplikasi anda sendiri melalui API, serta cara memilih Token Plan (pakej penggunaan) yang sesuai mengikut keperluan anda.

#### 1. Model Bahasa Besar Antarabangsa Utama: Landskap Tiga Kuasa

Pasaran model bahasa besar antarabangsa pada Ogos 2026 telah membentuk landskap tiga kuasa besar: OpenAI (siri GPT), Anthropic (siri Claude) dan Google (siri Gemini). Setiap syarikat mempunyai ciri yang tersendiri — mari kita kenali satu demi satu.

##### 1. Siri OpenAI GPT-5.6: Pejuang Serba Boleh yang Seimbang

OpenAI ialah perintis gelombang model bahasa besar, dan siri GPT sehingga kini masih menjadi model paling luas digunakan di dunia. Siri GPT-5.6 yang dikeluarkan pada Julai 2026 menggunakan strategi tiga kedudukan: varian utama GPT-5.6 Sol untuk keperluan penaakulan tahap tinggi, varian seimbang GPT-5.6 Terra untuk pembangunan harian, dan varian ringan GPT-5.6 Luna untuk senario beban serentak tinggi berkos rendah. Ketiga-tiga model berkongsi tetingkap konteks 1.05 juta Token, dan semuanya menyokong input imej, pemanggilan fungsi serta output berstruktur.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Varian</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Peranan</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Input (/juta Token)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Output (/juta Token)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Tetingkap konteks</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GPT-5.6 Sol</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Penaakulan utama</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$5.00 (sekitar 36 yuan)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$30.00 (sekitar 217 yuan)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1.05 juta Token</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GPT-5.6 Terra</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Seimbang harian</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$2.50 (sekitar 18 yuan)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$15.00 (sekitar 109 yuan)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1.05 juta Token</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GPT-5.6 Luna</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ringan kos rendah</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$1.00 (sekitar 7 yuan)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$6.00 (sekitar 44 yuan)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1.05 juta Token</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Harga siri OpenAI GPT-5.6 (Ogos 2026)

Kelebihan teras siri GPT terletak pada "keseimbangan" — penaakulan, pengaturcaraan, penulisan, multimodal; tiada kelemahan yang ketara. Ditambah pula dengan ekosistem sambungan OpenAI yang besar dan komuniti pembangunnya, dokumentasi dan rantaian alatnya paling lengkap. Bagi senario "tidak tahu nak pilih apa", GPT ialah jawapan lalai "pilih dengan mata tertutup pun tidak silap". Tetapi kelemahannya: akses dari China memerlukan rangkaian khas, ungkapan bahasa Cinanya kadangkala berbau "terjemahan", dan harga API berada pada tahap sederhana hingga tinggi.

::: div .success-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Berita Baik

{class="mt-1"}
Pada Ogos 2026, OpenAI mengumumkan model lalai untuk pengguna percuma dinaik taraf kepada GPT-5.6 Luna, serta membuka sembang teks tanpa had. Ini bermakna anda boleh merasai keupayaan asas GPT tanpa kos; bayaran hanya diperlukan apabila anda memerlukan penaakulan yang lebih kuat atau panggilan API.
:::

##### 2. Siri Anthropic Claude: Puncak Pengaturcaraan dan Kejituan

Jika GPT ialah atlet serba boleh, maka Claude ialah "puncak" dalam bidang pengaturcaraan. Siri Claude daripada Anthropic mendahului SWE-bench (ujian penanda aras kejuruteraan perisian) secara berterusan dengan jurang yang jauh, dengan kualiti penjanaan kod dan keupayaan melaksanakan projek peringkat kejuruteraan yang terbaik dalam industri. Lebih jarang lagi, kadar halusinasi Claude (kebarangkalian menjana maklumat palsu) paling rendah di seluruh rangkaian, hanya sekitar 1% — menjadikannya sangat sesuai untuk senario ketepatan tinggi seperti akademik dan undang-undang.

Senjata maut Claude yang satu lagi ialah konteks jangka panjang luar biasa: menyokong tetingkap konteks 1 juta Token, mampu "membaca habis" kontrak beratus-ratus muka surat atau seluruh kod projek sekali gus tanpa terlepas butiran. Ini hampir tiada pengganti dalam senario seperti penstrukturan semula kod dan analisis dokumen panjang. Claude Code, sebagai alat pengaturcaraan AI terminal, mencapai pendapatan tahunan AS$2.5 bilion menjelang pertengahan 2026 — itulah bukti paling kukuh pengiktirafan terhadap keupayaan pengaturcaraan Claude.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Varian</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Peranan</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Input (/juta Token)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Output (/juta Token)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Tetingkap konteks</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Fable 5</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Varian utama</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$10.00 (sekitar 72 yuan)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$50.00 (sekitar 362 yuan)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1 juta Token</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Opus 4.8</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Varian profesional</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$5.00 (sekitar 36 yuan)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$25.00 (sekitar 181 yuan)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1 juta Token</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Sonnet 5</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Varian nilai wang</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$2.00 (sekitar 14 yuan)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$10.00 (sekitar 72 yuan)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1 juta Token</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Harga siri Anthropic Claude (Ogos 2026; Sonnet 5 pada harga diskaun)

Kelemahan Claude ialah harga — harga output Fable 5 paling tinggi antara semua model, iaitu AS$50 setiap juta Token. Keupayaan multimodalnya (kefahaman imej dan video) juga agak lemah. Bagi pembangun persendirian berkemampuan terhad, Sonnet 5 pada tempoh diskaun sangat menonjol dari segi nilai wang.

##### 3. Siri Google Gemini: Raja Multimodal

Siri Gemini daripada Google telah berkembang ke versi 3.1 Pro pada 2026. Senjata maut terbesar Gemini ialah multimodal asli — penghuraian imej dan teks yang tepat, pengesanan jadual OCR tanpa ralat, pengekstrakan bingkai video yang cekap, dan turut menyokong penghuraian audio dan video secara mendalam. Ia terikat rapat dengan ekosistem Google (carian, e-mel, perkhidmatan awan) dan menonjol dalam pengambilan maklumat masa nyata serta kefahaman merentas modal. Gemini turut menyokong input konteks sehingga 2 juta Token, iaitu tetingkap konteks terbesar pada masa kini.

Kedudukan Gemini ialah "pilihan utama bagi penaakulan saintifik dan senario multimodal". Jika projek anda melibatkan banyak analisis imej, kefahaman video atau pengiraan saintifik, Gemini hampir tiada penanding. Tetapi dalam penjanaan kod teks tulen ia sedikit kalah daripada Claude, dan ungkapan bahasa Cinanya juga tidak semula jadi seperti model buatan China.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Perkara perbandingan</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">GPT-5.6</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Claude Fable 5</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Gemini 3.1 Pro</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Skor keseluruhan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">94.8</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">95.0</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">92.1</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Keupayaan pengaturcaraan (SWE-bench)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">74.9%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">64.3% (Pro)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sederhana</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tetingkap konteks</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1.05 juta Token</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1 juta Token</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2 juta Token</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Keupayaan multimodal</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Seimbang</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Agak lemah</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Paling kuat</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kadar halusinasi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Agak rendah</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Paling rendah (sekitar 1%)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Agak rendah</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ketersediaan di China</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Perlu rangkaian khas</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Perlu rangkaian khas</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Perlu rangkaian khas</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ekosistem API</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Paling lengkap</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sedang berkembang</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Terikat pada ekosistem Google</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Perbandingan mendatar tiga model antarabangsa (Ogos 2026)

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Perhatian: Halangan realiti penggunaan di China

{class="mt-1"}
Bagi pembangun di China, halangan utama GPT, Claude dan Gemini ialah akses rangkaian. Walaupun boleh digunakan secara tidak langsung melalui proksi Azure, platform agregasi API dan sebagainya, kestabilan dan pematuhan perlu dinilai sendiri. Jika projek anda mempunyai keperluan ketat terhadap keselamatan data, disyorkan mengutamakan model buatan China.
:::

#### 2. Model Bahasa Besar Buatan China Utama: Pelbagai Jenis Berkembang

Pada 2026, model bahasa besar buatan China telah bertukar daripada "pengejar" kepada "pelari seiring", malah "mendahului" dalam sesetengah bidang. Berbeza dengan kontroversi "model pembalut" tahun 2023, model utama buatan China pada 2026 sudah setanding dengan model tahap terbaik antarabangsa dalam penaakulan logik, penjanaan kod dan kefahaman bahasa Cina, dengan jurang menyusut kepada bawah 5%. Lebih penting lagi, model buatan China mempunyai kelebihan yang tidak boleh digantikan dalam senario bahasa Cina, kos harga dan pelancaran yang mematuhi peraturan.

##### 1. DeepSeek V4: Raja Nilai Wang

DeepSeek ialah kehadiran fenomena dalam kalangan model bahasa besar buatan China. Pada awal 2025, DeepSeek-V3 menggemparkan pasaran dengan kedudukan "sepuluh kali lebih murah daripada GPT tetapi keupayaan setanding", dan digelar industri sebagai "garis pemusnah" model AI sejagat — yang lebih murah tidak sebaik ia, yang lebih mahal pula tidak selimpat ia. Menjelang Ogos 2026, versi rasmi DeepSeek V4-Pro dikeluarkan: seni bina MoE berskala 1.6 trilion parameter dengan pengaktifan sekitar 49B, menyokong konteks 1 juta tanpa kehilangan, dan nilai wangnya bagi kod secara meluas dianggap puncak dunia.

DeepSeek V4 mencapai lompatan besar dalam keupayaan Agent — penanda aras DeepSWE melonjak daripada 12.8 kepada 62.7 (+390%), dan NL2Repo meningkat daripada 38.5 kepada 61.5. API menambah sokongan dwi-protokol Responses API dan Anthropic API, dan telah serasi dengan alat pengaturcaraan arus perdana seperti Codex dan Claude Code. Ini bermakna anda boleh menggunakan API DeepSeek menggantikan API Claude dalam Claude Code — kos menurun beberapa kali ganda, pengalaman hampir sama.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Varian</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Peranan</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Input (/juta Token)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Output (/juta Token)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Tetingkap konteks</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DeepSeek V4 Pro</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Penaakulan utama</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3 yuan (sekitar US$0.43)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">6 yuan (sekitar US$0.87)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1 juta Token</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DeepSeek V4 Flash</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ringan pantas</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1 yuan (sekitar US$0.14)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2 yuan (sekitar US$0.28)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1 juta Token</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Harga siri DeepSeek V4 (Ogos 2026, harga promosi)

Perbandingan harga: bagi 1 juta Token input + 1 juta Token output yang sama, DeepSeek V4 Flash berkos sekitar AS$0.42, GPT-5.6 Sol sekitar AS$35, dan Claude Fable 5 sekitar AS$60. Jurangnya sehingga 80-140 kali ganda.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Peringatan elak jerat: Harga DeepSeek akan naik

{class="mt-1"}
Pihak rasmi DeepSeek telah mengumumkan pada 6 Ogos 2026 "berancangan menaikkan harga API secara besar-besaran dalam masa terdekat", jadi harga promosi mungkin tidak bertahan lama. Sebahagian media mengkhabarkan kenaikan mungkin mencapai 30 kali ganda; sehingga 14 Ogos, pihak rasmi masih belum mengumumkan pelan penetapan harga akhir. Selain itu, versi rasmi DeepSeek V4 memperkenalkan mekanisme harga puncak dan lembah — harga panggilan pada waktu puncak meningkat dua kali ganda. Disyorkan memantau pengumuman rasmi untuk harga terkini.
:::

##### 2. Tongyi Qianwen Qwen3.7 Max: Pilihan Peringkat Perusahaan Alibaba Cloud

Siri Tongyi Qianwen (Qwen) daripada Alibaba Cloud bersandar pada ekosistem Alibaba Cloud dan mempunyai kelebihan semula jadi dalam pelancaran peringkat perusahaan. Qwen3.7 Max yang dikeluarkan pada Julai 2026 ialah model utama semasa: model padat 235B parameter dengan konteks asli 256K, boleh dikembangkan sehingga 1M. Kelebihan teras Qwen: ekosistem sumber terbuka yang matang (seluruh siri daripada 7B hingga 235B bersumber terbuka), kefahaman senario bahasa Cina yang tepat, serta integrasi mendalam dengan infrastruktur Alibaba Cloud.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Varian</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Harga output (/juta Token)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Senario sesuai</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">qwen-turbo</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">0.6 yuan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Soal jawab minimum, pengelasan teks, beban serentak tinggi</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">qwen-long</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2.0 yuan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pemprosesan konteks amat panjang 10M</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">qwen3.7-flash</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">7.2 yuan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sembang umum, penjanaan kandungan</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">qwen3.7-plus</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">12.0 yuan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Multimodal (imej + video), penulisan bahasa Cina</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">qwen3.7-max</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">36.0 yuan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Keupayaan bahasa Cina tahap utama, tugasan kompleks</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Harga berperingkat siri Tongyi Qianwen Qwen (Ogos 2026)

Harga Qwen menggunakan strategi berperingkat — daripada qwen-turbo berkos sangat rendah (output 0.6 yuan/juta Token) hingga model utama qwen3.7-max (output 36 yuan/juta Token), meliputi keseluruhan keperluan daripada soal jawab ringan hingga penaakulan kompleks. Bagi perusahaan yang sudah menggunakan Alibaba Cloud, Qwen ialah pilihan integrasi paling mudah.

##### 3. Zhipu GLM-5.1: Yang Pertama SWE-bench Buatan China

Siri GLM daripada Zhipu AI mempamerkan prestasi cemerlang pada 2026. GLM-5.1 meraih keputusan pertama buatan China pada SWE-bench: seni bina hibrid padat MoE 744B, menyokong konteks 1 juta. Kepakarannya ialah kefahaman semantik bahasa Cina yang tepat, serta menyokong pelancaran peribadi yang mematuhi peraturan di China — ini sangat penting bagi senario kewangan dan kerajaan yang menuntut keselamatan data tinggi. Harga GLM-5.1 ialah 6 yuan untuk input dan 24 yuan untuk output setiap juta Token, berada pada tahap pertengahan model buatan China.

##### 4. Kimi K3: Raja Teks Jangka Panjang

Siri Kimi daripada Moonshot AI terkenal dengan keupayaan memproses teks jangka panjang luar biasa. Kimi K3 yang dikeluarkan pada Julai 2026 berskala 2.8 trilion parameter dan memasuki gred pertama dunia dalam banyak penilaian tugasan kompleks. Senario teras Kimi ialah analisis kod sumber panjang dan pengambilan semula dokumen panjang yang dipertingkat — ia boleh memproses teks seluruh buku atau kod seluruh projek, dan cemerlang dalam tugasan pengambilan gaya "mencari jarum dalam timbunan jerami". Harga Kimi agak tinggi (output sekitar 12-20 yuan/juta Token), tetapi nilai wangnya dalam senario teks panjang tiada penanding.

##### 5. Doubao: Atlet Serba Boleh ByteDance

Siri Doubao daripada ByteDance mempamerkan prestasi stabil pada 2026. Doubao Seed 2.1 Pro ialah model utama Volcengine dengan konteks 256K, prestasi keseluruhan yang stabil dalam ujian sebenar, dan pengalaman senario bahasa Cina yang menonjol. Kelebihan Doubao: pendaftaran terus menerima Token percuma dalam kuantiti banyak, integrasi ekosistem Volcengine yang lengkap, dan harga dalam kalangan yang paling rendah di China. Bagi pemula yang ingin cepat merasai pengaturcaraan AI, Doubao ialah pilihan permulaan tanpa halangan.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Perkara perbandingan</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">DeepSeek V4</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Qwen3.7 Max</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">GLM-5.1</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Kimi K3</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Doubao 2.1 Pro</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Skor keseluruhan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">87.5</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">89.7</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">90.5</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">88+</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">85+</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Keupayaan pengaturcaraan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Amat kuat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kuat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SWE pertama buatan China</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kuat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pertengahan ke atas</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kefahaman bahasa Cina</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cemerlang</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cemerlang</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tepat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cemerlang</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cemerlang</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tetingkap konteks</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1 juta</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">256K-1M</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1 juta</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Amat panjang</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">256K</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Harga output (yuan/M)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">6</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">36</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">24</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">12-20</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">30</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sumber terbuka</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lesen MIT</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Seluruh siri sumber terbuka</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sebahagian sumber terbuka</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sumber tertutup</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sumber tertutup</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pelancaran peribadi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Disokong</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Disokong</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Disokong</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tidak disokong</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tidak disokong</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Perbandingan mendatar lima model buatan China (Ogos 2026)

Satu trend penting: "rasa jurang generasi" antara model buatan China dengan GPT/Claude telah hilang. Dalam penaakulan logik dan pertandingan matematik, jurang skor antara model utama buatan China dengan GPT-5 secara amnya hanya dalam angka satu digit. Dalam pemikiran seni bina berstruktur dan penaakulan kejuruteraan kompleks, Claude masih mendahului — ia mampu memberikan pelan seni bina yang lebih bernyawa dengan kreativiti, manakala model buatan China kadangkala kelihatan "kaku". Tetapi dalam senario bahasa Cina, kawalan kos dan pelancaran yang mematuhi peraturan, model buatan China mempunyai kelebihan yang jauh mengatasi.

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
Rajah 4: Perbandingan harga dan prestasi lima model (harga semakin rendah semakin baik, skor semakin tinggi semakin baik)
:::

#### 3. Kerangka Keputusan Pemilihan Model

Selepas memahami ciri setiap model, bagaimana memilih model untuk projek anda? Di sini kami berikan anda "kaedah keputusan empat soalan" — jawab empat soalan ini, dan anda boleh mengunci model yang paling sesuai dengan anda.

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-globe mr-1"></i> Projek anda dilaksanakan dalam negara atau antarabangsa?</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">Dalam negara → pilih model tempatan</span><span class="text-gray-400 mx-1">│</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">Antarabangsa → boleh pilih model luar negara</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-laptop-code mr-1"></i> Tugas utamanya pengekodan atau lain?</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">Pengekodan → Claude atau DeepSeek</span><span class="text-gray-400 mx-1">│</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center">Lain-lain → terus nilai</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-book mr-1"></i> Perlu konteks sangat panjang (&gt;500K Token)?</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">Perlu → Gemini atau Kimi</span><span class="text-gray-400 mx-1">│</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center">Tidak perlu → terus nilai</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-coins mr-1"></i> Bajet terhad?</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">Sensitif → DeepSeek atau Qwen-turbo</span><span class="text-gray-400 mx-1">│</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center">Tidak sensitif → GPT-5.6 atau Claude</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Rajah 5: Kaedah keputusan empat soalan pemilihan model bahasa besar
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Petua: Strategi gabungan

{class="mt-1"}
Kaedah keputusan ini bukan dogma — banyak senario memerlukan gabungan beberapa model. Satu strategi gabungan yang lazim: guna DeepSeek atau Qwen untuk pembangunan harian (kos rendah, bahasa Cina bagus), Claude untuk reka bentuk seni bina kritikal (penaakulan kuat, halusinasi rendah), dan Gemini untuk analisis multimodal (pemprosesan imej dan video). Tukar model mengikut keperluan, bukan "satu model diguna sehingga tamat".
:::

#### 4. Asas Panggilan API: Menyambungkan Model Bahasa Besar dari Sifar

Banyak tutorial pengaturcaraan AI hanya mengajar anda menggunakan antara muka sembang, tetapi "pengaturcaraan AI" yang sebenar — membolehkan aplikasi anda memanggil model bahasa besar — perlu melalui API. API (Application Programming Interface, antara muka pengaturcaraan aplikasi) ialah protokol komunikasi antara atur cara. Melalui API, kod anda boleh memanggil keupayaan model bahasa besar seperti memanggil satu fungsi.

##### 1. Apakah Itu Token

Sebelum memahami API, anda mesti memahami konsep "Token" dahulu. Token ialah unit asas pengebilan model bahasa besar, boleh difahami sebagai "unit bacaan dan penulisan AI". Satu Token lebih kurang bersamaan: 0.75 patah perkataan (4 aksara) dalam bahasa Inggeris, dan 0.5-1 aksara Cina dalam bahasa Cina. Satu teks bahasa Cina sepanjang 1000 aksara mengguna kira-kira 1500-2000 Token.

Token bukan bilangan perkataan, juga bukan bilangan aksara. Model bahasa besar menggunakan peng-token khusus (Tokenizer) untuk memotong teks menjadi Token. Bilangan Token bagi perkataan yang sama mungkin berbeza antara model — contohnya, "kecerdasan buatan" mungkin 3 Token dalam GPT tetapi 2 dalam DeepSeek. API kebanyakan model memulangkan jumlah Token yang sebenarnya digunakan, dan anda boleh melihatnya dalam respons API.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Anggaran Kos Token dengan Pantas

{class="mt-1"}
1 juta aksara bahasa Cina bersamaan kira-kira 1.5 juta Token. Menggunakan DeepSeek V4 Flash untuk 1 juta aksara input + 1 juta aksara output berkos sekitar AS$0.42 (sekitar 3 yuan); menggunakan Claude Fable 5 untuk kuantiti yang sama berkos sekitar AS$60 (sekitar 434 yuan). Itulah sebabnya pemilihan model mempengaruhi kos projek anda secara langsung.
:::

##### 2. Memperoleh API Key

Langkah pertama menggunakan API model bahasa besar ialah memperoleh API Key — satu rentetan kunci untuk pengesahan identiti. Setiap penyedia model mempunyai platform API tersendiri; anda perlu mendaftar akaun dan mencipta API Key. Berikut ialah pintu masuk platform API model-model utama dan proses memperolehnya:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Model</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Platform API</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Proses perolehan</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Kuota percuma</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DeepSeek</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">platform.deepseek.com</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Daftar → Sahkan identiti → Cipta API Key</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kuota hadiah untuk pengguna baharu</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tongyi Qianwen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">bailian.aliyun.com (Platform Bailian)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Log masuk akaun Alibaba Cloud → Aktifkan perkhidmatan → Cipta Key</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Percubaan percuma untuk pengguna baharu</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Zhipu GLM</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">open.bigmodel.cn</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Daftar → Sahkan identiti → Cipta API Key</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kuota hadiah untuk pengguna baharu</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kimi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">platform.moonshot.cn</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Daftar → Sahkan identiti → Cipta API Key</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kuota percuma terhad</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Doubao</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">volcengine.com (Volcengine)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Daftar → Aktifkan Volcano Ark → Cipta API Key</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pendaftaran memberi Token percuma yang banyak</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OpenAI GPT</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">platform.openai.com</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Daftar → Ikat kad kredit → Cipta API Key</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tiada kuota percuma (perlu bayar)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Anthropic Claude</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">console.anthropic.com</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Daftar → Ikat kad → Cipta API Key</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kuota kecil untuk pengguna baharu</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Platform API model utama dan cara memperoleh Key (Ogos 2026)

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Peringatan keselamatan: API Key = kata laluan dompet

{class="mt-1"}
API Key setara dengan kata laluan dompet anda — sesiapa yang mendapat Key boleh menggunakan kuota anda untuk memanggil model. Oleh itu: jangan sesekali menulis API Key dalam kod (urus dengan pemboleh ubah persekitaran); jangan sesekali memuat naik kod yang mengandungi Key ke repositori Git awam; jangan sesekali berkongsi tangkapan skrin yang mengandungi Key di media sosial. Jika Key bocor, padamkan serta-merta di platform dan cipta semula.
:::

##### 3. Panggilan API Pertama

Selepas memperoleh API Key, anda boleh memanggil API model bahasa besar dengan sebarang bahasa pengaturcaraan. Berikut ialah demonstrasi panggilan paling ringkas menggunakan Python — menghantar satu mesej kepada DeepSeek dan menerima balasannya.

::: div .code-block
:::inline div .code-head
<span>PYTHON · Panggilan API pertama</span><span class="dots">···</span>
:::

```
# Pasang SDK: pip install openai
# DeepSeek serasi dengan format OpenAI SDK, boleh terus guna
from openai import OpenAI
import os

# 1. Cipta klien (API Key dibaca daripada pemboleh ubah persekitaran)
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

# 2. Hantar permintaan
response = client.chat.completions.create(
    model="deepseek-chat",  # pilih model
    messages=[
        {"role": "system", "content": "Kamu pembantu pengaturcaraan Python."},
        {"role": "user", "content": "Tuliskan fungsi quick sort."}
    ]
)

# 3. Dapatkan balasan
print(response.choices[0].message.content)

# 4. Lihat penggunaan Token
print(f"Token masuk: {response.usage.prompt_tokens}")
print(f"Token keluar: {response.usage.completion_tokens}")
print(f"Jumlah Token: {response.usage.total_tokens}")
```
:::

Logik teras kod ini ialah: cipta klien (membawa API Key dan alamat model) → bina senarai mesej (system menetapkan peranan, user ialah input pengguna) → hantar permintaan → terima balasan. Corak ini hampir sesuai untuk semua model yang serasi dengan format OpenAI — cukup dengan menukar api_key dan base_url untuk bertukar model. Itulah sebabnya banyak model buatan China memilih keserasian dengan format OpenAI SDK: pembangun hanya perlu mengubah dua baris kod untuk bertukar model, kos pemindahan sangat rendah.

Berikut ialah perbezaan kod untuk bertukar kepada model lain — perhatikan hanya dua baris perlu diubah:

::: div .code-block
:::inline div .code-head
<span>PYTHON · Tukar model cukup ubah dua baris</span><span class="dots">···</span>
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
    # base_url boleh guna nilai lalai
)
# model="gpt-5.6-terra"
```
:::

##### 4. Mengendalikan Respons Strim

Dalam aplikasi sebenar, anda biasanya tidak mahu menunggu AI menulis habis semua kandungan sebelum dipaparkan sekaligus — itu membuat pengguna menunggu terlalu lama. Respons strim (Streaming) membolehkan anda memaparkan aksara demi aksara sebaik AI menjana, meningkatkan pengalaman pengguna dengan besar. Seperti mesin taip, huruf muncul satu demi satu — rasa pengguna benar-benar berbeza.

::: div .code-block
:::inline div .code-head
<span>PYTHON · Respons strim</span><span class="dots">···</span>
:::

```
# Respons strim: keluar huruf demi huruf
stream = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "user", "content": "Tuliskan tutorial bubble sort guna Python"}
    ],
    stream=True  # hidupkan strim
)

# terima blok demi blok dan cetak
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="", flush=True)
# hasil akan muncul huruf demi huruf seperti mesin taip
```
:::

#### 5. Panduan Membeli Token Plan

Kebanyakan penyedia model mempunyai dua cara pengebilan: bayar mengikut penggunaan (Pay-as-you-go) dan langganan pakej (Token Plan / Subscription). Memahami perbezaan kedua-duanya dapat membantu anda menurunkan kos penggunaan dengan besar.

##### 1. Bayar Mengikut Penggunaan vs Langganan Pakej

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Dimensi</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Bayar mengikut penggunaan (Pay-as-you-go)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Langganan pakej (Subscription)</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cara pengebilan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bayar sebanyak Token yang digunakan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bayar fi tetap terlebih dahulu, dapat kuota</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Senario sesuai</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Penggunaan tidak stabil, panggilan sesekali</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Penggunaan stabil, panggilan kerap</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kelebihan harga</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Harga standard</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lebih murah 20%-50% daripada bayar mengikut penggunaan</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Fleksibiliti</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Boleh guna bila-bila masa, tanpa komitmen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Perlu bayar terlebih dahulu, kuota yang tamat tempoh mungkin luput</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pengendalian lebihan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pengebilan mengikut penggunaan secara automatik</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bertukar kepada pengebilan mengikut penggunaan selepas melebihi kuota</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Platform utama</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Platform API rasmi setiap model</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OpenAI Plus/Pro, Claude Pro, Cursor Pro</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Perbandingan dua cara pengebilan

Bagi pemula, disyorkan bermula dengan bayar mengikut penggunaan — tidak perlu bayar terlebih dahulu, guna berapa bayar sepenuhnya. Apabila penggunaan bulanan anda stabil pada satu tahap (contohnya melebihi 50 yuan sebulan), barulah pertimbangkan bertukar kepada langganan pakej untuk mendapatkan harga unit lebih rendah.

##### 2. Sekilas Pandang Pakej Langganan Utama

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Pakej</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Yuran bulanan</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Kandungan termasuk</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Sesuai untuk</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ChatGPT Free</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Percuma</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sembang teks tanpa had dengan GPT-5.6 Luna</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pengalaman tanpa asas</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ChatGPT Plus</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$20/bulan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GPT-5.6 Sol, penjanaan imej, analisis data, akses sambungan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pengguna sederhana</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ChatGPT Pro</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$200/bulan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Penggunaan semua model tanpa had, akses keutamaan ciri baharu</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pengguna profesional berat</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Free</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Percuma</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sembang Claude dengan bilangan terhad</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pengalaman tanpa asas</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Claude Pro</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$20/bulan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Penggunaan Claude tanpa had, akses keutamaan model baharu</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pembangun pengaturcaraan</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cursor Free</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Percuma</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pelengkapan dan sembang AI dengan bilangan terhad</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pengalaman pemula</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cursor Pro</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$20/bulan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pelengkapan AI tanpa had, 500 permintaan premium sebulan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pembangun harian</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cursor Business</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">US$40/bulan/orang</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kerjasama pasukan, papan kawalan admin, mod privasi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Penggunaan pasukan</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Pakej langganan alat AI utama (Ogos 2026)

Pelan langganan model di China agak berbeza. DeepSeek terutamanya mengebil mengikut penggunaan dan tidak mempunyai pakej langganan bulanan — anda top up dan caj dibuat mengikut penggunaan sebenar. Tongyi Qianwen menyediakan pakej sumber prabayar di platform Bailian (membeli kuota Token tertentu dengan harga diskaun). Doubao juga mempunyai pelan prabayar serupa di Volcengine. Bagi pembangun di China, gabungan paling ekonomi lazimnya ialah: DeepSeek bayar mengikut penggunaan (pembangunan harian) + kuota percuma Doubao (uji rasa).

##### 3. Platform Agregasi API

Jika anda perlu menggunakan beberapa model serentak, platform agregasi API ialah pilihan yang menjimatkan kerumitan. Platform agregasi menyediakan satu API Key bersatu, dan anda boleh memanggil berpuluh model di seluruh dunia tanpa perlu mendaftar berasingan di setiap platform.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Platform</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ciri</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Kelebihan harga</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Senario sesuai</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OpenRouter (openrouter.ai)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Platform agregasi luar negara; satu Key untuk memanggil model seluruh dunia</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Harga telus; menyokong perbandingan harga masa nyata</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mahu bertukar antara pelbagai model luar negara secara fleksibel</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SiliconFlow (siliconflow.cn)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Platform agregasi tempatan; menyediakan API pelbagai model buatan China</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lebih murah 20%-30% daripada harga rasmi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pembangun tempatan yang mahu membanding harga pelbagai model</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Azure OpenAI (proksi Microsoft)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">API OpenAI melalui proksi Azure milik Microsoft</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Batch API boleh dapat diskaun 50%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Panggilan OpenAI peringkat perusahaan; tugasan tak segerak dalam kuantiti besar</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Baidu Qianfan (qianfan.baidubce.com)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Platform awan AI Baidu, menyediakan model seperti ERNIE</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kredit percuma untuk pengguna baharu</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pengguna ekosistem Baidu</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Platform pengagregatan API arus utama (Ogos 2026)

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Peringatan elak perangkap: jangan beli "Key kongsi"

{class="mt-1"}
Jangan membeli API Key "kongsi" yang kononnya murah di platform seperti Taobao atau Xianyu — Key ini biasanya berasal dari sumber yang tidak jelas, boleh disekat pada bila-bila masa, dan membawa risiko kebocoran data. Sentiasa dapatkan API Key melalui platform rasmi atau platform pengagregatan yang sah.
:::

##### 4. Strategi pengoptimuman kos

Memilih model yang betul hanyalah langkah pertama; cara "menggunakannya secara jimat" sama pentingnya. Berikut ialah beberapa strategi pengoptimuman kos yang telah terbukti dalam amalan:

1. Guna sepenuhnya cache hit. Banyak model menyediakan fungsi "cache" — apabila permintaan anda mengandungi kandungan yang telah diproses sebelum ini (contohnya arahan sistem), bahagian itu dibilkan pada harga yang sangat rendah. Harga cache hit DeepSeek hanya 1/60 daripada harga biasa. Letakkan arahan sistem yang tetap di awal senarai mesej untuk memaksimumkan cache hit.
2. Penghalaan berperingkat — gunakan model murah untuk tugasan mudah dan model mahal untuk tugasan kompleks. Contohnya, gunakan DeepSeek V4 Flash untuk klasifikasi teks (output 2 yuan/sejuta Token) dan Claude untuk reka bentuk seni bina (output 181 yuan/sejuta Token). Dalam sesuatu projek, 80% daripada panggilan boleh menggunakan model murah.
3. Hadkan panjang output. API dibilkan mengikut Token output; makin panjang output, makin mahal. Dalam situasi yang tidak memerlukan huraian panjang lebar, tetapkan parameter max_tokens untuk mengehadkan panjang output dan elakkan AI "bercakap berbelit".
4. Gunakan Batch API untuk tugasan bukan masa nyata. Jika anda mempunyai banyak tugasan yang tidak memerlukan respons segera (contohnya pelabelan data secara pukal atau ringkasan dokumen), gunakan Batch API untuk menikmati diskaun 50%. OpenAI dan Azure kedua-duanya menyediakan fungsi ini.
5. Pantau penggunaan Token. Kebanyakan platform API menyediakan papan pemuka statistik penggunaan. Semak taburan penggunaan secara berkala, kenal pasti panggilan yang paling banyak menghabiskan Token, dan buat pengoptimuman secara bersasar. Satu pelarasan kecil pada Prompt (contohnya menukar "sila jelaskan dengan terperinci" kepada "sila jelaskan dalam 3 ayat") boleh menjimatkan sehingga 50% Token.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Strategi pengoptimuman</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Jumlah penjimatan</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Tahap kesukaran pelaksanaan</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Penjelasan</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cache hit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sehingga 98%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Rendah</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Letakkan kandungan tetap di awal mesej</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Penghalaan berperingkat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">50%-80%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sederhana</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Guna model murah untuk tugasan mudah</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Hadkan panjang output</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">30%-60%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Rendah</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tetapkan parameter max_tokens</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Batch API</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">50%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Rendah</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Guna pemprosesan kelompok untuk tugasan bukan masa nyata</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pengoptimuman Prompt</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">20%-50%</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sederhana</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ringkaskan Prompt, kurangkan lebihan</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Strategi pengoptimuman kos dan kesannya (Ogos 2026)

#### 6. Amalan praktikal: menyepadukan API model besar ke dalam projek

Mari akhiri bab ini dengan satu amalan praktikal yang lengkap — mencipta "Penjana Ringkasan AI": pengguna memasukkan sekeping teks panjang, dan API model besar dipanggil untuk menjana ringkasan. Amalan ini akan menunjukkan aliran lengkap panggilan API: persediaan persekitaran, panggilan API, pengendalian ralat dan kawalan kos.

::: div .code-block
:::inline div .code-head
<span>PYTHON · ai_summarizer.py</span><span class="dots">···</span>
:::

```
# ai_summarizer.py - perumus teks AI
import os
from openai import OpenAI

# 1. Konfigurasi (baca API Key daripada pemboleh ubah persekitaran, jangan sesekali hardcode)
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

def summarize(text: str, max_length: int = 200) -> dict:
    """Merumuskan teks

    Args:
        text: teks asal yang perlu dirumuskan
        max_length: panjang rumusan maksimum (bilangan Token)

    Returns:
        dict: mengandungi rumusan dan maklumat penggunaan Token
    """
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {
                    "role": "system",
                    "content": "Kamu penjana rumusan."
                               "Rumuskan teks yang diberi pengguna secara ringkas."
                               "Rumusan tidak melebihi 3 ayat."
                },
                {
                    "role": "user",
                    "content": f"Rumuskan teks berikut:\n\n{text}"
                }
            ],
            max_tokens=max_length,  # hadkan panjang output
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

# 2. Contoh penggunaan
if __name__ == "__main__":
    long_text = """
    (tampal teks panjang di sini...)
    """

    result = summarize(long_text)

    if result["success"]:
        print(f"Rumusan: {result['summary']}")
        print(f"Token diguna: {result['total_tokens']}")
        # anggaran kos: DeepSeek V4 Flash
        cost = result['total_tokens'] * 0.000004  # kira-kira 0.4 sen per seribu Token
        print(f"Anggaran kos: {cost:.4f} yuan")
    else:
        print(f"Berlaku ralat: {result['error']}")
```
:::

Kod ini mencerminkan beberapa amalan terbaik panggilan API: API Key dibaca melalui pemboleh ubah persekitaran dan tidak pernah dikodkan terus dalam kod; fungsi mempunyai dokumentasi dan petunjuk jenis yang jelas; max_tokens ditetapkan untuk mengehadkan panjang output; temperature ditetapkan pada nilai rendah (0.3) untuk output yang lebih stabil; pengendalian ralat yang lengkap disediakan; dan maklumat penggunaan Token dipulangkan untuk penjejakan kos. Apabila anda meminta AI menulis kod seperti ini, beritahulah keperluan-keperluan ini — ia memang mampu melaksanakannya untuk anda.

:::inline div .quote-line
Pelajaran akhir bab ini: model ialah "peluru", metodologi ialah "taktik". Pilih peluru betul membantu peperangan lebih lancar, tetapi tanpa taktik baik, peluru sebanyak mana pun tidak menang. Selepas mengenali kelebihan setiap model dan cara guna API, anda ada "gudang peluru" yang cukup—tetapi bagaimana memenangkan peperangan tetap bergantung pada metodologi pemikiran yang dipelajari dalam bab-bab sebelumnya.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mari praktik: pastikan panggilan API pertama anda berjaya

{class="mt-1"}
Daftar ke satu platform model tempatan (digalakkan DeepSeek atau Zhipu; kedua-duanya memberi kredit kepada pengguna baharu), cipta API Key, masukkannya ke dalam pemboleh ubah persekitaran sistem (bukan di dalam kod!), kemudian jalankan kod "panggilan API pertama" di atas. Pada saat anda melihat balasan AI tercetak, anda telah melangkau garis sempadan antara "menggunakan AI" dan "membina aplikasi AI".
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan bab ini

- Tiga terkuat antarabangsa: GPT-5.6 (seimbang dan serba boleh), Claude (puncak pengaturcaraan + kadar halusinasi hanya 1%), Gemini (raja multimodal + konteks 2 juta)
- Lima terkuat tempatan: DeepSeek V4 (raja nilai untuk wang; perhatikan pengumuman kenaikan harga), Qwen3.7 (peringkat perusahaan), GLM-5.1 (nombor satu tempatan bagi SWE), Kimi K3 (teks sangat panjang), Doubao (permulaan percuma)
- Kaedah keputusan empat soalan: dilancarkan di mana? Pengaturcaraan atau yang lain? Perlu konteks sangat panjang? Bajet sensitif?
- Token ialah unit bil: 1 aksara Cina kira-kira 1.5-2 Token; 1 juta aksara Cina kira-kira 1.5 juta Token
- API Key = kata laluan dompet anda: urus dengan pemboleh ubah persekitaran; jangan sesekali dikodkan terus, jangan dimuat naik ke Git
- Model tempatan secara umumnya serasi dengan OpenAI SDK: untuk menukar model, hanya dua baris perlu diubah, iaitu api_key dan base_url
- Lima cara jimat: cache hit, penghalaan berperingkat, hadkan output, Batch API, pantau penggunaan
:::
