---
id: di-er-shi-san-zhang-github
part: chao-yue-pian
nav: Lampiran: Panduan pemula GitHub
toc: sub
kind: chapter
---

### Lampiran Bab 23: Panduan Pemula GitHub—Dari Hosting Kode ke Platform Kolaborasi

{class="chapter-intro mb-4"}
Bab sebelumnya membahas "pemikiran pemrograman", dan untuk benar-benar mewujudkan pemikiran pemrograman dan mengerjakan proyek bersama orang lain, tidak bisa dipisahkan dari satu nama—GitHub. Baik Anda mahasiswa ilmu komputer yang ingin mengikuti kompetisi, ingin menyimpan karya kode Anda, atau sekadar ingin melihat apa yang dikerjakan developer global, GitHub adalah platform yang harus Anda kenal. Bagian ini dimulai dari konsep paling dasar, membantu Anda membangun pemahaman yang jelas.

#### 1. Apa Sebenarnya GitHub Itu?

Singkatnya, GitHub adalah <strong>platform hosting kode dan kolaborasi berbasis Git</strong>. Diluncurkan pada 2008, diakuisisi Microsoft pada 2018, hingga kini masih menjadi platform hosting kode open source terbesar di dunia, menampung ratusan juta repository, mencakup hampir semua bahasa pemrograman mainstream.

Jika menggunakan analogi:<strong>Git adalah buku harian di komputer Anda, GitHub adalah platform blog publik</strong>—Anda bisa mempublikasikan karya Anda, mengikuti proyek orang lain, berpartisipasi dalam diskusi dan kolaborasi. Ia bukan hanya "gudang backstage programmer", tapi lebih seperti "kota teknologi" yang dibangun bersama oleh developer global—proyek lahir, diiterasi, didiskusikan, dan digunakan ulang di sini.

Bagi orang biasa, GitHub juga tidak terlalu jauh dari jangkauan. Banyak non-programmer menggunakannya untuk hosting catatan, buku elektronik, blog pribadi, bahkan untuk backup file konfigurasi. Selama Anda memiliki sedikit kebutuhan "ingin mengatur dan membagikan barang Anda", GitHub layak untuk dipelajari.

#### 2. Perbedaan Git dan GitHub (Konsep Kunci!)

Banyak orang bingung dengan dua istilah ini saat pertama kali bertemu, berikut kami uraikan:

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                        <thead>
                            <tr class="bg-light dark:bg-gray-700">
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Item Perbandingan</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Git</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">GitHub</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Esensi</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Alat kontrol versi (perangkat lunak)</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Platform hosting kode (situs web)</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lokasi berjalan</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Di komputer lokal</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cloud (akses browser)</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tanggung jawab inti</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mencatat setiap perubahan file (bagaimana diubah, siapa mengubah, kapan diubah)</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menempatkan repository Git di cloud, memudahkan penyimpanan, tampilan, kolaborasi</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Butuh jaringan?</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tidak perlu, bisa offline</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Perlu internet untuk akses</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kepemilikan</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Perangkat lunak open source, dibuat oleh Linus Torvalds (bapak Linux)</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Produk milik Microsoft</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kompetitor sejenis</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SVN, Mercurial</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GitLab, Gitee, Bitbucket</td>
                            </tr>
                        </tbody>
                    </table>
```

Singkatnya:<strong>Git mengurus "bagaimana mencatat perubahan", GitHub mengurus "di mana perubahan disimpan, bagaimana berkolaborasi"</strong>. Git adalah alat, berjalan secara lokal; GitHub adalah platform, menempatkan repository Git di cloud, memudahkan kolaborasi dan tampilan. Anda bisa menggunakan Git tanpa GitHub (misalnya menulis kode sendiri untuk kontrol versi), tapi menggunakan GitHub harus menggunakan Git (karena GitHub berbasis Git).

#### 3. Konsep dan Fungsi Inti GitHub

##### 📁 Konsep Dasar

Sebelum mulai, kenali beberapa kata frekuensi tinggi, jika tidak antarmuka GitHub akan membingungkan:

- <strong>Repository (Repo)</strong>: Satu proyek sesuai dengan satu repository, berisi semua file kode proyek, versi historis, dan dokumentasi. Bisa dipahami sebagai "folder proyek".
- <strong>Commit</strong>: Catatan satu modifikasi kode. Setiap Commit disertai pesan, mencatat "apa yang diubah kali ini, mengapa diubah". Ini adalah dasar Git/GitHub bisa "mundur waktu".
- <strong>Branch</strong>: Jalur pengembangan independen yang dipisahkan dari jalur utama. Misalnya ingin menambah fitur baru, bisa buka branch untuk pengembangan terpisah, setelah selesai merge kembali ke jalur utama, tidak mempengaruhi orang lain.
- <strong>Clone</strong>: Menyalin lengkap repository cloud ke komputer lokal, setelah itu bisa mengubah kode secara lokal.
- <strong>Push/Pull</strong>: Push adalah mengunggah kode lokal ke GitHub, Pull adalah mengunduh kode terbaru dari GitHub ke lokal. Ini adalah dua action inti untuk sinkronisasi kode saat kolaborasi tim.
- <strong>Pull Request (PR)</strong>: Saat Anda selesai mengubah kode di sebuah branch dan ingin merge ke branch utama, ajukan PR, biarkan anggota tim meninjau kode sebelum merge. Ini adalah mekanisme inti kolaborasi GitHub.
- <strong>Issue</strong>: Digunakan untuk mencatat bug, permintaan fitur, topik diskusi. Setiap Issue seperti thread diskusi, bisa menugaskan penanggung jawab, memberi label.
- <strong>Fork</strong>: Menyalin repository orang lain ke akun Anda sendiri, Anda bisa bebas mengubah di salinan Anda tanpa mempengaruhi repository asli. Setelah selesai bisa kirim PR ke penulis asli, minta merge perbaikan Anda.

##### 🛠️ Fungsi Inti

GitHub tidak hanya menyediakan penyimpanan kode, tetapi juga:

- <strong>Kontrol versi</strong>: Mencatat riwayat setiap perubahan kode, jika kode rusak bisa kembali ke versi normal sebelumnya kapan saja.
- <strong>Kolaborasi tim</strong>: Mendukung pengembangan paralel pada proyek yang sama oleh multiple user, banyak orang mengembangkan bersamaan tanpa menimpa, tanpa konflik.
- <strong>Pelacakan masalah</strong>: Gunakan Issue untuk mencatat bug dan permintaan fitur, memudahkan tim menindaklanjuti.
- <strong>Manajemen proyek</strong>: Terintegrasi dengan to-do list, project board (Projects), dan alat manajemen lainnya, setara dengan Trello ringan bawaan.
- <strong>Otomatisasi</strong>: Melalui <strong>GitHub Actions</strong> mengimplementasikan kompilasi otomatis, testing, packaging, deployment setelah commit kode, adalah alat inti "CI/CD (Continuous Integration/Continuous Deployment)" modern.
- <strong>Manajemen dokumentasi</strong>: README memperkenalkan proyek, Wiki menyimpan arsitektur detail dan standar pengembangan, Pages bahkan bisa langsung hosting situs web statis.
- <strong>Hosting dan tampilan kode</strong>: Setiap repository memiliki tampilan web yang cantik, mendukung syntax highlighting, adalah "etale" karya teknis Anda.
- <strong>Komunitas open source</strong>: Anda bisa Star (koleksi) proyek favorit, Watch (ikuti) dinamika proyek, Follow (ikuti) developer, berpartisipasi dalam kolaborasi open source global.

#### 4. Registrasi dan Memulai: Buat Repository Pertama Anda dalam Lima Menit

##### 📝 Registrasi Akun

1. Kunjungi<a href="https://github.com" class="text-primary hover:underline" target="_blank" rel="noopener">github.com</a>, klik "Sign up".
2. Isi email, setel kata sandi dan username (username akan muncul di alamat halaman pribadi Anda, disarankan menggunakan bahasa Inggris, misalnya<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">github.com/yourname</code>).
3. Selesaikan verifikasi email dan verifikasi human-machine.
4. Pilih paket gratis (Free) saja, sudah cukup untuk pengguna individu.

##### 📁 Buat Repository Pertama

1. Setelah login, klik tanda "+" di pojok kanan atas, pilih "New repository".
2. Isi nama repository (Repository name), misalnya<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">my-first-project</code>.
3. Tulis deskripsi singkat (Description), agar orang tahu untuk apa repository ini.
4. Pilih Public atau Private. Repository publik terlihat oleh semua orang, private hanya oleh Anda dan kolaborator. Akun gratis juga mendukung repository private tak terbatas.
5. Centang "Add a README file"—README adalah "buku panduan" proyek, setiap repository disarankan memilikinya.
6. Klik "Create repository", repository GitHub pertama Anda lahir!

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Pengetahuan Kecil: Apa itu README

{class="mt-1"}
README.md adalah file format Markdown, konten pertama yang dilihat orang saat membuka repository Anda. README yang baik biasanya berisi: pengenalan proyek, cara instalasi, contoh penggunaan, lisensi, kontak. Menulis README yang baik adalah kompetensi dasar programmer, juga ambang pertama apakah proyek bisa digunakan orang lain.
:::

#### 5. Workflow Dasar: Dari Lokal ke Cloud

Memahami workflow GitHub, intinya adalah mengingat siklus ini:<strong>Modifikasi lokal → Staging → Commit → Push → Update cloud</strong>. Berikut penjelasan setiap langkah dalam bahasa sederhana:

1. <strong>Modifikasi file</strong>: Tulis kode atau ubah dokumen dengan editor di komputer lokal.
2. <strong>git add</strong>: Tambahkan file yang dimodifikasi ke "staging area", setara dengan memberi tahu Git "perubahan ini saya siap catat".
3. <strong>git commit</strong>: Catat perubahan staging area secara resmi sebagai "commit", sertakan pesan, misalnya "fix login bug". Langkah ini hanya selesai secara lokal.
4. <strong>git push</strong>: Unggah commit lokal ke cloud GitHub, sehingga orang lain bisa melihatnya.
5. <strong>git pull</strong>: Sebelum mulai bekerja, tarik kode terbaru dari cloud terlebih dahulu, pastikan lokal sinkron dengan anggota tim lainnya.

Untuk pemula, ingat mantra ini:<strong>"Pull dulu sebelum ubah, setelah selesai add, commit dengan pesan, terakhir push"</strong>. Biasakan ini, kolaborasi tim tidak akan berantakan.

#### 6. Workflow Kolaborasi Tim: Bagaimana Pull Request Bekerja

Hal terkuat dari GitHub adalah mekanisme kolaborasinya. Workflow kolaborasi tim yang tipikal adalah seperti ini:

1. <strong>Buka branch</strong>: Buka branch baru dari branch utama (biasanya disebut main atau master), misalnya<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">feature/login</code>, kembangkan fitur baru di branch ini.
2. <strong>Kembangkan dan commit</strong>: Tulis kode di branch baru, commit berkali-kali untuk mencatat progres.
3. <strong>Push ke GitHub</strong>: Push branch ke repository cloud.
4. <strong>Ajukan Pull Request</strong>: Ajukan PR di halaman web GitHub, minta merge branch Anda ke branch utama. Jelaskan dengan jelas apa perubahan yang dibuat PR ini, mengapa diubah.
5. <strong>Code Review</strong>: Anggota tim meninjau kode Anda, memberikan pendapat atau saran perubahan. Anda bisa terus commit berdasarkan feedback, PR akan otomatis update.
6. <strong>Merge</strong>: Setelah review lolos, klik "Merge" untuk merge kode ke branch utama. Kontribusi Anda resmi masuk ke proyek!

Workflow ini memastikan <strong>setiap kode ditinjau sebelum masuk ke branch utama</strong>, sangat mengurangi probabilitas error. Proyek open source juga menggunakan mekanisme ini untuk menerima kontribusi dari orang asing di seluruh dunia—Anda benar-benar bisa mengajukan PR di proyek open source terkenal, setelah diterima Anda menjadi kontributor proyek tersebut.

#### 7. Skenario Aplikasi Tipikal GitHub

##### 🎓 Mahasiswa Mengikuti Kompetisi dan Proyek Mata Kuliah

Mahasiswa ilmu komputer mengikuti ACM, hackathon, tugas akhir, hampir selalu membutuhkan GitHub. Ia bisa menjadi platform kolaborasi tim sekaligus jendela tampilan karya—juri kompetisi bisa langsung melihat repository Anda, memahami kualitas kode dan proses kolaborasi. Banyak perusahaan saat rekrutmen juga meminta melampirkan halaman GitHub, sebagai bukti kemampuan teknis.

##### 📚 Hosting Basis Pengetahuan dan Catatan Pribadi

Non-programmer juga bisa menggunakan GitHub. Banyak orang menggunakannya untuk hosting catatan belajar, blog teknis (dengan GitHub Pages bisa membuat situs gratis), buku elektronik. Penulisan format Markdown + kontrol versi Git + backup cloud, tiga dalam satu.

##### 🌐 Berpartisipasi dalam Proyek Open Source

GitHub adalah pusat gerakan open source global. Anda bisa Fork proyek favorit, modifikasi lalu kirim PR untuk memberi balik ke komunitas; atau sekadar Star koleksi proyek bagus, lacak update. Berpartisipasi dalam open source adalah cara terbaik untuk meningkatkan teknis dan membangun reputasi.

##### 🤖 Deployment Otomatis dan CI/CD

Dengan GitHub Actions, bisa mengimplementasikan workflow otomatis penuh "kode push, otomatis test + otomatis deploy ke server". Banyak blog pribadi, situs dokumentasi dibangun seperti ini, setelah menulis artikel push, situs otomatis update.

##### 💾 Backup Kode dan Sinkronisasi Multi-Perangkat

Gunakan repository kode sebagai cloud drive, saat ganti komputer atau kerja multi-perangkat, git pull sekali bisa mendapatkan kode terbaru, tidak perlu lagi bolak-balik menyalin dengan flash drive.

#### 8. Beberapa Saran untuk Pemula

- <strong>Tulis pesan commit dengan jelas</strong>: Jangan tulis pesan tidak berguna seperti "update". Commit message yang baik: "fix bug halaman redirect salah setelah user login", setengah tahun kemudian meninjau kembali juga tahu apa yang dilakukan saat itu.
- <strong>Rajin commit, langkah kecil cepat</strong>: Commit sekali setiap selesai fitur kecil, bukan commit sekali setelah menulis seharian penuh. Jika ada masalah, lebih mudah dilokalisasi.
- <strong>Kembangkan dengan branch, jangan langsung ubah branch utama</strong>: Bahkan untuk proyek pribadi, biasakan membuka branch, saat kolaborasi tim di masa depan tidak akan panik.
- <strong>Manfaatkan .gitignore</strong>: File ini memberi tahu Git file mana yang tidak perlu dimasukkan dalam kontrol versi (seperti konfigurasi kata sandi, hasil kompilasi, folder dependensi), hindari mengunggah file sampah.
- <strong>Sering-sering lihat proyek open source yang bagus</strong>: Jelajahi GitHub Trending, lihat struktur kode, cara menulis README, workflow kolaborasi proyek berbintang tinggi, adalah cara gratis tercepat untuk meningkatkan diri.
- <strong>Ajukan GitHub Student Pack</strong>: Setelah verifikasi mahasiswa, bisa mendapatkan gratis banyak kuota alat dan layanan berbayar (Copilot, domain, layanan cloud, dll.), nilai ribuan dolar.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Peringatan Keamanan

{class="list-disc pl-6 mt-1 space-y-1"}
- Jangan pernah commit informasi sensitif seperti kata sandi, API key, string koneksi database ke GitHub, terutama repository publik—sekali bocor, akan di-scrape dalam hitungan detik, konsekuensinya serius.
- Jika tidak sengaja commit informasi sensitif, hanya menghapus file tidak cukup (masih ada di riwayat), gunakan<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">git filter-branch</code> atau alat profesional untuk membersihkan riwayat, dan segera ganti key yang bocor.
- Repository private juga tidak absolut aman, informasi sensitif sebaiknya dikelola dengan environment variable, tidak masuk ke repository kode.
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Catatan untuk Mengakses GitHub di Dalam Negeri

{class="mt-1"}
Akses GitHub di dalam negeri kadang tidak stabil, mungkin tidak bisa dibuka atau clone lambat. Bisa coba: ① Gunakan situs mirror domestik (seperti GitClone, ghproxy) untuk mempercepat clone; ② Konfigurasi Hosts atau gunakan proxy; ③ Jika utamanya untuk kolaborasi domestik, juga bisa pertimbangkan alternatif domestik <strong>Gitee</strong>, fungsinya serupa dan aksesnya cepat. Banyak tim hosting di GitHub dan Gitee sekaligus, mengakomodasi internasionalisasi dan kecepatan domestik.
:::

::: div .success-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Tingkat Lanjut: Bangun Blog Pribadi Gratis dengan GitHub Pages

{class="mt-1"}
GitHub Pages memungkinkan Anda hosting situs web statis secara gratis, dipadukan dengan generator situs statis seperti Jekyll, Hexo, Hugo, bisa dengan mudah membangun blog pribadi. Setelah menulis artikel Markdown push ke repository, blog otomatis update, juga dilengkapi HTTPS dan custom domain. Blog tak terhitung jumlahnya dibangun seperti ini, biaya nol, tanpa iklan, versi terkontrol.
:::

#### 9. Kesimpulan: Mengapa Semua Orang Harus Mengenal GitHub

GitHub sudah lama bukan hanya "alat programmer", ia lebih seperti <strong>cara kerja era digital</strong>: kontrol versi membuat segalanya traceable, mekanisme kolaborasi membuat tim beroperasi efisien, semangat open source membuat pengetahuan mengalir bebas. Bahkan jika Anda tidak menulis kode, memahami konsep "commit, branch, merge" juga bisa membantu Anda mengelola konten apa pun yang membutuhkan "modifikasi berulang + kolaborasi multi-orang" dengan lebih baik—dari makalah ke dokumen, dari catatan ke proposal.

Bagi mahasiswa ilmu komputer, GitHub adalah keterampilan wajib: ia adalah portofolio Anda, platform kolaborasi, perpustakaan sumber belajar, juga "resume" yang paling meyakinkan saat mencari pekerjaan di masa depan. Daftarkan akun lebih awal, unggah tugas mata kuliah dan proyek kecil Anda, kumpulkan secara bertahap, beberapa tahun kemudian Anda akan memiliki resume teknis yang membuat interviewer terkesan.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Mari Praktik: Selesaikan Pengalaman Pertama GitHub Anda

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Daftarkan akun GitHub, lengkapi profil pribadi (avatar, bio, bidang teknis yang diminati).
2. Buat repository publik bernama<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">hello-github</code>, centang "Add a README file".
3. Masuk ke repository, klik tombol edit README.md (ikon pensil), tulis perkenalan diri dengan Markdown, commit perubahan.
4. Di kolom pencarian GitHub, cari kata kunci yang Anda minati (misalnya<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">python-tutorial</code>), Star dua proyek yang Anda suka.
5. (Tingkat lanjut) Instal Git di komputer, Clone repository ke lokal, modifikasi README lalu push kembali ke cloud, selesaikan workflow lengkap "lokal → cloud".
:::
