---
id: di-er-shi-zhang-termux
part: jin-jie-pian
nav: Bab 20 Appendix
toc: sub
kind: supplement
---

### Bab 20 Lampiran: Termux — Lingkungan terminal Linux portabel pada perangkat Android

{class="chapter-intro mb-4"}
Jika Anda merasa mode pengembang belum cukup "hardcore", dan ingin mengalami command line Linux lengkap di ponsel, maka Termux adalah untuk Anda. Tanpa perlu izin root, ia dapat mengubah ponsel Android biasa menjadi workstation Linux portabel, merupakan senjata ampuh bagi pengguna lanjutan untuk menjelajahi pengembangan dan operasi mobile.

#### 1. Apa itu Termux

Keunggulan inti Termux terletak pada ringan dan sangat dapat diperluas, cocok untuk berbagai skenario seperti pengembangan, pembelajaran, dan administrasi sistem. Ini menggabungkan paket perangkat lunak standar dengan emulasi terminal yang presisi dalam satu solusi open source.

2\. Fungsi dan karakteristik inti

#### 2. Fungsi dan karakteristik inti

##### 🖥️ Lingkungan Linux lengkap

Termux <strong>Hanya Built-in Bash</strong> satu jenis Shell ini. Jika ingin memakai Zsh atau fish dan Shell lain, perlu via package manager install manual, misalnya:<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install zsh</code> atau<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install fish</code>. Bersamaan Termux mendukung editor Vim, Nano, Emacs, dll., memberikan pengalaman command line mendekati native. Pengguna bisa via "pkg install" install 2000+ package, termasuk GCC, OpenSSH, SQLMap, dan tool development serta security lain.

##### 📦 Manajemen paket yang kuat

🔒 Fungsi keamanan dan jaringan

##### 🔒 Fungsi keamanan dan jaringan

- <strong>: Mendukung fungsi klien dan server SSH, dapat terhubung remote ke perangkat lain atau menjadikan ponsel sebagai host SSH.</strong> Alat enkripsi
- <strong>: Menyediakan alat enkripsi seperti OpenSSL, mendukung enkripsi data dan komunikasi aman.</strong> Pembangunan server
- <strong>: Dapat mengkonfigurasi Nginx atau Apache untuk membangun server halaman web statis.</strong>🔧 Integrasi sistem dan ekstensi

##### 🔧 Integrasi sistem dan ekstensi

- Memanggil fungsi perangkat keras Android seperti sensor, kamera melalui plugin Termux:API.
- Mendukung koneksi keyboard Bluetooth dan layar eksternal, memiliki dukungan mouse lengkap.
- 3. Ekosistem plugin

#### 3. Ekosistem plugin

Nama plugin

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                        <thead>
                            <tr class="bg-light dark:bg-gray-700">
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Deskripsi fungsi</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Termux:API</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mengekspos fungsi Android API ke program command line</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Boot</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Memungkinkan menjalankan script saat perangkat booting</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Float</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menyediakan jendela terminal mengambang</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Styling</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mengaktifkan skema warna dan kustomisasi font untuk terminal</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Tasker</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mengintegrasikan script Termux dengan aplikasi otomasi Tasker</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Widget</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Memungkinkan menjalankan script dari widget layar utama</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Penting</td>
                            </tr>
                        </tbody>
                    </table>
```

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Termux dan plugin-nya harus diinstal dari sumber yang sama, karena mereka berbagi sharedUserId yang sama. Mencampur instalasi dari sumber berbeda (seperti F-Droid dan GitHub) akan menyebabkan error instalasi.

{class="mt-1"}
4\. Panduan instalasi dan konfigurasi
:::

#### 4. Panduan instalasi dan konfigurasi

##### 📥 Langkah instalasi

1. <strong>: Unduh dan instal Termux dari saluran resmi (F-Droid atau GitHub), tanpa perlu izin root.</strong> Inisialisasi sistem
2. <strong>: Setelah pertama kali dijalankan tunggu "Installing bootstrap packages" selesai.</strong> Dapatkan izin penyimpanan
3. <strong>: Jalankan</strong> pkg update &amp;&amp; pkg upgrade<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">untuk mendapatkan izin sistem file ponsel.</code> Update sumber perangkat lunak
4. <strong>: Jalankan</strong> pkg update &amp;&amp; pkg upgrade<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">untuk memperbarui paket perangkat lunak.</code>⚙️ Optimasi dasar

##### ⚙️ Optimasi dasar

- <strong>: Gunakan perintah</strong> termux-change-repo<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">untuk mengganti mirror source melalui antarmuka grafis (rekomendasi mirror Tsinghua University).</code> Pengaturan shortcut
- <strong>: Tombol volume turun mensimulasikan Ctrl, tombol volume naik mensimulasikan Esc, meningkatkan efisiensi input.</strong> Pempercantik antarmuka
- <strong>: Pasang Zsh + Oh My Zsh, konfigurasikan tema dan plugin.</strong>5. Skenario aplikasi tipikal

#### 5. Skenario aplikasi tipikal

##### 💻 Pengujian pengembangan mobile

🖥️ Operasi dan pemeliharaan server

##### 🖥️ Operasi dan pemeliharaan server

📚 Belajar operasi Linux

##### 📚 Belajar operasi Linux

Menyediakan environment Linux nyata, adalah platform ideal untuk belajar command line dan manajemen sistem, bisa latih Shell scripting, manajemen permission file Linux (seperti <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">chmod 755</code> setel permission bit rwxr-xr-x,<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">chown user:group</code> modifikasi ownership file,<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">ls -l</code> lihat permission tiga kelompok sembilan bit owner/group/other) dan perintah dasar lain. Perhatikan ini adalah model permission "tiga kelompok sembilan bit" klasik Unix/Linux (owner / group / other × read / write / execute), berbeda total dengan ACL access control list Windows NTFS, dua sistem yang berbeda.

##### 🔐 Pengujian keamanan jaringan

6\. Versi dan kompatibilitas

#### 6. Versi dan kompatibilitas

Kesimpulan

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Termux membawa pengalaman terminal Linux yang kuat ke perangkat Android, menjadikan ponsel sebagai alat pengembangan dan pembelajaran portabel. Baik pengembang, administrator sistem, maupun penggemar teknologi, semua dapat memanfaatkan Termux untuk menikmati pengalaman command line lengkap di perangkat mobile, mewujudkan konsep "Linux di saku".

{class="mt-1"}
Mari praktik: Jalankan perintah Linux pertama di ponsel
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Unduh dan instal Termux dari F-Droid, tunggu inisialisasi selesai saat pertama dijalankan.

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Jalankan
2. pkg update &amp;&amp; pkg upgrade<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">untuk memperbarui paket perangkat lunak.</code> Pasang Python:
3. pkg install python<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">.</code>.
4. python3 -c "print('Hello from Termux!')"<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">, rasakan keseruan menjalankan kode di ponsel.</code> IV. Bagian Melampaui (Bab 21-26)
:::
