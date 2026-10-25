---
id: di-liu-shi-wu-zhang
num: 65
part: ios-kai-fa-pian
nav: Bab 65: Projek 1—Buku Catatan Saya (Versi Setempat)
toc: default
kind: chapter
---

### Bab 65: Projek 1 — Buku Rekod Perbelanjaan Saya (Versi Tempatan)

{class="chapter-intro mb-4"}
Selamat datang ke 'projek sebenar' pertama anda. Buku rekod perbelanjaan ini walaupun tidak bersambung internet, tetapi lengkap segalanya: boleh merekod transaksi, melihat senarai transaksi, statistik bulanan, memadam dan mengubah. Selepas menyiapkannya, anda telah melalui keseluruhan aliran 'data → logik → antara muka' dengan lengkap. Jangan tergesa menyalin kod — fikir dengan jelas dahulu barulah bertindak; itulah prinsip kita sepanjang buku ini.

#### 1. Pemikiran keperluan: tanya lima soalan dahulu

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Elemen</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Jawapan</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Who (untuk siapa)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Untuk sendiri, keluarga dan rakan pun boleh</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">What (buat apa)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Rekod pendapatan/belanja, lihat senarai transaksi, rumusan bulanan, statistik mengikut kategori</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Why (mengapa)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Latihan praktikal + mengetahui ke mana wang dibelanjakan</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">How (bagaimana)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Swift + SwiftUI + SwiftData + MVVM, sepenuhnya tempatan tanpa backend</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Constraint (sekatan)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Siap dalam masa seminggu; sokongan minimum iOS 17 (syarat SwiftData)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Lima elemen keperluan buku rekod perbelanjaan

Kemudian pecahkan kepada langkah kecil 'setiap langkah boleh diguna': (1) bina lapisan data SwiftData (boleh simpan satu rekod); (2) halaman senarai (boleh lihat senarai transaksi); (3) pop timbul kemasukan (boleh tambah rekod); (4) padam dan sunting; (5) kad rumusan bulanan. Setiap langkah yang siap menjadikan App ini 'sesuatu yang boleh digunakan'.

#### 2. Lapisan data: berikan 'rekod' sebuah rumah

Takrifkan dahulu bentuk satu rekod — medan cukup guna tetapi jangan tamak:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Record.swift (model)</span><span class="dots">···</span>
:::

```
import SwiftData

@Model
class Record {
    var type: String      // "income" pendapatan | "expense" perbelanjaan
    var amount: Double    // Jumlah (yuan)
    var category: String  // Kategori: makanan, pengangkutan, gaji……
    var note: String      // Nota (pilihan)
    var date: Date        // Tarikh rekod

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
Petua: Mengapa jumlah guna Double?

{class="mt-1"}
App kewangan yang serius akan guna Decimal (perpuluhan jitu) untuk mengelak ralat titik terapung (masalah lama 0.1+0.2≠0.3). Projek latihan guna Double sudah memadai; jika suatu hari anda membuat produk kewangan sebenar, ingat tukar kepada Decimal atau 'Int dalam unit sen' — inilah perangkap yang dilalui oleh ramai pembangun terdahulu.
:::

#### 3. MVVM: antara muka dan logik 'berpisah'

Terus biar antara muka mengendalikan pangkalan data? Boleh berjalan, tetapi kod antara muka akan panjang dan bercelaru. Seni bina MVVM menjadikan tugas terbahagi: View (antara muka) hanya melukis, ViewModel (pusat logik) mengurus data, Model (SwiftData) mengurus penyimpanan.

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> View (paparan SwiftUI)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> ViewModel (hab logik @Observable)</span><span class="text-gray-400 mx-1">⇄</span> <span class="border-2 border-gray-400 bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-database mr-1"></i> Model (lapisan data SwiftData)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Rajah 4: Struktur tiga lapis MVVM — data mengalir sehala, setiap lapis tidak melangkaui sempadannya
:::

::: div .code-block
:::inline div .code-head
<span>SWIFT · RecordViewModel.swift (rangka)</span><span class="dots">···</span>
:::

```
import Observation

@Observable
class RecordViewModel {
    var records: [Record] = []
    private let context: ModelContext

    init(context: ModelContext) { self.context = context }

    func load() {
        // Menapis + mengisih dengan #Predicate milik SwiftData
        let descriptor = FetchDescriptor<Record>(
            sortBy: [SortDescriptor(\.date, order: .reverse)]
        )
        records = (try? context.fetch(descriptor)) ?? []
    }

    func add(type: String, amount: Double, category: String, note: String) {
        let r = Record(type: type, amount: amount, category: category, note: note)
        context.insert(r)
        try? context.save()
        load()                       // Muat semula, paparan terus segar
    }

    func delete(_ record: Record) {
        context.delete(record)
        try? context.save()
        load()
    }
}
```
:::

Dalam antara muka tulis @State private var vm = RecordViewModel(...), kemudian paparkan senarai terus dengan vm.records — data berubah, antara muka menyegarkan sendiri.

#### 4. Antara muka: halaman senarai + pop timbul kemasukan

::: div .code-block
:::inline div .code-head
<span>SWIFT · Halaman senarai rekod (petikan teras)</span><span class="dots">···</span>
:::

```
struct RecordListView: View {
    @State private var vm: RecordViewModel
    @State private var showAdd = false

    var body: some View {
        NavigationStack {
            List {
                Section("Baki bulan ini") {          // kad ringkasan
                    SummaryRow(records: vm.records)
                }
                Section("Urus niaga") {
                    ForEach(vm.records) { r in
                        RecordRow(record: r)
                    }
                    .onDelete { idx in
                        idx.forEach { vm.delete(vm.records[$0]) }
                    }
                }
            }
            .navigationTitle("Buku akaun saya")
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

Poin penting pop timbul kemasukan: papan kekunci medan jumlah guna .keyboardType(.decimalPad) (papan nombor), pendapatan/belanja guna kawalan bersegmen (Picker), kategori dipilih melalui menu, dan menekan 'Simpan' memanggil vm.add(...) serta dismiss() untuk menutup tetingkap.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Perhatian: jangan malas membuat pengesahan input

{class="mt-1"}
Medan jumlah mesti disahkan: nilai kosong, nombor negatif dan input tidak sah seperti "abc" semuanya perlu disekat (guna Double(text) untuk menilai; jika gagal ia memulangkan nil). Salah satu punca paling biasa App ranap ialah 'menganggap input pengguna sentiasa sopan'. Ingat: segala input pengguna mesti diperiksa seakan memeriksa musuh.
:::

#### 5. Sunting, padam dan rumusan

- Padam: .onDelete dalam List untuk padam dengan leret ke kiri + pop timbul pengesahan (padaman tersilap ialah perkara paling dibenci pengguna App rekod kewangan);
- Sunting: tekan baris untuk masuk ke pop timbul suntingan, isikan nilai asal terlebih dahulu (mengubah sedikit lebih jimat daripada menaip semula);
- Rumusan: guna filter + reduce untuk mengira 'pendapatan / belanja / baki bulan ini', dipaparkan pada kad di bahagian atas:

::: div .code-block
:::inline div .code-head
<span>SWIFT · Pengiraan ringkasan bulanan</span><span class="dots">···</span>
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

#### 6. Penerimaan: tiga lapis semakan + dua cabaran lanjutan

Selepas projek siap, jalankan penerimaan tiga lapis 'fungsi → sempadan → seni bina': boleh merekod ke tidak, boleh memadam ke tidak, adakah data masih ada selepas App dimulakan semula (fungsi); adakah ranap apabila jumlah dimasukkan 0 atau negatif (sempadan); adakah antara muka dan data bercampur aduk, adakah medan ditulis secara tetap (seni bina).

Selepas lulus penerimaan versi asas, berikan diri anda dua 'hidangan lanjutan':

1. Statistik kategori: tambah satu tab 'Statistik', guna Swift Charts untuk melukis perbelanjaan mengikut kategori sebagai carta pai/carta bar — pustaka carta rasmi Apple, beberapa baris kod terhasil carta;
2. Segerakan iCloud: mengaktifkan segerakan iCloud dalam SwiftData hanya perlu beberapa tetapan — buku rekod disegerakkan secara automatik antara iPhone/iPad, terus terasa 'canggih'.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Praktik: Siapkan minggu ini

{class="mt-1"}
Bertindak mengikut urutan 'lapisan data → ViewModel → halaman senarai → pop timbul kemasukan → kad rumusan', satu langkah sehari. Tersekat? Salin mesej ralat apa adanya kepada enjin carian atau AI (masih ingat Bahagian 7 'Praktik Pengekodan AI'? Semasa menerangkan masalah, nyatakan dengan jelas 'tingkah laku dijangka, tingkah laku sebenar, langkah menghasilkan semula'). Selepas siap, gunakannya untuk merekod perbelanjaan selama seminggu — menggunakan App buatan sendiri, rasa pencapaian akan mendorong anda terus maju.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan bab ini

- Lima elemen keperluan → pecahkan kepada langkah kecil 'setiap langkah boleh guna', barulah bertindak
- Lapisan data: model @Model + bekas modelContainer + pertanyaan FetchDescriptor
- Pembahagian MVVM: View hanya melukis, ViewModel @Observable mengurus logik, SwiftData mengurus penyimpanan
- Antara muka: List + Section + toolbar + sheet pop timbul kemasukan
- Penerimaan tiga lapis (fungsi/sempadan/seni bina) + cabaran lanjutan (Swift Charts, segerakan iCloud)
:::
