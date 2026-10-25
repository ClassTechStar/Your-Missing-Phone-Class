---
id: di-liu-shi-san-zhang
num: 63
part: ios-kai-fa-pian
nav: Bab 63: Paparan, Status dan Navigasi
toc: default
kind: chapter
---

### Bab 63: View, Negeri (State) dan Navigasi

{class="chapter-intro mb-4"}
Mainan satu halaman sudah pandai dibuat. Bab ini menyelesaikan dua soalan 'membesar': cara melompat-lompat antara berbilang halaman (navigasi), dan cara data mengalir antara halaman (pengurusan state). Selepas bab ini, anda boleh membina kerangka App berbilang halaman klasik seperti 'senarai → butiran → sunting'.

#### 1. Peta menyeluruh aliran data pengurusan state

Alat state SwiftUI bukan setakat @State. Lihat dahulu peta menyeluruh ini untuk memahami 'bila guna yang mana':

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Alat</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Mengurus apa</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Digunakan oleh</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Senario tipikal</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@State</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">State sementara peribadi halaman</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">View semasa</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pengira, teks medan input</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@Binding</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Meminjam state orang lain</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sub-view mengubah view induk</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Komponen tersuai</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@StateObject / @Observable</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Logik dikongsi merentas halaman</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Model pandangan (ViewModel)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pemuatan data, logik perniagaan</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">@EnvironmentObject / .environment</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">State dikongsi secara global</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Keseluruhan App</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Status log masuk pengguna, tetapan tema</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Peta menyeluruh alat state SwiftUI (pada 2026, @Observable sudah arus perdana)

::: div .code-block
:::inline div .code-head
<span>SWIFT · Arus perdana 2026: view model @Observable</span><span class="dots">···</span>
:::

```
// Cara moden iOS 17+: makro @Observable (digalakkan untuk projek baru)
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
            Text("Anda menekan \(model.count) kali")
            Button("Tekan saya") { model.increment() }
        }
    }
}
```
:::

Nasihat terus untuk pemula: state peribadi halaman guna @State, yang merentas halaman atau berlogik guna kelas @Observable. @StateObject/@ObservableObject dalam tutorial lama ialah gaya generasi sebelumnya — cukup sekadar boleh membaca; untuk kod baharu, ikut seperti di atas.

#### 2. NavigationStack: 'tindanan' lompatan halaman

Mulai iOS 16, navigasi berbilang halaman menggunakan NavigationStack — seperti timbunan pinggan: satu dimasukkan satu demi satu, dan dikeluarkan satu demi satu semasa kembali:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Navigasi NavigationStack</span><span class="dots">···</span>
:::

```
struct HomeView: View {
    var body: some View {
        NavigationStack {
            List {
                NavigationLink("Buku akaun Zhang San") {
                    DetailView(name: "Buku akaun Zhang San")   // halaman destinasi
                }
                NavigationLink("Buku akaun Li Si") {
                    DetailView(name: "Buku akaun Li Si")
                }
            }
            .navigationTitle("Senarai buku akaun")   // tajuk besar di atas
        }
    }
}

struct DetailView: View {
    let name: String
    var body: some View {
        Text("Halaman butiran \(name)")
            .navigationTitle(name)
            .navigationBarTitleDisplayMode(.inline)
    }
}
```
:::

NavigationLink ialah 'pautan lompatan yang boleh ditekan'; navigationTitle menjana tajuk bar navigasi dan butang kembali secara automatik. Untuk lompatan secara berprogram (contohnya kembali automatik selepas menekan 'Simpan'), gunakan @Environment(\.dismiss) untuk menutup halaman semasa — dengan dua helah ini, 90% keperluan navigasi sudah lengkap.

#### 3. Pop timbul dan tab bawah: sheet dan TabView

Selain 'menolak halaman', ada dua lagi interaksi klasik:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Pop timbul sheet + tab TabView</span><span class="dots">···</span>
:::

```
// 1. Pop separuh skrin/skrin penuh dari bawah (kegemaran borang input)
struct HomeView: View {
    @State private var showAdd = false
    var body: some View {
        Button("Catat") { showAdd = true }
            .sheet(isPresented: $showAdd) {
                AddRecordView()     // Halaman input yang dipaparkan
            }
    }
}

// 2. Bar tab bawah ("rangka" aplikasi)
struct MainTabView: View {
    var body: some View {
        TabView {
            RecordListView()
                .tabItem { Label("Buku akaun", systemImage: "book") }
            StatsView()
                .tabItem { Label("Statistik", systemImage: "chart.pie") }
            SettingsView()
                .tabItem { Label("Tetapan", systemImage: "gear") }
        }
    }
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Petua: Bila guna yang mana?

{class="mt-1"}
Peraturan pengalaman: aliran utama guna NavigationStack untuk menolak halaman (senarai→butiran), operasi sementara guna pop timbul sheet (tambah, sunting, sahkan), beberapa bahagian besar yang setara guna TabView (tab bawah). Gabungan ketiga-tiganya ialah kerangka hampir semua App.
:::

#### 4. List: senarai paling popular di iOS

Komponen paling kerap digunakan dan paling 'berbau Apple' di iOS ialah List — sedia ada garis pemisah, padam dengan leretan dan sorotan semasa ditekan:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Senarai List + leret untuk padam</span><span class="dots">···</span>
:::

```
struct RecordListView: View {
    @State private var records = ["Makan tengah hari 25.5", "LRT 6.0", "Gaji +8000"]

    var body: some View {
        List {
            ForEach(records, id: \.self) { r in
                Text(r)
            }
            .onDelete { indexSet in          // leret kiri untuk padam
                records.remove(atOffsets: indexSet)
            }
        }
    }
}
```
:::

Senarai + NavigationLink + sheet + TabView — gabungkan empat elemen ini, dan anda sudah boleh membina kerangka App lengkap 'senarai rekod → buka butiran → tekan + muncul borang kemasukan'. Projek buku rekod perbelanjaan bab seterusnya dibina begini.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Praktik: Bina 'kerangka tiga halaman'

#### 5. Kitaran hayat aplikasi: hadapan dan latar belakang

Sama seperti kitaran hayat Activity pada Android, App iOS juga mengalami perubahan state 'lahir, hadapan, latar belakang, mati'. Dalam SwiftUI, gunakan nilai persekitaran scenePhase untuk memerhatikannya:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Memerhati pertukaran hadapan/latar</span><span class="dots">···</span>
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
            case .active:    print("Kembali ke hadapan, sambung segar semula")
            case .inactive:  print("Dalam peralihan (panggilan masuk/baru beralih ke latar)")
            case .background: print("Masuk latar, simpan draf")
            @unknown default: break
            }
        }
    }
}
```
:::

Kegunaan tipikal: segarkan data semasa kembali ke hadapan, simpan draf semasa masuk ke latar belakang. iOS mengawal pelaksanaan latar belakang dengan sangat ketat — App biasa akan segera digantung (dibekukan) selepas masuk latar belakang; jangan berharap boleh membuat kerja berat secara senyap-senyap di latar belakang. Jika benar-benar perlu tugasan berkala, gunakan pemberitahuan tempatan dalam Bab 68, bukan 'kekal berjalan di latar belakang'.

{class="mt-1"}
Bina kerangka versi data palsu buku rekod perbelanjaan: TabView tiga tab (Rekod/Statistik/Tetapan) → halaman rekod guna List memaparkan data palsu, tekan baris untuk ke butiran (NavigationStack) → butang '+' penjuru atas kanan memunculkan sheet kemasukan. Tanpa menyimpan data, tanpa internet — semata-mata latihan kerangka. Kerangka ini siap, mengisinya dengan data sebenar pada Bab 65 menjadi perkara semula jadi.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan bab ini

- Empat alat state: @State (peribadi halaman), @Binding (pinjaman), @Observable (logik), .environment (global)
- Projek baharu guna makro @Observable menulis ViewModel; @ObservableObject tutorial lama cukup sekadar dapat dibaca
- NavigationStack menolak halaman; @Environment(\.dismiss) kembali secara berprogram
- Aliran utama tolak halaman, operasi sementara munculkan sheet, bahagian besar setara guna TabView
- List ialah senarai paling popular: garis pemisah dan padam leretan sedia guna
:::
