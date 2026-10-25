---
id: di-er-shi-san-zhang
num: 23
part: chao-yue-pian
nav: Bab 23: Pemikiran Pengaturcaraan dan Asas Automasi
toc: default
kind: chapter
---

### Bab 23: Pemikiran Pengaturcaraan &amp; Pengenalan Automasi

{class="chapter-intro mb-4"}
Anda tidak perlu mengendalikan secara manual setiap kali, dan tidak perlu mengingat apa yang perlu dilakukan—telefon akan menilai masa yang sesuai sendiri, dan melaksanakan sendiri.

#### Contohnya: Setiap pagi apabila anda bangun, anda perlu mematikan mod jangan ganggu secara manual, membuka WeChat untuk melihat mesej, membuka App cuaca untuk melihat apa yang perlu dipakai hari ini, membuka NetEase Cloud untuk memainkan lagu. Jika langkah-langkah ini dibungkus menjadi satu aliran automasi, ditetapkan "laksanakan secara automatik setiap pagi jam 7", maka apabila anda bangun hanya perlu mengambil telefon, semuanya sudah bersedia. Bukankah sangat puas apabila memikirkannya?

Hakikat automasi ialah rantai logik "jika... maka...", iaitu if-else dalam pengaturcaraan. Memahami cara berfikir ini, walaupun anda tidak menulis kod seumur hidup, keteraturan menyelesaikan masalah juga akan jauh lebih baik. Elemen teras:<strong>Syarat pencetus</strong> : Bilakah bermula? Boleh jadi "setiap pagi jam 7", "apabila saya menyambung ke Wi-Fi rumah", "apabila saya tiba di sesuatu lokasi", "apabila bateri telefon kurang daripada 20%".

Tindakan pelaksanaan

: Apa yang perlu dilakukan secara khusus? Boleh jadi menghantar satu mesej WeChat, membuka App tertentu, melaraskan volum, menukar kertas dinding, memainkan muzik, menghantar pemberitahuan... hampir semua perkara yang boleh anda lakukan secara manual pada telefon, automasi boleh lakukan.

1. <strong>Logik perantaraan</strong>(pilihan tetapi sangat kuat): Jika situasi A maka lakukan X, sebaliknya lakukan Y. Contohnya "jika hari bekerja maka mainkan podcast berita, hujung minggu mainkan muzik", ini dipanggil cabang bersyarat.
2. <strong>2. "Pintasan" iOS — Senjata Automasi Pengguna Apple</strong> App "Pintasan" (Shortcuts) Apple adalah aplikasi terbina dalam, tidak perlu dimuat turun. Konsep terasnya ialah menggabungkan pelbagai operasi seperti blok binaan. Mula-mula bincangkan beberapa konsep utama:
3. <strong>"Pintasan"</strong>: Satu aliran automasi lengkap, boleh diklik secara manual untuk dijalankan, atau diaktifkan melalui suara Siri. Contohnya anda berkata "Hey Siri, mod pulang ke rumah", ia akan melaksanakan satu siri operasi yang anda tetapkan secara automatik.

#### "Automasi"

: Arahan yang dijalankan secara automatik oleh syarat pencetus, tidak memerlukan anda mencetuskan secara manual. Contohnya "apabila telefon menyambung ke Bluetooth kereta, automatik membuka App peta". Automasi ditetapkan di bawah tab "Automasi", berasingan daripada "Pintasan".

- <strong>"Tindakan"</strong>: Unit pelaksanaan terkecil. Membuka App ialah satu tindakan, menghantar mesej ialah satu tindakan, mendapatkan cuaca ialah satu tindakan, melaraskan kecerahan ialah satu tindakan. Anda boleh merantai ratusan tindakan bersama.
- <strong>Berikut adalah beberapa contoh yang benar-benar berguna, ikuti sekali dan anda akan faham:</strong> Contoh Satu: Satu Klik "Aliran Selamat Pagi"
- <strong>Setiap pagi klik sekali (atau berkata kepada Siri "selamat pagi"), telefon akan secara automatik: mendapatkan cuaca hari ini → membaca cuaca dan suhu → memaparkan susunan kalendar hari ini → membuka App muzik kegemaran anda dan mula memainkan. Langkah operasi: Pintasan baharu → tambah tindakan "Dapatkan cuaca semasa" → tambah "Baca teks" → tambah "Dapatkan acara kalendar" → tambah "Paparkan peringatan" → tambah "Buka App" pilih NetEase Cloud Music. Semudah itu, seret sepenuhnya.</strong> Contoh Dua: Automasi "Mod Jimat Bateri"

Dalam tab "Automasi", pintasan baharu → pilih "Aras bateri" → tetapkan "kurang daripada 30%" → tambah tindakan "Tetapkan mod aras bateri rendah kepada hidup", "Kurangkan kecerahan skrin kepada 30%", "Matikan Bluetooth". Mulai sekarang apabila bateri telefon kurang daripada 30% ia akan memasuki keadaan jimat bateri secara automatik, tanpa perlu anda risau.

##### Contoh Tiga: Imbas Kod Automasi Catatan Perbelanjaan

Setiap kali selepas anda menggunakan WeChat/Alipay mengimbas kod untuk membayar, telefon akan membaca pemberitahuan pembayaran, secara automatik merekodkan jumlah dan perniagaan ke dalam satu nota atau jadual Numbers. Ini memerlukan penggunaan syarat pencetus "Terima SMS/pemberitahuan" dalam "Automasi" Pintasan (iOS 17+ menyokong pembacaan transaksi Wallet), dipadankan dengan tindakan "Tambah ke Numbers". Bagi mereka yang ingin mencatat perbelanjaan tetapi terlalu malas untuk mencatat secara manual, ini bagaikan penyelamat.

##### Terdapat juga satu kegunaan pintar yang tidak diketahui ramai: anda boleh menambah pintasan ke skrin utama, menjadikannya ikon App. Contohnya buat satu pintasan "teksi pulang ke rumah", letakkan ikon di atas meja, klik sekali terus membuka Didi dan menetapkan destinasi ke rumah, jauh lebih cepat daripada membuka App sendiri dan menaip perlahan-lahan.

3\. Automasi Android — Tasker dan Rakan-rakannya

##### Di pihak Android, keadaan agak lebih rumit, tetapi silingnya juga lebih tinggi. Mula-mula bincangkan yang mudah:

Tahap Permulaan: Auto-klik

Ramai telefon Android mempunyai "auto-klik" terbina dalam atau boleh dimuat turun dari kedai aplikasi. Prinsipnya sangat mudah: anda operasi secara manual sekali, ia merakam koordinat dan selang masa klik anda, kemudian boleh memainkan semula pada kelajuan tinggi. Contohnya App tertentu perlu menuntut ganjaran daftar masuk setiap hari, anda rakam sekali aliran klik, selepas itu ia berjalan secara automatik setiap hari dan selesai. Kelemahannya ialah: ia hanya mengenali koordinat, jika susun atur antara muka berubah (contohnya muncul iklan), ia akan klik salah.

#### Tahap Lanjutan: Tasker — Raja Automasi Android

Tasker diiktiraf sebagai alat automasi terkuat di platform Android, mendominasi kedudukan teratas sepanjang masa. Sejujurnya lengkung pembelajarannya agak curam, antara mukanya tidak begitu cantik, tetapi setelah mahir, anda akan rasa telefon tiba-tiba menjadi maha kuasa. Teras Tasker juga adalah mod "pencetus → tugas":

##### Profil (Profile)

: Mentakrifkan "bila mencetus". Syarat pencetus boleh jadi masa, lokasi, status sambungan Wi-Fi, sambungan Bluetooth, menerima pemberitahuan khusus, status bateri, orientasi skrin... syarat pencetus yang disokong Tasker terlalu banyak sehingga menakjubkan, ada puluhan jenis.

##### Tugas (Task)

: Mentakrifkan "apa yang perlu dilakukan selepas mencetus". Satu tugas boleh mengandungi pelbagai tindakan, dilaksanakan mengikut susunan. Jenis tindakan termasuk: melaraskan tetapan sistem (volum, kecerahan, Wi-Fi, Bluetooth, mod penerbangan), menghantar SMS, permintaan HTTP, melaksanakan arahan Shell, mengawal main balik media, memaparkan kotak dialog dan lain-lain.

- <strong>Berikut adalah beberapa senario klasik praktikal Tasker:</strong> Hidupkan Wi-Fi secara automatik apabila sampai rumah
- <strong>: Tetapkan syarat pencetus sebagai "Sambung ke stesen pangkalan tertentu" (kerana anda akan menyambung ke stesen pangkalan tetap berhampiran rumah) → tugas "Hidupkan Wi-Fi". Tidak perlu GPS dan tidak memakan kuasa, telefon masuk ke kawasan perumahan terus hidupkan Wi-Fi secara automatik.</strong> Mod mesyuarat

: Syarat pencetus ialah "Tajuk acara kalendar mengandungi 'mesyuarat'" → tugas "Tetapkan mod senyap, matikan volum media, auto-balas WeChat (memerlukan pemalam)". Tidak perlu lagi bimbang telefon tiba-tiba berbunyi semasa mesyuarat.

- <strong>Pelindung mata lewat malam</strong>: Syarat pencetus ialah "Masa 22:00-06:00" → tugas "Hidupkan mod pelindung mata, kurangkan kecerahan kepada 20%, tetapkan skrin kepada hitam putih (mod skala kelabu)". Skrin hitam putih sangat berkesan mengurangkan keinginan menatal video pendek—sekali gambar menjadi kelabu, anda tidak mahu menatal lagi.
- <strong>Automasi podcast apabila fon kepala dipasang</strong>: Syarat pencetus ialah "Fon kepala berwayar dipasang / fon kepala Bluetooth disambung" → tugas "Buka App Xiaoyuzhou dan mula memainkan episod terbaru". Pakai fon kepala boleh mendengar terus, tidak perlu buka kunci telefon cari App.
- <strong>Jika anda rasa Tasker terlalu sukar, boleh cuba versi ringkasnya:</strong> MacroDroid
- <strong>. Antara muka lebih mesra, templat melimpah, sesuai untuk pengguna yang tidak mahu bersusah payah. Selain itu, kini banyak sistem Android domestik (MIUI Xiaomi, HarmonyOS Huawei, ColorOS OPPO) mempunyai fungsi "senario" atau "pembantu pintar" terbina dalam, walaupun tidak sekuat Tasker, tetapi untuk automasi harian sudah cukup.</strong>4. Aplikasi Harian Pemikiran Automasi

Hasil terbesar mempelajari automasi sebenarnya bukan menjimatkan sedikit masa itu, tetapi <strong>mengubah cara anda berfikir tentang masalah</strong>. Sekali anda biasa dengan mod pemikiran "jika X berlaku, secara automatik lakukan Y", anda akan dapati banyak kerja berulang dalam kehidupan boleh dihapuskan. Contohnya:

#### Setiap kali selepas mengambil foto, sandaran automatik ke awan kemudian memampatkan foto tempatan kepada saiz kecil untuk menjimatkan ruang.

Setiap pagi secara automatik membaca susunan hari ini dari kalendar, menjana satu teks dan dihantar melalui WeChat kepada keluarga.<strong>Selepas menerima SMS pengesahan penerimaan kurier, secara automatik menambah satu item tindakan "ambil kurier" dalam nota.</strong> Apabila bateri telefon penuh, secara automatik mengeluarkan peringatan suara untuk cabut pengecas (mengelakkan cas berlebihan merosakkan bateri).

- Setiap kali masa balik kerja tiba, jika masih berhampiran syarikat (melalui penyetempatan stesen pangkalan), secara automatik mengingatkan "masa pulang".
- Perkara ini kedengaran sangat canggih, tetapi sebenarnya selagi anda menguasai dua konsep asas "pencetus + tindakan", dipadankan dengan Pintasan atau Tasker, semuanya boleh dibuat. Kuncinya ialah
- anda perlu sedar dahulu "perkara ini boleh diautomasi"
- —ramai orang bukan tidak tahu, tetapi langsung tidak berfikir ke arah itu.
- 5. Panduan Mengelak Perangkap: Masalah Biasa Automasi

Membuat automasi juga tidak semestinya lancar, ada beberapa perangkap yang saya tolong langkahi dahulu:<strong>Pencetus lokasi mungkin tidak berfungsi</strong>: Pencetus "tiba/berlepas lokasi" iOS menggunakan teknologi geopagar, ketepatan bergantung pada isyarat GPS dan pengoptimuman sistem. Kadang-kadang anda sudah sampai rumah sepuluh minit baru mencetus. Cadangan gunakan pencetus sambungan Wi-Fi atau stesen pangkalan menggantikan pencetus lokasi, lebih boleh dipercayai dan lebih menjimatkan kuasa.

#### "Automasi" Pintasan memerlukan kebenaran

: Dalam iOS, pencetus di bawah tab "Automasi" kebanyakan memerlukan pengesahan manual anda sebelum boleh berjalan (mekanisme keselamatan iOS). Tetapi sambungan Wi-Fi, sambungan Bluetooth, penghentian penggera ini boleh berjalan secara automatik sepenuhnya, tidak memerlukan pengesahan.

- <strong>Tasker memerlukan kebenaran kebolehaksesan</strong>: Banyak fungsi lanjutan (seperti simulasi klik) memerlukan kebenaran perkhidmatan kebolehaksesan, ini akan membuat telefon memaparkan pemberitahuan kekal dalam tetapan. Ini adalah reka bentuk keselamatan Android, tidak boleh dialihkeluarkan.
- <strong>Jangan buat automasi terlalu kompleks</strong>: Apabila baru mula membuat automasi, mulakan dari aliran kecil "2-3 tindakan". Jangan terus buat satu aliran super 20 langkah—proses nyahpepijat akan membuat anda gila.
- <strong>Petua Kecil: Postur yang betul untuk permulaan automasi</strong> Luangkan 5 minit berfikir: Apakah 3 perkara yang paling kerap anda ulang pada telefon setiap hari? Contohnya rutin pagi setiap hari, kebiasaan selepas menyambung fon kepala Bluetooth setiap kali, tetapan sebelum keluar setiap kali... Mula dari perkara kecil berfrekuensi tinggi ini, buat satu automasi ringkas untuk setiap satu. Walaupun setiap automasi hanya menjimatkan 5 saat anda, lama-kelamaan juga berjumlah banyak. Dan kepuasan selepas berjaya membuatnya, benar-benar boleh menimbulkan ketagihan.
- <strong>Berlatih: Tiga cabaran automasi permulaan</strong> Pilih satu yang paling sesuai untuk anda selesaikan, selepas selesai anda sudah memasuki tahap permulaan:

::: div .success-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Cabaran Satu: Automasi selamat pagi

{class="mt-1"}
: iOS: Dalam App Pintasan buat pintasan baharu → tambah "Dapatkan cuaca semasa" → "Baca teks" → "Buka App pilih NetEase Cloud". Selepas selesai anda boleh berkata kepada Siri "selamat pagi" untuk mencetus. Android: Dalam Tasker buat tugas baharu → tambah "Dapatkan cuaca" → "Baca" → "Buka App" → tetapkan masa pencetus setiap hari 7:00.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Cabaran Dua: Jimat bateri automatik aras rendah

{class="mt-1 mb-2"}
: iOS: Tab Automasi → Baharu → "Aras bateri" → kurang daripada 25% → tambah "Tetapkan mod aras bateri rendah hidup" + "Tetapkan kecerahan 25%". Android: Tasker buat Profil baharu → Status → Kuasa → Bateri 0-25% → Tugas "Hidupkan mod jimat bateri" + "Kurangkan kecerahan".

{class="list-decimal pl-6 mt-1 space-y-1"}
1. <strong>Cabaran Tiga: Navigasi automatik apabila menyambung Bluetooth kereta</strong>: iOS: Automasi → Baharu → "Bluetooth" → pilih Bluetooth kereta anda → tambah "Buka App pilih Amap" + "Volum media laras ke 80%". Android: Tasker → Profil → Status → Bluetooth disambung → pilih Bluetooth kereta → Tugas "Buka Amap" + "Naikkan volum media".
2. <strong>Lampiran Bab 23: Panduan Permulaan GitHub — Daripada Hos Kod ke Platform Kolaborasi</strong> Bab sebelumnya kita bincangkan "pemikiran pengaturcaraan", dan untuk benar-benar melaksanakan pemikiran pengaturcaraan dan membuat projek bersama orang lain, tidak boleh lari dari satu nama—GitHub. Sama ada anda pelajar jabatan sains komputer yang ingin menyertai pertandingan, ingin menyimpan karya kod anda, atau sekadar ingin melihat apa yang sedang dikerjakan oleh pembangun di seluruh dunia, GitHub adalah platform yang mesti anda kenali. Bahagian ini bermula dari konsep paling asas, membantu anda membina satu pemahaman yang jelas.
3. <strong>1. Apakah Sebenarnya GitHub?</strong> Ringkasnya, GitHub ialah sebuah
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Contact akan menerima pemberitahuan, boleh pilih terima atau tolak.

{class="list-disc pl-6 mt-1 space-y-1"}
- <strong>Kesan praktikal: Wi-Fi 7 router telah mula dijual, tetapi telefon perlu sokong. iPhone 15 Pro/16 siri, Xiaomi 14, Samsung S24 Ultra dll flagship 2024 telah sokong Wi-Fi 7; peranti lebih awal disokong melalui kemas kini OS. Jika ada router Wi-Fi 7, boleh nikmati kelajuan rangkaian lebih cepat dan lebih stabil.</strong>2. Cara waris menerima akses
- <strong>Setiap telefon ada fungsi "tersembunyi" yang tidak digunakan kebanyakan orang — ia bukan Easter Egg sengaja tersembunyi oleh jurutera, tetapi ditimbus dalam lapisan tetapan dalam, atau tidak diperkenalkan dengan jelas oleh pengiklanan. Bab ini akan kumpulkan beberapa fungsi paling praktikal yang patut anda cuba.</strong> Selepas kematian pengguna asal, waris perlu hantar sijil kematian kepada Apple.
- <strong>"Pilihan pembangun" adalah mod kawalan khas yang disediakan Android untuk jurutera, biasanya tidak ditunjukkan kepada pengguna biasa. Tetapi beberapa fungsi praktikal di dalamnya sangat berbaloi untuk dibuka.</strong> Selepas pengesahan, waris boleh guna Access Key untuk log masuk iCloud dan muat turun foto, nota, kenalan dll.
:::
