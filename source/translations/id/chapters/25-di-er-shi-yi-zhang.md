---
id: di-er-shi-yi-zhang
num: 21
part: chao-yue-pian
nav: Bab 21: Bedah Mendalam Jaringan Seluler dan Keamanan Informasi
toc: default
kind: chapter
---

### Bab 21: Pendalaman jaringan mobile dan keamanan informasi

{class="chapter-intro mb-4"}
1\. VPN: "Jubah Tembus Pandang" di Jaringan

#### VPN, kepanjangan dari Virtual Private Network (Jaringan Pribadi Virtual). Anda bisa membayangkannya sebagai terowongan bawah tanah khusus dan terenkripsi yang dibangun antara rumah Anda dan situs web yang ingin Anda kunjungi. Anda berjalan-jalan di dalam terowongan, orang di luar tidak bisa melihat apa yang Anda bawa atau ke mana Anda pergi.

Browsing biasa

- <strong>: Ponsel Anda → jaringan publik → situs web tujuan. Router dan switch di tengah, di mana saja seseorang bisa "mengintip" data yang Anda kirim. Terutama di Wi-Fi publik seperti kafe atau bandara, sejujurnya, ini seperti "berlari telanjang".</strong> Menggunakan VPN
- <strong>: Ponsel Anda → terowongan terenkripsi VPN → server VPN → situs web tujuan. Data dibungkus dengan enkripsi, "pengintai" hanya melihat sekumpulan karakter acak. Selain itu, situs web tujuan melihat alamat IP server VPN, bukan IP asli Anda.</strong> Jadi apa sebenarnya yang bisa dilakukan VPN? Singkatnya: pertama,

melindungi privasi Anda di Wi-Fi publik <strong>; kedua,</strong> melewati pembatasan geografis <strong>(misalnya mengakses konten yang hanya tersedia di negara tertentu); ketiga,</strong> mencegah ISP (penyedia layanan internet) mencatat kebiasaan browsing Anda <strong>. Tapi saya harus mengingatkan:</strong> jangan gunakan VPN gratis!<strong>Yang gratis biasanya berarti data Anda menjadi "komoditas" mereka. Saya punya teman yang menggunakan VPN gratis, lalu ponselnya tiba-tiba dipenuhi iklan pop-up, dan kemudian diketahui bahwa VPN tersebut menjual data browsingnya ke pengiklan. Jadi untuk memilih VPN, pilih merek berbayar yang besar (seperti NordVPN, ExpressVPN), atau jangan gunakan sama sekali.</strong> Selain itu, VPN bukanlah segalanya. VPN hanya melindungi data "sedang transit"—jika situs web tujuan itu sendiri tidak aman, atau ponsel Anda sudah terinfeksi malware, VPN tidak bisa membantu Anda.

2\. "Jebakan Manis" Wi-Fi Publik—Lebih Berbahaya dari yang Anda Bayangkan

#### Anda mungkin berpikir, hanya menghubungkan ke Wi-Fi gratis, seberapa besar risikonya? Saya ceritakan kisah nyata: peneliti keamanan pernah melakukan eksperimen, mendirikan hotspot Wi-Fi bernama "Starbucks_Free" di bandara, dalam waktu kurang dari satu jam ada ratusan orang yang terhubung. Padahal hotspot ini dibuat oleh peneliti sendiri, semua

lalu lintas tidak terenkripsi <strong>yang melewatinya—seperti konten halaman HTTP yang Anda akses, komunikasi App yang tidak mengaktifkan TLS—mereka benar-benar bisa menyadap dan melihatnya.</strong> Tapi perhatikan satu prasyarat penting: hari ini WeChat, mobile banking, dan Alipay yang Anda gunakan sehari-hari, sebagian besar sudah menggunakan enkripsi HTTPS. Artinya, bahkan jika penyerang menyadap paket data, yang mereka lihat hanyalah sekumpulan karakter acak,

tidak bisa langsung membaca konten chat atau kata sandi pembayaran Anda <strong>. Namun mereka tetap bisa mengetahui situs web mana yang Anda kunjungi (domain), dan jika beberapa App atau halaman web lama masih menggunakan transmisi HTTP plain text, maka kontennya akan sepenuhnya terbuka. Serangan ini disebut "Serangan Man-in-the-Middle", prinsipnya adalah penyerang "menyisipkan diri" antara Anda dan router Wi-Fi yang sebenarnya. Yang lebih mengerikan, banyak ponsel orang diatur ke "otomatis terhubung ke Wi-Fi yang dikenal", penyerang hanya perlu menamai hotspot mereka dengan nama Wi-Fi yang pernah Anda hubungkan sebelumnya (seperti "ChinaNet" atau "CMCC"), ponsel Anda akan otomatis terhubung.</strong> Lalu bagaimana mencegahnya? Beberapa saran praktis:

Periksa HTTPS

- <strong>: Awalan address bar adalah https://, tambahan "s" berarti Secure. Saat mengakses situs web apa pun yang memerlukan kata sandi, jika yang Anda lihat adalah http:// (tanpa s), berhenti dan jangan masukkan! Browser mainstream sekarang akan menampilkan peringatan "Tidak Aman" di situs non-HTTPS, jika Anda melihat tanda ini, waspadai.</strong> Matikan "Sambungan Otomatis"
- <strong>: Baik iPhone maupun Android, matikan "Gabung Otomatis" atau "Sambung Otomatis" di pengaturan Wi-Fi. Lebih baik mengetuk secara manual setiap kali daripada membiarkan ponsel memutuskan sendiri.</strong> Gunakan data seluler untuk operasi sensitif
- <strong>: Transfer uang, login mobile banking, memasukkan nomor KTP... operasi-operasi ini gunakan data 4G/5G Anda sendiri, jangan menghemat sedikit kuota data.</strong> Lupakan Wi-Fi yang jarang digunakan
- <strong>: Setelah pulang dari perjalanan bisnis atau liburan, "lupakan" Wi-Fi hotel dan bandara yang pernah Anda hubungi sementara. Dengan begitu ponsel tidak akan otomatis terhubung ke hotspot palsu dengan nama yang sama.</strong>3. Bagaimana HTTPS Melindungi Anda?—SSL/TLS Handshake

#### Baru saja kita menyebut HTTPS, lalu bagaimana sebenarnya cara kerjanya? Setiap kali Anda mengakses situs HTTPS, browser dan server akan melakukan "SSL/TLS handshake", seluruh prosesnya kira-kira seperti ini:

Browser Anda berkata: "Hei, server, saya ingin berkomunikasi dengan aman denganmu, ini daftar kemampuan enkripsi saya (algoritma enkripsi yang didukung, dll)."

1. Server membalas: "Baik, saya memilih skema enkripsi ini dari daftar Anda, ini sertifikat digital saya, yang berisi kunci publik saya, ditandatangani dan disertifikasi oleh lembaga CA tertentu."
2. Browser memverifikasi keaslian sertifikat: Apakah diterbitkan oleh CA tepercaya? Apakah sudah kedaluwarsa? Apakah domainnya cocok?
3. Setelah verifikasi berhasil, kedua pihak menggunakan enkripsi kunci publik untuk menegosiasikan "kunci sesi", dan semua komunikasi setelahnya dienkripsi dengan kunci ini.
4. Ini seperti saat Anda pergi ke bank: Anda menyerahkan KTP (sertifikat), teller memverifikasi identitas Anda, lalu kalian berdua menyepakati kode rahasia, dan percakapan selanjutnya hanya bisa dipahami oleh kalian berdua. Bahkan jika seseorang menguping, mereka hanya akan mendengar karakter acak yang terenkripsi.

Tapi perhatikan: HTTPS hanya menjamin bahwa "proses transmisi" terenkripsi, tidak menjamin situs web tujuan adalah pihak yang baik. Situs phishing juga bisa menggunakan HTTPS—ikon gembok kecil itu hanya menunjukkan bahwa Anda terhubung ke "suatu situs web", bukan berarti situs itu adalah situs yang ingin Anda tuju. Jadi Anda tetap perlu memeriksa sendiri apakah URL sudah benar.

4\. Keamanan DNS: Apakah "Buku Telepon Jaringan" Anda Aman?

#### DNS (Domain Name System) seperti buku telepon internet: Anda memasukkan "baidu.com", DNS membantu Anda menemukan alamat IP yang sesuai (misalnya 110.242.68.66), kemudian browser bisa terhubung. Masalahnya, kueri DNS tradisional adalah

plain text <strong>dan</strong> tidak dienkripsi <strong>! Artinya, ISP Anda, penyedia Wi-Fi, atau node perantara mana pun bisa melihat situs web apa yang Anda kunjungi.</strong> Yang lebih menjijikkan adalah "DNS hijacking": penyerang memanipulasi tahap DNS, mengarahkan "baidu.com" ke situs phishing palsu. Anda jelas memasukkan URL yang benar, tapi dibawa ke halaman login palsu yang terlihat sama persis, dan begitu Anda memasukkan kata sandi akun, semuanya berakhir.

Untungnya sekarang ada solusi DNS terenkripsi:

DNS over HTTPS (DoH)

- <strong>: Menyembunyikan kueri DNS dalam lalu lintas HTTPS, bercampur dengan lalu lintas browsing web normal, tidak bisa dibedakan mana yang merupakan kueri DNS.</strong> DNS over TLS (DoT)
- <strong>: Menggunakan protokol enkripsi TLS khusus untuk melindungi kueri DNS, port terpisah, administrator jaringan bisa tahu Anda menggunakan DoT tapi tidak bisa melihat isinya.</strong> Saya pribadi merekomendasikan menggunakan Cloudflare 1.1.1.1 atau Google 8.8.8.8 sebagai server DNS, keduanya mendukung DNS terenkripsi. Di pengaturan "DNS Pribadi" Android, cukup masukkan "one.one.one.one" atau "dns.google", sangat mudah. iPhone sedikit lebih rumit, perlu memasang profil deskripsi atau mengatur melalui App, tapi juga sepadan untuk dilakukan.

5\. Apakah "Mode Penyamaran" Benar-benar Bisa Membuat Anda Tak Terlihat?

#### Pertama, kesimpulannya:

Pertama, kesimpulannya:<strong>Apa yang dilakukannya: Tidak meninggalkan jejak secara lokal—setelah menutup jendela penyamaran, browser tidak menyimpan riwayat browsing, Cookies, catatan pengisian formulir, dan riwayat pencarian Anda. Meminjam komputer orang lain untuk mencari sesuatu, atau membeli hadiah tanpa ingin diketahui keluarga dari riwayat browsing, menggunakan mode penyamaran adalah pilihan yang tepat.</strong>

Apa yang tidak bisa dilakukannya:

Situs web yang Anda kunjungi

- tetap bisa melihat Anda datang <strong>—alamat IP, informasi perangkat, dan perilaku browsing Anda, jelas terlihat di sisi situs web.</strong> ISP Anda
- tetap bisa melihat situs web mana yang Anda kunjungi <strong>, hanya tidak bisa melihat konten spesifiknya (jika menggunakan HTTPS).</strong> Administrator jaringan kantor/sekolah
- juga bisa memantau <strong>perilaku online Anda.</strong> File yang Anda unduh dan bookmark yang Anda tambahkan akan
- tetap tersimpan <strong>, tidak hilang saat jendela ditutup.</strong> Jadi ingat: Mode penyamaran adalah "penghapus lokal", bukan "pakaian tembus pandang jaringan". Jika Anda benar-benar perlu menyembunyikan jejak online, gunakan kombinasi VPN + browser Tor, tapi untuk penggunaan sehari-hari, memahami hal ini sudah cukup.

6\. Privasi Browser: Jangan Biarkan Browser Menjual Anda

#### Anda mungkin tidak menyadari bahwa browser itu sendiri adalah pengumpul informasi raksasa. Cookies, riwayat browsing, cache, isi otomatis, izin lokasi... setiap satu bisa membocorkan privasi Anda. Beberapa saran:

Bersihkan data browsing secara berkala

- <strong>: Setiap sekian waktu, masuk ke pengaturan dan bersihkan Cookies, cache, dan riwayat. Bukan untuk mencegah "dilacak"—itu dengan menghapus Cookies sudah tidak terlalu efektif—melainkan untuk mencegah ponsel menjadi lambat. Cache browser bisa mengambil ruang beberapa Gigabyte.</strong> Hilangkan ilusi "Jangan Lacak"
- <strong>: Opsi "Kirim permintaan 'Jangan Lacak'" di browser pada dasarnya "meminta" situs web untuk tidak melacak Anda. Tapi apakah situs web mendengarkan atau tidak adalah hal lain, sebagian besar situs web langsung mengabaikannya. Jangan berharap padanya.</strong> Manfaatkan browser privasi
- <strong>: Firefox Focus, DuckDuckGo Browser, Brave—browser-browser ini secara default memblokir tracker dan iklan, jauh lebih bersih daripada pengaturan default Chrome dan Safari.</strong> Mesin pencari juga penting
- <strong>: Gunakan DuckDuckGo sebagai pengganti Baidu/Google, ia tidak mencatat riwayat pencarian Anda dan tidak membangun profil pengguna. Sejujurnya hasil pencarian memang tidak seakurat Google, tapi untuk pencarian informasi sehari-hari sudah cukup.</strong> Periksa izin App
- <strong>: Lihat di pengaturan ponsel izin apa yang diberikan ke browser Anda. Apakah benar-benar perlu akses ke lokasi, mikrofon, dan kontak Anda? Kemungkinan besar tidak.</strong>7. Daftar Keamanan Praktis: Lindungi Diri Mulai Sekarang

#### Sudah banyak dibahas, terakhir saya berikan daftar keamanan sederhana namun efektif—selesaikan dalam setengah jam, keamanan ponsel Anda akan melonjak secara signifikan:

Matikan sambungan Wi-Fi otomatis

1. <strong>: iPhone di Pengaturan - Wi-Fi, Android di pengaturan Wi-Fi.</strong> Ganti ke DNS terenkripsi
2. <strong>: Android langsung atur DNS Pribadi ke "dns.google", iPhone gunakan App atau profil deskripsi untuk mengatur DoH 1.1.1.1.</strong> Aktifkan autentikasi dua faktor (2FA)
3. <strong>: WeChat, Alipay, Apple ID, akun Google—yang bisa mengaktifkan 2FA, aktifkan semua. Kode verifikasi SMS sudah menjadi level 2FA terendah, lebih baik gunakan TOTP (seperti Google Authenticator, Microsoft Authenticator).</strong> Periksa semua izin App
4. <strong>: Tinjau izin setiap App, terutama lima item: lokasi, kontak, SMS, mikrofon, kamera. Anda akan menemukan bahwa beberapa App senter bahkan meminta akses ke kontak Anda—segera uninstall.</strong> Bersihkan data browser secara berkala
5. <strong>: Atur pengingat kalender, sebulan sekali, bersihkan cache dan Cookies.</strong> Jangan gunakan kabel data dari stasiun pengisian daya publik
6. <strong>: Port USB bisa mengisi daya sekaligus mentransfer data, stasiun pengisian daya berbahaya (disebut "Juice Jacking") bisa mencuri data saat Anda mengisi daya. Bawa charger dan kabel sendiri saat bepergian.</strong> Lakukan Sekarang: Lakukan "Pemeriksaan Keamanan" pada Ponsel Anda

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Upgrade DNS

{class="list-decimal pl-6 mt-1 space-y-1"}
1. <strong>: Android: Pengaturan &gt; Koneksi &amp; Berbagi &gt; DNS Pribadi &gt; masukkan "one.one.one.one" atau "dns.google". iPhone: Cari "1.1.1.1 DNS profile" di Safari, instal profil deskripsi, atau unduh App Cloudflare 1.1.1.1.</strong> Audit Wi-Fi
2. <strong>: Buka daftar Wi-Fi, "lupakan" semua hotspot yang tidak dikenal, jarang digunakan, atau namanya mencurigakan.</strong> Bersih-bersih izin besar-besaran
3. <strong>: Masuk ke Pengaturan &gt; Privasi/Manajemen Izin, periksa izin setiap App satu per satu. Tandai App yang permintaan izinnya tidak masuk akal (misalnya kalkulator meminta kontak), pertimbangkan untuk uninstall atau gunakan alternatif.</strong> Periksa keamanan akun
4. <strong>: Buka halaman keamanan Apple ID atau akun Google, lihat apakah ada login perangkat yang tidak dikenal, konfirmasi 2FA sudah aktif, periksa apakah kontak pemulihan tepercaya.</strong> Bab 22: Bagaimana AI Bekerja di Ponsel
:::
