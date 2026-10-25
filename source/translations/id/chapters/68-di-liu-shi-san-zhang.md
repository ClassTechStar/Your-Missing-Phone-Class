---
id: di-liu-shi-san-zhang
num: 63
part: ios-kai-fa-pian
nav: Bab 63: View, State, dan Navigasi
toc: default
kind: chapter
---

### Bab 63: View, State, dan Navigasi

{class="chapter-intro mb-4"}
Membuat mainan satu halaman sudah bisa. Bab ini menyelesaikan dua masalah "tumbuh dewasa": bagaimana berpindah-pindah antar beberapa halaman (navigasi), dan bagaimana data mengalir antar halaman (manajemen state). Setelah menuntaskan bab ini, kamu bisa membangun kerangka App multi-halaman klasik seperti "daftar → detail → edit".

#### 1. Peta Besar Aliran Data dalam Manajemen State

Alat state di SwiftUI tidak hanya @State. Lihat dulu peta besarnya untuk memahami "kapan memakai yang mana":

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Alat</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Mengatur apa</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Dipakai oleh</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Skenario khas</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@State</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">State sementara privat satu halaman</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">View saat ini</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Penghitung, teks kolom input</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Binding</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Meminjam state milik view lain</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">View anak mengubah view induk</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Komponen kustom</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@StateObject / @Observable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Logika yang dibagi lintas halaman</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">View model (ViewModel)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pemuatan data, logika bisnis</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@EnvironmentObject / .environment</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">State yang dibagi secara global</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Seluruh App</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Status login pengguna, pengaturan tema</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Peta alat state SwiftUI (pada 2026, @Observable sudah menjadi arus utama)

::: div .code-block
:::inline div .code-head
<span>SWIFT · Arus utama 2026: view model @Observable</span><span class="dots">···</span>
:::

```
// Cara modern di iOS 17+: makro @Observable (disarankan untuk proyek baru)
import Observation

@Observable
class CounterModel {                 // View model
    var count = 0
    func increment() { count += 1 }
}

struct CounterView: View {
    @State private var model = CounterModel()   // Memegang model

    var body: some View {
        VStack {
            Text("Kamu menekan \(model.count) kali")
            Button("Tekan aku") { model.increment() }
        }
    }
}
```
:::

Saran blak-blakan untuk pemula: yang privat satu halaman pakai @State, yang lintas halaman/berisi logika pakai kelas @Observable. @StateObject/@ObservableObject di tutorial lama adalah gaya generasi sebelumnya — cukup pahami cara membacanya; untuk kode baru, ikuti panduan di atas.

#### 2. NavigationStack: "Tumpukan" untuk Pindah Halaman

Sejak iOS 16, navigasi multi-halaman memakai NavigationStack — seperti tumpukan piring: satu masuk, satu ditaruh; saat kembali, dikeluarkan satu per satu:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Navigasi NavigationStack</span><span class="dots">···</span>
:::

```
struct HomeView: View {
    var body: some View {
        NavigationStack {
            List {
                NavigationLink("Buku kas Zhang San") {
                    DetailView(name: "Buku kas Zhang San")   // halaman tujuan
                }
                NavigationLink("Buku kas Li Si") {
                    DetailView(name: "Buku kas Li Si")
                }
            }
            .navigationTitle("Daftar buku kas")   // judul besar di atas
        }
    }
}

struct DetailView: View {
    let name: String
    var body: some View {
        Text("Halaman detail \(name)")
            .navigationTitle(name)
            .navigationBarTitleDisplayMode(.inline)
    }
}
```
:::

NavigationLink adalah "tautan pindah halaman yang bisa diklik"; navigationTitle otomatis membuat judul bilah navigasi dan tombol kembali. Untuk pindah halaman secara terprogram (misalnya otomatis kembali setelah menekan "Simpan"), gunakan @Environment(\.dismiss) untuk menutup halaman saat ini — dengan dua cara ini digabung, 90% kebutuhan navigasi sudah tercakup.

#### 3. Popup dan Tab Bawah: sheet dan TabView

Selain "mendorong halaman", ada dua interaksi klasik lainnya:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Popup sheet + tab TabView</span><span class="dots">···</span>
:::

```
// 1. Pop setengah layar/layar penuh dari bawah (favorit formulir input)
struct HomeView: View {
    @State private var showAdd = false
    var body: some View {
        Button("Catat") { showAdd = true }
            .sheet(isPresented: $showAdd) {
                AddRecordView()     // Halaman input yang muncul
            }
    }
}

// 2. Bar tab bawah ("kerangka" aplikasi)
struct MainTabView: View {
    var body: some View {
        TabView {
            RecordListView()
                .tabItem { Label("Buku kas", systemImage: "book") }
            StatsView()
                .tabItem { Label("Statistik", systemImage: "chart.pie") }
            SettingsView()
                .tabItem { Label("Pengaturan", systemImage: "gear") }
        }
    }
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tips: Kapan Memakai yang Mana?

{class="mt-1"}
Aturan praktis: alur utama memakai NavigationStack untuk mendorong halaman (daftar → detail), operasi sementara memakai popup sheet (tambah, edit, konfirmasi), dan beberapa bagian besar yang sederajat memakai TabView (tab bawah). Gabungan ketiganya adalah kerangka dari hampir semua App.
:::

#### 4. List: "Daftar Andalan" iOS

Komponen paling sering dipakai sekaligus paling khas Apple di iOS adalah List — garis pemisah, hapus dengan geser, dan sorotan saat diklik sudah tersedia secara bawaan:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Daftar List + geser untuk hapus</span><span class="dots">···</span>
:::

```
struct RecordListView: View {
    @State private var records = ["Makan siang 25.5", "MRT 6.0", "Gaji +8000"]

    var body: some View {
        List {
            ForEach(records, id: \.self) { r in
                Text(r)
            }
            .onDelete { indexSet in          // geser kiri untuk menghapus
                records.remove(atOffsets: indexSet)
            }
        }
    }
}
```
:::

Daftar + NavigationLink + sheet + TabView — gabungkan empat hal ini dan kamu sudah bisa membangun kerangka App lengkap "daftar catatan → buka detail → tekan + untuk entri". Proyek buku catatan keuangan di bab berikutnya dibangun persis seperti ini.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Praktik: Membangun "Kerangka Tiga Halaman"

#### 5. Siklus Hidup Aplikasi: Latar Depan dan Latar Belakang

Mirip siklus hidup Activity di Android, App iOS juga mengalami perubahan status "lahir, latar depan, latar belakang, mati". Di SwiftUI, amati lewat nilai lingkungan scenePhase:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Mengamati peralihan depan/latar</span><span class="dots">···</span>
:::

```
@main
struct MyApp: App {
    @Environment(\.scenePhase) private var phase

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .onChange(of: phase) { _, newPhase in
            switch newPhase {
            case .active:    print("Kembali ke depan, lanjutkan pembaruan")
            case .inactive:  print("Sedang transisi (panggilan masuk/beralih ke latar sesaat)")
            case .background: print("Masuk latar, simpan draf")
            @unknown default: break
            }
        }
    }
}
```
:::

Kegunaan khas: menyegarkan data saat kembali ke latar depan, menyimpan draf saat masuk latar belakang. iOS sangat ketat soal berjalan di latar belakang — App biasa segera ditangguhkan (dibekukan) tidak lama setelah masuk latar belakang, jadi jangan berharap bisa diam-diam mengerjakan tugas berat di sana; untuk tugas terjadwal, gunakan notifikasi lokal dari Bab 68, bukan "tetap hidup di latar belakang".

{class="mt-1"}
Buat kerangka buku catatan keuangan versi data palsu: TabView dengan tiga tab (buku catatan/statistik/pengaturan) → halaman buku catatan memakai List untuk menampilkan data palsu, ketuk baris untuk ke detail (NavigationStack) → tombol "+" di pojok kanan atas memunculkan sheet entri. Tanpa menyimpan data, tanpa internet, murni latihan kerangka — setelah kerangka ini jadi, mengisi data sungguhan di Bab 65 akan berjalan mulus.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan Bab Ini

- Empat alat state: @State (privat satu halaman), @Binding (pinjam), @Observable (logika), .environment (global)
- Proyek baru tulis view model dengan makro @Observable; @ObservableObject di tutorial lama cukup dibaca saja
- NavigationStack mendorong halaman; @Environment(\.dismiss) untuk kembali secara terprogram
- Alur utama mendorong halaman, operasi sementara memunculkan sheet, bagian besar yang sederajat memakai TabView
- List adalah "daftar andalan": garis pemisah dan hapus dengan geser langsung siap pakai
:::
