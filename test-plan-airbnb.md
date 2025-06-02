---

**<<Dokumen Rencana Pengujian - SOW # opsional>>**

**<<Aplikasi Web Airbnb - [Nama Institusi Anda]>>**

**Rencana Pengujian**

**Riwayat Perubahan Dokumen**

| Nomor Versi | Tanggal | Kontributor | Deskripsi |
|---|---|---|---|
| V1.0 | 2025-06-02 | [Nama Anda/Tim Anda] | Draf Awal Rencana Pengujian untuk Aplikasi Web Airbnb |

---

**Daftar Isi**

1.  [Pendahuluan](#1-pendahuluan)
    1.1. [Lingkup](#11-lingkup)
    1.1.1. [Dalam Lingkup](#111-dalam-lingkup)
    1.1.2. [Di Luar Lingkup](#112-di-luar-lingkup)
    1.2. [Tujuan Kualitas](#12-tujuan-kualitas)
    1.2.1. [Tujuan Utama](#121-tujuan-utama)
    1.2.2. [Tujuan Sekunder](#122-tujuan-sekunder)
    1.3. [Peran dan Tanggung Jawab](#13-peran-dan-tanggung-jawab)
    1.3.1. [Pengembang (Developer)](#131-pengembang-developer)
    1.3.2. [Pengguna/Penguji (Adopter/Tester)](#132-penggunapenguji-adoptertester)
    1.3.3. [Tim Manajemen Proses Pengujian](#133-tim-manajemen-proses-pengujian)
    1.4. [Asumsi untuk Eksekusi Pengujian](#14-asumsi-untuk-eksekusi-pengujian)
    1.5. [Kendala untuk Eksekusi Pengujian](#15-kendala-untuk-eksekusi-pengujian)
    1.6. [Definisi](#16-definisi)
2.  [Metodologi Pengujian](#2-metodologi-pengujian)
    2.1. [Tujuan](#21-tujuan)
    2.1.1. [Ikhtisar](#211-ikhtisar)
    2.1.2. [Pengujian Kegunaan (Usability Testing)](#212-pengujian-kegunaan-usability-testing)
    2.1.3. [Pengujian Unit (Multiple)](#213-pengujian-unit-multiple)
    2.1.4. [Pengujian Iterasi/Regresi](#214-pengujian-iterasiregresi)
    2.1.5. [Pengujian Rilis Final](#215-pengujian-rilis-final)
    2.1.6. [Kriteria Kelengkapan Pengujian](#216-kriteria-kelengkapan-pengujian)
    2.2. [Tingkat Pengujian](#22-tingkat-pengujian)
    2.2.1. [Pengujian Build](#221-pengujian-build)
    2.2.1.1. [Tingkat 1 - Pengujian Penerimaan Build](#2211-tingkat-1---pengujian-penerimaan-build)
    2.2.1.2. [Tingkat 2 - Pengujian Asap (Smoke Tests)](#2212-tingkat-2---pengujian-asap-smoke-tests)
    2.2.1.3. [Tingkat 2a - Pengujian Regresi Bug](#2213-tingkat-2a---pengujian-regresi-bug)
    2.2.2. [Pengujian Tonggak (Milestone Tests)](#222-pengujian-tonggak-milestone-tests)
    2.2.2.1. [Tingkat 3 - Pengujian Jalur Kritis (Critical Path Tests)](#2221-tingkat-3---pengujian-jalur-kritis-critical-path-tests)
    2.2.3. [Pengujian Rilis](#223-pengujian-rilis)
    2.2.3.1. [Tingkat 4 - Pengujian Standar](#2231-tingkat-4---pengujian-standar)
    2.2.3.2. [Tingkat 5 - Pengujian yang Disarankan](#2232-tingkat-5---pengujian-yang-disarankan)
    2.3. [Regresi Bug](#23-regresi-bug)
    2.4. [Triage Bug](#24-triage-bug)
    2.5. [Kriteria Penangguhan dan Persyaratan Lanjutan](#25-kriteria-penangguhan-dan-persyaratan-lanjutan)
    2.6. [Kelengkapan Pengujian](#26-kelengkapan-pengujian)
    2.6.1. [Kondisi Standar:](#261-kondisi-standar)
    2.6.2. [Kondisi Pelaporan & Triage Bug:](#262-kondisi-pelaporan--triage-bug)
3.  [Hasil Pengujian (Test Deliverables)](#3-hasil-pengujian-test-deliverables)
    3.1. [Matriks Hasil](#31-matriks-hasil)
    3.2. [Dokumen](#32-dokumen)
    3.2.1. [Dokumen Pendekatan Pengujian](#321-dokumen-pendekatan-pengujian)
    3.2.2. [Rencana Pengujian](#322-rencana-pengujian)
    3.2.3. [Jadwal Pengujian](#323-jadwal-pengujian)
    3.2.4. [Spesifikasi Pengujian](#324-spesifikasi-pengujian)
    3.2.5. [Matriks Ketertelusuran Persyaratan (Requirements Traceability Matrix)](#325-matriks-ketertelusuran-persyaratan-requirements-traceability-matrix)
    3.3. [Pelacakan Cacat & Debugging](#33-pelacakan-cacat--debugging)
    3.3.1. [Alur Kerja Pengujian](#331-alur-kerja-pengujian)
    3.3.2. [Pelaporan Cacat menggunakan G FORGE](#332-pelaporan-cacat-menggunakan-g-forge)
    3.4. [Laporan](#34-laporan)
    3.4.1. [Laporan status pengujian](#341-laporan-status-pengujian)
    3.4.2. [Laporan Penyelesaian Tahap](#342-laporan-penyelesaian-tahap)
    3.4.3. [Laporan Akhir Pengujian - Penandatanganan](#343-laporan-akhir-pengujian---penandatanganan)
    3.5. [Matriks Tanggung Jawab](#35-matriks-tanggung-jawab)
4.  [Kebutuhan Sumber Daya & Lingkungan](#4-kebutuhan-sumber-daya--lingkungan)
    4.1. [Alat Pengujian](#41-alat-pengujian)
    4.1.1. [Alat Pelacakan](#411-alat-pelacakan)
    4.1.1.1. [Manajemen Konfigurasi](#4111-manajemen-konfigurasi)
    4.2. [Lingkungan Pengujian](#42-lingkungan-pengujian)
    4.2.1. [Perangkat Keras](#421-perangkat-keras)
    4.2.2. [Perangkat Lunak](#422-perangkat-lunak)
    4.3. [Definisi Tingkat Keparahan dan Prioritas Bug](#43-definisi-tingkat-keparahan-dan-prioritas-bug)
    4.3.1. [Daftar Tingkat Keparahan](#431-daftar-tingkat-keparahan)
    4.3.2. [Daftar Prioritas](#432-daftar-prioritas)
    4.4. [Pelaporan Bug](#44-pelaporan-bug)
5.  [Istilah/Singkatan](#5-istilahsingkatan)

---

**Pendahuluan**

Dokumen pendekatan pengujian ini menjelaskan strategi, proses, alur kerja, dan metodologi yang tepat yang digunakan untuk merencanakan, mengorganisir, melaksanakan, dan mengelola pengujian proyek perangkat lunak.

Rencana pengujian ini menjelaskan strategi, proses, alur kerja, dan metodologi yang digunakan untuk merencanakan, mengorganisir, melaksanakan, dan mengelola pengujian untuk Aplikasi Web Airbnb.

**1.1 Lingkup**

Jelaskan cakupan pendekatan pengujian saat ini berdasarkan peran dan tujuan proyek Anda.

**1.1.1 Dalam Lingkup**

Rencana Pengujian Aplikasi Web Airbnb mendefinisikan pendekatan pengujian unit, integrasi, sistem, regresi, dan Penerimaan Klien (Client Acceptance testing). Lingkup pengujian meliputi hal-hal berikut:

- Pengujian semua persyaratan fungsional, kinerja aplikasi, keamanan, dan kasus penggunaan yang tercantum dalam dokumen Kasus Penggunaan untuk Aplikasi Web Airbnb.
- Persyaratan kualitas dan metrik kesesuaian untuk Aplikasi Web Airbnb.
- Pengujian end-to-end dan pengujian antarmuka dari semua sistem yang berinteraksi dengan Aplikasi Web Airbnb (misalnya, gateway pembayaran, layanan pemetaan).
- Pendaftaran dan Login Pengguna.
- Pencarian dan Filter Properti (Listing).
- Proses Pemesanan dan Reservasi.
- Manajemen Properti Host (membuat, mengedit, menghapus listing).
- Manajemen Profil Pengguna.
- Sistem Pesan antara Tamu dan Host.
- Sistem Peninjauan dan Peringkat.
- Proses Pembayaran dan Pengembalian Dana.
- Desain Responsif di berbagai perangkat (desktop, tablet, web seluler).
- Pengujian keamanan (misalnya, otentikasi, otorisasi, privasi data).
- Pengujian kinerja (misalnya, waktu muat halaman, waktu respons di bawah beban).

**1.1.2 Di Luar Lingkup**

Berikut ini dianggap di luar lingkup Rencana Pengujian sistem Airbnb dan cakupan pengujian:

- Pengujian persyaratan fungsional untuk sistem di luar aplikasi Airbnb (misalnya, integrasi pihak ketiga yang tidak langsung dikelola oleh Airbnb).
- Pengujian SOP Bisnis, pemulihan bencana, dan Rencana Kelangsungan Bisnis.
- Aplikasi seluler _native_ (iOS/Android).
- Pengujian API backend (kecuali jika terkait langsung dengan masalah fungsionalitas front-end).
- Pengujian kompatibilitas perangkat keras untuk perangkat pengguna tertentu di luar kompatibilitas browser umum.

**1.2 Tujuan Kualitas**

**1.2.1 Tujuan Utama**

Tujuan utama pengujian sistem aplikasi adalah untuk: memastikan bahwa sistem memenuhi semua persyaratan, termasuk persyaratan kualitas (AKA: persyaratan non-fungsional) dan metrik kesesuaian untuk setiap persyaratan kualitas dan memenuhi skenario kasus penggunaan serta menjaga kualitas produk. Pada akhir siklus pengembangan proyek, pengguna harus menemukan bahwa proyek telah memenuhi atau melampaui semua harapan mereka sebagaimana dirinci dalam persyaratan. Setiap perubahan, penambahan, atau penghapusan pada dokumen persyaratan, Spesifikasi Fungsional, atau Spesifikasi Desain akan didokumentasikan dan diuji pada tingkat kualitas tertinggi yang diizinkan dalam sisa waktu proyek dan dalam kemampuan tim pengujian.

Untuk Aplikasi Web Airbnb, ini berarti memastikan:

- Semua persyaratan fungsional yang ditentukan (misalnya, pencarian, pemesanan, manajemen listing) terpenuhi secara akurat dan efisien.
- Aplikasi berkinerja andal di bawah beban pengguna yang diharapkan.
- Antarmuka pengguna intuitif dan ramah pengguna.
- Kerentanan keamanan diidentifikasi dan ditangani.

**1.2.2 Tujuan Sekunder**

Tujuan sekunder pengujian sistem aplikasi akan menjadi: mengidentifikasi dan mengungkapkan semua masalah dan risiko terkait, mengkomunikasikan semua masalah yang diketahui kepada tim proyek, dan memastikan bahwa semua masalah ditangani dengan tepat sebelum rilis. Sebagai tujuan, ini membutuhkan pengujian aplikasi yang cermat dan metodis untuk pertama-tama memastikan semua area sistem diteliti dan, sebagai hasilnya, semua masalah (bug) yang ditemukan ditangani dengan tepat.

**1.3 Peran dan Tanggung Jawab**

Peran dan tanggung jawab dapat berbeda berdasarkan SOW yang sebenarnya. Fungsi yang tercantum di bawah ini adalah untuk fase pengujian.

**1.3.1 Pengembang (Developer)**

Bertanggung jawab untuk:

- Mengembangkan aplikasi web Airbnb.
- Mengembangkan kasus penggunaan dan persyaratan bekerja sama dengan Pengguna (Pemilik Produk/Analis Bisnis).
- Melakukan pengujian unit, sistem, regresi, dan integrasi untuk modul yang mereka kembangkan.
- Mendukung pengujian penerimaan pengguna.
- Melakukan debugging dan memperbaiki cacat yang dilaporkan.

**1.3.2 Pengguna/Penguji (Adopter/Tester)**

Bertanggung jawab untuk:

- Berkontribusi pada pengembangan kasus penggunaan, persyaratan melalui tinjauan.
- Berkontribusi untuk mengembangkan dan mengeksekusi skrip pengujian pengembangan melalui tinjauan.
- Melakukan Pengujian Penerimaan Pengguna Penuh, regresi, dan pengujian end-to-end; ini termasuk mengidentifikasi skenario pengujian, membangun skrip pengujian, mengeksekusi skrip, dan melaporkan hasil pengujian.
- Memberikan umpan balik tentang kegunaan dan fungsionalitas dari perspektif pengguna akhir.

**1.3.3 Tim Manajemen Proses Pengujian**

Grup ini bertanggung jawab untuk mengelola seluruh proses pengujian, alur kerja, dan manajemen kualitas dengan kegiatan dan tanggung jawab untuk:

- Memantau dan mengelola integritas pengujian dan mendukung kegiatan pengujian.
- Mengkoordinasikan kegiatan di seluruh pusat kanker.
- Memastikan kepatuhan terhadap rencana pengujian dan tujuan kualitas.
- Memfasilitasi rapat triage bug.
- Memberikan panduan yang tepat kepada Pengguna dan Pengembang untuk melakukan pengujian.

**1.4 Asumsi untuk Eksekusi Pengujian**

Di bawah ini adalah beberapa asumsi minimum (hitam) yang harus dilengkapi dengan beberapa contoh (merah). Contoh apa pun dapat digunakan jika dianggap sesuai untuk proyek tertentu. Asumsi baru juga dapat ditambahkan yang dianggap sesuai untuk proyek.

- Untuk pengujian Penerimaan Pengguna, tim Pengembang telah menyelesaikan pengujian unit, sistem, dan integrasi serta memenuhi semua Persyaratan (termasuk persyaratan kualitas) berdasarkan Matriks Ketertelusuran Persyaratan.
- Pengujian Penerimaan Pengguna akan dilakukan oleh Pengguna Akhir atau penguji QA khusus yang mensimulasikan perilaku pengguna akhir.
- Hasil pengujian akan dilaporkan setiap hari menggunakan [Alat pelacakan bug pilihan Anda, mis. Jira, Asana, Trello, atau GForge sesuai template].
- Skrip yang gagal dan daftar cacat dari [Alat pelacakan bug pilihan Anda] dengan bukti akan dikirim langsung ke Pengembang atau melalui alat yang ditunjuk.
- Kasus penggunaan telah dikembangkan oleh Pengguna untuk pengujian Penerimaan Pengguna. Kasus penggunaan disetujui oleh pemimpin pengujian.
- Skrip pengujian dikembangkan dan disetujui.
- Ketergantungan utama harus segera dilaporkan setelah rapat _kickoff_ pengujian.
- Data pengujian yang diperlukan akan tersedia di lingkungan pengujian.
- Lingkungan pengujian akan stabil dan dapat diakses selama siklus pengujian.

**1.5 Kendala untuk Eksekusi Pengujian**

Di bawah ini adalah beberapa asumsi minimum (hitam) diikuti dengan contoh kendala (merah). Contoh apa pun dapat digunakan jika dianggap sesuai untuk proyek tertentu. Kendala baru juga dapat ditambahkan yang dianggap sesuai untuk proyek.

- Pengguna harus memahami dengan jelas prosedur pengujian dan pencatatan cacat atau peningkatan.
- Tim Manajemen Proses Pengujian akan menjadwalkan telekonferensi dengan Pengembang dan Pengguna untuk melatih dan mengatasi masalah terkait pengujian.
- Pengembang akan menerima daftar konsolidasi permintaan untuk pengaturan lingkungan pengujian, pengaturan akun pengguna, set data (data aktual dan data tiruan), daftar cacat, dll. melalui [Alat pelacakan bug pilihan Anda] setelah rapat _kickoff_ pengujian Pengguna awal.
- Pengembang akan mendukung kegiatan pengujian yang sedang berlangsung berdasarkan prioritas.
- Skrip pengujian harus disetujui oleh Pemimpin Pengujian sebelum eksekusi pengujian.
- Skrip pengujian, lingkungan pengujian, dan ketergantungan harus ditangani selama rapat _kickoff_ pengujian di hadapan SME dan daftar permintaan harus diajukan dalam waktu 3 hari setelah rapat _kickoff_.
- Pengembang tidak dapat mengeksekusi skrip pengujian Penerimaan Pengguna dan End-to-End. Setelah debugging, pengembang dapat melakukan pengujian internal mereka, tetapi tidak ada hasil dari pengujian tersebut yang dapat dicatat/dilaporkan.
- Pengguna bertanggung jawab untuk mengidentifikasi ketergantungan antara skrip pengujian dan mengajukan permintaan yang jelas untuk menyiapkan lingkungan pengujian.
- Ketersediaan terbatas dari lingkungan pengujian spesifik (misalnya, versi browser atau jenis perangkat tertentu).
- Kendala waktu untuk setiap fase pengujian, sebagaimana didefinisikan dalam jadwal pengujian.
- Ketergantungan pada layanan atau API pihak ketiga yang mungkin memiliki _downtime_ atau batasan sendiri.

**1.6 Definisi**

- **Bug**: Setiap kesalahan atau cacat yang menyebabkan perangkat lunak/aplikasi atau perangkat keras tidak berfungsi. Hal tersebut juga termasuk dalam persyaratan dan tidak memenuhi alur kerja, proses, atau titik fungsi yang diperlukan.
- **Peningkatan (Enhancement)**: 1) Setiap perubahan atau modifikasi pada sistem yang ada untuk alur kerja dan proses yang lebih baik. 2) Kesalahan atau cacat yang menyebabkan perangkat lunak/aplikasi atau perangkat keras tidak berfungsi. Di mana 1) dan 2) TIDAK termasuk dalam persyaratan dapat dikategorikan sebagai peningkatan. Peningkatan dapat ditambahkan sebagai persyaratan baru setelah proses Manajemen Perubahan yang tepat.
- **UAT (User Acceptance Testing)**: Pengujian formal oleh pengguna akhir atau perwakilan klien untuk memastikan sistem memenuhi persyaratan bisnis dan sesuai untuk tujuan.
- **Pengujian Fungsional**: Pengujian untuk memastikan perangkat lunak berfungsi sesuai dengan spesifikasinya.
- **Pengujian Non-fungsional**: Pengujian atribut sistem yang tidak terkait dengan fungsi tertentu, seperti keandalan, kegunaan, efisiensi, dan pemeliharaan.
- **Pengujian Regresi**: Pengujian ulang untuk memastikan bahwa perubahan atau penambahan pada perangkat lunak tidak memengaruhi fungsionalitas yang ada secara negatif.

**2. Metodologi Pengujian**

**2.1 Tujuan**

**2.1.1 Ikhtisar**

Daftar di bawah ini tidak dimaksudkan untuk membatasi luasnya rencana pengujian dan dapat dimodifikasi agar sesuai untuk proyek tertentu. Tujuan dari Rencana Pengujian adalah untuk mencapai hal-hal berikut:

- Mendefinisikan strategi pengujian untuk setiap area dan sub-area untuk menyertakan semua persyaratan fungsional dan kualitas (non-fungsional).
- Membagi Spesifikasi Desain menjadi area dan sub-area yang dapat diuji (jangan bingung dengan spesifikasi pengujian yang lebih rinci). Pastikan juga untuk mengidentifikasi dan menyertakan area yang akan dihilangkan (tidak diuji) juga.
- Mendefinisikan prosedur pelacakan bug.
- Mengidentifikasi risiko pengujian.
- Mengidentifikasi sumber daya yang diperlukan dan informasi terkait.
- Memberikan Jadwal Pengujian.

**2.1.2 Pengujian Kegunaan (Usability Testing)**

Tujuan dari pengujian kegunaan adalah untuk memastikan bahwa komponen dan fitur baru akan berfungsi dengan cara yang dapat diterima oleh pelanggan. Pengembangan biasanya akan membuat prototipe komponen UI yang tidak berfungsi untuk mengevaluasi desain yang diusulkan. Pengujian kegunaan dapat dikoordinasikan dengan pengujian, tetapi pengujian aktual harus dilakukan oleh non-penguji (sedekat mungkin dengan pengguna akhir). Pengujian akan meninjau temuan dan memberikan tim proyek evaluasinya tentang dampak perubahan ini terhadap proses pengujian dan proyek secara keseluruhan.

Untuk Airbnb, ini akan melibatkan pengujian intuitivitas navigasi, kejelasan informasi, kemudahan pemesanan, dan pengalaman pengguna secara keseluruhan.

**2.1.3 Pengujian Unit (Multiple)**

Pengujian Unit dilakukan oleh Pengembang selama proses pengembangan kode untuk memastikan bahwa fungsionalitas dan cakupan kode yang tepat telah dicapai oleh setiap pengembang baik selama pengkodean maupun dalam persiapan untuk penerimaan ke pengujian iterasi. Berikut ini adalah contoh area proyek yang harus diuji unit dan ditandatangani sebelum diteruskan ke Pengujian Regresi:

- Database, Stored Procedures, Triggers, Tables, dan Indexes.
- Layanan NT.
- Konversi database.
- .OCX, .DLL, .EXE dan executable format biner lainnya.

Untuk Airbnb, ini termasuk menguji fungsi, komponen, dan modul individual seperti:

- Modul otentikasi pengguna.
- Algoritma pencarian listing.
- Integrasi pemrosesan pembayaran.
- Validasi data pada formulir.

**2.1.4 Pengujian Iterasi/Regresi**

Selama siklus berulang mengidentifikasi bug dan menerima build baru (mengandung perubahan kode perbaikan bug), ada beberapa proses yang umum untuk fase ini di semua proyek. Ini termasuk berbagai jenis pengujian: fungsionalitas, kinerja, stres, konfigurasi, dll. Ada juga proses mengkomunikasikan hasil dari pengujian dan memastikan bahwa rilis/iterasi baru mengandung perbaikan yang stabil (regresi). Proyek harus merencanakan minimal 2-3 siklus pengujian (rilis/iterasi build baru). Pada setiap iterasi, harus diadakan debriefing. Secara khusus, laporan harus menunjukkan bahwa sejauh yang dapat dicapai selama fase pengujian iterasi, semua bug severity 1 dan severity 2 yang teridentifikasi telah dikomunikasikan dan ditangani. Minimal, semua bug priority 1 dan priority 2 harus diselesaikan sebelum memasuki fase beta.

Untuk Airbnb, ini akan melibatkan siklus pengujian berulang setelah fitur baru ditambahkan atau bug diperbaiki, memastikan fungsionalitas yang ada tetap utuh.

**2.1.5 Pengujian Rilis Final**

Tim penguji dengan pengguna akhir berpartisipasi dalam proses tonggak ini juga dengan memberikan umpan balik konfirmasi pada masalah baru yang ditemukan, dan masukan berdasarkan masalah yang identik atau serupa yang terdeteksi sebelumnya. Tujuannya adalah untuk memverifikasi bahwa produk siap untuk didistribusikan, dapat diterima oleh pelanggan dan menghilangkan masalah operasional potensial. Dengan asumsi bug kritis diselesaikan selama pengujian iterasi sebelumnya - Sepanjang siklus pengujian Rilis Final, perbaikan bug akan difokuskan pada bug minor dan trivial (severity 3 dan 4). Pengujian akan melanjutkan proses verifikasi stabilitas aplikasi melalui pengujian regresi (bug yang diketahui ada, serta kasus pengujian yang ada). Target tonggak dari fase ini adalah untuk menetapkan bahwa aplikasi yang diuji telah mencapai tingkat stabilitas, yang sesuai untuk penggunaannya (jumlah pengguna, dll.), sehingga dapat dirilis ke pengguna akhir dan komunitas caBIG.

Untuk Airbnb, fase ini akan memastikan aplikasi stabil dan siap untuk digunakan publik.

**2.1.6 Kriteria Kelengkapan Pengujian**

Rilis untuk produksi hanya dapat terjadi setelah keberhasilan penyelesaian aplikasi yang diuji melalui semua fase dan tonggak yang dibahas sebelumnya. Target tonggak adalah menempatkan rilis/aplikasi (build) ke produksi setelah ditunjukkan bahwa aplikasi telah mencapai tingkat stabilitas yang memenuhi atau melampaui harapan klien sebagaimana didefinisikan dalam Persyaratan, Spesifikasi Fungsional, dan Standar Produksi caBIG.

**2.2 Tingkat Pengujian**

Pengujian suatu aplikasi dapat dipecah menjadi tiga kategori utama dan beberapa sub-tingkat. Tiga kategori utama meliputi pengujian yang dilakukan setiap build (Pengujian Build), pengujian yang dilakukan setiap tonggak utama (Pengujian Tonggak), dan pengujian yang dilakukan setidaknya sekali setiap siklus rilis proyek (Pengujian Rilis). Kategori pengujian dan tingkat pengujian didefinisikan di bawah ini:

**2.2.1 Pengujian Build**

**2.2.1.1 Tingkat 1 - Pengujian Penerimaan Build**

Pengujian Penerimaan Build harus membutuhkan waktu kurang dari 2-3 jam untuk diselesaikan (15 menit adalah tipikal). Kasus pengujian ini hanya memastikan bahwa aplikasi dapat dibangun dan diinstal dengan sukses. Kasus pengujian terkait lainnya memastikan bahwa pengguna menerima Dokumen Rilis Pengembangan yang tepat ditambah informasi terkait build lainnya (titik rilis, dll.). Tujuannya adalah untuk menentukan apakah pengujian lebih lanjut dimungkinkan. Jika ada kasus pengujian Tingkat 1 yang gagal, build dikembalikan ke pengembang tanpa diuji.

Untuk Airbnb, ini akan melibatkan verifikasi keberhasilan _deployment_ ke lingkungan pengujian dan peluncuran aplikasi dasar.

**2.2.1.2 Tingkat 2 - Pengujian Asap (Smoke Tests)**

Pengujian Asap harus diotomatisasi dan membutuhkan waktu kurang dari 2-3 jam (20 menit adalah tipikal). Kasus pengujian ini memverifikasi fungsionalitas utama pada tingkat tinggi. Tujuannya adalah untuk menentukan apakah pengujian lebih lanjut dimungkinkan. Kasus pengujian ini harus menekankan cakupan daripada kedalaman. Semua komponen harus disentuh, dan setiap fitur utama harus diuji secara singkat oleh Pengujian Asap. Jika ada kasus pengujian Tingkat 2 yang gagal, build dikembalikan ke pengembang tanpa diuji.

Untuk Airbnb, ini meliputi pemeriksaan cepat fungsionalitas kritis seperti login pengguna, pencarian properti, dan melihat listing.

**2.2.1.3 Tingkat 2a - Pengujian Regresi Bug**

Setiap bug yang _Open_ selama build sebelumnya, tetapi ditandai sebagai _Fixed_, _Needs Re-Testing_ untuk build yang sedang diuji saat ini, perlu diregresi, atau diuji ulang. Setelah pengujian asap selesai, semua bug yang diselesaikan perlu diregresi. Dibutuhkan antara 5 menit hingga 1 jam untuk meregresi sebagian besar bug.

**2.2.2 Pengujian Tonggak (Milestone Tests)**

**2.2.2.1 Tingkat 3 - Pengujian Jalur Kritis (Critical Path Tests)**

Kasus pengujian Jalur Kritis ditargetkan pada fitur dan fungsionalitas yang akan dilihat dan digunakan pengguna setiap hari. Kasus pengujian Jalur Kritis harus lulus pada akhir setiap 2-3 Siklus Pengujian Build. Mereka tidak perlu diuji setiap rilis, tetapi harus diuji setidaknya sekali per tonggak. Dengan demikian, semua kasus pengujian Jalur Kritis harus dieksekusi setidaknya sekali selama siklus Iterasi, dan sekali selama siklus Rilis Final.

Untuk Airbnb, jalur kritis meliputi: pendaftaran pengguna yang berhasil, mencari dan memesan properti, dan host berhasil mendaftarkan properti.

**2.2.3 Pengujian Rilis**

**2.2.3.1 Tingkat 4 - Pengujian Standar**

Kasus Pengujian yang perlu dijalankan setidaknya sekali selama seluruh siklus pengujian untuk rilis ini. Kasus-kasus ini dijalankan sekali, tidak diulang seperti kasus pengujian di tingkat sebelumnya. Pengujian Fungsional dan Pengujian Desain Rinci (Kasus Pengujian Spesifikasi Fungsional dan Spesifikasi Desain, masing-masing). Ini dapat diuji beberapa kali untuk setiap Siklus Pengujian Tonggak (Iterasi, Rilis Final, dll.). Kasus pengujian standar biasanya meliputi Instalasi, Data, GUI, dan area pengujian lainnya.

Untuk Airbnb, ini mencakup komprehensif functional testing of all features, data integrity, dan GUI responsiveness.

**2.2.3.2 Tingkat 5 - Pengujian yang Disarankan**

Ini adalah Kasus Pengujian yang akan menyenangkan untuk dieksekusi, tetapi dapat dihilangkan karena kendala waktu. Sebagian besar Kasus Pengujian Kinerja dan Stres adalah contoh klasik dari kasus pengujian yang Disarankan (meskipun beberapa harus dianggap sebagai kasus pengujian standar). Contoh lain dari kasus pengujian yang disarankan meliputi WAN, LAN, Jaringan, dan pengujian Beban.

Untuk Airbnb, ini bisa mencakup pengujian kinerja ekstensif di bawah beban yang sangat tinggi, atau pengujian latensi jaringan untuk pengguna di berbagai lokasi geografis.

**2.3 Regresi Bug**

Regresi Bug akan menjadi bagian utama di seluruh fase pengujian. Semua bug yang diselesaikan sebagai _Fixed_, _Needs Re-Testing_ akan diregresi ketika tim Pengujian diberitahu tentang rilis baru yang berisi perbaikan. Ketika sebuah bug lulus regresi, itu akan dianggap _Closed, Fixed_. Jika sebuah bug gagal regresi, tim pengujian pengguna akan memberitahu tim pengembangan dengan memasukkan catatan ke [Alat pelacakan bug pilihan Anda]. Ketika bug Severity 1 gagal regresi, tim Pengujian pengguna juga harus segera mengirim email ke pengembangan. Pemimpin Pengujian akan bertanggung jawab untuk melacak dan melaporkan kepada pengembangan dan manajemen produk status pengujian regresi.

**2.4 Triage Bug**

Triage Bug akan diadakan di seluruh fase siklus pengembangan. Triage Bug akan menjadi tanggung jawab Pemimpin Pengujian. Triage akan diadakan secara teratur dengan kerangka waktu yang ditentukan oleh tingkat penemuan bug dan jadwal proyek. Dengan demikian, akan menjadi tipikal untuk mengadakan beberapa triage selama fase Perencanaan, kemudian mungkin satu triage per minggu selama fase Desain, meningkat menjadi dua kali per minggu selama tahap akhir fase Pengembangan. Kemudian, fase Stabilisasi harus melihat pengurangan substansial dalam jumlah bug baru yang ditemukan, sehingga beberapa triage per minggu akan menjadi maksimum (untuk menangani status bug yang ada). Pemimpin Pengujian, Manajer Produk, dan Pemimpin Pengembangan harus terlibat dalam rapat triage ini. Pemimpin Pengujian akan menyediakan dokumentasi dan laporan yang diperlukan tentang bug untuk semua peserta. Tujuan dari triage adalah untuk menentukan jenis resolusi untuk setiap bug dan untuk memprioritaskan serta menentukan jadwal untuk semua Bug yang Akan Diperbaiki. Pengembangan kemudian akan menugaskan bug kepada orang yang tepat untuk perbaikan dan melaporkan resolusi setiap bug kembali ke sistem pelacak bug [Alat pelacakan bug pilihan Anda]. Pemimpin Pengujian akan bertanggung jawab untuk melacak dan melaporkan status semua resolusi bug.

**2.5 Kriteria Penangguhan dan Persyaratan Lanjutan**

Bagian ini harus didefinisikan untuk mencantumkan kriteria dan persyaratan lanjutan jika tingkat tertentu dan tingkat tujuan pengujian yang telah ditentukan tidak terpenuhi.

- Pengujian akan ditangguhkan pada modul perangkat lunak yang terpengaruh ketika bug kasus pengujian Asap (Tingkat 1) atau Jalur Kritis (Tingkat 2) ditemukan setelah iterasi ke-3.
- Pengujian akan ditangguhkan jika ada perubahan lingkup kritis yang memengaruhi Jalur Kritis.

Laporan bug harus diajukan oleh tim Pengembangan. Setelah memperbaiki bug, tim Pengembangan akan mengikuti kriteria rilis (dijelaskan di atas) untuk menyediakan rilis terbaru untuk Pengujian tambahan. Pada saat itu, pengguna akan meregresi bug, dan jika lulus, melanjutkan pengujian modul.

**2.6 Kelengkapan Pengujian**

Pengujian akan dianggap selesai ketika kondisi berikut telah terpenuhi:

**2.6.1 Kondisi Standar:**

- Ketika Pengguna dan Pengembang, setuju bahwa pengujian telah selesai, aplikasi stabil, dan setuju bahwa aplikasi memenuhi persyaratan fungsional.
- Eksekusi skrip dari semua kasus pengujian di semua area telah lulus.
- Kasus pengujian otomatis di semua area telah lulus.
- Semua bug prioritas 1 dan 2 telah diselesaikan dan ditutup.
- [Stakeholder/Client Name] menyetujui penyelesaian pengujian.
- Setiap area pengujian telah ditandatangani sebagai selesai oleh Pemimpin Pengujian.
- 50% dari semua bug severity 1 dan 2 yang diselesaikan telah berhasil diregresi ulang sebagai validasi akhir.
- Pengujian ad hoc di semua area telah selesai.

**2.6.2 Kondisi Pelaporan & Triage Bug:**

- Tingkat penemuan bug menunjukkan tren menurun sebelum Tingkat Bug Nol (tidak ada bug Sev. 1/2/3 baru yang ditemukan).
- Tingkat penemuan bug tetap 0 bug baru yang ditemukan (Severity 1/2/3) meskipun ada upaya pengujian konstan selama 3 hari atau lebih.
- Distribusi tingkat keparahan bug telah berubah menjadi penurunan yang stabil dalam bug Sev. 1 dan 2 yang ditemukan.
- Tidak ada bug _Must Fix_ yang tersisa meskipun pengujian berkelanjutan.

**3. Hasil Pengujian (Test Deliverables)**

Pengujian akan memberikan hasil spesifik selama proyek. Hasil ini terbagi dalam tiga kategori dasar: Dokumen, Kasus Pengujian / Penulisan Bug, dan Laporan.

**3.1 Matriks Hasil**

Di bawah ini adalah daftar artefak yang digerakkan oleh proses dan harus diproduksi selama siklus hidup pengujian. Hasil tertentu harus disampaikan sebagai bagian dari validasi pengujian, Anda dapat menambahkan ke daftar hasil di bawah ini yang mendukung tujuan keseluruhan dan untuk menjaga kualitas. Matriks ini harus diperbarui secara rutin sepanjang siklus pengembangan proyek dalam Rencana Pengujian spesifik proyek Anda.

| Hasil                                                             | Kategori                        |
| ----------------------------------------------------------------- | ------------------------------- |
| Dokumen Pendekatan Pengujian                                      | Dokumen                         |
| Rencana Pengujian                                                 | Dokumen                         |
| Jadwal Pengujian                                                  | Dokumen                         |
| Spesifikasi Pengujian                                             | Dokumen                         |
| Matriks Ketertelusuran Persyaratan                                | Dokumen                         |
| Kasus Pengujian / Hasil                                           | Penulisan Kasus Pengujian / Bug |
| Laporan Cakupan Pengujian                                         | Penulisan Kasus Pengujian / Bug |
| Pelacak bug [Alat pelacakan bug pilihan Anda] untuk pelaporan bug | Penulisan Kasus Pengujian / Bug |
| Laporan hasil pengujian                                           | Laporan                         |
| Laporan Akhir Pengujian - Penandatanganan                         | Laporan                         |

**3.2 Dokumen**

**3.2.1 Dokumen Pendekatan Pengujian**

Dokumen Pendekatan Pengujian berasal dari Dokumen Rencana Proyek, Persyaratan, dan Spesifikasi Fungsional. Dokumen ini mendefinisikan pendekatan pengujian keseluruhan yang akan diambil untuk proyek tersebut. Dokumen Pendekatan Pengujian Standar yang sedang Anda baca ini adalah _boilerplate_ dari mana dokumen Pendekatan Pengujian proyek yang lebih spesifik dapat diambil.

Setelah dokumen ini selesai, Pemimpin Pengujian akan mendistribusikannya kepada Manajer Produk, Pemimpin Pengembangan, Perwakilan Pengguna, Manajer Program, dan pihak lain yang diperlukan untuk peninjauan dan penandatanganan.

**3.2.2 Rencana Pengujian**

Rencana Pengujian berasal dari Pendekatan Pengujian, Persyaratan, Spesifikasi Fungsional, dan Spesifikasi Desain terperinci. Rencana Pengujian mengidentifikasi detail pendekatan pengujian, mengidentifikasi area kasus pengujian terkait dalam produk spesifik untuk siklus rilis ini. Tujuan dari dokumen Rencana Pengujian adalah untuk:

- Menentukan pendekatan yang akan digunakan Pengujian untuk menguji produk, dan hasil (diekstrak dari Pendekatan Pengujian).
- Membagi produk menjadi area-area yang berbeda dan mengidentifikasi fitur-fitur produk yang akan diuji.
- Menentukan prosedur yang akan digunakan untuk penandatanganan pengujian dan rilis produk.
- Menunjukkan alat yang digunakan untuk menguji produk.
- Mencantumkan rencana sumber daya dan penjadwalan.
- Menunjukkan orang yang dapat dihubungi yang bertanggung jawab atas berbagai area proyek.
- Mengidentifikasi risiko dan rencana kontingensi yang mungkin memengaruhi pengujian produk.
- Menentukan prosedur manajemen bug untuk proyek.
- Menentukan kriteria untuk penerimaan rilis pengembangan ke pengujian (build).

**3.2.3 Jadwal Pengujian**

Bagian ini tidak vital untuk dokumen secara keseluruhan dan dapat dimodifikasi atau dihapus jika diperlukan oleh penulis. Jadwal Pengujian adalah tanggung jawab Pemimpin Pengujian (atau Penjadwal Departemen, jika ada) dan akan didasarkan pada informasi dari Penjadwal Proyek (dilakukan oleh Manajer Produk). Jadwal Pengujian spesifik proyek dapat dilakukan di MS Project atau alat manajemen proyek lainnya seperti Jira/Asana.

**3.2.4 Spesifikasi Pengujian**

Dokumen Spesifikasi Pengujian berasal dari Rencana Pengujian serta dokumen Persyaratan, Spesifikasi Fungsional, dan Spesifikasi Desain. Dokumen ini menyediakan spesifikasi untuk konstruksi Kasus Pengujian dan mencakup daftar area kasus pengujian dan tujuan pengujian untuk setiap komponen yang akan diuji sebagaimana diidentifikasi dalam Rencana Pengujian proyek.

**3.2.5 Matriks Ketertelusuran Persyaratan (Requirements Traceability Matrix)**

Matriks Ketertelusuran Persyaratan (RTM) yang digunakan untuk menghubungkan skenario pengujian dengan persyaratan dan kasus penggunaan adalah bagian yang wajib dari dokumentasi Rencana Pengujian untuk semua proyek. Ketertelusuran persyaratan didefinisikan sebagai kemampuan untuk menjelaskan dan mengikuti kehidupan suatu persyaratan, baik dalam arah maju maupun mundur (yaitu dari asalnya, melalui pengembangan dan spesifikasinya, hingga penyebaran dan penggunaannya, dan melalui periode penyempurnaan dan iterasi berkelanjutan dalam fase mana pun dari ini). Yang penting adalah memilih template atau dasar dokumen yang mencapai ketertelusuran menyeluruh sepanjang masa proyek.

**3.3 Pelacakan Cacat & Debugging**

**3.3.1 Alur Kerja Pengujian**

Alur kerja di bawah ini menggambarkan proses alur kerja pengujian untuk Pengembang dan Pengguna untuk pengujian Penerimaan Pengguna dan End-to-End. Harap dicatat proses yang disorot kuning di mana Pengguna diminta untuk langsung mengirim daftar cacat dengan bukti kepada Pengembang. Demikian pula, Pengembang diminta untuk mengkonfirmasi langsung dengan Pengguna setelah perbaikan bug bersama dengan pembaruan di Bugzilla.

_(Diagram alur kerja akan disisipkan di sini, disesuaikan dengan alat yang digunakan, mis. Jira/GitHub Issues/alat internal)_

**3.3.2 Pelaporan Cacat menggunakan [Alat pelacakan bug pilihan Anda]**

SEMUA cacat harus dicatat menggunakan [Alat pelacakan bug pilihan Anda], untuk menangani dan melakukan debugging cacat. Pengguna juga diminta untuk mengirim laporan cacat harian kepada pengembang. Pengembang akan memperbarui daftar cacat di [Alat pelacakan bug pilihan Anda] dan memberitahu pemohon setelah cacat telah diselesaikan. Pengembang dan Pengguna diminta untuk meminta akun di [Alat pelacakan bug pilihan Anda] untuk ruang kerja relatif.

Debugging harus didasarkan pada Prioritas Tinggi > Sedang > Rendah, prioritas ini ditetapkan oleh Pengguna dan didasarkan pada seberapa kritis skrip pengujian dalam hal ketergantungan dan terutama didasarkan pada skenario kasus penggunaan.

- Semua cacat prioritas Tinggi harus ditangani dalam 1 hari setelah permintaan dan diselesaikan/ditutup dalam 2 hari setelah permintaan awal.
- Semua cacat prioritas Sedang harus ditangani dalam 2 hari setelah permintaan dan diselesaikan/ditutup dalam 4 hari setelah permintaan awal.
- Semua cacat prioritas Rendah harus diselesaikan/ditutup paling lambat 5 hari setelah permintaan awal.

**Contoh Bidang untuk Pelaporan Cacat (diadaptasi dari template):**

| Bidang            | Komentar                                                                                                                                                                                                            |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Perangkat Keras   | Cantumkan perangkat keras lingkungan pengujian. mis. PC, MAC, Mobile Device (Android/iOS).                                                                                                                          |
| Produk            | Airbnb Web Application.                                                                                                                                                                                             |
| Sistem Operasi    | Win 10, macOS, Linux, Android, iOS.                                                                                                                                                                                 |
| Versi             | Versi aplikasi.                                                                                                                                                                                                     |
| Tingkat Keparahan | Jika itu adalah peningkatan atau bug dengan tingkat keparahan minor hingga mayor yang mungkin tidak mengganggu pengujian lebih lanjut atau sepenuhnya menghalangi upaya pengujian di masa mendatang. (Lihat 4.3.1). |
| Resolusi          | Hanya PENGEMBANG yang akan memperbarui berdasarkan cacat.                                                                                                                                                           |
| Modul             | Untuk aplikasi dengan beberapa modul, pilih modul yang sesuai untuk cacat yang dilaporkan. (misalnya, User Management, Listing Search, Booking Flow, Payment Gateway).                                              |
| URL               | Tambahkan URL jika ada (misalnya, URL tempat bug terjadi).                                                                                                                                                          |
| Ditugaskan kepada | Akan diperbarui oleh Pengembang, kepada siapa tiket ditugaskan.                                                                                                                                                     |
| Prioritas         | Tetapkan prioritas berdasarkan tingkat keparahan. (Lihat 4.3.2).                                                                                                                                                    |
| Ringkasan         | Ringkasan cacat, bug, atau masalah.                                                                                                                                                                                 |
| Deskripsi Rinci.  | Detail cacat, bug, atau masalah (langkah-langkah untuk mereproduksi, hasil aktual, hasil yang diharapkan).                                                                                                          |
| Unggah file       | Lampirkan file bukti.                                                                                                                                                                                               |
| Kirim             | Kirim tiket bug.                                                                                                                                                                                                    |

**3.4 Laporan**

Pemimpin Pengujian akan bertanggung jawab untuk menulis dan mendistribusikan laporan berikut kepada personel proyek yang sesuai sesuai kebutuhan.

**3.4.1 Laporan status pengujian**

Laporan status mingguan atau dua mingguan akan diberikan oleh Pemimpin Pengujian kepada personel proyek. Laporan ini akan merangkum kegiatan pengujian mingguan, masalah, risiko, jumlah bug, cakupan kasus pengujian, dan metrik relevan lainnya.

**3.4.2 Laporan Penyelesaian Tahap**

Ketika setiap fase pengujian selesai, Pemimpin Pengujian akan mendistribusikan Laporan Penyelesaian Tahap kepada Manajer Produk, Pemimpin Pengembangan, dan Manajer Program untuk peninjauan dan penandatanganan. Poin-poin di bawah ini mengilustrasikan contoh apa yang mungkin termasuk dalam dokumen tersebut. Dokumen tersebut harus berisi metrik berikut:

- Total Kasus Pengujian, Jumlah yang Dieksekusi, Jumlah Lulus / Gagal, Jumlah yang Belum Dieksekusi.
- Jumlah Bug yang Ditemukan Hingga Saat Ini, Jumlah yang Diselesaikan, dan Jumlah yang Masih Terbuka.
- Rincian Bug berdasarkan Matriks Tingkat Keparahan / Prioritas.
- Diskusi Risiko yang Belum Terselesaikan.
- Diskusi Kemajuan Jadwal (apakah kita berada di tempat yang seharusnya?).

**3.4.3 Laporan Akhir Pengujian - Penandatanganan**

Laporan Pengujian Akhir akan dikeluarkan oleh Pemimpin Pengujian. Ini akan menyatakan sejauh mana pengujian sebenarnya telah selesai (disarankan laporan cakupan kasus pengujian), dan penilaian kesiapan produk untuk Dirilis ke Produksi.

**3.5 Matriks Tanggung Jawab**

Sisipkan matriks sumber daya pengujian siapa yang terlibat dan apa perannya.

| Peran            | Tanggung Jawab (Fase Pengujian)                                                                       |
| ---------------- | ----------------------------------------------------------------------------------------------------- |
| Test Lead        | Mengawasi seluruh proses pengujian, mengelola tim pengujian, melaporkan status, melakukan triage bug. |
| QA Tester        | Mengeksekusi kasus pengujian, melaporkan cacat, melakukan pengujian regresi.                          |
| Developer        | Memperbaiki bug, melakukan pengujian unit dan integrasi, menyediakan build baru.                      |
| Product Manager  | Mendefinisikan persyaratan, berpartisipasi dalam triage bug, memberikan persetujuan.                  |
| Business Analyst | Mengklarifikasi persyaratan, menyediakan skenario kasus penggunaan.                                   |
| UI/UX Designer   | Meninjau temuan pengujian kegunaan.                                                                   |

**4. Kebutuhan Sumber Daya & Lingkungan**

**4.1 Alat Pengujian**

**4.1.1 Alat Pelacakan**

[Alat pelacakan bug pilihan Anda, mis. Jira] bug tracker digunakan oleh [Organisasi Anda] untuk memasukkan dan melacak semua bug dan masalah proyek. Pemimpin Pengujian bertanggung jawab untuk memelihara database [Alat pelacakan bug pilihan Anda].

- **Pelacakan Bug**: Jira, Asana, Trello, atau yang serupa.
- **Manajemen Kasus Pengujian**: TestRail, Zephyr, qTest, atau terintegrasi dengan alat pelacakan bug.
- **Alat Otomatisasi**: Selenium WebDriver, Cypress, Playwright (untuk otomatisasi UI web).
- **Alat Pengujian Kinerja**: JMeter, LoadRunner, k6.
- **Alat Pengujian Keamanan**: OWASP ZAP, Burp Suite.
- **Alat Komunikasi**: Slack, Microsoft Teams.

**4.1.1.1 Manajemen Konfigurasi**

Harap sertakan rencana manajemen konfigurasi Anda.

- Sistem kontrol versi untuk artefak pengujian (misalnya, Git).
- Proses untuk mengelola berbagai versi aplikasi yang diuji.
- Manajemen konfigurasi lingkungan (misalnya, menggunakan Docker atau virtualisasi).

**4.2 Lingkungan Pengujian**

**4.2.1 Perangkat Keras**

Sertakan persyaratan perangkat keras minimum yang akan digunakan untuk menguji Aplikasi. Pengujian akan memiliki kontrol akses ke satu atau lebih server aplikasi/database yang terpisah dari yang digunakan oleh anggota tim proyek non-pengujian. Pengujian juga akan memiliki kontrol akses ke sejumlah _workstation_ PC yang dikonfigurasi secara bervariasi untuk memastikan pengujian dari berbagai konfigurasi perangkat keras klien minimum hingga yang direkomendasikan yang tercantum dalam dokumen Persyaratan, Spesifikasi Fungsional, dan Spesifikasi Desain proyek.

Untuk Airbnb, ini meliputi:

- **Test Servers**: Dedicated application and database servers for testing, separate from development and production environments.
- **Client Workstations**: Various configurations of PCs, Macs, and mobile devices (actual or emulated) to test responsiveness and compatibility.

**4.2.2 Perangkat Lunak**

Selain aplikasi dan perangkat lunak lain yang ditentukan pelanggan, daftar perangkat lunak berikut harus dianggap sebagai minimum:

- **Sistem Operasi**: Windows 10, macOS Ventura/Sonoma, berbagai distribusi Linux.
- **Peramban Web (Web Browsers)**: Versi terbaru Chrome, Firefox, Edge, Safari (on macOS/iOS).
- **Development Tools (for Developers)**: IDEs, version control clients.
- **Other**: VPN client (if test environment is restricted), specific browser plugins/extensions if required for testing.

**4.3 Definisi Tingkat Keparahan dan Prioritas Bug**

Bidang Tingkat Keparahan dan Prioritas Bug keduanya sangat penting untuk mengkategorikan bug dan memprioritaskan apakah dan kapan bug akan diperbaiki. Tingkat Tingkat Keparahan dan Prioritas bug akan didefinisikan sebagaimana diuraikan dalam tabel berikut di bawah ini. Pengujian akan menetapkan tingkat keparahan untuk semua bug. Pemimpin Pengujian akan bertanggung jawab untuk memastikan bahwa tingkat keparahan yang benar ditetapkan untuk setiap bug. Pemimpin Pengujian, Pemimpin Pengembangan, dan Manajer Program akan berpartisipasi dalam rapat tinjauan bug untuk menetapkan prioritas semua bug yang saat ini aktif. Rapat ini akan dikenal sebagai Rapat Triage Bug. Pemimpin Pengujian bertanggung jawab untuk mengatur rapat-rapat ini secara rutin untuk menangani kumpulan bug baru dan yang ada tetapi belum terselesaikan saat ini.

**4.3.1 Daftar Tingkat Keparahan**

Penguji yang memasukkan bug ke [Alat pelacakan bug pilihan Anda] juga bertanggung jawab untuk memasukkan Tingkat Keparahan bug.

| ID Tingkat Keparahan | Tingkat Keparahan | Deskripsi Tingkat Keparahan                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| -------------------- | ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1                    | Kritis            | Modul/produk _crash_ atau bug menyebabkan kondisi yang tidak dapat dipulihkan. Sistem _crash_, _GP Faults_, atau korupsi database atau file, atau potensi kehilangan data, program _hang_ yang membutuhkan _reboot_ adalah semua contoh bug Sev. 1. Untuk Airbnb: Aplikasi tidak responsif, ketidakmampuan untuk menyelesaikan pemesanan, kehilangan data pengguna/listing.                                                                                                                                                                                            |
| 2                    | Tinggi            | Komponen sistem utama tidak dapat digunakan karena kegagalan atau fungsionalitas yang salah. Bug Sev. 2 menyebabkan masalah serius seperti kurangnya fungsionalitas, atau pesan kesalahan yang tidak memadai atau tidak jelas yang dapat berdampak besar pada pengguna, mencegah area lain dari aplikasi untuk diuji, dll.. Bug Sev. 2 dapat memiliki _workaround_, tetapi _workaround_ tersebut tidak nyaman atau sulit. Untuk Airbnb: Pencarian tidak mengembalikan hasil, kesalahan _gateway_ pembayaran yang mencegah transaksi, host tidak dapat membuat listing. |
| 3                    | Sedang            | Fungsionalitas komponen atau proses yang salah. Ada _workaround_ sederhana untuk bug jika itu Sev. 3. Untuk Airbnb: Masalah tampilan minor, pesan kesalahan yang salah yang tidak menghalangi fungsionalitas, masalah paginasi.                                                                                                                                                                                                                                                                                                                                        |
| 4                    | Minor             | Kesalahan dokumentasi atau bug severity 3 yang ditandatangani. Untuk Airbnb: Kesalahan ketik, ketidaksejajaran UI minor, masalah estetika yang tidak memengaruhi fungsionalitas.                                                                                                                                                                                                                                                                                                                                                                                       |

**4.3.2 Daftar Prioritas**

| ID Prioritas | Tingkat Prioritas                            | Deskripsi Prioritas                                                                                                     |
| ------------ | -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| 5            | Harus Diperbaiki (Must Fix)                  | Bug ini harus segera diperbaiki; produk tidak dapat dirilis dengan bug ini.                                             |
| 4            | Seharusnya Diperbaiki (Should Fix)           | Ini adalah masalah penting yang harus diperbaiki sesegera mungkin. Akan memalukan bagi perusahaan jika bug ini dirilis. |
| 3            | Perbaiki Saat Ada Waktu (Fix When Have Time) | Masalah harus diperbaiki dalam waktu yang tersedia. Jika bug tidak menunda tanggal rilis, maka perbaiki.                |
| 2            | Prioritas Rendah (Low Priority)              | Tidak penting (saat ini) bahwa bug ini ditangani. Perbaiki bug ini setelah semua bug lain diperbaiki.                   |
| 1            | Trivial                                      | Peningkatan/Fitur yang bagus untuk dimiliki yang hanya di luar lingkup saat ini.                                        |

**4.4 Pelaporan Bug**

Tim pengujian mengakui bahwa proses pelaporan bug adalah alat komunikasi kritis dalam proses pengujian. Tanpa komunikasi informasi bug dan masalah lainnya yang efektif, proses pengembangan dan rilis akan terpengaruh secara negatif. Pemimpin Pengujian akan bertanggung jawab untuk mengelola proses pelaporan bug. Alat dan proses pelaporan bug standar pengujian akan digunakan. [Alat pelacakan bug pilihan Anda] adalah alat Pencatat / Pelacak Bug standar perusahaan. Pengujian dan pengembangan akan memasukkan data mereka ke dalam database [Alat pelacakan bug pilihan Anda] mengikuti definisi entri bidang yang didefinisikan di bawah ini.

**5. Istilah/Singkatan**

Istilah di bawah ini digunakan sebagai contoh, harap tambahkan/hapus istilah yang relevan dengan dokumen.

| ISTILAH/SINGKATAN | DEFINISI                                                                                                                                                                                                                        |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| API               | Antarmuka Pemrograman Aplikasi (Application Program Interface)                                                                                                                                                                  |
| UAT               | Pengujian Penerimaan Pengguna (User Acceptance Testing)                                                                                                                                                                         |
| UI                | Antarmuka Pengguna (User Interface)                                                                                                                                                                                             |
| UX                | Pengalaman Pengguna (User Experience)                                                                                                                                                                                           |
| E2E               | Pengujian End-to-End: Menguji skenario pengguna dan berbagai kondisi jalur dengan memverifikasi bahwa sistem berjalan dan melakukan tugas secara akurat dengan set data yang sama dari awal hingga akhir, sebagaimana dimaksud. |
| N/A               | Tidak Berlaku (Not Applicable)                                                                                                                                                                                                  |
| QA                | Jaminan Kualitas (Quality Assurance)                                                                                                                                                                                            |
| RTM               | Matriks Ketertelusuran Persyaratan (Requirements Traceability Matrix)                                                                                                                                                           |
| SME               | Ahli Subjek (Subject Matter Expert)                                                                                                                                                                                             |
| SOP               | Prosedur Operasi Standar (Standard Operating Procedure)                                                                                                                                                                         |
| TBD               | Akan Ditentukan (To Be Determined)                                                                                                                                                                                              |
| SQL               | Bahasa Kueri Terstruktur (Structured Query Language)                                                                                                                                                                            |
| HTTP/HTTPS        | Protokol Transfer Hiperteks / Protokol Transfer Hiperteks Aman                                                                                                                                                                  |
| SEO               | Optimasi Mesin Pencari (Search Engine Optimization)                                                                                                                                                                             |
| PWA               | Aplikasi Web Progresif (Progressive Web Application)                                                                                                                                                                            |
| CSRF              | Pemalsuan Permintaan Lintas Situs (Cross-Site Request Forgery)                                                                                                                                                                  |
| XSS               | Skrip Lintas Situs (Cross-Site Scripting)                                                                                                                                                                                       |
