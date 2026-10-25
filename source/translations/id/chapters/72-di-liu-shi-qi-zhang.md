---
id: di-liu-shi-qi-zhang
num: 67
part: ios-kai-fa-pian
nav: Bab 67: Memoles dan Menerbitkan—Masuk ke App Store
toc: default
kind: chapter
---

### Bab 67: Penyempurnaan dan Rilis — Pengujian, Debugging, dan Terbit di App Store

{class="chapter-intro mb-4"}
App sudah jadi, lalu apa? Bab ini menjawab tiga hal untuk bergerak "dari bisa jalan" menuju "siap diserahkan": cara debug yang efisien untuk mencari bug, cara menulis tes untuk mencegah regresi, dan cara mengirim App ke App Store agar diunduh seluruh dunia. Menerbitkan bukan sekadar seremoni — itulah garis pemisah antara sebuah karya dan sebuah produk.

#### 1. Tiga Jurus Debug: print, Breakpoint, dan Pratinjau

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Alat</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Fungsi</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Cara memakai</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">print + konsol</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Melihat log saat berjalan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Di kode tulis print("nilai=\(x)"), lihat keluarannya di konsol bagian bawah Xcode</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Debug dengan breakpoint</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menghentikan program di baris tertentu untuk melihat nilai variabel</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Klik sekali di samping nomor baris hingga muncul tanda biru; program berhenti saat mencapai titik itu, lalu telusuri selangkah demi selangkah</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pratinjau SwiftUI + debugger</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Melihat antarmuka dan hierarki view secara real-time</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kanvas #Preview + pemeriksa View Hierarchy saat runtime</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Tiga jurus debug

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tips: Cara Membaca Log Crash?

{class="mt-1"}
Saat Swift crash, konsol menampilkan "Fatal error" beserta penyebabnya, dan Xcode berhenti di baris yang salah sambil menyorotnya. Riwayat crash di perangkat asli bisa dilihat di Xcode → Window → Organizer → Crashes (perlu akun berbayar). Untuk kata kunci pencarian, utamakan "kalimat pertama penyebab error + swiftui" — pertanyaan yang presisi menghasilkan jawaban yang presisi.
:::

#### 2. Pengujian: Memberi Asuransi pada Kode

Tes manual tidak bisa diandalkan — mengubah satu fitur, fitur lain bisa rusak diam-diam. Tes adalah "obat penyesalan" sekaligus "rompi anti-peluru". iOS memakai framework XCTest, terbagi dua:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Tingkatan</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Menguji apa</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Target</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Kecepatan</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tes unit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Logika murni (perhitungan, validasi)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstAppTests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Hitungan detik</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tes UI</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Perilaku antarmuka sungguhan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstAppUITests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Hitungan menit</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tes manual</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Perasaan dan pengalaman pengguna sungguhan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">——</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Selalu dibutuhkan</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Tingkatan pengujian iOS (proyek templat sudah menyiapkan dua Test Target)

::: div .code-block
:::inline div .code-head
<span>SWIFT · Contoh unit test</span><span class="dots">···</span>
:::

```
import XCTest

// Pisahkan logika "mengubah teks nominal menjadi angka" menjadi fungsi murni
func parseAmount(_ input: String) -> Double? {
    guard let v = Double(input.trimmingCharacters(in: .whitespaces)),
          v > 0 else { return nil }
    return v
}

final class AmountTests: XCTestCase {
    func testEmptyInputReturnsNil() {
        XCTAssertNil(parseAmount(""))
    }
    func testNegativeReturnsNil() {
        XCTAssertNil(parseAmount("-5"))
    }
    func testNormalValueParses() {
        XCTAssertEqual(parseAmount("12.5"), 12.5)
    }
}
```
:::

Jalankan tes: ⌘U. Setelah semuanya hijau baru ubah kode — hati pun tenang. Validasi nominal dan perhitungan ringkasan di buku catatan keuangan semuanya sebaiknya dilindungi tes unit.

#### 3. Penandatanganan dan Packaging: Memberi App "Cap Resmi"

Setiap App iOS harus ditandatangani sebelum bisa dipasang — sebagai bukti "paket ini berasal dari kamu dan tidak diutak-atik". Hubungan tingkatannya:

- Tahap belajar: Apple ID gratis + penandatanganan otomatis Xcode (Personal Team), bisa dijalankan di perangkat asli, perlu diperpanjang setiap 7 hari;
- Tahap distribusi: akun pengembang berbayar (99 dolar AS/tahun) menerbitkan sertifikat dan provisioning profile, barulah bisa terbit di App Store dan dipasang jangka panjang.

Packaging: menu Xcode Product → Archive (mengarsipkan); setelah build selesai, di Organizer pilih Distribute App → pilih App Store Connect → unggah. Pengarsipan wajib memakai Generic iOS Device sebagai target (bukan simulator) — langkah yang sering terlupakan pemula.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Peringatan Jebakan: Sertifikat Hilang = Pembaruan Terputus

{class="mt-1"}
Begitu sertifikat penandatanganan dan kunci privat hilang, kamu tidak bisa lagi mengirim pembaruan untuk App lama — pengguna hanya bisa memasang aplikasi "benar-benar baru". Backup sertifikat dengan baik (ekspor .p12 dari Keychain) dan simpan kata sandinya. Untungnya Apple menyediakan "penandatanganan otomatis" dan manajemen sertifikat cloud (centang Automatically manage signing di Xcode), yang menghemat sebagian besar kerumitan manual.
:::

#### 4. Alur Lengkap Menerbitkan ke App Store

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> Mendaftar akun developer</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-invoice mr-1"></i> Menyiapkan materi store</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-box mr-1"></i> Unggah paket build</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-clipboard-list mr-1"></i> Isi informasi privasi dan review</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> Review Apple (1-7 hari)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-party-horn mr-1"></i> Rilis di store</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Gambar 5: Enam langkah menerbitkan ke App Store
:::

- Registrasi: developer.apple.com, akun pribadi 99 dolar AS/tahun;
- Aset: ikon (1024×1024, jangan pakai sudut membulat — Apple yang memotongnya sendiri), tangkapan layar (berbagai ukuran iPhone), deskripsi, tautan kebijakan privasi;
- Kuesioner privasi: laporkan dengan jujur data apa saja yang dikumpulkan — buku catatan keuangan tanpa internet boleh memilih "tidak mengumpulkan data apa pun";
- Review: pengajuan pertama biasanya menunggu 1–7 hari; jika ditolak, perbaiki satu per satu sesuai "catatan review" — alasan penolakan Apple biasanya ditulis sangat spesifik, tinggal diikuti;
- TestFlight: sebelum terbit, kirim dulu versi tes ke teman-teman untuk uji internal (maksimal 10.000 orang), kumpulkan satu putaran masukan sebelum mengajukan resmi — sangat profesional.

#### 5. Membuat Aset Toko: Kesan Pertama Menentukan Jumlah Unduhan

Halaman toko adalah etalase yang dilihat pengguna saat "berkunjung". Tiga aset menentukan kesan pertama:

- Ikon: 1024×1024, jangan asal pakai tangkapan layar. Kalau tidak punya kemampuan desain, buat grafis sederhana dengan alat AI; baru dianggap layak jika tetap mudah dikenali sekali lihat setelah diperkecil di layar utama;
- Tangkapan layar: minimal 2 set (ukuran utama iPhone), memperlihatkan skenario fitur paling inti; setiap gambar diberi satu kalimat caption berbahasa manusia ("Catat dalam sekejap" sepuluh kali lebih baik daripada "Solusi pencatatan keuangan yang efisien");
- Deskripsi: kalimat pertama menjelaskan dengan jelas "ini apa + untuk siapa"; jangan menumpuk kata "paling profesional, paling hebat" — kejujuran lebih efektif daripada bombastis.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Praktik: "Menyerahkan" Buku Catatan Keuangan Sekali

#### 6. Daftar Singkat Pelaporan Crash dan Optimasi Performa

Sebelum App terbit, dua hal ini layak masing-masing diberi waktu setengah jam:

##### 1. Pemantauan crash

Tidak crash saat kamu menguji belum berarti tidak crash di ponsel pengguna. Apple menyediakan laporan crash gratis di Xcode Organizer (log crash perangkat asli untuk akun berbayar); solusi yang lebih praktis adalah mengintegrasikan SDK pihak ketiga (seperti Firebase Crashlytics). Menerbitkan tanpa pemantauan crash sama dengan menyetir dengan mata terpejam.

##### 2. Empat pemeriksaan performa

1. Daftar memakai LazyVStack / List: daftar panjang jangan dipaksakan dengan VStack biasa — lazy loading adalah pelajaran performa pertama;
2. Gambar jangan langsung pakai resolusi asli: gunakan AsyncImage (gambar jarak jauh) dan cache sistem; gambar asli 5MB cukup untuk membuat ponsel tua tersendat;
3. Jangan mengerjakan tugas berat di thread utama: jaringan dan file besar semuanya lewat async/await;
4. Ukur dengan Instruments: profiler bawaan Xcode (Time Profiler, pemeriksa kebocoran memori) — ukur dulu, baru optimasi; jangan mengandalkan perasaan.

{class="mt-1"}
① Lengkapi 3 tes unit untuk logika seperti parseAmount (jalankan hijau dengan ⌘U); ② gunakan breakpoint untuk menangkap sendiri satu crash buatanmu dan perbaiki; ③ buat satu paket lewat Product → Archive, lalu ajak teman uji internal via TestFlight; ④ jika ada sisa tenaga, daftar akun pengembang dan benar-benar ajukan buku catatan keuanganmu ke App Store. Tiga langkah pertama bisa diselesaikan malam ini juga.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan Bab Ini

- Tiga jurus debug: log print, breakpoint, pratinjau SwiftUI dan pemeriksa view
- XCTest: tes unit (⌘U) + tes UI + tes manual, sudah disiapkan di templat
- Penandatanganan: akun gratis pakai penandatanganan otomatis (perpanjang tiap 7 hari); hanya akun berbayar yang bisa mendistribusikan
- Packaging: Generic iOS Device + Archive + Distribute; sertifikat wajib di-backup
- Enam langkah menerbitkan: registrasi → aset → unggah → kuesioner privasi → review → terbit; uji internal dulu lewat TestFlight
:::
