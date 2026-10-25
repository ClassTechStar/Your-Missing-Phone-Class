---
id: di-er-shi-yi-zhang
num: 21
part: chao-yue-pian
nav: Bab 21: Kajian Mendalam Rangkaian Mudah Alih dan Keselamatan Maklumat
toc: default
kind: chapter
---

### Bab 21: Pendalaman Rangkaian Bergerak & Keselamatan Maklumat

{class="chapter-intro mb-4"}
Kita menggunakan telefon untuk melayari internet, membuat pembayaran, dan bersembang setiap hari, rasa sangat mudah. Tetapi pernahkah anda terfikir, rekod sembang anda, kata laluan pembayaran, foto-foto anda... berapa kerap maklumat ini "berlari telanjang" di internet? Jujurlah, kebanyakan orang langsung tidak pernah memikirkan masalah ini, tetapi sekali berlaku insiden—contohnya akaun dicuri, kad bank dikuras—baru menyesal sudah terlambat. Dalam bab ini, kita akan bincang dengan baik, bagaimana membuat kehidupan digital anda tidak begitu "telus".

#### 1. VPN: "Jubah Halimunan" dalam Rangkaian

: Telefon anda → terowong disulitkan VPN → pelayan VPN → laman web sasaran. Data disulitkan dan dibungkus, "pengintip" hanya boleh melihat sekelompok kod tidak bermakna. Selain itu, laman web sasaran melihat alamat IP pelayan VPN, bukan IP sebenar anda.

- <strong>Jadi apa sebenarnya VPN boleh lakukan? Ringkasnya: pertama,</strong> melindungi privasi anda pada Wi-Fi awam
- <strong>; kedua,</strong> memintas sekatan geografi

(contohnya melihat kandungan yang hanya tersedia di negara tertentu); ketiga,<strong>menghalang ISP anda daripada merekodkan tabuan pelayaran anda</strong>. Tetapi saya perlu ingatkan satu perkara:<strong>jangan guna VPN percuma!</strong> Di sebalik percuma sering bermakna data anda adalah "barang dagangan" mereka. Saya ada seorang kawan yang menggunakan VPN percuma tertentu, akibatnya telefonnya mula memaparkan iklan secara misteri, kemudian baru diketahui VPN itu menjual data pelayarannya kepada pengiklan dalam bentuk pakej. Jadi memilih VPN, sama ada pilih jenama berbayar besar (seperti NordVPN, ExpressVPN), atau jangan guna langsung.<strong>Selain itu, VPN bukan penyelesaian segala-galanya. Ia hanya melindungi data "dalam penghantaran", jika laman web sasaran itu sendiri tidak selamat, atau telefon anda sudah dijangkiti perisian hasad, VPN juga tidak dapat membantu anda.</strong>2. Perangkap Manis Wi-Fi Awam — Lebih Bahaya Daripada Yang Anda Bayangkan <strong>Anda mungkin rasa, bukankah hanya menyambung Wi-Fi percuma, berapa besar risikonya? Biar saya ceritakan satu kisah benar: penyelidik keselamatan pernah membuat eksperimen, memasang satu titik panas Wi-Fi bernama "Starbucks_Free" di lapangan terbang, dalam masa kurang satu jam sudah ada ratusan orang menyambung. Hakikatnya titik panas ini dibina oleh penyelidik sendiri, semua</strong> trafik tidak disulitkan

yang melalui titik panas ini—seperti kandungan laman HTTP yang anda layari, komunikasi App yang tidak mengaktifkan TLS—mereka benar-benar boleh menangkap dan melihatnya.

#### 2. Perangkap Manis Wi-Fi Awam — Lebih Bahaya Daripada Yang Anda Bayangkan

tidak dapat membaca secara langsung kandungan sembang atau kata laluan pembayaran anda <strong>. Namun mereka masih boleh mengetahui laman web mana yang anda lawati (nama domain), jika App atau laman web lama tertentu masih menggunakan penghantaran teks biasa HTTP, maka kandungannya akan terdedah sepenuhnya. Serangan ini dipanggil "Serangan Orang Tengah" (Man-in-the-Middle), prinsipnya ialah penyerang "menyisip" diri di antara anda dan penghala Wi-Fi sebenar. Yang lebih menakutkan, telefon ramai orang diset "auto-sambung Wi-Fi yang dikenali", penyerang hanya perlu menamakan titik panasnya dengan nama Wi-Fi yang pernah anda sambung sebelum ini (contohnya "ChinaNet" atau "CMCC"), telefon anda akan menyambung secara automatik.</strong> Jadi bagaimana mencegahnya? Beberapa cadangan praktikal:

Pastikan HTTPS <strong>: Permulaan bar alamat ialah https://, "s" tambahan bermaksud Secure. Apabila melawat mana-mana laman web yang memerlukan input kata laluan, jika yang anda lihat ialah http:// (tanpa s), berhenti serta-merta jangan input! Kini pelayar utama akan memaparkan amaran "tidak selamat" di laman web bukan HTTPS, apabila melihat tanda ini anda perlu berwaspada.</strong> Matikan "Auto-sambung"

: Sama ada iPhone atau Android, pergi ke tetapan Wi-Fi dan matikan "Auto-Join" atau "Auto-sambung". Lebih baik klik secara manual setiap kali, jangan biar telefon menilai sendiri.

- <strong>Gunakan data mudah alih untuk operasi sensitif</strong>: Pemindahan wang, log masuk perbankan dalam talian, memasukkan nombor kad pengenalan... operasi ini gunakan data 4G/5G anda sendiri secara jujur, jangan berkira sedikit kos data itu.
- <strong>Lupakan Wi-Fi yang jarang digunakan</strong>: Selepas pulang dari perjalanan perniagaan atau percutian, "lupakan" semua Wi-Fi hotel dan lapangan terbang yang pernah disambung sementara. Dengan ini telefon tidak akan menyambung secara automatik ke titik panas palsu dengan nama yang sama pada kali seterusnya.
- <strong>3. Bagaimana HTTPS Melindungi Anda? — Jabat Tangan SSL/TLS</strong> Tadi kita sebut tentang HTTPS, jadi bagaimana ia sebenarnya berfungsi? Setiap kali anda melawat laman web HTTPS, pelayar dan pelayan akan melakukan satu "jabat tangan SSL/TLS", keseluruhan proses lebih kurang seperti ini:
- <strong>Pelayar anda berkata: "Hei, pelayan, saya ingin berkomunikasi secara selamat dengan anda, ini senarai keupayaan penyulitan saya (algoritma penyulitan yang disokong dan lain-lain)."</strong> Pelayan membalas: "Baik, saya memilih skim penyulitan ini dari senarai anda, ini sijil digital saya, yang mengandungi kunci awam saya, ditandatangani dan disahkan oleh CA tertentu."

#### 3. Bagaimana HTTPS Melindungi Anda? — Jabat Tangan SSL/TLS

Selepas pengesahan lulus, kedua-dua pihak menggunakan penyulitan kunci awam untuk merundingkan satu "kunci sesi", komunikasi selepas itu semua disulitkan dengan kunci ini.

1. Ini seperti anda pergi ke bank untuk urusan: Anda menyerahkan kad pengenalan (sijil), kerani mengesahkan identiti anda, kemudian kedua-dua pihak bersetuju dengan satu kod rahsia, perbualan selepas itu hanya kedua-dua anda yang faham. Walaupun ada orang mengintip di sebelah, mereka hanya boleh mendengar kod sulit yang tidak bermakna.
2. Tetapi perhatikan: HTTPS hanya menjamin proses "penghantaran" disulitkan, tidak menjamin laman web sasaran adalah pihak yang baik. Laman web pancingan juga boleh menggunakan HTTPS—ikon gembok kecil itu hanya menunjukkan anda menyambung ke "sesuatu laman web", tidak bermakna laman web itu ialah yang anda ingin tuju. Jadi anda masih perlu menyemak sendiri sama ada alamat web adalah betul.
3. 4. Keselamatan DNS: Adakah "Buku Telefon Rangkaian" Anda Selamat?
4. DNS (Sistem Nama Domain) seperti buku telefon internet: anda memasukkan "baidu.com", DNS membantu anda mencari alamat IP yang sepadan (contohnya 110.242.68.66), kemudian pelayar baru boleh menyambung. Masalahnya ialah, pertanyaan DNS tradisional adalah

teks biasa

,

#### 4. Keselamatan DNS: Adakah "Buku Telefon Rangkaian" Anda Selamat?

! Maksudnya, ISP anda, penyedia Wi-Fi, atau mana-mana nod perantara, semuanya boleh melihat laman web mana yang anda telah lawati.<strong>Yang lebih menjengkelkan ialah "pembajakan DNS": penyerang mengganggu di bahagian DNS, mengarahkan "baidu.com" ke laman web pancingan palsu. Anda jelas memasukkan alamat web yang betul, tetapi dibawa ke halaman log masuk yang kelihatan sama tetapi sebenarnya palsu, sekali memasukkan akaun dan kata laluan anda sudah selesai.</strong> Nasib baik kini ada skim DNS sulit:<strong>DNS over HTTPS (DoH)</strong>: Menyembunyikan pertanyaan DNS dalam trafik HTTPS, bercampur dengan trafik pelayaran web biasa, mustahil untuk membezakan mana yang pertanyaan DNS.

DNS over TLS (DoT)

: Menggunakan protokol penyulitan TLS khusus untuk melindungi pertanyaan DNS, port berasingan, pentadbir rangkaian boleh mengetahui anda menggunakan DoT tetapi tidak dapat melihat kandungannya.

- <strong>Saya peribadi mengesyorkan menggunakan Cloudflare 1.1.1.1 atau Google 8.8.8.8 sebagai pelayan DNS, kedua-duanya menyokong DNS sulit. Dalam tetapan "DNS Peribadi" Android, terus isi "one.one.one.one" atau "dns.google", sangat mudah. iPhone agak lebih rumit, perlu memasang fail profil atau menetapkan melalui App, tetapi juga berbaloi untuk dilakukan.</strong>5. Adakah "Pelayaran Tanpa Jejak" Benar-Benar Menjadikan Anda Halimunan?
- <strong>Kesimpulan dahulu:</strong> Mod tanpa jejak adalah langsir rumah anda, bukan jubah halimunan.

Apa yang ia lakukan: Tidak meninggalkan jejak secara tempatan—selepas menutup tetingkap tanpa jejak, pelayar tidak menyimpan sejarah pelayaran, Cookies, rekod pengisian borang, rekod carian. Meminjam komputer orang lain untuk mencari sesuatu, atau membeli hadiah tanpa mahu dikesan oleh keluarga dari sejarah pelayaran, menggunakan mod tanpa jejak adalah sesuai.

#### 5. Adakah "Pelayaran Tanpa Jejak" Benar-Benar Menjadikan Anda Halimunan?

Lipatan melintang (gaya buku)<strong>masih boleh melihat anda datang</strong>

, alamat IP anda, maklumat peranti, tingkah laku pelayaran, jelas di pihak laman web.

ISP anda

- masih boleh melihat laman web mana yang anda lawati <strong>, hanya tidak dapat melihat kandungan khusus (jika menggunakan HTTPS).</strong> Pentadbir rangkaian syarikat/sekolah
- juga boleh memantau <strong>tingkah laku pelayaran anda.</strong> Fail yang anda muat turun, penanda buku yang ditambah akan
- kekal <strong>, tidak akan hilang apabila tetingkap ditutup.</strong> Jadi ingat: Mod tanpa jejak ialah "pemadam tempatan", bukan "jubah halimunan rangkaian". Jika anda benar-benar perlu menyembunyikan jejak pelayaran, perlu menggunakan gabungan VPN + pelayar Tor, tetapi untuk penggunaan harian, memahami perkara ini sudah memadai.
- 6. Privasi Pelayar: Jangan Biarkan Pelayar Menjual Anda mungkin tidak sedar, pelayar itu sendiri adalah sebuah pengumpul maklumat yang besar. Cookies, sejarah pelayaran, cache, auto-isi, kebenaran lokasi... setiap satu boleh membocorkan privasi anda. Beberapa cadangan: Bersihkan data pelayaran secara berkala

: Setiap beberapa ketika, pergi ke tetapan dan bersihkan Cookies, cache, sejarah pelayaran. Bukan untuk menghalang "penjejakan"—membersihkan Cookies sudah tidak begitu berkesan—tetapi untuk mengelakkan telefon semakin perlahan. Cache pelayar boleh menggunakan beberapa GB ruang.

#### 6. Privasi Pelayar: Jangan Biarkan Pelayar Menjual Anda

: Pilihan "Hantar permintaan 'Jangan Jejak'" dalam pelayar, hakikatnya ialah "memohon" laman web untuk tidak menjejak anda. Tetapi sama ada laman web mendengar atau tidak adalah urusan lain, kebanyakan laman web terus mengabaikannya. Jangan bergantung padanya.

- <strong>Manfaatkan pelayar perlindungan privasi</strong>: Firefox Focus, pelayar DuckDuckGo, Brave—pelayar ini secara lalai menyekat penjejak dan iklan, jauh lebih bersih daripada tetapan lalai Chrome dan Safari.
- <strong>Enjin carian juga penting</strong>: Gunakan DuckDuckGo menggantikan carian Baidu/Google, ia tidak merekodkan sejarah carian anda, tidak membina profil pengguna. Sejujurnya hasil carian memang tidak setepat Google, tetapi untuk carian maklumat harian sudah memadai.
- <strong>Semak kebenaran App</strong>: Pergi ke tetapan telefon dan lihat kebenaran apa yang diberikan kepada pelayar anda. Adakah ia benar-benar perlu mengakses lokasi, mikrofon, senarai kenalan anda? Kemungkinan besar tidak perlu.
- <strong>7. Senarai Keselamatan Praktikal: Lindungi Diri Anda Mulai Sekarang</strong> Sudah bercakap banyak, akhirnya berikan anda satu senarai keselamatan yang ringkas dan kasar, habiskan setengah jam, keselamatan telefon anda akan meningkat secara kualitatif:
- <strong>Matikan auto-sambung Wi-Fi</strong>: iPhone dalam Tetapan - WLAN, Android dalam tetapan Wi-Fi.

#### 7. Senarai Keselamatan Praktikal: Lindungi Diri Anda Mulai Sekarang

: Android terus tetapkan DNS Peribadi ke "dns.google", iPhone gunakan App atau fail profil untuk menetapkan DoH 1.1.1.1.

1. <strong>Aktifkan pengesahan dwifaktor (2FA)</strong>: WeChat, Alipay, Apple ID, akaun Google, mana yang boleh aktifkan 2FA, aktifkan semuanya. Kod pengesahan SMS sudah menjadi peringkat terendah 2FA, lebih baik gunakan TOTP (seperti Google Authenticator, Microsoft Authenticator).
2. <strong>Semak kebenaran App satu kali</strong>: Semak kebenaran setiap App satu persatu, terutamanya lima item: lokasi, senarai kenalan, SMS, mikrofon, kamera. Anda akan dapati sesetengah App lampu suluh sebenarnya meminta senarai kenalan anda—segera nyahpasang.
3. <strong>Bersihkan data pelayar secara berkala</strong>: Tetapkan peringatan kalendar, sekali sebulan, bersihkan cache, Cookies.
4. <strong>Jangan guna kabel data stesen pengecasan awam</strong>: Port USB boleh mengecas dan juga memindahkan data, stesen pengecasan hasad (dipanggil "Juice Jacking") boleh mencuri data semasa anda mengecas. Bawa penyesuai pengecasan dan kabel sendiri apabila keluar.
5. <strong>Buat sekarang: Berikan telefon anda satu "pemeriksaan keselamatan"</strong> Peningkatan DNS
6. <strong>: Android: Tetapan &gt; Sambungan &amp; Perkongsian &gt; DNS Peribadi &gt; Isikan "one.one.one.one" atau "dns.google". iPhone: Gunakan Safari untuk mencari "1.1.1.1 DNS profile" pasang fail profil, atau muat turun App Cloudflare 1.1.1.1.</strong> Audit Wi-Fi

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>: Buka senarai Wi-Fi, "lupakan" semua titik panas yang tidak dikenali, jarang digunakan, atau nama yang pelik.

{class="list-decimal pl-6 mt-1 space-y-1"}
1. <strong>Pembersihan besar kebenaran</strong>: Masuk ke Tetapan &gt; Privasi/Pengurusan Kebenaran, semak kebenaran App satu persatu. Tandai App yang meminta kebenaran tidak munasabah (contohnya kalkulator meminta senarai kenalan), pertimbangkan untuk menyahpasang atau gunakan pengganti.
2. <strong>Semak keselamatan akaun</strong>: Buka halaman keselamatan Apple ID atau akaun Google, lihat ada mana-mana peranti tidak dikenali log masuk, sahkan 2FA sudah diaktifkan, semak sama ada kontak pemulihan boleh dipercayai.
3. <strong>Bab 22: Cara AI Berfungsi dalam Telefon</strong> Selamat datang ke "pertunjukan sihir" paling hebat telefon, protagonisnya ialah: kecerdasan buatan. Foto cantik "sekali tangkap" yang anda gunakan setiap hari, pembantu suara yang responsif, kaedah input yang semakin memahami anda, di sebaliknya berdiri otak halimunan ini.
4. <strong>1. Kamera AI: "Bilik Gelap Pasca-Pemprosesan" Anda Berpindah ke Telefon</strong> Fotografi pengkomputeran AI masa kini lebih seperti memasukkan satu pasukan editor foto profesional + jurugambar terus ke dalam butang shutter. Sebelum anda menekan butang shutter, AI sudah mula berfungsi: mengimbas suasana, mengenal pasti "ini langit biru", "ini wajah manusia", "ini pemandangan malam".
:::
