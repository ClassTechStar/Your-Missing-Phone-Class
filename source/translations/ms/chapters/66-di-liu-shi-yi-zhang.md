---
id: di-liu-shi-yi-zhang
num: 61
part: ios-kai-fa-pian
nav: Bab 61: Kilat Swift—Bahasa Pertama Pembangunan Apple
toc: default
kind: chapter
---

### Bab 61: Pengenalan pantas Swift — bahasa utama pembangunan Apple

{class="chapter-intro mb-4"}
Dalam bab ini kita belajar bahasa secara rasmi. Jangan bimbang — Swift terkenal "mesra pemula", dan anda tidak perlu menghafal buku tatabahasa: kuasai dahulu 20% tatabahasanya, dan anda sudah boleh memahami serta menulis 80% kod harian. Sisanya dirujuk sambil membuat projek. Ingat prinsip pembelajaran kita: memahami > menghafal, boleh guna > mahir.

#### 1. Pemboleh ubah dan jenis: memberi nama kepada data

Program ialah "data + logik". Pemboleh ubah ialah memberi nama kepada data dan menyimpannya. Swift mengisytiharkan dengan let dan var:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Pemboleh ubah</span><span class="dots">···</span>
:::

```
let name = "Zhang San"        // let: pemalar (digalakkan sebagai lalai)
var age = 18             // var: pemboleh ubah (boleh diubah kemudian)

age = 19                 // <i class="fas fa-check-circle mr-1"></i> var boleh diubah
// name = "Li Si"         // <i class="fas fa-times-circle mr-1"></i> let tidak boleh diubah, ralat semasa kompilasi

let score: Int = 100     // juga boleh tulis jenisnya secara jelas
let pi = 3.14            // tidak ditulis pun boleh dikesan automatik

print("Hai, \(name)")   // interpolasi rentetan: tanda kembar + kurungan
```
:::

Ingat jenis-jenis biasa melalui satu jadual:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Jenis</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Menyimpan apa</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Contoh</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Int</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Integer</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">42</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Double</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Perpuluhan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3.14</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">String</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Teks</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"Hai"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bool</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Benar/Salah</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">true / false</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">[Int] (tatasusunan)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sekumpulan data</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">[1, 2, 3]</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Jenis asas biasa Swift

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Petua: prinsip utamakan let

{class="mt-1"}
Peraturan besi komuniti Swift: secara lalai gunakan let, gunakan var hanya jika benar-benar perlu. Jika anda menggunakan var di tempat yang boleh menggunakan let, Xcode akan memberi amaran berwarna kuning. Kebiasaan ini membantu anda mengelakkan satu kategori besar bug "pemboleh ubah diubah tanpa sengaja" — semakin sedikit perubahan dalam kod, semakin mudah ia ditadbir.
:::

#### 2. Optional: "azimat anti-ranap" Swift

Ini konsep paling penting dalam Swift, tiada tandingan. Ringkasnya: apabila sesuatu nilai mungkin "tiada", Swift memaksa anda mengendalikannya — membasmi "ranapan penunjuk kosong", mimpi ngeri industri ini, pada peringkat bahasa.

::: div .code-block
:::inline div .code-head
<span>SWIFT · Optional</span><span class="dots">···</span>
:::

```
var name: String = "Zhang San"   // Jenis biasa: langsung tidak boleh nil
// name = nil                // <i class="fas fa-times-circle mr-1"></i> Ditahan terus oleh pengkompil

var nickname: String? = nil  // beri tanda soal: membenarkan nil (optional)
nickname = "San Er"

// Guna optional mesti "buka bungkusnya" dahulu:
if let n = nickname {        // if let: buka bungkus dengan selamat
    print("Hai, \(n)")
} else {
    print("Belum ada nama panggilan")
}

let len = nickname?.count ?? 0   // ?? memberi nilai lalai (nil coalescing)
print(len)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Perhatian: ! ialah "tindakan berisiko tinggi"

{class="mt-1"}
Menulis nickname! (pembungkusan paksa) dalam kod sama seperti menjerit kepada pengkompil "saya jamin ia bukan nil" — sekali tersalah teka, aplikasi terus ranap. Prinsip zaman pemula: gunakan if let / ?? sebanyak mungkin, jangan guna !. Semasa Xcode melengkapkan kod, kadangkala ia menambah ! tanpa sengaja; ingat untuk membuangnya.
:::

#### 3. Fungsi dan penutupan (closure): membungkus logik menjadi "butang"

Fungsi ialah sepotong logik yang bernama, seperti butang pada alat kawalan jauh. Penutupan (Closure) pula ialah "fungsi tanpa nama", boleh diserahkan kepada orang lain pada bila-bila masa:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Fungsi dan closure</span><span class="dots">···</span>
:::

```
// Fungsi: nama di hadapan, parameter dan jenis pemulangan di belakang
func greet(name: String) -> String {
    return "Hai, \(name)!"
}
print(greet(name: "Zhang San"))     // Semasa memanggil mesti nyatakan nama parameter

// Closure: takrif terus di situ, ringkas
let numbers = [1, 2, 3, 4]
let doubled = numbers.map { $0 * 2 }   // $0 = elemen semasa
// [2, 4, 6, 8]

let big = numbers.filter { $0 > 2 }    // Tapisan
// [3, 4]
```
:::

Dalam SwiftUI, penutupan ada di mana-mana: kurungan kerinting selepas Button("Tekan saya") { ... } ialah sebuah penutupan. Hafalkan "kombinasi koleksi" seperti map, filter dan sorted — 90% pemprosesan senarai pada masa hadapan ialah gabungan ketiga-tiganya.

#### 4. Struct dan protokol: sistem "Lego" Swift

Keutamaan rasmi Swift jelas: utamakan struct, gunakan class hanya apabila perlu pewarisan. Struct ialah "jenis nilai" — apabila disalin, masing-masing bergerak sendiri; secara semula jadi mengurangkan satu kategori bug:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Struct dan protocol</span><span class="dots">···</span>
:::

```
// Struct: kotak penyimpan data
struct Record {
    var id = UUID()
    var amount: Double
    var category: String
    var date: Date

    // Struct ada "memberwise initializer" sendiri: terus boleh dicipta
}
let r = Record(amount: 25.5, category: "Makanan", date: Date())

// Protocol: persetujuan "keupayaan apa yang wajib ada"
protocol Identifiable {
    var id: UUID { get }
}
struct Record: Identifiable { ... }   // Mematuhi protocol = berjanji melaksanakan tuntutannya
```
:::

Dalam SwiftUI, hampir semuanya ialah struct (View ialah protokol). Jika belum faham ayat ini sekarang, tidak mengapa — Bab 62 akan bertemu dengannya setiap hari. Dalam dunia Swift, peluk struct dahulu.

#### 5. Kad rujukan pantas tatabahasa untuk yang tiada asas

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Apa yang mahu dibuat</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Cara menulis</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Takrifkan pemalar/pemboleh ubah</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">let x = 1</code> / <code class="inline">var x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Interpolasi rentetan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"Hai, \(name)"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Takrifkan fungsi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">func nama(parameter: jenis) -> jenisPulangan { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Percabangan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if syarat { ... } else { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ulangan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">for x in tatasusunan { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ungkai nilai dengan selamat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if let x = nilai pilihan { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Nilai lalai</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">x ?? nilai lalai</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Takrifkan struktur (struct)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">struct X { var a: Int; var b: String }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Closure</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">{ $0 * 2 }</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Kad rujukan pantas sintaks Swift (edisi pemula)

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Praktik: Mainkan Swift 15 minit dalam Playgrounds

{class="mt-1"}
Ada Mac? Buka Xcode → Playground; tiada Mac? Guna Swift Playgrounds di iPad atau tapak web latihan. Jalankan setiap kod dalam bab ini, ubah-ubah nombor dan teks, dan sengaja buat beberapa ralat untuk melihat cara Xcode memberi amaran. 15 minit 'main dahulu, belajar kemudian' ini akan memudahkan anda dua kali ganda apabila memulakan Bab 62.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan bab ini

- Utamakan let, guna var dengan berhati-hati; jenis dikesan secara automatik, tetapi anda juga boleh nyatakan secara jelas selepas titik bertindih (:)
- Nilai pilihan ialah jiwa Swift: nilai yang mungkin kosong mesti diproses, if let / ?? ialah azimat pelindung anda, manakala ! ialah operasi berisiko tinggi
- Panggilan fungsi perlu sertakan nama parameter; closure = fungsi tanpa nama, dan ia ada di mana-mana dalam SwiftUI
- Utamakan struct dan patuhi protokol (protocol); hampir semua perkara dalam SwiftUI ialah struct
- 20% sintaks menanggung 80% kerja: kuasai penggunaan dahulu, kemudian barulah mendalami
:::
