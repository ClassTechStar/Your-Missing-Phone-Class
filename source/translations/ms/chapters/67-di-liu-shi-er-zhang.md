---
id: di-liu-shi-er-zhang
num: 62
part: ios-kai-fa-pian
nav: Bab 62: Pembangunan Antara Muka—Pengenalan SwiftUI
toc: default
kind: chapter
---

### Bab 62: Pembangunan Antara Muka — Pengenalan SwiftUI

{class="chapter-intro mb-4"}
Antara muka ialah segala yang dilihat oleh pengguna. SwiftUI ialah rangka kerja antara muka jenis deklaratif yang dikeluarkan Apple pada 2019 — anda hanya perlu 'menyatakan' bentuk antara muka, dan sistem yang menguruskan pemaparan, penyesuaian mod gelap serta pelbagai saiz skrin secara automatik. Menjelang 2026, SwiftUI sudah menjadi arus perdana mutlak untuk projek baharu. Dalam bab ini, kita belajar 'melukis'.

#### 1. Falsafah SwiftUI: deklaratif, bukan imperatif

Pembangunan antara muka lama bersifat 'imperatif': anda memberitahu sistem 'cipta butang → letak di (20,30) → tetapkan warna' langkah demi langkah seperti mengarahkan. SwiftUI bersifat 'deklaratif': anda hanya menerangkan 'di atas skrin ada butang merah bertulis "Klik saya"', dan bagaimana melukisnya serta bila melukis semula menjadi urusan sistem.

::: div .code-block
:::inline div .code-head
<span>SWIFT · View SwiftUI pertama</span><span class="dots">···</span>
:::

```
import SwiftUI

struct ContentView: View {
    var body: some View {      // body: menggambarkan "rupawan paparan"
        VStack {               // disusun menegak
            Text("Hai, dunia!")
                .font(.largeTitle)      // modifier: tajuk besar
            Button("Tekan saya") {
                print("Ditekan")
            }
            .buttonStyle(.borderedProminent)  // butang pejal biru
        }
        .padding()
    }
}
```
:::

Perkara utama: view = struktur yang mematuhi protokol View, sifat body menerangkan antara muka, dan modifier dirantai seperti 'memakaikan solek'. Inilah seluruh asas SwiftUI.

#### 2. View asas: teks, butang, medan input, imej

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">View</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Fungsinya</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Contoh</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Paparkan teks</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text("Halo")</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Butang</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button("Klik saya") { tindakan }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Medan input</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField("Petunjuk", text: $teks)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Image</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Paparkan imej</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Image(systemName: "star.fill")</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Empat view asas utama SwiftUI

Perhatikan Image(systemName:) — Apple menyediakan pustaka ikon terbina dalam SF Symbols (beribu-ribu ikon percuma); nama seperti "star.fill" terus memaparkan ikon bintang penuh. Inilah faedah tersembunyi pembangunan iOS: membina antara muka hampir tidak memerlukan carian bahan ikon.

#### 3. Tiga alat susun atur: VStack, HStack, ZStack

- VStack: disusun menegak (seperti beratur mengambil makanan);
- HStack: disusun mengufuk (seperti duduk bersebelahan);
- ZStack: ditindihkan (seperti kad poker disusun bertindih — sesuai untuk lencana dan lapisan tonjolan).

::: div .code-block
:::inline div .code-head
<span>SWIFT · Set tiga susun atur + modifier kerap guna</span><span class="dots">···</span>
:::

```
VStack(alignment: .leading, spacing: 12) {
    HStack {
        Text("Bil")
        Spacer()                 // Ruang kenyal: tolak bahagian kanan sampai hujung
        Text("-25.5 yuan").foregroundColor(.red)
    }
    Divider()                    // Garis pembahagi
    Text("Nota: makan tengah hari")
}
.padding(16)                     // beri ruang sekeliling
.background(Color(.systemGray6)) // latar kelabu muda
.cornerRadius(12)                // bucu bulat

// Susunan modifier berpengaruh: padding dahulu baru background, latar tidak merangkumi jarak padding
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Perhatian: susunan modifier mempengaruhi hasil

{class="mt-1"}
padding(16).background(kelabu) dan background(kelabu).padding(16) memberi hasil berbeza — yang pertama 'beri ruang dahulu, barulah warnakan' (latar belakang tidak merangkumi ruang tepi), yang kedua 'warnakan dahulu, barulah beri ruang' (latar belakang merangkumi ruang tepi). 'Jalur putih pelik' yang paling kerap mengelirukan pemula berpunca dari sini. Jika tidak pasti, tukar sahaja susunannya dan pratonton akan terus memberi jawapan.
:::

#### 4. Negeri (state) dan pengikatan: membuat antara muka 'hidup'

Antara muka statik membosankan. Peraturan SwiftUI: antara muka sentiasa mencerminkan state dengan setia; state berubah, antara muka dilukis semula secara automatik.

::: div .code-block
:::inline div .code-head
<span>SWIFT · Pengira @State</span><span class="dots">···</span>
:::

```
struct CounterView: View {
    @State private var count = 0   // @State: bila nilai ini berubah, lukis semula

    var body: some View {
        VStack {
            Text("Anda menekan \(count) kali")
            Button("Tekan saya +1") {
                count += 1          // ubah state, paparan terus segar
            }
        }
    }
}
```
:::

Medan input perlu "pengikatan dua hala" — simbol $ menghantar "nilai dan kuasa mengubahnya" bersama-sama:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Ikatan dua hala @Binding</span><span class="dots">···</span>
:::

```
struct InputView: View {
    @State private var text = ""

    var body: some View {
        TextField("Taip sesuatu", text: $text)  // ikatan dua hala dengan $
            .textFieldStyle(.roundedBorder)
        Text("Anda menaip: \(text)")   // terkini semasa menaip
    }
}
```
:::

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hand-pointer mr-1"></i> Tindakan pengguna</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> State berubah (count += 1)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> SwiftUI mengesan perubahan</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> Lukis semula paparan automatik (body dikira semula)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Rajah 3: Aliran data sehala "state → antara muka" dalam SwiftUI
:::

#### 5. Pratonton, tema dan animasi: 'tambahan luar' SwiftUI

- Makro #Preview: tambah #Preview { ContentView() } di bahagian bawah fail, dan kanvas di sebelah kanan memaparkan hasil secara masa nyata — ubah kod, apa yang dilihat itulah yang diperoleh;
- Mod gelap percuma: gunakan warna sistem (Color(.systemGray6), .primary) dan bukannya warna tetap; mod gelap disesuaikan secara automatik tanpa satu baris tambahan;
- Animasi selesai dalam satu baris: withAnimation { count += 1 } atau tambah .animation(.default, value: count) pada view — peralihan menjadi lancar.

::: div .code-block
:::inline div .code-head
<span>SWIFT · Animasi dikuasai dalam 10 minit</span><span class="dots">···</span>
:::

```
struct AnimatedHeartView: View {
    @State private var liked = false

    var body: some View {
        Button {
            withAnimation(.spring(duration: 0.4)) {
                liked.toggle()
            }
        } label: {
            Image(systemName: liked ? "heart.fill" : "heart")
                .font(.system(size: 48))
                .foregroundColor(liked ? .red : .gray)
                .scaleEffect(liked ? 1.3 : 1.0)
        }
    }
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Petua: Fungsi dahulu, animasi kemudian

{class="mt-1"}
Masalah lazim pemula ialah 'antara muka belum betul, tetapi sibuk memikirkan animasi'. Pastikan fungsi berjalan dahulu, tambahkan kesan animasi secara menyeluruh di hujungnya — animasi hanyalah sentuhan hiasan, manakala fungsi ialah keperluan yang menyelamatkan. Ini juga selaras dengan prinsip kita sepanjang buku ini: 'kesederhanaan di atas segalanya'.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Praktik: Bina 'butang mood'

#### 6. Rujukan pantas modifier lazim: satu halaman dalam tangan, antara muka tak jadi masalah

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Apa yang mahu dibuat</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Modifier</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ruang tepi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.padding(16)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sudut bulat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.cornerRadius(12)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Warna latar belakang</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.background(Color(.systemGray6))</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Fon dan saiz fon</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.font(.title.bold())</code> / <code class="inline">.font(.system(size: 20))</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Warna latar depan (teks/ikon)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.foregroundColor(.red)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Rapatkan penuh lebar</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.frame(maxWidth: .infinity)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Saiz tetap</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.frame(width:100, height: 44)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Penjajaran</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">VStack(alignment: .leading)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kelegapan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.opacity(0.6)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bayang</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.shadow(radius: 5)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gerak ketikan (tap)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.onTapGesture { ... }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Jenis papan kekunci</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.keyboardType(.decimalPad)</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Rujukan pantas modifier lazim SwiftUI

Tidak apa-apa jika tidak dapat diingat — halaman ini memang untuk dirujuk. Yang paling kerap digunakan sebenarnya hanya empat yang pertama: padding, sudut bulat, latar belakang dan fon.

{class="mt-1"}
Ubah projek templat menjadi penukar mood: satu butang yang apabila ditekan berkitar antara 😀 gembira → 😢 sedih → 😡 marah, teks dan warna latar berubah mengikutnya. Petunjuk: gunakan tatasusunan untuk menyimpan tiga set (teks + warna), @State untuk menyimpan indeks, dan (index + 1) % 3 semasa ditekan. Selepas siap, hantar kepada rakan untuk dimainkan dan terimalah gelombang pertama 'wow, anda sudah boleh buat App'.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan bab ini

- SwiftUI bersifat deklaratif: anda menerangkan 'bentuknya', sistem yang melukis dan melukis semula
- View = struktur yang mematuhi protokol View; body menerangkan antara muka; modifier dirantai seperti 'memakaikan solek'
- Empat view asas: Text / Button / TextField / Image; pustaka ikon SF Symbols percuma dan lengkap
- Tiga alat susun atur: VStack menegak, HStack mengufuk, ZStack bertindih; Spacer ialah ruang fleksibel
- @State menghidupkan antara muka; $ mengikat dua hala untuk disuapkan ke medan input
- #Preview — apa dilihat itulah yang diperoleh; warna sistem menyesuaikan mod gelap secara automatik; withAnimation memberi kesan animasi dalam satu baris
:::
