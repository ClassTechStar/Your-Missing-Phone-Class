---
id: di-shi-si-zhang
num: 14
part: ruan-jian-pian
nav: Bab 14: Topik Khas Pengurus Kata Laluan
toc: default
kind: chapter
---

### Bab 14: Topik Khas Pengurus Kata Laluan

{class="chapter-intro mb-4"}
2\. Prinsip kerja pengurus kata laluan

#### 1. Mengapa anda perlukan pengurus kata laluan?

: Semua kata laluan disimpan selepas disulitkan kuat, hanya anda boleh nyahsulit.

Kata laluan utama

#### 2. Prinsip kerja pengurus kata laluan

1. <strong>Isi automatik</strong>: Pada antara muka log masuk laman web atau App, pengurus kata laluan automatik isi kata laluan akaun.
2. <strong>Jana kata laluan</strong>: Boleh jana kata laluan rawak, kompleks, tingkatkan keselamatan.
3. <strong>3. Cadangan pengurus kata laluan utama</strong> Terbina dalam sistem:
4. <strong>iCloud Keychain</strong>: Pilihan utama pengguna ekosistem Apple. Integrasi tanpa jurang dengan Safari, App, percuma, selamat. Kekurangannya penggunaan merentas platform tak senang.

#### III. Pengenalan prinsip penyulitan

Fahami prinsip penyulitan pengurus kata laluan, boleh bantu anda tentukan sama ada pembekal perkhidmatan boleh dipercayai. Berikut dalam bahasa mudah terangkan beberapa konsep teras.

##### 1. Penyulitan AES-256

AES (Advanced Encryption Standard) adalah algoritma penyulitan simetri yang diiktiraf oleh NIST (Institut Standard dan Teknologi Kebangsaan AS), digunakan secara meluas oleh bank, tentera, kerajaan. "256" merujuk panjang kunci 256 bit — secara teori perlu masa melebihi umur alam semesta untuk pecah secara paksa. Pengurus kata laluan utama (1Password, Bitwarden, KeePass dll) semua guna AES-256 untuk menyulitkan perpustakaan kata laluan anda.

##### 2. Senibina pengetahuan sifar (Zero-Knowledge Architecture)

"Pengetahuan sifar" bukan bermakna pembekal perkhidmatan tidak simpan apa-apa, tetapi bermakna <strong>Penyulitan dan penyahsulitan semua dilakukan pada peranti tempatan anda, pelayan hanya simpan teks tersulit</strong>. Aliran khusus:

1. Anda masukkan kata laluan utama pada klien.
2. Klien guna kata laluan utama terbit kunci penyulitan (langkah ini selesai pada telefon/komputer anda).
3. Hanya teks tersulit sahaja dimuat naik ke pelayan.
4. Log masuk seterusnya, pelayan hantar teks tersulit, klien guna kata laluan utama penyahsulit semula.

Perkara utama:<strong>Kata laluan utama tidak pernah meninggalkan peranti anda</strong>, pelayan juga tiada. Jadi walaupun pembekal dihack, hacker dapat hanya teks tersulit yang tidak boleh disahsulit — kecuali mereka boleh teka kata laluan utama anda.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Mengapa "pengetahuan sifar" bermakna pembekal juga tidak nampak kata laluan anda?

{class="mt-1"}
Kerana kunci penyahsulit diterbitkan dari kata laluan utama anda, manakala kata laluan utama hanya wujud dalam fikiran anda, hanya diguna pada peranti tempatan. Pelayan pembekal tiada kata laluan utama, tiada kunci penyahsulit, hanya teks tersulit. Inilah sebabnya Bitwarden, 1Password dll pembekal sah semuanya nyatakan "kami juga tidak boleh nampak kata laluan anda" — bukan mereka tidak mahu nampak, tetapi secara teknikal tidak boleh.
:::

##### 3. Fungsi terbitan kunci: PBKDF2 dan Argon2

Kata laluan utama tidak boleh diguna terus sebagai kunci penyulitan — ia perlu melalui "fungsi terbitan kunci". Fungsi ini bertujuan <strong>Sengaja buat pengiraan perlahan</strong>, buat kos pecah paksa hacker terlalu tinggi untuk praktikal.

- <strong>PBKDF2</strong>: Standard lama, diguna secara meluas oleh iCloud Keychain, Bitwarden, LastPass dll. Melalui iterasi berulang (biasanya 100,000 kali ke atas) hash untuk melambatkan pecah.
- <strong>Argon2</strong>: Juara pertandingan hash kata laluan 2015, lebih moden daripada PBKDF2. Selain "penggunaan kuasa pengiraan" juga perkenalkan "penggunaan memori" — buat GPU/ASIC dll perkakasan khas juga susah pecah. Bitwarden, KeePassXC dll telah menyokong.

Bilangan iterasi lebih tinggi lebih selamat, tetapi kelajuan buka kunci juga lebih perlahan. Pembekal sah akan umumkan algoritma terbitan dan bilangan iterasi, untuk audit komuniti keselamatan.

##### 4. Amaran kes: Kebocoran data LastPass 2022

Ogos 2022, pengurus kata laluan lama LastPass umumkan persekitaran pembangunannya diceroboh; November tahun sama mendedahkan, hacker ambil sandaran perpustakaan kata laluan pengguna (teks tersulit). Pengajaran utama:

- <strong>Senibina pengetahuan sifar pertahankan garis asas</strong>: Kerana perpustakaan kata laluan itu sendiri tersulit, hacker dapat teks tersulit tetapi tidak boleh nyahsulit — syaratnya kata laluan utama pengguna cukup kuat.
- <strong>Pengguna kata laluan utama lemah paling bahaya</strong>: Hacker boleh pecah paksa luar talian kata laluan utama lemah, jadi pengguna kata laluan utama lemah atau berulang menghadapi risiko sebenar.
- <strong>Metadata juga bocor</strong>: Walaupun kandungan kata laluan tersulit, tetapi URL laman, nota dll metadata mungkin tidak tersulit, akan dedahkan perkhidmatan mana pengguna guna.

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Belajaran dari LastPass

{class="mt-1"}
Pertama, kata laluan utama mesti panjang dan unik (disyorkan 16 karakter ke atas, termasuk huruf besar/kecil, nombor, simbol); Kedua, utamakan pembekal yang menyokong Argon2id, bilangan iterasi tinggi; Ketiga, akaun nilai tinggi (bank, e-mel) mesti aktifkan pengesahan kedua berasingan, jangan hanya bergantung pengurus kata laluan.
:::

#### IV. Cadangan pengurus kata laluan utama

##### : Senang untuk pengguna Android. Integrasi dengan Chrome, sistem Android, percuma.

- <strong>Huawei Password Vault</strong>: Terbina dalam sistem HarmonyOS, sesuai untuk pengguna Huawei.
- <strong>Alat profesional pihak ketiga:</strong> Bitwarden
- <strong>: Sumber terbuka percuma, fungsi kuat, menyokong semua platform. Sangat dicadangkan untuk pengguna yang mengutamakan privasi.</strong>1Password

##### : Antara muka cantik, fungsi kaya, sesuai untuk keluarga dan team. Berbayar.

- <strong>LastPass</strong>: Pengurus kata laluan lama, fungsi versi percuma terhad.
- <strong>KeePass</strong>: Storan tempatan sepenuhnya, sumber terbuka percuma. Sesuai untuk pengguna geek.
- <strong>4. Amalan terbaik penggunaan pengurus kata laluan</strong> Tetapkan kata laluan utama yang kuat
- <strong>: Kata laluan utama adalah garis pertahanan terakhir, pastikan tetapkan kata laluan yang panjang dan kompleks, dan ingat baik.</strong> Aktifkan pengesahan dua faktor

#### V. Penilaian sebenar kekuatan kata laluan

Pengurus kata laluan biasanya papar bar penunjuk "kekuatan kata laluan" (merah/kuning/hijau), tetapi penilaian ini selalunya hanya lihat panjang dan jenis aksara, tidak komprehensif. Untuk betul-betul tentukan kata laluan selamat atau tidak, perlu pertimbang "entropi" dan "sama ada telah bocor".

##### 1. Entropi (Entropy): Ukuran saintifik kekuatan kata laluan

"Entropi" ukur ketidakpastian kata laluan, unit adalah bit. Entropi lebih tinggi, bilangan percubaan pecah paksa lebih banyak.

- <strong>"123456"</strong>: Entropi sangat rendah, pecah serta-merta.
- <strong>"P@ssw0rd"</strong>: Nampak kompleks, tetapi muncul dalam semua senarai serangan kamus, entropi masih rendah.
- <strong>"correct horse battery staple"</strong>: Empat perkataan rawak, entropi kira-kira 44 bit, kesukaran pecah jauh melebihi "P@ssw0rd".
- <strong>16 aksara rawak (huruf besar+kecil+nombor+simbol)</strong>: Entropi kira-kira 100 bit, kuasa pengiraan semasa tidak boleh pecah paksa.

Kesimpulan:<strong>"Panjang + rawak" lebih penting daripada "simbol kompleks"</strong>. Inilah sebab kata laluan panjang rawak yang dijana pengurus kata laluan benar-benar selamat.

##### 2. HaveIBeenPwned: Semak kata laluan anda sama ada telah bocor

Diselenggara oleh penyelidik keselamatan Troy Hunt <a href="https://haveibeenpwned.com" class="text-primary hover:underline" target="_blank" rel="noopener">haveibeenpwned.com</a> Mengandungi akaun dan kata laluan yang bocor dalam kebocoran data besar lepas. Anda boleh:

1. Masukkan e-mel, semak akaun anda sama ada terdedah dalam kebocoran tertentu.
2. Guna fungsi Pwned Passwords semak kata laluan sama ada dalam pangkalan data bocor diketahui (pengurus kata laluan dan browser telah terbina dalam pertanyaan ini).

Jika kata laluan muncul dalam pangkalan data bocor,<strong>tidak kira nampak betapa kompleks mesti tukar serta-merta</strong>— kerana serangan kamus akan utamakan kata laluan diketahui ini.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-shield-alt mr-2"></i>Prinsip pertanyaan k-Anonimiti

{class="mt-1"}
Bimbang masukkan kata laluan di HaveIBeenPwned akan bocor lagi? Jangan bimbang. Pertanyaan moden guna protokol "k-anonimiti": browser hanya hantar 5 bit pertama hash kata laluan ke pelayan, pelayan pulangkan senarai hash bermula dengan 5 bit ini, banding secara tempatan. Maksudnya, pelayan tidak pernah nampak hash kata laluan penuh anda. 1Password, Bitwarden "pengesanan kata laluan bocor" semua berfungsi seperti ini.
:::

##### 3. Fungsi pemantauan terbina dalam pengurus kata laluan

- <strong>1Password Watchtower</strong>: Pantau real-time kata laluan lemah, berulang, bocor, luput, laman tidak guna 2FA, dan papar secara gred merah/orange/kuning.
- <strong>Bitwarden Vault Health</strong>: Versi percuma boleh lihat kata laluan lemah, berulang; versi berbayar boleh kesan kata laluan bocor (berdasarkan HaveIBeenPwned).
- <strong>Cadangan keselamatan iCloud Keychain</strong>: iOS Tetapan → Kata Laluan → Cadangan Keselamatan, akan maklum anda kata laluan mana muncul dalam kebocoran diketahui, mana berulang guna.
- <strong>Alat semak kata laluan Google Password Manager</strong>: Terbina dalam Chrome, boleh sekali semak kata laluan bocor, lemah, berulang.

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Sekarang semak: Adakah kata laluan anda selamat

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Buka haveibeenpwned.com, masukkan e-mel biasa anda, lihat muncul dalam kebocoran mana.
2. Pengguna iPhone: Tetapan → Kata Laluan → Cadangan Keselamatan, proses amaran merah satu demi satu.
3. Pengguna Chrome: Tetapan → Kata Laluan → Semak Kata Laluan, ikut arahan ubah.
4. Pengguna 1Password/Bitwarden: Buka Watchtower/Health Reports, utamakan proses "bocor" dan "berulang".
:::

#### VI. Passkey: Login tanpa kata laluan masa depan

2024-2026, teknologi kata laluan sedang mengalami revolusi —<strong>Passkey (kunci laluan)</strong> berpotensi ganti sepenuhnya kata laluan tradisional. Apple, Google, Microsoft tiga platform utama bersama dorong, disokong oleh FIDO Alliance dan W3C, ini perubahan cara login terbesar dalam beberapa dekad.

##### 1. Apakah Passkey?

Passkey berasaskan standard FIDO2 / WebAuthn, guna <strong>Pasangan kunci pada peranti</strong> ganti kata laluan. Prinsip boleh dipermudahkan:

- Telefon anda jana sepasang kunci:<strong>Kunci awam</strong>(daftar ke laman web) + <strong>Kunci peribadi</strong>(sentiasa dalam cip keselamatan peranti anda).
- Apabila log masuk, laman web hantar "cabaran", telefon anda guna kunci peribadi tandatangan, kemudian laman web guna kunci awam sahkan.
- Sebelum tandatangan perlu anda lalui pengecaman biometrik (Face ID / cap jari) atau PIN peranti sahkan identiti.
- Sepanjang proses,<strong>tiada apa-apa kata laluan dihantar dalam rangkaian</strong>.

##### 2. Passkey vs kata laluan tradisional

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                        <thead>
                            <tr class="bg-light dark:bg-gray-700">
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Dimensi</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Kata laluan tradisional</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Passkey</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Anti pancingan</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lemah, laman pancingan boleh curi kata laluan</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Semula jadi anti pancingan, kunci peribadi hanya tandatangan untuk domain sebenar</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Kesan kebocoran pelayan</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Hash kata laluan mungkin dipecah</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pelayan hanya simpan kunci awam, bocor tiada kesan</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Kemudahan</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Perlu ingat/taip/urus</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Face ID/cap jari log masuk satu saat</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Serangan ulangan</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mungkin ditangkap middleman ulang</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Setiap tandatangan sekali guna, tidak boleh ulang</td>
                            </tr>
                        </tbody>
                    </table>
```

##### 3. Status sokongan setiap platform

- <strong>Apple iCloud Keychain Passkey</strong>: iOS 16+ / macOS Ventura+ sokong native, Passkey boleh segerak antara semua peranti log masuk Apple ID sama, peranti baharu log masuk laman tidak perlu cipta semula.
- <strong>Google Password Manager Passkey</strong>: Android + Chrome sokong native, Passkey disimpan dalam akaun Google, segerak merentas peranti Android; sejak 2023 akaun peribadi Google telah menyokong login Passkey.
- <strong>Microsoft</strong>: Windows 11 / Edge telah menyokong Passkey; akaun Microsoft, Outlook, Office dll perkhidmatan beransur buka login Passkey, dan boleh urus dalam Microsoft Authenticator.
- <strong>1Password / Bitwarden</strong>: Telah menyokong cipta, simpan, segerak merentas platform Passkey, buat anda tidak terhad satu ekosistem.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Segerak merentas peranti adalah pencapaian utama

{class="mt-1"}
Masalah terbesar Passkey awal adalah "terikat satu peranti" — tukar telefon perlu cipta semula. Sejak 2023 Apple, Google, Microsoft capai segerak awan Passkey: iCloud Keychain segerak merentas Apple, Google Password Manager segerak merentas Android. 1Password dll pihak ketiga pula hubungkan segerak merentas ekosistem. Ini bermakna Passkey telah ada kepraktikal untuk ganti kata laluan.
:::

##### 4. Cara cipta dan guna Passkey pada telefon

<strong>Laluan iOS (iPhone):</strong>

1. Pada laman sokong Passkey (seperti Google, Microsoft, Amazon, eBay, PayPal) halaman keselamatan akaun pilih "Tambah Passkey".
2. Sistem popup Face ID / Touch ID pengesahan, selepas lulus Passkey auto dijana dan disimpan ke iCloud Keychain.
3. Log masuk seterusnya laman ini, masukkan nama pengguna kemudian pilih "Guna iPhone log masuk", Face ID sekali imbas selesai.
4. Pintu pengurusan: Tetapan → Kata Laluan → cari laman berkenaan, nampak item Passkey.

<strong>Laluan Android:</strong>

1. Pada laman sokong Passkey halaman keselamatan akaun pilih "Tambah Passkey".
2. Google Password Manager popup → pilih akaun Google anda → kunci skrin pengesahan (cap jari/pola/PIN).
3. Passkey auto disimpan ke Google Password Manager, segerak merentas peranti Android akaun sama.
4. Log masuk seterusnya, pilih "Guna Passkey", kunci skrin buka sekali selesai.
5. Pintu pengurusan: Android Tetapan → Kata laluan, kunci dan auto-isi → Password Manager → google.com.

##### 5. Login Passkey merentas peranti

Jika anda log masuk laman yang hanya ada Passkey di iPhone pada komputer Windows, boleh imbas kod sahkan:

1. Halaman log masuk laman pilih "Guna Passkey".
2. Pilih "Guna peranti lain".
3. Komputer papar kod QR, guna iPhone imbas.
4. iPhone popup Face ID pengesahan, sahkan selepas laman selesai log masuk pada komputer.

Proses ini melalui komunikasi penyulitan dwi Bluetooth+Internet, kunci peribadi Passkey tidak akan meninggalkan iPhone anda.

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Cuba sekarang: Alami login tanpa kata laluan

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Log masuk akaun Google → Keselamatan → Passkey → Tambah Passkey, alami Face ID/cap jari log masuk.
2. Log masuk akaun Microsoft → Keselamatan → Pilihan keselamatan lanjutan → Tambah Passkey.
3. Pada Taobao, JD, eBay, PayPal dll perkhidmatan yang telah sokong Passkey cuba baharu.
4. Kekalkan kata laluan tradisional sebagai sandaran, beransur pindah akaun nilai tinggi ke Passkey.
:::

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Cadangan peralihan

{class="mt-1"}
Passkey belum ganti sepenuhnya kata laluan — banyak laman masih dalam fasa "Passkey + kata laluan" wujud serentak. Cadangan: akaun nilai tinggi utamakan aktifkan Passkey, tetapi <strong>jangan terus padam kata laluan tradisional</strong>, kekal sebagai sandaran; pada masa yang sama terus guna pengurus kata laluan, kerana tidak semua laman sokong Passkey. Anggap Passkey sebagai "tambahan kuat pengurus kata laluan" bukan "ganti serta-merta".
:::

#### VII. Kunci keselamatan perkakasan

Jika keperluan keselamatan anda lebih tinggi daripada pengguna biasa — contoh pegang jumlah besar cryptocurrency, adalah eksekutif/wartulis/aktivis, atau lindungi akaun teras entreprise — kunci keselamatan perkakasan adalah pilihan lebih boleh dipercayai daripada SMS pengesahan.

##### 1. Apakah kunci keselamatan perkakasan?

Kunci perkakasan adalah peranti fizikal (rupa flash drive), cip keselamatan dalaman simpan kunci peribadi anda, perlu sentuhan fizikal atau NFC untuk selesai pengesahan. Produk wakil:

- <strong>YubiKey</strong>(Syarikat Yubico): Paling utama, sokong FIDO2/WebAuthn, U2F, OTP, PIV, OpenPGF, USB-C / USB-A / NFC pelbagai interface. Siri 5 $50-70.
- <strong>Google Titan</strong>: Keluaran Google, USB-C + NFC / Bluetooth, kira-kira $30-40.
- <strong>OnlyKey</strong>: Alternatif sumber terbuka, sokong pelbagai protokol.
- <strong>Alternatif domestik</strong>: Seperti Feitian ePasskey, harga lebih berpatutan.

##### 2. Mengapa kunci perkakasan lebih selamat daripada SMS pengesahan?

- <strong>Anti pancingan</strong>: Sama seperti Passkey, kunci perkakasan hanya respons kepada domain sebenar, laman pancingan tidak boleh tipu kod pengesahan.
- <strong>Anti culik SIM</strong>: SMS pengesahan boleh ditangkap melalui serangan SIM-swap, kunci perkakasan tidak perlu nombor telefon.
- <strong>Anti middleman</strong>: Protokol FIDO2 setiap tandatangan mengandungi nilai cabaran, tidak boleh ulang.
- <strong>Pemisahan fizikal</strong>: Kunci peribadi sentiasa dalam cip perkakasan, malware walaupun ceroboh komputer anda juga tidak boleh baca.

##### 3. Senario sesuai

- Akaun bursa cryptocurrency, pemulihan dompet.
- SSO entreprise, VPN kerja jauh, SSH log masuk pelayan.
- E-mel, GitHub, media sosial dll "akaun utama" — sekali ceroboh boleh reset semua akaun lain.
- Wartawan, peguam, eksekutif dll orang sensitif tinggi.

##### 4. Cara konfigur kunci perkakasan sebagai pengesahan kedua

Contoh akaun Google + YubiKey:

1. Beli YubiKey (disyorkan beli dua sekali, satu harian, satu sandaran, simpan di lokasi berbeza).
2. Log masuk myaccount.google.com → Keselamatan → Pengesahan dua langkah.
3. Pilih "Tambah kunci keselamatan" → Masukkan YubiKey ke port USB-C atau dekatkan NFC telefon.
4. Ikut arahan sentuh titik logam YubiKey selesai pendaftaran.
5. Disyorkan daftar kunci sandaran kedua.
6. Dalam tetapan "pengesahan dua langkah", tetapkan kunci perkakasan sebagai kaedah pengesahan utama, SMS pengesahan sebagai sandaran.

Laman utama yang menyokong: Google, GitHub, Microsoft, Apple ID, Facebook, Twitter, Dropbox, GitLab, AWS, Coinbase, Binance dll.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Strategi dwi-kunci

{class="mt-1"}
Risiko terbesar kunci perkakasan adalah "hilang". Cadangan: ② serentak daftar dua kunci berbeza; ③ satu bawa (keychain), satu simpan di rumah dalam safe atau bank deposit box; ④ sesetengah laman benarkan "kod pemulihan sandaran" dicetak simpan luar talian. Ini jika kunci utama hilang, juga tidak akan dikunci keluar akaun secara kekal.
:::

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Saluran pembelian perlu berhati-hati

{class="mt-1"}
Mesti beli dari kedai rasmi atau ejen sah, jangan beli kunci terpakai atau sumber tidak diketahui — secara teori perkakasan yang telah diprapasang mungkin telah ditanam pintu belakang. Firmware YubiKey tidak boleh dikemas kini selepas kilang, tetapi Yubico akan terus tolak pengumuman keselamatan, ikut laman web rasmi mereka.
:::

#### VIII. Perkongsian kata laluan keluarga/pasukan

Dalam senario keluarga, Netflix, WiFi rumah, router backend, kunci pintar perlu berkongsi keluarga; senario pasukan, pelayan, pangkalan data, akaun media sosial perlu kerjasama berbilang orang.<strong>Hantar kata laluan melalui WeChat, tulis dalam dokumen kongsi adalah amalan berisiko tinggi</strong>— sekali rekod sembang atau kebenaran dokumen bocor, kata laluan bocor.

##### 1. "Vault kongsi" 1Password

1Password adalah produk contoh perkongsian keluarga dan pasukan. Mekanisme terasnya adalah <strong>Berbilang vault</strong>:

- <strong>Vault peribadi</strong>: Hanya anda boleh lihat, seperti bank, e-mel dll akaun peribadi.
- <strong>Vault kongsi</strong>: Ahli keluarga atau pasukan semua boleh lihat, seperti Netflix, WiFi rumah, kad kredit kongsi.
- <strong>Pengredan kebenaran</strong>: Versi pasukan boleh tetapkan sesetengah ahli "lihat sahaja" atau "lihat tetapi tidak edit".

Ahli keluarga atau pasukan tidak perlu kongsi kata laluan utama, masing-masing guna akaun sendiri log masuk, tetapi boleh lihat kandungan vault kongsi yang dibenarkan. Selepas kata laluan diubah semua ahli segerak real-time.

##### 2. Fungsi "Organization" Bitwarden

Versi percuma Bitwarden sokong perkongsian kata laluan peribadi (melalui fungsi "Send" kongsi masa terhad satu kata laluan); versi berbayar boleh cipta "Organization", kongsi beberapa item kepada ahli keluarga atau rakan sepasukan, kebenaran boleh terperinci. Bitwarden juga sediakan pilihan self-hosted, sesuai entreprise yang tuntut kedaulatan data tinggi.

##### 3. Senario keluarga: Cara selamat kongsi Netflix, WiFi dll kata laluan

- <strong>Netflix / laman video</strong>: Guna "vault kongsi" 1Password Families simpan kata laluan log masuk, ahli keluarga masing-masing log masuk, tidak perlu hantar dalam kumpulan.
- <strong>Kata laluan WiFi rumah</strong>: Peranti iOS boleh melalui AirDrop terus kongsi kata laluan WiFi kepada tetamu, tidak perlu sebut; Android 12+ juga ada fungsi "Nearby Share WiFi".
- <strong>Kunci pintar, peranti pintar rumah</strong>: Cuba guna fungsi "ahli keluarga" App pengeluar cipta akaun berasingan untuk setiap orang, bukan kongsi satu akaun pentadbir.
- <strong>Router rumah backend</strong>: Kata laluan pentadbir simpan ke vault kongsi 1Password, WiFi tetamu buka SSID berasingan.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Nilai untuk wang 1Password Families

{class="mt-1"}
1Password Families kira-kira $4.99/bulan, sokong maksimum 5 ahli keluarga, setiap orang ada vault peribadi berasingan + 4 vault kongsi. Kira-kira kurang $1/bulan setiap orang, adalah skim perkongsian keluarga pengalaman terbaik sekarang. Bitwarden versi keluarga $10/tahun sokong 6 orang, nilai untuk wang lebih tinggi, tetapi pengalaman antara muka sedikit kurang.
:::

##### 4. Senario pasukan: Perkongsian kata laluan pelayan/pangkalan data

- <strong>1Password Teams / Business</strong>: Boleh cipta berbilang vault mengikut jabatan, kumpulan projek, kawalan kebenaran butiran, semua tingkah laku akses boleh diaudit.
- <strong>Bitwarden Teams / Enterprise</strong>: Skim sumber terbuka, boleh self-hosted, versi entreprise sokong integrasi SSO, segerak direktori.
- <strong>Prinsip pemisahan tanggungjawab</strong>: Kata laluan pentadbir tidak patut hanya satu orang pegang — tetapkan 2-3 "contact emergency", pastikan perniagaan tidak terputus apabila personel kunci bertugas/bercuti.
- <strong>Proses peletakan jawatan</strong>: Apabila peletakan jawatan, serta-merta tarik balik kebenaran pengurus kata laluan, perlu pusing semua kata laluan sensitif tinggi yang dia sentuh.

##### 5. Akses Kecemasan (Emergency Access): Jika anda ada masalah

Bayangkan senario: Anda urus sendiri semua akaun penting keluarga, tetapi kemalangan masuk hospital atau meninggal, keluarga tidak boleh log masuk bank, e-mel, akaun insurans.<strong>Fungsi "Akses Kecemasan"</strong> direka untuk ini — benarkan keluarga/rakan dipercayai, apabila anda tidak boleh respons, dapat perpustakaan kata laluan anda.

<strong>Tetapan akses kecemasan Bitwarden:</strong>

1. Log masuk Bitwarden Web Vault → Tetapan → Akses Kecemasan.
2. Tambah e-mel contact yang dipercayai, jemput dia terima.
3. Tetapkan "tempoh menunggu" (disyorkan 7-14 hari): dari dia mula permintaan ke anda sahkan.
4. Jika anda tidak respons dalam tempoh menunggu (tolak atau tidak bertindak), selepas tamat dia auto dapat akses.
5. Anda boleh tolak permintaan atau tarik balik kebenaran akses kecemasan bila-bila masa.

<strong>Akses kecemasan 1Password:</strong>

1. 1Password tidak terus panggil "akses kecemasan", tetapi melalui fungsi "organisasi keluarga/pasukan" boleh capai — masukkan keluarga ke versi keluarga, letak sebahagian item ke "vault kongsi".
2. Untuk pengguna versi peribadi, disyorkan beritahu kata laluan utama kepada keluarga yang sangat dipercayai, atau tulis dalam sampul dimeterai simpan di safe.
3. 1Password juga sediakan "recovery code", apabila aktifkan dwi-faktor mesti cetak simpan.

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Sekarang tetapkan: Tinggalkan "kunci sandaran" untuk keluarga

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Pilih keluarga yang dipercayai sebagai "contact kecemasan".
2. Dalam pengurus kata laluan tetapkan akses kecemasan (Bitwarden) atau masukkan vault kongsi keluarga (1Password).
3. Tulis kata laluan utama + recovery code pada kertas, sampul, simpan di safe rumah atau beritahu keluarga yang dipercayai.
4. Semak setiap separuh tahun, sahkan contact kecemasan masih sesuai.
:::

#### IX. Amalan terbaik pengurus kata laluan

- <strong>Semak kata laluan lemah secara berkala</strong>: Kebanyakan pengurus kata laluan ada fungsi "Audit Keselamatan", bantu anda cari kata laluan lemah dan kata laluan pendua.
- <strong>Jangan lupa kata laluan utama</strong>: Kata laluan utama tak boleh dipulihkan, lupa bermakna hilang semua kata laluan. Cadangan tulis di atas kertas, letak di tempat selamat.
- <strong>Akses kecemasan</strong>: Tetapkan kenalan kecemasan, sekiranya anda tak boleh akses, orang yang dipercayai boleh dapat kata laluan anda.
- <strong>Peringatan penting</strong> Pengurus kata laluan walaupun senang, tapi ada risiko: jika kata laluan utama bocor, semua kata laluan terdedah. Jadi kata laluan utama tak boleh sama dengan kata laluan lain, juga tak boleh tulis di tempat mudah dijumpai. Tambahan pula, cadangan pilih penyedia perkhidmatan dengan rekod keselamatan baik.
- <strong>Cuba sekarang: Mula guna pengurus kata laluan</strong> Pilih satu pengurus kata laluan (cadangan Bitwarden atau terbina dalam sistem).

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Daftar akaun, tetapkan satu kata laluan utama yang kuat.

{class="mt-1"}
Import kata laluan sedia ada (jika ada) atau mula tambah kata laluan baharu.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Pasang pemalam pelayar atau App telefon, alami fungsi isi automatik.

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Semak laporan audit keselamatan, cari kata laluan yang perlu diperbaiki.
2. III. Bahagian Lanjutan (Bab 15-20)
3. Selepas menguasai asas dan aplikasi perisian, mari kita terokai fungsi lanjutan telefon pintar dengan lebih mendalam. Kandungan ini akan membantu anda menjadi pakar telefon pintar sejati, malah membuka kunci beberapa "kemahiran tersembunyi".
4. Bab 15: Sains Bateri &amp; Pengoptimuman Ketahanan
5. Bateri ialah "jantung tenaga" telefon pintar anda. Bab ini membantu anda memahami perangai bateri, belajar teknik cas dan ketahanan secara saintifik, dan mengucapkan selamat tinggal kepada kebimbangan paras bateri.
:::
