---
id: di-wu-shi-jiu-zhang
num: 59
part: ios-kai-fa-pian
nav: Bab 59: Mengenali iOS—Ekosistem Apple dan Ekosistem Pembangunan
toc: default
kind: chapter
---

### Bab 59: Mengenali iOS — ekosistem Apple dan ekosistem pembangunan

{class="chapter-intro mb-4"}
Tahniah kerana membuat keputusan ini — daripada "pengguna iPhone" kepada "orang yang menulis aplikasi untuk iPhone". Sebelum mula, mari kita buka peta dahulu: dari mana iOS datang? Apakah maksud "taman berdinding" Apple kepada pembangun? Apa yang berlaku di antara jari anda menaip papan kekunci sehingga aplikasi sampai ke telefon pengguna?

#### 1. Asal usul iOS: sebuah telefon mengubah satu industri

Pada Januari 2007, Steve Jobs mengeluarkan iPhone generasi pertama pada sidang media. Pada masa itu ia bahkan tidak menyokong aplikasi pihak ketiga — sehinggalah 2008, Apple melancarkan App Store dan iPhone SDK, membenarkan pembangun seluruh dunia menulis perisian untuk iPhone. Pada saat itu, "ekonomi aplikasi" dilahirkan: hingga hari ini, terdapat berjuta-juta aplikasi di App Store, dengan bahagian kumulatif kepada pembangun melebihi ratusan bilion dolar AS.

Sistem itu sendiri turut berevolusi: pada asalnya bernama iPhone OS, ditukar nama kepada iOS pada 2010; nombor versi berjalan hingga iOS 17 (2023), kemudian pada 2025, Apple menukar penamaan mengikut tahun — iOS 26 dikeluarkan pada 2025, dan versi semasa pada Ogos 2026 ialah iOS 27. Nama boleh berubah, tetapi satu perkara tidak pernah berubah: tabiat membayar pengguna iOS dan reputasi kualiti perisianya diakui terbaik dalam ekosistem mudah alih — aplikasi yang sama, hasil di iOS sering jauh lebih tinggi daripada di Android.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Peristiwa</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Tahun</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Perkara penting untuk pembangun</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">App Store dilancarkan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2008</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ekosistem pembangunan pihak ketiga bermula</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift dikeluarkan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2014</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bahasa pembangunan iOS moden muncul</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI dikeluarkan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2019</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Rangka kerja antara muka deklaratif, garis utama buku ini</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">iOS 26 (tahun pertama nama baharu)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2025</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Penamaan mengikut tahun; Apple Intelligence disepadukan sepenuhnya</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">iOS 27</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2026</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Versi terkini semasa (asas buku ini)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Kronologi pembangunan iOS (sehingga Ogos 2026)

#### 2. Taman berdinding: "peraturan" dan "dividen" ekosistem Apple

Ekosistem Apple sering digambarkan sebagai "Taman Berdinding" (Walled Garden) — banyak peraturan dan diurus dengan ketat: aplikasi mesti melalui semakan sebelum diterbitkan, pembangunan mesti menggunakan Mac dan Xcode, pengedaran utamanya melalui App Store. Bunyinya sesak? Tetapi bagi pembangun, peraturan ini membawa dividen berbentuk wang sebenar:

- Pecahan peranti sangat kecil: model iPhone hanya beberapa jenis sahaja, saiz skrin dan versi sistem sangat seragam — dengan menyokong 5 model sahaja, anda sudah meliputi 95% pengguna (Android mungkin perlu menyokong puluhan model);
- Kadar kemas kini versi sistem sangat tinggi: dalam beberapa minggu selepas sistem baharu dikeluarkan, tujuh hingga lapan daripada sepuluh pengguna sudah menaik taraf; API baharu boleh digunakan dengan yakin tanpa perlu menjaga "sistem lama lima tahun lepas";
- Tabiat membayar pengguna baik: pengguna App Store lebih sanggup membelanjakan wang untuk aplikasi dan pembelian dalam apl;
- Semakan memang ketat, tetapi kedainya bersih: tiruan dan perisian jahat jarang, produk baik lebih mudah dilihat.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Perhatian: jelas dahulu tentang kos

{class="mt-1"}
Pembangunan iOS mempunyai syarat wajib: mesti ada sebuah Mac (Xcode eksklusif macOS), penerbitan memerlukan akaun pembangun 99 dolar AS setahun (akaun pembangun peribadi percuma boleh debug pada peranti sebenar secara tempatan, tetapi tidak boleh menerbitkan). Fikirkan pelaburan ini dengan matang sebelum memulakan — tetapi berita baiknya, pada peringkat pembelajaran akaun percuma sudah cukup, akan diterangkan dalam Bab 60.
:::

#### 3. Bahasa apa yang digunakan: Objective-C atau Swift?

Dalam sejarah pembangunan iOS juga ada dua "watak utama". Objective-C ialah veteran pengasas — digunakan dari 2008 hingga 2014; Swift ialah bahasa baharu yang dikeluarkan Apple pada 2014, kemudian berevolusi hingga Swift 6 (dikeluarkan 2024, memperkenalkan semakan konkurensi yang ketat), dan pada 2026, projek baharu hampir semuanya menggunakan Swift.

Nasihat jujur untuk anda yang tiada asas: terus belajar Swift, Objective-C tak perlu dilihat pun — melainkan selepas bekerja anda perlu menyelenggara kod warisan sepuluh tahun lepas. Kelebihan Swift: sintaks bersih (tanpa beban titik koma dan fail header zaman bahasa C), mekanisme Optional membasmi "ranapan penunjuk kosong" pada peringkat bahasa, berpadu tanpa jahitan dengan SwiftUI, dan ada Swift Playgrounds di iPad untuk belajar sambil bermain.

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
Gaya Objective-C (relik zaman purba)

{class="font-mono text-xs leading-relaxed"}
NSString *name = @"Ali"; [name stringByAppendingString:@"Hai"]; // tanda kurung siku + penunjuk + titik koma, tiga serangkai
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
Gaya Swift (moden dan bersih)

{class="font-mono text-xs leading-relaxed"}
var name = "Ali" name += "Hai" // sejelas bahasa semula jadi
:::
:::

#### 4. Bagaimana sebuah aplikasi dilahirkan?

Seperti semua platform, kelahiran aplikasi iOS juga mempunyai satu aliran kerja. Tetapi versi Apple ada dua "pemeriksaan keselamatan" tambahan:

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-lightbulb mr-1"></i> Idea</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center">📐 Reka bentuk (paparan+fungsi)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-keyboard mr-1"></i> Menulis kod (Swift + SwiftUI)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hammer mr-1"></i> Kompilasi dan tandatangan</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> Ujian (emulator+peranti sebenar)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-stamp mr-1"></i> Semakan Apple</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-party-horn mr-1"></i> Naik ke App Store</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Rajah 1: Aliran penuh sebuah aplikasi iOS daripada idea hingga diterbitkan (perhatikan peringkat "semakan" yang tambahan)
:::

Konsep utama dalam aliran ini:

- Tandatangan (Signing): setiap aplikasi iOS mesti "ditandatangani" sebelum boleh dipasang — membuktikan "pakej ini datang daripada anda dan tidak diubah suai". Pada peringkat pembelajaran, Xcode menandatangani secara automatik dengan Apple ID anda; semasa menerbitkan, gunakan sijil pembangun. Diterangkan terperinci dalam Bab 67.
- Simulator: iPhone maya di atas Mac, medan utama pembangunan dan debug. Ia berjalan pada CPU Mac, jadi sangat lancar; pengalamannya jauh lebih baik daripada emulator Android.
- TestFlight: alat "pengedaran ujian dalaman" rasmi Apple — sebelum penerbitan, hantar versi ujian kepada sehingga 10000 pengguna ujian, yang memasang dan mencubanya melalui aplikasi TestFlight. Ini keanggunan yang hanya ada dalam ekosistem iOS.

#### 5. Gambaran penuh tindanan teknologi iOS: "senarai senjata" anda

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Lapisan</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Pilihan utama (2026)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Untuk apa</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bahasa</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift 6</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bahasa untuk menulis logik</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Antara muka</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftUI + garis panduan reka bentuk Apple (HIG)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Melukis antara muka dengan kod (garis utama buku ini)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Seni bina</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MVVM + @Observable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Memisahkan antara muka dan logik</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Storan data</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SwiftData (pangkalan data) + UserDefaults (konfigurasi)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menyimpan data ke dalam telefon</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Rangkaian</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">URLSession + async/await + Codable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Berhubung dengan pelayan</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Alat binaan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode Build System / xcodebuild</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menukar kod kepada pakej pemasangan</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Persekitaran pembangunan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode (eksklusif macOS)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">IDE rasmi Apple</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Gambaran pantas tindanan teknologi utama iOS 2026

Ada perasan? Senarai ini lebih pendek sedikit daripada Android — kerana Apple telah "menguruskan" banyak perkara. Kos ekosistem tertutup ialah kebebasan; balasannya ialah ketenangan: tak perlu bingung memilih pustaka rangkaian atau pangkalan data yang mana, yang diberikan secara rasmi sering kali penyelesaian terbaik.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Praktik: lihat "pengenalan Apple" telefon anda

{class="mt-1"}
Buka [Tetapan] → [Am] → [Perihal] pada iPhone, catat tiga perkara: versi iOS, nama model, ruang tersedia. Kemudian santai layari halaman "Hari Ini" di App Store dan perhatikan tangkapan skrin serta teks aplikasi berkualiti — mulai hari ini, sudut pandangan anda melayari kedai mesti bertukar daripada "pengguna" kepada "pembangun".
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan bab ini

- 2008 App Store dilancarkan, "ekonomi aplikasi" lahir; versi semasa 2026 ialah iOS 27
- Kira-kira taman berdinding: banyak peraturan, tetapi peranti sedikit, versi baharu, pengguna sanggup membayar, kedai bersih
- Syarat wajib: mesti ada Mac; penerbitan perlukan akaun pembangun 99 dolar AS setahun; pada peringkat pembelajaran akaun percuma sudah cukup
- Terus belajar Swift; Objective-C hanya untuk kod warisan
- Aliran kerja ada satu peringkat lebih daripada Android: semakan Apple; TestFlight ialah alat hebat pengedaran ujian dalaman
- Tindanan teknologi piawai 2026: Swift 6 + SwiftUI + MVVM + SwiftData + URLSession + Xcode
:::
