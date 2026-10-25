---
id: di-si-shi-liu-zhang
num: 46
part: ai-biancheng-pian
nav: Bab 46: Jalan Menuju Tingkat Lanjut—Dari Pengguna ke Arsitek
toc: default
kind: chapter
---

### Bab 46: Jalan Menuju Level Lanjut — Dari Pengguna Menjadi Arsitek

{class="chapter-intro mb-4"}
Setelah kamu menguasai metodologi Bab 37 sampai Bab 44 dan mampu menyelesaikan pengembangan proyek dengan AI dengan lancar, apa langkah berikutnya? Bab ini membahas jalan naik level dari "pengguna alat AI" menjadi "arsitek sistem berbasis AI". Fokus pada tahap ini bukan lagi "bagaimana membuat AI menulis kode dengan baik", melainkan "bagaimana memadukan AI lebih baik ke dalam keseluruhan alur pengembangan".

#### 1. Protokol MCP dan perluasan alat

MCP (Model Context Protocol) adalah protokol terbuka yang muncul pada 2025 dan mulai meluas pada 2026; ia menetapkan standar komunikasi antara model AI dan alat eksternal. Sederhananya, MCP membuat AI bisa "memakai alat"—bukan hanya menghasilkan kode, tetapi juga mengeksekusi perintah, mengkueri database, memanggil API, dan mengoperasikan sistem berkas.

Sebelum MCP, setiap alat AI punya cara integrasi alatnya sendiri yang tidak saling kompatibel. Kemunculan MCP berarti: satu alat yang memenuhi standar MCP bisa dipakai oleh alat AI mana pun yang mendukung MCP. Ini sangat menekan biaya integrasi alat dan memperluas batas kemampuan AI dari "menghasilkan teks" menjadi "mengeksekusi aksi".

Bagi pengguna tingkat lanjut, makna MCP adalah: kamu bisa membangun kemampuan alat yang disesuaikan untuk AI. Misalnya, jika timmu punya satu sistem deployment internal, kamu bisa menulis satu alat MCP agar AI langsung memanggil sistem deployment itu tanpa perlu berpindah manual ke terminal. Kemampuan "AI memanggil alat" seperti ini adalah infrastruktur dari Agentic Engineering.

#### 2. Alur kerja kustom dan Skills

Ketika kamu menjalankan alur pemrograman AI yang sama berulang-ulang, padukan menjadi "alur kerja kustom" atau "Skills". Misalnya, timmu mungkin punya alur tinjauan kode baku—periksa keamanan dulu, lalu kinerja, lalu kemudahan perawatan. Kamu bisa menulis alur itu menjadi satu Skill agar AI menjalankannya secara otomatis setiap kali meninjau kode.

Nilai inti alur kerja kustom adalah "konsistensi"—ia memastikan setiap eksekusi mengikuti standar yang sama, tidak menyimpang karena panjang pendeknya percakapan atau perbedaan konteks. Ini sangat penting untuk kolaborasi tim: jika semua anggota memakai alur kerja yang sama, gaya kode dan standar kualitas hasil kerja mereka akan cenderung seragam.

Cara membangun alur kerja kustom berbeda-beda antar alat. Cursor mendukung Rules dan Custom Instructions, Claude Code mendukung perintah kustom, Replit mendukung Runme. Tetapi gagasan intinya sama: "mengodekan" praktik terbaikmu menjadi templat instruksi yang bisa dieksekusi AI.

#### 3. Pola kolaborasi multi-Agent

Menjelang 2026, kolaborasi multi-Agent mulai menjadi topik yang hangat dibicarakan. Gagasan intinya: jangan hanya memakai satu AI untuk menyelesaikan tugas, melainkan gunakan beberapa AI dengan pembagian tugas berbeda untuk bekerja sama. Misalnya, satu AI menulis kode, satu AI menulis pengujian, satu AI meninjau kode—masing-masing menjalankan tugasnya dan saling memeriksa.

Keunggulan kolaborasi multi-Agent terletak pada "pembagian tugas" dan "verifikasi silang": setiap Agent fokus pada bidangnya sehingga kualitas hasilnya lebih tinggi; pemeriksaan silang antar-Agent bisa menemukan masalah yang mungkin terlewat bila dikerjakan sendirian. Tetapi kekurangannya juga jelas: biaya koordinasi tinggi, beban komunikasi besar, dan debugging lebih rumit.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tips: "multi-Agent" juga bisa dimainkan sendirian

{class="mt-1"}
Bagi pengembang perorangan, kamu tidak perlu membangun sistem multi-Agent yang rumit—kamu bisa "memerankan" berbagai peran untuk mensimulasikan kolaborasi multi-Agent. Misalnya: gunakan satu percakapan dulu agar AI menulis kode fungsinya; lalu buka percakapan baru (dengan konteks CLAUDE.md) dan minta AI "meninjau kode ini selaku peninjau kode"; terakhir buka satu percakapan lagi dan minta AI "memperbaiki kode sesuai catatan tinjauan". Cara "satu orang banyak peran" ini memberikan sebagian besar manfaat kolaborasi multi-Agent tanpa perlu infrastruktur rumit.
:::

#### 4. Jalur belajar berkelanjutan

Pemrograman AI adalah bidang yang berubah sangat cepat. Praktik terbaik hari ini bisa saja perlu diperbarui besok. Berikut beberapa saran untuk belajar terus-menerus:

Pertama, ikuti sumber aslinya, bukan tafsiran orang kedua. Tweet asli Andrej Karpathy dan CLAUDE.md, dokumentasi resmi Anthropic dan OpenAI, catatan pembaruan berbagai alat—semua ini adalah informasi tingkat pertama. Artikel dan tutorial komunitas adalah tafsiran dan ringkasan atas informasi itu; bermanfaat tetapi bisa terdistorsi. Biasakan membaca sumber aslinya.

Kedua, belajar dipacu praktik. Jangan "selesai belajar baru mengerjakan", melainkan "belajar sambil mengerjakan". Setiap kali menemui tipe masalah baru (misalnya pertama kali menangani unggah berkas, pertama kali terhubung ke API pihak ketiga), jadikan itu kesempatan mempelajari pengetahuan terkait. Efisiensi belajar dalam praktik jauh melampaui teori yang dipelajari lepas dari konteks.

Ketiga, jaga kepekaan terhadap alat tanpa berlebihan mengejar yang baru. Setiap satu-dua bulan, sisihkan setengah hari untuk mengetahui alat dan tren terbaru—tetapi jangan berpindah alat setiap kali ada yang baru. Patokannya: apakah alat baru itu mampu menembus hambatanmu yang signifikan? Kalau tidak, kombinasi sekarang sudah cukup.

Keempat, bangun basis pengetahuan pribadi. Catat setiap percakapan yang berhasil memecahkan masalah rumit, setiap pelajaran dari kesalahan, dan setiap metode yang terbukti efektif. Tidak perlu dipublikasikan—ini "catatan metodologi" milikmu sendiri. Seiring waktu, ia akan menjadi aset paling berhargamu.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mari praktik: mulai "buku catatan jebakan"

{class="mt-1"}
Buat satu dokumen hari ini (perangkat lunak catatan atau berkas .md sama saja), tuliskan tiga pelajaran pemrograman AI yang paling ingin kamu ingat sampai hari ini—sekecil apa pun, misalnya "ingat berpikir dulu sebelum bertanya". Ke depan, setiap kali terpeleset atau menemukan trik baru, tambahkan satu catatan. Setengah tahun kemudian saat membacanya kembali, kamu akan berterima kasih kepada dirimu hari ini.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan bab ini

- MCP adalah standar komunikasi antara AI dan alat: membuat AI bisa mengeksekusi perintah, mengkueri database, memanggil API
- Nilai inti alur kerja kustom/Skills adalah "konsistensi": mengodekan praktik terbaik menjadi templat instruksi
- Multi-Agent = pembagian tugas + verifikasi silang; pengembang perorangan bisa mensimulasikannya dengan "satu orang banyak peran"
- Empat trik belajar berkelanjutan: baca sumber asli, belajar sambil praktik, tidak berlebihan mengejar yang baru, bangun basis pengetahuan pribadi
:::
