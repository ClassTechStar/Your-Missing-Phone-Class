---
id: di-wu-shi-yi-zhang
num: 51
part: an-zhuo-kai-fa-pian
nav: Bab 51: Pembangunan Antara Muka—Pengenalan Jetpack Compose
toc: default
kind: chapter
---

### Bab 51: Pembangunan Antara Muka — Pengenalan kepada Jetpack Compose

{class="chapter-intro mb-4"}
Antara muka ialah segala yang dilihat pengguna. Sebelum Compose muncul, antara muka Android ditulis dengan XML — rumit seperti soalan isi tempat kosong; pada 2021 Google memperkenalkan Jetpack Compose: terus 'melukis' antara muka dengan kod Kotlin, apa yang dilihat itulah yang diperoleh, ubah satu baris kod dan pratonton terus disegar semula. Menjelang 2026, Compose sudah menjadi arus perdana mutlak untuk projek baharu. Dalam bab ini, kita belajar 'melukis'.

#### 1. Pemikiran Compose: Antara Muka Ialah Fungsi

Pemikiran teras Compose dalam satu ayat: antara muka = fungsi. Setiap benda yang boleh dipaparkan pada skrin (teks, butang, imej) ialah satu 'fungsi boleh gubal' (Composable), ditanda dengan @Composable. Menyarangnya seperti bongkahan kayu itulah antara muka.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Paparan Compose pertama</span><span class="dots">···</span>
:::

```
@Composable
fun Greeting(name: String) {
    Text(text = "Hai, $name!")     // Satu "balok teks"
}

// Komposisi bersarang: balok besar membungkus balok kecil
@Composable
fun HomeScreen() {
    Column {                          // Disusun menegak
        Greeting(name = "Zhang San")
        Greeting(name = "Li Si")
        Button(onClick = { /* apa dibuat selepas ditekan */ }) {
            Text("Tekan saya")
        }
    }
}
```
:::

Perhatikan 'topi' @Composable ini — ia memberitahu kompiler 'ini bongkahan antara muka'. Bongkahan boleh disarang tanpa had, dan itulah keseluruhan rahsia Compose.

#### 2. Komponen Asas: Teks, Butang, Kotak Input, Imej

Komponen Compose ialah 'bongkahan kayu'; inilah empat yang paling lazim:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3"><thead><tr class="bg-light dark:bg-gray-700"><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Komponen</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Untuk apa</th><th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Parameter wajib</th></tr></thead><tbody><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Text</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Papar teks</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">text (teks yang dipaparkan)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Button</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Butang</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">onClick (panggil balik ketikan)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">TextField</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Kotak input</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">value, onValueChange (panggil balik perubahan input)</td></tr><tr><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Image</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Papar imej</td><td class="border border-gray-300 dark:border-gray-600 px-3 py-2">painter (sumber imej)</td></tr></tbody></table>
```
:::

{class="text-xs text-gray-500 dark:text-gray-400 mb-3"}
Empat komponen asas Compose

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Contoh komponen asas</span><span class="dots">···</span>
:::

```
@Composable
fun BasicWidgets() {
    Column {
        Text(text = "Ini satu teks")
        Button(onClick = { println("Ditekan") }) {
            Text("Butang")
        }
        var input by remember { mutableStateOf("") }
        TextField(
            value = input,
            onValueChange = { input = it },
            label = { Text("Taip sesuatu") }
        )
    }
}
```
:::

Dalam dua baris kotak input itu muncul remember { mutableStateOf("") } — inilah 'sihir keadaan' (state) Compose, dijelaskan terperinci dalam Bahagian 5 bab ini. Buat sementara ini, cukup kenal muka dahulu.

#### 3. Set Tiga Susun Atur: Column, Row, Box

Komponen sudah ada, macam mana menyusunnya? Ingat tiga 'kotak' ini:

- Column: disusun menegak (seperti beratur mengambil makanan);
- Row: disusun mengufuk (seperti duduk bersebelahan);
- Box: ditindih (seperti kad poker disusun bersama, sesuai untuk lencana sudut dan topeng).

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Set tiga susun atur</span><span class="dots">···</span>
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
        Text("Lencana kecil tersusun di atas")
    }
}
```
:::

Mahu susun atur lebih menawan? Tambahkan Modifier (pengubah) pada komponen — ia umpama memberi 'solekan' kepada bongkahan kayu:

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Buah Modifier kerap guna</span><span class="dots">···</span>
:::

```
Text(
    text = "Teks yang menarik",
    modifier = Modifier
        .padding(16.dp)          // beri ruang sekeliling
        .fillMaxWidth()          // penuhi lebar
        .background(Color.Blue)  // warna latar
        .clickable { /* klik */ }// boleh diklik
)
// Rantaian: dipanggil satu demi satu, susunan berpengaruh (padding dahulu baru latar, latar tidak merangkumi jarak padding)
```
:::

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Perhatian: Susunan Modifier Ada Caranya

{class="mt-1"}
padding(16.dp).background(Blue) dan background(Blue).padding(16.dp) memberi hasil berbeza — yang pertama 'beri ruang dahulu, kemudian warna' (latar belakang tidak termasuk jidar), yang kedua 'warna dahulu, kemudian beri ruang' (latar belakang termasuk jidar). Pemula paling mudah tersilap melukis 'jidar putih pelik' di sini. Jika tidak pasti, tukar susunannya dan cuba; pratonton terus memberitahu jawapannya.
:::

#### 4. Keadaan: Menghidupkan Antara Muka

Antara muka statik tidak menarik. Mahu butang menambah +1 selepas ditekan, mahu kotak input boleh menaip? Anda perlukan keadaan (State). Peraturan Compose: antara muka sentiasa setia mencerminkan keadaan; keadaan berubah, antara muka dilukis semula secara automatik.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · State: pengira klik</span><span class="dots">···</span>
:::

```
@Composable
fun Counter() {
    // remember + mutableStateOf: mengingati nilai yang boleh berubah ini
    var count by remember { mutableStateOf(0) }

    Column {
        Text(text = "Anda menekan $count kali")
        Button(onClick = { count++ }) {   // ubah state
            Text("Tekan saya +1")                // paparan terus segar
        }
    }
}
```
:::

Tiga baris kod, satu pengira yang hidup. Inilah kelebihan Compose berbanding cara lama: tidak perlu 'segar semula antara muka' secara manual, ubah data sahaja. Ingat dua fungsi utama: remember (mengekalkan nilai supaya tidak dikosongkan semasa antara muka disusun semula) dan mutableStateOf (memberitahu Compose 'nilai ini berubah, lukis semula').

::: div .figure
:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-hand-pointer mr-1"></i> Pengguna menekan</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-primary bg-indigo-50 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-redo mr-1"></i> State berubah (count++)</span>
:::

:::inline div .flex .flex-wrap .items-center .justify-center .gap-2 .my-2
<span class="border-2 border-amber-500 bg-amber-50 text-amber-900 dark:bg-amber-950 dark:text-amber-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-brain mr-1"></i> Compose mengesan perubahan</span><span class="text-gray-400 mx-1">➜</span> <span class="border-2 border-green-500 bg-green-50 text-green-900 dark:bg-green-950 dark:text-green-200 rounded-md px-3 py-1 text-sm text-center"><i class="fas fa-palette mr-1"></i> Lukis semula paparan automatik (recomposition)</span>
:::

{class="text-xs text-gray-500 dark:text-gray-400 mt-1"}
Rajah 3: Aliran data satu hala 'keadaan → antara muka' Compose
:::

#### 5. Tema dan Mod Gelap: Konfigurasi Sekali, Berkuat Kuasa Global

MyFirstAppTheme { ... } dalam projek templat itulah tema. Ia berasaskan spesifikasi reka bentuk Material 3, membantu anda mengurus warna, fon dan bentuk secara menyeluruh. Menyokong mod gelap hanya perlu tiga langkah:

1. Takrifkan dua set skema warna cerah/gelap dalam tema (templat sudah menjana ColorScheme secara automatik);
2. Apabila sistem bertukar ke mod gelap, isSystemInDarkTheme() menilai secara automatik;
3. Guna warna yang disediakan tema (contohnya MaterialTheme.colorScheme.primary) dan bukannya nilai warna yang ditulis terus.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Petua: Pengambilan Warna Dinamik Material 3

{class="mt-1"}
'Material You' sejak Android 12 membolehkan aplikasi mendapatkan warna daripada kertas dinding anda. Templat Compose menyokongnya secara lalai (dynamicColor). Aplikasi anda akan 'bertukar pakaian' secara automatik pada telefon pengguna berbeza — itulah romantik Android moden.
:::

#### 6. Pratonton, Animasi dan Sunting Langsung: 'Kuasa Tambahan' Compose

Tiga 'kuasa tambahan' Compose dalam pengalaman pembangunan; sekali guna, sukar kembali:

- Pratonton @Preview: tambahkan anotasi @Preview pada Composable, Android Studio terus memaparkan antara muka di sebelah kanan — apa yang dilihat itulah yang diperoleh semasa mengubah kod, tidak perlu memasang ke telefon setiap kali;
- Suntingan langsung (Live Edit): Android Studio 2026 menyokong 'kemas kini panas' sebahagian perubahan pada emulator/peranti sebenar; penyesuaian kecil seperti mengubah warna teks berubah sekelip mata pada peranti;
- API animasi: animateFloatAsState, AnimatedVisibility — beberapa baris kod sudah cukup untuk membuat elemen beralih dengan lancar — 'kesan premium' sering cuma berbeza dengan puluhan baris ini.

::: div .code-block
:::inline div .code-head
<span>KOTLIN · Animasi dikuasai dalam 10 minit</span><span class="dots">···</span>
:::

```
@Composable
fun AnimatedBox() {
    var big by remember { mutableStateOf(false) }
    // Apabila nilai berubah, bertransisi secara halus ke nilai sasaran
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
Petua: Fungsi Dahulu, Animasi Kemudian

{class="mt-1"}
Penyakit lazim pemula: 'antara muka belum betul, dah sibuk fikirkan animasi'. Pastikan fungsi berjalan dahulu, barulah tambahkan kesan gerak secara menyeluruh pada akhirnya — ini juga prinsip 'ringkas itu utama': animasi ialah hiasan yang menambah nilai, fungsi ialah pertolongan di saat genting.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mari cuba: Buat 'Butang Mood'

{class="mt-1"}
Ubah projek templat menjadi penukar mood: satu butang, setiap ketikan berselang-seli antara 😀 gembira → 😢 sedih → 😡 marah, dengan teks dan warna latar belakang turut berubah. Petunjuk: guna when untuk memilih teks dan warna mengikut keadaan. Selepas siap, hantar kepada kawan untuk dimainkan, dan terimalah gelombang pertama 'wow, kau boleh buat aplikasi'.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan Bab

- Pemikiran Compose: antara muka = fungsi @Composable, disarang gaya bongkahan
- Empat komponen: Text / Button / TextField / Image
- Set tiga susun atur: Column menegak, Row mengufuk, Box bertindih
- Rantai Modifier 'solekan': padding, fillMaxWidth, background, clickable — susunannya bermakna
- Keadaan ialah jiwa: remember + mutableStateOf, ubah data maka antara muka dilukis semula secara automatik
- Tema guna Material 3 + warna dinamik, mod gelap dikonfigurasi sekali dan berkuat kuasa global
:::
