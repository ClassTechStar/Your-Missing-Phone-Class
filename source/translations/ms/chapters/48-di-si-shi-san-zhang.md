---
id: di-si-shi-san-zhang
num: 43
part: ai-biancheng-pian
nav: Bab 43: Kejuruteraan Perbualan—Teknik Perbualan Berkesan
toc: default
kind: chapter
---

### Bab 43: Kejuruteraan Perbualan — Teknik Berbual untuk Kerjasama Cekap dengan AI

{class="chapter-intro mb-4"}
Perbualan ialah cara interaksi teras dalam pengaturcaraan AI. Tetapi ingat: "berbual" tidak sama dengan "bercakap santai" — perbualan pengaturcaraan AI yang cekap ialah teknik komunikasi berstruktur, dan kita namakan "kejuruteraan perbualan". Ia mengkaji: bagaimana memperoleh output kod berkualiti tertinggi dengan bilangan giliran perbualan paling sedikit. Terus terang, bab ini mengajar anda cara "bercakap jelas" dengan AI.

#### 1. Strategi lapisan Prompt

Perbualan dengan AI boleh dibahagikan kepada tiga lapisan, dan setiap lapisan menjalankan fungsi berbeza. Dengan memahami ketiga-tiga lapisan ini, anda boleh menggabungkan Prompt yang cekap seperti menyusun blok binaan.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Lapisan</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Fungsi</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Contoh</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Kekerapan</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lapisan sistem</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menetapkan peranan AI dan kekangan menyeluruh</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"Anda seorang pakar React; kod mesti ditulis dalam TypeScript"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ditetapkan sekali pada permulaan projek</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lapisan tugasan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menerangkan tugasan khusus yang hendak dibuat semasa ini</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"Bina satu komponen borang yang mengandungi medan nama pengguna dan kata laluan"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Diberikan pada permulaan setiap tugasan</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lapisan maklum balas</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menilai dan membetulkan output AI</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"Medan kata laluan tiada suis papar/sembunyi, sila tambahkan"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Diberikan mengikut kualiti output</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Tiga lapisan Prompt perbualan

Prompt lapisan sistem biasanya ditulis dalam fail memori projek (contohnya CLAUDE.md) dan tidak perlu diulang pada setiap perbualan. Lapisan tugasan ialah yang paling kerap anda gunakan dalam perbualan — ia patut mengandungi tiga unsur: "buat apa", "guna teknologi apa" dan "ada kekangan apa". Lapisan maklum balas paling menguji kemahiran — maklum balas yang baik membolehkan AI membetulkan dengan tepat; maklum balas yang buruk hanya membuatnya meneka semula.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tip: Tiga senjata utama maklum balas

{class="mt-1"}
Templat maklum balas yang praktikal ialah "nyatakan masalah + terangkan jangkaan + berikan konteks". Contohnya: "Pengendalian ralat pada baris 25 hanya menggunakan console.log (nyatakan masalah); persekitaran pengeluaran patut menggunakan pengendali ralat yang seragam dan memulangkan mesej mesra pengguna (terangkan jangkaan); projek ini ada fungsi handleError yang boleh digunakan (berikan konteks)". Maklum balas sebegini sepuluh kali lebih berkesan daripada "ubah sikit pengendalian ralat".
:::

#### 2. Perbualan penyahpepijatan: cara menerangkan ralat supaya AI cepat mengenal pasti

Penyahpepijatan ialah salah satu situasi paling kerap dalam pengaturcaraan AI. Apabila anda menemui bug, cara anda menerangkan masalah kepada AI terus menentukan sama ada ia dapat membantu anda mengenal pasti dan membaikinya dengan cepat. Berikut ialah empat perkara penting dalam perbualan penyahpepijatan:

1. Tunjukkan maklumat asal kepada AI, bukan penerangan ulangan anda. Rujuk terus log ralat, tindanan pengecualian (exception stack) dan kod berkaitan kepada AI menggunakan @, bukan menerangkannya dengan "macam ada ralat entah apa". AI melihat maklumat asal jauh lebih tepat berbanding melihat tafsiran anda.
2. Terangkan perbezaan antara "tingkah laku dijangka" dan "tingkah laku sebenar". "Saya jangka selepas butang diklik ia akan pergi ke halaman utama (dijangka), tetapi sebenarnya selepas diklik halaman langsung tiada tindak balas (sebenar)" — penerangan sedemikian jauh lebih berguna daripada "butang rosak".
3. Berikan langkah penghasilan semula. "Masukkan nama pengguna dahulu, kemudian klik butang log masuk, maka ralat ini akan muncul" — langkah penghasilan semula membolehkan AI mensimulasikan laluan operasi anda, dan lebih mudah mengenal pasti masalah.
4. Nyatakan dengan jelas apa yang telah anda cuba. "Saya sudah semak permintaan rangkaian; ia memulangkan 200 dan data normal" — ini membantu AI mengetepikan arah yang telah disahkan, tanpa membazir masa mengulang siasatan.

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
Penerangan penyahpepijatan yang kurang baik

{class="font-mono text-xs leading-relaxed"}
Butang diklik tiada tindak balas, tolong tengokkan
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
Penerangan penyahpepijatan yang baik

{class="font-mono text-xs leading-relaxed"}
Selepas butang log masuk diklik, halaman langsung tiada tindak balas. Tingkah laku dijangka: selepas diklik, pergi ke halaman /home Tingkah laku sebenar: selepas diklik, langsung tiada tindak balas, konsol tiada ralat Langkah penghasilan semula: 1. Masukkan nama pengguna admin dan kata laluan 123456 di halaman log masuk 2. Klik butang "Log Masuk" 3. Halaman tiada tindak balas Sudah disiasat: - Permintaan rangkaian normal, pulangan 200 - Peristiwa onClick telah diikat - Kod komponen LoginButton telah disemak Fail berkaitan: @src/components/LoginButton.tsx @src/pages/Login.tsx
:::
:::

#### 3. Strategi iterasi: langkah kecil pantas vs refaktor besar-besaran

Iterasi dalam pengaturcaraan AI mempunyai dua strategi asas, sesuai untuk situasi berbeza. Memahami perbezaannya membantu anda membuat pilihan yang betul dalam keadaan berbeza.

Strategi "langkah kecil pantas" sesuai untuk pembangunan fungsi dan pembaikan bug. Intipatinya: setiap kali, minta AI membuat satu ubah suai kecil sahaja, dan buat yang berikutnya selepas pengesahan lulus. Kelebihannya: setiap langkah boleh disahkan dan boleh dikembalikan, risiko terkawal; kekurangannya: kelajuan lebih perlahan dan memerlukan interaksi perbualan yang kerap. Sesuai untuk: pembangunan fungsi baharu, penerokaan ketika tidak pasti penyelesaian optimum, dan iterasi berhati-hati ketika kurang yakin dengan output AI.

Strategi "refaktor besar-besaran" sesuai untuk ubah suai berskala besar apabila sasaran sudah jelas. Intipatinya: terangkan sasaran lengkap sekali gus, dan biarkan AI merancang serta melaksanakan keseluruhan ubah suai secara autonomi. Kelebihannya: kelajuan tinggi; AI dapat melihat gambaran menyeluruh untuk membuat keputusan seni bina yang lebih baik. Kekurangannya: risiko tinggi; jika tafsiran AI tersasar, kos pembetulan besar. Sesuai untuk: naik taraf seni bina yang jelas, migrasi kod berskala besar dan refaktor yang dijamin dengan ujian secukupnya.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Dimensi</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Langkah kecil pantas</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Refaktor besar-besaran</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Jumlah ubah suai setiap kali</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Satu fungsi atau satu bug</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Satu modul atau satu lapisan seni bina</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kekerapan pengesahan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Disahkan serta-merta selepas setiap ubah suai</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Disahkan serentak selepas semua ubah suai selesai</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bilangan giliran perbualan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Banyak (5-10 giliran/fungsi)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sedikit (1-3 giliran/modul)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Risiko</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Rendah; setiap langkah boleh dikembalikan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tinggi; kos pembetulan sisihan besar</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Situasi sesuai</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Fungsi baharu, pembangunan penerokaan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Refaktor dan migrasi bersasaran jelas</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Prasyarat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tiada keperluan khas</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Perlu ada liputan ujian</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Perbandingan dua strategi iterasi

Dalam amalan, kedua-dua strategi sering digunakan secara bergabung. Contohnya, semasa refaktor satu modul, gunakan dahulu "refaktor besar-besaran" untuk meminta AI mengemukakan pelan menyeluruh; selepas pelan disemak, gunakan "langkah kecil pantas" untuk melaksanakannya langkah demi langkah. Dengan itu, perspektif menyeluruh dijamin dan risiko pelaksanaan terkawal.

#### 4. Pengurusan konteks bagi perbualan berbilang giliran

Seiring bertambahnya bilangan giliran perbualan, anda perlu menguruskan konteks perbualan secara proaktif untuk mengelakkan masalah "AI terlupa maklumat awal". Berikut ialah beberapa teknik pengurusan konteks yang praktikal.

Pertama, "sauhkan" maklumat penting. Pada permulaan perbualan, tuliskan kekangan penting dengan jelas, dan ulanginya semula pada masa yang sesuai dalam perbualan seterusnya. Contohnya "ingat, data kita disimpan dalam localStorage, tidak boleh guna pangkalan data" — ulangkan kekangan ini dalam permintaan ubah suai yang berkaitan untuk mengelakkan AI terlupa.

Kedua, gunakan dengan bijak teknik "ringkasan-sambungan". Apabila perbualan menjadi sangat panjang, minta AI "meringkaskan kemajuan setakat ini dan senarai tugas yang belum selesai", kemudian buka perbualan baharu dengan ringkasan itu sebagai titik permulaan. Dengan itu, konteks penting dikekalkan dan kemerosotan perbualan panjang dielakkan.

Ketiga, "satu perbualan satu tugasan". Ini strategi pengurusan konteks paling mudah dan juga paling berkesan. Setiap perbualan hanya mengendalikan satu tugasan atau satu fungsi; selepas selesai, buka perbualan baharu untuk yang berikutnya. Ini secara semula jadi mengehadkan panjang perbualan dan mengekalkan kejelasan konteks.

Keempat, manfaatkan fungsi pengurusan konteks pada alat. Kebanyakan alat pengaturcaraan AI mempunyai butang "kosongkan konteks" atau "sesi baharu" — apabila anda berasa kualiti jawapan AI menurun, jangan teragak-agak, buka sesi baharu. Kehilangan sebahagian sejarah perbualan jauh lebih baik daripada terus berjuang dalam konteks yang telah merosot.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mari praktik: menjadi "pesakit" untuk AI anda sekali

{class="mt-1"}
Sengaja bina satu halaman kecil di dalam pelayar dan ciptakan satu bug (contohnya butang tiada tindak balas). Kemudian, mengikut format "penerangan penyahpepijatan yang baik" dalam bab ini, terangkan kepada AI secara lengkap sekali: maklumat asal, dijangka vs sebenar, langkah penghasilan semula dan perkara yang sudah disiasat. Rasakan perbezaan kelajuan AI mengenal pasti masalah — anda akan memahami mengapa "menerangkan masalah" itu sendiri satu kemahiran.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan bab ini

- Tiga lapisan Prompt: lapisan sistem (ditulis dalam fail memori), lapisan tugasan (buat apa + teknologi + kekangan), lapisan maklum balas (nyatakan masalah + jangkaan + konteks)
- Empat perkara penting penyahpepijatan: beri maklumat asal, dijangka vs sebenar, langkah penghasilan semula, perkara sudah disiasat
- Langkah kecil pantas: risiko rendah giliran banyak, sesuai untuk fungsi baharu; refaktor besar-besaran: risiko tinggi giliran sedikit, perlukan jaminan ujian
- Empat teknik pengurusan konteks: sauhkan maklumat penting, ringkasan-sambungan, satu perbualan satu tugasan, buka sesi baharu dengan tegas
:::
