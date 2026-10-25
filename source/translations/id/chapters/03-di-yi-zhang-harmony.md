---
id: di-yi-zhang-harmony
part: ji-chu-pian
nav:  Lampiran Bab 1: Topik khusus sistem operasi HarmonyOS
toc: default
kind: supplement
---

### Lampiran Bab 1: Topik khusus sistem operasi HarmonyOS

{class="chapter-intro mb-4"}
HarmonyOS adalah sistem operasi self-developed Huawei, sejak dirilis 2019 hingga sekarang, sudah melewati beberapa versi besar. Ia bukan sekadar "pengganti Android lain", melainkan spesies baru dengan filosofi desain unik. Mari kita pelajari lebih dalam sistem operasi yang sedang naik daun ini.

#### 1. Apa itu HarmonyOS? Mengapa ia berbeda?

Filosofi inti HarmonyOS adalah "interkoneksi dari segala hal". Berbeda dari sistem operasi tradisional yang utamanya melayani perangkat tunggal, HarmonyOS sejak awal desain sudah mempertimbangkan kolaborasi multi-perangkat.

<strong>Arsitektur distributed</strong> adalah jiwa HarmonyOS. Sederhananya, ia bisa memvirtualkan beberapa perangkat menjadi satu "super terminal". Ponsel, tablet, komputer, jam tangan, TV Anda, bukan lagi individu terisolasi, melainkan "organ" dari satu kesatuan, bisa saling memanggil kemampuan satu sama lain.

Contoh: Anda menggunakan ponsel menonton video, ingin menonton di layar besar, cara tradisional adalah screen casting; sedangkan di HarmonyOS, Anda bisa langsung "mengalirkan" video ke TV untuk lanjut menonton, ponsel menjadi remote. Ini bukan screen casting sederhana, melainkan aplikasi itu sendiri berjalan lintas perangkat.

#### 2. HarmonyOS 4.3: Versi matang berbasis AOSP

HarmonyOS 4.3 adalah versi yang saat ini banyak di-deploy di ponsel Huawei. Perlu dijelaskan, HarmonyOS 4.3 kompatibel dengan code framework Android Open Source Project (AOSP), karena itu ia bisa kompatibel penuh dengan aplikasi Android—sebagian besar aplikasi yang Anda download dari Huawei AppGallery pada dasarnya masih aplikasi Android, berjalan melalui compatibility layer HarmonyOS. Tapi HarmonyOS 4.3 bukan sekadar shell Android, ia menambahkan banyak kemampuan distributed self-developed Huawei, Ark Engine, dan teknologi lain di atas AOSP.

##### Fitur inti:

- <strong>Kompatibilitas aplikasi Android</strong>: Karena dikembangkan berbasis AOSP, HarmonyOS 4.3 bisa menjalankan hampir semua aplikasi Android, pengguna hampir tidak merasakan perbedaan.
- <strong>Ark Engine</strong>: Compiler dan runtime self-developed Huawei, membuat aplikasi berjalan lebih lancar, lebih hemat daya. Dibanding versi awal, kelancaran meningkat jelas.
- <strong>Super terminal</strong>: Di control center, bisa secara intuitif melihat perangkat HarmonyOS lain di sekitar, drag untuk connect. Ponsel memanggil keyboard mouse komputer, tablet memanggil kamera ponsel, semua sangat mudah.
- <strong>Service card</strong>: Mirip widget iOS, tapi lebih fleksibel. Bisa swipe up icon aplikasi untuk expand card, menampilkan informasi kunci, tanpa membuka aplikasi.
- <strong>Mode Murni</strong>: Hanya mengizinkan instalasi aplikasi dari AppGallery resmi, mengurangi risiko malware.
- <strong>Privacy center</strong>: Mengelola izin aplikasi secara terpusat, melihat record perilaku aplikasi.

##### Karakteristik user interface:

- <strong>Magazine lock screen</strong>: Lock screen menampilkan gambar dan artikel cantik, swipe untuk masuk ke desktop.
- <strong>Universal card</strong>: Icon desktop bisa di-expand menjadi card, menampilkan lebih banyak informasi.
- <strong>Super hub</strong>: Area penyimpanan sementara, bisa menampung teks, gambar, file sementara, lalu drag ke aplikasi mana saja untuk digunakan. Sharing lintas aplikasi menjadi sangat halus.
- <strong>Smart search</strong>: Global search, bisa mencari aplikasi, file, pengaturan, webpage.

#### 3. HarmonyOS NEXT (HarmonyOS 6): Titik awal sejati sistem operasi self-developed Huawei

HarmonyOS NEXT (HarmonyOS NEXT 5.0) dan HarmonyOS 4.3 memiliki perbedaan mendasar—ia menggunakan microkernel HarmonyOS self-developed Huawei, tidak lagi bergantung pada kernel Linux dan kode AOSP, juga <strong>tidak lagi langsung mendukung aplikasi Android</strong>. Ini adalah langkah kunci HarmonyOS dari "bentuk transisi kompatibel Android" resmi menuju "sistem operasi sepenuhnya independen".

##### Perubahan besar:

- <strong>Kernel sepenuhnya self-developed</strong>: HarmonyOS NEXT menggunakan kernel self-developed Huawei, tidak lagi mengandung kode AOSP apa pun. Sistem lebih ringkas, lebih aman, lebih efisien.
- <strong>Tidak lagi mendukung aplikasi Android</strong>: Ini perubahan terbesar. HarmonyOS NEXT hanya bisa menjalankan aplikasi native HarmonyOS, tidak bisa instal dan jalankan file APK. Sebelum upgrade harap konfirmasi aplikasi yang sering Anda gunakan sudah punya versi native HarmonyOS.
- <strong>Ekosistem aplikasi native</strong>: Huawei sedang mendorong pengembang untuk migrasi aplikasi ke platform native HarmonyOS. Saat ini aplikasi mainstream seperti WeChat, Alipay, Taobao sudah merilis versi native HarmonyOS, tapi sebagian aplikasi niche mungkin belum diadaptasi.
- <strong>Arsitektur keamanan Star Shield</strong>: Sistem keamanan baru, perlindungan full-chain dari hardware ke software. Mendukung kontrol izin lebih granular, seperti "fuzzy location"—aplikasi hanya tahu Anda kira-kira di mana, tidak tahu lokasi presisi.
- <strong>Integrasi AI mendalam</strong>: Kemampuan AI system-level, bukan hanya aplikasi tertentu yang punya AI. Misalnya AI subtitle bisa real-time translate video, AI cutout bisa smart recognize subject.
- <strong>Cross-device seamless flow</strong>: Kemampuan distributed lebih lanjut. State aplikasi bisa switch seamlessly antar perangkat, dokumen yang Anda edit di ponsel, saat berjalan ke komputer otomatis terbuka di komputer.
- <strong>Meta service</strong>: Layanan lightweight yang bisa digunakan tanpa instalasi. Misalnya scan QR code langsung membuka fungsi tertentu, tanpa download aplikasi dulu.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Wajib baca sebelum upgrade ke HarmonyOS NEXT

{class="mt-1"}
Setelah upgrade ke HarmonyOS NEXT, ponsel Anda tidak akan bisa menjalankan aplikasi Android. Harap pastikan sebelum upgrade: ① Aplikasi yang sering Anda gunakan sudah punya versi native HarmonyOS; ② Pekerjaan atau kehidupan Anda tidak ada skenario yang harus bergantung pada aplikasi Android. Setelah upgrade tidak bisa rollback ke HarmonyOS 4.3.
:::

##### Perubahan logika operasi:

- <strong>Gesture navigation</strong>: Swipe edge kiri-kanan untuk back, swipe up dari bawah untuk kembali ke desktop, swipe up dan tahan untuk multi-task.
- <strong>Smart multi-window</strong>: Mendukung split-screen, floating window, parallel view dan berbagai bentuk multi-task lainnya.
- <strong>Changlian call</strong>: Layanan video call Huawei, mendukung screen sharing, beauty, background blur.

#### 4. Ekosistem HarmonyOS: Perangkat dan aplikasi

HarmonyOS bukan hanya sistem ponsel, melainkan ekosistem yang mencakup berbagai perangkat.

##### Tipe perangkat yang didukung:

- <strong>Ponsel dan tablet</strong>: Perangkat inti, fungsi paling lengkap.
- <strong>Smartwatch dan band</strong>: Berjalan independen atau berkolaborasi dengan ponsel.
- <strong>Smart screen (TV)</strong>: Pusat hiburan keluarga.
- <strong>Smart speaker</strong>: Portal interaksi suara.
- <strong>Mobil</strong>: HarmonyOS cockpit, pengalaman smart driving cabin.
- <strong>Rumah pintar</strong>: Kulkas, AC, mesin cuci, dll.

##### Status ekosistem aplikasi:

AppGallery HarmonyOS sudah memiliki jutaan aplikasi, App mainstream pada dasarnya tersedia. Huawei juga aktif mendorong pengembang membuat aplikasi native HarmonyOS. Per pertengahan 2026, WeChat, Alipay, Taobao, Douyin, Meituan, JD.com, dan aplikasi top lainnya sudah meluncurkan versi native HarmonyOS, penggunaan sehari-hari pada dasarnya tanpa hambatan. Beberapa aplikasi niche dan industri mungkin masih dalam penyesuaian, sebelum upgrade disarankan konfirmasi apakah App yang sering Anda gunakan sudah didukung.

#### 5. Tips praktis HarmonyOS

- <strong>Super terminal</strong>: Swipe down dari pojok kanan atas layar untuk membuka control center, klik "Super Terminal", bisa melihat perangkat lain di sekitar, drag untuk connect.
- <strong>Super hub</strong>: Long press teks/gambar/file, pilih "Copy to hub", lalu di aplikasi lain long press untuk paste, atau drag keluar.
- <strong>Service card</strong>: Swipe up icon aplikasi untuk expand card, long press card bisa adjust size atau add to desktop.
- <strong>Smart multi-window</strong>: Swipe dari edge kiri-kanan layar ke dalam dan tahan, buka sidebar, klik aplikasi untuk buka sebagai floating window.
- <strong>Privacy protection</strong>: Pengaturan &gt; Privasi, bisa melihat record penggunaan izin aplikasi, mengatur fuzzy location, dll.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Pengaturan dalam mode pengembang dapat mempengaruhi stabilitas sistem, opsi yang tidak dipahami jangan diubah sembarangan. Setelah mengaktifkan debugging USB, berhati-hatilah saat menghubungkan ke komputer, jangan hubungkan ke komputer yang tidak dipercaya.

{class="mt-1"}
Sistem HarmonyOS terus update dan iterasi, versi berbeda mungkin ada beberapa perbedaan. Deskripsi artikel ini berdasarkan fitur utama HarmonyOS 4.3 dan 6, fungsi spesifik harap merujuk pada versi aktual ponsel Anda. Disarankan menjaga sistem update, untuk mendapatkan fitur terbaru dan security patch.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Coba sekarang: Rasakan fitur khas HarmonyOS

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Buka control center, temukan "Super Terminal", lihat apakah ada perangkat HarmonyOS lain di sekitar.
2. Coba "Super hub": Copy sebagian teks ke hub, lalu drag keluar di Notes.
3. Swipe up beberapa icon aplikasi yang sering digunakan, lihat service card menampilkan konten apa.
4. Ke Pengaturan &gt; Privasi, lihat aplikasi mana yang baru-baru ini menggunakan izin sensitif.
:::
