---
id: di-san-shi-liu-zhang
num: 36
part: er-tong-pian
nav: Bab 36:Telefon dan Rumah Pintar—Membuat Rumah Lebih Bijak
toc: default
kind: chapter
---

### Bab 36:Telefon dan rumah pintar - menjadikan rumah anda pintar

{class="chapter-intro mb-4"}
Telefon juga boleh melakukan satu perkara yang semakin penting - menjadi "alat kawalan jauh" untuk seluruh rumah. Dari sebuah lampu, satu soket, hinggalah satu kunci pintu, rumah pintar sedang bertukar daripada "mainan peminat teknologi" kepada "kelengkapan harian". Bab ini membantu anda memahami protokol, ekosistem, hab, dan set permulaan, kemudian ditutup dengan senarai semak keselamatan, supaya anda tidak menjadi mangsa "kepintaran" itu sendiri.

#### 1. Protokol rumah pintar: pilihan anda sangat penting

Sebelum membeli peranti pintar, lihat dahulu protokol yang disokongnya; ini menentukan sama ada ia boleh "diperintah" oleh telefon dan ekosistem anda. Kini terdapat empat protokol utama, dengan sifat masing-masing seperti berikut:

- Protokol Matter: dikeluarkan pada 2022 oleh CSA (Connectivity Standards Alliance), di sebaliknya ialah gergasi seperti Apple, Google, Amazon, dan Samsung yang bergabung tenaga. Matlamatnya hanya satu - membolehkan peranti pintar semua jenama bertutur dalam bahasa yang sama. Pada 2023-2026 ia sedang pesat menjadi piawaian penyatuan; peranti yang menyokongnya boleh disambungkan serentak ke Apple HomeKit, Google Home, Amazon Alexa, dan Mijia, tidak lagi terikat kepada satu ekosistem sahaja.
- Protokol Thread: "paip" rangkaian asas bagi Matter. Penggunaan kuasa rendah, membentuk rangkaian sendiri (jika satu nod tiada bekalan kuasa, isyarat secara automatik melalui laluan lain), respons pantas tanpa tersangkut. Beli peranti yang mempunyai Thread Border Router (seperti HomePod mini, Apple TV 4K, hab gateway Xiaomi), pengalamannya jelas lebih stabil.
- Wi-Fi: jalur lebar besar, boleh sambung terus ke penghala, tetapi penggunaan kuasa tinggi dan mudah sesak apabila banyak peranti; sesuai untuk kamera, robot penghisap debu dan peranti yang perlu memindahkan data besar.
- Bluetooth (BLE): pemasangan rangkaian mudah dan jimat kuasa, tetapi jarak pendek dan tidak boleh membentuk rangkaian sendiri; sesuai untuk kunci pintu, alat suhu dan kelembapan, serta peranti data kecil.
- Zigbee: protokol lama berkuasa rendah yang membentuk rangkaian sendiri, memerlukan gateway khusus; peranti murah dan stabil, tetapi keserasian merentas jenama lemah, dan sedang digantikan secara beransur oleh Matter+Thread.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
Prinsip dalam satu ayat

{class="mt-1"}
Pada 2026 apabila membeli peranti pintar, utamakan melihat sama ada ada label "Matter over Thread" - ini pilihan yang paling tahan ujian masa pada masa kini. Peranti lama yang hanya menyokong Wi-Fi atau Bluetooth tidak perlu ditinggalkan dengan tergesa-gesa; gunakan dahulu, dan beralih ke Matter semasa membeli yang baharu.
:::

#### 2. Perbandingan tiga ekosistem utama

Protokol ialah "bahasa", ekosistem ialah "kumpulan". Walaupun semuanya menyokong Matter, anda masih perlu memilih satu ekosistem utama untuk membina automasi dan kawalan suara. Perbandingan tiga ekosistem utama seperti berikut:

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                    <thead>
                        <tr class="bg-light dark:bg-gray-700">
                            <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ekosistem</th>
                            <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Kelebihan</th>
                            <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Kekurangan</th>
                            <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Sesuai untuk</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple HomeKit</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Privasi paling kuat (terutamanya pemprosesan setempat), integrasi lancar dengan iPhone/Siri/Shortcut</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Bilangan peranti kurang dan agak mahal, perlukan HomePod atau Apple TV sebagai hab</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pengguna yang seluruh keluarganya guna peranti Apple dan mengutamakan privasi serta pengalaman</td>
                        </tr>
                        <tr>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mijia (Xiaomi)</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pilihan peranti paling banyak, nilai wang terbaik, pembantu suara Xiao AI mudah digunakan</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ekosistem agak tertutup, banyak data dimuat naik ke awan, iklan agak banyak</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pengguna baharu yang bajet terhad dan mahu melengkapkan seluruh rumah dalam satu tempat</td>
                        </tr>
                        <tr>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Huawei Smart Life (HarmonyOS)</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Peralihan tanpa jahitan dengan telefon/tablet/jam HarmonyOS, bilangan peranti berkembang pesat</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Sokongan peranti luar negara kurang, ekosistem masih mengejar</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Pengguna telefon Huawei yang menghargai kerjasama berbilang peranti "Super Device"</td>
                        </tr>
                    </tbody>
                </table>
```

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
Cadangan membuat keputusan memilih ekosistem

{class="mt-1"}
Pilih ekosistem mengikut telefon: pengguna iPhone utamakan HomeKit, pengguna Huawei utamakan Smart Life, pengguna Android lain paling senang dengan Mijia. Dengan protokol Matter, peranti dari ekosistem berbeza juga boleh dikawal oleh telefon yang sama, jadi anda tidak perlu "berpihak" sekali untuk selama-lamanya.
:::

#### 3. Telefon sebagai hab rumah

Dalam kebanyakan senario permulaan, telefon itulah "hab rumah" anda - mengawal lampu, penghawa dingin, langsir, dan keselamatan melalui aplikasi, malah boleh membina senario automasi supaya rumah "bergerak dengan sendirinya":

- Kawalan peranti: buka aplikasi HomeKit/Mijia/AI Life, boleh menyalakan dan mematikan lampu dari jauh atau setempat, laraskan suhu warna, tetapkan suhu penghawa dingin, tutup buka langsir, dan lihat paparan kamera.
- Senario automasi: gabungkan "syarat -> tindakan"; tiga senario yang paling kerap digunakan: Mod pulang: lokasi sampai rumah + langit gelap -> nyalakan lampu lobi + hidupkan penghawa dingin + tutup langsir + kunci pintu.
- Mod keluar rumah: orang terakhir keluar (lokasi meninggalkan rumah atau pintu dikunci) -> matikan lampu + matikan penghawa dingin + matikan soket + aktifkan kamera + aktifkan sistem pengawasan.
- Mod tidur: setiap malam jam 23:00 -> matikan semua lampu utama + tutup langsir + penghawa dingin ditetapkan 26 darjah + nyalakan lampu malam.

- Sentuh NFC: tampal satu label NFC di pintu, dan telefon yang disentuh terus mencetuskan senario berkenaan (sentuh sekali untuk lampu masuk pintu, sentuh lagi untuk mod tidur). iPhone menggunakan automasi "Shortcut", sementara Android boleh menulis melalui "Dompet" atau aplikasi pengeluar.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mari cuba: bina "Mod Pulang"

{class="mt-1"}
Dalam bahagian "Automasi" aplikasi rumah pintar telefon anda, cipta satu yang baharu: pilih syarat pencetus "sampai ke sesuatu lokasi" (rumah), kemudian tambahkan tindakan satu demi satu "nyalakan lampu lobi" "tetapkan penghawa dingin 26 darjah" "tutup langsir". Selepas simpan, keluar berjalan sebentar dan pulang untuk melihat sama ada lampu menyala dengan sendirinya - rasa berjaya kali pertama itu lebih mengujakan daripada membeli peranti baharu.
:::

#### 4. Cadangan set permulaan

Tidak perlu melengkapkan semuanya sekaligus; bermula dengan set empat perkara ini sudah menampung kira-kira 80% keperluan harian:

- Speaker pintar: Xiao AI (ekosistem Mijia, nilai wang tinggi) / HomePod mini (ekosistem Apple, sekali gus menjadi hab Thread) / Alexa (liputan ekosistem luar negara luas). Perhatian: speaker menentukan ekosistem suara anda, jadi tentukan ekosistem dahulu sebelum membeli speaker.
- Mentol pintar: Yeelight (Mijia/Matter, suhu warna dan kecerahan boleh dilaras, murah) / Philips Hue (warna cantik, stabil, tetapi perlukan Hue Bridge, agak mahal). Perhatian: sebelum membeli, sahkan saiz soket mentol (E27/B22) dan sama ada anda perlu laras warna.
- Soket pintar: soket pintar Xiaomi (murah, ada statistik penggunaan elektrik) / TP-Link Kasa (sokongan Matter luar negara baik). Perhatian: apabila digunakan untuk peranti berkuasa tinggi (pemanas air, pemanas ruang), pastikan semak kuasa terkadarnya, jangan melebihi beban.
- Kunci pintu pintar: Lockin/Xiaomi (nilai wang, integrasi Mijia) / Kaadas (pengeluar kunci tradisional besar, struktur mekanikal mantap). Perhatian: sahkan sama ada menyokong Matter atau ekosistem anda, dan perhatikan jangka hayat bateri serta lokasi lubang kunci kecemasan.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
Cadangan turutan pembelian

{class="mt-1"}
Beli speaker pintar dahulu (tentukan ekosistem) -> kemudian mentol dan soket pintar (ambang rendah, kesan serta-merta) -> akhir sekali kunci pintu dan kamera (melibatkan keselamatan, pilih dengan teliti). Tambah hanya satu jenis peranti pada satu masa, biasakan dahulu sebelum menambah lagi, supaya elak "beli tapi tak tahu guna".
:::

#### 5. Perkara keselamatan yang perlu diberi perhatian

Semakin banyak peranti pintar di rumah, semakin luas permukaan serangan. Empat perkara berikut ialah garis bawah, sila semak satu demi satu:

1. Tukar kata laluan lalai: kata laluan lalai kilang kamera, penghala, dan kunci pintu semuanya boleh didapati terbuka di internet; perkara pertama selepas membeli ialah menukarnya kepada kata laluan kukuh yang "panjang dan tidak berulang".
2. Kemas kini firmware dengan tepat pada masanya: firmware yang dihantar pengeluar selalunya membaiki celah keselamatan; aktifkan "kemas kini automatik" dalam aplikasi, atau sekurang-kurangnya semak secara manual sekali sebulan.
3. Pengasingan rangkaian: letakkan peranti IoT pada satu Wi-Fi berasingan (atau rangkaian tetamu), terpisah daripada rangkaian utama telefon dan komputer. Jika sesuatu peranti ditembusi, sukar pula untuk mengancam data penting anda secara melintang.
4. Perlindungan privasi: aktifkan penutupan "zon privasi" pada kamera (contohnya bilik tidur dan bilik air tidak dirakam), matikan rakaman awan 24 jam; jangan biarkan paparan kamera semasa anda tiada di rumah dibuka kepada aplikasi pihak ketiga untuk jangka panjang.

::: div .danger-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
Jangan terpijak perangkap-perangkap ini

{class="list-disc pl-6 mt-1 space-y-1"}
- Jangan gunakan fungsi "buka kunci jauh" kunci pintu untuk orang asing - utamakan kata laluan sementara yang luput sebaik digunakan.
- Jangan arahkan kamera terus ke katil atau ke luar tingkap - yang terbocor ialah privasi anda sendiri.
- Jangan terpedaya harga murah membeli peranti "tanpa jenama" - kebanyakannya tidak mengemas kini firmware, sama seperti memasang pintu belakang di rumah anda.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan bab ini

{class="list-disc pl-5 text-sm space-y-0.5"}
- Matter+Thread ialah arah penyatuan 2023-2026; apabila membeli peranti baharu, utamakan melihat label ini
- Tiga ekosistem utama masing-masing ada kelebihannya: Apple mengutamakan privasi dan pengalaman, Mijia mengutamakan nilai wang, Huawei mengutamakan kerjasama berbilang peranti
- Telefon boleh menjadi hab; apabila tiga senario "pulang/keluar/tidur" dibina dengan baik, rumah boleh bergerak dengan sendirinya
- Set permulaan empat perkara: speaker pintar, mentol, soket, kunci pintu; tambah secara beransur mengikut turutan ini
- Tukar kata laluan lalai, kemas kini firmware, asingkan rangkaian, tutup zon privasi - empat garis bawah keselamatan yang tidak boleh diketepikan
:::
