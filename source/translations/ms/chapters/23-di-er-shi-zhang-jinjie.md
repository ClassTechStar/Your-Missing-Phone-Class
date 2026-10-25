---
id: di-er-shi-zhang-jinjie
num: 20
part: jin-jie-pian
nav: Bab 20: Mod Pembangun dan Kebenaran Lanjutan
toc: default
kind: supplement
---

### Bab 20: Mod Pembangun & Kebenaran Lanjutan

{class="chapter-intro mb-4"}
Bab ini disediakan untuk pengguna yang ingin menerokai "fungsi tersembunyi" telefon pintar dengan lebih mendalam. Mod pembangun, kebenaran Root, kunci BL... konsep-konsep yang kedengaran sangat geek ini sebenarnya tidak jauh dari pengguna biasa.

#### 1. Mod Pembangun: Buka Kunci Tetapan Tersembunyi

HarmonyOS

##### : Tetapan &gt; Tentang Telefon &gt; Ketik "Versi HarmonyOS" 7 kali berturut-turut.

- <strong>iOS</strong>: Pengguna biasa tidak boleh mengaktifkan mod pembangun penuh, memerlukan akaun Apple Developer berbayar.
- <strong>HarmonyOS</strong> Nyahpepijat USB
- <strong>Android</strong> Pelarasan kelajuan animasi

##### Laluan tetapan Android biasa:

- <strong>Paparkan operasi sentuhan</strong>: Suis wajib buka untuk sambung komputer operasi lanjutan (seperti flash, pemulihan data, arahan ADB), rujuk bahagian "Arahan praktikal ADB" bab ini.
- <strong>Paksa penggunaan GPU</strong>: Paparkan titik sentuh pada skrin (titik bulat kecil ikut jari), sesuai untuk rakam tutorial operasi atau demonstrasi.

##### Cari laluan dalam sistem HarmonyOS: Tetapan → Perihal telefon → Ketik "Nombor binaan" berulang kali.

- <strong>2. Fungsi praktikal dalam Pilihan Pembangun</strong> Kawal kelajuan animasi — Buat telefon "lebih pantas"
- <strong>Tiga skala kelajuan animasi: Animasi tingkap, Animasi peralihan, Tempoh animasi. Lalai semua 1x, ubah semua ke 0.5x, telefon akan terasa lebih pantas dan responsif.</strong> Hidupkan perkhidmatan USB — Boleh ADB debug
- <strong>Selepas aktifkan "Debug USB", komputer boleh hubung telefon melalui ADB untuk pelbagai operasi lanjutan (sandaran penuh, skrin cermin, pasang APK dll).</strong>: Paparkan masa render setiap bingkai dalam graf bar real-time pada skrin, garis hijau wakili 16.6ms (ambang masa bingkai 60fps). Bar melebihi garis hijau bermaksud dropped frame. Ini adalah alat pembangun untuk mengesan App lag, pengguna biasa juga boleh guna untuk bandingkan App mana optimasi teruk - lebih

##### Pilih ART (Android Runtime) dalam pilihan, boleh tingkatkan kelancaran App.

- <strong>Perkara yang perlu diperhatikan</strong> Had proses latar belakang — Jimat kuasa dan memori
- <strong>"Had proses latar belakang" boleh tetapkan bilangan App maksimum yang serentak berjalan, pilih 4 atau "Tidak ada proses latar belakang", boleh kurangkan penggunaan kuasa dan memori (tetapi mungkin kesan pemberitahuan App).</strong> Tunjukkan sentuhan — Alat bantu tunjuk ajar

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Fungsi kunci BL:

{class="mt-1"}
Perlindungan keselamatan
:::

#### 2. OEM Unlocking: Suis "flash" dalam pilihan pembangun

Dalam pilihan pembangun ada satu suis yang tidak ketara tetapi sangat penting - "OEM Unlocking" (sesetengah jenama panggil "OEM Unlocking Allowed" atau "Device Unlocking"). Suis ini sendiri tidak akan buka kunci BL, tetapi ia adalah "kebenaran awal": hanya buka ia, pengeluar baru benarkan anda buka kunci BL melalui arahan fastboot atau alat jenama.

- <strong>Paparkan kadar penyegaran semasa skrin, boleh sahkan sama ada App sokong kadar penyegaran tinggi.</strong> Warna GPU palsu — Alat debug render
- <strong>Hubungan dengan kunci BL</strong>: OEM Unlocking adalah "permohonan kelayakan", buka kunci BL adalah "operasi sebenar". Yang pertama hanya klik dalam tetapan telefon, yang kedua perlu pergi ke laman web pengeluar memohon kod buka kunci, guna komputer jalankan arahan fastboot (seperti <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">fastboot flashing unlock</code> Berikut adalah pilihan yang boleh menyebabkan ketidakstabilan sistem jika salah tetapkan,
- <strong>jangan cuba tanpa kepastian</strong>: Ya. Suis "OEM Unlocking" akan kembali ke status tutup selepas set semula kilang, tetapi kunci BL sekali dibuka adalah status peringkat fizikal, tidak akan kembali terkunci kerana set semula kilang - perlu pelaksanaan manual <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">fastboot flashing lock</code> Fake Telephony: Ujian pengecaman pembawa, boleh sebabkan isu rangkaian.
- <strong>Tetapkan pemilihan DSP: Boleh sebabkan audio tidak normal.</strong>: Kecuali anda pasti mahu flash atau Root, jika tidak kekal tutup. Ia dan "USB debugging" adalah dua suis berasingan, semasa flash biasanya perlu buka kedua-dua serentak.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Mod demo: Mod paparan demo kedai, akan ganggu penggunaan biasa.

{class="mt-1"}
Android awal tiada suis ini, perisian hasad hanya perlu dapat kebenaran boleh senyap-senyap flash masuk sistem. Google kemudian mewajibkan semua pengeluar Android tambah suis "OEM Unlocking" dalam pilihan pembangun, sebagai pengesahan "persetujuan pengguna". Inilah sebabnya walaupun anda buka kunci BL, jika suis OEM Unlocking ditutup, flash semula masih akan gagal.
:::

#### 3. Kunci BL (Kunci Bootloader): Pintu pertama flash

Anti-curi

##### : Walaupun telefon pintar di-flash, tanpa kata laluan akaun asal ia tidak boleh digunakan.

- <strong>Had waranti</strong>: Membuka kunci BL biasanya bermakna kehilangan waranti rasmi.
- <strong>Dasar kunci BL setiap jenama:</strong> Xiaomi
- <strong>: Boleh dibuka kuncinya, perlu mengikat akaun dan menunggu tempoh (7-30 hari).</strong> Huawei

##### : Selepas 2018 berhenti menyediakan kod nyahkunci, asasnya tidak boleh dibuka kuncinya secara rasmi.

- <strong>OnePlus</strong>: Boleh dibuka kuncinya, agak longgar.
- <strong>OPPO/vivo</strong>: Sesetengah model boleh dibuka kuncinya, perlu memohon.
- <strong>Samsung</strong>: Boleh dibuka kuncinya, tetapi akan mencetuskan pemutus Knox, kehilangan fungsi seperti Samsung Pay.
- <strong>Apple</strong>: Peranti iOS tiada konsep kunci BL dalam erti kata tradisional, tetapi ada mekanisme keselamatan yang serupa.
- <strong>Samsung</strong> Kebenaran Root bersamaan dengan Administrator Windows, adalah kebenaran tertinggi sistem Android. Selepas mendapat kebenaran Root, anda boleh mengubah suai fail sistem, menyahpasang aplikasi yang dipasang sebelumnya, menggunakan App lanjutan yang memerlukan Root.
- <strong>Xiaomi</strong> Nyahpasang aplikasi yang dipasang sebelumnya yang tidak boleh dinyahpasang.

#### 4. Arahan praktikal ADB: Kawal telefon melalui komputer

ADB nama penuh Android Debug Bridge, adalah alat baris arahan rasmi Google, benarkan komputer berkomunikasi dengan telefon Android melalui USB atau Wi-Fi. Ia sendiri tidak perlu Root, hanya telefon buka "USB debugging" boleh guna. Boleh faham sebagai "alat kawalan jauh guna komputer beri arahan kepada telefon" - flash, pasang App, pindah fail, semak log, semua bergantung padanya.

##### Cara sambung melalui USB:

1. Telefon: Masuk pilihan pembangun -&gt; Buka "USB debugging".
2. Komputer: Muat turun Platform Tools dari laman web rasmi Google (mengandungi <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb</code> Langkah ini perlu dimulakan dengan <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">fastboot</code> 2. Pengecaman visual "Selektif Aksesibiliti" ‑ Pilih butang kecil dengan ketat
3. Sambung telefon dan komputer dengan kabel data, telefon akan popup "Benarkan USB debugging?", tanda "Sentiasa benarkan" dan sahkan.
4. Tetapan → Aksesibiliti → Selektif Aksesibiliti → Hidupkan <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb devices</code> Selepas aktif, boleh tetapkan "tindakan automatik" (klik auto, dwi-klik auto dll) pada sebarang butang kecil, sesuai butang terlalu kecil untuk ditekan. <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">List of devices attached / xxxxxxxx device</code>3. Boleh ubah teks kejutan ‑8 Cakap perintah, operasi auto

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Cara cepat yang sering diabaikan.

{class="mt-1"}
Tetapan → Aksesibiliti → Boleh ubah teks kejutan → Tambah perintah <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb devices</code> Paparan "unauthorized" atau tidak senarai peranti, kebanyakan adalah pemacu tidak dipasang atau lupa klik "benarkan" pada telefon. Samsung/Xiaomi dan jenama lain boleh pasang "USB driver" atau "phone assistant" masing-masing; Mac dan Linux biasanya tidak perlu pemacu. Jika popup telefon tidak sengaja ditutup, cabut dan pasang semula kabel data akan popup semula.
:::

##### 4. Imbasan belakang peranti ‑ Logo belakang ketuk dua kali

- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb install app.apk</code>: Pasang APK dari komputer ke telefon (<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-r</code> Tetapan → Aksesibiliti → Sentuh → Ketuk Belakang → Pilih "Ketuk Dua Kali" atau "Ketuk Tiga Kali"<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-s</code> Boleh tetapkan tindakan: Tangkap skrin, buka Pusat Kawalan, buka kamera, jalankan pintasan dll.
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb uninstall com.xxx.xxx</code>5. OCR skrin penuh ‑ Tangkap skrin terus kenalpasti teks
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">Selepas tangkap skrin penuh, ketik butang teks dalam pratonton, boleh pilih sebarang teks dalam gambar untuk salin atau cari.</code> Teknologi: Apple panggil "Live Text", diperkenalkan iOS 15, diperkasai iOS 17 dengan keupayaan kenalpasti video.
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">6. Pintar Peribadi (Personal Hotspot) ‑ Kongsikan rangkaian tanpa kata laluan</code>: Tarik fail telefon ke komputer (lebih cepat daripada hantar kepada diri WeChat kemudian muat turun).
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell</code> Tetapan → Hotspot Peribadi → Benarkan Kebolehpadanan Keluarga <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">ls</code> AI. AI tanpa peranan ialah seorang "ahli serba boleh tetapi tidak mahir dalam apa-apa"; dengan peranan, ia boleh "memasuki" identiti itu, berfikir seperti profesional tersebut.<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pm</code> AI. AI tanpa peranan ialah seorang "ahli serba boleh tetapi tidak mahir dalam apa-apa"; dengan peranan, ia boleh "memasuki" identiti itu, berfikir seperti profesional tersebut.<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">am</code> III. ADB: Pengendalian aras kawalan Android
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb reboot bootloader</code>: Restart telefon masuk mod Fastboot (pintu masuk flash).
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb reboot recovery</code>1. Pasang ADB
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm list packages</code> Muat turin Platform Tools Android SDK (platform-tools-latest-windows.zip) dari laman web rasmi Android. <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-s</code> Ekstrak ke mana-mana direktori, contoh C:\adb. <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-3</code> Dalam terminal (CMD/PowerShell/Git Bash) laksanakan adb, jika papar nombor versi bermakna pemasangan berjaya.
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">2. Sambung telefon</code>: Nyahpasang App pra-pasang untuk pengguna semasa, tanpa Root, rujuk praktikal di bawah.

##### Praktikal nyahpasang App pra-pasang tanpa Root:

Ini adalah salah satu fungsi ADB paling praktikal: guna <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pm uninstall --user 0</code> Arahan boleh nyahpasang App pra-pasang untuk "pengguna semasa", tanpa perlu Root, juga tidak kesan partisi sistem. App yang diuninstall "hilang" dalam sistem, tetapi sebenarnya masih dalam partisi sistem, selepas set semula kilang akan kembali.

1. 3. Arahan praktikal ADB <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm list packages -s</code> Senarai semua aplikasi sistem, cari nama pakej yang anda mahu uninstall. Contohnya pelayar Xiaomi adalah <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.browser</code>, Huawei AppGallery adalah <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.vmall.client</code>.
2. Pasang APK: adb install [fail apk] <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">Sandaran penuh: adb backup -apk -shared -all -f backup.ab</code> Skrin cermin: adb shell screencap -p /sdcard/screenshot.png
3. Rekod skrin: adb shell screenrecord /sdcard/video.mp4<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">2. Sambung telefon</code>4. Aplikasi tipikal: Padam tanpa padam App sistem <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm uninstall --user 0 com.android.browser</code> Banyak telefon Android disertai banyak App pra-pasang yang tidak boleh dipadam. Guna ADB boleh: <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">Success</code> Dapatkan nama pakej App: adb shell pm list packages | grep [nama App sebahagian]
4. Padam untuk pengguna semasa (tidak berkesan pada semua pengguna): adb shell pm disable-user --user 0 [nama pakej]<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">Selepas dilumpuhkan App tidak lagi muncul, tetapi masih dalam sistem, boleh aktifkan semula bila-bila: adb shell pm enable [nama pakej]</code>.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-skull-crossbones mr-2"></i>5. Awas keselamatan ADB

{class="mt-1"}
"pm uninstall --user 0" walaupun adalah cara selamat tanpa Root, tetapi padam aplikasi sistem penting secara sembarangan (seperti <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.systemui</code> Jangan guna komputer awam atau wayar data tidak dipercayai untuk debug USB.<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.phone</code> IV. Root: Membuka kunci kebenaran tertinggi Android<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.settings</code> Root bermaksud akses pentadbir tertinggi Android, boleh ubah apa sahaja dalam sistem. Ini kuasa yang sangat kuat tetapi juga sangat berbahaya.
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>1. Kaedah Root biasa

{class="mt-1"}
Unlock Bootloader: Langkah pertama, buka kunci pengesan but, kebanyakan pengeluar perlu permohonan rasmi.<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">--user 0</code> bermaksud "hanya nyahpasang untuk pemilik semasa", fail APK dalam partisi sistem masih wujud, hanya tidak papar kepada pemilik. Inilah sebabnya ia tidak perlu Root - tidak sentuh fail sistem, hanya ubah "konfigurasi pengguna". Ini juga sebabnya ia boleh "pasang semula" - kembalikan konfigurasi pengguna. Nyahpasang biasa betul-betul padam dari sistem, semua pengguna tidak lagi ada; nyahpasang ADB hanya "sembunyi dari pengguna semasa".
:::

#### 5. Kebenaran Root: "Pentadbir super" Android

Kebenaran Root setara dengan super user dalam Linux (mempunyai kawalan penuh ke atas direktori /, boleh baca tulis mana-mana fail), adalah kebenaran tertinggi sistem Android. Ia berbeza secara asas dengan Administrator Windows: Windows atas sebab keselamatan telah membuat banyak sekatan kepada pentadbir (kebenaran tertinggi sebenar sebenarnya TrustedInstaller), walaupun Administrator juga tidak boleh seperti Linux root terus melaksanakan <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">sudo rm -rf /*</code>. Selepas dapat kebenaran Root, anda boleh ubah fail sistem, nyahpasang aplikasi pra-pasang, guna App lanjutan yang memerlukan Root.

##### Memasang Recovery pihak ketiga dan ROM tersuai.

- Risiko Root:
- Kehilangan waranti
- : Kebanyakan pengeluar tidak mewartikan telefon pintar yang telah di-Root.
- Risiko keselamatan

##### : App hasad mungkin mendapat kebenaran Root, menyebabkan akibat yang serius.

- <strong>Sistem tidak stabil</strong>: Salah operasi boleh menyebabkan sistem ranap.
- <strong>App perbankan tidak boleh digunakan</strong>: Ramai App perbankan dan pembayaran akan menolak berjalan apabila mengesan Root.
- <strong>Kemas kini OTA gagal</strong>: Mungkin tidak boleh menerima kemas kini sistem rasmi secara normal.
- <strong>Amaran Serius</strong> Operasi Root mempunyai risiko tertentu, boleh menyebabkan telefon pintar menjadi bata (tidak boleh dihidupkan). Jika anda baru mula, disyorkan untuk memahami pengetahuan berkaitan dengan secukupnya terlebih dahulu, dan pastikan ada sandaran yang lengkap. Sebelum beroperasi sila baca tutorial dengan teliti, sahkan model dan versi sistem telefon pintar anda.
- <strong>4. Cadangan untuk Pengguna Biasa</strong> Mod pembangun

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-skull-crossbones mr-2"></i>: Boleh diaktifkan, alami fungsi seperti percepatan animasi, tetapi jangan ubah tetapan lain sesuka hati.

{class="mt-1"}
Kunci BL
:::

#### 6. Pengesahan SafetyNet dan Play Integrity: Kenapa App bank tidak boleh guna selepas Root

Ramai pengguna Root pernah hadapi momen ranap ini: selepas Root bersemangat pasang satu kelompok modul, hasilnya buka App bank - "Peranti anda tidak selamat, tidak boleh guna", Google Pay juga tidak boleh guna, bahkan Netflix enggan mainkan HD. Di sebalik ini adalah dua mekanisme pengesahan integriti peranti Google: SafetyNet lama dan Play Integrity API baru.

##### Apakah SafetyNet / Play Integrity:

- <strong>SafetyNet Attestation (versi lama, sejak 2017)</strong>: API pengesahan integriti peranti awal Google, App melaluinya bertanya pelayan Google "peranti ini sama ada lulus ujian keserasian CTS, sama ada dalam status rasmi tidak diubahsuai". Keputusan dibahagikan kepada Basic Attestation (pengesahan asas) dan Strong Attestation (pengesahan kuat, bergantung kunci perkakasan). Google telah umumkan SafetyNet akan beransur-ansur dihentikan selepas 2024.
- <strong>Kerosakan sistem: Salah ubah boleh sebabkan telefon tidak boleh but (brick).</strong>: Alternatif yang dilancarkan Google, lebih ketat dan lebih menyeluruh daripada SafetyNet. Selain integriti peranti, juga termasuk "integriti aplikasi" (App sama ada diubahsuai) dan "integriti akaun/kebenaran" (akaun pengguna sama ada dipercayai Google). App baru harus berpindah ke Play Integrity.
- <strong>Kegagalan App: Banking, pembayaran, Netflix DRM dll App akan enggan berjalan.</strong>: App bank, kewangan, pembayaran (seperti Google Pay, bank dalam talian setiap bank, Alipay/WeChat Pay senario tertentu), media streaming (perlindungan hak cipta HD Netflix), anti-pemipat permainan tertentu (seperti permainan Tencent/NetEase), App pejabat enterprise (semakan pematuhan MDM).

##### Google laksanakan SafetyNet (kini diganti Play Integrity API) untuk mengesan peranti root. Selepas dikesan, App sensitif (bank, pembayaran) akan enggan berjalan. Magisk boleh sembunyi root melalui modul Zygisk DenyList, tetapi ini permainan kucing-dan-tikus berterusan antara Google dan komuniti root.

- <strong>5. Cadangan: Jangan root melainkan benar-benar perlu</strong>: Peranti menjalankan sistem Android rasmi, Bootloader tidak dibuka kunci, tiada Root, lulus ujian keserasian CTS. Boleh guna App bank, pembayaran secara normal.
- <strong>V. Aksesibiliti: Telefon juga "boleh jadi mesra"</strong> Sistem telefon moden ada fungsi aksesibiliti yang kaya, asalnya untuk pengguna kurang upaya, tetapi banyak juga praktikal untuk pengguna biasa.
- <strong>1. Pembesar Suara (Live Listen)</strong>: Tahap tertinggi, memerlukan sokongan kunci perkakasan (seperti cip Titan M siri Google Pixel), kebanyakan model jenama pihak ketiga walaupun tidak Root juga tidak capai tahap ini.
- <strong>Tetapan → Aksesibiliti → Peranti Audio → Pembesar Suara</strong>: Peranti telah Root, buka kunci BL, flash ROM pihak ketiga atau dikenalpasti sebagai emulator, kebanyakan App pembayaran/bank akan terus enggan berjalan.

##### Kenapa App ini gagal selepas Root:

App melalui Play Integrity API hantar permintaan pengesahan ke pelayan Google, Google akan semak pelbagai penunjuk peranti - status kunci Bootloader, sama ada partisi sistem diubahsuai, sama ada wujud fail binari su, sama ada SELinux dalam mod permisif dll. Sebarang kelewatan akan menyebabkan tahap pengesahan dikembalikan rendah atau kosong, App bank nampak "peranti tidak selamat", semula jadi enggan berkhidmat.

##### 3. Keterangan langsung

Untuk menikmati kemudahan Root sambil masih boleh guna App bank, komuniti telah membangunkan siri skim "sembunyi status Root". Idea teras semua adalah: biar program pengesanan nampak bukan sistem yang diubahsuai, tetapi peranti yang "nampak normal".

- <strong>SuperSU</strong>: Skim Systemless Root paling utama - tidak ubah partisi sistem, tetapi capai Root melalui mount. Kelebihan reka bentuk ini adalah kebarangkalian kegagalan kemas kini OTA kecil, nyahpasang lebih bersih, adalah asas semua skim sembunyi berikut. Tetapi guna Magisk masih perlu buka kunci BL.
- <strong>4. Penggera realiti maya</strong>: Modul sembunyi terbina dalam Magisk awal, boleh sembunyikan Root untuk App tertentu. Tetapi sejak 2021 telah dibuang oleh Magisk rasmi, sebab Google berterusan menaiktaraf kaedah pengesanan, kedua-dua pihak terjebak "permainan kucing dan tikus".
- <strong>Zygisk</strong> Tetapan → Aksesibiliti → Penggera Realiti Maya
- <strong>Shamiko</strong>: Modul sembunyi paling utama kini, bekerjasama dengan Zygisk, boleh untuk App tertentu (mod "senarai putih terbalik") sembunyi Root, sembunyi Magisk sendiri, pemalsuan status kunci Bootloader. Shamiko diedarkan melalui repositori LSPosed atau GitHub.
- <strong>Play Integrity Fix(osm0sis)</strong>: Modul Magisk khusus untuk pengesanan Google Play Integrity, akan ubah cap jari peranti (fingerprint) biar Google fikir peranti anda adalah model rasmi yang tidak Root.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Tetapan → Aksesibiliti → Kandungan Dibacakan → Baca Skrin

{class="mt-1"}
Google setiap satu masa akan kemas kini peraturan pengesanan, pengeluar App juga akan ikut menaiktaraf pengesahan Play Integrity. Skim sembunyi yang masih boleh guna hari ini, esok mungkin dikenalpasti. Jika anda sepenuhnya bergantung App bank/pembayaran (seperti pemindahan harian, bayar kod imbas), pilihan paling selamat masih: jangan Root, jangan buka kunci BL. Skim sembunyi lebih sesuai untuk konfigurasi pemain "telefon utama tidak Root + telefon sandaran main Root".
:::

#### 7. Nasihat untuk pengguna biasa

- <strong>Root</strong>7. Input suara
- <strong>OEM Unlocking dan kunci BL</strong>: Jika anda tidak merancang flash atau Root, kedua-dua suis kekal lalai (tutup) paling selamat.
- <strong>ADB</strong>: Alat berkuasa tanpa Root, orang biasa juga boleh guna - contohnya guna <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pm uninstall --user 0</code> Bab 8: Digital Legacy — Apa yang berlaku kepada akaun selepas kita tiada
- <strong>Kunci Bootloader</strong>: Pengguna biasa tidak disyorkan Root, risiko lebih besar daripada manfaat. Jika benar-benar perlu fungsi tertentu, boleh dahulu faham sama ada ada alternatif tanpa Root (seperti guna ADB nyahpasang pra-pasang, guna Shizuku ganti sebahagian fungsi Root).

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Cari "Penskalaan Animasi Tetingkap", "Penskalaan Animasi Peralihan", "Penskalaan Tempoh Animasi", tetapkan semuanya kepada 0.5x atau matikan.

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Rasakan sama ada telefon pintar menjadi lebih pantas.
2. Lampiran Bab 20: Termux — Persekitaran Terminal Linux Mudah Alih pada Peranti Android
3. Jika anda rasa mod pembangun masih belum cukup "keras", dan mahu mengalami baris perintah Linux yang lengkap pada telefon pintar, maka Termux adalah untuk anda. Ia tidak memerlukan kebenaran root, dan boleh menjadikan telefon pintar Android biasa menjadi stesen kerja Linux mudah alih, merupakan senjata ampuh bagi pengguna lanjutan untuk menerokai pembangunan dan pentadbiran mudah alih.
4. 1. Apakah itu Termux
5. Termux adalah emulator terminal sumber terbuka dan aplikasi persekitaran Linux yang direka khusus untuk peranti Android, ia tidak memerlukan kebenaran root untuk menyediakan pengalaman shell Linux yang lengkap pada telefon pintar. Sebagai aplikasi ringan (pakej pemasangan hanya kira-kira 30MB), Termux menyokong ekosistem perisian yang kaya melalui sistem pengurusan pakej APT, membolehkan pengguna menjalankan Python, Node.js, Git, SSH dan alat lain pada peranti mudah alih, malah membina pelayan atau melakukan ujian penembusan.
:::
