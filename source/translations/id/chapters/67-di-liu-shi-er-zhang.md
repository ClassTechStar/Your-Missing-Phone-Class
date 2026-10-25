---
id: di-liu-shi-er-zhang
num: 62
part: ios-kai-fa-pian
nav: Bab 62: Pengembangan Antarmuka—Pengenalan SwiftUI
toc: default
kind: chapter
---

### Bab 62: Pengembangan Antarmuka — Pengenalan SwiftUI

{class="chapter-intro mb-4"}
Antarmuka adalah segala sesuatu yang dilihat pengguna. SwiftUI adalah framework antarmuka deklaratif yang diperkenalkan Apple pada 2019 — kamu cukup "mendeklarasikan" seperti apa tampilan antarmukanya, dan sistem otomatis menangani render, adaptasi dark mode, serta penyesuaian ke berbagai ukuran layar. Pada 2026, SwiftUI sudah menjadi arus utama mutlak untuk proyek baru. Di bab ini, kita belajar "menggambar".

#### 1. Gagasan SwiftUI: Deklaratif, Bukan Imperatif

Pengembangan antarmuka gaya lama bersifat "imperatif": kamu mengarahkan sistem langkah demi langkah — "buat tombol → taruh di (20,30) → atur warna". SwiftUI bersifat "deklaratif": kamu cukup mendeskripsikan "di layar ada tombol merah bertuliskan 'Klik Aku'", lalu bagaimana menggambarnya dan kapan menggambar ulang menjadi urusan sistem sendiri.

::: div .code-block
:::inline div .code-head
<span>SWIFT · View SwiftUI pertama</span><span class="dots">···</span>
:::

```
import SwiftUI

struct ContentView: View {
    var body: some View {      // body: mendeskripsikan "wujud tampilan"
        VStack {               // disusun vertikal
            Text("Halo, dunia!")
                .font(.largeTitle)      // modifier: judul besar
            Button("Tekan aku") {
                print("Ditekan")
            }
            .buttonStyle(.borderedProminent)  // tombol solid biru
        }
        .padding()
    }
}
```
:::

Poin kunci: view = struct yang mengikuti protokol View, properti body mendeskripsikan antarmuka, dan .modifier() menyusun "make-up" secara berantai. Inilah seluruh fondasi dasar SwiftUI.

#### 2. View Dasar: Teks, Tombol, Kolom Input, Gambar

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">View</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Fungsi</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Contoh</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menampilkan teks</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text("Halo")</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tombol</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button("Klik Aku") { aksi }</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kolom input</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField("Petunjuk", text: $teks)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Image</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menampilkan gambar</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">Image(systemName: "star.fill")</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Empat view dasar SwiftUI

Perhatikan Image(systemName:) — Apple menyediakan pustaka ikon bawaan SF Symbols (ribuan ikon gratis), dan nama seperti "star.fill" langsung menampilkan bintang penuh. Ini bonus tersembunyi pengembangan iOS: membuat antarmuka hampir tidak perlu mencari aset ikon.

#### 3. Trio Layout: VStack, HStack, ZStack

- VStack: tersusun vertikal (seperti antre mengambil makanan di kantin);
- HStack: tersusun horizontal (seperti duduk berjajar);
- ZStack: ditumpuk (seperti kartu remi ditumpuk, cocok untuk badge dan overlay).

::: div .code-block
:::inline div .code-head
<span>SWIFT · Trio layout + modifier yang sering dipakai</span><span class="dots">···</span>
:::

```
VStack(alignment: .leading, spacing: 12) {
    HStack {
        Text("Tagihan")
        Spacer()                 // Ruang elastis: mendorong kanan sampai ujung
        Text("-25.5 yuan").foregroundColor(.red)
    }
    Divider()                    // Garis pemisah
    Text("Catatan: makan siang")
}
.padding(16)                     // beri ruang di sekeliling
.background(Color(.systemGray6)) // latar abu muda
.cornerRadius(12)                // sudut membulat

// Urutan modifier berpengaruh: padding dulu baru background, latar tidak termasuk jarak padding
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Perhatian: Urutan modifier berpengaruh

{class="mt-1"}
padding(16).background(abu) dan background(abu).padding(16) hasilnya berbeda — yang pertama "memberi jarak dulu, lalu mewarnai" (latar tidak termasuk jarak), yang kedua "mewarnai dulu, lalu memberi jarak" (latar termasuk jarak). "Garis putih aneh" yang paling sering membingungkan pemula berasal dari sini. Kalau ragu, tukar saja urutannya — pratinjau langsung memberi jawaban.
:::

#### 4. State dan Binding: Menghidupkan Antarmuka

Antarmuka statis itu membosankan. Aturan SwiftUI: antarmuka selalu setia mencerminkan state; begitu state berubah, antarmuka otomatis digambar ulang.

::: div .code-block
:::inline div .code-head
<span>SWIFT · Penghitung @State</span><span class="dots">···</span>
:::

```
struct CounterView: View {
    @State private var count = 0   // @State: saat nilai ini berubah, gambar ulang

    var body: some View {
        VStack {
            Text("Kamu menekan \(count) kali")
            Button("Tekan aku +1") {
                count += 1          // ubah state, tampilan menyegarkan sendiri
            }
        }
    }
}
```
:::

Kolom input memakai "binding dua arah" — simbol $ mengirimkan "nilai beserta hak mengubahnya" sekaligus:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Binding dua arah @Binding</span><span class="dots">···</span>
:::

```
struct InputView: View {
    @State private var text = ""

    var body: some View {
        TextField("Ketik sesuatu", text: $text)  // binding dua arah dengan $
            .textFieldStyle(.roundedBorder)
        Text("Kamu mengetik: \(text)")   // ter-update langsung saat mengetik
    }
}
```
:::

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hand-pointer mr-1"></i> Aksi pengguna</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> State berubah (count += 1)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> SwiftUI mendeteksi perubahan</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> Menggambar ulang tampilan otomatis (body dihitung ulang)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Gambar 3: Aliran data satu arah "state → antarmuka" pada SwiftUI
:::

#### 5. Pratinjau, Tema, dan Animasi: "Senjata Ampuh" SwiftUI

- Makro #Preview: tambahkan #Preview { ContentView() } di bagian bawah file, dan kanvas di sebelah kanan langsung merender secara real-time — mengubah kode terlihat hasilnya saat itu juga;
- Dark mode gratis: gunakan warna sistem (Color(.systemGray6), .primary) alih-alih warna yang ditulis tetap; dark mode otomatis menyesuaikan tanpa kode tambahan;
- Animasi selesai dalam satu baris: withAnimation { count += 1 } atau tambahkan .animation(.default, value: count) pada view — transisinya mulus.

::: div .code-block
:::inline div .code-head
<span>SWIFT · Animasi yang dikuasai dalam 10 menit</span><span class="dots">···</span>
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
Tips: Fungsinya Dulu, Animasi Belakangan

{class="mt-1"}
Celah umum pemula adalah "antarmuka belum benar, tapi sudah sibuk memikirkan animasi". Pastikan fiturnya berjalan dulu, baru tambahkan efek gerak secara seragam di tahap akhir — animasi adalah hiasan pelengkap, fungsi adalah kebutuhan pokok. Ini juga sesuai prinsip kita selama ini: "kesederhanaan di atas segalanya".
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Praktik: Membuat "Tombol Suasana Hati"

#### 6. Contekan Modifier yang Sering Dipakai: Satu Halaman, Antarmuka Beres

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ingin melakukan apa</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Modifier</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Jarak sisi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.padding(16)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sudut membulat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.cornerRadius(12)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Warna latar</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.background(Color(.systemGray6))</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Font dan ukuran huruf</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.font(.title.bold())</code> / <code class="inline">.font(.system(size: 20))</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Warna latar depan (teks/ikon)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.foregroundColor(.red)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Memenuhi lebar</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.frame(maxWidth: .infinity)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ukuran tetap</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.frame(width:100, height: 44)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Perataan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">VStack(alignment: .leading)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Transparansi</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.opacity(0.6)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bayangan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.shadow(radius: 5)</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gerakan ketuk (tap)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.onTapGesture { ... }</code></td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Jenis keyboard</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><code class="inline">.keyboardType(.decimalPad)</code></td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Contekan modifier SwiftUI yang sering dipakai

Tidak apa-apa kalau tidak hafal — halaman ini memang untuk dibuka saat perlu. Yang paling sering dipakai sebenarnya hanya empat yang pertama: padding, sudut membulat, warna latar, dan font.

{class="mt-1"}
Ubah proyek templat menjadi pengganti suasana hati: satu tombol yang setiap diklik berganti siklus antara 😀 senang → 😢 sedih → 😡 marah, dengan teks dan warna latar ikut berubah. Petunjuk: simpan tiga pasangan (teks + warna) dalam array, simpan indeksnya di @State, dan saat diklik gunakan (index + 1) % 3. Setelah jadi, kirim ke teman untuk dicoba, dan rasakan gelombang pertama "wow kamu bisa bikin App".
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan Bab Ini

- SwiftUI bersifat deklaratif: kamu mendeskripsikan "tampilannya seperti apa", sistem yang menggambar dan menggambar ulang
- View = struct yang mengikuti protokol View; body mendeskripsikan antarmuka; modifier menyusun "make-up" berantai
- Empat view dasar: Text / Button / TextField / Image; pustaka ikon SF Symbols gratis sebanyak-banyaknya
- Trio layout: VStack vertikal, HStack horizontal, ZStack bertumpuk; Spacer adalah ruang elastis
- @State menghidupkan antarmuka; $ untuk binding dua arah ke kolom input
- #Preview hasilnya terlihat langsung; warna sistem otomatis menyesuaikan dark mode; withAnimation efek gerak satu baris
:::
