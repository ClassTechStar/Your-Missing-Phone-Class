---
id: di-liu-shi-qi-zhang
num: 67
part: ios-kai-fa-pian
nav: Bab 67: Penghalusan dan Penerbitan—Menerbitkan di App Store
toc: default
kind: chapter
---

### Bab 67: Penggilapan dan Penerbitan — Pengujian, Penyahpepijatan dan Muat Naik ke App Store

{class="chapter-intro mb-4"}
App sudah siap, kemudian apa? Bab ini menjawab tiga perkara untuk 'dari boleh berjalan' kepada 'boleh dihantar': cara menyahpepiat dan mencari bug dengan cekap, cara menulis ujian untuk mencegah regresi, dan cara menghantar App ke App Store agar boleh dimuat turun oleh seluruh dunia. Muat naik bukan sekadar upacara — ia titik peralihan yang mengubah sesebuah karya menjadi produk.

#### 1. Tiga senjata penyahpepijatan: print, titik sekatan, pratonton

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Alat</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Fungsinya</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Cara guna</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">print + konsol</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Melihat log pelaksanaan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Dalam kod tulis print("nilai=\(x)"), lihat output pada konsol bahagian bawah Xcode</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Penyahpepijatan titik sekatan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Memerintahkan program berhenti pada baris tertentu dan melihat nilai pemboleh ubah</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Klik sekali di sebelah nombor baris untuk munculkan penanda biru; pelaksanaan berhenti di situ dan anda boleh melangkah satu demi satu</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pratonton SwiftUI + penyahpepijat</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Melihat antara muka dan hierarki view secara masa nyata</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kanvas #Preview + pemeriksa View Hierarchy semasa pelaksanaan</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Tiga senjata penyahpepijatan

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Petua: Ranap, bagaimana membacanya?

{class="mt-1"}
Apabila Swift ranap, konsol mencetak 'Fatal error' beserta sebabnya, dan Xcode berhenti pada baris ralat sambil menyerlahkannya. Sejarah ranap pada peranti sebenar boleh dilihat di Xcode → Window → Organizer → Crashes (memerlukan akaun berbayar). Utamakan mencari kata kunci 'ayat pertama sebab ralat + swiftui' — soalan yang tepat barulah mendapat jawapan yang tepat.
:::

#### 2. Pengujian: memberikan insurans kepada kod

Ujian manual tidak boleh diharap — selepas mengubah fungsi ini, fungsi lain rosak secara senyap. Ujian ialah 'ubat penyesalan' sekali gus 'baju tahan peluru'. iOS menggunakan rangka kerja XCTest, terdiri daripada dua jenis:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Lapisan</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Menguji apa</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Target</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Kelajuan</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ujian unit</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Logik tulen (pengiraan, pengesahan)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstAppTests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tahap saat</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ujian UI</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tingkah laku antara muka sebenar</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MyFirstAppUITests</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tahap minit</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ujian manual</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Rasa dan pengalaman manusia sebenar</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">——</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sentiasa diperlukan</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Lapisan ujian iOS (projek templat sudah menyediakan dua Test Target)

::: div .code-block
:::inline div .code-head
<span>SWIFT · Contoh ujian unit</span><span class="dots">···</span>
:::

```
import XCTest

// Pisahkan logik "tukar rentetan jumlah kepada nombor" menjadi fungsi tulen
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

Jalankan ujian: ⌘U. Semua hijau barulah ubah kod, hati pun tenang. Pengesahan jumlah dan pengiraan rumusan dalam buku rekod perbelanjaan semuanya harus dilindungi oleh ujian unit.

#### 3. Pemeteraian dan pembungkusan: mencap 'cop' pada App

Setiap App iOS mesti dimeterai sebelum boleh dipasang — sebagai bukti 'pakej ini datang daripada anda dan tidak diganggu gugat'. Hubungan hierarkinya:

- Peringkat pembelajaran: Apple ID percuma + pemeteraian automatik Xcode (Personal Team), boleh dijalankan pada peranti sebenar, perlu diperbaharui setiap 7 hari;
- Peringkat pengedaran: akaun pembangun berbayar (99 dolar AS/tahun) mengeluarkan sijil dan fail provisioning, barulah boleh dimuat naik dan dipasang secara jangka panjang.

Bungkus: menu Xcode Product → Archive (arkib), selepas binaan selesai buka Organizer dan pilih Distribute App → pilih App Store Connect → muat naik. Pengarkiban mesti menggunakan Generic iOS Device sebagai sasaran (bukan simulator); inilah langkah yang kerap dilupakan oleh pemula.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Amaran: sijil hilang = kemas kini terhenti

{class="mt-1"}
Sekali sijil pemeteraian dan kunci peribadi hilang, anda tidak dapat lagi menghantar kemas kini kepada App lama — pengguna hanya boleh memasang aplikasi 'baru sepenuhnya'. Buat sandaran sijil dengan betul (eksport .p12 daripada Keychain) dan simpan kata laluannya dengan baik. Nasib baik Apple menyediakan 'pemeteraian automatik' dan pengurusan sijil awan (tanda Automatically manage signing dalam Xcode), yang dapat menghapuskan kebanyakan kesukaran kerja manual.
:::

#### 4. Proses penuh muat naik ke App Store

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-alt mr-1"></i> Daftar akaun pembangun</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-file-invoice mr-1"></i> Menyiapkan bahan kedai</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-box mr-1"></i> Muat naik pakej binaan</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-clipboard-list mr-1"></i> Isi maklumat privasi dan semakan</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-search mr-1"></i> Semakan Apple (1-7 hari)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-party-horn mr-1"></i> Naik ke kedai</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Rajah 5: Enam langkah muat naik ke App Store
:::

- Pendaftaran: developer.apple.com, akaun individu 99 dolar AS/tahun;
- Bahan: ikon (1024×1024, jangan sertakan sudut bulat — Apple memotongnya sendiri), tangkapan skrin (pelbagai saiz iPhone), huraian, pautan dasar privasi;
- Soal selidik privasi: isytiharkan dengan jujur data apa yang dikumpul — buku rekod perbelanjaan yang tidak bersambung internet boleh menjawab 'tidak mengumpul sebarang data';
- Semakan: penyerahan pertama sering menunggu 1-7 hari; jika ditolak, ubah satu demi satu mengikut 'nota semakan' — sebab penolakan Apple biasanya ditulis dengan sangat khusus, cukup ikut sahaja;
- TestFlight: sebelum muat naik, kirim dahulu versi ujian kepada rakan untuk ujian dalaman (paling banyak 10000 orang), kumpulkan satu pusingan maklum balas barulah serahkan secara rasmi — sungguh berbau profesional.

#### 5. Cara membuat bahan kedai: tanggapan pertama menentukan muat turun

Halaman kedai ialah etalase yang dilihat pengguna semasa 'membelah kedai'. Tiga bahan menentukan tanggapan pertama:

- Ikon: 1024×1024, jangan gunakan tangkapan skrin sambil lewa. Tiada kemahiran reka bentuk? Jana grafik ringkas dengan alat AI; barulah layak jika masih dapat dikenali dengan sekali pandang walaupun dikecilkan pada skrin utama;
- Tangkapan skrin: sekurang-kurangnya 2 set (saiz utama iPhone), memaparkan senario fungsi paling teras; setiap satu disertai satu ayat teks berbahasa manusia ('catat sekelip mata' sepuluh kali lebih baik daripada 'penyelesaian pengurusan kewangan yang cekap');
- Huraian: ayat pertama menjelaskan 'apa ini + untuk siapa'; jangan menimbunkan 'paling profesional, paling hebat' — kejujuran lebih berkesan daripada pembesaran.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Praktik: 'Hantar' buku rekod perbelanjaan sekali

#### 6. Senarai ringkas pelaporan ranap dan pengoptimuman prestasi

Sebelum App dimuat naik, dua perkara ini wajar meluangkan setengah jam masing-masing:

##### 1. Pemantauan ranap

App tidak ranap semasa anda menguji tidak bermakna ia tidak akan ranap pada telefon pengguna. Apple menyediakan laporan ranap percuma dalam Xcode Organizer (akaun berbayar boleh melihat log ranap peranti sebenar); penyelesaian yang lebih senang ialah menyepadukan SDK pihak ketiga (seperti Firebase Crashlytics). Muat naik tanpa pemantauan ranap sama seperti memandu dengan mata terpejam.

##### 2. Empat semakan kendiri prestasi

1. Senarai guna LazyVStack / List: senarai panjang jangan gunakan VStack biasa secara keras — pemuatan malas ialah pelajaran pertama prestasi;
2. Imej jangan paksa masuk imej asal: guna AsyncImage (imej jauh) dan cache sistem; imej asal 5MB cukup untuk membekukan model lama;
3. Jangan lakukan kerja berat pada urutan utama: rangkaian dan fail besar semuanya melalui async/await;
4. Ukur dengan Instruments: penganalisis prestasi terbina dalam Xcode (Time Profiler, semakan kebocoran memori) — ukur dahulu, kemudian barulah optimumkan, jangan ikut perasaan.

{class="mt-1"}
(1) Tambah 3 ujian unit bagi logik seperti parseAmount (jalankan hijau dengan ⌘U); (2) guna titik sekatan untuk menangkap sendiri satu ranap buatan sendiri dan membaikinya; (3) Product → Archive bungkus satu pakej, melalui TestFlight jemput rakan untuk ujian dalaman; (4) ada kelapangan? Daftar akaun pembangun dan serahkan buku rekod perbelanjaan untuk dimuat naik benar-benar. Tiga langkah pertama boleh siap malam ini juga.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan bab ini

- Tiga senjata penyahpepijatan: log print, titik sekatan, pratonton SwiftUI dan pemeriksa view
- XCTest: ujian unit (⌘U) + ujian UI + ujian manual, sudah disediakan dalam templat
- Pemeteraian: akaun percuma pemeteraian automatik (diperbaharui setiap 7 hari); akaun berbayar diperlukan untuk pengedaran
- Pembungkusan: Generic iOS Device + Archive + Distribute; sijil wajib dibuat sandaran
- Enam langkah muat naik: daftar → bahan → muat naik → soal selidik privasi → semakan → terbit; ujian dalaman TestFlight dahulu
:::
