---
id: di-yi-zhang-memory
part: ji-chu-pian
nav:  Tambahan: Analisis Pengembangan Ingatan Telefon Android
toc: sub
kind: supplement
---

### Tambahan: Analisis Pengembangan Ingatan Telefon Android

{class="chapter-intro mb-4"}
Apabila membeli telefon, anda sering nampak pengiklanan seperti "12GB+8GB RAM" — seolah-olah secara ajaib mendapat 8GB RAM tambahan. Tetapi adakah ia benar-benar membolehkan telefon lebih pantas? Adakah ia sebaliknya merosakkan telefon? Bahagian ini akan menjelaskan sepenuhnya teknologi "pengembangan ingatan" ini.

#### I. Definisi Asas

"Pengembangan ingatan" telefon Android (juga dikenali sebagai pengembangan ingatan, gabungan ingatan, RAM Plus dan lain-lain)<strong>bukan benar-benar menambah cip RAM fizikal</strong>, tetapi teknologi perisian tahap sistem: melalui pengasingan dinamik sebahagian ruang storan dalaman telefon (ROM/UFS flash) untuk mensimulasikan sebagai RAM maya untuk digunakan.

Sebagai metafora: RAM fizikal ialah "meja kerja kelajuan tinggi", ingatan yang diperluas ialah "bilik simpanan sementara". Apabila meja kerja tidak mencukupi, sistem akan memindahkan data yang tidak digunakan buat sementara ke bilik simpanan, dan memindahkan kembali apabila diperlukan. Bilik simpanan besar, tetapi pemindahan bolak-balik pasti lebih perlahan daripada terus diletakkan di meja kerja.

#### II. Prinsip Teknologi

Kaedah pelaksanaan pengeluar arus perdana utama ada dua:

##### 1. Pemampatan zRAM

Membahagikan ruang data mampatan dalam RAM, menyimpan kod aplikasi tidak aktif secara mampatan, nisbah mampatan kira-kira 2:1. Data masih dalam RAM, kelajuan cepat, tidak merosakkan flash, tetapi memerlukan CPU terlibat dalam mampatan dan penyahmampatan.

##### 2. Partisi swap

Terus membahagikan ruang tetap dalam flash UFS sebagai ingatan maya, menulis data proses latar belakang ke storan. Bergantung kepada lebar jalur storan, kelajuan baca-tulis jauh lebih rendah daripada ingatan fizikal.

"12GB+8GB RAM" yang diiklankan pengeluar biasanya gabungan 12GB RAM fizikal + 8GB ingatan maya flash. Perlu diperhatikan, zRAM secara lalai tidak mengambil storan badan, hanya apabila zRAM sepenuhnya dipenuhi data, sistem akan membuat fail pertukaran pada storan, dan keadaan ini sangat jarang berlaku.

#### III. Jurang Kelajuan adalah Halangan Utama

Had asas teknologi ini terletak pada perbezaan kelajuan. Flash UFS 4.0 arus perdana kini mempunyai kelajuan baca berurutan kira-kira 4200MB/s, hanya 1/10–1/15 daripada ingatan fizikal LPDDR5X. Oleh itu, dalam tahap mampatan zRAM beban ringan kelajuan hampir RAM sebenar, tetapi sebaik sahaja memasuki senario beban tinggi, kelajuan akan jatuh kepada beberapa persepuluh.

#### IV. Senario Sesuai dan Sempadan Manfaat

Pengembangan ingatan bukan penawar, kesannya berbeza mengikut model dan senario penggunaan:

- <strong>Berguna</strong>: Model dengan 6GB RAM fizikal + UFS 3.1 ke atas, ruang tinggal ≥30GB, selepas mengaktifkan pengembangan 3GB, bilangan latar belakang aktif boleh lebih 3-4, kadar muat semula berkurang 68%, sesuai untuk pengguna pelbagai tugas berat seperti penghantar makanan, pemandu teksi.
- <strong>Senario harian</strong>: Peningkatan ketara untuk WeChat berbilang, tab pelayar aktif, respons mesej pemesejan segera, masa permulaan sejuk aplikasi latar belakang berkurang dengan jelas.
- <strong>Senario terhad</strong>: Peningkatan terhad untuk senario lebar jalur tinggi seperti muat turun permainan besar, penyuntingan video 4K.
- <strong>Memudaratkan</strong>: Model dengan 8GB RAM + UFS 2.2 dan ruang tinggal tidak mencukupi, selepas mengaktifkan, turun naik kadar bingkai permainan sebaliknya membesar, menonton video pendek lebih banyak menggunakan kuasa, pertukaran tersekat.
- <strong>Tidak berkesan</strong>: Model RAM besar 16GB ke atas manfaat hampir sifar, paling banyak lebih aktif 1 App, tetapi akan meningkatkan beban CPU 12%, haba naik 2-3°C. Untuk model RAM lebih besar daripada 12GB, cadangan terus tutup untuk mengelakkan pengiraan mampatan yang tidak bermakna.

#### V. Penamaan dan Cara Mengaktifkan Setiap Pengeluar

Setiap jenama panggilan berbeza: Xiaomi panggil "Pengembangan Ingatan", Huawei panggil "Gabungan Ingatan", Samsung panggil "RAM Plus", vivo namakan "Extended RAM", OnePlus panggil "Memory Extension". Fungsi ini adalah keupayaan natif sistem, tiada hubungan langsung dengan versi asas Android.

Laluan pengaktifan umum: Masuk [Tetapan] → [Lagi Tetapan] → Cari subitem [Ingatan] atau [Prestasi] → Aktifkan "Pengembangan Ingatan" dan pilih tahap kapasiti (biasanya 2GB–7GB), berkuat kuasa selepas mulakan semula. Selepas mengaktifkan, sistem akan memaparkan gabungan ingatan seperti "8GB+4GB".

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Fungsi kunci BL:

{class="list-disc pl-6 mt-1 space-y-1"}
- Pengembangan ingatan akan mengambil sebahagian ruang storan badan, pastikan storan tinggal tidak kurang daripada 20-30GB, jika tidak mungkin menjejaskan kelancaran sistem.
- Flash sebagai ingatan maya akan ada kehausan baca-tulis, walaupun hayat flash UFS moden agak panjang, tetapi swap frekuensi tinggi jangka panjang masih boleh mempercepat penuaan storan.
- Jika telefon itu sendiri RAM fizikal kecil (seperti 4GB dan ke bawah), mengaktifkan pengembangan ingatan hanya boleh meringankan kecemasan sementara, tidak dapat menyelesaikan masalah tersekat secara asas.
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Rumusan

{class="mt-1"}
Pengembangan ingatan adalah teknologi pengoptimuman tahap sistem yang matang, boleh meningkatkan keupayaan pelbagai tugas dan kadar latar belakang aktif model pertengahan hingga bawah tanpa mengubah perkakasan, tetapi terhad oleh jurang kelajuan besar antara flash dan ingatan fizikal, bukan "ubat penawar universal". Sama ada mengaktifkan, berapa besar, perlu mengambil kira saiz RAM fizikal model, spesifikasi flash, ruang storan tinggal dan tabiat penggunaan.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Mari Berlatih: Lihat Adakah Telefon Anda Ada Pengembangan Ingatan

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Buka [Tetapan], cari "Pengembangan Ingatan", "Gabungan Ingatan", "RAM Plus" atau "Extended RAM".
2. Selepas jumpa, lihat sama ada diaktifkan sekarang, dan berapa tetapan kapasiti pengembangan.
3. Bandingkan dengan kandungan bahagian ini untuk menilai: Berapa RAM fizikal model anda? Apa spesifikasi flash? Adakah ruang storan tinggal mencukupi?
4. Cuba tutup atau kurangkan kapasiti pengembangan, perhatikan perubahan latar belakang aktif dan haba selama seminggu, cari tetapan yang paling sesuai untuk diri sendiri.
:::
