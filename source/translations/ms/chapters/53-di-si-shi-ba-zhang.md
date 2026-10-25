---
id: di-si-shi-ba-zhang
num: 48
part: an-zhuo-kai-fa-pian
nav: Bab 48: Mengenali Android—Daripada Sistem Pengendalian kepada Ekosistem Pembangunan
toc: default
kind: chapter
---

### Bab 48: Mengenali Android — Daripada Sistem Operasi kepada Ekosistem Pembangunan

{class="chapter-intro mb-4"}
Tahniah kerana membuat keputusan ini — daripada "orang yang bermain telefon" kepada "orang yang membina aplikasi telefon". Sebelum bertindak, mari bentangkan peta dahulu: dari mana datangnya Android? Mengapa pembangun sedunia menulis aplikasi untuknya? Dan apa yang berlaku sepanjang perjalanan sebuah App daripada jari anda menaip papan kekunci hingga sampai ke telefon pengguna?

#### 1. Asal usul Android: daripada "robot kecil" kepada "sistem terbesar di dunia"

Kisah Android bermula pada 2003 — seorang jurutera bernama Andy Rubin menubuhkan syarikat Android dengan matlamat yang sederhana: membina sistem operasi pintar yang "lebih faham kamera". Kemudian Google membelinya pada 2005; pada 2007, bersama-sama puluhan pengeluar, ditubuhkan Open Handset Alliance (OHA); dan pada September 2008, telefon Android pertama, HTC Dream (G1), dilancarkan secara rasmi.

Kisah selepasnya sudah semua orang tahu: menjelang 2026, Android ialah sistem operasi mudah alih dengan pangsa pasaran terbesar di dunia, dengan jumlah peranti aktif mencecah bilion. Telefon anda, kotak TV, skrin besar dalam kereta dan jam pintar — kemungkinan besar semuanya berjalan atas Android. Apa maksudnya? Maksudnya, setiap baris kod yang anda tulis mempunyai peluang digunakan oleh paling ramai orang di dunia.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tip: Gen sumber terbuka Android

{class="mt-1"}
Kod teras Android (AOSP, Android Open Source Project) ialah sumber terbuka — mana-mana pengeluar boleh mengambilnya untuk diubah suai dan diperibadikan. Itulah sebabnya Xiaomi ada MIUI (kini dipanggil HyperOS), Huawei ada lapisan keserasian HarmonyOS dan Samsung ada One UI. Ini perkara baik untuk pembangun: yang anda pelajari ialah "pembangunan Android", bukan "pembangunan sesuatu jenama" — satu set kemahiran, boleh digunakan di merata tempat.
:::

Evolusi nombor versi juga menarik: bermula dengan Cupcake (kek cawan) 1.5, setiap versi besar dinamakan sempena pencuci mulut — Donut, Eclair, Froyo, Gingerbread... sehinggalah Android 10 pada 2019 baharu ditukar kepada nombor tulen. Sehingga Ogos 2026, versi rasmi terkini ialah Android 17, manakala "versi sokongan minimum" yang sebenarnya perlu anda ambil peduli semasa membangun — App arus utama biasanya menetapkannya antara Android 8 (API 26) dan Android 10 (API 29); dengan menyokong peranti beberapa tahun lalu, barulah pangkalan pengguna anda cukup besar.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Versi</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Kod nama/tahun</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Perkara penting bagi pembangun</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 8 (API 26)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Oreo · 2017</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Saluran pemberitahuan, had latar belakang — garis minimum bagi banyak peranti lama</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 10 (API 29)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2019</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Storan berperingkat (scoped storage) muncul; peraturan akses fail berubah besar</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 12 (API 31)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2021</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pengambilan warna dinamik Material You; peningkatan besar rupa antara muka</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 13 (API 33)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2022</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kebenaran pemberitahuan semasa runtime; pop-up bertanya "benarkah hantar pemberitahuan"</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 14-15 (API 34-35)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2023-2024</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kembali ramalan (predictive back), halaman 16KB, privasi makin ketat</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android 16-17 (API 36-37)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2025-2026</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Rentak versi kecil lebih pantas; integrasi keupayaan AI (seperti sambungan Gemini)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Sejarah ringkas versi Android (sehingga Ogos 2026; tumpuan utama pembangunan)

#### 2. Menulis dengan bahasa apa: Java atau Kotlin?

Dalam sejarah pembangunan Android, dua bahasa arus utama pernah muncul. Java ialah "warga tua pengasas" — digunakan sejak Android dilahirkan; Kotlin ialah "warganegara kelas pertama" yang dilantik Google pada 2017, dan sejak 2019 pihak rasmi menyatakan jelas "Kotlin dahulu" (Kotlin-first). Menjelang 2026, hampir semua projek baharu menggunakan Kotlin, dan kebanyakan projek lama juga sedang berhijrah sedikit demi sedikit.

Terus terang sahaja: jika anda benar-benar sifar asas, belajar Kotlin terus; jangan pusing belakang untuk menyentuh Java. Tiga sebabnya: pertama, jumlah kod Kotlin 30%-40% lebih sedikit daripada Java (fungsi yang sama, Kotlin lebih pendek dan jelas); kedua, ia secara semula jadi melindungi daripada "null pointer", mimpi ngeri pemula; ketiga, semua tutorial moden, dokumentasi rasmi dan alat pengaturcaraan AI (masih ingat buku pengaturcaraan AI kita?) semuanya berpandukan Kotlin. Java hanya akan anda jumpa semasa menyelenggara projek lama atau membaca kod lama.

::: div .grid .md:grid-cols-2 .gap-3 .my-3
::: div .border .rounded-md .p-3 .border-t-4 .border-t-red-500
{class="vs-title"}
Gaya Java (versi berjela)

{class="font-mono text-xs leading-relaxed"}
public class MainActivity extends Activity {<br>&nbsp;&nbsp;@Override<br>&nbsp;&nbsp;protected void onCreate(Bundle b) {<br>&nbsp;&nbsp;&nbsp;&nbsp; super.onCreate(b);<br>&nbsp;&nbsp;&nbsp;&nbsp; setContentView(R.layout.activity);<br>&nbsp;&nbsp;}<br>}
:::

::: div .border .rounded-md .p-3 .border-t-4 .border-t-green-500
{class="vs-title"}
Gaya Kotlin (versi ringkas)

{class="font-mono text-xs leading-relaxed"}
class MainActivity : ComponentActivity() {<br>&nbsp;&nbsp;override fun onCreate(b: Bundle?) {<br>&nbsp;&nbsp;&nbsp;&nbsp; super.onCreate(b)<br>&nbsp;&nbsp;&nbsp;&nbsp;setContent { App() }<br>&nbsp;&nbsp;}<br>}
:::
:::

Untuk perkara yang sama, Kotlin menjimatkan seguni kurungan kerinting dan kod templat. Bab 50 kita akan mempelajarinya secara rasmi; buat masa ini anda hanya perlu ingat: "bahasa kebangsaan" pembangunan Android dipanggil Kotlin.

#### 3. Bagaimana sebuah App dilahirkan?

Ramai orang sangka "membangun App" ialah membuka komputer dan menaip kod secara berlebihan. Sebenarnya, daripada idea hingga ke telefon pengguna, sebuah App secara kasarnya melalui talian pengeluaran seperti berikut:

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-lightbulb mr-1"></i> Idea</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center">📐 Reka bentuk (paparan+fungsi)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-keyboard mr-1"></i> Menulis kod</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hammer mr-1"></i> Kompilasi dan bungkus (APK/AAB)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-flask mr-1"></i> Ujian (emulator+peranti sebenar)</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-rocket mr-1"></i> Terbitkan (kedai/pakej pemasangan)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Rajah 1: Aliran penuh sebuah App Android daripada idea hingga pelancaran
:::

Dalam aliran ini, ada dua konsep yang perlu anda kenali sekarang:

- APK: format pakej pemasangan aplikasi Android (.apk); hanya dua klik sudah boleh dipasang ke telefon, seperti .exe dalam Windows. Untuk ujian sendiri pada kebiasaannya atau dikongsi dengan kawan untuk mencuba, gunakan yang ini.
- AAB: Android App Bundle (.aab), "format pakej canggih" untuk pelancaran di Google Play. Kedai akan memotongnya secara dinamik mengikut model telefon pengguna supaya pakej yang dimuat turun lebih kecil untuk setiap orang. Tidak boleh dipasang sendiri; hanya boleh diserahkan kepada kedai.

Selain itu, anda juga akan sentiasa mendengar satu istilah: SDK (Software Development Kit, kit alat pembangunan perisian). Ia ialah satu set lengkap "peralatan pembangunan" yang disediakan secara rasmi oleh Android — termasuk pustaka API pelbagai versi, alat penyahpepijatan, imej emulator dan sebagainya. Kelas seperti Activity dan Button yang anda panggil semasa menulis kod semuanya datang daripada SDK.

#### 4. Gambaran menyeluruh teknologi Android: "senarai senjata" anda

Sebelum belajar secara rasmi, kenali dahulu persediaan standard projek Android arus utama pada 2026 — tidak mengapa jika anda belum memahami senarai ini; setelah selesai menghabiskan seluruh buku dan membaca semula, semuanya akan terang dengan jelas:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Lapisan</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Pilihan arus utama (2026)</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Untuk apa digunakan</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bahasa</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotlin 2.x</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bahasa untuk menulis logik</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Antara muka</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Jetpack Compose + Material 3</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Melukis antara muka dengan kod (garis utama buku ini)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Seni bina</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MVVM + ViewModel</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Memisahkan antara muka dan logik supaya kod tidak berselerak</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Penyimpanan data</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Room (pangkalan data) + DataStore (konfigurasi)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menyimpan data ke dalam telefon</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Rangkaian</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Retrofit + OkHttp + korutin Kotlin</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bercakap dengan pelayan</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Alat binaan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Gradle + Kotlin DSL</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mengubah kod menjadi pakej pemasangan</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Persekitaran pembangunan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android Studio</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">IDE "pakej lengkap" rasmi Google</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Sekilas pandang tindanan teknologi Android arus utama 2026

Jangan gentar dengan rentetan istilah Inggeris ini. Ia seperti periuk belanga dan pinggan mangkuk di dapur — buat masa ini anda hanya perlu tahu "memasak perlu masuk dapur"; cara menggunakan setiap alat akan dibongkarkan satu demi satu dalam bab-bab berikutnya. Dan berita baiknya: semasa mencipta projek baharu, Android Studio akan menyediakan keseluruhan set ini secara automatik untuk anda; anda hanya perlu fokus memasak.

#### 5. Android vs iOS: "pelajaran memilih pihak" pertama bagi pembangun

Mungkin anda memegang peranti Android dan Apple secara serentak. Sebagai pembangun, perbezaan pengalaman kedua-dua pihak berbaloi difahami lebih awal — bukan pilihan kubu "mana yang lebih baik", tetapi kiraan realistik "pihak mana lebih sesuai untuk anda memulakan langkah":

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Dimensi</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Pembangunan Android</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Pembangunan iOS</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Komputer pembangunan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Windows / Mac / Linux semuanya boleh</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mesti Mac (Xcode eksklusif)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Alat pembangunan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Android Studio (percuma)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Xcode (percuma) + yuran tahunan pelancaran kedai 99 dolar AS</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Semakan pelancaran</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Longgar; beberapa jam hingga beberapa hari</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ketat; 1-7 hari adalah lazim</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pasang pada peranti untuk mencuba</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">APK bebas diedarkan dan bebas dipasang</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pengedaran terhad, ujian perlukan penandatanganan/TestFlight</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Persekitaran pendapatan</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Terutamanya iklan/saluran dalam negara</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tabiat pembelian dalam apl di App Store lebih baik</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kos pembelajaran</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Banyak konsep (empat komponen utama dan sebagainya)</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ekosistem tertutup tetapi sistem seragam, dokumentasi berkualiti</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Perbandingan laluan pembangunan Android dan iOS (Ogos 2026)

Jujur sahaja: jika komputer anda bukan Mac, soalan ini langsung tidak perlu difikirkan — Android adalah satu-satunya pilihan. Jika anda ada Mac, Bahagian 8 dan 9 buku ini boleh dibaca secara berdampingan; cara berfikir pengaturcaraannya serupa, jadi selepas menguasai satu pihak, mempelajari pihak yang satu lagi akan jauh lebih pantas.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mari cuba: Lihat 'Android' dalam telefon anda

{class="mt-1"}
Buka [Tetapan] → [Mengenai Telefon] pada telefon anda (atau 'Mengenai Peranti'), cari baris 'Versi Android' — ketik beberapa kali berturut-turut dan anda boleh mencetuskan permainan easter egg sistem. Catat nombor versi anda, dan rujuk jadual versi di atas untuk melihat generasinya. Telefon anda itulah 'peranti ujian pembangunan' pertama anda.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan Bab

- Android lahir pada 2008; pada 2026 ia ialah sistem mudah alih dengan bahagian pasaran terbesar di dunia, dengan peranti aktif berbilion
- Versi rasmi terkini ialah Android 17; aplikasi arus utama menyokong sekurang-kurangnya Android 8-10 supaya pangkalan pengguna cukup besar
- Semua projek baharu guna Kotlin: kod kurang 30%+, elak null pointer, pilihan rasmi
- APK dipasang sendiri, AAB untuk kedai; SDK ialah kit peralatan pembangunan rasmi
- Tindanan teknologi standard 2026: Kotlin + Compose + MVVM + Room + Retrofit + Gradle + Android Studio
:::
