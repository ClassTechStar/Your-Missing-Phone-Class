---
id: di-er-shi-san-zhang-github
part: chao-yue-pian
nav:  Lampiran: Panduan Permulaan GitHub
toc: sub
kind: chapter
---

### Lampiran Bab 23: Panduan Permulaan GitHub — Daripada Hos Kod ke Platform Kolaborasi

{class="chapter-intro mb-4"}
Bab sebelumnya kita bincangkan "pemikiran pengaturcaraan", dan untuk benar-benar melaksanakan pemikiran pengaturcaraan dan membuat projek bersama orang lain, tidak boleh lari dari satu nama—GitHub. Sama ada anda pelajar jabatan sains komputer yang ingin menyertai pertandingan, ingin menyimpan karya kod anda, atau sekadar ingin melihat apa yang sedang dikerjakan oleh pembangun di seluruh dunia, GitHub adalah platform yang mesti anda kenali. Bahagian ini bermula dari konsep paling asas, membantu anda membina satu pemahaman yang jelas.

#### 1. Apakah Sebenarnya GitHub?

Git ialah buku harian di komputer anda, GitHub ialah platform blog awam <strong>—anda boleh menerbitkan karya sendiri, mengikuti projek orang lain, menyertai perbincangan dan kolaborasi. Ia bukan sahaja "gudang belakang pentas pengaturcara", lebih seperti sebuah "bandar teknologi" yang dibina bersama oleh pembangun di seluruh dunia—projek dilahirkan di sini, diulang, dibincangkan, diguna semula.</strong> Bagi orang biasa, GitHub juga bukan sesuatu yang jauh dari jangkauan. Ramai bukan pengaturcara menggunakannya untuk menghoskan nota, buku elektronik, blog peribadi, malah untuk menyandarkan fail konfigurasi. Selagi anda mempunyai sedikit keperluan "mahu mengemas benda anda dengan baik dan berkongsi", GitHub berbaloi untuk anda kenali.

2\. Perbezaan Antara Git dan GitHub (Konsep Penting!)<strong>Ramai orang akan mengelirukan dua perkataan ini ketika pertama kali terdedah, di sini membantu anda menyusun dengan jelas:</strong> Perbandingan

Git

#### 2. Perbezaan Antara Git dan GitHub (Konsep Penting!)

Hakikat

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                        <thead>
                            <tr class="bg-light dark:bg-gray-700">
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Alat kawalan versi (perisian)</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Platform hos kod (laman web)</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Lokasi pelaksanaan</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pada komputer tempatan</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Awan (diakses melalui pelayar)</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tanggungjawab teras</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Merakam setiap perubahan fail (bagaimana diubah, siapa mengubah, bila diubah)</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Meletakkan repositori Git di awan, memudahkan storan, paparan, kolaborasi</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Perlukan rangkaian</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tidak perlu, boleh digunakan luar talian</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Perlu sambungan rangkaian untuk mengakses</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kepemilikan</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Perisian sumber terbuka, dicipta oleh Linus Torvalds (bapa Linux)</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Produk di bawah Microsoft</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pesaing serupa</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SVN, Mercurial</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GitLab, Gitee, Bitbucket</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ringkasnya:</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Git mengurus "bagaimana merakam perubahan", GitHub mengurus "perubahan diletakkan di mana, bagaimana berkolaborasi"</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">. Git ialah alat, berjalan secara tempatan; GitHub ialah platform, meletakkan repositori Git di awan, memudahkan kolaborasi dan paparan. Anda boleh guna Git sahaja tanpa GitHub (contohnya menulis kod sendiri untuk pengurusan versi), tetapi menggunakan GitHub mesti guna Git (kerana GitHub berasaskan Git).</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3. Konsep Teras dan Fungsi GitHub</td>
                            </tr>
                        </tbody>
                    </table>
```

📁 Konsep Asas <strong>Sebelum bertindak, kenali beberapa perkataan berfrekuensi tinggi dahulu, jika tidak melihat antara muka GitHub akan keliru:</strong> Repositori (Repository, singkatannya Repo)

#### 3. Konsep Teras dan Fungsi GitHub

##### 📁 Konsep Asas

: Rekod satu pengubahsuaian kod. Setiap Commit disertakan mesej maklumat, merakam "apa yang diubah kali ini, mengapa diubah". Ini adalah asas bagi Git/GitHub untuk "mengembalikan masa".

- <strong>Cabang (Branch)</strong>: Garis pembangunan bebas yang bercabang dari garisan utama. Contohnya anda ingin menambah fungsi baharu, boleh buka satu cabang untuk membangunkan secara berasingan, selepas selesai kemudian gabungkan kembali ke garisan utama, tidak menjejaskan orang lain.
- <strong>Klon (Clone)</strong>: Menyalin repositori awan secara lengkap ke komputer tempatan, selepas itu boleh mengubah kod secara tempatan.
- <strong>Dorong (Push)/Tarik (Pull)</strong>: Push ialah memuat naik kod tempatan ke GitHub, Pull ialah memuat turun kod terkini dari GitHub ke tempatan. Ini adalah dua tindakan teras untuk menyegerakkan kod semasa kolaborasi pasukan.
- <strong>Permintaan Gabung (Pull Request, singkatannya PR)</strong>: Apabila anda selesai mengubah kod pada satu cabang dan ingin menggabungkannya ke cabang utama, anda memulakan satu PR, membolehkan ahli pasukan menyemak kod sebelum menggabungkan. Ini adalah mekanisme teras kolaborasi GitHub.
- <strong>Isu (Issue)</strong>: Digunakan untuk merakam bug, permintaan fungsi, topik perbincangan. Setiap Issue seperti satu hantaran perbincangan, boleh ditugaskan orang bertanggungjawab, diberikan label.
- <strong>Fork</strong>: Menyalin repositori orang lain ke akaun anda sendiri, anda boleh mengubah salinan anda sesuka hati, tidak menjejaskan repositori asal. Selepas siap mengubah, boleh hantar PR kepada penulis asal, meminta menggabungkan penambahbaikan anda.
- <strong>🛠️ Fungsi Teras</strong> GitHub menyediakan bukan sahaja storan kod, tetapi juga termasuk:
- <strong>Kawalan versi</strong>: Merakam sejarah setiap perubahan kod, kod rosak boleh kembali ke versi normal sebelumnya bila-bila masa.

##### 🛠️ Fungsi Teras

: Menyokong pembangunan selari berbilang pengguna pada projek yang sama, ramai orang membangunkan serentak tidak akan menimpa, tidak akan berkonflik.

- <strong>Penjejakan masalah</strong>: Gunakan Issue merakam bug dan permintaan fungsi, memudahkan pasukan menjejaki.
- <strong>Pengurusan projek</strong>: Mengintegrasikan item tindakan, papan projek (Projects) dan alat pengurusan lain, setara dengan Trello ringan terbina dalam.
- <strong>Automasi</strong>: Melalui
- <strong>GitHub Actions</strong> merealisasikan kompilasi automatik, ujian, pembungkusan, penyebaran selepas kod dihantar, merupakan alat teras "CI/CD (Integrasi Berterusan/Penyebaran Berterusan)" moden.
- <strong>Pengurusan dokumentasi</strong>: README memperkenalkan projek, Wiki menyimpan seni bina terperinci dan spesifikasi pembangunan, Pages malah boleh terus menghoskan laman web statik.<strong>Hos kod dan paparan</strong>: Setiap repositori mempunyai paparan laman web yang cantik, menyokong penonjolan sintaks, merupakan "muka depan" karya teknikal anda.
- <strong>Komuniti sumber terbuka</strong>: Anda boleh Star (kutip) projek yang disukai, Watch (ikuti) dinamik projek, Follow (ikuti) pembangun, menyertai kolaborasi sumber terbuka global.
- <strong>4. Pendaftaran dan Permulaan: Lima Minit Mencipta Repositori Pertama Anda</strong>📝 Daftar akaun
- <strong>Lawati</strong> github.com

#### 4. Pendaftaran dan Permulaan: Lima Minit Mencipta Repositori Pertama Anda

##### 📝 Daftar akaun

1. github.com/yourname<a href="https://github.com" class="text-primary hover:underline" target="_blank" rel="noopener">).</a>Selesaikan pengesahan e-mel dan pengesahan manusia-mesin.
2. Pilih pelan percuma (Free) sudah memadai, untuk pengguna peribadi cukup sepenuhnya.<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">📁 Cipta repositori pertama</code> Selepas log masuk klik tanda "+" di penjuru kanan atas, pilih "New repository".
3. Isikan nama repositori (Repository name), contohnya
4. my-first-project

##### 📁 Cipta repositori pertama

1. Tulis satu penerangan ringkas (Description), membiarkan orang lain tahu repositori ini untuk apa.
2. Pilih Awam (Public) atau Peribadi (Private). Repositori awam boleh dilihat semua orang, peribadi hanya boleh dilihat diri sendiri dan kolaborator. Akaun percuma juga menyokong repositori peribadi tanpa had.<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">Tandakan "Add a README file"—README ialah "manual arahan" projek, setiap repositori disyorkan mempunyainya.</code>
3. Pengetahuan Kecil: Apakah README
4. README.md ialah fail format Markdown, kandungan pertama yang dilihat orang lain apabila membuka repositori anda. README yang baik biasanya mengandungi: pengenalan projek, kaedah pemasangan, contoh penggunaan, lesen, maklumat hubungan. Menulis README yang baik adalah kualiti asas pengaturcara, juga merupakan ambang pertama sama ada projek boleh digunakan oleh orang lain.
5. 5. Aliran Kerja Asas: Daripada Tempatan ke Awan
6. Memahami aliran kerja GitHub, terasnya ialah mengingat kitaran ini:

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Ubah tempatan → Peringkat → Commit → Push → Kemas kini awan

{class="mt-1"}
. Di bawah ini dijelaskan setiap langkah dalam bahasa mudah:
:::

#### 5. Aliran Kerja Asas: Daripada Tempatan ke Awan

: Tulis kod atau ubah dokumen menggunakan editor di komputer tempatan.<strong>git add</strong>: Masukkan fail yang diubah ke "kawasan peringatan", setara dengan memberitahu Git "perubahan ini saya bersedia merakamnya".

1. <strong>git commit</strong>: Merakam perubahan di kawasan peringatan secara rasmi menjadi satu "commit", disertakan satu ayat penjelasan, contohnya "baiki bug log masuk". Langkah ini hanya dilengkapkan secara tempatan.
2. <strong>git push</strong>: Memuat naik commit tempatan ke awan GitHub, supaya orang lain boleh melihatnya.
3. <strong>git pull</strong>: Sebelum mula bekerja, tarik kod terkini dari awan dahulu, memastikan tempatan kekal disegerakkan dengan ahli pasukan yang lain.
4. <strong>Bagi pemula, ingat formula ini:</strong>"Pull dulu baru ubah, selepas ubah add, commit bawa penjelasan, akhirnya push ke atas"
5. <strong>. Biasakan tabiat ini, kolaborasi pasukan tidak akan kacau.</strong>6. Aliran Kerja Kolaborasi Pasukan: Bagaimana Pull Request Berfungsi

Tempat paling kuat GitHub terletak pada mekanisme kolaborasinya. Satu aliran kerja kolaborasi pasukan yang tipikal adalah seperti ini:<strong>Buka cabang</strong>: Buka satu cabang baharu dari cabang utama (biasanya dipanggil main atau master), contohnya

#### 6. Aliran Kerja Kolaborasi Pasukan: Bagaimana Pull Request Berfungsi

, membangunkan fungsi baharu pada cabang ini.

1. <strong>Bangun dan commit</strong>: Tulis kod pada cabang baharu, commit berkali-kali merakam kemajuan.<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">Dorong ke GitHub</code>: Dorong cabang ke repositori awan.
2. <strong>Mulakan Pull Request</strong>: Mulakan PR di laman web GitHub, meminta menggabungkan cabang anda ke cabang utama. Jelaskan dengan jelas apa perubahan yang dilakukan PR ini, mengapa diubah.
3. <strong>Semakan kod (Code Review)</strong>: Ahli pasukan melihat kod anda, mengemukakan pendapat atau cadangan pengubahsuaian. Anda boleh terus commit berdasarkan maklum balas, PR akan dikemas kini secara automatik.
4. <strong>Gabung</strong>: Selepas semakan lulus, klik "Merge" untuk menggabungkan kod ke cabang utama. Sumbangan anda secara rasmi memasuki projek!
5. <strong>Aliran ini menjamin</strong> mana-mana kod sebelum memasuki cabang utama telah disemak
6. <strong>, sangat mengurangkan kebarangkalian kesilapan. Projek sumber terbuka juga menggunakan mekanisme ini untuk menerima sumbangan daripada orang asing di seluruh dunia—anda benar-benar boleh menghantar PR pada sesetengah projek sumber terbuka terkenal, selepas diterima anda menjadi penyumbang projek tersebut.</strong>7. Senario Aplikasi Tipikal GitHub

🎓 Pelajar menyertai pertandingan dan projek kursus <strong>Pelajar jabatan sains komputer menyertai ACM, hackathon, reka bentuk pengijazahan, hampir semuanya tidak boleh lari dari GitHub. Ia bukan sahaja boleh menjadi platform kolaborasi pasukan, juga boleh menjadi tetingkap pameran karya—juri pertandingan boleh terus melihat repositori anda, memahami kualiti kod dan proses kolaborasi. Ramai syarikat semasa merekrut juga meminta melampirkan halaman utama GitHub, sebagai bukti keupayaan teknikal.</strong>📚 Pangkalan pengetahuan peribadi dan hos nota

#### 7. Senario Aplikasi Tipikal GitHub

##### 🎓 Pelajar menyertai pertandingan dan projek kursus

GitHub adalah pusat gerakan sumber terbuka global. Anda boleh Fork projek yang disukai, mengubah dan menghantar PR untuk membalas komuniti; juga boleh sekadar Star mengutip projek baik, menjejaki kemas kini. Menyertai sumber terbuka adalah jalan terbaik untuk meningkatkan teknologi dan mengumpul reputasi.

##### 📚 Pangkalan pengetahuan peribadi dan hos nota

Dengan bantuan GitHub Actions, boleh merealisasikan aliran sepenuhnya automatik "kod sekali push, automatik uji + automatik sebar ke pelayan". Ramai blog peribadi dan laman dokumentasi dibina sedemikian, selepas menulis artikel push sekali, laman web dikemas kini secara automatik.

##### 🌐 Menyertai projek sumber terbuka

Gunakan repositori kod sebagai pemacu awan, tukar komputer, bekerja berbilang peranti, git pull sekali boleh mendapatkan kod terkini, tidak perlu lagi salin bolak-balik menggunakan pemacu USB.

##### 🤖 Penyebaran automatik dan CI/CD

Mesej commit mesti ditulis dengan jelas

##### 💾 Sandaran kod dan penyegerakan berbilang peranti

Rajin commit, langkah kecil berlari pantas

#### 8. Beberapa Cadangan untuk Pemula

- <strong>Gunakan cabang untuk membangun, jangan ubah terus cabang utama</strong>: Walaupun projek peribadi, biasakan membuka cabang, semasa kolaborasi pasukan pada masa hadapan tidak akan tergopoh-gopoh.
- <strong>Manfaatkan .gitignore</strong>: Fail ini digunakan untuk memberitahu Git fail mana yang tidak perlu dimasukkan dalam pengurusan versi (contohnya konfigurasi kata laluan, keluaran kompilasi, folder kebergantungan), mengelakkan memuat naik fail sampah.
- <strong>Banyak melihat projek sumber terbuka yang cemerlang</strong>: Layari GitHub Trending, lihat struktur kod projek bintang tinggi, cara menulis README, aliran kolaborasi, adalah cara percuma paling cepat untuk meningkatkan diri.
- <strong>Mohon pakej pelajar GitHub</strong>: Selepas pengesahan pelajar boleh mendapatkan kuota banyak alat dan perkhidmatan berbayar secara percuma (Copilot, nama domain, perkhidmatan awan dll.), bernilai ribuan dolar.
- <strong>Peringatan Keselamatan</strong> Jangan sekali-kali memuat naik kata laluan, kunci API, rentetan sambungan pangkalan data dan maklumat sensitif lain ke GitHub, terutamanya repositori awam—selepas bocor, akan ditangkap oleh perayau dalam beberapa saat, akibatnya serius.
- <strong>Tidak sengaja memuat naik maklumat sensitif, hanya memadam fail tidak cukup (masih ada dalam rekod sejarah), perlu gunakan</strong> git filter-branch

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>atau alat profesional membersihkan sejarah, dan segera tukar kunci yang bocor.

{class="list-disc pl-6 mt-1 space-y-1"}
- Repositori peribadi juga tidak mutlak selamat, maklumat sensitif lebih baik diurus menggunakan pemboleh ubah persekitaran, jangan masuk ke repositori kod.
- Perkara yang perlu diperhatikan apabila mengakses GitHub dari dalam negara<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">GitHub kadang-kadang tidak stabil apabila diakses dari dalam negara, mungkin muncul tidak boleh dibuka, klon perlahan. Boleh cuba: ① Gunakan tapak cermin dalam negara (seperti GitClone, ghproxy) mempercepat klon; ② Konfigurasikan Hosts atau gunakan proksi; ③ Jika utamanya untuk kolaborasi dalam negara, juga boleh pertimbangkan pengganti domestik</code> Gitee
- , fungsinya serupa dan kelajuan akses pantas. Ramai pasukan akan menghoskan di GitHub dan Gitee serentak, mengambil kira kedua-dua pengantarabangsaan dan kelajuan domestik.
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Gaya lanjutan: Gunakan GitHub Pages membina blog peribadi percuma

{class="mt-1"}
GitHub Pages membolehkan anda menghoskan satu laman web statik secara percuma, dipadankan dengan penjana tapak statik seperti Jekyll, Hexo, Hugo, boleh membina blog peribadi dengan mudah. Selepas menulis artikel Markdown push ke repositori, blog dikemas kini secara automatik, juga dilengkapi HTTPS dan nama domain tersuai. Blog ramai blogger teknikal dibina sedemikian, kos sifar, tiada iklan, versi terkawal.<strong>9. Ringkasan: Mengapa Setiap Orang Patut Mengenali GitHub</strong> GitHub sudah lama bukan sekadar "alat pengaturcara", ia lebih seperti satu
:::

::: div .success-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>cara kerja era digital

{class="mt-1"}
: pengurusan versi menjadikan semua boleh dijejak, mekanisme kolaborasi menjadikan pasukan beroperasi cekap, semangat sumber terbuka menjadikan pengetahuan mengalir bebas. Walaupun anda tidak menulis kod, memahami konsep "commit, cabang, gabung" juga boleh membantu anda menguruskan lebih baik apa-apa kandungan yang memerlukan "pengubahsuaian berulang + kolaborasi berbilang orang"—daripada tesis kepada dokumen, daripada nota kepada cadangan.
:::

#### 9. Ringkasan: Mengapa Setiap Orang Patut Mengenali GitHub

Mari bertindak: Selesaikan pengalaman pertama GitHub anda <strong>Daftar satu akaun GitHub, lengkapkan profil peribadi (avatar, pengenalan, bidang teknologi yang diminati).</strong> Cipta satu repositori awam bernama

hello-github

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>, tandakan "Add a README file".

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Masuk ke repositori, klik butang edit README.md (ikon pensil), tulis satu pengenalan diri dengan Markdown, commit perubahan.
2. Dalam bar carian GitHub cari satu kata kunci yang anda minati (contohnya<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">python-tutorial</code>), Star dua projek yang anda suka.
3. (Lanjutan) Pasang Git di komputer, klon repositori ke tempatan, ubah README kemudian push kembali ke awan, selesaikan satu aliran kerja "tempatan → awan" yang lengkap.
4. Bab 24: Analisis Mendalam Kebenaran Root &amp; Kunci BL<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">Bab ini adalah pengembangan mendalam terhadap kandungan Bab 20, sesuai untuk pengguna yang benar-benar ingin memahami mekanisme peringkat bawah telefon, malah mencuba memuat turun sistem. Sila ambil perhatian, operasi ini mempunyai risiko tertentu, sila berhati-hati.</code>1. Memahami Bootloader Secara Mendalam
5. Bootloader ialah program pertama yang berjalan semasa telefon dimulakan, tugasnya ialah memulakan perkakasan, memuatkan kernel sistem pengoperasian. Boleh anggap Bootloader sebagai "penjaga pintu" telefon.
:::
