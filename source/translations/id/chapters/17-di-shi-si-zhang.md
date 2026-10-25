---
id: di-shi-si-zhang
num: 14
part: ruan-jian-pian
nav: Bab 14: Khusus Pengelola Kata Sandi
toc: default
kind: chapter
---

### Bab 14: Topik khusus pengelola kata sandi

{class="chapter-intro mb-4"}
1\. Mengapa Anda Memerlukan Password Manager?

#### 1. Mengapa Anda Memerlukan Password Manager?

Password manager menyelesaikan dilema ini: Anda hanya perlu mengingat satu master password, ia membantu Anda mengingat semua kata sandi lainnya.

2\. Cara Kerja Password Manager

#### 2. Cara Kerja Password Manager

1. <strong>: Semua kata sandi disimpan dengan enkripsi kuat, hanya Anda yang bisa mendekripsi.</strong> Master Password
2. <strong>: Anda mengatur satu master password, digunakan untuk membuka kunci brankas kata sandi. Master password itu sendiri tidak disimpan di server.</strong> Auto-fill
3. <strong>: Di antarmuka login website atau aplikasi, password manager otomatis mengisi akun dan kata sandi.</strong> Generasi Kata Sandi
4. <strong>: Dapat menghasilkan kata sandi acak dan kompleks, meningkatkan keamanan.</strong>3. Rekomendasi Password Manager Mainstream

#### 3. Pengantar Prinsip Enkripsi

Memahami prinsip enkripsi password manager membantu Anda menilai apakah suatu layanan layak dipercaya. Berikut penjelasan beberapa konsep inti dalam bahasa sederhana.

##### 1. Enkripsi AES-256

AES (Advanced Encryption Standard) adalah algoritma enkripsi simetris yang diakui oleh NIST (National Institute of Standards and Technology) Amerika Serikat, banyak digunakan oleh bank, militer, dan pemerintah. "256" berarti panjang key 256 bit — secara teori butuh waktu melebihi usia alam semesta untuk brute force. Password manager mainstream (1Password, Bitwarden, KeePass, dll.) semua memakai AES-256 untuk mengenkripsi vault password Anda.

##### 2. Arsitektur Zero-Knowledge

"Zero-knowledge" bukan berarti penyedia layanan tidak menyimpan apa-apa, melainkan <strong>Enkripsi dan dekripsi semua dilakukan lokal di perangkat Anda, server hanya menyimpan ciphertext yang sudah dienkripsi</strong>. Alur spesifik:

1. Anda memasukkan master password di sisi klien.
2. Klien derive encryption key dari master password (langkah ini diselesaikan di ponsel/komputer Anda).
3. Hanya ciphertext yang dienkripsi yang diupload ke server.
4. Saat login berikutnya, server mengirim ciphertext, klien lagi-lagi dekripsi dengan master password.

Poin kunci:<strong>Master password itu sendiri tidak pernah meninggalkan perangkat Anda</strong>, di server juga tidak ada. Jadi bahkan jika penyedia layanan diretas, hacker hanya mendapatkan setumpuk ciphertext yang tidak bisa didekripsi — kecuali mereka bisa menebak master password Anda.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Mengapa "zero-knowledge" berarti penyedia layanan juga tidak bisa melihat password Anda?

{class="mt-1"}
Karena decryption key di-derive dari master password Anda, dan master password hanya ada di pikiran Anda, hanya digunakan di perangkat lokal Anda. Server penyedia layanan tidak punya master password, tidak punya decryption key, hanya ciphertext. Inilah sebabnya penyedia layanan resmi seperti Bitwarden, 1Password secara eksplisit menyatakan "kami juga tidak bisa melihat password Anda" — bukan tidak mau lihat, tapi secara teknis tidak bisa.
:::

##### 3. Key Derivation Function: PBKDF2 dan Argon2

Master password tidak bisa langsung dipakai sebagai encryption key — perlu diproses melalui "key derivation function". Fungsi ini bertugas <strong>Sengaja memperlambat komputasi</strong>, membuat biaya brute force hacker menjadi tidak feasibel.

- <strong>PBKDF2</strong>: Standar lama, digunakan luas oleh iCloud Keychain, Bitwarden, LastPass, dll. Melalui iterasi berulang (biasanya 100.000+ kali) hash untuk memperlambat cracking.
- <strong>Argon2</strong>: Juara Password Hashing Competition 2015, lebih modern dari PBKDF2. Selain "konsumsi compute" juga memperkenalkan "konsumsi memori" — membuat hardware khusus seperti GPU/ASIC juga sulit mempercepat cracking. Bitwarden, KeePassXC, dll. sudah mendukung.

Semakin tinggi jumlah iterasi semakin aman, tapi kecepatan unlock juga melambat. Penyedia layanan resmi akan mempublikasikan algoritma derivation dan jumlah iterasi yang digunakan, untuk memudahkan audit komunitas keamanan.

##### 4. Studi Kasus: Kebocoran Data LastPass 2022

Agustus 2022, password manager lama LastPass mengumumkan environment development-nya diretas; November tahun yang sama lebih lanjut mengungkapkan, hacker mengambil backup vault password pengguna (ciphertext terenkripsi). Pelajaran kunci dari insiden ini:

- <strong>Arsitektur zero-knowledge mempertahankan garis bawah</strong>: Karena vault password itu sendiri terenkripsi, hacker mendapatkan ciphertext tapi tidak bisa dekripsi — dengan syarat master password pengguna cukup kuat.
- <strong>Pengguna master password lemah paling berbahaya</strong>: Hacker bisa brute force offline master password lemah, karena itu pengguna dengan master password lemah atau berulang menghadapi risiko nyata.
- <strong>Metadata juga bocor</strong>: Meskipun konten password terenkripsi, metadata seperti URL situs dan catatan mungkin tidak terenkripsi, akan mengungkapkan layanan apa saja yang digunakan pengguna.

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Yang dipelajari dari insiden LastPass

{class="mt-1"}
Pertama, master password harus panjang dan unik (disarankan 16+ karakter, termasuk huruf besar/kecil, angka, simbol); kedua, prioritaskan penyedia layanan yang mendukung Argon2id dengan iterasi tinggi; ketiga, untuk akun high-value (bank, email) pastikan aktifkan verifikasi dua faktor independen, jangan hanya andalkan password manager.
:::

#### 4. Rekomendasi Password Manager Mainstream

##### iCloud Keychain

- <strong>: Pilihan utama pengguna ekosistem Apple. Integrasi mulus dengan Safari dan aplikasi, gratis, aman. Kekurangannya penggunaan lintas platform tidak nyaman.</strong> Google Password Manager
- <strong>: Nyaman untuk pengguna Android. Integrasi dengan Chrome dan sistem Android, gratis.</strong> Huawei Password Vault
- <strong>: Bawaan sistem HarmonyOS, cocok untuk pengguna Huawei.</strong> Alat Profesional Pihak Ketiga:

##### Bitwarden

- <strong>: Open source gratis, fitur kuat, mendukung semua platform. Sangat direkomendasikan untuk pengguna yang mengutamakan privasi.</strong>1Password
- <strong>: Antarmuka indah, fitur kaya, cocok untuk keluarga dan tim. Berbayar.</strong> LastPass
- <strong>: Password manager lama, versi gratis fiturnya terbatas.</strong> KeePass
- <strong>: Penyimpanan sepenuhnya lokal, open source gratis. Cocok untuk pengguna geek.</strong>4. Praktik Terbaik Penggunaan Password Manager

#### 5. Evaluasi Nyata Kekuatan Password

Password manager umumnya menampilkan indikator "password strength" (merah/kuning/hijau), tapi evaluasi ini sering hanya melihat panjang dan jenis karakter, tidak komprehensif. Untuk benar-benar menilai apakah password aman, perlu mempertimbangkan "entropy" dan "apakah sudah pernah bocor".

##### 1. Entropy: Ukuran Ilmiah Kekuatan Password

"Entropy" mengukur ketidakpastian password, satuan bit. Semakin tinggi entropy, semakin banyak upaya brute force yang dibutuhkan.

- <strong>"123456"</strong>: Entropy sangat rendah, crack sekejap.
- <strong>"P@ssw0rd"</strong>: Terlihat kompleks, tapi muncul di semua list dictionary attack, entropy tetap rendah.
- <strong>"correct horse battery staple"</strong>: Empat kata acak, entropy sekitar 44 bit, kesulitan crack jauh melampaui "P@ssw0rd".
- <strong>16 karakter acak (termasuk besar/kecil+angka+simbol)</strong>: Entropy sekitar 100 bit, compute power saat ini tidak bisa brute force.

Kesimpulan:<strong>"Panjang + randomitas" lebih penting dari "simbol kompleks"</strong>. Inilah juga alasan password acak panjang yang di-generate password manager benar-benar aman.

##### 2. HaveIBeenPwned: Cek Apakah Password Anda Sudah Bocor

Dipelihara oleh security researcher Troy Hunt <a href="https://haveibeenpwned.com" class="text-primary hover:underline" target="_blank" rel="noopener">haveibeenpwned.com</a> mencatat akun dan password yang bocor dari berbagai insiden kebocoran data besar. Anda bisa:

1. Masukkan email, cek apakah akun Anda terekspos dalam suatu kebocoran.
2. Pakai fitur Pwned Passwords untuk query apakah suatu password ada di database kebocoran yang diketahui (password manager dan browser sudah built-in query ini).

Jika suatu password muncul di database kebocoran,<strong>meskipun terlihat sekompleks apa pun harus segera diganti</strong>— karena dictionary attack akan prioritas mencoba password yang diketahui ini.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-shield-alt mr-2"></i>Prinsip Query k-Anonymity

{class="mt-1"}
Khawatir input password di HaveIBeenPwned akan bocor lagi? Tidak perlu khawatir. Query modern memakai protokol "k-anonymity": browser hanya mengirim 5 karakter pertama hash password ke server, server mengembalikan semua list hash yang diawali 5 karakter tersebut, lalu dicocokkan secara lokal. Artinya, server tidak pernah melihat hash password lengkap Anda. "Leaked password detection" 1Password dan Bitwarden semua bekerja seperti ini.
:::

##### 3. Fitur Monitoring Built-in Password Manager

- <strong>1Password Watchtower</strong>: Real-time monitor password lemah, password duplikat, password bocor, password kedaluwarsa, situs tanpa 2FA, ditampilkan dengan grading merah/oranye/kuning.
- <strong>Bitwarden Vault Health</strong>: Versi gratis sudah bisa cek password lemah dan duplikat; versi premium bisa deteksi password bocor (berbasis HaveIBeenPwned).
- <strong>"Security Recommendations" iCloud Keychain</strong>: iOS Settings → Passwords → Security Recommendations, akan mengingatkan password mana yang muncul di kebocoran yang diketahui, mana yang dipakai berulang.
- <strong>"Password Checkup" Google Password Manager</strong>: Built-in Chrome, bisa sekali klik cek password bocor, lemah, dan duplikat.

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Cek Sekarang: Apakah Password Anda Aman

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Buka haveibeenpwned.com, masukkan email yang sering Anda pakai, lihat di kebocoran mana Anda muncul.
2. Pengguna iPhone: Settings → Passwords → Security Recommendations, proses peringatan merah satu per satu.
3. Pengguna Chrome: Settings → Passwords → Check Passwords, ubah sesuai petunjuk.
4. Pengguna 1Password/Bitwarden: Buka Watchtower/Health Reports, prioritaskan proses item "bocor" dan "duplikat".
:::

#### 6. Passkey: Masa Depan Login Tanpa Password

2024-2026, teknologi password sedang mengalami revolusi —<strong>Passkey</strong> diharapkan bisa sepenuhnya menggantikan password tradisional. Apple, Google, Microsoft tiga platform besar mendorong bersama, didukung oleh FIDO Alliance dan W3C, ini adalah perubahan terbesar dalam cara login selama puluhan tahun.

##### 1. Apa itu Passkey?

Passkey berbasis standar FIDO2 / WebAuthn, memakai <strong>key pair di perangkat</strong> menggantikan password. Prinsipnya bisa disederhanakan:

- Ponsel Anda meng-generate sepasang key:<strong>Public key</strong>(didaftarkan ke situs) + <strong>Private key</strong>(selalu ada di security chip perangkat Anda).
- Saat login, situs mengirim "challenge", ponsel Anda menandatangani dengan private key, lalu diverifikasi oleh situs dengan public key.
- Sebelum menandatangani perlu verifikasi biometrik (Face ID / sidik jari) atau PIN perangkat untuk konfirmasi identitas.
- Seluruh proses,<strong>tidak ada password yang ditransmisikan di jaringan</strong>.

##### 2. Passkey vs Password Tradisional

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                        <thead>
                            <tr class="bg-light dark:bg-gray-700">
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Dimensi</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Password Tradisional</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Passkey</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Anti-Phishing</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Buruk, situs phishing bisa mencuri password</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Naturally anti-phishing, private key hanya menandatangani domain asli</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Dampak Kebocoran Server</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Hash password mungkin bisa di-crack</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Server hanya simpan public key, bocor tidak berdampak</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Kemudahan</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Perlu hafal/input/kelola</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Face ID/sidik jari login satu detik</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Replay Attack</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mungkin diintercept dan di-replay man-in-the-middle</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Setiap tanda tangan sekali pakai, tidak bisa di-replay</td>
                            </tr>
                        </tbody>
                    </table>
```

##### 3. Dukungan Platform

- <strong>Apple iCloud Keychain Passkey</strong>: iOS 16+ / macOS Ventura+ native mendukung, Passkey bisa sinkron antar semua perangkat yang login Apple ID yang sama, perangkat baru login situs tanpa perlu buat ulang.
- <strong>Google Password Manager Passkey</strong>: Android + Chrome native mendukung, Passkey disimpan di akun Google, sinkron antar perangkat Android; sejak 2023 akun personal Google sudah mendukung login dengan Passkey.
- <strong>Microsoft</strong>: Windows 11 / Edge sudah mendukung Passkey; akun Microsoft, Outlook, Office, dll. bertahap membuka login Passkey, dan bisa dikelola di Microsoft Authenticator.
- <strong>1Password / Bitwarden</strong>: Sudah mendukung pembuatan, penyimpanan, sinkronisasi cross-platform Passkey, membuat Anda tidak terbatas pada satu ekosistem.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Sinkronisasi cross-device adalah terobosan kunci

{class="mt-1"}
Pain point terbesar Passkey awal adalah "terikat satu perangkat" — ganti ponsel harus buat ulang. Sejak 2023 Apple, Google, Microsoft mengimplementasikan sinkronisasi cloud Passkey: iCloud Keychain sync antar perangkat Apple, Google Password Manager sync antar perangkat Android. 1Password dan pihak ketiga lain membuka sinkronisasi cross-ecosystem. Artinya Passkey sudah memiliki praktikalitas untuk menggantikan password.
:::

##### 4. Cara Membuat dan Menggunakan Passkey di Ponsel

<strong>Jalur iOS (iPhone):</strong>

1. Di halaman keamanan akun situs yang mendukung Passkey (seperti Google, Microsoft, Amazon, eBay, PayPal) pilih "Add passkey".
2. Sistem memunculkan jendela verifikasi Face ID / Touch ID, setelah lolos Passkey otomatis di-generate dan disimpan ke iCloud Keychain.
3. Saat login situs tersebut berikutnya, setelah input username pilih "Login with iPhone", Face ID sekali scan selesai.
4. Entri manajemen: Settings → Passwords → cari situs terkait, terlihat entri Passkey.

<strong>Jalur Android:</strong>

1. Di halaman keamanan akun situs yang mendukung Passkey pilih "Add passkey".
2. Pop-up Google Password Manager → pilih akun Google Anda → verifikasi screen lock (sidik jari/pola/PIN).
3. Passkey otomatis disimpan ke Google Password Manager, sinkron antar perangkat Android dengan akun yang sama.
4. Saat login berikutnya, pilih "Use Passkey", screen lock sekali buka selesai.
5. Entri manajemen: Android Settings → Passwords, passkeys &amp; autofill → Password Manager → google.com.

##### 5. Login Passkey Cross-Device

Jika Anda login ke situs yang hanya punya Passkey di iPhone di komputer Windows, bisa scan kode QR untuk otorisasi:

1. Halaman login situs pilih "Use Passkey".
2. Pilih "Use another device".
3. Komputer menampilkan QR code, scan dengan iPhone.
4. iPhone memunculkan verifikasi Face ID, setelah konfirmasi situs selesai login di komputer.

Proses ini melalui komunikasi double encryption Bluetooth + internet, private key Passkey tidak akan meninggalkan iPhone Anda.

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Coba Sekarang: Rasakan Login Tanpa Password

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Login akun Google → Security → Passkeys → Add passkey, rasakan login Face ID/sidik jari.
2. Login akun Microsoft → Security → Advanced security options → Add passkey.
3. Coba di Taobao, JD, eBay, PayPal, dll. yang sudah mendukung Passkey.
4. Simpan password tradisional sebagai backup, bertahap migrasi akun high-value ke Passkey.
:::

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Saran Masa Transisi

{class="mt-1"}
Passkey belum sepenuhnya menggantikan password — banyak situs masih dalam tahap "Passkey + password" berdampingan. Saran: akun high-value prioritaskan aktifkan Passkey, tapi <strong>jangan langsung hapus password tradisional</strong>, simpan sebagai cadangan; bersamaan terus gunakan password manager, karena tidak semua situs mendukung Passkey. Anggap Passkey sebagai "suplemen kuat password manager" bukan "pengganti langsung".
:::

#### 7. Hardware Security Key

Jika requirement keamanan Anda lebih tinggi dari pengguna biasa — misalnya memegang banyak cryptocurrency, adalah eksekutif/jurnalis/aktivis, atau melindungi akun inti perusahaan — hardware security key adalah pilihan yang lebih andal dibanding SMS verification code.

##### 1. Apa itu Hardware Security Key?

Hardware key adalah perangkat fisik (mirip USB drive), security chip internal menyimpan private key Anda, perlu kontak fisik atau NFC untuk menyelesaikan verifikasi. Produk representatif:

- <strong>YubiKey</strong>(perusahaan Yubico): Paling mainstream, mendukung FIDO2/WebAuthn, U2F, OTP, PIV, OpenPGP, USB-C / USB-A / NFC dan berbagai interface. Seri 5 seharga 50-70 USD.
- <strong>Google Titan</strong>: Produk Google, USB-C + NFC / Bluetooth, sekitar 30-40 USD.
- <strong>OnlyKey</strong>: Alternatif open-source, mendukung banyak protokol.
- <strong>Alternatif Domestik</strong>: Seperti ePasskey Feitian, harga lebih terjangkau.

##### 2. Mengapa Hardware Key Lebih Aman dari SMS Verification Code?

- <strong>Anti-Phishing</strong>: Sama seperti Passkey, hardware key hanya merespons domain asli, situs phishing tidak bisa menipu verification code.
- <strong>Anti SIM Hijacking</strong>: SMS verification code bisa di-intercept serangan SIM-swap, hardware key tidak butuh nomor ponsel.
- <strong>Anti Man-in-the-Middle</strong>: Protokol FIDO2 setiap tanda tangan mengandung challenge value, tidak bisa di-replay.
- <strong>Isolasi Fisik</strong>: Private key selalu di dalam hardware chip, malware bahkan jika meretas komputer Anda juga tidak bisa membacanya.

##### 3. Skenario yang Cocok

- Akun exchange cryptocurrency, pemulihan wallet.
- SSO enterprise, VPN remote working, SSH login server.
- Email, GitHub, media sosial, dll. "akun utama" — sekali diretas bisa reset semua akun lain.
- Jurnalis, pengacara, eksekutif, dan orang sensitif tinggi lainnya.

##### 4. Cara Konfigurasi Hardware Key sebagai Verifikasi Dua Faktor

Contoh akun Google + YubiKey:

1. Beli YubiKey (disarankan beli dua sekaligus, satu untuk harian, satu cadangan, simpan di lokasi berbeda).
2. Login myaccount.google.com → Security → 2-Step Verification.
3. Pilih "Add security key" → masukkan YubiKey ke port USB-C atau dekatkan ke area sensor NFC ponsel.
4. Ikuti petunjuk sentuh metal contact YubiKey untuk menyelesaikan registrasi.
5. Disarankan mendaftarkan key cadangan kedua.
6. Di settings "2-Step Verification", set hardware key sebagai metode verifikasi utama, SMS verification code sebagai cadangan.

Situs mainstream yang mendukung: Google, GitHub, Microsoft, Apple ID, Facebook, Twitter, Dropbox, GitLab, AWS, Coinbase, Binance, dll.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Strategi Dual Key

{class="mt-1"}
Risiko terbesar hardware key adalah "kehilangan". Saran: ① sekaligus daftarkan dua key berbeda; ② satu dibawa (gantungan kunci), satu disimpan di brankas rumah atau safe deposit box bank; ③ sebagian situs mengizinkan "recovery code cadangan" dicetak untuk disimpan offline. Dengan begitu bahkan jika key utama hilang, tidak akan terkunci permanen di luar akun.
:::

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Hati-hati Channel Pembelian

{class="mt-1"}
Pastikan beli dari toko resmi atau agen resmi, jangan beli key bekas atau sumber tidak jelas — secara teori hardware yang sudah di-preset mungkin sudah ditanam backdoor. Firmware YubiKey tidak bisa diupdate setelah keluar pabrik, tapi Yubico akan terus push security advisory, perhatikan situs resminya.
:::

#### 8. Sharing Password Keluarga/Tim

Dalam skenario keluarga, Netflix, Wi-Fi rumah, backend router, password smart lock perlu dipakai bersama keluarga; dalam skenario tim, server, database, akun media sosial perlu kolaborasi multipihak.<strong>Mengirim password via WeChat atau menulis di shared document adalah praktik berisiko tinggi</strong>— sekali riwayat chat atau permission document bocor, password juga bocor.

##### 1. "Shared Vault" 1Password

1Password adalah produk benchmark sharing keluarga dan tim. Mekanisme intinya adalah <strong>multiple vault</strong>:

- <strong>Personal Vault</strong>: Hanya Anda yang bisa lihat, seperti akun pribadi bank, email.
- <strong>Shared Vault</strong>: Keluarga atau anggota tim semua bisa lihat, seperti Netflix, Wi-Fi rumah, kartu kredit bersama.
- <strong>Permission Tiering</strong>: Versi tim bisa setel anggota tertentu "read-only" atau "read-only tanpa edit".

Keluarga atau anggota tim tidak perlu sharing master password, masing-masing login dengan akun sendiri, tapi bisa melihat konten shared vault yang diotorisasi. Setelah password diubah semua anggota sinkron real-time.

##### 2. Fitur "Organization" Bitwarden

Versi gratis Bitwarden mendukung sharing password personal (via fitur "Send" share time-limited single password); versi premium bisa membuat "Organization", membagikan beberapa entri ke anggota keluarga atau kolega tim, permission bisa dibagi halus. Bitwarden juga menyediakan opsi self-hosted, cocok untuk enterprise dengan requirement kedaulatan data tinggi.

##### 3. Skenario Keluarga: Cara Aman Sharing Password Netflix, Wi-Fi, dll.

- <strong>Netflix / Situs Video</strong>: Simpan login password di "Shared Vault" 1Password Families, anggota keluarga masing-masing login, tanpa perlu kirim di grup.
- <strong>Password Wi-Fi Rumah</strong>: Antar perangkat iOS bisa via AirDrop langsung sharing password Wi-Fi ke tamu, tanpa perlu dibacakan; Android 12+ juga punya fitur "Nearby Share Wi-Fi".
- <strong>Smart Lock, Smart Home Appliances</strong>: Usahakan pakai fitur "Family Member" App vendor untuk membuat akun terpisah per orang, bukan sharing satu akun admin.
- <strong>Backend Router Rumah</strong>: Password admin disimpan di 1Password Shared Vault, Wi-Fi tamu buka SSID terpisah.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Value for Money 1Password Families

{class="mt-1"}
1Password Families sekitar 4.99 USD/bulan, mendukung maksimal 5 anggota keluarga, masing-masing punya personal vault independen + 4 shared vault. Dihitung per orang kurang dari 1 USD/bulan, saat ini solusi sharing keluarga dengan pengalaman terbaik. Versi keluarga Bitwarden 10 USD/tahun mendukung 6 orang, value for money lebih tinggi, tapi pengalaman antarmuka sedikit kalah.
:::

##### 4. Skenario Tim: Sharing Password Server/Database

- <strong>1Password Teams / Business</strong>: Bisa membuat multiple vault per departemen, project team, permission control fine-grained, semua perilaku akses bisa diaudit.
- <strong>Bitwarden Teams / Enterprise</strong>: Solusi open-source, bisa self-hosted, versi enterprise mendukung SSO integration, directory sync.
- <strong>Prinsip Separation of Duties</strong>: Password admin tidak boleh hanya dipegang satu orang — setel 2-3 "emergency contact", pastikan saat personil kunci resign/cuti bisnis tidak terputus.
- <strong>Proses Resign</strong>: Saat karyawan resign segera cabut akses password manager-nya, jika perlu rotasi semua password sensitif tinggi yang perlu disentuhnya.

##### 5. Emergency Access: Jika Terjadi Sesuatu pada Anda

Bayangkan skenario: Anda mengelola sendiri semua akun penting keluarga, tapi tiba-tiba dirawat di rumah sakit atau meninggal, keluarga tidak bisa login ke bank, email, akun asuransi.<strong>Fitur "Emergency Access"</strong> dirancang untuk hal ini — otorisasi seorang keluarga/teman terpercaya, untuk mendapatkan vault password Anda saat Anda tidak bisa merespons.

<strong>Setting Emergency Access Bitwarden:</strong>

1. Login Bitwarden Web Vault → Settings → Emergency Access.
2. Tambahkan email kontak terpercaya, undang untuk accept.
3. Setel "waiting period" (disarankan 7-14 hari): time window dari permintaan dikirim sampai Anda konfirmasi.
4. Jika Anda tidak merespons dalam waiting period (menolak atau tidak melakukan apa-apa), setelah jatuh tempo pihak tersebut otomatis mendapatkan akses.
5. Anda kapan saja bisa manual menolak permintaan atau cabut permission Emergency Access.

<strong>Emergency Access 1Password:</strong>

1. 1Password tidak secara langsung disebut "Emergency Access", tapi melalui fitur "Family/Team Organization" bisa diimplementasikan — tambahkan keluarga ke versi Families, lalu masukkan sebagian entri ke "Shared Vault".
2. Untuk pengguna versi personal, disarankan memberi tahu master password ke satu keluarga yang sangat dipercaya, atau tulis di amplop tertutup simpan di brankas.
3. 1Password juga menyediakan "Recovery Code", saat mengaktifkan 2FA pastikan cetak dan simpan.

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Set Sekarang: Simpan "Kunci Cadangan" untuk Keluarga

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Pilih satu keluarga terpercaya sebagai "Emergency Contact".
2. Di password manager setel Emergency Access (Bitwarden) atau gabung shared vault keluarga (1Password).
3. Tulis master password + recovery code di kertas, segel di amplop, simpan di brankas rumah atau beri tahu keluarga terpercaya.
4. Review setiap enam bulan, konfirmasi apakah emergency contact masih tepat.
:::

#### 9. Praktik Terbaik Penggunaan Password Manager

- <strong>: Master password adalah pertahanan terakhir, pastikan mengatur kata sandi yang panjang dan kompleks, dan ingat baik-baik.</strong> Aktifkan Two-Factor Authentication
- <strong>: Aktifkan 2FA untuk akun password manager, menambah lapisan perlindungan.</strong> Periksa Kata Sandi Lemah Secara Berkala
- <strong>: Sebagian besar password manager memiliki fitur "Security Audit", membantu menemukan kata sandi lemah dan duplikat.</strong> Jangan Lupa Master Password
- <strong>: Master password tidak bisa dipulihkan, lupa berarti kehilangan semua kata sandi. Disarankan tulis di kertas, simpan di tempat aman.</strong> Akses Darurat
- <strong>: Atur emergency contact, jika Anda tidak bisa mengakses, orang yang dipercaya bisa mendapatkan kata sandi Anda.</strong> Pengingat Penting

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Password manager meski nyaman, tetapi juga ada risiko: jika master password bocor, semua kata sandi terbuka. Jadi master password tidak boleh sama dengan kata sandi lain, juga tidak boleh ditulis di tempat yang mudah ditemukan. Selain itu, disarankan pilih penyedia layanan dengan rekam jejak keamanan yang baik.

{class="mt-1"}
Coba Sekarang: Mulai Menggunakan Password Manager
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Pilih satu password manager (rekomendasi Bitwarden atau bawaan sistem).

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Daftar akun, atur master password yang kuat.
2. Impor kata sandi yang ada (jika ada) atau mulai tambah kata sandi baru.
3. Install ekstensi browser atau aplikasi ponsel, rasakan fitur auto-fill.
4. Periksa laporan security audit, temukan kata sandi yang perlu diperbaiki.
5. III. Bagian Lanjutan (Bab 15-20)
:::
