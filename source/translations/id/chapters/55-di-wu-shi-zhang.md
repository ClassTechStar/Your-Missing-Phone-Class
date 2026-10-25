---
id: di-wu-shi-zhang
num: 50
part: an-zhuo-kai-fa-pian
nav: Bab 50: Kilat Kotlin—Bahasa Utama Pengembangan Android
toc: default
kind: chapter
---

### Bab 50: Cepat Mengenal Kotlin—Bahasa Pertama Pengembangan Android

{class="chapter-intro mb-4"}
Di bab ini kita resmi belajar bahasanya. Jangan tegang—Kotlin terkenal 'ramah pemula', dan kamu tidak perlu menghafal buku tata bahasa: dengan menguasai 20% sintaksnya dulu, kamu bisa memahami dan menulis 80% kode sehari-hari. Sisanya dipelajari sambil mengerjakan proyek. Ingat prinsip belajar kita: memahami > menghafal, bisa pakai > mahir.

#### 1. Variabel dan Tipe: Memberi Nama pada Data

Program adalah 'data + logika'. Variabel adalah memberi nama pada data dan menyimpannya. Kotlin punya dua cara deklarasi:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Variabel</span><span class="dots">···</span>
:::

```
val name = "Zhang San"        // val: variabel hanya-baca (disarankan jadi default)
var age = 18             // var: variabel yang bisa berubah (masih bisa diganti)

age = 19                 // <i class="fas fa-check-circle mr-1"></i> var bisa diubah
// name = "Li Si"         // <i class="fas fa-times-circle mr-1"></i> val tidak bisa diubah, error saat kompilasi

val score: Int = 100     // juga bisa menuliskan tipenya secara eksplisit
val pi = 3.14            // tidak ditulis pun otomatis terdeteksi
```
:::

Tipe yang sering dipakai hanya beberapa; hafalkan lewat satu tabel:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Tipe</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Menyimpan Apa</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Contoh</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Int</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bilangan bulat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">42</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Double</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bilangan desimal</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3.14</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">String</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Teks</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"Halo"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Boolean</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Benar/salah</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">true / false</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">List&lt; T&gt;</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sekumpulan data</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">listOf(1, 2, 3)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Tipe-tipe dasar Kotlin yang sering dipakai

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tips: Prinsip val Dulu

{class="mt-1"}
Hukum besi komunitas Kotlin: pakai val secara bawaan, pakai var hanya kalau memang perlu. Kalau tempat yang bisa memakai val malah memakai var, IDE akan memperingatkanmu dengan teks kuning. Kebiasaan ini menyelamatkanmu dari satu golongan besar bug 'variabel berubah tanpa sengaja'—makin sedikit hal yang berubah, makin mudah kodenya ditelusuri.
:::

#### 2. Fungsi: Mengemas Logika Menjadi 'Tombol'

Fungsi adalah logika yang diberi nama, seperti tombol di remote—ditekan sekali (dipanggil), serangkaian aksi langsung dijalankan. Di Kotlin dideklarasikan dengan fun:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Fungsi</span><span class="dots">···</span>
:::

```
fun greet(name: String): String {
    return "Halo, $name!"     // simbol $ menyisipkan variabel ke dalam string
}

println(greet("Zhang San"))        // Keluaran: Halo, Zhang San!

// Fungsi satu baris bisa ditulis singkat sebagai ekspresi
fun add(a: Int, b: Int) = a + b

println(add(3, 5))            // Keluaran: 8
```
:::

Beberapa poin penting: parameter ditulis di dalam kurung (nama dulu, tipe belakang, dipisah titik dua); tipe kembalian ditulis setelah kurung; template string $namavariabel adalah kepraktisan andalan Kotlin—tidak perlu menyambung-nyambung 'string + variabel' seperti di Java.

#### 3. Kondisi dan Perulangan: Membuat Program 'Berpikir'

Kecerdasan program datang dari dua hal: bisa menilai (if/when) dan bisa mengulang (for/while).

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Percabangan dan perulangan</span><span class="dots">···</span>
:::

```
// Percabangan: if / else
val age = 17
if (age >= 18) {
    println("Dewasa")
} else {
    println("Di bawah umur")
}

// Banyak cabang: when (jauh lebih enak daripada switch)
val score = 85
val level = when {
    score >= 90 -> "Sangat baik"
    score >= 60 -> "Lulus"
    else -> "Semangat terus!"
}

// Ulangi: loop for
val fruits = listOf("apel", "pisang", "jeruk")
for (fruit in fruits) {
    println("Aku suka makan$fruit")
}
```
:::

when adalah cara percabangan banyak yang paling sering dipakai di Kotlin; dalam pengembangan Android kamu memakainya setiap hari (misalnya menampilkan tampilan berbeda sesuai status).

#### 4. Null Safety: 'Jimat Penyelamat' Kotlin

Bug paling terkenal era Java bernama NullPointerException (pengecualian pointer kosong)—program mengakses sesuatu yang 'tidak berisi apa-apa' dan langsung crash. Statistik menunjukkan ia selalu menduduki puncak daftar crash Android. Kotlin menyelesaikannya dari level bahasa: secara bawaan nilai kosong tidak diizinkan.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Null Safety</span><span class="dots">···</span>
:::

```
var name: String = "Zhang San"   // Tipe biasa: sama sekali tidak boleh null
// name = null                // <i class="fas fa-times-circle mr-1"></i> Ditemukan langsung oleh compiler

var nickname: String? = null // beri tanda tanya: mengizinkan null
nickname = "San Er"

// Saat memakai nullable type, wajib ditangani dengan aman:
println(nickname?.length)    // safe call: null tetap kembalikan null, tidak crash
val len = nickname?.length ?: 0   // Elvis operator: kalau null beri nilai default
println(len)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Perhatian: Jangan Tertukar antara ? dan ?:

{class="mt-1"}
String? berarti 'boleh kosong', sedangkan a ?: b berarti 'jika a kosong pakai b' (bentuknya mirip rambut Elvis, makanya disebut operator Elvis). Di awal menulis kode, kalau kompiler munculkan 'error terkait null', delapan dari sepuluh kali kamu lupa menangani tipe nullable—justru itu bahasanya sedang melindungimu.
:::

#### 5. Kelas dan Objek: Cetakan Pembuat 'Komponen'

Kelas adalah 'cetakan' bagi objek, objek adalah 'hasil jadi' dari kelas. Semua hal di Android—halaman, tombol, data—adalah objek. Kotlin punya senjata ampuh bernama data class (kelas data), khusus 'wadah data', satu baris setara puluhan baris Java:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Class dan data class</span><span class="dots">···</span>
:::

```
// Kelas biasa: cetakan
class Dog(val name: String) {
    fun bark() = println("$name gonggong!")
}

val dog = Dog("Bobi")      // Buat objek
dog.bark()                 // Bobi gonggong!

// data class: kotak penyimpan data (otomatis punya equals/copy dll.)
data class User(val id: Int, val name: String, val email: String)

val me = User(1, "Zhang San", "zhangsan@example.com")
val twin = me.copy(name = "Zhang Sanfeng")   // Salin sambil mengubah satu field
```
:::

Nanti kalau kamu membuat aplikasi catatan keuangan, satu catatan adalah satu data class: data class Record(val amount: Double, val category: String, val date: String). Lihat, kamu sudah bisa menulis struktur kode seperti proyek sungguhan.

#### 6. Lambda dan Fungsi Tingkat Tinggi: 'Gula Sintaks' Kotlin

Di kode Android kamu akan melihat { ... } setiap hari; 'fungsi tanpa nama' itu disebut lambda (fungsi anonim). onClick milik Button = { count++ } adalah sebuah lambda—mengemas 'apa yang dilakukan setelah ditekan' menjadi satu bungkus lalu menyerahkannya ke tombol.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Perkenalan lambda</span><span class="dots">···</span>
:::

```
// Cara biasa: definisikan fungsi bernama, baru kirimkan
fun double(x: Int) = x * 2
val result = listOf(1, 2, 3).map(::double)

// Gaya lambda: didefinisikan di tempat, ringkas
val result2 = listOf(1, 2, 3).map { it * 2 }   // it = elemen saat ini

// Saring + ubah berantai (sangat umum di proyek nyata)
val bills = listOf(12.5, 88.0, 5.0, 200.0)
val bigBills = bills.filter { it > 50 }.sorted()
// [88.0, 200.0]—"tagihan di atas 50, diurutkan rapi"
```
:::

Catat beberapa 'kombinasi koleksi' yang sering muncul: filter (menyaring), map (mengubah), sorted (mengurutkan), sum (menjumlahkan). 90% pengolahan daftarmu ke depan adalah kombinasi empat jurus ini. Filosofi Kotlin: logika yang bisa dijelaskan dengan satu kalimat, jangan ditulis lima kalimat.

#### 7. Kartu Cheatsheet Sintaks untuk Pemula Total

Jangan mencoba menghafal semua sintaks dalam sehari. Simpan kartu ini, buka saat menulis kode, dua pekan kemudian otomatis terbiasa:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ingin Melakukan Apa</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Cara Menulisnya</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mendefinisikan variabel hanya-baca</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">val x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mendefinisikan variabel yang bisa berubah</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">var x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mendefinisikan fungsi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">fun nama(parameter): tipeKembalian { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Percabangan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if (kondisi) {...} else {...}</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Percabangan banyak</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">when { kondisi -> hasil }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Perulangan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">for (x in daftar) { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menyambung string</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"Halo, $name"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menangani nilai kosong</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">x?.length ?: 0</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mendefinisikan data class</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">data class X(val a: Int, val b: String)</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Kartu cheatsheet sintaks Kotlin (edisi pemula)

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Praktik: Mainkan Kotlin 10 Menit Tanpa Memasang Apa Pun

{class="mt-1"}
Buka play.kotlinlang.org di peramban (taman bermain resmi Kotlin), tempelkan setiap potongan kode bab ini dan jalankan, ubah-ubah angka dan teksnya, lihat bagaimana keluarannya berubah. 10 menit 'main dulu belajar kemudian' ini akan membuatmu dua kali lebih ringan saat memulai Bab 51.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan Bab Ini

- Utamakan val, pakai var seperlunya; tipe bisa ditebak otomatis, tapi boleh juga dinyatakan eksplisit setelah titik dua
- Fungsi = logika yang dikemas; template string $ adalah kepraktisan andalannya
- if/when untuk percabangan, for untuk perulangan; when adalah 'serbaguna' di pengembangan Android
- Null safety adalah jimat penyelamat Kotlin: tipe biasa menolak null, tipe nullable harus ditangani dengan ? / ?:
- data class adalah kotak penyimpan data, satu properti satu baris, dipakai setiap hari di proyek nyata
- 20% sintaks mengerjakan 80% pekerjaan: bisa pakai dulu, mahir kemudian
:::
