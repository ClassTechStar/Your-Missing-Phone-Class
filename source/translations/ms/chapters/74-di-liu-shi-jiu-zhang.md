---
id: di-liu-shi-jiu-zhang
num: 69
part: ios-kai-fa-pian
nav: Bab 69: Manual Rujukan Pantas dan Sumber
toc: default
kind: chapter
---

### Bab 69: Buku Rujukan Pantas dan Sumber

{class="chapter-intro mb-4"}
Bab ini ialah buku rujukan pantas yang boleh digunakan secara berasingan. Apabila tidak ingat sesuatu gaya penulisan atau perlu membuat keputusan pantas, terus buka di sini. Disyorkan menjadikannya 'kad poket': rujukan pantas kod lazim, soalan lazim, sumber pembelajaran — jangan terlepas satu halaman pun.

#### 1. Kad rujukan pantas kod lazim

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Apa yang mahu dibuat</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Kod utama</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">State peribadi halaman</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@State private var x = nilai awal</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Logik merentas halaman</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">@Observable class VM { var x = 0 }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Susun atur menegak/mengufuk</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">VStack { }</code> / <code class="inline">HStack { }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ruang fleksibel</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Spacer()</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Senarai</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">List { ForEach(tatasusunan) { ... } }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lompatan halaman</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">NavigationStack + NavigationLink</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pop timbul bawah</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">.sheet(isPresented: $show) { kandungan }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tutup halaman semasa</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">@Environment(\.dismiss) var dismiss</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ambil data melalui internet</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">try await URLSession.shared.data(from: url)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Penghuraian JSON</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">struct X: Codable</code> + <code class="inline">JSONDecoder().decode</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Simpan tetapan kecil</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">UserDefaults.standard.set(nilai, forKey: "kunci")</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Simpan data berstruktur</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">@Model</code> + <code class="inline">modelContainer</code> + <code class="inline">@Query</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Penyesuaian mod gelap</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Guna warna sistem (.primary / Color(.systemGray6)), jangan tulis secara tetap</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Jalankan ujian</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><kbd>⌘U</kbd></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Kad rujukan pantas pembangunan iOS (edisi Ogos 2026)

#### 2. Soalan lazim FAQ

Q1: Saya tiada Mac, boleh belajar pembangunan iOS?

Boleh belajar bahasa, tetapi tidak boleh membuat pembangunan penuh. Swift Playgrounds pada iPad/iPhone boleh menyiapkan keseluruhan kandungan Bab 61; tetapi Xcode eksklusif untuk macOS, akhirnya anda mesti mempunyai sebuah Mac. Bajet terhad? Sewa Mac awan atau beli Mac mini terpakai dahulu sebagai peralihan, kemudian tentukan pelaburan selepas menamatkan bahasa.

Q2: Berapa kos untuk belajar pembangunan iOS?

Peringkat pembelajaran: 0 kos (Xcode percuma + Apple ID percuma untuk ujian pada peranti sebenar). Peringkat penerbitan: akaun pembangun 99 dolar AS/tahun (kira-kira 700 yuan). Ditambah pelaburan perkakasan sebuah Mac, itulah keseluruhan kosnya. Berbanding pulangannya — walaupun alat kecil di App Store juga mempunyai pengguna berbayar — perakaunan ini berbaloi.

Q3: Belajar SwiftUI atau UIKit dahulu?

SwiftUI. Projek baharu, tutorial baharu dan jawatan baharu pada 2026 semuanya berasaskan SwiftUI, dan buku ini menggunakannya dari mula hingga akhir. UIKit ialah rangka kerja generasi sebelumnya dan masih digunakan dalam banyak projek lama — selepas anda mahir SwiftUI, tambah UIKit mengikut keperluan (dokumen rasmi menyediakan tutorial interoperasi); ia mudah dikuasai kemudian. Jangan terbalikkan urutannya.

Q4: Mudahkah mencari kerja dalam pembangunan iOS?

Keadaan pasaran pada 2026: jawatan peringkat permulaan yang hanya 'boleh melukis antara muka' bersaing sengit, tetapi pembangun yang 'faham Swift + SwiftUI + mempunyai karya diterbitkan' tetap dicari-cari. Gaji sederhana jawatan iOS sentiasa berada di tangga teratas antara pelbagai tumpukan teknologi. Untuk anda yang masih dalam peringkat pembelajaran, resume terbaik ialah App buatan sendiri yang ada di dalam kedai itu.

Q5: Apa yang perlu dilakukan jika App ditolak semasa semakan?

Jangan panik, ini perkara biasa—kebarangkalian ditolak pada penghantaran pertama tidak rendah. Sebab penolakan Apple biasanya ditulis dengan sangat terperinci (halaman mana, garis panduan yang mana). Baiki satu demi satu, kemudian balas dengan penerangan dalam App Store Connect dan hantar semula. Tiga sebab penolakan yang paling biasa: kegunaan kebenaran tidak dijelaskan dengan jelas, antara muka mempunyai bug, dan metadata (tangkapan skrin/penerangan) tidak sepadan dengan aplikasi sebenar. Memeriksa ketiga-tiga perkara ini lebih awal boleh menjimatkan satu pusingan penantian.

#### 3. Rujukan Pantas Pintasan Xcode yang Kerap Digunakan

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Tindakan</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Pintasan</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Jalankan / Uji</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘R / ⌘U</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Buka pratonton kanvas</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌥⌘↩</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Buka fail dengan pantas</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘O</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Carian menyeluruh</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘F</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Format indentasi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌃I</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Komen / Buang komen</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘/</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kosongkan cache binaan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⇧⌘K</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lompat ke definisi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">⌘ + klik</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Namakan semula (tukar nama dengan selamat di seluruh projek)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Klik kanan → Refactor → Rename</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Rujukan Pantas Pintasan Xcode yang Kerap Digunakan

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tips: Masalah kompilasi misteri? Kosongkan cache dahulu

{class="mt-1"}
"Semalam boleh jalan, hari ini tak boleh lagi"—daripada sepuluh kejadian aneh sebegini, enam atau tujuh daripadanya berpunca daripada cache binaan yang bercelaru. Kosongkan dengan ⇧⌘K kemudian bina semula, ini boleh menyembuhkan lebih separuh masalah misteri. Kalau masih tidak boleh, mulakan semula Xcode (sekali dengan Mac), dan kalau masih gagal juga, "padam folder DerivedData"—inilah tiga langkah muktamad yang diwarisi secara lisan dalam kalangan pembangun iOS.
:::

#### 4. Sumber Pembelajaran yang Disyorkan

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Jenis</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Sumber</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Sebab disyorkan</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Rasmi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">developer.apple.com</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Dokumentasi rasmi Apple, semua tutorial SwiftUI/Swift ada di dalamnya, rujukan paling sahih</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Rasmi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI Tutorials daripada Apple</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kursus rasmi tunjuk ajar langkah demi langkah, sangat mesra untuk pengguna baharu</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Rasmi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Laman rasmi Swift (swift.org)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Dokumentasi rasmi bahasa dan tapak latihan dalam talian</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Komuniti</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Hacking with Swift</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Perpustakaan tutorial percuma Paul Hudson, kualitinya diakui berada di peringkat teratas</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Komuniti</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Stack Overflow (tag swiftui)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tempat pertama meminta pertolongan apabila berlaku ralat</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Video</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Saluran rasmi Apple Developer (video WWDC)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Penerangan sahih tentang teknologi baharu setiap tahun</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Reka bentuk</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Panduan Antara Muka Manusia Apple (HIG)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kitab rasmi untuk menghasilkan antara muka ber"rasa Apple"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pelengkap</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bahagian Ketujuh "Praktik Pengaturcaraan AI" (Bab 37-47)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Panduan lengkap menggunakan AI bagi membantu pembangunan iOS</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Senarai Sumber Pembelajaran Pembangunan iOS (Ogos 2026)

#### 5. Penutup: Daripada App Pertama ke App ke-N

Bila dilihat kembali, anda telah bergerak daripada "tidak tahu apa itu SwiftUI" kepada memasang Xcode, mempelajari Swift, melukis antara muka dengan SwiftUI, menyambungkan App kepada pangkalan data dan rangkaian, kemudian menguji, membungkus dan menerbitkannya—sepanjang perjalanan ini, anda telah menamatkan bahagian yang paling sukar dalam perjalanan daripada sifar ke satu.

Dunia teknologi berubah dengan sangat pantas: rangka kerja akan dinaik taraf, alat akan ditukar ganti, dan AI akan mengambil alih lebih banyak kerja "menaip papan kekunci". Tetapi ada satu perkara yang tidak akan lapuk: kebolehan anda menguraikan idea yang kabur menjadi langkah yang jelas, kemudian melaksanakannya langkah demi langkah. Alat ialah pembesar, manakala cara berfikir ialah asas. Pembesar boleh diganti, tetapi asas tidak boleh tergugat.

:::inline div .quote-line
Anda bukan lagi sekadar "orang yang mahir guna telefon". Anda boleh mengubah idea dalam kepala menjadi aplikasi yang benar-benar berjalan pada ratusan juta iPhone. Mulai hari ini, berkarya dengan papan kekunci—itulah romantisme pembangun iOS.
:::

#### Rujukan

{class="list-decimal pl-6 mb-3 space-y-1 text-xs text-gray-500"}
1. Apple Inc. (2026). SwiftUI Framework Documentation. developer.apple.com.
2. Apple Inc. (2026). Swift Programming Language Guide. swift.org.
3. Apple Inc. (2026). SwiftData Framework Documentation. developer.apple.com.
4. Apple Inc. (2026). App Store Review Guidelines. developer.apple.com/app-store/review.
5. Apple Inc. (2026). Human Interface Guidelines (HIG). developer.apple.com/design.
6. Apple Inc. (2026). Xcode 27 Release Notes and App Distribution Guide.
