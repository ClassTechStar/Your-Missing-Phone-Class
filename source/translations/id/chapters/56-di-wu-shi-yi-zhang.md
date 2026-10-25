---
id: di-wu-shi-yi-zhang
num: 51
part: an-zhuo-kai-fa-pian
nav: Bab 51: Pengembangan Antarmuka—Pengenalan Jetpack Compose
toc: default
kind: chapter
---

### Bab 51: Pengembangan Antarmuka—Pengantar Jetpack Compose

{class="chapter-intro mb-4"}
Antarmuka adalah segala sesuatu yang dilihat pengguna. Sebelum Compose muncul, antarmuka Android ditulis dengan XML—rumit seperti mengerjakan soal isian; pada 2021 Google merilis Jetpack Compose: antarmuka 'digambar' langsung dengan kode Kotlin, apa yang terlihat itulah hasilnya—ubah satu baris kode, pratinjau langsung menyegar. Memasuki 2026, Compose sudah menjadi arus utama mutlak proyek-proyek baru. Bab ini kita belajar 'menggambar'.

#### 1. Cara Berpikir Compose: Antarmuka Adalah Fungsi

Inti pemikiran Compose dalam satu kalimat: antarmuka = fungsi. Setiap hal yang bisa tampil di layar (teks, tombol, gambar) adalah 'fungsi composable' (Composable), ditandai dengan @Composable. Menyusunnya bertingkat seperti balok susun, itulah antarmuka.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Tampilan Compose pertama</span><span class="dots">···</span>
:::

```
@Composable
fun Greeting(name: String) {
    Text(text = "Halo, $name!")     // Satu "balok teks"
}

// Komposisi bersarang: balok besar membungkus balok kecil
@Composable
fun HomeScreen() {
    Column {                          // Disusun vertikal
        Greeting(name = "Zhang San")
        Greeting(name = "Li Si")
        Button(onClick = { /* apa yang dilakukan saat diklik */ }) {
            Text("Tekan aku")
        }
    }
}
```
:::

Perhatikan 'topi' @Composable—ia memberi tahu kompiler 'ini balok susun antarmuka'. Baloknya bisa disusun bertingkat tanpa batas, itulah seluruh rahasia Compose.

#### 2. Komponen Dasar: Teks, Tombol, Kolom Input, Gambar

Komponen Compose adalah 'balok-baloknya'; empat di antaranya paling sering dipakai:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Komponen</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Fungsinya Apa</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Parameter Wajib</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menampilkan teks</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">text (teks yang ditampilkan)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Tombol</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onClick (callback saat ditekan)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kolom input</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">value, onValueChange (callback saat input berubah)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Image</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Menampilkan gambar</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">painter (sumber daya gambar)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Empat komponen dasar Compose

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Contoh komponen dasar</span><span class="dots">···</span>
:::

```
@Composable
fun BasicWidgets() {
    Column {
        Text(text = "Ini sebuah teks")
        Button(onClick = { println("Ditekan") }) {
            Text("Tombol")
        }
        var input by remember { mutableStateOf("") }
        TextField(
            value = input,
            onValueChange = { input = it },
            label = { Text("Ketik sesuatu") }
        )
    }
}
```
:::

Pada dua baris kolom input muncul remember { mutableStateOf("") }—itulah 'sihir state' milik Compose, akan dibahas tuntas di bagian 5 bab ini. Sekarang cukup kenalan dulu.

#### 3. Trio Tata Letak: Column, Row, Box

Komponen sudah ada, bagaimana menatanya? Ingat tiga 'kotak' ini:

- Column: menyusun ke bawah (seperti antre mengambil makanan);
- Row: menyusun menyamping (seperti duduk berjajar);
- Box: menyusun menumpuk (seperti kartu poker ditumpuk, cocok untuk lencana sudut dan lapisan penutup).

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Trio layout</span><span class="dots">···</span>
:::

```
Column {
    Text("Baris pertama")
    Row {
        Text("Kiri")
        Text("Kanan")
    }
    Box {
        Text("Lapisan bawah")
        Text("Lencana kecil yang menumpuk di atas")
    }
}
```
:::

Ingin tata letaknya lebih cantik? Tambahkan Modifier (pemberi efek) pada komponen—ia seperti 'menata rias' balok susun:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Jurus Modifier yang sering dipakai</span><span class="dots">···</span>
:::

```
Text(
    text = "Teks yang menarik",
    modifier = Modifier
        .padding(16.dp)          // beri ruang di sekeliling
        .fillMaxWidth()          // penuhi lebar
        .background(Color.Blue)  // warna latar
        .clickable { /* klik */ }// bisa diklik
)
// Rantai: dipanggil satu per satu, urutan berpengaruh (padding dulu baru latar, latar tidak termasuk jarak padding)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Perhatian: Urutan Modifier Ada Aturannya

{class="mt-1"}
padding(16.dp).background(Blue) dan background(Blue).padding(16.dp) hasilnya berbeda—yang pertama 'memberi ruang dulu lalu mengecat' (latar tidak menutupi margin), yang kedua 'mengecat dulu lalu memberi ruang' (latar ikut menutupi margin). Pemula paling sering salah menggambar 'pinggiran putih aneh' di sini. Kalau ragu, tukar saja urutannya dan pratinjau langsung memberi jawaban.
:::

#### 4. State: Membuat Antarmuka 'Hidup'

Antarmuka statis itu membosankan. Ingin angka bertambah 1 saat tombol ditekan, kolom input bisa diketik? Itu butuh state (keadaan). Aturan Compose: antarmuka selalu setia mencerminkan state; state berubah, antarmuka otomatis digambar ulang.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · State: penghitung klik</span><span class="dots">···</span>
:::

```
@Composable
fun Counter() {
    // remember + mutableStateOf: mengingat nilai yang bisa berubah ini
    var count by remember { mutableStateOf(0) }

    Column {
        Text(text = "Kamu menekan $count kali")
        Button(onClick = { count++ }) {   // ubah state
            Text("Tekan aku +1")                // tampilan menyegarkan sendiri
        }
    }
}
```
:::

Tiga baris kode, satu penghitung yang hidup. Di sinilah Compose terasa enak dibanding cara lama: tidak perlu 'menyegarkan antarmuka' secara manual, cukup ubah datanya. Ingat dua fungsi kunci: remember (menjaga nilai agar tidak terhapus saat antarmuka tersusun ulang) dan mutableStateOf (memberi tahu Compose 'jika nilai ini berubah, gambar ulang').

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hand-pointer mr-1"></i> Pengguna menekan</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> State berubah (count++)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> Compose mendeteksi perubahan</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> Menggambar ulang tampilan otomatis (recomposition)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Gambar 3: Aliran data satu arah 'state → antarmuka' pada Compose
:::

#### 5. Tema dan Mode Gelap: Sekali Atur, Berlaku Global

MyFirstAppTheme { ... } di proyek templat itulah temanya. Ia berbasis spesifikasi desain Material 3, membantumu mengatur warna, font, dan bentuk secara terpadu. Mendukung mode gelap hanya butuh tiga langkah:

1. Tentukan dua set palet warna terang/gelap di tema (templat sudah otomatis membuat ColorScheme);
2. Saat sistem beralih ke mode gelap, isSystemInDarkTheme() otomatis mendeteksinya;
3. Gunakan warna yang disediakan tema (misalnya MaterialTheme.colorScheme.primary), bukan nilai warna yang ditulis langsung.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tips: Warna Dinamis Material 3

{class="mt-1"}
Mulai Android 12, 'Material You' memungkinkan aplikasi mengambil warna dari wallpaper-mu. Templat Compose mendukungnya secara bawaan (dynamicColor). Aplikasimu akan 'berganti kostum' otomatis di ponsel tiap pengguna—itulah romantisme Android modern.
:::

#### 6. Pratinjau, Animasi, dan Live Edit: 'Cheat' Compose

Tiga 'cheat' Compose soal pengalaman pengembangan; sekali memakai, tidak mau kembali:

- Pratinjau @Preview: beri anotasi @Preview pada Composable, Android Studio langsung merender tampilannya di sisi kanan—ubah kode, hasilnya langsung terlihat, tidak perlu memasang ke ponsel tiap kali;
- Live Edit: Android Studio versi 2026 mendukung 'pembaruan panas' sebagian perubahan di emulator/ponsel asli; penyesuaian kecil seperti warna teks langsung berubah di perangkat dalam sekejap;
- API animasi: animateFloatAsState, AnimatedVisibility—beberapa baris kode membuat elemen berpindah dengan mulus—'kesan premium' sering hanya selisih puluhan baris ini.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Animasi yang dikuasai dalam 10 menit</span><span class="dots">···</span>
:::

```
@Composable
fun AnimatedBox() {
    var big by remember { mutableStateOf(false) }
    // Saat nilai berubah, otomatis bertransisi halus ke nilai target
    val size by animateDpAsState(if (big) 120.dp else 60.dp)

    Box(Modifier
        .size(size)
        .background(MaterialTheme.colorScheme.primary)
        .clickable { big = !big }
    )
}
```
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tips: Fungsi Dulu, Animasi Kemudian

{class="mt-1"}
Kebiasaan buruk pemula: 'antarmuka belum benar, tapi sudah sibuk memikirkan animasi'. Pastikan fungsinya jalan dulu, tambahkan efek gerak di akhir secara serentak—ini juga prinsip 'kesederhanaan di atas segalanya': animasi adalah pemanis, fungsi adalah penyelamat.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Praktik: Membuat 'Tombol Suasana Hati'

{class="mt-1"}
Ubah proyek templat menjadi pengganti suasana hati: satu tombol, setiap ditekan berputar antara 😀 senang → 😢 sedih → 😡 marah, teks dan warna latar ikut berubah. Petunjuk: pakai when untuk memilih teks dan warna berdasarkan state. Setelah jadi, kirim ke teman untuk dimainkan, panen gelombang pertama 'wow, kamu sudah bisa bikin aplikasi'.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan Bab Ini

- Pemikiran Compose: antarmuka = fungsi @Composable, disusun bertingkat seperti balok
- Empat komponen utama: Text / Button / TextField / Image
- Trio tata letak: Column menyusun ke bawah, Row menyusun menyamping, Box menyusun menumpuk
- Modifier berantai 'menata rias': padding, fillMaxWidth, background, clickable—urutannya bermakna
- State adalah jiwa: remember + mutableStateOf; data berubah, antarmuka otomatis digambar ulang
- Tema pakai Material 3 + warna dinamis; mode gelap sekali atur berlaku global
:::
