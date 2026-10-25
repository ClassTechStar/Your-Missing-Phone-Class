---
id: di-si-shi-san-zhang
num: 43
part: ai-biancheng-pian
nav: Bab 43: Conversation Engineering—Teknik Percakapan Efisien
toc: default
kind: chapter
---

### Bab 43: Rekayasa Percakapan — Teknik Berdialog untuk Kolaborasi Efisien dengan AI

{class="chapter-intro mb-4"}
Percakapan adalah cara interaksi inti dalam pemrograman AI. Tapi perlu diingat: "berdialog" tidak sama dengan "ngobrol santai"—percakapan pemrograman AI yang efisien adalah teknik komunikasi yang terstruktur, yang kita sebut "rekayasa percakapan". Objek kajiannya: bagaimana mendapatkan hasil kode berkualitas tertinggi dengan jumlah putaran percakapan paling sedikit. Singkatnya, bab ini mengajarkan cara "menyampaikan maksud dengan jelas" kepada AI.

#### 1. Strategi Prompt berlapis

Percakapan dengan AI dapat dibagi menjadi tiga lapisan, masing-masing menjalankan fungsi berbeda. Memahami ketiga lapisan ini membuatmu bisa merangkai Prompt yang efisien seperti menyusun balok susun.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Lapisan</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Fungsi</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Contoh</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Frekuensi</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lapisan sistem</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menetapkan peran AI dan batasan global</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"Kamu adalah ahli React, kode wajib memakai TypeScript"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Diatur sekali di awal proyek</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lapisan tugas</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menjelaskan tugas spesifik yang sedang dikerjakan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"Buat satu komponen form yang berisi kolom nama pengguna dan kata sandi"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Diberikan di awal setiap tugas</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lapisan umpan balik</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menilai dan mengoreksi hasil kerja AI</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"Kolom kata sandi belum punya tombol tampil/sembunyikan, tolong ditambahkan"</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Diberikan sesuai kualitas hasil kerja</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Tiga lapisan Prompt dalam percakapan

Prompt lapisan sistem biasanya ditulis di berkas memori proyek (misalnya CLAUDE.md) dan tidak perlu diulang di setiap percakapan. Lapisan tugas adalah yang paling sering kamu pakai dalam percakapan—ia harus memuat tiga unsur: "apa yang dikerjakan", "teknologi apa yang dipakai", dan "apa batasannya". Lapisan umpan balik adalah yang paling menguji kemampuan—umpan balik yang baik membuat AI mengoreksi dengan tepat, umpan balik yang buruk hanya membuatnya menebak lagi.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tips: Tiga jurus andalan umpan balik

{class="mt-1"}
Satu templat umpan balik yang praktis adalah "tunjukkan masalah + jelaskan harapan + beri konteks". Contoh: "Penanganan error di baris 25 hanya memakai console.log (tunjukkan masalah), untuk lingkungan produksi seharusnya memakai error handler terpadu dan mengembalikan pesan yang ramah pengguna (jelaskan harapan), di proyek ini sudah ada fungsi handleError yang bisa dipakai (beri konteks)". Umpan balik seperti ini sepuluh kali lebih efektif daripada sekadar "perbaiki penanganan errornya".
:::

#### 2. Percakapan debugging: cara mendeskripsikan error agar AI cepat menemukan sumbernya

Debugging adalah salah satu skenario paling sering dalam pemrograman AI. Saat kamu menemui bug, cara mendeskripsikan masalah kepada AI langsung menentukan apakah ia bisa cepat menemukan dan memperbaikinya. Berikut empat poin penting dalam percakapan debugging:

1. Beri AI informasi mentah untuk "dilihat", bukan parafrasamu. Salin log error, stack trace, dan kode terkait langsung ke AI lewat @, jangan mendeskripsikannya dengan "kayak ada error gitu deh". AI yang melihat informasi mentah jauh lebih akurat daripada yang hanya mendengar tafsirmu.
2. Jelaskan perbedaan antara "perilaku yang diharapkan" dan "perilaku aktual". "Seharusnya setelah tombol diklik halaman berpindah ke beranda (harapan), tapi nyatanya setelah diklik tidak ada reaksi sama sekali (aktual)"—deskripsi seperti ini jauh lebih berguna daripada "tombolnya rusak".
3. Sertakan langkah reproduksi. "Pertama isi nama pengguna, lalu klik tombol login, errornya muncul"—langkah reproduksi memungkinkan AI meniru alur operasimu sehingga lebih mudah menemukan masalahnya.
4. Sebutkan dengan jelas apa yang sudah kamu coba. "Saya sudah memeriksa permintaan jaringan, statusnya 200, datanya normal"—ini membantu AI mengeliminasi arah yang sudah terverifikasi, sehingga tidak membuang waktu menyelidik ulang.

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
Deskripsi debugging yang buruk

{class="font-mono text-xs leading-relaxed"}
Tombol tidak merespons saat diklik, tolong cek
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
Deskripsi debugging yang baik

{class="font-mono text-xs leading-relaxed"}
Halaman tidak bereaksi setelah tombol login diklik. Perilaku yang diharapkan: berpindah ke halaman /home setelah diklik Perilaku aktual: tidak ada reaksi apa pun setelah diklik, konsol tidak menampilkan error Langkah reproduksi: 1. Di halaman login, isi nama pengguna admin dan kata sandi 123456 2. Klik tombol "Login" 3. Halaman tidak bereaksi Sudah diperiksa: - Permintaan jaringan normal, status 200 - Event onClick sudah terikat - Sudah memeriksa kode komponen LoginButton Berkas terkait: @src/components/LoginButton.tsx @src/pages/Login.tsx
:::
:::

#### 3. Strategi iterasi: langkah kecil cepat vs restrukturisasi besar

Ada dua strategi dasar iterasi dalam pemrograman AI, masing-masing cocok untuk skenario berbeda. Memahami perbedaannya membantumu membuat pilihan yang tepat di berbagai situasi.

Strategi "langkah kecil cepat" cocok untuk pengembangan fitur dan perbaikan bug. Intinya: setiap kali hanya minta AI melakukan satu perubahan kecil, verifikasi sampai lolos, baru lanjut ke perubahan berikutnya. Kelebihannya, setiap langkah bisa diverifikasi dan bisa dikembalikan sehingga risikonya terkendali; kekurangannya, lebih lambat dan butuh interaksi percakapan yang sering. Cocok untuk: pengembangan fitur baru, eksplorasi saat solusi terbaik belum pasti, dan iterasi hati-hati saat kamu belum terlalu yakin dengan hasil AI.

Strategi "restrukturisasi besar" cocok untuk perubahan skala besar dengan tujuan yang sudah jelas. Intinya: jelaskan tujuan lengkapnya sekali jalan, lalu biarkan AI merencanakan dan mengeksekusi seluruh perubahan secara mandiri. Kelebihannya, lebih cepat dan AI dapat melihat gambaran menyeluruh untuk mengambil keputusan arsitektur yang lebih baik; kekurangannya, risikonya tinggi—jika pemahaman AI menyimpang, biaya koreksinya besar. Cocok untuk: peningkatan arsitektur yang jelas, migrasi kode skala besar, dan restrukturisasi yang dilindungi pengujian memadai.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Aspek</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Langkah kecil cepat</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Restrukturisasi besar</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ukuran tiap perubahan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Satu titik fitur atau satu bug</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Satu modul atau satu lapisan arsitektur</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Frekuensi verifikasi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Verifikasi langsung setelah tiap perubahan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Verifikasi sekaligus setelah semua perubahan selesai</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Putaran percakapan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Banyak (5-10 putaran per fitur)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sedikit (1-3 putaran per modul)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Risiko</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Rendah, tiap langkah bisa dikembalikan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tinggi, biaya koreksi penyimpangan besar</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Skenario yang cocok</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Fitur baru, pengembangan eksploratif</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Restrukturisasi atau migrasi dengan tujuan jelas</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Prasyarat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tanpa syarat khusus</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Perlu cakupan pengujian</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Perbandingan dua strategi iterasi

Dalam praktik, kedua strategi ini sering dipadukan. Misalnya saat merestrukturisasi satu modul: pakai dulu "restrukturisasi besar" agar AI menyusun rencana menyeluruh, setelah rencananya ditinjau, lanjutkan dengan "langkah kecil cepat" untuk mengeksekusinya bertahap. Dengan begitu, perspektif global tetap terjaga sekaligus risiko eksekusi terkendali.

#### 4. Manajemen konteks dalam percakapan multi-putaran

Seiring bertambahnya putaran percakapan, kamu perlu mengelola konteks percakapan secara aktif untuk menghindari masalah "AI lupa informasi awal". Berikut beberapa teknik manajemen konteks yang praktis.

Pertama, "jangkarkan" informasi kunci. Di awal percakapan, tuliskan batasan-batasan penting dengan jelas, dan ulangi kembali pada saat yang tepat di percakapan berikutnya. Misalnya "ingat, data kita disimpan di localStorage, tidak boleh pakai database"—tegaskan kembali batasan ini pada permintaan perubahan yang relevan agar AI tidak lupa.

Kedua, manfaatkan teknik "ringkas-lanjut". Ketika percakapan jadi sangat panjang, minta AI "merangkum kemajuan dan daftar tugas sejauh ini", lalu buka percakapan baru dengan ringkasan itu sebagai titik awal. Dengan begitu konteks kunci tetap tersimpan dan penurunan kualitas percakapan panjang bisa dihindari.

Ketiga, "satu percakapan, satu tugas". Ini strategi manajemen konteks yang paling sederhana sekaligus paling efektif. Setiap percakapan hanya menangani satu tugas atau satu titik fitur; setelah selesai, buka percakapan baru untuk tugas berikutnya. Ini secara alami membatasi panjang percakapan dan menjaga konteks tetap jernih.

Keempat, gunakan fitur manajemen konteks pada alat yang dipakai. Sebagian besar alat pemrograman AI punya tombol "bersihkan konteks" atau "sesi baru"—saat kamu merasa kualitas jawaban AI menurun, jangan ragu, buka sesi baru. Kehilangan sebagian riwayat percakapan jauh lebih baik daripada terus berjuang dalam konteks yang sudah menurun.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mari praktik: berperan sebagai "pasien" untuk AI-mu

{class="mt-1"}
Dengan sengaja buat satu halaman kecil di browser dan ciptakan satu bug (misalnya tombol tidak berfungsi). Lalu, mengikuti format "deskripsi debugging yang baik" di bab ini, jelaskan masalahnya secara lengkap kepada AI: informasi mentah, harapan vs aktual, langkah reproduksi, dan hal-hal yang sudah diperiksa. Rasakan perbedaan kecepatan AI menemukan masalah—kamu akan paham mengapa "mendeskripsikan masalah" sendiri adalah sebuah keterampilan.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan bab ini

- Tiga lapis Prompt: lapisan sistem (ditulis di berkas memori), lapisan tugas (apa yang dikerjakan + teknologi + batasan), lapisan umpan balik (tunjukkan masalah + harapan + konteks)
- Empat poin debugging: beri informasi mentah, harapan vs aktual, langkah reproduksi, hal yang sudah diperiksa
- Langkah kecil cepat: risiko rendah, putaran banyak, cocok untuk fitur baru; restrukturisasi besar: risiko tinggi, putaran sedikit, butuh dukungan pengujian
- Empat trik manajemen konteks: jangkarkan informasi kunci, ringkas-lanjut, satu percakapan satu tugas, berani buka sesi baru
:::
