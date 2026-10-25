---
id: di-liu-shi-yi-zhang
num: 61
part: ios-kai-fa-pian
nav: Bab 61: Kilat Swift—Bahasa Utama Pengembangan Apple
toc: default
kind: chapter
---

### Bab 61: Kilat Mengenal Swift — Bahasa Pertama Pengembangan Apple

{class="chapter-intro mb-4"}
Di bab ini kita resmi belajar bahasanya. Jangan tegang — Swift terkenal "ramah pemula", dan kamu tak perlu menghafal buku sintaks: kuasai dulu 20% sintaksnya, kamu sudah bisa membaca dan menulis 80% kode sehari-hari. Sisanya dicari sambil mengerjakan proyek. Ingat prinsip belajar kita: pahami > hafalkan, bisa pakai > mahir.

#### 1. Variabel dan tipe: Memberi nama pada data

Program adalah "data + logika". Variabel adalah memberi nama pada data agar tersimpan. Swift mendeklarasikannya dengan let dan var:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Variabel</span><span class="dots">···</span>
:::

```
let name = "Zhang San"        // let: konstanta (disarankan jadi default)
var age = 18             // var: variabel (masih bisa diubah)

age = 19                 // <i class="fas fa-check-circle mr-1"></i> var bisa diubah
// name = "Li Si"         // <i class="fas fa-times-circle mr-1"></i> let tidak bisa diubah, error saat kompilasi

let score: Int = 100     // juga bisa menuliskan tipenya secara eksplisit
let pi = 3.14            // tidak ditulis pun otomatis terdeteksi

print("Halo, \(name)")   // interpolasi string: backslash + tanda kurung
```
:::

Tipe yang sering dipakai, cukup dihafal dengan satu tabel:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Tipe</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Menyimpan apa</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Contoh</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Int</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bilangan bulat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">42</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Double</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bilangan desimal</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3.14</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">String</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Teks</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"Halo"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bool</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Benar/salah</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">true / false</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">[Int] (array)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sekumpulan data</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">[1, 2, 3]</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Tipe dasar Swift yang sering dipakai

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tips: Prinsip utamakan let

{class="mt-1"}
Hukum besi komunitas Swift: bawaannya pakai let, var baru kalau memang perlu. Memakai var di tempat yang bisa let akan kena peringatan kuning dari Xcode. Kebiasaan ini menghilangkan satu kelas besar bug "variabel berubah tanpa sengaja" — makin sedikit kode yang bisa berubah, makin mudah ditelusuri.
:::

#### 2. Optional: "Jimat anti-crash" milik Swift

Ini konsep terpenting Swift, tanpa pesaing. Satu kalimat: saat sebuah nilai mungkin "tak ada", Swift memaksamu menanganinya — menghapus "crash null pointer", mimpi buruk industri ini, dari level bahasa.

::: div .code-block
:::inline div .code-head
<span>SWIFT · Optional</span><span class="dots">···</span>
:::

```
var name: String = "Zhang San"   // Tipe biasa: sama sekali tidak boleh nil
// name = nil                // <i class="fas fa-times-circle mr-1"></i> Ditemukan langsung oleh compiler

var nickname: String? = nil  // beri tanda tanya: mengizinkan nil (optional)
nickname = "San Er"

// Memakai optional wajib "membungkusnya dibuka":
if let n = nickname {        // if let: membuka dengan aman
    print("Halo, \(n)")
} else {
    print("Belum ada nama panggilan")
}

let len = nickname?.count ?? 0   // ?? memberi nilai default (nil coalescing)
print(len)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Perhatian: ! adalah "operasi berisiko tinggi"

{class="mt-1"}
Menulis nickname! di kode (forced unwrap) sama saja berteriak ke compiler "saya jamin ini bukan nil" — begitu tebakanmu salah, App langsung crash. Prinsip masa pemula: sebisa mungkin pakai if let / ??, jangan pakai !. Saat melengkapi kode, Xcode kadang iseng menyisipkan ! sekalian — ingat untuk menghapusnya.
:::

#### 3. Fungsi dan closure: Mengemas logika menjadi "tombol"

Fungsi adalah logika yang punya nama, seperti tombol di remote. Closure adalah "fungsi tanpa nama" yang bisa langsung disodorkan ke pihak lain:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Fungsi dan closure</span><span class="dots">···</span>
:::

```
// Fungsi: nama di depan, parameter dan tipe kembalian di belakang
func greet(name: String) -> String {
    return "Halo, \(name)!"
}
print(greet(name: "Zhang San"))     // Saat memanggil harus menyebut nama parameter

// Closure: didefinisikan di tempat, ringkas
let numbers = [1, 2, 3, 4]
let doubled = numbers.map { $0 * 2 }   // $0 = elemen saat ini
// [2, 4, 6, 8]

let big = numbers.filter { $0 > 2 }    // Menyaring
// [3, 4]
```
:::

Di SwiftUI closure ada di mana-mana: kurung kurawal setelah Button("Tekan aku") { ... } adalah sebuah closure. Hafalkan baik-baik "kombinasi jurus" koleksi: map, filter, sorted — 90% pengolahan daftar kelak adalah gabungan ketiganya.

#### 4. Struct dan protokol: Sistem "LEGO"-nya Swift

Preferensi resmi Swift jelas: utamakan struct (structure), pakai class baru saat butuh pewarisan. Struct adalah "value type" — saat disalin masing-masing jalan sendiri, alami bebas dari satu kelas bug:

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

    // Struct punya "memberwise initializer" bawaan: langsung bisa dibuat
}
let r = Record(amount: 25.5, category: "Makan", date: Date())

// Protocol: kesepakatan "kemampuan apa saja yang wajib dimiliki"
protocol Identifiable {
    var id: UUID { get }
}
struct Record: Identifiable { ... }   // Mengikuti protocol = berjanji mengimplementasikan tuntutannya
```
:::

Di SwiftUI hampir semuanya struct (View adalah protokol). Belum paham kalimat ini tidak apa-apa — kamu akan bertemu terus di Bab 62; di dunia Swift, peluk dulu struct.

#### 5. Kartu cepat sintaks untuk kamu yang nol dasar

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ingin melakukan apa</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Cara menulis</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mendefinisikan konstanta/variabel</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">let x = 1</code> / <code class="inline">var x = 1</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Interpolasi string</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">"Halo, \(name)"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mendefinisikan fungsi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">func nama(parameter: Tipe) -> TipeHasil { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Percabangan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if kondisi { ... } else { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Perulangan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">for x in array { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Unwrap aman</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">if let x = nilaiOpsional { ... }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Nilai default</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">x ?? nilaiDefault</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mendefinisikan struct</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">struct X { var a: Int; var b: String }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Closure</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">{ $0 * 2 }</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Kartu contekan sintaks Swift (versi pemula)

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Praktik: Bermain Swift 15 Menit di Playgrounds

{class="mt-1"}
Punya Mac? Buka Xcode → Playground; belum punya Mac? Gunakan Swift Playgrounds di iPad atau berlatih di versi web di browser. Jalankan setiap potongan kode di bab ini, ubah-ubah angka dan teksnya, dan sengaja buat beberapa kesalahan untuk melihat bagaimana Xcode memberi peringatan. Lima belas menit "bermain dulu, belajar kemudian" ini akan membuat kamu dua kali lebih mudah saat memulai Bab 62.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan Bab Ini

- Utamakan let, hati-hati dengan var; tipe diinferensi otomatis, boleh juga dideklarasikan eksplisit setelah titik dua
- Nilai opsional adalah jiwa Swift: yang bisa kosong wajib ditangani, if let / ?? adalah jimat penyelamat, dan ! adalah operasi berisiko tinggi
- Pemanggilan fungsi harus menyertakan nama parameter; closure = fungsi tanpa nama, ada di mana-mana di SwiftUI
- Utamakan struct, ikuti protokol (Protocol); hampir semua di SwiftUI adalah struct
- 20% sintaks mengerjakan 80% pekerjaan: kuasai dulu cara pakainya, baru dalami
:::
