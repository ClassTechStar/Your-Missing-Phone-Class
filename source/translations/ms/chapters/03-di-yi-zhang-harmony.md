---
id: di-yi-zhang-harmony
part: ji-chu-pian
nav:  Tambahan Bab 1: Topik Khas Sistem Pengendalian HarmonyOS
toc: default
kind: supplement
---

### Tambahan Bab 1: Topik Khas Sistem Pengendalian HarmonyOS

{class="chapter-intro mb-4"}
HarmonyOS adalah sistem pengendalian yang dibangunkan sendiri oleh Huawei, dari diterbitkan pada 2019 hingga kini, telah melalui beberapa versi besar. Ia bukan sahaja "pengganti Android yang lain", tetapi spesies baru dengan falsafah reka bentuk unik. Mari kita mendalami sistem pengendalian yang sedang meningkat naik ini.

#### I. Apa itu HarmonyOS? Mengapa Ia Berbeza?

Falsafah teras HarmonyOS adalah "sambungan segala perkara". Berbeza dengan sistem pengendalian tradisional yang terutamanya berkhidmat peranti tunggal, HarmonyOS dari awal reka bentuk telah mengambil kira kerjasama pelbagai peranti.

<strong>Seni bina teragih</strong> adalah jiwa HarmonyOS. Ringkasnya, ia boleh menggabungkan pelbagai peranti secara maya menjadi satu "super terminal". Telefon, tablet, komputer, jam tangan, TV anda, bukan lagi individu terpencil, tetapi "organ" keseluruhan, boleh saling memanggil keupayaan antara satu sama lain.

Contohnya: Anda menggunakan telefon menonton video, ingin menonton di skrin besar, cara tradisional adalah paparan skrin; manakala pada HarmonyOS, anda boleh terus "mengalirkan" video ke TV untuk terus menonton, telefon menjadi kawalan jauh. Ini bukan paparan skrin mudah, tetapi aplikasi itu sendiri berjalan merentasi peranti.

#### II. HarmonyOS 4.3: Versi Matang Berdasarkan AOSP

HarmonyOS 4.3 adalah versi yang digunakan secara meluas pada telefon Huawei kini. Perlu dijelaskan, HarmonyOS 4.3 serasi dengan rangka kerja kod projek sumber terbuka Android (AOSP), jadi ia boleh serasi sepenuhnya dengan aplikasi Android — kebanyakan App yang anda muat turun dari Huawei AppGallery pada asasnya masih aplikasi Android, berjalan melalui lapisan serasi HarmonyOS. Tetapi HarmonyOS 4.3 bukan sekadar shell Android, ia telah menambah banyak keupayaan teragih buatan sendiri Huawei, enjin Ark dan teknologi lain berdasarkan AOSP.

##### Ciri teras:

- <strong>Serasi aplikasi Android</strong>: Disebabkan dibangunkan berdasarkan AOSP, HarmonyOS 4.3 boleh menjalankan hampir semua aplikasi Android dengan normal, pengguna hampir tidak dapat merasakan perbezaan.
- <strong>Enjin Ark</strong>: Pengkompil dan masa jalan buatan sendiri Huawei, menjadikan aplikasi berjalan lebih lancar, lebih menjimatkan kuasa. Berbanding versi awal, kelancaran meningkat dengan jelas.
- <strong>Super terminal</strong>: Dalam pusat kawalan, boleh nampak secara intuitif peranti HarmonyOS lain di sekeliling, seret untuk sambung. Telefon memanggil papan kekunci tetikus komputer, tablet memanggil kamera telefon, semua sangat mudah.
- <strong>Kad perkhidmatan</strong>: Serupa dengan widget iOS, tetapi lebih fleksibel. Boleh sapu ke atas ikon App untuk mengembangkan kad, memaparkan maklumat utama, tanpa membuka App.
- <strong>Sangat disyorkan untuk semua pengguna mengaktifkannya</strong>: Hanya membenarkan pemasangan aplikasi dari kedai aplikasi rasmi, mengurangkan risiko perisian hasad.
- <strong>Pusat privasi</strong>: Pengurusan berpusat kebenaran aplikasi, melihat rekod tingkah laku aplikasi.

##### Ciri antara muka pengguna:

- <strong>Kunci skrin majalah</strong>: Skrin kunci memaparkan gambar dan artikel cantik, sapu untuk masuk ke desktop.
- <strong>Kad universal</strong>: Ikon desktop boleh dikembangkan menjadi kad, memaparkan lebih banyak maklumat.
- <strong>Super transit</strong>: Kawasan storan sementara, boleh menyimpan teks, gambar, fail sementara, kemudian seret ke mana-mana App untuk digunakan. Perkongsian merentasi aplikasi menjadi sangat lancar.
- <strong>Carian pintar</strong>: Carian global, boleh cari aplikasi, fail, tetapan, laman web.

#### III. HarmonyOS NEXT (HarmonyOS 6): Permulaan Sebenar Sistem Pengendalian Sendiri Huawei

HarmonyOS NEXT (HarmonyOS NEXT 5.0) berbeza secara asas dengan HarmonyOS 4.3 — ia menggunakan mikrokernel HarmonyOS buatan sendiri Huawei, tidak lagi bergantung kepada kernel Linux dan kod AOSP, juga <strong>tidak lagi menyokong aplikasi Android secara langsung</strong>. Ini adalah langkah penting HarmonyOS dari "bentuk peralihan serasi Android" secara rasmi menuju "sistem pengendalian sepenuhnya bebas".

##### Perubahan besar:

- <strong>Kernel sepenuhnya sendiri</strong>: HarmonyOS NEXT menggunakan kernel buatan sendiri Huawei, tidak lagi mengandungi sebarang kod AOSP. Sistem lebih ringkas, lebih selamat, lebih cekap.
- <strong>Tidak lagi menyokong aplikasi Android</strong>: Ini adalah perubahan terbesar. HarmonyOS NEXT hanya boleh menjalankan aplikasi HarmonyOS natif, tidak boleh memasang dan menjalankan fail APK. Sebelum menaik taraf, sila sahkan App yang sering anda guna ada versi HarmonyOS natif.
- <strong>Ekosistem aplikasi natif</strong>: Huawei sedang berusaha mendorong pembangun untuk memindahkan aplikasi ke platform HarmonyOS natif. Kini App arus perdana seperti WeChat, Alipay, Taobao telah melancarkan versi HarmonyOS natif, tetapi sesetengah aplikasi niche mungkin belum disesuaikan.
- <strong>Seni bina keselamatan Star Shield</strong>: Sistem keselamatan baharu, perlindungan rantaian penuh dari perkakasan ke perisian. Menyokong kawalan kebenaran lebih halus, seperti "lokasi kabur" — aplikasi hanya tahu anda secara kasar di mana, tidak tahu lokasi tepat.
- <strong>Integrasi mendalam AI</strong>: Keupayaan AI tahap sistem, bukan sahaja App tertentu ada AI. Contohnya sari kata AI boleh menterjemah video masa nyata, potong AI boleh mengecam subjek secara pintar.
- <strong>Aliran merentasi peranti tanpa siut</strong>: Keupayaan teragih lebih lanjut. Status aplikasi boleh bertukar antara peranti tanpa siut, dokumen yang anda edit pada telefon, berjalan ke komputer auto dibuka pada komputer.
- <strong>Perkhidmatan meta</strong>: Perkhidmatan ringan yang boleh digunakan tanpa pemasangan. Contohnya imbas kod QR terus membuka fungsi tertentu, tanpa perlu muat turun App dahulu.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Wajib Baca Sebelum Menaik taraf ke HarmonyOS NEXT

{class="mt-1"}
Selepas menaik taraf ke HarmonyOS NEXT, telefon anda tidak akan dapat menjalankan aplikasi Android. Sila pastikan sebelum menaik taraf: ① App yang sering anda guna ada versi HarmonyOS natif; ② Kerja atau kehidupan anda tiada senario yang mesti bergantung kepada aplikasi Android. Tidak boleh kembali ke HarmonyOS 4.3 selepas menaik taraf.
:::

##### Perubahan logik operasi:

- <strong>Navigasi gerak isyarat</strong>: Tepi kiri kanan sapu untuk kembali, bawah sapu ke atas untuk kembali ke desktop, sapu ke atas dan tahan untuk pelbagai tugas.
- <strong>Tetingkap pintar berbilang</strong>: Menyokong pelbagai bentuk pelbagai tugas seperti skrin berpisah, tetingkap terapung, pandangan selari.
- <strong>Panggilan Celia</strong>: Perkhidmatan panggilan video Huawei, menyokong perkongsian skrin, kecantikan, kabur latar belakang.

#### IV. Ekosistem HarmonyOS: Peranti dan Aplikasi

HarmonyOS bukan sahaja sistem telefon, tetapi ekosistem yang meliputi pelbagai peranti.

##### Jenis peranti yang disokong:

- <strong>Telefon dan tablet</strong>: Peranti teras, fungsi paling lengkap.
- <strong>Jam tangan pintar dan gelang</strong>: Berjalan secara berasingan atau bekerjasama dengan telefon.
- <strong>Skrin pintar (TV)</strong>: Pusat hiburan keluarga.
- <strong>Speaker pintar</strong>: Pintu masuk interaksi suara.
- <strong>Kereta</strong>: Kokpit HarmonyOS, pengalaman kokpit memandu pintar.
- <strong>Rumah pintar</strong>: Peti sejuk, penyaman udara, mesin basuh dan lain-lain.

##### Status ekosistem aplikasi:

Pasaran aplikasi HarmonyOS telah mempunyai jutaan aplikasi, App utama asasnya ada. Huawei juga aktif menggalakkan pembangun mencipta aplikasi native HarmonyOS. Sehingga pertengahan 2026, WeChat, Alipay, Taobao, Douyin, Meituan, JD dan aplikasi utama lain telah melancarkan versi native HarmonyOS, penggunaan harian asasnya tanpa halangan. Sebahagian aplikasi niche dan industri mungkin masih dalam penyesuaian, sebelum naik taraf disyorkan sahikan App yang kerap anda guna telah menyokong.

#### V. Tip Penggunaan HarmonyOS

- <strong>Super terminal</strong>: Sapu ke bawah dari sudut kanan atas skrin buka pusat kawalan, ketik "Super Terminal", boleh nampak peranti lain di sekeliling, seret untuk sambung.
- <strong>Super transit</strong>: Tekan lama teks/gambar/fail, pilih "Salin ke Transit", kemudian dalam App lain tekan lama untuk tampal, atau seret keluar.
- <strong>Kad perkhidmatan</strong>: Sapu ke atas ikon App untuk mengembangkan kad, tekan lama kad boleh laraskan saiz atau tambah ke desktop.
- <strong>Tetingkap pintar berbilang</strong>: Sapu ke dalam dari tepi kiri kanan skrin dan tahan, buka bar sisi, ketik aplikasi untuk dibuka sebagai tetingkap terapung.
- <strong>Perlindungan privasi</strong>: Tetapan &gt; Privasi, boleh lihat rekod penggunaan kebenaran aplikasi, tetapkan lokasi kabur dan lain-lain.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Fungsi kunci BL:

{class="mt-1"}
Sistem HarmonyOS sentiasa dikemas kini dan diulang, versi berbeza mungkin ada sedikit perbezaan. Penerangan dalam artikel ini berdasarkan ciri utama HarmonyOS 4.3 dan 6, fungsi khusus sila rujuk versi sebenar telefon anda. Cadangkan kekal kemas kini sistem, untuk mendapatkan fungsi terkini dan tampung keselamatan.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Cuba Sekarang: Alami Ciri Khas HarmonyOS

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Buka pusat kawalan, cari "Super Terminal", lihat sama ada ada peranti HarmonyOS lain di sekeliling.
2. Cuba "Super Transit": Salin satu teks ke transit, kemudian seret keluar dalam nota.
3. Sapu ke atas beberapa ikon App biasa, lihat kandungan yang dipaparkan oleh kad perkhidmatan mereka.
4. Pergi ke Tetapan &gt; Privasi, lihat aplikasi yang baru menggunakan kebenaran sensitif.
:::
