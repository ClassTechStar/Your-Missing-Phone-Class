---
id: di-liu-shi-wu-zhang
num: 65
part: ios-kai-fa-pian
nav: Bab 65: Proyek 1—Aplikasi Pembukuan Saya (Versi Lokal)
toc: default
kind: chapter
---

### Bab 65: Proyek 1 — Buku Catatan Keuangan Saya (Versi Lokal)

{class="chapter-intro mb-4"}
Selamat datang di "proyek serius" pertamamu. Buku catatan keuangan ini meski tidak terhubung internet, isinya lengkap: bisa mencatat transaksi, melihat riwayat, merangkum per bulan, serta menghapus dan mengubah. Setelah menyelesaikannya, kamu telah melewati alur lengkap "data → logika → antarmuka". Jangan buru-buru menyalin kode — pikirkan dulu dengan jelas, baru mulai; itu prinsip kita selama ini.

#### 1. Memikirkan Kebutuhan: Tanya Dulu Lima Pertanyaan

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Elemen</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Jawaban</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who (untuk siapa)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Untuk sendiri, boleh juga untuk keluarga dan teman</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What (membuat apa)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mencatat pemasukan/pengeluaran, melihat riwayat, merangkum per bulan, statistik per kategori</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why (mengapa)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Berlatih + mengetahui uang habis ke mana</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How (bagaimana membuatnya)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift + SwiftUI + SwiftData + MVVM, murni lokal tanpa backend</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint (batasan)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Selesai dalam satu minggu; minimal mendukung iOS 17 (syarat SwiftData)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Lima elemen kebutuhan buku catatan keuangan

Lalu pecah menjadi langkah-langkah kecil yang "setiap langkahnya langsung bisa dipakai": ① bangun lapisan data SwiftData (bisa menyimpan satu transaksi); ② halaman daftar (bisa melihat riwayat); ③ popup entri (bisa menambah catatan); ④ hapus dan edit; ⑤ kartu ringkasan bulanan. Setiap langkah selesai, App selalu berupa "sesuatu yang bisa dipakai".

#### 2. Lapisan Data: Memberi "Catatan" Sebuah Rumah

Pertama, definisikan seperti apa satu transaksi — field cukup untuk kebutuhan, jangan serakah:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Record.swift (model)</span><span class="dots">···</span>
:::

```
import SwiftData

@Model
class Record {
    var type: String      // "income" pemasukan | "expense" pengeluaran
    var amount: Double    // Nominal (yuan)
    var category: String  // Kategori: makan, transportasi, gaji……
    var note: String      // Catatan (opsional)
    var date: Date        // Tanggal pencatatan

    init(type: String, amount: Double, category: String, note: String = "", date: Date = Date()) {
        self.type = type
        self.amount = amount
        self.category = category
        self.note = note
        self.date = date
    }
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tips: Mengapa Nominal Memakai Double?

{class="mt-1"}
App finansial yang serius memakai Decimal (desimal presisi) untuk menghindari galat floating-point (masalah lama 0.1+0.2≠0.3). Untuk proyek latihan, Double sudah cukup; jika suatu hari membuat produk finansial sungguhan, ingat ganti ke Decimal atau "Int dengan satuan sen" — ini lubang yang telah menelan banyak pendahulu.
:::

#### 3. MVVM: Antarmuka dan Logika "Berpisah Rumah"

Langsung membuat antarmuka mengoperasikan basis data? Bisa jalan, tapi kode antarmukanya akan panjang dan berantakan. Arsitektur MVVM membuat semuanya menjalankan tugasnya masing-masing: View (antarmuka) hanya menggambar, ViewModel (pusat logika) mengelola data, Model (SwiftData) mengelola penyimpanan.

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> View (tampilan SwiftUI)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> ViewModel (pusat logika @Observable)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-database mr-1"></i> Model (lapisan data SwiftData)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Gambar 4: Struktur tiga lapis MVVM — data mengalir satu arah, tiap lapis tidak melampaui batasnya
:::

::: div .code-block
:::inline div .code-head
<span>SWIFT · RecordViewModel.swift (kerangka)</span><span class="dots">···</span>
:::

```
import Observation

@Observable
class RecordViewModel {
    var records: [Record] = []
    private let context: ModelContext

    init(context: ModelContext) { self.context = context }

    func load() {
        // Menyaring + mengurutkan dengan #Predicate milik SwiftData
        let descriptor = FetchDescriptor<Record>(
            sortBy: [SortDescriptor(\.date, order: .reverse)]
        )
        records = (try? context.fetch(descriptor)) ?? []
    }

    func add(type: String, amount: Double, category: String, note: String) {
        let r = Record(type: type, amount: amount, category: category, note: note)
        context.insert(r)
        try? context.save()
        load()                       // Muat ulang, tampilan ikut menyegarkan
    }

    func delete(_ record: Record) {
        context.delete(record)
        try? context.save()
        load()
    }
}
```
:::

Di antarmuka tulis @State private var vm = RecordViewModel(...), lalu langsung render daftar dari vm.records — begitu data berubah, antarmuka otomatis menyegarkan.

#### 4. Antarmuka: Halaman Daftar + Popup Entri

::: div .code-block
:::inline div .code-head
<span>SWIFT · Halaman daftar pencatatan (potongan inti)</span><span class="dots">···</span>
:::

```
struct RecordListView: View {
    @State private var vm: RecordViewModel
    @State private var showAdd = false

    var body: some View {
        NavigationStack {
            List {
                Section("Saldo bulan ini") {          // kartu rekap
                    SummaryRow(records: vm.records)
                }
                Section("Mutasi") {
                    ForEach(vm.records) { r in
                        RecordRow(record: r)
                    }
                    .onDelete { idx in
                        idx.forEach { vm.delete(vm.records[$0]) }
                    }
                }
            }
            .navigationTitle("Buku kas saya")
            .toolbar {
                Button { showAdd = true } label: {
                    Image(systemName: "plus")
                }
            }
            .sheet(isPresented: $showAdd) {
                AddRecordView(vm: vm)          // dialog input
            }
        }
    }
}
```
:::

Poin penting popup entri: keyboard kolom nominal memakai .keyboardType(.decimalPad) (keyboard angka), pemasukan/pengeluaran memakai kontrol tersegmentasi (Picker), kategori dipilih lewat menu, dan saat menekan "Simpan" panggil vm.add(...) lalu dismiss() untuk menutup popup.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Perhatian: Jangan Malas Memvalidasi Input

{class="mt-1"}
Kolom nominal wajib divalidasi: nilai kosong, angka negatif, dan input tidak sah seperti "abc" semuanya harus ditahan (cek dengan Double(text); jika gagal mengembalikan nil). Salah satu penyebab paling umum App crash adalah "menganggap input pengguna anak yang penurut". Ingat: semua yang diketik pengguna harus diperiksa seperti musuh.
:::

#### 5. Edit, Hapus, dan Ringkasan

- Hapus: .onDelete pada List untuk hapus dengan geser ke kiri + popup konfirmasi (salah hapus adalah hal yang paling dibenci pengguna App pencatat keuangan);
- Edit: ketuk baris untuk masuk popup edit dengan nilai lama sudah terisi (mengubah sedikit lebih hemat tenaga daripada mengetik ulang);
- Ringkasan: pakai filter + reduce untuk menghitung "pemasukan / pengeluaran / saldo bulan ini", ditampilkan dalam kartu di bagian atas:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Perhitungan rekap bulanan</span><span class="dots">···</span>
:::

```
func monthSummary(_ records: [Record]) -> (income: Double, expense: Double) {
    let cal = Calendar.current
    let monthRecords = records.filter {
        cal.isDate($0.date, equalTo: Date(), toGranularity: .month)
    }
    let income = monthRecords
        .filter { $0.type == "income" }
        .reduce(0) { $0 + $1.amount }
    let expense = monthRecords
        .filter { $0.type == "expense" }
        .reduce(0) { $0 + $1.amount }
    return (income, expense)
}
```
:::

#### 6. Penerimaan: Pemeriksaan Tiga Lapis + Dua Tantangan Lanjutan

Setelah proyek selesai, lakukan penerimaan tiga lapis sesuai "fungsi → batas → arsitektur": bisa mencatat atau tidak, bisa menghapus atau tidak, apakah data tetap ada setelah App dimulai ulang (fungsi); apakah crash saat nominal diisi 0 atau negatif (batas); apakah antarmuka dan data tercampur, apakah ada field yang ditulis mati (arsitektur).

Setelah versi dasar lolos penerimaan, beri dirimu dua "hidangan lanjutan":

1. Statistik kategori: tambahkan tab "Statistik", gunakan Swift Charts untuk menggambar pengeluaran per kategori sebagai diagram lingkaran/batang — pustaka grafik resmi Apple, beberapa baris kode langsung jadi grafik;
2. Sinkronisasi iCloud: mengaktifkan sinkronisasi iCloud di SwiftData hanya perlu beberapa pengaturan — buku catatan otomatis tersinkron antara iPhone/iPad, langsung terasa "canggih".

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Praktik: Selesaikan Minggu Ini

{class="mt-1"}
Bekerjalah mengikuti urutan "lapisan data → ViewModel → halaman daftar → popup entri → kartu ringkasan", satu langkah per hari. Kalau macet, tempelkan pesan error apa adanya ke mesin pencari atau AI (masih ingat Bagian 7 "Praktik Pemrograman dengan AI"? Saat mendeskripsikan masalah, jelaskan dengan jelas "perilaku yang diharapkan, perilaku yang terjadi, langkah reproduksi"). Setelah selesai, pakai untuk mencatat keuangan selama satu minggu — memakai App buatan sendiri memberi rasa pencapaian yang mendorongmu terus berjalan.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan Bab Ini

- Lima elemen kebutuhan → pecah menjadi langkah kecil "setiap langkah bisa dipakai", baru mulai bekerja
- Lapisan data: model @Model + kontainer modelContainer + kueri FetchDescriptor
- Pembagian tugas MVVM: View hanya menggambar, ViewModel @Observable mengelola logika, SwiftData mengelola penyimpanan
- Antarmuka: List + Section + toolbar + popup entri sheet
- Penerimaan tiga lapis (fungsi/batas/arsitektur) + tantangan lanjutan (Swift Charts, sinkronisasi iCloud)
:::
