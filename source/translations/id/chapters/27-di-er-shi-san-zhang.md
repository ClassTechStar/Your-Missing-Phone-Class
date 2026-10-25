---
id: di-er-shi-san-zhang
num: 23
part: chao-yue-pian
nav: Bab 23: Pengenalan Berpikir Pemrograman dan Otomatisasi
toc: default
kind: chapter
---

### Bab 23: Pemikiran Pemrograman dan Pengenalan Otomatisasi

{class="chapter-intro mb-4"}
Pada dua bab sebelumnya, kita membangun "dinding batas" keamanan untuk ponsel dan melihat "otak AI" yang semakin cerdas di dalamnya. Sekarang, mari kita buka salah satu potensi tertinggi ponsel: membuatnya "berpikir" seperti programmer dan secara otomatis menyelesaikan tugas beruntun yang Anda tentukan. Anda mungkin berkata: "Saya tidak bisa menulis kode, apa hubungannya dengan saya?" Tenang, bab ini tidak mengharuskan Anda menulis satu baris kode pun—ponsel modern telah menurunkan ambang "pemrograman" ke tingkat drag-and-drop.

#### 1. Apa Sebenarnya Otomatisasi Itu?

Dalam bahasa sederhana, otomatisasi adalah:<strong>membiarkan ponsel secara otomatis melakukan serangkaian hal untuk Anda saat suatu kondisi terpenuhi.</strong> Anda tidak perlu mengoperasikan secara manual setiap kali, juga tidak perlu mengingat apa yang harus dilakukan—ponsel akan menilai waktunya sendiri dan mengeksekusinya sendiri.

Contoh: Setiap pagi saat Anda bangun, Anda harus mematikan mode jangan ganggu secara manual, membuka WeChat untuk melihat pesan, membuka App cuaca untuk melihat apa yang harus dipakai hari ini, membuka NetEase Cloud untuk memutar lagu. Jika langkah-langkah ini dikemas menjadi satu alur otomatisasi, diatur ke "eksekusi otomatis setiap pagi jam 7", maka saat Anda bangun, Anda hanya perlu mengambil ponsel, semuanya sudah siap. Bukankah menyenangkan membayangkannya?

Otomatisasi pada dasarnya adalah rantai logika "jika... maka...", if-else dalam pemrograman. Begitu Anda memahami cara berpikir ini, bahkan jika Anda tidak pernah menulis kode seumur hidup, keteraturan Anda dalam menangani masalah akan jauh lebih baik. Elemen inti:

1. <strong>Kondisi pemicu</strong>: Kapan mulai? Bisa "setiap pagi jam 7", "saat saya terhubung ke Wi-Fi rumah", "saat saya tiba di lokasi tertentu", "saat baterai ponsel di bawah 20%".
2. <strong>Tindakan eksekusi</strong>: Apa yang harus dilakukan? Bisa mengirim pesan WeChat, membuka App tertentu, menyesuaikan volume, mengganti wallpaper, memutar musik, mengirim notifikasi... hampir semua yang bisa Anda lakukan secara manual di ponsel, otomatisasi bisa melakukannya.
3. <strong>Logika perantara</strong>(opsional tapi sangat kuat): Jika situasi A maka lakukan X, jika tidak lakukan Y. Misalnya "jika hari kerja maka putar podcast berita, akhir pekan maka putar musik", ini disebut percabangan kondisional.

#### 2. "Shortcuts" iOS—Senjata Otomatisasi Pengguna Apple

App "Shortcuts" Apple adalah aplikasi bawaan, tidak perlu diunduh. Konsep intinya adalah menyusun berbagai operasi seperti balok bangunan. Pertama, beberapa konsep kunci:

- <strong>"Shortcut"</strong>: Alur otomatisasi lengkap, bisa dijalankan dengan klik manual, atau dipanggil melalui suara Siri. Misalnya Anda bilang "Hey Siri, mode pulang", ia akan otomatis mengeksekusi serangkaian operasi yang Anda atur.
- <strong>"Automation"</strong>: Instruksi yang berjalan otomatis oleh kondisi pemicu, tidak perlu Anda picu secara manual. Misalnya "saat ponsel terhubung ke Bluetooth mobil, otomatis buka App peta". Otomatisasi diatur di tab "Automation", terpisah dari "Shortcut".
- <strong>"Action"</strong>: Unit eksekusi terkecil. Membuka App adalah satu action, mengirim pesan adalah satu action, mendapatkan cuaca adalah satu action, menyesuaikan kecerahan adalah satu action. Anda bisa merangkai ratusan action bersama.

Berikut beberapa contoh praktis yang benar-benar berguna, Anda akan mengerti setelah mencobanya:

##### Contoh 1: "Alur Selamat Pagi" Satu Klik

Setiap pagi klik sekali (atau bilang ke Siri "selamat pagi"), ponsel akan otomatis: mendapatkan cuaca hari ini → membacakan cuaca dan suhu → menampilkan jadwal kalender hari ini → membuka App musik favorit Anda dan mulai memutar. Langkah operasi: Buat shortcut baru → tambah action "Dapatkan Cuaca Saat Ini" → tambah "Bacakan Teks" → tambah "Dapatkan Acara Kalender" → tambah "Tampilkan Pengingat" → tambah "Buka App" pilih NetEase Cloud Music. Sesederhana itu, sepanjang proses drag-and-drop.

##### Contoh 2: "Mode Hemat Baterai" Otomatis

Di tab "Automation", buat automation baru → pilih "Level Baterai" → setel "di bawah 30%" → tambah action "Setel Mode Daya Rendah ke Aktif", "Kurangi Kecerahan Layar ke 30%", "Matikan Bluetooth". Sekarang ponsel akan otomatis masuk mode hemat daya saat baterai di bawah 30%, tidak perlu Anda khawatir.

##### Contoh 3: Catatan Keuangan Otomatis Setelah Scan Kode

Setiap kali Anda membayar dengan scan kode WeChat/Alipay, ponsel akan membaca notifikasi pembayaran, otomatis mencatat jumlah dan merchant ke memo atau spreadsheet Numbers. Ini memerlukan kondisi pemicu "menerima SMS/notifikasi" di "Automation" Shortcuts (iOS 17+ mendukung pembacaan transaksi Wallet), dipadukan dengan action "Tambah ke Numbers". Bagi yang ingin mencatat pengeluaran tapi malas mencatat manual, ini penyelamat.

Ada satu trik yang tidak banyak diketahui: Anda bisa menambahkan shortcut ke layar utama, menjadi ikon App. Misalnya buat shortcut "Pulang dengan Taksi", letakkan ikon di desktop, klik sekali langsung membuka Didi dan mengatur tujuan ke rumah, jauh lebih cepat daripada Anda membuka App dan mengetik perlahan.

#### 3. Otomatisasi Android—Tasker dan Teman-temannya

Di sisi Android, situasinya sedikit lebih kompleks, tapi langit-langitnya juga lebih tinggi. Pertama, yang sederhana:

##### Level Pemula: Auto Clicker

Banyak ponsel Android memiliki "Auto Clicker" bawaan atau bisa diunduh di app store. Prinsipnya sangat sederhana: Anda mengoperasikan secara manual sekali, ia merekam koordinat klik dan interval waktu Anda, lalu bisa memutar ulang dengan kecepatan tinggi. Misalnya App tertentu memberi hadiah check-in harian, Anda rekam sekali alur klik, setelah itu otomatis berjalan setiap hari. Kekurangannya: Ia hanya mengenali koordinat, jika tata letak antarmuka berubah (misalnya muncul iklan), ia akan klik salah.

##### Level Menengah: Tasker—Raja Otomatisasi Android

Tasker adalah alat otomatisasi terkuat yang diakui di platform Android, mendominasi puncak secara konsisten. Sejujurnya kurva belajarnya agak curam, antarmukanya tidak terlalu bagus, tapi begitu terbiasa, Anda akan merasa ponsel tiba-tiba menjadi serba bisa. Inti Tasker juga pola "picu → tugas":

- <strong>Profile</strong>: Mendefinisikan "kapan memicu". Kondisi pemicu bisa waktu, lokasi, status koneksi Wi-Fi, koneksi Bluetooth, menerima notifikasi tertentu, status baterai, orientasi layar... kondisi pemicu yang didukung Tasker absurd banyaknya, ada puluhan.
- <strong>Task</strong>: Mendefinisikan "apa yang dilakukan setelah picu". Satu tugas bisa berisi beberapa action, dieksekusi secara berurutan. Jenis action meliputi: menyesuaikan pengaturan sistem (volume, kecerahan, Wi-Fi, Bluetooth, mode pesawat), mengirim SMS, permintaan HTTP, mengeksekusi perintah Shell, mengontrol pemutaran media, menampilkan dialog, dll.

Berikut beberapa skenario klasik praktis Tasker:

- <strong>Otomatis nyalakan Wi-Fi saat tiba di rumah</strong>: Atur kondisi pemicu ke "terhubung ke BTS tertentu" (karena di dekat rumah Anda akan terhubung ke BTS tetap) → tugas "Nyalakan Wi-Fi". Tanpa GPS dan tidak boros daya, ponsel otomatis menyalakan Wi-Fi saat masuk area perumahan.
- <strong>Mode rapat</strong>: Kondisi pemicu "Judul acara kalender mengandung 'rapat'" → tugas "Setel mode senyap, matikan volume media, balas WeChat otomatis (perlu plugin)". Tidak perlu lagi khawatir ponsel tiba-tiba berdering saat rapat.
- <strong>Mode melindungi mata tengah malam</strong>: Kondisi pemicu "Waktu 22:00-06:00" → tugas "Aktifkan mode melindungi mata, kurangi kecerahan ke 20%, setel layar ke hitam-putih (mode grayscale)". Layar hitam-putih sangat efektif untuk mengurangi keinginan menonton video pendek—begitu layar menjadi abu-abu, Anda tidak ingin menonton lagi.
- <strong>Otomatis putar podcast saat earphone dicolok</strong>: Kondisi pemicu "earphone berkabel dicolok / earphone Bluetooth terhubung" → tugas "Buka App Xiaoyuzhou dan mulai putar episode terbaru". Pakai earphone langsung bisa mendengarkan, tanpa perlu membuka kunci ponsel mencari App.

Jika Anda merasa Tasker terlalu sulit, cobalah versi sederhananya:<strong>MacroDroid</strong>. Antarmuka jauh lebih ramah, template lengkap, cocok untuk pengguna yang tidak ingin repot. Selain itu, banyak sistem Android domestik sekarang (MIUI Xiaomi, HarmonyOS Huawei, ColorOS OPPO) memiliki fungsi "skenario" atau "asisten cerdas" bawaan, meskipun tidak sekuat Tasker, untuk otomatisasi sehari-hari sudah lebih dari cukup.

#### 4. Aplikasi Sehari-hari Pemikiran Otomatisasi

Hasil terbesar dari mempelajari otomatisasi sebenarnya bukan menghemat sedikit waktu, melainkan <strong>mengubah cara Anda berpikir tentang masalah</strong>. Begitu Anda terbiasa dengan pola pikir "jika X terjadi, otomatis lakukan Y", Anda akan menemukan banyak pekerjaan repetitif dalam kehidupan yang bisa dihilangkan. Misalnya:

- Setiap kali selesai memotret, otomatis backup ke cloud lalu kompres foto lokal ke ukuran kecil untuk menghemat ruang.
- Setiap pagi otomatis membaca jadwal hari ini dari kalender, menghasilkan teks dan mengirimkannya ke keluarga melalui WeChat.
- Setelah menerima SMS tanda terima paket, otomatis menambahkan to-do "ambil paket" di memo.
- Saat baterai ponsel penuh, otomatis memberi pengingat suara untuk mencabut charger (menghindari overcharge yang merusak baterai).
- Setiap hari saat jam pulang tiba, jika masih di dekat kantor (melalui lokasi BTS), otomatis mengingatkan "saatnya pulang".

Hal-hal ini terdengar canggih, tapi sebenarnya selama Anda menguasai dua konsep dasar "picu + tindakan", dengan Shortcuts atau Tasker, semuanya bisa dibuat. Kuncinya adalah <strong>Anda harus terlebih dahulu menyadari "hal ini bisa diotomatisasi"</strong>—banyak orang bukan tidak bisa, tapi tidak pernah berpikir ke arah itu.

#### 5. Panduan Jebakan: Masalah Umum Otomatisasi

Otomatisasi tidak selalu mulus, ada beberapa jebakan yang sudah saya lalui untuk Anda:

- <strong>Pemicu lokasi mungkin tidak akurat</strong>: "Tiba/Meninggalkan lokasi" iOS menggunakan teknologi geofencing, akurasi tergantung sinyal GPS dan optimasi sistem. Kadang Anda sudah sampai di rumah 10 menit baru terpicu. Disarankan menggunakan pemicu koneksi Wi-Fi atau BTS sebagai pengganti pemicu lokasi, lebih andal dan lebih hemat daya.
- <strong>"Automation" Shortcuts perlu otorisasi</strong>: Di iOS, sebagian besar pemicu di tab "Automation" perlu konfirmasi manual untuk berjalan (mekanisme keamanan iOS). Tapi pemicu koneksi Wi-Fi, koneksi Bluetooth, dan alarm berhenti bisa benar-benar berjalan otomatis tanpa konfirmasi.
- <strong>Tasker perlu mengaktifkan izin aksesibilitas</strong>: Banyak fungsi lanjutan (seperti simulasi klik) memerlukan izin layanan aksesibilitas, ini akan membuat ponsel menampilkan notifikasi permanen di pengaturan. Ini adalah desain keamanan Android, tidak bisa dihilangkan.
- <strong>Jangan buat otomatisasi terlalu kompleks</strong>: Saat baru mulai otomatisasi, mulailah dengan alur kecil "2-3 action". Jangan langsung membuat alur super 20 langkah—debugging akan membuat Anda gila.

::: div .success-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Tip: Cara yang Tepat untuk Memulai Otomatisasi

{class="mt-1"}
Luangkan 5 menit untuk berpikir: Apa 3 hal yang paling sering Anda ulangi di ponsel setiap hari? Misalnya rutinitas pagi, kebiasaan setiap kali menghubungkan earphone Bluetooth, pengaturan sebelum bepergian... mulailah dari hal-hal kecil frekuensi tinggi ini, buat satu otomatisasi sederhana untuk masing-masing. Bahkan jika setiap otomatisasi hanya menghemat 5 detik, akumulasi seiring waktu sangat signifikan. Dan kepuasan setelah membuatnya benar-benar adiktif.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Mari Berlatih: Tiga Tantangan Otomatisasi Pemula

{class="mt-1 mb-2"}
Pilih satu yang paling cocok untuk Anda, setelah selesai Anda sudah lulus dasar:

{class="list-decimal pl-6 mt-1 space-y-1"}
1. <strong>Tantangan 1: Otomatisasi selamat pagi</strong>: iOS: Di App Shortcuts buat shortcut baru → tambah "Dapatkan Cuaca Saat Ini" → "Bacakan Teks" → "Buka App pilih NetEase Cloud". Setelah selesai Anda bisa bilang ke Siri "selamat pagi" untuk memicu. Android: Di Tasker buat tugas baru → tambah "Dapatkan Cuaca" → "Bacakan" → "Buka App" → setel waktu pemicu setiap hari 7:00.
2. <strong>Tantangan 2: Hemat baterai otomatis saat baterai rendah</strong>: iOS: Tab Automation → Baru → "Level Baterai" → di bawah 25% → tambah "Setel Mode Daya Rendah Aktif" + "Setel Kecerahan 25%". Android: Tasker buat Profile → Status → Daya → Baterai 0-25% → Tugas "Mode Hemat Daya Aktif" + "Kurangi Kecerahan".
3. <strong>Tantangan 3: Navigasi otomatis saat terhubung Bluetooth mobil</strong>: iOS: Automation → Baru → "Bluetooth" → pilih Bluetooth mobil Anda → tambah "Buka App pilih Amap" + "Volume Media ke 80%". Android: Tasker → Profile → Status → Bluetooth Terhubung → pilih Bluetooth mobil → Tugas "Buka Amap" + "Naikkan Volume Media".
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Studi Kasus 3: Otomatisasi "Routine Selamat Pagi"

{class="list-disc pl-6 mt-1 space-y-1"}
- <strong>Skenario</strong>: Setiap hari 7:00 otomatis bacakan cuaca + matikan silent + buka berita.
- <strong>Langkah</strong>: iOS: Shortcuts → Automation → Time Trigger → Add "Get Weather" + "Set Volume" + "Open App"; Android: MacroDroid → Trigger (Time 7:00) → Action (Media Volume / Open URL / TTS Read Weather).
- <strong>Hasil yang Diharapkan</strong>: Tanpa install bisa implementasi, menurunkan barrier entry.
:::
