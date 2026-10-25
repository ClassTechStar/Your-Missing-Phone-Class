---
id: di-si-shi-wu-zhang
num: 45
part: ai-biancheng-pian
nav: Bab 45: Jaminan Kualiti—Memastikan Kod AI Boleh Dipercayai
toc: default
kind: chapter
---

### Bab 45: Jaminan Kualiti — Menjadikan Kod AI Boleh Dipercayai

{class="chapter-intro mb-4"}
Kod yang ditulis AI mempunyai satu ciri: ia biasanya "nampak betul" — pemboleh ubah dinamakan mengikut piawaian, komen lengkap dan logik jelas. Tetapi "nampak betul" tidak sama dengan "memang betul". Masalah tersembunyi dalam kod AI sering lebih sukar ditemui berbanding kod tulisan manusia, kerana kualiti permukaannya terlalu tinggi sehingga mudah membuat orang lengai. Bab ini mengajar anda cara membina sistem jaminan kualiti yang berkesan untuk kod AI — dengan tiga benteng iaitu ujian, semakan dan kawalan versi — untuk mengubah "nampak betul" menjadi "memang betul".

#### 1. Dipandu ujian: minta AI menulis ujian

Ujian ialah benteng pertama jaminan kualiti pengaturcaraan AI. Berita baiknya: meminta AI menulis ujian lebih mudah dan lebih boleh dipercayai daripada memintanya menulis kod fungsi — kerana tingkah laku dijangka ujian adalah jelas, dan kurang menghasilkan kod yang "nampak betul tetapi sebenarnya tidak".

Aliran kerja pengaturcaraan AI yang dipandu ujian ialah: biarkan AI menulis kod fungsi dahulu; selepas pengesahan fungsi asas lulus, terus minta ia menulis kes ujian. Kes ujian patut meliputi laluan normal, situasi sempadan dan situasi luar biasa. Kemudian minta AI membetulkan kod fungsi berdasarkan maklum balas ujian. Kelebihan aliran ini: sebaik sahaja ujian ditulis, ia menjadi alat pengesahan berterusan — sebarang ubah suai seterusnya boleh disahkan dengan menjalankan ujian untuk memastikan tiada masalah regresi diperkenalkan.

::: div .code-block
:::inline div .code-head
<span>Arahan untuk AI: menulis ujian</span><span class="dots">···</span>
:::

```
Tulis ujian unit untuk fungsi calculate_discount.
Kes ujian sepatutnya meliputi:
1. Laluan normal:
   - barang 100 yuan diskaun 20% -> 80
   - barang 200 yuan diskaun 50% -> 100
2. Kes sempadan:
   - barang 0 yuan diskaun 20% -> 0
   - barang 100 yuan tiada diskaun -> 100 (tidak didiskaun)
   - barang 100 yuan diskaun 0% -> 100 (harga penuh)
3. Kes luar biasa:
   - harga negatif -> perlu lontar ralat
   - kadar diskaun > 1 -> perlu lontar ralat
   - input bukan nombor -> Perlu melontar ralat
Guna rangka kerja Vitest, berikan fail ujian yang lengkap.
```
:::

Perhatikan ciri arahan ini: ia menyenaraikan tiga kategori kes ujian (normal, sempadan, luar biasa) dengan jelas, tanpa memberikan AI ruang bebas untuk "menguji secara pilihan". Kadangkala AI hanya menulis ujian laluan normal untuk "cepat siap"; menyenaraikan semua kategori dengan jelas dapat mengelakkan masalah ini.

#### 2. Teknik semakan kod

Walaupun ada liputan ujian, anda tetap perlu membuat semakan manusia ke atas kod yang dihasilkan AI. Semakan kod bukan membaca baris demi baris — itu terlalu memakan masa dan terlalu bergantung pada tahap pengaturcaraan anda. Semakan kod AI yang berkesan patut memberi perhatian kepada beberapa dimensi penting berikut:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Dimensi semakan</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Apa yang diberi perhatian</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Masalah biasa</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Keselamatan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pengesahan input, pengendalian kunci, perlindungan suntikan SQL</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AI kerap lupa mengesahkan input; kunci dikodkan terus dalam kod</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pengendalian ralat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Adakah pengecualian ditangkap; adakah mesej ralat munasabah</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AI gemar menggunakan blok catch kosong atau sekadar console.log</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Prestasi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Adakah ada masalah prestasi yang ketara, seperti pertanyaan N+1 atau gelung tanpa henti</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kadangkala AI menulis algoritma O(n²)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kebolehselenggaraan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Adakah struktur kod jelas; adakah penamaan bermakna</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sekali-sekala AI menjana kod yang terlalu abstrak</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pengurusan kebergantungan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Adakah kebergantungan yang diperkenalkan perlu; adakah versi jelas</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AI cenderung memperkenalkan pustaka yang tidak perlu</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Dimensi penting semakan kod AI

Semasa menyemak, anda tidak perlu memeriksa satu persatu sendiri — boleh minta AI membantu membuat semakan pusingan pertama. Arahan seperti: "Sila semak keselamatan, pengendalian ralat dan prestasi kod ini, dan nyatakan masalah yang berpotensi." Keupayaan AI menyemak diri sendiri sentiasa meningkat; walaupun tidak dapat menggantikan semakan manusia sepenuhnya, ia boleh membantu anda menapis sebahagian besar masalah yang ketara.

#### 3. Kawalan versi: peranan Git dalam pengaturcaraan AI

Peranan Git dalam pengaturcaraan AI lebih penting daripada dalam pengaturcaraan tradisional. Kerana setiap ubah suai AI boleh memperkenalkan perubahan yang tidak dapat diduga, anda memerlukan "ubat penyesalan" yang boleh dipercayai — kawalan versi itulah ubat penyesalannya.

Amalan terbaik Git dalam pengaturcaraan AI ialah "commit kerap, maju dengan langkah kecil". Setiap kali satu fungsi yang boleh disahkan siap, buat satu commit. Dengan itu, apabila sesuatu ubah suai AI bermasalah, anda boleh kembali dengan tepat ke keadaan sebelumnya yang masih boleh digunakan, tanpa perlu meruntuhkan semua kerja.

Satu lagi teknik praktikal ialah "pengasingan cawangan". Bagi ubah suai AI yang hasilnya tidak pasti (contohnya refaktor besar-besaran), ciptakan satu cawangan baharu dahulu untuk melakukannya. Jika hasilnya memuaskan, gabungkan semula ke cawangan utama; jika tidak, padamkan terus cawangan itu tanpa menjejaskan cawangan utama. Ini jauh lebih selamat daripada mengubah suai berulang kali pada cawangan utama.

1. Sebelum setiap ubah suai AI, pastikan ruang kerja bersih (tiada perubahan yang belum di-commit). Dengan itu, jika hasil ubah suai AI tidak memuaskan, anda boleh gunakan git checkout . untuk kembali dengan cepat.
2. Selepas setiap ubah suai AI dan selepas pengesahan lulus, commit serta-merta. Mesej commit menerangkan apa yang dilakukan oleh ubah suai kali ini, contohnya "feat: tambah fungsi pendaftaran pengguna".
3. Bagi refaktor besar-besaran, ciptakan cawangan dahulu: git checkout -b refactor/auth-system. Siapkan ubah suai pada cawangan itu, dan gabungkan hanya selepas ujian lulus.
4. Amalkan tabiat melihat diff. Selepas setiap ubah suai AI, gunakan git diff untuk melihat secara spesifik apa yang diubah. Ini bukan sahaja membantu anda menemui masalah, malah membantu anda mempelajari kod.

#### 4. Perangkap biasa dan panduan mengelaknya

Terdapat beberapa perangkap yang berulang kali muncul dalam pengaturcaraan AI, dan hampir semua pemula akan terpijak padanya. Mengetahuinya lebih awal membantu anda mengelak banyak jalan berbelit.

##### 1. Perangkap pertama: perangkap kepercayaan

"Kod yang ditulis AI nampak sangat profesional, tentu tiada masalah kan?" — inilah perangkap paling berbahaya. Kod yang dijana AI kelihatan sangat kemas di permukaan — penamaan berpiawaian, komen lengkap, struktur jelas — "kesan profesional permukaan" inilah yang membuat orang lengai. Tetapi kekemasan permukaan tidak bermakna logiknya betul. Penawarnya: sentiasa sahkan melalui ujian, bukan menilai melalui "nampak betul atau tidak".

##### 2. Perangkap kedua: perangkap pembengkakan

"Memandangkan AI boleh menolong saya menulis kod, kenapa tidak buat fungsinya lebih menyeluruh?" — ini akan menyebabkan pembengkakan kod. AI sangat pandai "memberi lebih": anda minta ia membuat satu halaman log masuk, ia akan memberi anda satu sistem pengurusan pengguna yang lengkap. Fungsi berlebihan bukan sahaja menambah kerumitan, malah menambah kebarangkalian muncul bug. Penawarnya: patuhi prinsip Simplicity First dengan ketat, dan beritahu AI dengan jelas "buat fungsi ini sahaja, jangan tambah yang lain".

##### 3. Perangkap ketiga: perangkap kefahaman

"AI patutnya memahami maksud saya kan?" — tidak semestinya. Walaupun keupayaan pemahaman AI sangat kuat, ia tetap akan "meneka" untuk keperluan yang kabur. Apabila tekaannya salah, kod yang dihasilkan juga salah. Lebih menyusulkan, kod tekaannya yang salah biasanya "nampak sangat munasabah", membuatkan anda tersilap menganggap ia memahami. Penawarnya: berikan butiran khusus yang cukup dalam arahan, untuk mengurangkan ruang AI "meneka".

##### 4. Perangkap keempat: perangkap konteks

"Saya sudah katakan dalam perbualan sebelum ini, AI patutnya masih ingat kan?" — sangat mungkin ia tidak ingat. Seiring perbualan bertambah panjang atau sesi baharu dibuka, AI akan kehilangan konteks awal. Jika sesuatu kekangan penting tidak ditulis ke dalam fail memori projek, besar kemungkinan ia diabaikan dalam ubah suai seterusnya. Penawarnya: tuliskan kekangan penting ke dalam fail memori projek, jangan bergantung pada ingatan perbualan.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Ingatan pantas empat perangkap utama

{class="mt-1"}
Perangkap kepercayaan — jangan percaya "nampak betul"; perangkap pembengkakan — AI suka "memberi lebih"; perangkap kefahaman — ia akan "meneka" keperluan yang kabur; perangkap konteks — ingatan perbualan akan "terlupa". Penawar masing-masing: sahkan melalui ujian, buang yang berlebihan, beri butiran secukupnya, tulis ke dalam fail memori.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mari praktik: bina tiga benteng untuk projek anda

{class="mt-1"}
Jika anda sudah mula membuat projek satu (laman alat): (1) minta AI menulis 3 kategori kes ujian bagi fungsi teras; (2) semak kod mengikut lima dimensi (keselamatan/pengendalian ralat/prestasi/kebolehselenggaraan/kebergantungan); (3) mulakan projek dengan git dan buat commit pertama. Setelah tiga benteng lengkap, barulah projek anda benar-benar menjadi milik anda.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan bab ini

- Kod AI "nampak betul" ≠ "memang betul" — kualiti permukaan yang terlalu tinggi malah membuat orang lengai
- Minta AI menulis ujian: senaraikan dengan jelas tiga kategori kes (normal/sempadan/luar biasa) untuk mengelakkan "ujian secara pilihan"
- Lima dimensi semakan: keselamatan, pengendalian ralat, prestasi, kebolehselenggaraan, pengurusan kebergantungan
- Git ialah "ubat penyesalan": commit kerap, maju langkah kecil, pengasingan cawangan, kerap lihat diff
- Empat perangkap utama: kepercayaan (sahkan melalui ujian), pembengkakan (buang yang berlebihan), kefahaman (beri butiran secukupnya), konteks (tulis dalam fail memori)
:::
