---
id: di-si-shi-si-zhang
num: 44
part: ai-biancheng-pian
nav: Bab 44: Praktik daripada 0 ke 1—Aliran Penuh Projek Lengkap
toc: default
kind: chapter
---

### Bab 44: Amalan dari 0 ke 1 — Aliran Kerja Lengkap Sesuatu Projek

{class="chapter-intro mb-4"}
Teori sudah selesai dipelajari; kini masanya untuk bertindak. Bab ini bukan tutorial "ikut sahaja taip" yang mudah, tetapi satu metodologi amalan tentang "cara berfikir, cara bertanya, cara mengesahkan". Kita akan menggunakan tiga projek dengan tahap kesukaran berbeza untuk menunjukkan proses pemikiran lengkap daripada keperluan hingga hasil siap. Apa pun alat yang anda gunakan, aliran kerja ini sesuai.

#### 1. Projek satu: laman alat peribadi minimalis (peringkat permulaan)

##### 1. Pemikiran keperluan

Sasaran: cipta satu laman web alat peribadi yang memaparkan pintu masuk kepada 3-4 alat kecil yang berguna. Ini projek frontend tulen, tidak memerlukan backend dan pangkalan data. Fokusnya bukan pada betapa kompleksnya alat itu sendiri, tetapi pada pengalaman aliran kerja lengkap "daripada keperluan ke hasil siap".

Mengikut lima unsur keperluan: Who (siapa) — kegunaan peribadi. What (apa) — satu laman web yang memaparkan pintu masuk alat. Why (kenapa) — mengumpulkan alat yang kerap digunakan dalam satu halaman untuk akses mudah. How (bagaimana) — satu fail HTML+CSS+JS, tanpa framework. Constraint (kekangan) — siap dalam 30 minit, tidak perlu dilancarkan.

##### 2. Memberi arahan

Berdasarkan prinsip Think Before Coding, arahan anda patut mengandungi maklumat yang cukup untuk AI memahami sasaran, tetapi tidak perlu menentukan setiap butiran pelaksanaan:

::: div .code-block
:::inline div .code-head
<span>Arahan untuk AI</span><span class="dots">···</span>
:::

```
Sila bina satu laman web alat peribadi dengan keperluan:
1. HTML fail tunggal (CSS dan JS dalam baris), tanpa rangka kerja
2. Tema gelap, gaya minimalis moden
3. Paparkan 4 kad pintu masuk alat:
   - alat perumus teks
   - alat pengira kata
   - alat pemilih warna
   - penjana kod QR
4. Setiap kad ada ikon, tajuk dan huraian ringkas
5. Kad ada kesan animasi ketika hover
6. Responsif, boleh guna pada telefon
7. Ada bar tajuk di atas
Terus berikan fail HTML lengkap.
```
:::

##### 3. Penerimaan dan iterasi

Selepas AI memberikan kod, buat penerimaan mengikut semakan tiga lapisan pengesahan iterasi. Lapisan pertama, pengesahan fungsi: bolehkah fail dibuka dalam pelayar? Adakah kesemua 4 kad dipaparkan? Adakah animasi hover berfungsi normal? Lapisan kedua, pengesahan sempadan: adakah susun atur normal pada saiz skrin telefon? Adakah kad bertukar baris apabila tetingkap sangat sempit? Lapisan ketiga, pengesahan seni bina: adakah kod boleh dibaca? Adakah CSS digabungkan dalam satu teg style? Adakah ada lebihan yang ketara?

Jika anda juga mahu melaksanakan fungsi sesuatu kad alat (bukan sekadar pintu masuk), boleh ditambah secara berperingkat — tambahkan fungsi satu alat setiap kali, dan tambahkan yang berikutnya selepas pengesahan. Inilah aplikasi sebenar strategi "langkah kecil pantas".

#### 2. Projek dua: sistem catatan kewangan full-stack (peringkat pertengahan)

##### 1. Pemikiran keperluan dan PRD

Sasaran: satu aplikasi catatan kewangan full-stack yang mempunyai frontend, backend dan pangkalan data. Projek ini jauh lebih kompleks daripada yang pertama dan perlu menggunakan kaedah kejuruteraan keperluan dalam Bab 40.

Tulis PRD dahulu. Mengikut templat dalam Seksyen 3 Bab 40, tuliskan gambaran keseluruhan projek, senarai fungsi, pelan teknikal, model data dan pelan pembangunan. Pemilihan pelan teknikal perlu mempertimbangkan prinsip Simplicity First — frontend menggunakan React tetapi tanpa pengurusan status yang kompleks seperti Redux; backend menggunakan Node.js tetapi tanpa microservices; pangkalan data menggunakan SQLite dan bukan PostgreSQL (pada peringkat pembangunan).

Pelan pembangunan dipecahkan kepada 5 langkah: Langkah 1 rangka API backend (pelayan Express + SQLite + antara muka CRUD); Langkah 2 halaman asas frontend (senarai rekod + borang tambah); Langkah 3 penyepaduan frontend-backend (panggilan API + paparan data); Langkah 4 fungsi kategori dan penapisan; Langkah 5 ringkasan bulanan dan carta ringkas. Setiap langkah yang siap ialah "sesuatu yang boleh digunakan".

##### 2. Menetapkan fail memori projek

Sebelum mula mengekod, cipta dahulu fail memori projek. Ini amalan teras kejuruteraan konteks — memastikan AI memahami latar belakang projek pada permulaan setiap perbualan.

::: div .code-block
:::inline div .code-head
<span>CLAUDE.md</span><span class="dots">···</span>
:::

```
# Projek: aplikasi perakaunan penuh
## Ringkasan
Aplikasi perakaunan peribadi, menyokong rekod, kategori dan ringkasan bulanan.
## Teknologi
- Frontend: React + TypeScript + Vite
- Backend: Node.js + Express + TypeScript
- Pangkalan data: SQLite (melalui better-sqlite3)
- Definisi jenis dikongsi frontend-backend
## Persetujuan API
- Laluan asas: /api
- Format respons: { success: boolean, data: any, error: string }
- Gaya RESTful
## Model data
Record { id, amount, type, category, note, date }
## Peraturan penulisan kod
- TypeScript mod ketat
- Inden 2 ruang
- Fungsi ada komen JSDoc
- Komen dan mesej komit dalam bahasa Mandarin
```
:::

##### 3. Pelaksanaan berperingkat

Mengikut pelan pembangunan, setiap langkah disiapkan dengan satu perbualan berasingan. Berikut contoh arahan untuk langkah pertama:

::: div .code-block
:::inline div .code-head
<span>Arahan untuk AI (Step 1)</span><span class="dots">···</span>
:::

```
Saya perlu cipta rangka API backend.
Keperluan:
1. Pelayan Express, port 3001
2. Pangkalan data SQLite, nama jadual records
3. Medan jadual records:
   id (TEXT PRIMARY KEY)
   amount (REAL)
   type (TEXT: 'income'|'expense')
   category (TEXT)
   note (TEXT)
   date (TEXT: YYYY-MM-DD)
4. API CRUD:
   GET /api/records - dapatkan semua rekod
   POST /api/records - tambah rekod
   PUT /api/records/:id - kemas kini rekod
   DELETE /api/records/:id - padam rekod
5. Middleware pengendalian ralat
Berikan struktur kod backend yang lengkap.
```
:::

Perhatikan ciri arahan ini: ia hanya menerangkan langkah semasa (rangka backend), tanpa mencampurkan keperluan frontend; ia menyenaraikan medan dan antara muka dengan jelas (memberikan AI kekangan yang cukup), tetapi pelaksanaan khusus ditentukan oleh AI; ia mematuhi prinsip Goal-Driven Execution — menyebut "buat apa" dan bukan "cara buat".

Selepas AI memberikan kod, sahkan serta-merta: jalankan pelayan, uji setiap antara muka dengan curl atau Postman untuk memastikan ia berfungsi normal. Selepas dipastikan tiada masalah, buka perbualan baharu untuk Langkah 2 (halaman asas frontend). Setiap langkah mematuhi kitaran "arahan-pengesahan-perbualan baharu".

#### 3. Projek tiga: aplikasi dipertingkat AI (peringkat lanjutan)

##### 1. Konsep projek

Sasaran: satu aplikasi yang menyambung ke API model besar — contohnya "Pembantu Pembelajaran AI"; pengguna memasukkan kandungan pembelajaran, dan AI menjana ringkasan, mengaitkan poin pengetahuan serta mengesyorkan sumber pembelajaran. Keistimewaan projek ini ialah: aplikasi anda sendiri sedang memanggil AI, jadi anda perlu mengendalikan panggilan API, kejuruteraan prompt, pengendalian ralat dan masalah baharu yang lain.

Pelajaran terpenting yang diajarkan projek ini ialah: apabila anda "menggunakan AI untuk menulis kod yang memanggil AI", anda perlu memberi perhatian lebih kepada kejuruteraan prompt. Prompt yang digunakan oleh aplikasi anda semasa memanggil API model besar juga perlu mematuhi prinsip yang dibincangkan dalam panduan ini — jelas, ringkas dan berpandukan sasaran.

##### 2. Perkara teknikal penting

Projek ini melibatkan beberapa perkara teknikal yang belum anda temui dalam dua projek terdahulu:

- Pengurusan kunci API: kunci tidak boleh sesekali dikodkan terus dalam kod; urus dengan pemboleh ubah persekitaran;
- Pengendalian respons penstriman: balasan model besar biasanya disalurkan secara berperingkat (streaming) dan perlu dipaparkan sedikit demi sedikit;
- Kawalan penggunaan Token: model besar dibilkan mengikut token, jadi penggunaan perlu dikawal pada peringkat aplikasi;
- Pengurusan templat Prompt: fungsi yang berbeza menggunakan templat prompt yang berbeza, jadi perlu diurus secara berstruktur.

Semua perkara teknikal ini boleh dilaksanakan dengan bantuan AI, tetapi anda perlu memahami "kenapa" setiap satu — kenapa kunci tidak boleh dikodkan terus? Kenapa perlu respons penstriman? Kenapa penggunaan token perlu dikawal? Hanya dengan memahami "kenapa", anda dapat menilai sama ada penyelesaian AI itu munasabah.

#### 4. Senarai semak aliran kerja amalan sejagat

Apa pun saiz projeknya, berikut ialah senarai semak aliran kerja amalan pengaturcaraan AI yang sejagat. Setiap kali memulakan projek baharu, lalui senarai ini untuk memastikan tiada langkah penting terlepas.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Peringkat</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Apa yang dibuat</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Prinsip berkaitan</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">1. Pemikiran keperluan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lalui lima unsur keperluan; fikirkan dengan jelas apa yang hendak dibuat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Think Before Coding</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2. Penguraian keperluan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pecahkan keperluan besar kepada langkah kecil yang boleh disahkan secara berasingan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Simplicity First</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3. Menulis PRD</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Susun menjadi dokumen berstruktur sebagai rujukan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Goal-Driven</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">4. Menetapkan fail memori</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cipta CLAUDE.md atau fail seumpamanya</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Harness Engineering</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">5. Pelaksanaan berperingkat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Satu perbualan bagi setiap langkah: arahan-pengesahan-langkah seterusnya</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Surgical Changes</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">6. Pengujian dan pengesahan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Uji ketepatan fungsi serta-merta selepas setiap langkah siap</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Iterate &amp; Verify</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">7. Semakan kod</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Semak kesesuaian seni bina, keselamatan dan kebolehselenggaraan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Iterate &amp; Verify</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">8. Iterasi dan pengoptimuman</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Buat penambahbaikan beriterasi berdasarkan hasil ujian dan semakan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Iterate &amp; Verify</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Senarai semak aliran kerja amalan pengaturcaraan AI sejagat

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mari praktik: siapkan "Projek satu" minggu ini

{class="mt-1"}
Jadikan "laman alat peribadi" dalam Seksyen 1 Bab 44 sebagai tugasan pengaturcaraan AI pertama anda: luangkan 5 minit untuk melalui lima unsur, hantar arahan kepada AI (alat mana pun boleh), kemudian buat penerimaan mengikut pengesahan tiga lapisan. Siapkannya dalam 30 minit — hasil kerja pengaturcaraan AI pertama anda akan lahir. Selepas siap, simpanlah dengan baik; ia ialah cenderamata anda bertukar daripada "pembaca" kepada "pengamal".
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan bab ini

- Projek satu (permulaan): laman alat frontend tulen — alami aliran kerja lengkap; boleh siap dalam 30 minit
- Projek dua (pertengahan): sistem catatan kewangan full-stack — PRD + fail memori + pelaksanaan berperingkat 5 langkah; setiap langkah "boleh digunakan"
- Projek tiga (lanjutan): pembantu pembelajaran AI — guna AI menulis kod yang memanggil AI; perhatikan kejuruteraan prompt
- Aliran kerja sejagat lapan langkah: pemikiran keperluan → penguraian → PRD → fail memori → pelaksanaan berperingkat → ujian → semakan → iterasi
- Setiap langkah mematuhi kitaran "arahan-pengesahan-perbualan baharu"
:::
