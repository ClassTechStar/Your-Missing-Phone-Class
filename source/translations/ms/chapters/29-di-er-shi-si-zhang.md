---
id: di-er-shi-si-zhang
num: 24
part: chao-yue-pian
nav: Bab 24: Analisis Mendalam Kebenaran Root dan Kunci BL
toc: default
kind: chapter
---

### Bab 24: Analisis Mendalam Kebenaran Root & Kunci BL

{class="chapter-intro mb-4"}
Bab ini adalah pengembangan mendalam terhadap kandungan Bab 20, sesuai untuk pengguna yang benar-benar ingin memahami mekanisme peringkat bawah telefon, malah mencuba memuat turun sistem. Sila ambil perhatian, operasi ini mempunyai risiko tertentu, sila berhati-hati.

#### 1. Memahami Bootloader Secara Mendalam

Menghalang penurunan taraf

##### : Menghalang pengguna memuat turun versi sistem lama untuk mengeksploitasi kelemahan yang diketahui.

- <strong>Melindungi data</strong>: Walaupun memuat turun sistem baharu, tanpa kata laluan akaun asal juga tidak boleh mengakses data pengguna.
- <strong>2. Aliran Terperinci Membuka Kunci BL (Contoh Xiaomi)</strong> Mohon kebenaran nyahkunci
- <strong>: Mohon nyahkunci di laman web alat nyahkunci Xiaomi.</strong> Ikat akaun

##### 🔐 Storan dan pengesahan peringkat perkakasan

Status kunci BL (Locked/Unlocked) dan kunci awam pengeluar, biasanya disimpan dalam kawasan perkakasan terlindung (seperti partisi devinfo Qualcomm, eFuse atau partisi RPMB), halang diubahsuai oleh perisian. Setiap boot, Bootloader akan baca status dari kawasan selamat ini, dan tentukan sama ada jalankan pengesahan tandatangan ketat.

##### 🔐 Pengesahan tandatangan digital

Pengeluar apabila keluarkan kemas kini sistem atau image, akan guna kunci peribadi sendiri untuk menandatangani. Semasa peranti boot, Bootloader akan guna kunci awam terbina dalam untuk mengesahkan image sistem (seperti boot.img, recovery.img). Cara kerjanya:

1. III. Google Inactive Account Manager
2. Google sediakan "Inactive Account Manager" untuk mengurus akaun selepas kematian atau tidak aktif lama.
3. 1. Cara menetapkan

##### 🔗 Rantai boot selamat

Kunci BL adalah cincin pertama seluruh rantai boot selamat. Selepas lulus pengesahan, barulah muat dan laksanakan bootloader peringkat seterusnya (seperti kernel), lapis demi lapis pastikan persekitaran boot sistem boleh dipercayai.

##### 📊 Kunci vs Buka kunci: Dua kesan kunci BL

Pilih data mana yang boleh dikongsi dengan kontak (Foto, Gmail, Drive dll).

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 dark:border-gray-600 text-sm">
                            <thead>
                                <tr class="bg-gray-100 dark:bg-gray-800">
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Tetapkan sama ada padam akaun selepas berkongsi data.</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">2. Cara ia berfungsi</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Jika akaun tidak log masuk selama tempoh yang ditetapkan, Google hantar pemberitahuan kepada kontak.</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Kontak akan menerima link untuk muat turun data yang dipilih.</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Jika tetapkan padam akaun, akaun akan dipadam selepas tempoh tambahan 3 bulan.<br><span class="text-emerald-600 dark:text-emerald-400">IV. Facebook Memorial Account</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">⚠️ Keselamatan menurun: Benarkan flash ROM pihak ketiga, mekanisme pengesahan integriti sistem gagal, perisian hasad jika dapat kebenaran Root boleh ubahsuai sistem secara mendalam</span></td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">1. Cara menetapkan Legacy Contact</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Log masuk Facebook → Tetapan → Memorialization Settings<br><span class="text-emerald-600 dark:text-emerald-400">Pilih rakan sebagai Legacy Contact.</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">Legacy Contact boleh: menulis pos akhir, mengemas kini foto profil, membalas permintaan kawan.</span></td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Legacy Contact tidak boleh: log masuk sebagai pemilik, baca mesej peribadi, padam pos lama.</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2. Akaun memorial<br><span class="text-emerald-600 dark:text-emerald-400">Selepas kematian, akaun ditukar ke status "Memorial" — kata "Remembering" ditambah berdekatan nama.</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">Tidak boleh log masuk, tidak muncul dalam saranan kawan, tidak ada iklan.</span></td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">V. Langkah-langkah digital legacy yang anda boleh ambil sekarang</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1. Senarai akaun penting<br><span class="text-emerald-600 dark:text-emerald-400">Buat senarai semua akaun penting: e-mel, bank, media sosial, langganan, simpanan foto.</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">Risiko data: Unlock akan paksa padam semua data pengguna; jika tidak disulit dengan betul selepas unlock, storan data mungkin tidak selamat; selepas hilang lebih mudah di flash untuk ekstrak data</span></td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">2. Tetapkan kontak warisan</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pastikan fungsi yang bergantung pada persekitaran selamat (seperti pembayaran, App bank) berjalan normal<br><span class="text-emerald-600 dark:text-emerald-400">Untuk akaun yang tidak sokong, beritahu keluarga cara mengakses (melalui pengurus kata laluan atau nota fizikal).</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">Fungsi terhad: Sesetengah aplikasi sensitif keselamatan (seperti Google Pay, App bank) mungkin enggan berjalan disebabkan pengesanan status BL unlock; perkhidmatan DRM mungkin diturunkan, kesan pemainanan video HD</span></td>
                                </tr>
                            </tbody>
                        </table>
```
:::

#### 2. Aliran Terperinci Membuka Kunci BL (Contoh Xiaomi)

1. <strong>Tempoh menunggu</strong>: Mengikut peringkat akaun, perlu menunggu 7-30 hari.
2. <strong>Operasi nyahkunci</strong>: Gunakan alat nyahkunci Xiaomi sambung ke komputer untuk nyahkunci.
3. <strong>3. Pelbagai Skim Root</strong> Magisk
4. <strong>: Skim Root moden, reka bentuk Systemless, boleh menyembunyikan status Root.</strong> Kernelsu

#### 3. Pelbagai Skim Root

- <strong>SuperSU</strong>: Skim Root lama, kini telah berhenti dikemas kini.
- <strong>4. Pengenalan Memuat Turun Sistem</strong> Memuat turun sistem merujuk kepada memasang sistem pengoperasian baharu pada telefon. Jenis memuat turun yang biasa:
- <strong>Muat turun ROM rasmi</strong>: Memasang sistem rasmi, digunakan untuk menyelamatkan bata atau menurunkan taraf.

#### 4. Pengenalan Memuat Turun Sistem

: Seperti TWRP, digunakan untuk sandaran pemulihan, memuat turun ROM pihak ketiga.

- <strong>Muat turun ROM pihak ketiga</strong>: Seperti LineageOS, Pixel Experience dll., mengalami sistem yang berbeza.
- <strong>Amaran Penting</strong> Memuat turun sistem ada risiko, operasi perlu berhati-hati. Boleh menyebabkan:
- <strong>Telefon menjadi bata (tidak boleh dihidupkan)</strong> Hilang waranti

#### 5. Samsung Knox: Harga tidak boleh balik buka kunci BL

Berbeza dengan pengeluar Android lain, mekanisme buka kunci BL telefon Samsung ada reka bentuk "trip" yang unik:<strong>Bagi telefon Samsung, buka kunci akan pencetus Knox tripping, kekal hilang sebahagian fungsi keselamatan (seperti Samsung Pay); akan padam semua data dilindungi; kesan waranti</strong> Semak setiap tahun: Adakah kontak warisan masih sesuai? Adakah akaun baharu perlu ditambah?

- <strong>5. Pertimbangkan wasiat digital</strong>: Telefon ada satu fius eFuse, sekali dikesan BL dibuka kunci akan terbakar secara kekal, tidak boleh dipulihkan.
- <strong>VI. Pemulihan dan pemindahan data telefon lama</strong>: Samsung Pay (kad transit/kad bank), Knox Secure Folder, kawalan MDM enterprise, sesetengah App insurans kesihatan akan gagal.
- <strong>1. Pindah ke telefon baharu</strong> iPhone ke iPhone: Guna Quick Start (letakkan dua telefon berdekatan, ikut arahan).
- <strong>Android ke Android: Guna Google Backup atau alat pemindahan pengeluar.</strong>: Pihak rasmi jelas nyata selepas Knox trip tidak lagi nikmati perkhidmatan waranti.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Android ke iPhone: Guna App "Move to iOS" Apple.

{class="mt-1"}
Knox trip Samsung adalah <strong>Foto: Sandaran iCloud/Google Photos, atau salin terus melalui kabel USB.</strong>, sekali dicetus tidak boleh kembali ke status kilang. Jika anda hanya mahu guna fungsi yang asalnya memerlukan Root, cadangan dahulu semak sama ada ada alternatif tanpa Root.
:::

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-skull-crossbones mr-2"></i>Data hilang

{class="mt-1"}
Fungsi pembayaran tidak normal

{class="list-disc pl-6 mt-1 space-y-1"}
- Sebelum memuat turun sistem mesti buat sandaran lengkap, baca tutorial dengan teliti, sahkan model dan versi sepadan.
- Sistem tidak stabil
- XDA Developers
- : Komuniti pembangun Android terbesar di dunia, mempunyai tutorial memuat turun dan sumber ROM yang kaya.

{class="mt-1"}
Coolapk
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>: Komuniti digital terkenal dalam negara, mempunyai banyak tutorial dan perbincangan dalam bahasa Cina.

{class="list-disc pl-6 mt-1 space-y-1"}
- <strong>Forum setiap model</strong>: Seperti komuniti Xiaomi, komuniti OnePlus dll., mempunyai tutorial rasmi dan bukan rasmi.
- <strong>Bab 25: Pemprosesan Telefon Terpakai &amp; Warisan Digital</strong> Hei kawan-kawan, selepas lebih dua puluh bab "latihan", dipercayai anda telah bertumbuh daripada "pemula digital" menjadi pengguna telefon yang agak tenang. Tetapi kehidupan teknologi sentiasa berkitlar—kekasih baru akhirnya menjadi kekasih lama. Apabila anda bersedia membiarkan rakan lama ini "bersara", adakah anda tahu bagaimana berpisah secara bermaruah dan selamat?
- <strong>1. "Eutanasia" Telefon Lama: Panduan Jual atau Hadiah Selamat</strong> Prinsip teras: Pembersihan data bukan "memadam", tetapi "menindih".
:::

#### 6. Soalan Lazim (Q& A)

::: div .qa-item .mt-3
{class="font-semibold mb-1"}
<i class="fas fa-question-circle text-primary mr-1"></i>Q1: Selepas buka kunci BL boleh pulih?

{class="mb-2 pl-6"}
<strong>A:</strong> Boleh kunci semula. Biasanya perlu flash pakej wayar rasmi lengkap, dan guna skrip flash tertentu (seperti Xiaomi <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">flash_all_lock.bat</code>) boleh kunci semula. Tetapi perhatikan, selepas kunci semula, sesetengah trip keselamatan yang dicetus oleh buka kunci (seperti Knox Samsung) mungkin tidak boleh balik.
:::

::: div .qa-item .mt-3
{class="font-semibold mb-1"}
<i class="fas fa-question-circle text-primary mr-1"></i>Q2: Selepas buka kunci bagaimana Root?

{class="mb-2 pl-6"}
<strong>A:</strong> Buka kunci BL hanya langkah pertama. Root biasanya perlukan:

{class="list-decimal pl-12 mb-2 space-y-1"}
1. Tetapan → Sistem → Pilihan set semula → Padam semua data (Android).
2. Melalui Recovery flash Magisk dan pengurus Root lain untuk patch image boot, bagi mendapat kebenaran Root.
:::
