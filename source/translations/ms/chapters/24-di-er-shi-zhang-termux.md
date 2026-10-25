---
id: di-er-shi-zhang-termux
part: jin-jie-pian
nav: Lampiran Bab 20
toc: sub
kind: supplement
---

### Lampiran Bab 20: Termux — Persekitaran Terminal Linux Mudah Alih pada Peranti Android

{class="chapter-intro mb-4"}
Jika anda rasa mod pembangun masih belum cukup "keras", dan mahu mengalami baris perintah Linux yang lengkap pada telefon pintar, maka Termux adalah untuk anda. Ia tidak memerlukan kebenaran root, dan boleh menjadikan telefon pintar Android biasa menjadi stesen kerja Linux mudah alih, merupakan senjata ampuh bagi pengguna lanjutan untuk menerokai pembangunan dan pentadbiran mudah alih.

#### 1. Apakah itu Termux

Termux terbina dalam pelbagai persekitaran Shell seperti Bash, Zsh, fish, menyokong editor seperti Vim, Nano, Emacs, menyediakan pengalaman baris perintah yang hampir natif. Pengguna boleh memasang 2000+ pakej perisian melalui "pkg install", termasuk GCC, OpenSSH, SQLMap dan alat pembangunan serta keselamatan lain.

📦 Pengurusan Pakej yang Berkuasa

#### 2. Fungsi dan Ciri Teras

##### 🖥️ Persekitaran Linux Lengkap

Termux <strong>I. Kehilangan akaun: Apa yang berlaku jika tidak diuruskan</strong> Jika seseorang meninggal dunia secara mengejut, keluarga mungkin hadapi masalah berikut:<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install zsh</code>.<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg install fish</code> Akaun bank tidak boleh diakses: Wang dalam akaun bank dalam talian mungkin tidak boleh diakses oleh waris.

##### 📦 Pengurusan Pakej yang Berkuasa

Alat penyulitan

##### 🔒 Fungsi Keselamatan dan Rangkaian

- <strong>Pembinaan pelayan</strong>: Boleh mengkonfigurasi Nginx atau Apache untuk membina pelayan halaman web statik.
- <strong>🔧 Integrasi dan Sambungan Sistem</strong> Mengakses kebenaran penyimpanan telefon pintar, merealisasikan pengurusan fail tempatan.
- <strong>Memanggil fungsi perkakasan Android seperti penderia, kamera melalui pemalam Termux:API.</strong> Menyokong sambungan papan kekunci Bluetooth dan paparan luaran, dengan sokongan tetikus yang lengkap.

##### 🔧 Integrasi dan Sambungan Sistem

- Aplikasi teras Termux boleh dikembangkan melalui beberapa aplikasi pemalam pilihan, menyediakan fungsi dan integrasi tambahan:
- Nama Pemalam
- Penerangan Fungsi

#### 3. Ekosistem Pemalam

Mendedahkan fungsi API Android kepada program baris perintah

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                        <thead>
                            <tr class="bg-light dark:bg-gray-700">
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Termux:Boot</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Membenarkan skrip dijalankan semasa peranti dimulakan</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Float</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menyediakan tetingkap terminal terapung</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Styling</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Membolehkan penyesuaian skema warna dan fon untuk terminal</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Tasker</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mengintegrasikan skrip Termux dengan aplikasi automasi Tasker</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux:Widget</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Membenarkan skrip dijalankan dari widget skrin utama</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Petuan Penting</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Termux dan pemalamnya mesti dipasang dari sumber yang sama, kerana mereka berkongsi sharedUserId yang sama. Pemasangan campuran dari sumber yang berbeza (seperti F-Droid dan GitHub) akan menyebabkan ralat pemasangan.</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">4. Panduan Pemasangan dan Konfigurasi</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">📥 Langkah Pemasangan</td>
                            </tr>
                        </tbody>
                    </table>
```

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Muat turun aplikasi

{class="mt-1"}
: Muat turun dan pasang Termux dari saluran rasmi (F-Droid atau GitHub), tidak memerlukan kebenaran root.
:::

#### 4. Panduan Pemasangan dan Konfigurasi

##### 📥 Langkah Pemasangan

1. <strong>Dapatkan kebenaran penyimpanan</strong>: Laksanakan
2. <strong>termux-setup-storage</strong> untuk mendapatkan kebenaran sistem fail telefon pintar.
3. <strong>Kemas kini sumber perisian</strong>: Laksanakan<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pkg update &amp;&amp; pkg upgrade</code> untuk mengemas kini senarai pakej perisian.
4. <strong>⚙️ Pengoptimuman Asas</strong>: Laksanakan<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">.</code> termux-change-repo

##### ⚙️ Pengoptimuman Asas

- <strong>Tetapan kekunci pintasan</strong>: Kekunci volume turun menyelakuti Ctrl, kekunci volume naik menyelakuti Esc, meningkatkan kecekapan input.<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">Percantikan antara muka</code>: Pasang Zsh + Oh My Zsh, konfigurasikan tema dan pemalam.
- <strong>5. Senario Aplikasi Tipikal</strong>💻 Ujian Pembangunan Mudah Alih
- <strong>Membina persekitaran pembangunan yang lengkap pada telefon pintar, menulis dan menjalankan skrip Python, menggunakan GCC untuk menyusun program C, menguruskan repositori kod melalui Git, menggabungkan SSH untuk menyegerakkan dengan pelayan jarak jauh.</strong>🖥️ Pentadbiran Pelayan

#### 5. Senario Aplikasi Tipikal

##### 💻 Ujian Pembangunan Mudah Alih

Menyediakan persekitaran Linux yang sebenar, merupakan platform ideal untuk mempelajari baris perintah dan pentadbiran sistem, boleh berlatih penulisan skrip Shell, pengurusan kebenaran fail dan arahan asas lain.

##### 🖥️ Pentadbiran Pelayan

Memasang alat keselamatan seperti Nmap, SQLMap, Hydra, Metasploit, menjalankan pengimbasan rangkaian dan ujian penembusan.

##### 📚 Pembelajaran Operasi Linux

Kehilangan foto: Foto dalam awan mungkin hilang kerana akaun tidak log masuk lama. <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">chmod 755</code> Identiti palsu: Akaun media sosial mungkin diambil alih oleh orang lain untuk penipuan.<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">chown user:group</code> Langganan auto-baharu: Langganan mungkin terus dicas walaupun pemilik telah meninggal.<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">ls -l</code> II. Apple Legacy Contact — Penyelesaian rasmi iOS

##### 🔐 Ujian Keselamatan Rangkaian

Termux membawa pengalaman terminal Linux yang berkuasa ke peranti Android, menjadikan telefon pintar sebagai alat pembangunan dan pembelajaran mudah alih. Sama ada pembangun, pentadbir sistem atau peminat teknologi, semuanya boleh menggunakan Termux untuk menikmati pengalaman baris perintah yang lengkap pada peranti mudah alih, merealisasikan konsep "Linux dalam poket".

#### 6. Versi dan Keserasian

Muat turun dan pasang Termux dari F-Droid, tunggu permulaan selesai kali pertama.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Laksanakan

{class="mt-1"}
pkg update &amp;&amp; pkg upgrade
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>untuk mengemas kini pakej perisian.

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Pasang Python:
2. pkg install python<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">.</code> Masukkan
3. python3 -c "print('Hello from Termux!')"<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">, rasai keseronokan menjalankan kod pada telefon pintar.</code>
4. Bahagian ini akan membawa anda memasuki dunia digital yang lebih mendalam. Daripada keselamatan maklumat kepada prinsip AI, daripada pemikiran pengaturcaraan kepada warisan digital, kandungan ini akan membantu anda menjadi seorang warganegara digital yang sebenar.<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">Bab 21: Pendalaman Rangkaian Bergerak &amp; Keselamatan Maklumat</code> Kita menggunakan telefon untuk melayari internet, membuat pembayaran, dan bersembang setiap hari, rasa sangat mudah. Tetapi pernahkah anda terfikir, rekod sembang anda, kata laluan pembayaran, foto-foto anda... berapa kerap maklumat ini "berlari telanjang" di internet? Jujurlah, kebanyakan orang langsung tidak pernah memikirkan masalah ini, tetapi sekali berlaku insiden—contohnya akaun dicuri, kad bank dikuras—baru menyesal sudah terlambat. Dalam bab ini, kita akan bincang dengan baik, bagaimana membuat kehidupan digital anda tidak begitu "telus".
:::
