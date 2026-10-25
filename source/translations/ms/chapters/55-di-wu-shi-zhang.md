---
id: di-wu-shi-zhang
num: 50
part: an-zhuo-kai-fa-pian
nav: Bab 50: Kilat Kotlin—Bahasa Pertama Pembangunan Android
toc: default
kind: chapter
---

### Bab 50: Panduan Pantas Kotlin — Bahasa Pertama Pembangunan Android

{class="chapter-intro mb-4"}
Dalam bab ini kita mula belajar bahasa secara rasmi. Jangan gementar — Kotlin terkenal 'mesra pemula', dan anda tidak perlu menghafal buku tatabahasa: kuasai dahulu 20% tatabahasa, anda sudah boleh memahami dan menulis 80% kod harian. Sisanya dicari semasa membuat projek. Ingat prinsip pembelajaran kita: memahami > menghafal, boleh guna > mahir.

#### 1. Pemboleh Ubah dan Jenis: Memberi Nama kepada Data

Program ialah 'data + logik'. Pemboleh ubah ialah memberi nama kepada data dan menyimpannya. Kotlin ada dua cara pengisytiharan:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Pemboleh ubah</span><span class="dots">···</span>
:::

```
val name = "Zhang San"        // val: pemboleh ubah baca sahaja (digalakkan sebagai lalai)
var age = 18             // var: pemboleh ubah boleh ubah (boleh ditukar kemudian)

age = 19                 // <i class="fas fa-check-circle mr-1"></i> var boleh diubah
// name = "Li Si"         // <i class="fas fa-times-circle mr-1"></i> val tidak boleh diubah, ralat semasa kompilasi

val score: Int = 100     // juga boleh tulis jenisnya secara jelas
val pi = 3.14            // tidak ditulis pun boleh dikesan automatik
```
:::

Jenis yang lazim hanya beberapa jenis, ingat dengan satu jadual:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Jenis</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Menyimpan apa</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Contoh</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Int</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Nombor bulat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">42</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Double</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Nombor perpuluhan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3.14</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">String</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Teks</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"Hai"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Boolean</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Benar/Salah</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">true / false</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">List&lt; T&gt;</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Satu set data</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">listOf(1, 2, 3)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Jenis asas lazim Kotlin

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Petua: Prinsip Keutamaan val

{class="mt-1"}
Hukum mutlak komuniti Kotlin: guna val secara lalai, guna var hanya apabila benar-benar perlu. Jika guna var di tempat yang boleh guna val, IDE akan memberi amaran dengan teks kuning. Tabiat ini membantu anda mengelakkan satu kategori besar pepijat 'pemboleh ubah diubah tanpa sengaja' — semakin sedikit perubahan pada kod, semakin mudah ia difahami.
:::

#### 2. Fungsi: Membungkus Logik Menjadi 'Butang'

Fungsi ialah satu logik yang bernama, seperti butang pada alat kawalan jauh — tekan sekali (panggil), satu siri tindakan dilaksanakan. Dalam Kotlin, isytiharkan dengan fun:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Fungsi</span><span class="dots">···</span>
:::

```
fun greet(name: String): String {
    return "Hai, $name!"     // simbol $ menyisipkan pemboleh ubah ke dalam rentetan
}

println(greet("Zhang San"))        // Output: Hai, Zhang San!

// Fungsi satu baris boleh ditulis ringkas sebagai ungkapan
fun add(a: Int, b: Int) = a + b

println(add(3, 5))            // Output: 8
```
:::

Beberapa perkara penting: parameter ditulis dalam tanda kurung (nama di hadapan, jenis di belakang, dipisahkan dengan usus besar); jenis pulangan ditulis selepas tanda kurung; templat rentetan $namapembolehubah ialah kemudahan khas Kotlin — tidak perlu lagi mencantum 'rentetan + pemboleh ubah' seperti dalam Java.

#### 3. Syarat dan Gelung: Membuat Program 'Berfikir'

Kepintaran program datang daripada dua perkara: tahu menilai (if/when) dan tahu mengulang (for/while).

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Syarat dan gelung</span><span class="dots">···</span>
:::

```
// Penilaian: if / else
val age = 17
if (age >= 18) {
    println("Dewasa")
} else {
    println("Belum dewasa")
}

// Pelbagai cabang: when (jauh lebih selesa daripada switch)
val score = 85
val level = when {
    score >= 90 -> "Cemerlang"
    score >= 60 -> "Lulus"
    else -> "Terus berusaha!"
}

// Ulangan: gelung for
val fruits = listOf("epal", "pisang", "oren")
for (fruit in fruits) {
    println("Aku suka makan$fruit")
}
```
:::

when ialah cara pencabangan berbilang yang paling kerap digunakan dalam Kotlin; dalam pembangunan Android anda akan menggunakannya setiap hari (contohnya memaparkan antara muka berbeza mengikut keadaan).

#### 4. Keselamatan Null: 'Penyelamat Nyawa' Kotlin

Pepijat paling terkenal zaman Java dipanggil NullPointerException (pengecualian penuding kosong) — program mengakses sesuatu yang 'tiada apa-apa' dan terus ranap. Menurut statistik, ia sentiasa nombor satu dalam senarai ranapan Android. Kotlin menyelesaikannya pada peringkat bahasa: nilai kosong tidak dibenarkan secara lalai.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Null Safety</span><span class="dots">···</span>
:::

```
var name: String = "Zhang San"   // Jenis biasa: langsung tidak boleh null
// name = null                // <i class="fas fa-times-circle mr-1"></i> Ditahan terus oleh pengkompil

var nickname: String? = null // beri tanda soal: membenarkan null
nickname = "San Er"

// Semasa guna jenis nullable, mesti ditangani dengan selamat:
println(nickname?.length)    // safe call: null kekal pulangkan null, tidak runtuh
val len = nickname?.length ?: 0   // Elvis operator: jika null beri nilai lalai
println(len)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Perhatian: Jangan Tertukar antara ? dan ?:

{class="mt-1"}
String? bermaksud 'dibenarkan kosong', a ?: b bermaksud 'jika a kosong guna b' (bentuknya mirip gaya rambut Elvis, sebab itu dipanggil operator Elvis). Ketika mula menulis kod, jika kompiler melaporkan 'ralat berkaitan null', kebarangkalian besar anda terlupa mengendalikan jenis boleh kosong — itulah bahasa itu sedang melindungi anda.
:::

#### 5. Kelas dan Objek: Acuan Pembuat 'Komponen'

Kelas ialah 'acuan' objek, objek ialah 'hasil siap' kelas. Segala benda dalam Android — halaman, butang, data — semuanya objek. Dalam Kotlin ada senjata ajaib dipanggil data class (kelas data), khusus untuk 'memuat data'; satu baris setara puluhan baris Java:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Kelas dan data class</span><span class="dots">···</span>
:::

```
// Kelas biasa: acuan
class Dog(val name: String) {
    fun bark() = println("$name menyalak!")
}

val dog = Dog("Anggor")      // Buat objek
dog.bark()                 // Anggor menyalak!

// data class: kotak penyimpan data (automatik ada equals/copy dll.)
data class User(val id: Int, val name: String, val email: String)

val me = User(1, "Zhang San", "zhangsan@example.com")
val twin = me.copy(name = "Zhang Sanfeng")   // Salin sambil ubah satu medan
```
:::

Kelak apabila anda membina buku perakaunan, setiap rekod ialah satu data class: data class Record(val amount: Double, val category: String, val date: String). Tengok, anda sudah mampu menulis struktur kod projek sebenar.

#### 6. Lambda dan Fungsi Peringkat Tinggi: 'Gula Sintaks' Kotlin

Dalam kod Android anda akan melihat { ... } 'fungsi tanpa nama' ini setiap hari; ia dipanggil lambda (fungsi tanpa nama). onClick = { count++ } pada Button ialah satu lambda — membungkus 'apa yang dilakukan selepas ditekan' menjadi satu bungkusan dan menyerahkannya kepada butang.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Pengenalan lambda</span><span class="dots">···</span>
:::

```
// Cara biasa: takrifkan fungsi bernama dahulu, kemudian hantar
fun double(x: Int) = x * 2
val result = listOf(1, 2, 3).map(::double)

// Gaya lambda: takrif terus di situ, ringkas
val result2 = listOf(1, 2, 3).map { it * 2 }   // it = elemen semasa

// Tapis + ubah berantai (sangat biasa dalam projek sebenar)
val bills = listOf(12.5, 88.0, 5.0, 200.0)
val bigBills = bills.filter { it > 50 }.sorted()
// [88.0, 200.0]—"bil melebihi 50, disusun kemas"
```
:::

Ingat beberapa 'gabungan koleksi' yang kerap digunakan: filter (menapis), map (menukar), sorted (menyusun), sum (menjumlah). 90% pemprosesan senarai anda kelak ialah gabungan empat cara ini. Falsafah Kotlin: logik yang boleh dijelaskan dengan satu ayat, jangan sesekali tulis lima ayat.

#### 7. Kad Rujukan Pantas Tatabahasa untuk Pemula

Jangan cuba menghafal semua tatabahasa dalam sehari. Simpan kad ini, rujuk semasa menulis kod; selepas dua minggu ia menjadi semula jadi:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Apa yang mahu dibuat</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Cara menulis</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Takrif pemboleh ubah baca sahaja</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">val x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Takrif pemboleh ubah boleh berubah</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">var x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Takrif fungsi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">fun nama(parameter): jenisPulangan { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menilai</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if (syarat) {...} else {...}</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Berbilang cabang</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">when { syarat -> hasil }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lalui senarai</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">for (x in senarai) { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cantuman rentetan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"Hai, $name"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Urus nilai kosong</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">x?.length ?: 0</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Takrif kelas data</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">data class X(val a: Int, val b: String)</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Kad rujukan pantas tatabahasa Kotlin (versi pemula)

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mari cuba: Tanpa memasang sebarang perisian, bermain Kotlin 10 minit dahulu

{class="mt-1"}
Buka play.kotlinlang.org dalam pelayar (taman permainan dalam talian rasmi Kotlin), tampal dan jalankan setiap kod dalam bab ini, ubah suai nombor dan teks, dan lihat bagaimana output berubah. 10 minit 'bermain dahulu, belajar kemudian' ini akan memudahkan anda dua kali ganda apabila memulakan Bab 51.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan Bab

- Utamakan val, guna var dengan berhati-hati; jenis boleh disimpulkan secara automatik, atau diisytiharkan secara jelas selepas usus besar
- Fungsi = logik yang dibungkus; templat rentetan $ ialah kemudahan khas
- Menilai dengan if/when, mengulang dengan for; when ialah 'serba boleh' dalam pembangunan Android
- Keselamatan null penyelamat nyawa Kotlin: jenis biasa menolak null, jenis boleh kosong mesti dikendalikan dengan ? / ?:
- data class ialah kotak penyimpan data, satu medan satu baris, digunakan setiap hari dalam projek sebenar
- 20% tatabahasa buat 80% kerja: boleh guna dahulu, mahir kemudian
:::
