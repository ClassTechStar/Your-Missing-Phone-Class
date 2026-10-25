---
id: di-er-shi-wu-zhang
num: 25
part: chao-yue-pian
nav: Bab 25: Penanganan Ponsel Bekas dan Warisan Digital
toc: default
kind: chapter
---

### Bab 25: Penanganan Ponsel Bekas dan Warisan Digital

{class="chapter-intro mb-4"}
Hei, teman-teman, setelah lebih dari dua puluh bab "pelatihan", saya yakin Anda telah tumbuh dari "pemula digital" menjadi pengguna ponsel yang cukup mahir. Tapi kehidupan teknologi selalu berputar—cinta baru akhirnya menjadi cinta lama. Saat Anda bersiap mempensiunkan "rekan lama" Anda, tahukah Anda bagaimana berpisah dengan layak dan aman?

#### 1. "Eutanasia" Ponsel Lama: Panduan Jual atau Hadiah dengan Aman

Prinsip inti: Data cleaning bukan "hapus", tapi "overwrite". Banyak orang mengira drag foto ke recycle bin, clear album sudah selesai, hasilnya setelah ponsel berganti tangan, pemilik baru pakai data recovery software scan, foto lama, riwayat chat, foto KTP semua kembali — "skenario memalukan" seperti ini terjadi setiap tahun.

1. <strong>"Bersih-bersih" mandiri</strong>: Selesaikan backup lengkap terakhir kali, logout semua akun (iCloud, akun Huawei/Xiaomi/Samsung, akun Google), matikan fungsi "Find My Phone" — jika tidak pengguna berikutnya akan diblokir oleh activation lock.
2. <strong>"Format" ultimate</strong>: "Factory reset" ponsel modern biasanya termasuk encrypted wipe — yang dihancurkan adalah encryption key itu sendiri, sekali key hilang, seluruh data disk instan menjadi gibberish.
3. <strong>"Ilusi" Terakhir (hanya perangkat lama)</strong>: Ponsel modern (iOS 8+, Android 6+) sudah default full disk encryption (FBE), factory reset akan menghancurkan encryption key, data secara teori tidak bisa recovery,<strong>tidak perlu langkah ini</strong>. Hanya untuk perangkat non-encrypted yang sangat lama (sebelum 2015), baru perlu setelah factory reset pakai junk file fill storage, lalu execute factory reset sekali lagi.

<strong>Tabel Cepat Path Wipe Data Berbagai Merek</strong>: Meskipun prinsip sama, tapi setiap merek menyembunyikan "factory reset" di posisi yang sedikit berbeda, perbedaan kunci sebagai berikut.

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                        <thead>
                            <tr class="bg-light dark:bg-gray-700">
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Merek</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Entri Wipe</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Perbedaan Kunci dan Catatan</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Huawei</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Settings &gt; System &amp; Update &gt; Reset &gt; Factory Reset</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Perlu pertama logout akun Huawei dan matikan "Find My Phone", jika tidak akan trigger activation lock; dalam mode pure mungkin butuh verifikasi password.</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xiaomi / Redmi</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Settings &gt; My Device &gt; Factory Reset</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Di bawah ada opsi "Format Virtual SD Card" dan "Clear All Content &amp; Settings", keduanya harus dicentang; sebelum logout akun Xiaomi pertama matikan "Find Device".</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OPPO / OnePlus</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Settings &gt; Additional Settings &gt; Restore Phone &gt; Thoroughly Clear All Data</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ColorOS menyediakan mode "Thorough Clear", akan multiple overwrite storage; perlu input lock screen password untuk konfirmasi.</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">vivo</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Settings &gt; System Management &gt; Backup &amp; Reset &gt; Clear All Data</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Centang "Format Phone Storage" baru bisa clean SD card area; perlu logout akun vivo, matikan "Find Phone".</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Samsung</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Settings &gt; General Management &gt; Reset &gt; Factory Reset</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Perlu pertama remove akun Samsung dan matikan "Find My Phone"; sebagian model ada opsi "Auto Overwrite", disarankan aktifkan.</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">: Pengaturan → Nama Anda → iCloud → iCloud Cloud Backup → Aktifkan. Ponsel terhubung daya, terhubung Wi-Fi, saat layar terkunci akan otomatis dicadangkan. 5GB gratis kemungkinan besar tidak cukup, disarankan upgrade ke 50GB dengan 6 yuan.</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Settings &gt; General &gt; Transfer or Reset iPhone &gt; Erase All Content and Settings</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Harus pertama logout Apple ID, jika tidak pengguna berikutnya diblokir iCloud activation lock; iOS 15+ mendukung "Keep iCloud Data on Logout" untuk investigasi nanti.</td>
                            </tr>
                        </tbody>
                    </table>
```

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Tiga Hal yang Paling Mudah Diabaikan

{class="list-disc pl-6 mt-2 space-y-1"}
- <strong>Tidak Logout Akun</strong>: Ponsel dijual ke pembeli berikutnya lalu di-lock remote, sendiri juga tidak bisa keluar, akhirnya hanya bisa bawa KTP ke service center resmi untuk unlock.
- <strong>SD Card Tidak Dikeluarkan</strong>: Factory reset tidak akan format foto di external SD card, ingat manual keluarkan atau format terpisah.
- <strong>USB Drive/Perangkat OTG Tidak Diputus</strong>: Selama proses wipe jika tersambung perangkat external, mungkin salah wipe data perangkat external, juga mungkin menyebabkan wipe terputus.
:::

#### 2. Warisan Digital: Bagaimana Menempatkan Jiwa Sosial Anda?

Data di ponsel, sudah lama bukan "virtual" lagi. Itu membawa dana Anda, hubungan sosial, hasil kreasi, bahkan "identitas digital" Anda.<strong>Setelah seseorang meninggal, aset ini bagaimana harus ditangani?</strong> Ini bukan lagi masalah abstrak, tapi dilema nyata yang dihadapi semakin banyak keluarga — kerabat tidak tahu password, platform tidak mengizinkan warisan, cryptocurrency selamanya hilang.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-gavel mr-2"></i>Dasar Hukum: Pasal 49 Personal Information Protection Law

{class="mt-1"}
Pasal 49 Personal Information Protection Law RRT yang berlaku 2021 secara jelas menyatakan:<strong>Jika natural person meninggal, kerabat dekatnya untuk kepentingan legal dan wajar sendiri, bisa menjalankan hak akses, salin, koreksi, hapus, dll. terhadap personal information terkait almarhum sebagaimana diatur dalam bab ini; kecuali almarhum saat hidup memiliki arranjo lain.</strong>

{class="mt-2"}
Ini berarti:

{class="list-disc pl-6 mt-1 space-y-1"}
- <strong>Kerabat dekat punya dasar hukum</strong> untuk mengajukan ke platform memproses akun dan personal information almarhum.
- "Kepentingan legal dan wajar" biasanya termasuk mengurus warisan, menutup akun, menghapus privasi sensitif, dll.
- Jika almarhum saat hidup punya will atau arranjo lain (seperti menunjuk legacy contact), mengikuti arranjo tersebut.
- Platform tidak bisa dengan alasan "privasi pengguna" menolak kooperasi secara umum, tapi proses spesifik berbeda-beda.
:::

{class="font-semibold mt-4 mb-1"}
##### 1. WeChat dan Alipay: Akun tidak bisa diwariskan, tapi dana bisa

Kedua App yang paling sering dipakai orang Tiongkok ini, aturannya masing-masing berbeda:

- <strong>Akun WeChat</strong>: Berdasarkan "Tencent WeChat Software License and Service Agreement", kepemilikan akun milik Tencent, pengguna hanya punya right of use,<strong>akun itu sendiri tidak bisa diwariskan, tidak bisa ditransfer</strong>. Tapi dalam akun <strong>dana WeChat Pay Balance, Qianliantong</strong> termasuk personal property, kerabat dekat bisa dengan death certificate, proof of kinship, inheritance notary letter mengajukan ke Tenpay untuk withdraw atau transfer.
- <strong>Alipay</strong>: Akun juga tidak bisa langsung diwariskan, tapi Alipay Balance, Yu'e Bao, Licaitong, dll.<strong>dana termasuk inheritable property</strong>. Ahli waris bisa via "Customer Service Hotline" Alipay atau offline submit death certificate, inheritance notary letter untuk proses; produk wealth management Ant Fortune perlu via proses fund company.
- <strong>Riwayat Chat</strong>: Secara hukum termasuk privasi pribadi, platform tidak akan aktif memberikan ke keluarga. Jika melibatkan clue warisan, bisa via litigasi atau notary apply untuk obtain.

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Menggunakan kata sandi lemah seperti tanggal lahir / 123456 / qwerty;

{class="list-disc pl-6 mt-2 space-y-1"}
- <strong>Jangan langsung memberikan password akun almarhum ke keluarga untuk "dipakai lanjut"</strong>— ini melanggar agreement platform, saat dana dibekukan atau bahkan trigger risk control pembuktian lebih sulit.
- <strong>Jangan coba pakai ponsel almarhum terima verification code untuk "withdraw"</strong>— mungkin diidentifikasi sebagai penyalahgunaan, justru melanggar hukum.
- <strong>Jangan Menunda</strong>: Sebagian akun jika lama tidak login akan auto-cancel, recovery dana akan lebih merepotkan.
:::

{class="font-semibold mt-4 mb-1"}
##### 2. "Legacy Contact" Apple: Tunjuk Lebih Awal, Hasilnya Berlipat Ganda

Sejak iOS 15.2 Apple meluncurkan fitur "Legacy Contact", mengizinkan pengguna menunjuk kontak terpercaya lebih awal, setelah meninggal kontak tersebut bisa dengan <strong>death certificate + Legacy Contact access key</strong> mengajukan akses ke data iCloud almarhum (foto, notes, kontak, notes, dll.). Langkah operasi:

1. Di iPhone masuk <strong>[Settings] &gt; [Nama Anda] &gt; [Sign-In &amp; Security] &gt; [Legacy Contact]</strong>.
2. Klik "Add Legacy Contact", gunakan Face ID untuk konfirmasi identitas.
3. Pilih kontak (pilih dari contacts), sistem akan generate satu <strong>access key</strong>.
4. Serahkan access key via SMS, email atau cetak fisik ke pihak tersebut, dan ingatkan untuk simpan dengan baik.
5. Bisa tambah banyak kontak sebagai backup, menghindari single point of failure.

Yang ditunjuk tidak butuh perangkat Apple, dengan key dan death certificate bisa apply akses di situs resmi Apple. Seluruh proses biasanya selesai dalam 7 hari.

{class="font-semibold mt-4 mb-1"}
##### 3. "Inactive Account Manager" Google: Otomatis Mengurus Setelah Meninggal

Google menyediakan "Inactive Account Manager", bisa saat pengguna lama tidak login otomatis execute operasi preset — ini salah satu mekanisme digital legacy paling lengkap saat ini.

1. Kunjungi <strong>myaccount.google.com/inactive</strong>, login akun Google.
2. Setel periode timeout: trigger setelah 3 / 6 / 12 / 18 bulan tidak login.
3. Tambahkan trusted contact (maksimal 10 orang), dan setel masing-masing bisa akses data apa (Gmail, Photos, Drive, dll.).
4. Opsional: setel auto-reply email, memberi tahu pengirim bahwa Anda tidak bisa memproses.
5. Pilihan terakhir: setelah jatuh tempo apakah <strong>share data ke kontak</strong>, atau <strong>langsung hapus akun</strong>.
6. Setel nomor ponsel sebagai verifikasi fallback, menghindari false trigger.

{class="font-semibold mt-4 mb-1"}
##### 4. Akun Media Sosial Domestik: Proses Memorialisasi dan Deaktivasi

Platform media sosial mainstream domestik menangani akun almarhum dengan dua pendekatan:<strong>"Memorialisasi" (retain akun untuk kerabat berkenang)</strong>"dalam kondisi apa"<strong>"Deaktivasi" (hapus total)</strong>. Keluarga bisa dengan death certificate, proof of kinship, ID card pemohon mengajukan ke customer service platform.

- <strong>Weibo</strong>: Mendukung "memorialisasi" akun, diajukan oleh kerabat dengan death certificate, akun akan di-lock tidak bisa login tapi konten retain, homepage akan menampilkan "Akun ini telah disetel sebagai akun peringatan". Juga bisa apply deaktivasi, perlu menyediakan inheritance notary.
- <strong>Douyin</strong>: Via "Saya - Settings - Feedback &amp; Help - Account &amp; Security - Account Deactivation" atau customer service manual, submit death certificate, proof of kinship, ID card pemohon, setelah review lulus bisa deactivate atau convert ke status memorial.
- <strong>Bilibili</strong>: Channel customer service submit proof almarhum dan proof kerabat, bisa apply deaktivasi akun atau retain sebagai halaman peringatan; penanganan video historial UP perlu dikombinasikan dengan copyright statement.
- <strong>Xiaohongshu</strong>: Via customer service resmi appeal, submit death certificate, proof of kinship, bisa apply deaktivasi akun dan hapus konten.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Pengingat Kunci

{class="list-disc pl-6 mt-2 space-y-1"}
- Aturan setiap platform akan update, sebelum memproses pertama cek panduan terbaru customer service resmi.
- Semua proof document disarankan pertama scan backup baru submit, original simpan dengan baik.
- Saat memproses cross-platform sekali jalan, bisa secara terpadu apply satu <strong>inheritance notary letter</strong>, menghemat bolak-balik proses.
:::

{class="font-semibold mt-4 mb-1"}
##### 5. Tantangan Warisan Aset Digital

Selain akun media sosial, semakin banyak orang memegang <strong>aset digital yang benar-benar bernilai</strong>, masalah warisannya lebih kompleks:

- <strong>Cryptocurrency (Bitcoin, Ethereum, dll.)</strong>: Berbasis prinsip "private key adalah kepemilikan",<strong>tanpa private key berarti aset hilang</strong>. Ahli waris tidak bisa via document legal ke on-chain "appeal". Saran: Simpan mnemonic/private key dengan sharding di banyak lokasi fisik aman (seperti safe deposit box bank + brankas rumah), dan di will tunjukkan cara akses.
- <strong>Akun Exchange</strong>: Mirip dengan akun bank, bisa dengan inheritance notary letter mengajukan ke exchange (seperti Binance, OKX) untuk disposal, tapi exchange cross-border prosesnya lama.
- <strong>Domain</strong>: Termasuk inheritable property, ahli waris di domain registrar (seperti Alibaba Cloud, GoDaddy) submit inheritance notary lalu bisa proses transfer.
- <strong>Kekayaan Intelektual (artikel original, video, paten, copyright software)</strong>: Property rights dalam copyright bisa diwariskan (moral rights tidak diwariskan), right of revenue bisa dinikmati ahli waris sampai 50 tahun setelah kematian penulis.
- <strong>Cloud Storage dan Cloud Drive</strong>: Konten data milik personal, bisa diwariskan; tapi sebagian platform agreement menyatakan akun itu sendiri tidak bisa ditransfer, perlu pertama download lalu deactivate.

::: div .danger-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-skull-crossbones mr-2"></i>Harga Nyata Cryptocurrency "Hilang"

{class="mt-1"}
Menurut laporan Chainalysis, global sudah ada <strong>lebih dari 3 juta Bitcoin</strong> karena private key hilang selamanya tidak bisa recovery, setara dengan seperenam dari total yang ada. Jika Anda memegang crypto asset, pastikan minimal satu orang yang Anda mutlak percaya tahu <strong>recovery path</strong>— jika tidak kekayaan ini akan selamanya tertidur di blockchain.
:::

{class="font-semibold mt-4 mb-1"}
##### 6. Template "Digital Will"

Will properti tradisional tidak bisa mengurus aset digital. Disarankan Anda setiap tahun update satu lampiran "digital will", disimpan bersama dengan will resmi. Template berikut untuk referensi:

::: div .bg-light .dark:bg-gray-700 .rounded-lg .p-4 .mt-2 .mb-3 .text-sm
{class="font-semibold mb-2"}
"Lampiran Disposal Aset Digital Personal" (Template)

{class="mb-1"}
<strong>Bagian 1: Daftar Akun</strong>(Hanya catat nama akun dan platform,<strong>jangan tulis password</strong>)

{class="list-disc pl-6 mb-2 space-y-0.5"}
- Sosial: WeChat (akun xxx), Weibo, Douyin, Bilibili, Xiaohongshu, dll.
- Pembayaran: Alipay, WeChat Pay, berbagai App kartu bank
- Cloud: iCloud, Huawei Cloud, Xiaomi Cloud, akun Google, akun Microsoft
- Email: QQ Mail, NetEase Mail, Gmail, dll.
- Lainnya: Cloud drive, subscription service, akun game, dll.

{class="mb-1"}
<strong>Bagian 2: Skema Escrow Password</strong>

{class="list-disc pl-6 mb-2 space-y-0.5"}
- Cara simpan master password: Pakai password manager (seperti Bitwarden, 1Password), master password ditulis di fisik kertas, disegel di brankas rumah.
- Recovery key/mnemonic: Simpan dengan sharding, minimal dua lokasi fisik (seperti safe deposit box bank + brankas rumah).
- Orang yang berwenang query: Nama, nomor ID, hubungan dengan Anda, kontak.

{class="mb-1"}
<strong>Bagian 3: Keinginan Disposal</strong>

{class="list-disc pl-6 mb-2 space-y-0.5"}
- Berbagai akun apakah ingin "memorialisasi" atau "deaktivasi".
- Apakah data iCloud / Google ditunjuk "Legacy Contact" atau "Inactive Account Manager".
- Crypto asset diwariskan ke siapa, penjelasan path akses private key.
- Revenue karya copyright dinikmati oleh siapa.

{class="mb-1"}
<strong>Bagian 4: Kontak dan Platform</strong>

{class="list-disc pl-6 space-y-0.5"}
- Nama eksekutor terpercaya, kontak, kontak cadangan.
- Entri customer service platform tempat tinggal dan daftar proof material yang dibutuhkan.
- Tanggal update lampiran ini: ____ tahun __ bulan __ hari, tanggal review berikutnya: ____ tahun __ bulan __ hari.
:::

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Tips Hukum tentang "Password"

{class="mt-1"}
Menulis password langsung di will ada risiko bocor, dan setelah will dibuka semua ahli waris bisa melihat.<strong>Cara yang lebih aman: Di will hanya tulis "daftar akun + keinginan disposal + lokasi escrow password", password asli via master password manager secara terpisah diberikan ke eksekutor terpercaya</strong>. Dengan begitu sesuai requirement legal, juga menurunkan risiko password bocor.
:::

#### 3. Perjalanan Terakhir yang Ramah Lingkungan

Satu ponsel mengandung puluhan jenis logam seperti emas, perak, tembaga, rare earth, membuang sembarangan baik mencemari tanah, juga membuang sumber daya. Channel daur ulang yang benar ada tiga jenis, masing-masing fokus:

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                        <thead>
                            <tr class="bg-light dark:bg-gray-700">
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Channel</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Harga Daur Ulang</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Keamanan Data</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">: Produksi profesional kelas atas. Seri iPhone 15 Pro mendukung shooting video Apple ProRes (hingga 4K 60fps), tetapi format ProRes RAW saat ini perlu digunakan bersama perangkat perekam eksternal, ponsel belum mendukung shooting langsung.</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Trade-in Resmi (Huawei/Apple/Xiaomi, dll.)</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sedang, sering ditambah voucher subsidi</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tertinggi, resmi punya proses standar</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Paling worth it saat berencana ganti ponsel merek yang sama</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Platform Daur Ulang Pihak Ketiga (Aihuishou, Zhuanzhuan, Huisoubao, dll.)</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sedikit lebih tinggi, bisa compare harga</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cukup tinggi, ada laporan data wipe</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ingin langsung cair, tidak terikat merek</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Donasi Amal (seperti sekolah pedesaan, lembaga amal)</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tanpa return ekonomi</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Perlu wipe menyeluruh sendiri</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Perangkat masih usable, ingin berbuat baik</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Manfaatkan Sisa (Simpan &amp; Modifikasi)</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Hemat uang perangkat baru</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pemilik asli terus pakai, tanpa risiko</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Performa perangkat masih OK, ada kebutuhan modifikasi di rumah</td>
                            </tr>
                        </tbody>
                    </table>
```

- <strong>Recycle resmi/Trade-in</strong>: Cara yang paling direkomendasikan, proses standar, keamanan data terjamin. Situs resmi Apple, Huawei, Xiaomi, dll. semua punya entri "Trade-in", setelah evaluasi bisa dipakai diskon harga ponsel baru.
- <strong>Platform recycle resmi</strong>: Pilih platform daur ulang berskala besar dengan reputasi baik, setelah order kurir jemput, setelah inspeksi transfer. Pastikan pilih <strong>yang menyediakan "laporan data wipe"</strong> platform, dan simpan bukti.
- <strong>Donasi Amal</strong>: Bisa kontak sekolah pedesaan lokal, organisasi amal komunitas, ponsel lama bisa dimodifikasi menjadi tablet pengajaran atau ponsel lansia.<strong>Sebelum donasi pastikan execute proses wipe lengkap, dan lepas semua SIM/SD card</strong>.
- <strong>Manfaatkan kembali</strong>: Modifikasi menjadi navigator mobil, smart home hub, kamera CCTV, baby monitor, digital photo frame. Satu ponsel lama bisa bertugas beberapa tahun lagi.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-leaf mr-2"></i>Fakta Sampah Elektronik

{class="mt-1"}
Circuit board satu ponsel mengandung <strong>emas, perak, palladium, tembaga</strong> dan logam mulia lainnya, setiap ton circuit board bekas kandungan emasnya puluhan kali dari bijih emas. Tapi jika dibuang sembarangan, timbal, merkuri, kadmium di dalamnya akan meresap ke tanah dan air tanah, polusi berlangsung puluhan tahun.<strong>Daur ulang yang benar melindungi lingkungan sekaligus mendaur ulang logam langka.</strong>
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Praktik: Lakukan "Pemakaman Standar" untuk Ponsel Lama Anda

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Backup lengkap terakhir kali: foto diunggah ke cloud, file penting disalin ke komputer, riwayat chat diekspor untuk arsip.
2. Keluar dari semua akun: iCloud / Huawei / Xiaomi / Google, matikan "Find My Phone".
3. Keluarkan kartu SIM dan kartu SD, putuskan semua periferal OTG.
4. Lakukan factory reset terenkripsi, jika perlu centang "format penyimpanan" secara manual.
5. (Perangkat lama saja) Isi penyimpanan dengan file sampah, lalu factory reset sekali lagi.
6. Pilih perhentian berikutnya: trade-in resmi, platform daur ulang formal, donasi amal, atau hadiahkan ke keluarga.
7. Perbarui "daftar warisan digital" Anda, coret perangkat yang sudah pensiun dari daftar.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-calendar-check mr-2"></i>Daftar tugas bulan ini

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Tetapkan Apple "Legacy Contact" atau setel Google "Inactive Account Manager" untuk ponsel utama Anda saat ini.
2. Gunakan template bagian ini untuk menyusun "Lampiran Penanganan Aset Digital Pribadi", diskusikan lokasi penyimpanan dengan keluarga.
3. Periksa apakah ada 2 ponsel lama menganggur di rumah, jadwalkan daur ulang melalui platform resmi atau formal.
:::
