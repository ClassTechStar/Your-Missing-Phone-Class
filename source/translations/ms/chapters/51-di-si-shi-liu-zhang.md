---
id: di-si-shi-liu-zhang
num: 46
part: ai-biancheng-pian
nav: Bab 46: Jalan Lanjutan—Daripada Pengguna kepada Arkitek
toc: default
kind: chapter
---

### Bab 46: Jalan Lanjutan — Daripada Pengguna kepada Arkitek

{class="chapter-intro mb-4"}
Apabila anda telah menguasai metodologi Bab 37 hingga 44 dan boleh menggunakan AI dengan mahir untuk menyiapkan pembangunan projek, apakah langkah seterusnya? Bab ini meneroka jalan naik taraf daripada "pengguna alat AI" kepada "arkitek sistem AI". Fokus pada peringkat ini bukan lagi "cara membuat AI menulis kod yang baik", tetapi "cara menjadikan AI lebih baik menyatu dengan keseluruhan aliran pembangunan".

#### 1. Protokol MCP dan pengembangan alat

MCP (Model Context Protocol) ialah satu protokol terbuka yang muncul pada 2025 dan semakin meluas pada 2026; ia mentakrifkan piawaian komunikasi antara model AI dengan alat luaran. Secara mudahnya, MCP membolehkan AI "menggunakan alat" — bukan sahaja menjana kod, malah menjalankan arahan, membuat pertanyaan pangkalan data, memanggil API dan mengendalikan sistem fail.

Sebelum MCP, setiap alat AI mempunyai cara integrasi alatnya sendiri yang tidak serasi antara satu sama lain. Kehadiran MCP bermakna: satu alat yang mematuhi piawaian MCP boleh digunakan oleh mana-mana alat AI yang menyokong MCP. Ini mengurangkan kos integrasi alat dengan banyak, dan juga mengembangkan sempadan keupayaan AI daripada "menjana teks" kepada "melaksanakan tindakan".

Bagi pengguna lanjutan, makna MCP ialah: anda boleh membina keupayaan alat tersuai untuk AI. Contohnya, jika pasukan anda mempunyai satu sistem pelancaran (deployment) dalaman, anda boleh menulis satu alat MCP supaya AI terus memanggil sistem pelancaran itu tanpa perlu bertukar secara manual ke terminal. Keupayaan "AI memanggil alat" inilah infrastruktur asas Agentic Engineering.

#### 2. Aliran kerja tersuai dan Skills

Apabila anda berulang kali menjalankan aliran pengaturcaraan AI yang tetap, anda boleh mengukuhkannya menjadi "aliran kerja tersuai" atau "Skills". Contohnya, pasukan anda mungkin mempunyai satu aliran semakan kod standard — semak keselamatan dahulu, kemudian prestasi, kemudian kebolehselenggaraan. Anda boleh menulis aliran ini menjadi satu Skill supaya AI secara automatik mengikutinya pada setiap semakan kod.

Nilai teras aliran kerja tersuai ialah "konsistensi" — ia memastikan setiap pelaksanaan mematuhi piawaian yang sama, tanpa sisihan akibat panjang perbualan atau perbezaan konteks. Ini amat penting untuk kerjasama pasukan: apabila setiap ahli menggunakan aliran kerja yang sama, gaya kod dan piawaian kualiti output akan cenderung seragam.

Cara membina aliran kerja tersuai berbeza mengikut alat. Cursor menyokong Rules dan Custom Instructions; Claude Code menyokong arahan tersuai; Replit menyokong Runme. Tetapi idea terasnya sama: "mengekod" amalan terbaik anda menjadi templat arahan yang boleh dilaksanakan oleh AI.

#### 3. Mod kerjasama berbilang Agent

Menjelang 2026, kerjasama berbilang Agent mula menjadi topik hangat. Idea terasnya: bukan hanya menggunakan satu AI untuk menyiapkan tugasan, tetapi menggunakan beberapa AI yang berpecah tugas untuk bekerjasama. Contohnya, satu AI bertanggungjawab menulis kod, satu AI menulis ujian, satu AI membuat semakan kod — masing-masing menjalankan tugasnya dan saling memeriksa.

Kelebihan kerjasama berbilang Agent terletak pada "pembahagian tugas" dan "pengesahan silang": setiap Agent memberi tumpuan kepada bidangnya sendiri, kualiti output lebih tinggi; pemeriksaan silang antara Agent dapat menemui masalah yang mungkin terlepas daripada pandangan sendiri. Tetapi kekurangannya juga jelas: kos penyelarasan tinggi, overhead komunikasi besar dan penyahpepijatan lebih rumit.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Tip: Seorang pun boleh bermain "berbilang Agent"

{class="mt-1"}
Bagi pembangun individu, anda tidak perlu membina sistem berbilang Agent yang kompleks — anda boleh "memegang watak" yang berbeza untuk mensimulasikan kerjasama berbilang Agent. Contohnya: gunakan satu perbualan untuk meminta AI menulis kod fungsi; kemudian buka satu perbualan baharu (dengan konteks CLAUDE.md), meminta AI "menyemak kod ini sebagai penyemak kod"; akhirnya buka satu perbualan lagi untuk meminta AI "membaiki kod berdasarkan pandangan semakan". Cara "seorang banyak watak" ini memperoleh sebahagian besar manfaat kerjasama berbilang Agent tanpa memerlukan infrastruktur yang kompleks.
:::

#### 4. Laluan pembelajaran berterusan

Pengaturcaraan AI ialah bidang yang berubah dengan pantas. Amalan terbaik hari ini mungkin perlu dikemas kini esok. Berikut beberapa cadangan untuk pembelajaran berterusan:

Pertama, perhatikan sumber asal, bukan tafsiran orang kedua. Tweet asal dan CLAUDE.md milik Andrej Karpathy, dokumentasi rasmi Anthropic dan OpenAI, log kemas kini alat-alat utama — semua ini maklumat sumber pertama. Artikel dan tutorial komuniti ialah tafsiran dan rumusan terhadap maklumat ini; ada nilainya tetapi mungkin terpesong. Amalkan tabiat membaca bahan asal.

Kedua, pembelajaran dipacu amalan. Jangan "habis belajar baharu mahu buat", tetapi "belajar sambil buat". Setiap kali menemui jenis masalah baharu (contohnya kali pertama mengendalikan muat naik fail atau kali pertama menyambung API pihak ketiga), jadikan itu peluang untuk mempelajari pengetahuan berkaitan. Kecekapan pembelajaran dalam amalan jauh lebih tinggi daripada pembelajaran teori yang terpisah daripada situasi.

Ketiga, kekal peka terhadap alat tetapi jangan berlebihan mengejar yang baharu. Setiap satu dua bulan, luangkan setengah hari untuk mengetahui alat dan trend terkini — tetapi jangan bertukar setiap kali ada alat baharu. Ukurannya: adakah alat baharu itu dapat meningkatkan dengan ketara salah satu bottleneck anda? Jika tidak, gabungan semasa sudah memadai.

Keempat, bina pangkalan pengetahuan peribadi. Rekodkan setiap perbualan ketika menyelesaikan masalah kompleks, setiap pengajaran daripada terpijak perangkap dan setiap kaedah yang berkesan. Tidak perlu diterbitkan secara terbuka — ini "nota metodologi" anda sendiri. Dengan pengumpulan dari masa ke masa, ia akan menjadi aset paling berharga anda.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Mari praktik: buka satu "buku nota pengajaran perangkap"

{class="mt-1"}
Mulakan hari ini dengan membina satu dokumen (perisian nota atau fail .md pun boleh), dan tuliskan tiga pandangan pengaturcaraan AI yang paling anda ingin ingat setakat ini — walaupun sekadar "ingat, fikir dahulu dengan jelas sebelum bertanya". Selepas ini, setiap kali terpijak perangkap atau mempelajari muslihat baharu, catatkan satu entri ke dalamnya. Enam bulan kemudian apabila membaca semula, anda akan berterima kasih kepada diri anda hari ini.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Ringkasan bab ini

- MCP ialah piawaian komunikasi antara AI dan alat: membolehkan AI menjalankan arahan, bertanya pangkalan data dan memanggil API
- Nilai teras aliran kerja tersuai/Skills ialah "konsistensi": mengekod amalan terbaik menjadi templat arahan
- Berbilang Agent = pembahagian tugas + pengesahan silang; pembangun individu boleh mensimulasikan dengan "seorang banyak watak"
- Empat kaedah pembelajaran berterusan: baca sumber asal, belajar sambil buat, jangan berlebihan mengejar yang baharu, bina pangkalan pengetahuan peribadi
:::
