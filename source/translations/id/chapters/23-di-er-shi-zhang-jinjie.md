---
id: di-er-shi-zhang-jinjie
num: 20
part: jin-jie-pian
nav: Bab 20: Mode Pengembang dan Hak Akses Tingkat Lanjut
toc: default
kind: supplement
---

### Bab 20: Mode pengembang dan izin lanjutan

{class="chapter-intro mb-4"}
1\. Mode pengembang: Buka pengaturan tersembunyi

#### 1. Mode pengembang: Buka pengaturan tersembunyi

Cara mengaktifkan:

##### Android

- <strong>Android</strong> HarmonyOS
- <strong>HarmonyOS</strong> iOS
- <strong>: Pengguna biasa tidak dapat mengaktifkan mode pengembang lengkap, membutuhkan akun Apple Developer berbayar.</strong> Fungsi yang umum digunakan:

##### Daftar fungsi umum:

- <strong>: Menghubungkan ke komputer untuk operasi lanjutan, seperti flashing, pemulihan data.</strong>: Saklar wajib aktif untuk operasi advanced koneksi ke komputer (seperti flashing, recovery data, perintah ADB), detail lihat bagian "Perintah ADB Praktis" bab ini.
- <strong>: Menampilkan titik sentuh di layar, cocok untuk merekam tutorial.</strong>: Tampilkan touch point di layar (titik kecil mengikuti jari), cocok untuk rekam tutorial operasi atau demo.

##### Terkait performa dan kelancaran:

- <strong>Adjust kecepatan animasi (Window animation scale / Transition animation scale / Animator duration scale)</strong>: Tiga opsi ini mengontrol durasi animasi saat buka App dan switch page. Default 1x, setel ke 0.5x akan membuat ponsel "terlihat" lebih cepat (sebenarnya kecepatan running program tidak berubah, hanya animasi lebih cepat), setel ke off maka langsung jump tanpa animasi. Kebanyakan geek akan setel 0.5x, tetap ada sense transisi tapi terlihat cepat; fully off akan membuat operasi terlihat kaku, dan mungkin menutupi lag nyata program, justru membuat Anda salah mengira "sangat lancar".
- <strong>Force GPU Rendering</strong>: Memaksa semua drawing 2D via GPU bukan CPU. Pada model lama atau beberapa App yang tidak optimal bisa meningkatkan kelancaran scroll, tapi juga akan menambah beban GPU dan konsumsi daya. Ponsel modern default sudah banyak memakai GPU rendering, saklar ini pada model mid-to-high end dampaknya terbatas, lebih merupakan opsi warisan sejarah, pengguna biasa biarkan default.
- <strong>Profile GPU Rendering</strong>: Menampilkan di layar dengan bar chart real-time waktu render per frame, garis hijau horizontal mewakili 16.6ms (threshold frame time 60fps). Bar melebihi garis hijau berarti dropped frame. Ini senjata developer untuk troubleshoot lag App, pengguna biasa juga bisa pakai untuk membandingkan App mana yang optimalisasinya buruk — misalnya suatu App saat scroll bar sering melebihi garis merah, itu pada dasarnya salahnya.

##### Terkait background dan battery life:

- <strong>: Membatasi jumlah aplikasi yang berjalan di latar belakang, menghemat daya.</strong>: Bisa setel "Standard limit" "Maks 1 proses" "Maks 2 proses", dll. Sepintas membatasi proses background bisa hemat baterai, tapi sebenarnya background management bawaan Android sudah cukup baik, membatasi secara paksa justru menyebabkan App sering reload (cold start justru lebih boros daya, pengalaman juga buruk). Opsi ini lebih cocok untuk debugging, tidak disarankan pengguna biasa aktifkan jangka panjang, biarkan "Standard limit".
- <strong>Don't Keep Activities</strong>: Setiap keluar dari satu antarmuka langsung destroy. Sangat tidak direkomendasikan, akan menyebabkan App sering white screen dan reload, hanya untuk test recovery logic App.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Pengaturan dalam mode pengembang dapat mempengaruhi stabilitas sistem, opsi yang tidak dipahami jangan diubah sembarangan. Setelah mengaktifkan debugging USB, berhati-hatilah saat menghubungkan ke komputer, jangan hubungkan ke komputer yang tidak dipercaya.

{class="mt-1"}
2\. BL lock (Bootloader lock): Pintu pertama flashing
:::

#### 2. OEM Unlocking: "Saklar Flashing" di Developer Options

Di Developer Options ada saklar yang tidak mencolok tapi sangat penting — "OEM unlocking" (sebagian merek menyebutnya "OEM unlocking allow" atau "Device unlock"). Saklar ini sendiri tidak akan unlock BL lock, tapi merupakan "prasyarat izin": hanya jika diaktifkan, vendor baru mengizinkan Anda unlock BL via perintah fastboot atau tool vendor.

- <strong>Fungsi Saklar</strong>: Setara dengan deklarasi ke vendor "saya setuju melepaskan garansi, risiko ditanggung sendiri, tolong izinkan saya unlock BL". Jika saklar ini off, semua perintah unlock BL akan langsung ditolak.
- <strong>Hubungan dengan BL Lock</strong>: OEM unlocking adalah "mengajukan kualifikasi", BL unlock adalah "operasi aktual". Yang pertama di settings ponsel klik saja, yang kedua perlu ke situs vendor mengajukan unlock code, pakai komputer jalankan perintah fastboot (seperti <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">fastboot flashing unlock</code>), keduanya tidak boleh kurang satu pun.
- <strong>Apakah Factory Reset Akan Reset?</strong>: Ya. Saklar "OEM unlocking" setelah factory reset akan kembali ke status off, tapi BL lock sekali di-unlock adalah status fisik level, tidak akan re-lock karena factory reset — perlu manual execute <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">fastboot flashing lock</code> untuk bisa re-lock.
- <strong>Kapan Harus Dibuka</strong>: Kecuali Anda yakin ingin flashing atau Root, jika tidak biarkan off. Ini dan "USB debugging" adalah dua saklar independen, saat flashing biasanya perlu sekaligus dibuka.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Trivia: Mengapa Vendor Menyetel Saklar Ini

{class="mt-1"}
Awalnya Android tidak punya saklar ini, malware selama dapat permission bisa diam-diam flash system. Google kemudian mewajibkan semua vendor Android menambahkan saklar "OEM unlocking" di Developer Options, sebagai konfirmasi "persetujuan pengguna yang informed". Inilah sebabnya bahkan jika Anda sudah unlock BL lock, jika saklar OEM unlocking off, re-flash tetap akan gagal.
:::

#### 3. BL Lock (Bootloader Lock): Pintu Pertama Flashing

Fungsi BL lock:

##### Perlindungan keamanan

- <strong>: Mencegah malware di-flash ke sistem.</strong> Anti-pencurian
- <strong>: Bahkan jika ponsel di-flash, tanpa kata sandi akun asli tidak dapat digunakan.</strong> Batasan garansi
- <strong>: Membuka BL biasanya berarti kehilangan garansi resmi.</strong> Kebijakan BL lock setiap merek:

##### Xiaomi

- <strong>Xiaomi</strong> Huawei
- <strong>Huawei</strong> OnePlus
- <strong>: Dapat di-unlock, relatif longgar.</strong> OPPO/vivo
- <strong>: Sebagian model dapat di-unlock, perlu pengajuan.</strong> Samsung
- <strong>Samsung</strong> Apple
- <strong>Apple</strong>3. Izin Root: "Administrator super" Android

#### 4. Perintah ADB Praktis: Kontrol Ponsel via Komputer

ADB kepanjangan Android Debug Bridge, adalah command line tool resmi dari Google, membuat komputer berkomunikasi dengan ponsel Android via USB atau Wi-Fi. Itu sendiri tidak butuh Root, selama ponsel aktifkan "USB debugging" bisa dipakai. Bisa dipahami sebagai "remote control yang memberi instruksi ke ponsel via komputer" — flashing, install App, transfer file, cek log, semua mengandalkannya.

##### Cara connect via USB:

1. Sisi ponsel: Masuk Developer Options → aktifkan "USB debugging".
2. Sisi komputer: Download Platform Tools dari situs resmi Google (berisi <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb</code> "dalam kondisi apa" <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">fastboot</code> dua file executable), extract ke direktori mana pun.
3. Hubungkan ponsel dan komputer dengan kabel data, di ponsel akan muncul pop-up "Allow USB debugging?", centang "Always allow" dan OK.
4. Di command line komputer (PowerShell atau cmd Windows) execute <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb devices</code>, jika output mirip <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">List of devices attached / xxxxxxxx device</code>, berarti sudah terhubung.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Driver dan Pop-up Otorisasi Jangan Diabaikan

{class="mt-1"}
Pengguna Windows jika <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb devices</code> menampilkan "unauthorized" atau tidak menampilkan device, kemungkinan driver belum terinstall atau lupa klik "Allow" di ponsel. Merek seperti Samsung/Xiaomi bisa install "USB driver" atau "Phone Assistant" masing-masing untuk melengkapi driver; Mac dan Linux umumnya tanpa driver. Jika pop-up ponsel tidak sengaja di-close, cabut-colok kabel data akan muncul lagi.
:::

##### Perintah ADB umum:

- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb install app.apk</code>: Install APK dari komputer ke ponsel (<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-r</code> berarti overwrite install dan retain data;<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-s</code> install ke SD card).
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb uninstall com.xxx.xxx</code>: Uninstall App berdasarkan package name.
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb push [path komputer] /sdcard/[path target]</code>: Push file dari komputer ke ponsel.
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb pull /sdcard/[file] [path komputer]</code>: Pull file dari ponsel ke komputer (jauh lebih cepat daripada kirim ke WeChat sendiri lalu download).
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell</code>: Masuk Linux Shell ponsel, bisa langsung execute <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">ls</code>,<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pm</code>,<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">am</code> dan perintah lain.
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb reboot bootloader</code>: Reboot ponsel masuk Fastboot mode (entry flashing).
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb reboot recovery</code>: Reboot masuk Recovery mode.
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm list packages</code>: List package name semua aplikasi yang terinstall di ponsel (wajib untuk cari package name). Tambah <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-s</code> hanya lihat sistem app, tambah <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-3</code> hanya lihat app pihak ketiga.
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm uninstall --user 0 [package name]</code>: Uninstall pre-installed App untuk current user, tanpa Root, lihat praktik di bawah.

##### Praktik uninstall pre-installed App tanpa Root:

Ini salah satu fungsi ADB paling praktis: pakai <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pm uninstall --user 0</code> perintah bisa uninstall pre-installed App untuk "current user", tanpa perlu Root, juga tidak mempengaruhi system partition. App yang di-uninstall "hilang" dari sistem, tapi sebenarnya masih di system partition, setelah factory reset akan kembali.

1. Pertama pakai <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm list packages -s</code> list semua sistem app, cari package name yang ingin Anda uninstall. Misalnya browser Xiaomi adalah <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.browser</code>, Huawei AppGallery adalah <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.vmall.client</code>.
2. Tidak yakin package name sesuai App mana? Bisa di komputer pakai <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm list packages | findstr [keyword]</code> untuk search, atau install App pihak ketiga "Package Viewer" di ponsel untuk langsung lihat package name setiap App.
3. Execute uninstall:<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm uninstall --user 0 [package name]</code>, misalnya <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm uninstall --user 0 com.android.browser</code>. Return <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">Success</code> berarti sukses.
4. Ingin restore? Dua metode: ① Factory reset (paling thorough tapi repot); ② Reinstall:<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell cmd package install-existing [package name]</code>.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-skull-crossbones mr-2"></i>Jangan Sembarangan Hapus Paket Inti Sistem

{class="mt-1"}
"pm uninstall --user 0" meskipun adalah cara aman tanpa Root, tapi sembarangan hapus sistem app kunci (seperti <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.systemui</code> status bar,<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.phone</code> telepon,<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.settings</code> settings) akan menyebabkan sistem crash, black screen, tidak bisa boot, dan masalah serius lainnya. Sebelum hapus, Google dulu "apakah package name ini bisa dihapus", lebih baik hapus sedikit daripada salah hapus. Disarankan sekali hanya hapus satu-dua, konfirmasi tidak ada masalah baru lanjut.
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Trivia: Apa Arti --user 0

{class="mt-1"}
Sejak Android 4.2 mendukung multi-user, setiap user punya ID independen (owner adalah 0, additional user mulai dari 10).<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">--user 0</code> berarti "hanya uninstall untuk owner saat ini", file APK di system partition masih ada, hanya tidak ditampilkan ke owner. Inilah sebabnya tidak butuh Root — tidak menyentuh file sistem, hanya mengubah "user config". Ini juga perbedaan terbesar dengan uninstall setelah Root: uninstall Root benar-benar hapus dari sistem, semua user tidak lagi punya; uninstall ADB hanya "sembunyi untuk current user".
:::

#### 5. Root Permission: "Super Administrator" Android

Root permission setara dengan super user di Linux (punya kontrol penuh atas direktori /, bisa read-write file apa pun), adalah permission tertinggi sistem Android. Berbeda fundamental dengan Administrator Windows: Windows karena pertimbangan keamanan membatasi administrator dalam banyak hal (permission tertinggi sebenarnya adalah TrustedInstaller), bahkan Administrator juga tidak bisa seperti Linux root langsung execute <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">sudo rm -rf /*</code>. Setelah mendapatkan Root permission, Anda bisa memodifikasi file sistem, uninstall pre-installed app, menggunakan App advanced yang butuh Root.

##### Meng-uninstall aplikasi pre-installed yang tidak bisa di-uninstall.

- Menggunakan aplikasi fungsi lanjutan (seperti Titanium Backup, Greenify).
- Memodifikasi antarmuka dan fungsi sistem.
- Memasang Recovery pihak ketiga dan custom ROM.
- Risiko Root:

##### Kehilangan garansi

- <strong>Hilang garansi</strong> Risiko keamanan
- <strong>: Aplikasi berbahaya mungkin mendapatkan izin Root, menyebabkan konsekuensi serius.</strong> Sistem tidak stabil
- <strong>: Kesalahan operasi dapat menyebabkan sistem crash.</strong> Aplikasi bank tidak bisa digunakan
- <strong>: Banyak aplikasi bank dan pembayaran mendeteksi Root akan menolak berjalan.</strong> Update OTA gagal
- <strong>: Mungkin tidak dapat menerima update sistem resmi secara normal.</strong> Peringatan serius

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-skull-crossbones mr-2"></i>Operasi Root memiliki risiko tertentu, dapat menyebabkan ponsel brick (tidak bisa dinyalakan). Jika Anda pemula, disarankan memahami pengetahuan terkait secara menyeluruh dulu, dan pastikan ada cadangan lengkap. Sebelum operasi baca tutorial dengan teliti, konfirmasikan model ponsel dan versi sistem Anda.

{class="mt-1"}
4\. Saran untuk pengguna biasa
:::

#### 6. Sertifikasi SafetyNet dan Play Integrity: Mengapa App Bank Tidak Bisa Dipakai Setelah Root

Banyak pengguna Root pernah mengalami momen frustrasi seperti ini: setelah Root dengan antusias install banyak module, hasilnya buka App bank — "Perangkat Anda tidak aman, tidak bisa digunakan", Google Pay juga tidak bisa dipakai, bahkan Netflix menolak playback HD. Di balik ini adalah dua set mekanisme sertifikasi integritas perangkat Google: SafetyNet lama dan Play Integrity API baru.

##### Apa itu SafetyNet / Play Integrity:

- <strong>SafetyNet Attestation (versi lama, sejak 2017)</strong>: API cek integritas perangkat yang diluncurkan Google awal, app via ini query ke server Google "apakah perangkat ini lulus uji kompatibilitas CTS, apakah dalam status resmi yang tidak dimodifikasi". Return result dibagi Basic Attestation (verifikasi dasar) dan Strong Attestation (verifikasi kuat, bergantung hardware key). Google sudah umumkan SafetyNet akan bertahap discontinued setelah 2024.
- <strong>Play Integrity API (versi baru, sejak 2022)</strong>: Solusi pengganti yang diluncurkan Google, lebih ketat dan komprehensif daripada SafetyNet. Selain integritas perangkat, juga termasuk "integritas aplikasi" (apakah App di-tamper) dan "integritas akun/otorisasi" (apakah akun pengguna dipercaya Google). App baru harus migrasi ke Play Integrity.
- <strong>Siapa yang Memakai</strong>: App bank, finansial, pembayaran (seperti Google Pay, mobile banking berbagai bank, sebagian skenario Alipay/WeChat Pay), streaming media (perlindungan hak cipta HD Netflix), sebagian anti-cheat game (seperti sebagian game Tencent/NetEase), App office enterprise (cek kepatuhan perangkat MDM).

##### Tiga tingkat hasil sertifikasi Play Integrity:

- <strong>MEETS_DEVICE_INTEGRITY (Integritas perangkat lulus)</strong>: Perangkat menjalankan sistem Android resmi, Bootloader tidak di-unlock, tidak Root, lulus uji kompatibilitas CTS. Bisa normal memakai App bank, pembayaran.
- <strong>MEETS_BASIC_INTEGRITY (Integritas dasar lulus)</strong>: Perangkat pada dasarnya terpercaya, tapi mungkin ada anomali ringan. Beberapa App akan degrade penggunaan (seperti Netflix masih bisa play tapi batasi resolusi), beberapa App bank ketat akan langsung menolak.
- <strong>MEETS_STRONG_INTEGRITY (Integritas kuat lulus)</strong>: Level tertinggi, butuh dukungan hardware key (seperti chip Titan M seri Google Pixel), kebanyakan model merek pihak ketiga bahkan tanpa Root juga tidak mencapai level ini.
- <strong>Tanpa label (NO_INTEGRITY)</strong>: Perangkat sudah Root, BL di-unlock, flash ROM pihak ketiga atau diidentifikasi sebagai emulator, mayoritas App pembayaran/bank akan langsung menolak running.

##### Mengapa App ini tidak berfungsi setelah Root:

App via Play Integrity API mengirim permintaan sertifikasi ke server Google, Google akan cek banyak indikator perangkat — status lock Bootloader, apakah system partition dimodifikasi, apakah ada binary su, apakah SELinux dalam mode permissive, dll. Satu pun anomali akan menyebabkan level sertifikasi yang di-return menurun atau kosong, App bank melihat "perangkat tidak aman", natural menolak layanan.

##### Solusi penyembunyian modern: Magisk Hide / Shamiko / Zygisk:

Untuk menikmati kemudahan Root bersamaan masih bisa pakai App bank, komunitas mengembangkan serangkaian solusi "menyembunyikan status Root". Ide inti semua: membuat program deteksi melihat bukan sistem yang dimodifikasi, tapi perangkat yang "terlihat normal".

- <strong>Magisk</strong>: Solusi Systemless Root paling mainstream saat ini — tidak memodifikasi system partition, tapi via mounting mencapai Root. Keuntungan desain ini adalah kemungkinan gagal OTA update kecil, uninstall cukup bersih, adalah fondasi semua solusi penyembunyian berikutnya. Tapi memakai Magisk masih perlu unlock BL lock.
- <strong>Magisk Hide (sudah discontinued)</strong>: Module hide built-in Magisk awal, bisa hide Root untuk App tertentu. Tapi sejak 2021 sudah dihapus oleh Magisk official, alasannya Google terus meningkatkan metode deteksi, kedua pihak terjebak dalam "permainan kucing dan tikus".
- <strong>Zygisk</strong>: Mekanisme baru yang diperkenalkan Magisk 24.0+, mirip Riru, via inject proses Zygote mencapai module loading, lebih tersembunyi daripada langsung memodifikasi sistem. Mengaktifkan Zygisk adalah prasyarat memakai solusi hide modern.
- <strong>Shamiko</strong>: Module hide paling mainstream saat ini, bekerja sama dengan Zygisk, bisa hide Root untuk App tertentu (mode "reverse whitelist"), hide Magisk itu sendiri, memalsukan status Bootloader lock. Shamiko didistribusikan via repo LSPosed atau GitHub.
- <strong>Play Integrity Fix(osm0sis)</strong>: Module Magisk khusus untuk deteksi Google Play Integrity, akan memodifikasi device fingerprint membuat Google menganggap perangkat Anda adalah model resmi yang belum Root.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Permainan Kucing dan Tikus Tidak Pernah Berakhir

{class="mt-1"}
Google setiap sekali waktu akan update aturan deteksi, vendor App juga akan ikut upgrade verifikasi Play Integrity. Solusi hide yang masih bisa dipakai hari ini, besok mungkin sudah diidentifikasi. Jika Anda sepenuhnya mengandalkan App bank/pembayaran (misalnya transfer harian, scan QR bayar), pilihan paling aman tetap: jangan Root, jangan unlock BL lock. Solusi hide lebih cocok untuk konfigurasi player "ponsel utama tidak Root + ponsel cadangan main Root".
:::

#### 7. Saran untuk Pengguna Biasa

- <strong>: Bisa diaktifkan, rasakan fungsi seperti akselerasi animasi, tetapi jangan mengubah pengaturan lain sembarangan.</strong>: Bisa diaktifkan, rasakan accelerasi animasi, analisis GPU rendering, dll., tapi jangan sembarangan ubah opsi lain yang tidak dipahami.
- <strong>OEM Unlocking dan BL Lock</strong>: Jika Anda tidak berencana flashing atau Root, kedua saklar biarkan default (off) paling aman.
- <strong>ADB</strong>: Tool powerful tanpa Root, orang biasa juga bisa pakai — misalnya pakai <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pm uninstall --user 0</code> uninstall pre-installed App. Tapi sebelum hapus pastikan cek jelas apakah package name bisa dihapus.
- <strong>: Pengguna biasa tidak disarankan Root, risiko lebih besar dari manfaat. Jika benar-benar membutuhkan fungsi tertentu, bisa cari tahu dulu apakah ada alternatif yang tidak membutuhkan Root.</strong>: Pengguna biasa tidak disarankan Root, risiko lebih besar dari manfaat. Jika memang butuh fungsi tertentu, bisa pertama pahami apakah ada alternatif tanpa Root (misalnya pakai ADB uninstall pre-installed, pakai Shizuku menggantikan sebagian fungsi Root).

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Masuk ke Pengaturan &gt; Tentang Ponsel.

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Klik "Nomor Versi" 7 kali berturut-turut, sampai notifikasi mode pengembang aktif.
2. Kembali ke pengaturan, temukan "Opsi Pengembang" (biasanya di bagian bawah pengaturan atau di "Sistem").
3. Temukan "Skala Animasi Jendela", "Skala Animasi Transisi", "Skala Durasi Animasi Program", atur semuanya ke 0.5x atau matikan.
4. Rasakan apakah ponsel menjadi lebih cepat.
5. Bab 20 Lampiran: Termux — Lingkungan terminal Linux portabel pada perangkat Android
:::
