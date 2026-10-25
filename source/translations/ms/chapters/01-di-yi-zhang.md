---
id: di-yi-zhang
num: 01
part: ji-chu-pian
nav: Bab 1: Hai, Komputer Peribadi Saya
toc: default
kind: chapter
---

### Bab 1: Hello, Komputer Peribadi Saya

{class="chapter-intro mb-4"}
Telefon anda sebenarnya adalah komputer super peribadi dalam poket anda. Ia jauh lebih hebat berjuta kali ganda daripada komputer yang pernah mendaratkan manusia di bulan, namun berdiam diri di tapak tangan anda. Hari ini, mari kita kenali "gergasi senyap" ini dengan baik.

#### I. "Organ Dalam" Perkakasan Telefon: Analisis Mendalam

Telefon walaupun kecil, organ lengkap. Mari kita kenali komponen-komponen tepat ini satu demi satu seperti kelas anatomi.

##### 1. SoC (System on Chip): "Otak + Jantung" Telefon

SoC adalah singkatan System on Chip, diterjemahkan sebagai "keseluruhan sistem dimasukkan ke dalam satu cip". Ia bukan sahaja CPU (Pemproses Pusat), tetapi mengintegrasikan CPU, GPU (Pemproses Grafik), NPU (Pemproses Neural), ISP (Pemproses Isyarat Imej), baseband (bertanggungjawab untuk komunikasi) dan lain-lain semuanya bersama.

Ini seperti membina bangunan kerajaan bandar, loji kuasa, pusat komunikasi, balai polis semua dalam satu bangunan, kecekapan sangat tinggi.

##### CPU: Teras Pengiraan Universal

CPU adalah komponen paling teras dalam SoC, bertanggungjawab mengendalikan kebanyakan tugas pengiraan. CPU telefon menggunakan seni bina ARM, berbeza dengan seni bina x86 komputer, seni bina ARM menggunakan set arahan ringkas (RISC) sebagai ciri, penggunaan kuasa lebih rendah, lebih sesuai untuk peranti mudah alih.

<strong>Reka bentuk saiz teras CPU</strong>: CPU telefon moden secara umum menggunakan seni bina "besar-kecil" (teknologi big.LITTLE ARM), membahagikan teras kepada tahap prestasi berbeza:

- <strong>Teras super besar/teras besar</strong>: Prestasi paling kuat, bertanggungjawab untuk tugas berat. Seperti muat turun permainan, pelancaran aplikasi, pengiraan kompleks. Frekuensi tertinggi (3GHz+), tetapi penggunaan kuasa juga paling besar.
- <strong>Teras sederhana</strong>: Imbangan prestasi dan penggunaan kuasa, mengendalikan tugas beban sederhana harian. Menyapu Weibo, menonton video, bertukar pelbagai tugas bergantung kepadanya.
- <strong>Teras kecil/teras kecekapan</strong>: Penggunaan kuasa paling rendah, mengendalikan tugas latar belakang ringan. Mod sedia, mendengar muzik, menerima mesej dan lain-lain, hampir tidak menggunakan kuasa.

Tiga tahap teras bekerjasama: penjadual sistem mengikut beban tugas menguntukkan secara automatik — tugas ringan diberikan kepada teras kecil untuk menjimatkan kuasa, kerja berat diberikan kepada teras besar untuk berkuasa, selepas selesai bertukar kembali ke teras kecil. Inilah sebabnya telefon boleh bermain permainan dengan lancar dan juga sedia satu hari penuh.

<strong>Ciri seni bina setiap jenama</strong>:

- <strong>Qualcomm Snapdragon 8 Elite</strong>: Menggunakan seni bina CPU Oryon buatan sendiri (diperolehi dari pengambilalihan Nuvia), 2 teras super (4.32GHz) + 6 teras prestasi (3.53GHz), semuanya berdasarkan proses 3nm generasi kedua TSMC. Sepenuhnya meninggalkan seni bina awam ARM, prestasi teras tunggal dan berbilang teras mencapai peningkatan melompat. GPU ialah Adreno 830, menggunakan seni bina kepingan, prestasi grafik meningkat 40%, Hexagon NPU kuasa pengiraan kira-kira 45 TOPS, prestasi inferens AI meningkat 45%. (Nota: Versi tersuai Galaxy Samsung mempunyai frekuensi lebih tinggi, teras super boleh mencapai 4.47GHz.)
- <strong>MediaTek Dimensity 9400</strong>: 1 teras super besar (Cortex-X925, 3.62GHz) + 3 teras prestasi (Cortex-X4, 3.3GHz) + 4 teras kecekapan (Cortex-A720, 2.4GHz), seni bina semua teras besar diteruskan, proses 3nm generasi kedua TSMC. GPU ialah Immortalis-G925 (12 teras), prestasi puncak meningkat 41%, prestasi penjejakan sinar meningkat 40%. Pemproses AI ialah NPU 890 generasi kelapan, menyokong operasi model besar sisi peranti, latihan LoRA sisi peranti dan penjanaan video sisi peranti.
- <strong>Apple A18 Pro</strong>: 2 teras prestasi (kira-kira 4.04GHz) + 4 teras kecekapan (kira-kira 2.4GHz), proses 3nm generasi kedua TSMC. GPU 6 teras menyokong penjejakan sinar tahap perkakasan, NPU 16 teras (kira-kira 35 TOPS) menyediakan kuasa pengiraan yang kuat untuk AI sisi peranti dan Apple Intelligence. Seni bina buatan sendiri Apple masih memimpin dalam prestasi teras tunggal dan nisbah kecekapan, seni bina ingatan bersatu menyediakan kelebihan lebar jalur tinggi untuk inferens AI.
- <strong>Huawei Kirin 9020</strong>: Dipasang pada siri Mate 70, menggunakan seni bina CPU Taishan buatan sendiri, keupayaan NPU dan ISP terus diperkuat, menyokong 5.5G dan komunikasi satelit, mewakili kejayaan terbaru cip domestik.

##### GPU: Enjin Pemaparan Grafik

GPU (Graphics Processing Unit) khusus bertanggungjawab untuk tugas grafik dan pengiraan selari. Bilangan terasnya jauh lebih banyak daripada CPU (mudah beratus-ratus ribu teras), tetapi fungsi setiap teras agak mudah, sesuai untuk memproses sejumlah besar pengiraan serupa secara serentak.

<strong>Aliran pemaparan grafik</strong>:

1. <strong>Pemprosesan bucu</strong>: Mengira koordinat kedudukan setiap bucu dalam model 3D.
2. <strong>Rasterisasi</strong>: Menukar grafik 3D kepada piksel pada skrin 2D.
3. <strong>Bayang piksel</strong>: Mengira warna, tekstur, kesan pencahayaan untuk setiap piksel.
4. <strong>Penggabungan output</strong>: Menggabungkan semua lapisan menjadi gambar akhir, dihantar ke skrin untuk dipaparkan.

<strong>Pengaruh GPU terhadap penggunaan harian</strong>: Bukan sahaja permainan! Luncuran antara muka, kesan animasi, main balik video, penapis foto, aplikasi AR semuanya bergantung kepada GPU. Telefon dengan GPU lemah, luncuran antara muka mungkin kehilangan bingkai, permainan langsung tersekat.

<strong>GPU setiap jenama</strong>: Qualcomm menggunakan GPU Adreno buatan sendiri; MediaTek menggunakan GPU ARM Mali; Apple menggunakan GPU buatan sendiri, prestasi dan kecekapan adalah penanda aras industri.

##### NPU: Enjin Pecutan AI

NPU (Neural Processing Unit) adalah pemproses yang direka khusus untuk operasi rangkaian neural. Berbanding dengan CPU dan GPU, NPU lebih cekap dan penggunaan kuasa lebih rendah apabila memproses tugas AI.

<strong>Cara operasi rangkaian neural</strong>: Operasi teras NPU ialah pendaraban matriks dan operasi konvolusi — inilah pengiraan paling asas dan paling kerap dalam rangkaian neural. NPU melalui pengoptimuman tahap perkakasan, boleh memproses sejumlah besar operasi matriks secara selari, kelajuan puluhan kali lebih cepat daripada CPU, tetapi penggunaan kuasa jauh lebih rendah.

<strong>Aliran pemprosesan AI</strong>:

1. <strong>Input data</strong>: Imej kamera, audio mikrofon, data sensor dan lain-lain.
2. <strong>Prapemprosesan</strong>: Melaraskan format dan saiz data, menyesuaikan keperluan input rangkaian neural.
3. <strong>Pengiraan inferens</strong>: NPU memuatkan model yang dilatih, melakukan pengiraan maju ke atas data input, menghasilkan output.
4. <strong>Pascapemprosesan</strong>: Menukar output AI kepada hasil yang boleh digunakan, seperti koordinat muka, kandungan teks, label adegan.

<strong>Senario aplikasi sebenar</strong>:

- <strong>Fotografi pengiraan</strong>: Sintesis waktu malam, kabur potret, pemprosesan HDR, kecantikan AI.
- <strong>Pembantu suara</strong>: Pengecaman suara, pemahaman bahasa semula jadi, sintesis suara.
- <strong>Terjemahan masa nyata</strong>: Sari kata AI, terjemahan perbualan.
- <strong>Pengecaman pintar</strong>: Pengecaman teks (OCR), pengecaman objek, pengecaman adegan.
- <strong>Model besar sisi peranti</strong>: Cip perdana terkini telah menyokong operasi model AI besar kecil (aras parameter 7B) di sisi peranti, merealisasikan dialog AI luar talian, ringkasan dokumen, penulisan pintar dan lain-lain. Hexagon NPU Snapdragon 8 Elite mempunyai kuasa pengiraan kira-kira 45 TOPS, NPU 890 Dimensity 9400 juga menyokong model besar sisi peranti (kelajuan inferens LLM meningkat 80%), NPU 16 teras A18 Pro Apple menyediakan kuasa pengiraan kira-kira 35 TOPS.
- <strong>Pemprosesan imej AI</strong>: Penyingkiran AI (buang pelakon dalam foto dengan satu ketik), pengembangan gambar AI (memperluas sempadan imej), penukaran gaya AI, penjanaan gambar teks dan lain-lain.

##### ISP: Pemproses Isyarat Imej

ISP memproses data mentah dari kamera, menukar isyarat cahaya kepada gambar yang cantik.

<strong>Bagaimana menilai prestasi?</strong> Lihat modelnya! Apple A18 Pro, Qualcomm Snapdragon 8 Elite, MediaTek Dimensity 9400, Huawei Kirin 9020 semuanya tahap perdana. Pertengahan lihat Snapdragon 8s Gen3/7+ Gen3, Dimensity 8400. Jangan hanya lihat bilangan teras, seni bina dan proses (nombor nanometer) lebih penting. Proses 3nm adalah paling maju kini, nisbah kecekapan jauh lebih baik daripada 5nm dan 4nm.

##### 2. RAM (Ingatan Akses Rawak): Meja Kerja Sementara

RAM seperti meja pejabat anda, lebih besar, lebih banyak fail boleh dibuka serentak. 12GB adalah arus perdana sekarang, 16GB sesuai untuk pengguna berat, 24GB ke atas adalah pilihan pemain permainan dan geek.

Jenis RAM juga penting: LPDDR5 lebih cepat dan lebih menjimatkan kuasa daripada LPDDR4X. Walaupun RAM Apple tidak besar, pengoptimuman sistem baik, jadi nampak "cukup".

<strong>Apakah yang berlaku jika RAM tidak mencukupi?</strong> App akan dibunuh oleh sistem di latar belakang, perlu muat semula apabila bertukar. Inilah sebabnya kadang-kadang bertukar WeChat kembali, permainan sudah hilang.

##### 3. Storan (ROM/Flash Memory): Gudang Jangka Panjang

Storan seperti rak buku anda, tempat semua gambar, video, App disimpan. Arus perdana kini ialah UFS 3.1 atau UFS 4.0, kelajuan beberapa kali ganda lebih cepat daripada eMMC lama.

<strong>Mengapa kelajuan storan penting?</strong> Ia menentukan kelajuan pembukaan App, kelajuan muat turun permainan, kelajuan penyimpanan gambar. Selepas digunakan lama, storan perlahan akan menjadikan telefon semakin tersekat.

##### 4. Skrin: Mata Anda

Skrin adalah tetingkap utama interaksi antara anda dan telefon, kualiti secara langsung mempengaruhi pengalaman.

- <strong>Bahan</strong>: OLED warna cerah, kontras tinggi, lebih menjimatkan kuasa (apabila memaparkan hitam piksel tidak memancar), tetapi pada kecerahan rendah mungkin ada kelipan frekuensi yang merosakkan mata; LCD lebih melindungi mata, kos rendah, tetapi kontras dan warna tidak sebaik OLED.
- <strong>Resolusi</strong>: 1080P adalah arus perdana, 2K lebih jelas tetapi lebih menggunakan kuasa. Konsep "skrin retina" Apple ialah: pada jarak tertentu, mata manusia tidak dapat membezakan piksel.
- <strong>Kadar segar semula</strong>: 60Hz adalah standard, 90Hz/120Hz lebih lancar, luncuran seperti sutera. Kadar segar semula tinggi menggunakan kuasa, jadi banyak telefon menyokong kadar segar semula adaptif (LTPO), laraskan secara dinamik mengikut kandungan.
- <strong>Kadar persampelan sentuh</strong>: Mempengaruhi kelajuan tindak balas sentuh, pemain permainan perlu ambil perhatian, semakin tinggi semakin responsif.
- <strong>Kaedah peredupan</strong>: Peredupan DC lebih melindungi mata daripada peredupan PWM, pada kecerahan rendah tidak mudah penat mata. Kini banyak telefon menyokong peredupan PWM frekuensi tinggi, juga untuk melindungi mata.

##### Teknologi HDR Skrin

HDR (High Dynamic Range) membolehkan skrin memaparkan bahagian terang yang lebih terang dan bahagian gelap yang lebih gelap serentak, rasa hierarki gambar meningkat dengan ketara.

- <strong>Prinsip pelaksanaan</strong>: Julat kecerahan skrin biasa terhad (SDR), jurang antara paling terang dan paling gelap tidak cukup besar. Skrin HDR mempunyai kecerahan puncak lebih tinggi (biasanya 1000 nit ke atas), kontras lebih besar, gamut warna lebih luas, boleh memaparkan lebih banyak butiran.
- <strong>Standard arus perdana</strong>: HDR10 (paling asas, sumber terbuka percuma), HDR10+ (dipromosikan oleh Samsung, metadata dinamik), Dolby Vision (kualiti gambar terbaik tetapi memerlukan kebenaran). Standard yang disokong telefon bergantung kepada perkakasan skrin dan kebenaran sistem.
- <strong>Kesan sebenar</strong>: Apabila menonton video HDR, cahaya matahari lebih menyilaukan, bayang lebih dalam, warna lebih kaya. Prasyaratnya video itu sendiri dibuat HDR, skrin juga menyokong paparan HDR.

##### Teknologi HDR Imej

HDR semasa mengambil gambar dan HDR skrin adalah dua perkara berbeza. HDR imej adalah menyelesaikan masalah "bahagian terang terlebih dedahan, bahagian gelap hitam mati" melalui algoritma.

- <strong>Prinsip algoritma</strong>: Apabila menekan butang pengatup, telefon sebenarnya mengambil beberapa gambar dengan dedahan berbeza (kurang dedahan mengekalkan butiran bahagian terang, terlebih dedahan mengekalkan butiran bahagian gelap, dedahan normal mengekalkan nada tengah), kemudian menggabungkannya menjadi satu gambar julat dinamik tinggi.
- <strong>Aliran pemprosesan</strong>: Tangkapan pelbagai bingkai → pampasan jajaran (anti-goyangan tangan) → penggabungan dedahaan/pemetaan nada → pembetulan warna → output gambar akhir.
- <strong>Pengoptimuman kesan</strong>: Telefon kini telah mencapai "HDR masa nyata" — gambar yang dilihat dalam viewfinder adalah kesan selepas pemprosesan HDR, apa yang dilihat adalah apa yang diperolehi. Smart HDR Apple dan HDR automatik Android sangat matang.

##### 5. Bateri dan Pengecasan: Sumber Tenaga

Bateri adalah komponen paling "berumur pendek" telefon, digunakan dua tiga tahun akan jelas menua. Kapasiti arus perdana kini 5500-7500mAh.

- <strong>Kuasa pengecasan</strong>: Kem Android telah bergolak hingga 100W malah 200W, penuh dalam lebih sepuluh minit; Apple masih berkisar 20-30W. Pengecasan pantas merosakkan bateri? Gunakan aksesori asli tiada masalah besar, telefon mempunyai perlindungan kawalan suhu.
- <strong>Pengecasan wayarles</strong>: Mudah tetapi kecekapan rendah, haba banyak. Sesuai untuk pengecasan sewenang-wenangnya di pejabat, tidak sesuai apabila tergesa-gesa keluar.
- <strong>Pengecasan songsang</strong>: Telefon menjadi power bank, mengecas fon kepala, jam tangan, untuk kecemasan.

##### 6. Kamera: Sihir Cahaya dan Bayang

Telefon kini mudah mempunyai tiga empat kamera, masing-masing dengan pembahagian kerja:

- <strong>Kamera utama</strong>: Paling kerap digunakan, sensor terbesar, kualiti gambar terbaik.
- <strong>Sudut ultra luas</strong>: Mengambil gambar landskap, bangunan, medan pandang lebih luas.
- <strong>Telefoto</strong>: Mengambil gambar jauh, ada zoom optik dan zoom digital.
- <strong>Makro</strong>: Mengambil gambar objek kecil pada jarak sangat dekat.

<strong>Bilangan piksel bukan segalanya!</strong> Saiz sensor (sensor besar menekan sensor kecil), saiz bukaan (f/1.8 lebih besar daripada f/2.4), anti-goyangan (OIS anti-goyangan optik sangat penting) semuanya mempengaruhi kualiti gambar. Fotografi pengiraan (algoritma AI) semakin penting kini, boleh menggabungkan beberapa gambar menjadi satu gambar yang baik.

##### Lens Telefoto Periskop

Lens telefoto tradisional memerlukan laluan optik yang panjang, akan menjadikan telefon sangat tebal. Telefoto periskop melalui prisma 90 darjah membengkokkan cahaya, membolehkan laluan cahaya berkembang melintang di dalam telefon, dengan itu mencapai zoom optik 5x malah 10x sambil mengekalkan telefon nipis.

- <strong>Prinsip struktur</strong>: Cahaya masuk dari lensa → prisma membengkok 90 darjah → melintasi kumpulan lensa sepanjang lebar telefon → sampai ke sensor. Setara dengan meletakkan teleskop menegak secara mendatar.
- <strong>Ciri optik</strong>: Gandaan zoom optik tinggi (5x-10x), kualiti gambar jauh lebih baik daripada zoom digital. Tetapi saiz sensor biasanya lebih kecil daripada kamera utama, prestasi cahaya malap secara umum.
- <strong>Kelebihan pengimejan</strong>: Mengambil gambar bulan, bangunan jauh, gambar rapat pentas, adalah yang tidak dapat dicapai oleh telefon biasa.

##### OIS Anti-goyangan Optik vs EIS Anti-goyangan Elektronik

Anti-goyangan adalah teknologi utama yang mempengaruhi kualiti gambar dan rakaman video, prinsip dua kaedah berbeza sepenuhnya:

- <strong>OIS (anti-goyangan optik)</strong>: Melalui pergerakan fizikal lensa atau sensor untuk mengimbangi goyangan tangan. Lensa mempunyai giroskop mikro dalaman untuk mengesan arah dan amplitud goyangan, kemudian memandu motor untuk menggerakkan kumpulan lensa secara songsang. Kelebihannya tidak kehilangan kualiti gambar, kelemahannya kos tinggi, mengambil ruang.
- <strong>EIS (anti-goyangan elektronik)</strong>: Melalui algoritma perisian memotong dan mengimbangi gambar untuk mengimbangi goyangan. Telefon merakam julat gambar yang sedikit lebih besar, kemudian mengikut data giroskop memotong kawasan yang stabil. Kelebihannya tidak memerlukan perkakasan tambahan, kelemahannya akan memotong gambar (medan pandang menjadi kecil), mungkin kabur dalam cahaya malap.
- <strong>Pilihan sebenar</strong>: Mengambil gambar utamakan OIS, merakam video gabungan kedua-dua paling baik. Kini banyak telefon perdana menyokong "Sensor-Shift" anti-goyangan anjakan sensor, lebih baik daripada anti-goyangan lensa tradisional.

##### Zoom Optik vs Zoom Digital

- <strong>Zoom optik</strong>: Melalui pergerakan fizikal kumpulan lensa menukar jarak fokus, kualiti gambar tidak hilang. Zoom optik pada telefon biasanya hanya gandaan tetap (seperti 2x, 3x, 5x, 10x), tidak boleh zoom berterusan seperti kamera.
- <strong>Zoom digital</strong>: Memperbesar kawasan tengah gambar, pada asasnya pemotongan + interpolasi pembesaran. Semakin banyak pembesaran, semakin teruk kualiti gambar. Zoom digital 100x nampak sangat hebat, tetapi kualiti gambar sebenar sudah sangat kabur.
- <strong>Zoom campuran</strong>: Menggabungkan optik dan digital, menggunakan algoritma sintesis pelbagai bingkai untuk mengimbangi kehilangan kualiti gambar antara gandaan zoom optik. Kesannya lebih baik daripada digital tulen, tetapi masih tidak sebaik optik.

##### Audio: Pembesar Suara dan Cip Paparan Berasingan

<strong>Pembesar suara tunggal vs pembesar suara berganda</strong>:

- <strong>Pembesar suara tunggal</strong>: Hanya satu unit pembesar suara di bahagian bawah, bunyi cenderung ke satu sisi, tiada rasa stereo. Telefon pertengahan hingga bawah biasa.
- <strong>Pembesar suara berganda (stereo)</strong>: Pembesar suara di bahagian atas dan bawah, membentuk medan bunyi stereo. Menonton video, mendengar muzik saluran kiri kanan jelas, rasa imersif jauh lebih kuat. Earpiece juga berfungsi sebagai pembesar suara atas adalah skim biasa.
- <strong>Perbezaan kualiti bunyi</strong>: Pembesar suara berganda bukan sahaja "bunyi lebih kuat", kuncinya rasa ruang dan rasa hierarki. Menonton filem dengan pembesar suara tunggal, selalu rasa kurang sesuatu.

<strong>Cip paparan berasingan telefon permainan</strong>:

Sesetengah telefon permainan dan telefon prestasi dilengkapi dengan cip pemprosesan paparan berasingan, fungsinya:

- <strong>Penyisipan bingkai</strong>: Menyisipkan bingkai permainan 30fps kepada 60fps atau 120fps melalui algoritma, gambar lebih lancar. Proses ini dilakukan pada cip paparan berasingan, tidak menggunakan sumber GPU SoC.
- <strong>Super resolusi</strong>: Meningkatkan gambar resolusi rendah kepada resolusi tinggi melalui algoritma AI, kualiti gambar lebih jelas.
- <strong>Mengurangkan penggunaan kuasa</strong>: Kerana penyisipan bingkai dan super resolusi dikendalikan oleh cip paparan berasingan, beban SoC berkurang, haba dan penggunaan kuasa berkurang, permainan lebih stabil.

##### Penentuan GPS: Frekuensi Tunggal dan Frekuensi Berganda

Penentuan telefon terutamanya bergantung kepada sistem navigasi satelit seperti GPS.

- <strong>GPS frekuensi tunggal</strong>: Hanya menerima isyarat jalur L1, ketepatan penentuan kira-kira 3-5 meter. Cukup di kawasan terbuka, tetapi di ngarai bandar dengan bangunan tinggi, pantulan isyarat akan menyebabkan anjakan penentuan yang besar.
- <strong>GPS frekuensi berganda</strong>: Menerima isyarat dua jalur L1 dan L5 serentak. Jalur L5 mempunyai panjang gelombang lebih panjang, keupayaan anti-gangguan lebih kuat, pengiraan gabungan frekuensi berganda boleh menghapuskan kebanyakan ralat ionosfera, ketepatan penentuan boleh mencapai 1-3 meter. Kelebihan jelas apabila navigasi bandar, penentuan teksi.
- <strong>Sokongan pelbagai buruj</strong>: Telefon moden bukan sahaja menyokong GPS, tetapi juga menyokong BeiDou (China), GLONASS (Rusia), Galileo (Eropah) dan pelbagai sistem satelit. Semakin banyak satelit disambungkan serentak, semakin cepat dan tepat penentuan.

##### 7. Sensor: Antena Kecil Telefon

Telefon menyembunyikan lebih sedozen sensor, bekerja senyap:

- <strong>Pemecut + Giroskop</strong>: Mengesan postur telefon, bermain permainan stereng, auto putar skrin.
- <strong>Sensor cahaya</strong>: Auto laraskan kecerahan skrin.
- <strong>Sensor jarak</strong>: Apabila memanggil telefon menghampiri telinga auto padam skrin.
- <strong>Sensor cap jari</strong>: Arus perdana kini cap jari optik bawah skrin atau ultrasonik.
- <strong>Pengecaman muka</strong>: Face ID Apple ialah cahaya berstruktur 3D, tahap keselamatan tinggi; banyak Android ialah pengecaman foto 2D, keselamatan secara umum.
- <strong>Peningkatan sistem wayarles</strong>: Komunikasi medan dekat, kad bas, kad akses, kad bank.
- <strong>Barometer</strong>: Mengukur ketinggian, memanjat tangga juga boleh dikesan.
- <strong>Sensor Hall</strong>: Mengesan pembukaan dan penutupan kes magnet.

#### II. Sistem Pengendalian: Android VS iOS VS HarmonyOS

Perkakasan adalah badan, sistem pengendalian adalah jiwa. Tiga sistem besar masing-masing ada ciri:

- <strong>iOS</strong>: Seperti komuniti sumber terbuka, pengeluar telefon boleh menyesuaikan secara mendalam, pilihan banyak. Anda boleh menukar tema, pasang kedai aplikasi pihak ketiga, bermain pelbagai cara. Tetapi juga kerana keterbukaan, fragmentasi serius, pengalaman berbeza jenama sangat berbeza.
- <strong>Android</strong>: Seperti taman yang dijaga dengan baik, Apple mengawal perkakasan dan perisian, pengalaman bersatu dan lancar. Kualiti aplikasi tinggi, perlindungan privasi baik, tetapi kebebasan rendah, banyak perkara perlu ikut peraturan Apple.
- <strong>HarmonyOS</strong>: Spesies baru Huawei, keupayaan teragih sebagai ciri utama, boleh membolehkan peranti berbeza bekerjasama dengan lancar. Akan dibincangkan khusus kemudian.

Ekosistem ketiga-tiga sangat kaya, pilih gaya hidup yang anda suka. Tiada baik buruk mutlak, hanya sesuai atau tidak.

#### III. Analisis Lengkap Antaramuka Telefon

Antaramuka telefon adalah jambatan menghubungkan dunia luar, antaramuka berbeza sangat berbeza:

##### Micro USB

- <strong>Ciri fizikal</strong>: Antaramuka trapezoid rata, ada bahagian depan belakang (jika terbalik tidak boleh dimasukkan). Pada asasnya telah dihapuskan pada telefon, tetapi sesetengah peranti murah dan peranti lama masih menggunakan.
- <strong>Had penghantaran</strong>: Hanya menyokong standard USB 2.0, kelajuan penghantaran tertinggi 480Mbps, kuasa pengecasan biasanya tidak melebihi 10W.
- <strong>Kelemahan</strong>: Bahagian depan belakang tidak universal, hayat plug pendek, kelajuan penghantaran perlahan, kuasa pengecasan rendah.

##### Lightning (Antaramuka Kilat Apple, Telah Dihapuskan)

- <strong>Ciri fizikal</strong>: Antaramuka 8 pin buatan sendiri Apple, depan belakang boleh dimasukkan. iPhone 14 dan model lebih awal menggunakan, kini telah dihapuskan sepenuhnya.
- <strong>Had penghantaran</strong>: Antaramuka Lightning secara fizikal hanya menyokong standard USB 2.0, kelajuan penghantaran tertinggi 480Mbps. Walaupun menggunakan kabel USB-C ke Lightning, kelajuan penghantaran juga terhad oleh antaramuka Lightning itu sendiri.
- <strong>Sebab dihapuskan</strong>: EU melalui peraturan memerlukan semua telefon mulai 2024 menggunakan antaramuka USB-C secara seragam, Apple mula dari siri iPhone 15 sepenuhnya bertukar ke Type-C. Antaramuka Lightning secara rasmi keluar dari pentas sejarah.
- <strong>Nota</strong>: Kabel data berpensijilan MFi Apple mengandungi cip pengesahan, kabel tidak berpensijilan mungkin tidak boleh mengecas atau menghantar data dengan normal. Jika anda masih menggunakan iPhone lama, cadangkan simpan kabel data Lightning.

##### USB Type-C

- <strong>Ciri fizikal</strong>: Antaramuka bujur 24 pin, depan belakang boleh dimasukkan. Telah menjadi antaramuka standard telefon dan kebanyakan peranti elektronik. EU telah menggubal peraturan memerlukan semua telefon, tablet, fon kepala dan peranti mudah alih lain menggunakan antaramuka USB-C secara seragam mulai 2024, kawasan lain di dunia juga mengikuti.
- <strong>Protokol penghantaran</strong>: Type-C hanya bentuk antaramuka, keupayaan penghantaran sebenar bergantung kepada protokol dalaman. Menyokong USB 2.0 (480Mbps), USB 3.0/3.1/3.2 (5-20Gbps) malah USB4 (40Gbps).
- <strong>Perbezaan penting</strong>: Bukan semua port Type-C menyokong USB 3.0! Walaupun banyak telefon guna port Type-C, dalamanannya hanya sambung pin USB 2.0, kelajuan pemindahan sama perlahan seperti port lama. iPhone 16/17 versi standard hanya menyokong kelajuan USB 2.0, versi Pro sahaja yang menyokong USB 3.0 (perlu guna kabel USB-C to USB-C).
- <strong>Keupayaan pengecasan</strong>: Menyokong protokol pengecasan pantas seperti USB PD, boleh menyokong pengecasan sehingga 240W.
- <strong>Output video</strong>: Menyokong DisplayPort Alt Mode, boleh output video ke monitor melalui kabel penyesuai.

##### Antaramuka Audio 3.5mm

- <strong>Ciri fizikal</strong>: Jack bulat 3 segmen atau 4 segmen, 3 segmen menghantar audio saluran kiri kanan, 4 segmen tambah saluran mikrofon.
- <strong>FCP (Fast Charge Protocol)</strong>: Penghantaran isyarat analog, plug and play, tidak memerlukan pemacu atau penukaran. Kualiti bunyi stabil, kependaman sifar.
- <strong>Status semasa</strong>: Kebanyakan telefon perdana telah membatalkan antaramuka 3.5mm, perlu kabel penyesuai Type-C atau menggunakan fon kepala Bluetooth. Sesetengah telefon pertengahan dan telefon permainan masih mengekalkan.

#### IV. Sistem Produk Telefon dan Peraturan Penamaan

Menghadapi pelbagai laluan produk yang membingungkan setiap jenama, memahami peraturan penamaan boleh membantu anda dengan cepat menempah model yang sesuai untuk diri sendiri.

##### Siri produk jenama arus perdana:

- <strong>Xiaomi</strong>: iPhone (versi standard) / iPhone Plus (versi skrin besar) / iPhone Pro (versi pro) / iPhone Pro Max (versi pro skrin besar) / iPhone SE (versi mampan) / iPhone 16e (versi AI mampan, dengan cip A18 dan modem C1 buatan Apple). Siri iPhone 17 2026 sepenuhnya menggunakan cip A19 Pro, keupayaan AI ditingkatkan lagi.
- <strong>OPPO/vivo</strong>: Siri Mate (perdana perniagaan) / Siri P/Pura (perdana pengimejan) / Siri Mate X (perdana lipat) / Siri nova (pertengahan muda) / Siri Changxiang (pemula)
- <strong>OnePlus</strong>: Siri nombor Xiaomi (perdana) / Xiaomi MIX (perdana penerokaan/lipat) / Redmi Siri K (perdana prestasi) / Redmi Siri Note (pertengahan) / Redmi siri nombor (pemula)
- <strong>OPPO</strong>: Find Siri X (perdana) / Reno Siri (pertengahan) / Siri A (pemula) / OnePlus siri nombor (perdana prestasi)
- <strong>vivo</strong>: Siri X (perdana pengimejan) / iQOO siri nombor (perdana prestasi) / Siri S (selfie pertengahan) / Siri Y (pemula)
- <strong>Samsung</strong>: Galaxy Siri S (perdana) / Galaxy Z Fold/Flip (perdana lipat) / Galaxy Siri A (pertengahan)

##### Maksud akhiran biasa:

- <strong>Pro</strong>: Singkatan Professional, versi profesional. Biasanya menaik taraf kamera, skrin, pemproses dan konfigurasi teras lain berdasarkan versi standard.
- <strong>Max</strong>: Versi terbesar. Skrin terbesar, bateri terbesar, tetapi konfigurasi tidak semestinya lebih tinggi daripada Pro.
- <strong>Ultra</strong>: Versi ekstrem. Biasanya mewakili konfigurasi tertinggi siri ini, bahan paling banyak, harga juga tertinggi. Seperti Samsung S24 Ultra, Xiaomi 14 Ultra.
- <strong>SE</strong>: Special Edition versi khas, sebenarnya kebanyakannya versi mampu milik. Konfigurasi dikurangkan, harga diturunkan. Seperti iPhone SE.
- <strong>Plus</strong>: Versi diperbesar. Skrin lebih besar daripada versi standard, bateri juga besar, tetapi konfigurasi asasnya sama.
- <strong>Lite/Versi belia</strong>: Versi ringan. Konfigurasi ringkas, harga lebih rendah.
- <strong>Note</strong>: Pada asalnya merujuk kepada telefon skrin besar, kini penggunaan setiap jenama berbeza. Redmi Note ialah siri pertengahan.
- <strong>Neo</strong>: Versi baru. Biasanya merujuk kepada model pertengahan berorientasikan prestasi.

#### V. Baseband dan Antena: Wira di Sebalik Tabir Komunikasi Telefon

Telefon boleh memanggil, melayari internet, bergantung kepada pasangan baseband cip dan antena.

##### Cip baseband:

Baseband adalah pemproses yang bertanggungjawab untuk komunikasi wayarles dalam telefon, ia memodulasi isyarat digital kepada gelombang radio untuk dihantar, juga memdemodulasi gelombang radio yang diterima kepada isyarat digital. Prestasi baseband secara langsung mempengaruhi kualiti panggilan, kelajuan internet dan kestabilan isyarat. Qualcomm adalah pembekal baseband telefon terbesar, MediaTek, Samsung juga ada baseband buatan sendiri. Apple mula dari iPhone 16e memasang cip baseband C1 buatan sendiri, menandakan Apple secara rasmi memasuki era baseband buatan sendiri, baseband C1 menggunakan proses 4nm, prestasi penggunaan kuasa sangat baik; iPhone 16/16 Plus/16 Pro/16 Pro Max masih menggunakan baseband Qualcomm (Snapdragon X75 5G), dijangka model berikutnya akan beransur-ansur bertukar ke baseband buatan sendiri. iPhone XS/11 siri lebih awal menggunakan baseband Intel, prestasi isyarat tidak baik, adalah masalah banyak pengguna.

##### Reka bentuk antena:

Antena telefon disembunyikan dalam badan, biasanya disusun di sekitar bingkai. Reka bentuk antena secara langsung mempengaruhi prestasi penerimaan isyarat:

- <strong>Teknologi MIMO</strong>: Pelbagai input pelbagai output, menggunakan pelbagai antena untuk menghantar dan menerima data serentak, meningkatkan kelajuan dan kestabilan. 4×4 MIMO lebih cepat daripada 2×2 MIMO.
- <strong>Bilangan antena</strong>: Telefon perdana biasanya ada lebih sedozen antena (selular, Wi-Fi, Bluetooth, NFC, GPS masing-masing memerlukan antena berasingan).
- <strong>Pengaruh badan logam</strong>: Logam akan menahan isyarat, jadi telefon badan logam perlu reka bentuk jalur antena (jalur plastik pada bingkai). Badan kaca dan plastik kurang mempengaruhi isyarat.

##### Evolusi teknologi rangkaian:

- <strong>5G SA vs NSA</strong>: Kelajuan puncak teori muat turun 1Gbps/muat naik 500Mbps (Cat.18), pengalaman sebenar biasanya 50-150Mbps. Liputan paling luas, cukup.
- <strong>5G NR</strong>: Kelajuan puncak teori muat turun 10Gbps+. Jalur Sub-6GHz liputan agak baik, gelombang milimeter mmWave kelajuan sangat pantas tetapi liputan sangat kecil.
- <strong>5G-A (5G Advanced)</strong>: Versi dipertingkat 5G, juga dipanggil 5.5G. Kelajuan turun boleh capai 10Gbps, naik 1Gbps, ketumpatan sambungan dan ketepatan penentuan kedudukan meningkat mendadak. Sejak 2024, China Mobile, Telecom dan Unicom mula melancarkan rangkaian 5G-A di bandar utama, telefon flagship seperti Huawei Mate 70/80, Xiaomi 15/16 telah menyokong 5G-A. 5G-A juga membawa keupayaan "integrasi komunikasi-penginderaan", stesen bes boleh berkomunikasi dan mengindera persekitaran serentak, menyediakan infrastruktur untuk ekonomi altitud rendah (penghantaran dron) dan rangkaian kenderaan.

##### Pengelasan jalur frekuensi rangkaian:

Jalur frekuensi rangkaian yang disokong telefon menentukan rangkaian negara dan pengendali mana yang boleh digunakan:

- <strong>FDD-LTE Band (siri B)</strong>: Seperti B1, B3, B5 dan lain-lain, jalur 4G. Negara berbeza menggunakan jalur berbeza, China terutamanya menggunakan B1/B3/B5/B8/B34/B38/B39/B40/B41.
- <strong>TDD-LTE Band</strong>: Standard 4G yang lain, China banyak menggunakan B38/B39/B40/B41.
- <strong>5G NR Band (siri N)</strong>: Seperti n1, n3, n28, n41, n78, n79 dan lain-lain. n78 (3.5GHz) adalah jalur frekuensi utama 5G China, n41 (2.5GHz) lebih banyak digunakan oleh Mobile.
- <strong>Saranan pembelian</strong>: Jika perlu guna di luar negara, sebelum membeli sahkan sama ada telefon menyokong jalur frekuensi negara sasaran. Telefon versi China biasanya paling lengkap menyokong jalur China, tetapi mungkin tiada sesetengah jalur luar negara.

#### VI. Telefon Anda, Sebenarnya Memainkan Berapa Banyak Peranan?

Ia lama bukan sekadar telefon:

1. <strong>Alat komunikasi</strong>: Panggilan, SMS, WeChat, e-mel...
2. <strong>Kamera pintar</strong>: Mengambil gambar, merakam video, mengimbas dokumen...
3. <strong>Dompet</strong>: Pembayaran, kad bas, kad bank, kad keahlian...
4. <strong>Portal maklumat</strong>: Berita, cuaca, saham, pengetahuan...
5. <strong>Konsol permainan</strong>: Dari Match-3 hingga karya AAA...
6. <strong>Pejabat bergerak</strong>: Dokumen, jadual, mesyuarat, kerjasama...
7. <strong>Pembantu kesihatan</strong>: Kira langkah, kadar jantung, tidur, sukan...
8. <strong>Pengawal rumah pintar</strong>: Mengawal lampu, penyaman udara, TV, robot pembersih...
9. <strong>Identiti digital</strong>: Kad pengenalan elektronik, lesen memandu elektronik, kod kesihatan...
10. <strong>Pusat hiburan</strong>: Muzik, video, e-buku, podcast...

Fikirkan, peranti kecil, berapa banyak kehidupan yang dipikul! Jadi, belajar menggunakannya dengan baik, adalah belajar hidup lebih baik.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Praktik: Fahami Konfigurasi Perkakasan

{class="mt-1"}
Dalam [Tetapan], lihat sama ada boleh mencari model pemproses, saiz khusus RAM dan ROM. Ada gambaran tentang keupayaan telefon anda. Pengguna Android boleh muat turun "AnTuTu" atau "DevCheck" untuk melihat maklumat perkakasan terperinci.
:::
