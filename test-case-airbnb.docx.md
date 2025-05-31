

**Test Case**  
Airbnb 25.22  
Kelompok F4

| Owner | : Airbnb Inc |
| :---- | :---- |
| Scope | : To validate known functions of the features. |
| Originator | :  |
| Status | : Draft/In Process/Approved |
| Document ID | : TCE001 |
| Location | : San Francisco, California, United States |

**Daftar Isi**

**[1\. Introduction	4](#introduction)**

[**2\. Scope	4**](#scope)

[**3\. Related Document	4**](#related-document)

[**4\. Traceability Matrix	5**](#traceability-matrix)

[**5\. Test Cases	6**](#test-cases)

[5.1 Pencarian dan Penemuan Properti (Search & Discovery)	6](#pencarian-dan-penemuan-properti-\(search-&-discovery\))

[5.1.1 Test Item: Pencarian properti berdasarkan lokasi	6](#test-item:-pencarian-properti-berdasarkan-lokasi)

[5.1.2 Test Item: Pencarian properti dengan filter tanggal	7](#test-item:-pencarian-properti-dengan-filter-tanggal)

[5.1.3 Test Item: Pencarian properti dengan filter jumlah dan jenis tamu	9](#test-item:-pencarian-properti-dengan-filter-jumlah-dan-jenis-tamu)

[5.1.4 Test Item: Pencarian properti dengan filter jenis properti	10](#test-item:-pencarian-properti-dengan-filter-jenis-properti)

[5.1.5 Test Item: Pencarian properti dengan filter rentang harga	11](#test-item:-pencarian-properti-dengan-filter-rentang-harga)

[5.1.6 Test Item: Pencarian properti dengan filter fasilitas	12](#test-item:-pencarian-properti-dengan-filter-fasilitas)

[5.1.7 Test Item: Pencarian properti dengan filter karakteristik khusus tambahan	13](#test-item:-pencarian-properti-dengan-filter-karakteristik-khusus-tambahan)

[5.1.8 Test Item: Pencarian properti dengan filter jumlah kamar tidur dan kamar mandi	14](#test-item:-pencarian-properti-dengan-filter-jumlah-kamar-tidur-dan-kamar-mandi)

[5.1.9 Test Item: Pencarian properti dalam bentuk daftar	15](#test-item:-pencarian-properti-dalam-bentuk-daftar)

[5.1.10 Test Item: Penampilan informasi pencarian ringkas	15](#test-item:-penampilan-informasi-pencarian-ringkas)

[5.1.11 Test Item: Daftar keinginan pengguna	16](#test-item:-daftar-keinginan-pengguna)

[5.2 User Management	19](#user-management)

[5.2.1 Test Item: Pendaftaran akun	19](#test-item:-pendaftaran-akun)

[5.2.2 Test Item: Masuk akun	21](#test-item:-masuk-akun)

[5.2.3 Test Item: Lupa kata sandi	22](#test-item:-lupa-kata-sandi)

[5.2.4 Test Item: Pengeditan profil	23](#test-item:-pengeditan-profil)

[5.2.5 Test Item: Pengelolaan metode pembayaran	25](#test-item:-pengelolaan-metode-pembayaran)

[5.2.6 Test Item: Riwayat pemesanan pengguna	27](#test-item:-riwayat-pemesanan-pengguna)

[5.2.7 Test Item: Pengelolaan notifikasi	28](#test-item:-pengelolaan-notifikasi)

[5.3 Detail Properti	29](#detail-properti)

[5.3.1 Test Item: Penampilan galeri foto properti	29](#test-item:-penampilan-galeri-foto-properti)

[5.3.2 Test Item: Penampilan deskripsi lengkap properti	30](#test-item:-penampilan-deskripsi-lengkap-properti)

[5.3.3 Test Item: Penampilan detail spesifik properti	31](#test-item:-penampilan-detail-spesifik-properti)

[5.3.4 Test Item: Penampilan daftar fasilitas	32](#test-item:-penampilan-daftar-fasilitas)

[5.3.5 Test Item: Penampilan kalender ketersediaan	33](#test-item:-penampilan-kalender-ketersediaan)

[5.3.6 Test Item: Penampilan total harga	34](#test-item:-penampilan-total-harga)

[5.3.7 Test Item: Penampilan aturan rumah	35](#test-item:-penampilan-aturan-rumah)

[5.3.8 Test Item: Penampilan kebijakan pembatalan properti	36](#test-item:-penampilan-kebijakan-pembatalan-properti)

[5.3.9 Test Item: Penampilan lokasi properti di peta	37](#test-item:-penampilan-lokasi-properti-di-peta)

[5.3.10 Test Item: Penampilan informasi profil tuan rumah	38](#test-item:-penampilan-informasi-profil-tuan-rumah)

[5.3.11 Test Item: Penampilan semua ulasan properti	38](#test-item:-penampilan-semua-ulasan-properti)

[5.4 Review dan Rating	40](#review-dan-rating)

[5.4.1 Test Item: Pemberian ulasan dan rating tamu	40](#test-item:-pemberian-ulasan-dan-rating-tamu)

[5.4.2 Test Item: Pemberian ulasan dan rating tamu host	41](#test-item:-pemberian-ulasan-dan-rating-tamu-host)

[5.4.3 Test Item: Publikasi ulasan dan rating	42](#test-item:-publikasi-ulasan-dan-rating)

[5.5 Customer Support	43](#customer-support)

[5.5.1 Test Item: Pusat bantuan/FAQ	43](#test-item:-pusat-bantuan/faq)

**Airbnb Test Case**

1. # **Introduction** {#introduction}

   Tujuan dari dokumen *Test Case* ini adalah guna menentukan dan mengomunikasikan kondisi spesifik yang perlu divalidasi untuk memungkinkan penilaian sistem. *Test Case* didasari oleh banyak hal tetapi mostly mencakup *Use Case*, *performance characteristics*, dan risiko yang menjadi perhatian proyek.

2. # **Scope** {#scope}

   Pengujian ditujukan untuk memverifikasi bahwa fitur-fitur pada website Airbnb bekerja dengan sesuai. Fitur-fitur pada website Airbnb yang akan dites adalah:

1. Pencarian dan Penemuan Properti (Search & Discovery)  
2. User Management  
3. Detail Properti  
4. Review dan Rating  
5. Customer Support

3. # **Related Document** {#related-document}

   Adapun dokumen terkait *Test Case* ini tertera pada tabel berikut.

   Tabel 1\. Related Document

| Document | Location |
| ----- | ----- |
| Test Strategy | main/Test Strategy.docs |
| Test Plan | main/ |
| Test Scenario | main/test-scenario-airbnb |
| Kebutuhan Fungsional dan non Fungsional aplikasi | main/kebutuhan-aplikasi-airbnb |

4. # **Traceability Matrix** {#traceability-matrix}

   Tabel berikut menjelaskan pemetaan hubungan antara persyaratan dari dokumen spesifikasi persyaratan dan item pengujian terkait.

   Tabel 2\. Tracebility Matrix

| Requirement | Validated by |
| ----- | ----- |
| FR-CP01 | Test item 5.1.1 |
| FR-CP02 | Test item 5.1.2 |
| FR-CP03 | Test item 5.1.3 |
| FR-CP04 | Test item 5.1.4 |
| FR-CP05 | Test item 5.1.5 |
| FR-CP06 | Test item 5.1.6 |
| FR-CP07 | Test item 5.1.7 |
| FR-CP08 | Test item 5.1.8 |
| FR-CP09 | Test item 5.1.9 |
| FR-CP10 | Test item 5.1.10 |
| FR-CP11 | Test item 5.1.11 |
| FR-USR01 | Test item 5.2.1 |
| FR-USR02 | Test item 5.2.2 |
| FR-USR03 | Test item 5.2.3 |
| FR-USR04 | Test item 5.2.4 |
| FR-USR05 | Test item 5.2.5 |
| FR-USR06 | Test item 5.2.6 |
| FR-USR07 | Test item 5.2.7 |
| FR-DP01 | Test item 5.3.1 |
| FR-DP02 | Test item 5.3.2 |
| FR-DP03 | Test item 5.3.3 |
| FR-DP04 | Test item 5.3.4 |
| FR-DP05 | Test item 5.3.5 |
| FR-DP06 | Test item 5.3.6 |
| FR-DP07 | Test item 5.3.7 |
| FR-DP08 | Test item 5.3.8 |
| FR-DP09 | Test item 5.3.9 |
| FR-DP10 | Test item 5.3.10 |
| FR-DP11 | Test item 5.3.11 |
| FR-RR01 | Test item 5.4.1 |
| FR-RR02 | Test item 5.4.2 |
| FR-RR03 | Test item 5.4.3 |
| FR-CS01 | Test item 5.5.1 |
| FR-CS02 |  |
| FR-CS03 |  |

5. # **Test Cases** {#test-cases}

   1. ## **Pencarian dan Penemuan Properti (Search & Discovery)** {#pencarian-dan-penemuan-properti-(search-&-discovery)}

      1. ### ***Test Item: Pencarian properti berdasarkan lokasi*** {#test-item:-pencarian-properti-berdasarkan-lokasi}

   Scope: Sistem harus memungkinkan pengguna untuk mencari properti berdasarkan lokasi (kota, negara bagian, negara, alamat spesifik, atau penunjuk di peta).

   Scenario: Pencarian Properti Berdasarkan Lokasi

   

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result | Automated | Note |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | :---: | ----- |
| Test Item: Pencarian properti berdasarkan lokasi |  |  |  |  |  |  |  |  |
| TC-CP-A-01 | Pencarian properti dengan nama kota yang valid. | 1\. Buka halaman utama Airbnb. 2\. Masukkan "Kyoto" di kolom "Ke mana?" 3\. Klik tombol "Cari". | Sistem menampilkan daftar properti yang tersedia di Kyoto. |  |  |  | FALSE |  |
| TC-CP-A-02 | Pencarian properti dengan nama negara yang valid. | 1\. Buka halaman utama Airbnb. 2\. Masukkan "Italia" di kolom "Ke mana?". 3\. Klik tombol "Cari". | Sistem menampilkan daftar properti yang tersedia di berbagai kota di Italia, atau peta Italia dengan penanda properti. |  |  |  | FALSE |  |
| TC-CP-A-03 | Pencarian properti dengan alamat spesifik yang valid. | 1\. Buka halaman utama Airbnb. 2\. Masukkan "Jl. Sudirman No.1, Jakarta Pusat" di kolom "Ke mana?". 3\. Klik tombol "Cari". | Sistem menampilkan properti yang berada di sekitar alamat tersebut atau peta yang terpusat pada alamat tersebut. |  |  |  | FALSE |  |
| TC-CP-A-04 | Pencarian properti dengan nama lokasi yang tidak ada/salah. | 1\. Buka halaman utama Airbnb. 2\. Masukkan "Wakanda" di kolom "Ke mana?". 3\. Klik tombol "Cari". | Sistem menampilkan pesan "Tidak ada hasil ditemukan untuk 'Wakanda'" atau saran lokasi alternatif. |  |  |  | FALSE |  |
| TC-CP-A-05 | Pencarian properti dengan input kosong pada kolom lokasi. | 1\. Buka halaman utama Airbnb. 2\. Biarkan kolom "Ke mana?" kosong. 3\. Klik tombol "Cari" (jika aktif). | Tombol "Cari" nonaktif, atau muncul pesan error yang meminta pengguna memasukkan destinasi. |  |  |  | FALSE |  |
| TC-CP-A-06 | Pencarian properti menggunakan fitur "Saya Fleksibel". | 1\. Buka halaman utama Airbnb. 2\. Klik opsi/tombol "Saya Fleksibel" pada bagian destinasi. 3\. Pilih durasi menginap (misalnya "Akhir Pekan", "Seminggu"). 4\. Klik "Cari". | Sistem menampilkan berbagai properti populer di berbagai destinasi yang sesuai dengan preferensi fleksibel dan durasi yang dipilih. |  |  |  | FALSE |  |

   

      2. ### ***Test Item: Pencarian properti dengan filter tanggal*** {#test-item:-pencarian-properti-dengan-filter-tanggal}

   Scope: Sistem harus memungkinkan pengguna untuk memfilter hasil pencarian berdasarkan tanggal check-in dan check-out.

   Scenario: Filter Tanggal Check-in dan Check-out

   

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result | Automated | Note |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | :---: | ----- |
| Test Item: Pencarian properti dengan filter tanggal |  |  |  |  |  |  |  |  |
| TC-CP-B-01 | Filter pencarian dengan rentang tanggal check-in dan check-out yang valid. | 1\. Lakukan pencarian awal berdasarkan lokasi (misalnya "Bali"). 2\. Di halaman hasil pencarian, klik filter tanggal. 3\. Pilih tanggal check-in dan check-out yang valid dan tersedia. 4\. Klik "Terapkan" atau "Simpan". | Hasil pencarian diperbarui, hanya menampilkan properti yang tersedia pada rentang tanggal yang dipilih. |  |  |  | FALSE |  |
| TC-CP-B-02 | Filter pencarian dengan tanggal check-out sebelum tanggal check-in. | dengan tanggal check-out sebelum tanggal check-in.1. Lakukan pencarian awal. 2\. Klik filter tanggal. 3\. Pilih tanggal check-in. 4\. Pilih tanggal check-out sebelum tanggal check-in. | Sistem menampilkan pesan error bahwa tanggal check-out harus setelah tanggal check-in, atau kalender mencegah pemilihan tanggal yang tidak valid. |  |  |  | FALSE |  |
| TC-CP-B-03 | Filter pencarian tanpa memilih tanggal (menghapus filter tanggal). | 1\. Lakukan pencarian dengan filter tanggal aktif. 2\. Klik filter tanggal. 3\. Klik opsi "Hapus tanggal" atau sejenisnya. 4\. Klik "Terapkan". | Filter tanggal dihapus, hasil pencarian menampilkan properti tanpa batasan tanggal tertentu (mungkin meminta untuk memilih tanggal). |  |  |  | FALSE |  |
| TC-CP-B-04 | Filter pencarian dengan tanggal di masa lalu. | 1\. Lakukan pencarian awal. 2\. Klik filter tanggal. 3\. Coba pilih tanggal check-in di masa lalu. | Kalender seharusnya tidak memungkinkan pemilihan tanggal di masa lalu untuk check-in. |  |  |  | FALSE |  |
| TC-CP-B-05 | Filter pencarian dengan durasi menginap yang sangat panjang (misalnya \> 1 tahun) | 1\. Lakukan pencarian awal. 2\. Klik filter tanggal. 3\. Pilih tanggal check-in. 4\. Pilih tanggal check-out dengan durasi lebih dari 1 tahun. 5\. Klik "Terapkan". | Sistem mungkin menampilkan properti yang mendukung penginapan jangka panjang, atau menampilkan pesan batasan durasi maksimal jika ada. |  |  |  | FALSE |  |

   

      3. ### ***Test Item: Pencarian properti dengan filter jumlah dan jenis tamu*** {#test-item:-pencarian-properti-dengan-filter-jumlah-dan-jenis-tamu}

   Scope: Sistem harus memungkinkan pengguna untuk memfilter berdasarkan jumlah tamu (dewasa, anak-anak, bayi).

   Scenario: Filter Jumlah Tamu

   

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result | Automated | Note |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | :---: | ----- |
| Test Item: Pencarian properti dengan filter jumlah dan jenis tamu |  |  |  |  |  |  |  |  |
| TC-CP-C-01 | Filter dengan jumlah dewasa valid. | 1\. Lakukan pencarian awal. 2\. Klik filter "Tamu". 3\. Atur jumlah dewasa menjadi "2". 4\. Klik "Terapkan". | Hasil pencarian diperbarui, menampilkan properti yang dapat mengakomodasi minimal 2 tamu dewasa. |  |  |  | FALSE |  |
| TC-CP-C-02 | Filter dengan jumlah dewasa, anak-anak, dan bayi yang valid. | 1\. Lakukan pencarian awal. 2\. Klik filter "Tamu". 3\. Atur jumlah dewasa "2", anak-anak "1", bayi "1". 4\. Klik "Terapkan". | Hasil pencarian diperbarui, menampilkan properti yang dapat mengakomodasi kombinasi tamu tersebut. |  |  |  | FALSE |  |
| TC-CP-C-03 | Filter dengan jumlah tamu melebihi kapasitas umum (misalnya, 20 tamu untuk apartemen standar). | 1\. Lakukan pencarian awal. 2\. Klik filter "Tamu". 3\. Atur jumlah dewasa menjadi "20". 4\. Klik "Terapkan". | Hasil pencarian menampilkan properti yang sangat besar atau pesan bahwa tidak ada properti yang sesuai dengan jumlah tamu tersebut, atau filter dibatasi pada jumlah maksimal. |  |  |  | FALSE |  |
| TC-CP-C-04 | Filter dengan jumlah tamu "0" (nol) atau input tidak valid. | 1\. Lakukan pencarian awal. 2\. Klik filter "Tamu". 3\. Coba atur jumlah dewasa menjadi "0" atau input string "abc". 4\. Klik "Terapkan". | Sistem seharusnya mencegah input "0" untuk dewasa atau input non-numerik. Minimum 1 dewasa biasanya diperlukan. Pesan error ditampilkan atau input diabaikan. |  |  |  | FALSE |  |
| TC-CP-C-05 | Menambah jumlah bayi tanpa adanya tamu dewasa. | 1\. Lakukan pencarian awal. 2\. Klik filter "Tamu". 3\. Atur jumlah dewasa menjadi "0" (jika memungkinkan) atau biarkan "1" lalu coba kurangi. 4\. Atur jumlah bayi menjadi "1". 5\. Klik "Terapkan". | Sistem seharusnya mensyaratkan minimal satu tamu dewasa jika ada bayi atau anak-anak. Pesan error ditampilkan. |  |  |  | FALSE |  |

   

      4. ### ***Test Item: Pencarian properti dengan filter jenis properti*** {#test-item:-pencarian-properti-dengan-filter-jenis-properti}

   Scope: Sistem harus memungkinkan pengguna untuk memfilter berdasarkan jenis properti (seluruh rumah/apartemen, kamar pribadi, kamar bersama).

   Scenario: Filter Jenis Properti

   

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result | Automated | Note |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | :---: | ----- |
| Test Item: Pencarian properti dengan filter jenis properti |  |  |  |  |  |  |  |  |
| TC-CP-D-01 | Filter dengan memilih satu jenis properti (misalnya, "Apartemen"). | 1\. Lakukan pencarian awal. 2\. Temukan dan klik filter "Jenis Tempat". 3\. Pilih "Apartemen". 4\. Klik "Tampilkan hasil" atau "Terapkan". | Hasil pencarian diperbarui dan hanya menampilkan properti dengan jenis "Apartemen". |  |  |  | FALSE |  |
| TC-CP-D-02 | Filter dengan memilih beberapa jenis properti (misalnya, "Rumah" dan "Vila"). | 1\. Lakukan pencarian awal. 2\. Klik filter "Jenis Tempat". 3\. Pilih "Rumah". 4\. Pilih "Vila". 5\. Klik "Tampilkan hasil". | Hasil pencarian diperbarui dan menampilkan properti yang berjenis "Rumah" ATAU "Vila". |  |  |  | FALSE |  |
| TC-CP-D-03 | Menghapus semua pilihan filter jenis properti. | 1\. Lakukan pencarian dengan filter jenis properti aktif. 2\. Klik filter "Jenis Tempat". 3\. Batalkan pilihan semua jenis properti yang sebelumnya dipilih, atau klik "Hapus". 4\. Klik "Tampilkan hasil". | Filter jenis properti dihapus, hasil pencarian menampilkan semua jenis properti yang relevan dengan kriteria pencarian lainnya. |  |  |  | FALSE |  |
| TC-CP-D-04 | Memilih jenis properti yang sangat spesifik atau langka. | 1\. Lakukan pencarian awal (mungkin di area yang luas). 2\. Klik filter "Jenis Tempat". 3\. Cari dan pilih jenis properti yang langka (misalnya, "Kastil", "Pulau"). 4\. Klik "Tampilkan hasil". | Hasil pencarian menampilkan properti jenis tersebut jika ada, atau pesan "Tidak ada hasil ditemukan" jika tidak ada yang sesuai. |  |  |  | FALSE |  |

   

      5. ### ***Test Item: Pencarian properti dengan filter rentang harga*** {#test-item:-pencarian-properti-dengan-filter-rentang-harga}

   Scope: Sistem harus memungkinkan pengguna untuk memfilter berdasarkan rentang harga per malam.

   Scenario: Filter Rentang Harga

   

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result | Automated | Note |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | :---: | ----- |
| Test Item: Pencarian properti dengan filter rentang harga |  |  |  |  |  |  |  |  |
| TC-CP-E-01 | Menggunakan filter harga pada hasil pencarian | 1\. Di halaman hasil pencarian, temukan filter harga. 2\. Atur rentang harga minimum dan maksimum (misalnya, Rp 500.000 \- Rp 1.500.000 per malam). 3\. Terapkan filter. | Daftar akomodasi diperbarui dan hanya menampilkan properti yang sesuai dengan rentang harga yang dipilih. |  |  |  | FALSE |  |
| TC-CP-E-02 | Filter dengan rentang harga minimum dan maksimum yang valid. | 1\. Lakukan pencarian awal. 2\. Klik filter "Harga". 3\. Atur harga minimum (misalnya Rp 500.000). 4\. Atur harga maksimum (misalnya Rp 2.000.000). 5\. Klik "Tampilkan hasil" atau "Simpan". | Hasil pencarian diperbarui, hanya menampilkan properti dengan harga per malam dalam rentang yang dipilih. |  |  |  | FALSE |  |
| TC-CP-E-03 | Filter dengan harga minimum lebih besar dari harga maksimum. | 1\. Lakukan pencarian awal. 2\. Klik filter "Harga". 3\. Atur harga minimum (misalnya Rp 2.000.000). 4\. Atur harga maksimum (misalnya Rp 500.000). 5\. Klik "Tampilkan hasil". | Sistem menampilkan pesan error bahwa harga minimum tidak boleh lebih besar dari harga maksimum, atau slider harga mencegah konfigurasi ini. |  |  |  | FALSE |  |
| TC-CP-E-04 | Filter hanya dengan harga minimum. | 1\. Lakukan pencarian awal. 2\. Klik filter "Harga". 3\. Atur harga minimum (misalnya Rp 1.000.000). 4\. Biarkan harga maksimum pada nilai default tertinggi atau kosong. 5\. Klik "Tampilkan hasil". | Hasil pencarian diperbarui, menampilkan properti dengan harga per malam sama dengan atau lebih besar dari harga minimum yang dipilih. |  |  |  | FALSE |  |
| TC-CP-E-05 | Filter hanya dengan harga maksimum. | 1\. Lakukan pencarian awal. 2\. Klik filter "Harga". 3\. Biarkan harga minimum pada nilai default terendah atau kosong. 4\. Atur harga maksimum (misalnya Rp 800.000). 5\. Klik "Tampilkan hasil". | Hasil pencarian diperbarui, menampilkan properti dengan harga per malam sama dengan atau lebih kecil dari harga maksimum yang dipilih. |  |  |  | FALSE |  |
| TC-CP-E-06 | Filter dengan input non-numerik pada rentang harga. | 1\. Lakukan pencarian awal. 2\. Klik filter "Harga". 3\. Coba masukkan "abc" di kolom harga minimum atau maksimum. 4\. Klik "Tampilkan hasil". | Sistem seharusnya mencegah input non-numerik, menampilkan pesan error, atau mengabaikan input yang tidak valid. |  |  |  | FALSE |  |
| TC-CP-E-07 | Menghapus filter harga setelah diterapkan. | 1\. Lakukan pencarian dengan filter harga aktif. 2\. Klik filter "Harga". 3\. Atur ulang slider ke rentang default atau klik opsi "Hapus". 4\. Klik "Tampilkan hasil". | Filter harga dihapus, hasil pencarian menampilkan properti tanpa batasan harga tertentu. |  |  |  | FALSE |  |

   

      6. ### ***Test Item: Pencarian properti dengan filter fasilitas*** {#test-item:-pencarian-properti-dengan-filter-fasilitas}

   Scope: Sistem harus memungkinkan pengguna untuk memfilter berdasarkan fasilitas (misalnya, Wi-Fi, dapur, kolam renang, parkir gratis, AC, mesin cuci).

   Scenario: Filter Fasilitas

   

| Test Item: Pencarian properti dengan filter fasilitas |  |  |  |  |  |  |  |  |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | :---: | ----- |
| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result | Automated | Note |
| TC-CP-F-01 | Filter dengan memilih satu fasilitas penting (misalnya, "Wi-Fi"). | 1\. Lakukan pencarian awal. 2\. Buka bagian filter, temukan "Fasilitas". 3\. Pilih "Wi-Fi". 4\. Klik "Tampilkan hasil". | Hasil pencarian diperbarui dan hanya menampilkan properti yang menyediakan fasilitas Wi-Fi. |  |  |  | FALSE |  |
| TC-CP-F-02 | Filter dengan memilih beberapa fasilitas (misalnya, "Dapur", "Parkir gratis"). | 1\. Lakukan pencarian awal. 2\. Buka filter "Fasilitas". 3\. Pilih "Dapur". 4\. Pilih "Parkir gratis". 5\. Klik "Tampilkan hasil". | Hasil pencarian diperbarui dan hanya menampilkan properti yang menyediakan KEDUA fasilitas tersebut (Dapur DAN Parkir gratis). |  |  |  | FALSE |  |
| TC-CP-F-03 | Menghapus filter fasilitas setelah diterapkan. | 1\. Lakukan pencarian dengan filter fasilitas aktif. 2\. Buka filter "Fasilitas". 3\. Batalkan pilihan semua fasilitas yang dipilih, atau klik "Hapus". 4\. Klik "Tampilkan hasil". | Filter fasilitas dihapus, hasil pencarian menampilkan properti tanpa batasan fasilitas tertentu. |  |  |  | FALSE |  |
| TC-CP-F-04 | Filter dengan memilih fasilitas yang jarang ada atau sangat spesifik. | 1\. Lakukan pencarian awal. 2\. Buka filter "Fasilitas". 3\. Pilih fasilitas yang jarang (misalnya, "Helipad" jika ada sebagai opsi, atau "Akses ski-in/ski-out"). 4\. Klik "Tampilkan hasil". | Hasil pencarian menampilkan properti yang memiliki fasilitas tersebut jika ada, atau pesan "Tidak ada hasil ditemukan" jika tidak ada yang sesuai. |  |  |  | FALSE |  |

   

      7. ### ***Test Item: Pencarian properti dengan filter karakteristik khusus tambahan*** {#test-item:-pencarian-properti-dengan-filter-karakteristik-khusus-tambahan}

   Scope: Sistem harus memungkinkan pengguna untuk memfilter berdasarkan karakteristik khusus (misalnya, ramah hewan peliharaan, aksesibilitas kursi roda, sarapan gratis).

   Scenario: Filter Karakteristik Khusus

   

| Test Item: Pencarian properti dengan filter karakteristik khusus tambahan |  |  |  |  |  |  |  |  |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | :---: | ----- |
| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result | Automated | Note |
| TC-CP-G-01 | Filter dengan memilih satu karakteristik khusus (misalnya, "Boleh bawa hewan peliharaan") | 1\. Lakukan pencarian awal. 2\. Buka bagian filter, temukan opsi seperti "Aturan Rumah" atau "Fitur Tambahan". 3\. Pilih "Boleh bawa hewan peliharaan". 4\. Klik "Tampilkan hasil". | Hasil pencarian diperbarui dan hanya menampilkan properti yang memperbolehkan hewan peliharaan. |  |  |  | FALSE |  |
| TC-CP-G-02 | Filter dengan memilih beberapa karakteristik khusus. | 1\. Lakukan pencarian awal. 2\. Buka filter relevan. 3\. Pilih "Check-in mandiri". 4\. Pilih "Cocok untuk acara". 5\. Klik "Tampilkan hasil". | Hasil pencarian diperbarui dan hanya menampilkan properti yang memenuhi SEMUA karakteristik yang dipilih. |  |  |  | FALSE |  |
| TC-CP-G-03 | Menghapus filter karakteristik khusus setelah diterapkan. | 1\. Lakukan pencarian dengan filter karakteristik khusus aktif. 2\. Buka filter relevan. 3\. Batalkan pilihan semua karakteristik yang dipilih atau klik "Hapus". 4\. Klik "Tampilkan hasil". | Filter karakteristik khusus dihapus, hasil pencarian menampilkan properti tanpa batasan karakteristik tersebut. |  |  |  | FALSE |  |

   

      8. ### ***Test Item: Pencarian properti dengan filter jumlah kamar tidur dan kamar mandi*** {#test-item:-pencarian-properti-dengan-filter-jumlah-kamar-tidur-dan-kamar-mandi}

   Scope: Sistem harus memungkinkan pengguna untuk memfilter berdasarkan jumlah kamar tidur dan kamar mandi.

   Scenario: Filter Jumlah Kamar Tidur dan Kamar Mandi

   

| Test Item: Pencarian properti dengan filter jumlah kamar tidur dan kamar mandi |  |  |  |  |  |  |  |  |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | :---: | ----- |
| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result | Automated | Note |
| TC-CP-H-01 | Filter dengan jumlah kamar tidur spesifik (misalnya, "2 Kamar Tidur"). | 1\. Lakukan pencarian awal. 2\. Buka bagian filter, temukan "Kamar tidur dan tempat tidur". 3\. Pilih "2" untuk kamar tidur. 4\. Klik "Tampilkan hasil". | Hasil pencarian diperbarui dan hanya menampilkan properti dengan minimal 2 kamar tidur (atau tepat 2, tergantung implementasi). |  |  |  | FALSE |  |
| TC-CP-H-02 | Filter dengan jumlah kamar mandi spesifik (misalnya, "1 Kamar Mandi"). | 1\. Lakukan pencarian awal. 2\. Buka filter "Kamar tidur dan tempat tidur" atau filter terpisah untuk kamar mandi. 3\. Pilih "1" untuk kamar mandi. 4\. Klik "Tampilkan hasil". | Hasil pencarian diperbarui dan hanya menampilkan properti dengan minimal 1 kamar mandi (atau tepat 1). |  |  |  | FALSE |  |
| TC-CP-H-03 | Filter dengan jumlah kamar tidur dan kamar mandi tertentu. | 1\. Lakukan pencarian awal. 2\. Buka filter relevan. 3\. Pilih "3" untuk kamar tidur. 4\. Pilih "2" untuk kamar mandi. 5\. Klik "Tampilkan hasil". | Hasil pencarian diperbarui, menampilkan properti dengan minimal 3 kamar tidur DAN minimal 2 kamar mandi. |  |  |  | FALSE |  |
| TC-CP-H-04 | Filter dengan memilih "Berapa pun" atau "Fleksibel" untuk kamar tidur/mandi. | 1\. Lakukan pencarian awal. 2\. Buka filter relevan. 3\. Pilih opsi "Berapa pun" atau biarkan default untuk kamar tidur/mandi. 4\. Klik "Tampilkan hasil". | Jumlah kamar tidur/mandi tidak menjadi batasan utama, menampilkan properti dengan berbagai jumlah kamar tidur/mandi. |  |  |  | FALSE |  |
| TC-CP-H-05 | Mencoba input non-numerik atau negatif untuk jumlah kamar. | 1\. Lakukan pencarian awal. 2\. Buka filter relevan. 3\. Coba masukkan "-1" atau "abc" jika ada field input manual (biasanya berupa pilihan \+/- atau dropdown). | Sistem mencegah input tidak valid. Tombol \+/- tidak akan mengizinkan nilai negatif. Dropdown hanya menampilkan opsi valid. |  |  |  | FALSE |  |

   

      9. ### ***Test Item: Pencarian properti dalam bentuk daftar*** {#test-item:-pencarian-properti-dalam-bentuk-daftar}

   Scope: Sistem harus menampilkan hasil pencarian dalam bentuk daftar dan peta interaktif.

   Scenario: Tampilan Daftar dan Peta

   

| Test Item: Pencarian properti dalam bentuk daftar |  |  |  |  |  |  |  |  |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | :---: | ----- |
| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result | Automated | Note |
| TC-CP-I-01 | Verifikasi tampilan daftar hasil pencarian standar. | 1\. Lakukan pencarian properti dengan kriteria apa pun. | Halaman hasil pencarian menampilkan daftar properti. Setiap item daftar menampilkan informasi ringkas (foto, nama, harga, rating). |  |  |  | FALSE |  |
| TC-CP-I-02 | Verifikasi pagination pada tampilan daftar (jika hasil banyak). | 1\. Lakukan pencarian yang menghasilkan banyak properti. 2\. Scroll ke bawah halaman. 3\. Cari dan klik tombol "Berikutnya" atau nomor halaman. | Daftar properti di halaman berikutnya ditampilkan. Tombol pagination berfungsi dengan benar (maju, mundur, ke halaman spesifik). |  |  |  | FALSE |  |
| TC-CP-I-03 | Verifikasi tampilan saat tidak ada hasil yang ditemukan. | 1\. Lakukan pencarian dengan kriteria yang sangat spesifik sehingga tidak ada hasil (misalnya lokasi "Xyz123" dengan filter harga sangat tinggi dan fasilitas langka). | Halaman menampilkan pesan bahwa tidak ada properti yang cocok dengan kriteria pencarian. Mungkin menawarkan saran untuk mengubah filter. |  |  |  | FALSE |  |
| TC-CP-I-04 | Verifikasi sorting/pengurutan daftar (jika ada opsi). | 1\. Lakukan pencarian. 2\. Cari opsi pengurutan (misalnya "Harga Terendah", "Rating Tertinggi"). 3\. Pilih salah satu opsi pengurutan. | Daftar properti diurutkan ulang sesuai dengan opsi yang dipilih. |  |  |  | FALSE |  |

   

      10. ### ***Test Item: Penampilan informasi pencarian ringkas*** {#test-item:-penampilan-informasi-pencarian-ringkas}

   Scope: Sistem harus menampilkan informasi ringkas untuk setiap properti di hasil pencarian (gambar utama, lokasi, harga per malam, rating ulasan, jumlah ulasan).

   Scenario: Informasi Detail Properti

   

| Test Item: Penampilan informasi pencarian ringkas |  |  |  |  |  |  |  |  |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | :---: | ----- |
| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result | Automated | Note |
| TC-CP-J-01 | Verifikasi tampilan foto utama properti. | 1\. Lakukan pencarian properti. 2\. Amati setiap item daftar di hasil pencarian. | Setiap item daftar menampilkan setidaknya satu foto utama properti yang representatif. |  |  |  | FALSE |  |
| TC-CP-J-02 | Verifikasi tampilan nama/judul properti. | 1\. Lakukan pencarian properti. 2\. Amati setiap item daftar. | Setiap item daftar menampilkan nama atau judul properti yang jelas dan deskriptif. |  |  |  | FALSE |  |
| TC-CP-J-03 | Verifikasi tampilan harga per malam. | 1\. Lakukan pencarian properti. 2\. Amati setiap item daftar. | Setiap item daftar menampilkan harga per malam atau harga total untuk tanggal yang dipilih (jika tanggal sudah dimasukkan). Format mata uang benar. |  |  |  | FALSE |  |
| TC-CP-J-04 | Verifikasi tampilan rating rata-rata dan jumlah ulasan (jika ada). | 1\. Lakukan pencarian properti. 2\. Amati setiap item daftar. | Setiap item daftar menampilkan rating bintang rata-rata dan jumlah ulasan (misalnya "⭐ 4.8 (120 ulasan)"). Jika tidak ada ulasan, tampilkan "Baru" atau sejenisnya. |  |  |  | FALSE |  |
| TC-CP-J-05 | Verifikasi tampilan jenis properti atau deskripsi singkat. | 1\. Lakukan pencarian properti. 2\. Amati setiap item daftar. | Setiap item daftar menampilkan jenis properti (misalnya "Seluruh apartemen") atau deskripsi singkat (misalnya "2 tamu · 1 kamar tidur · 1 kamar mandi"). |  |  |  | FALSE |  |
| TC-CP-J-06 | Verifikasi tautan ke halaman detail properti dari informasi ringkas. | 1\. Lakukan pencarian properti. 2\. Klik pada salah satu item daftar (foto, nama, atau area yang ditentukan). | Pengguna diarahkan ke halaman detail lengkap dari properti yang dipilih. |  |  |  | FALSE |  |

   

      11. ### ***Test Item: Daftar keinginan pengguna*** {#test-item:-daftar-keinginan-pengguna}

   Scope: Sistem harus menyediakan fitur "Daftar Keinginan" (Wishlist) agar pengguna dapat menyimpan properti.

   Scenario: Fitur Daftar Keinginan (Wishlist)

   

| Test Item: Daftar keinginan pengguna |  |  |  |  |  |  |  |  |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | :---: | ----- |
| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result | Automated | Note |
| TC-CP-K-01 | Menambahkan properti ke daftar keinginan baru dari halaman hasil pencarian. | 1\. Pengguna sudah login. 2\. Lakukan pencarian properti. 3\. Pada salah satu item properti di hasil pencarian, klik ikon hati (❤) atau "Simpan". 4\. Saat diminta membuat daftar keinginan baru, masukkan nama "Liburan Impian". 5\. Klik "Buat". | Properti berhasil ditambahkan ke daftar keinginan baru "Liburan Impian". Ikon hati menjadi terisi. Notifikasi sukses muncul. |  |  |  | FALSE |  |
| TC-CP-K-02 | Menambahkan properti ke daftar keinginan yang sudah ada. | 1\. Pengguna sudah login dan memiliki setidaknya satu daftar keinginan. 2\. Lakukan pencarian properti. 3\. Klik ikon hati pada properti lain. 4\. Pilih daftar keinginan yang sudah ada dari daftar yang muncul. | Properti berhasil ditambahkan ke daftar keinginan yang dipilih. Ikon hati menjadi terisi. |  |  |  | FALSE |  |
| TC-CP-K-03 | Menghapus properti dari daftar keinginan dari halaman hasil pencarian. | 1\. Pengguna sudah login. 2\. Temukan properti yang sudah ada di daftar keinginan (ikon hati terisi). 3\. Klik ikon hati yang terisi tersebut. | Properti berhasil dihapus dari daftar keinginan. Ikon hati menjadi kosong/tidak terisi. |  |  |  | FALSE |  |
| TC-CP-K-04 | Melihat daftar keinginan. | 1\. Pengguna sudah login. 2\. Klik menu profil pengguna. 3\. Pilih opsi "Daftar Keinginan" atau "Simpanan". | Halaman daftar keinginan ditampilkan, memperlihatkan semua daftar keinginan yang telah dibuat pengguna beserta properti di dalamnya. |  |  |  | FALSE |  |
| TC-CP-K-05 | Membuat daftar keinginan baru dari halaman Daftar Keinginan. | 1\. Pengguna sudah login dan berada di halaman Daftar Keinginan. 2\. Klik tombol "Buat daftar keinginan baru". 3\. Masukkan nama "Rencana Akhir Pekan". 4\. Klik "Buat". | Daftar keinginan baru "Rencana Akhir Pekan" berhasil dibuat dan muncul di halaman Daftar Keinginan. |  |  |  | FALSE |  |
| TC-CP-K-06 | Mengedit nama daftar keinginan. | 1\. Pengguna sudah login dan berada di halaman Daftar Keinginan. 2\. Pilih salah satu daftar keinginan. 3\. Klik opsi "Edit" atau ikon pensil pada nama daftar keinginan. 4\. Ubah nama daftar keinginan. 5\. Simpan perubahan. | Nama daftar keinginan berhasil diubah. |  |  |  | FALSE |  |
| TC-CP-K-07 | Menghapus daftar keinginan. | 1\. Pengguna sudah login dan berada di halaman Daftar Keinginan. 2\. Pilih salah satu daftar keinginan. 3\. Klik opsi "Edit" atau menu titik tiga. 4\. Pilih "Hapus daftar keinginan ini". 5\. Konfirmasi penghapusan. | Daftar keinginan berhasil dihapus dari daftar. |  |  |  | FALSE |  |
| TC-CP-K-08 | Mencoba menambahkan properti ke wishlist tanpa login. | 1\. Pengguna belum login. 2\. Lakukan pencarian properti. 3\. Klik ikon hati (❤) atau "Simpan" pada salah satu properti. | Sistem akan meminta pengguna untuk login atau mendaftar terlebih dahulu sebelum dapat menyimpan properti ke daftar keinginan. Pengguna diarahkan ke halaman login/pendaftaran. |  |  |  | FALSE |  |

   

   

   

   

   2. ## **User Management** {#user-management}

      1. ### ***Test Item: Pendaftaran akun*** {#test-item:-pendaftaran-akun}

   Scope: Sistem harus memungkinkan pengguna untuk mendaftar akun baru menggunakan email, Google, Facebook, atau Apple ID.

   Scenario: Registrasi Pengguna baru

   

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result | Automated | Note |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| User Management |  |  |  |  |  |  |  |  |
| Test Item: Pendaftaran akun |  |  |  |  |  |  |  |  |
| TC-USR-A-01 | Pendaftaran akun baru dengan semua informasi valid. | 1\. Buka halaman utama Airbnb. 2\. Klik tombol "Daftar". 3\. Pilih metode pendaftaran (misalnya, "Lanjutkan dengan email"). 4\. Isi semua kolom wajib (Nama Depan, Nama Belakang, Tanggal Lahir, Email, Kata Sandi) dengan data yang valid dan unik. 5\. Setujui Syarat & Ketentuan. 6\. Klik tombol "Setuju dan lanjutkan" atau "Daftar". | Pengguna berhasil masuk. Pengguna diarahkan ke halaman utama atau dashboard. Profil pengguna (nama/foto) ditampilkan. |  |  |  | FALSE |  |
| TC-USR-A-02 | Pendaftaran akun dengan email yang sudah terdaftar. | 1\. Buka halaman utama Airbnb. 2\. Klik tombol "Daftar". 3\. Pilih metode pendaftaran dengan email. 4\. Isi semua kolom wajib dengan data valid, namun gunakan alamat email yang sudah terdaftar di Airbnb. 5\. Klik tombol "Daftar". | Sistem menampilkan pesan error "Kata sandi salah" atau "Email atau kata sandi Anda salah." Pengguna tetap di halaman masuk. |  |  |  | FALSE |  |
| TC-USR-A-03 | Pendaftaran akun dengan kata sandi yang tidak memenuhi syarat (misalnya, terlalu pendek). | 1\. Buka halaman utama Airbnb. 2\. Klik tombol "Daftar". 3\. Pilih metode pendaftaran dengan email. 4\. Isi semua kolom wajib dengan data valid, namun masukkan kata sandi yang terlalu pendek (misalnya, "123"). 5\. Klik tombol "Daftar". | Sistem menampilkan pesan error "Tidak ada akun yang cocok dengan email ini" atau "Email atau kata sandi Anda salah." Pengguna tetap di halaman masuk. |  |  |  | FALSE |  |
| TC-USR-A-04 | Pendaftaran akun dengan kolom wajib tidak diisi. | 1\. Buka halaman utama Airbnb. 2\. Klik tombol "Daftar". 3\. Pilih metode pendaftaran dengan email. 4\. Biarkan salah satu kolom wajib (misalnya, Nama Belakang) kosong. 5\. Isi kolom lainnya. 6\. Klik tombol "Daftar". | Sistem menampilkan pesan error yang menunjukkan bahwa kolom tersebut wajib diisi. Pendaftaran gagal. |  |  |  | FALSE |  |
| TC-USR-A-05 | Pendaftaran akun dengan format email tidak valid. | dengan format email tidak valid.1. Buka halaman utama Airbnb. 2\. Klik tombol "Daftar". 3\. Pilih metode pendaftaran dengan email. 4\. Isi semua kolom wajib, namun masukkan format email yang salah (misalnya, "tes@contoh" atau "https://www.google.com/search?q=tes.contoh.com"). 5\. Klik tombol "Daftar". | Sistem menampilkan pesan error bahwa format email tidak valid. Pendaftaran gagal. |  |  |  | FALSE |  |
| TC-USR-A-06 | Pendaftaran akun dengan usia di bawah batas minimum. | 1\. Buka halaman utama Airbnb. 2\. Klik tombol "Daftar". 3\. Pilih metode pendaftaran dengan email. 4\. Isi semua kolom wajib, namun masukkan tanggal lahir yang mengindikasikan usia di bawah batas minimum yang ditetapkan Airbnb (misalnya, di bawah 18 tahun). 5\. Klik tombol "Daftar". | Sistem menampilkan pesan error bahwa pengguna tidak memenuhi syarat usia atau pendaftaran diblokir. Pendaftaran gagal. |  |  |  | FALSE |  |
| TC-USR-A-07 | Pendaftaran menggunakan akun pihak ketiga (misalnya Google/Facebook). | 1\. Buka halaman utama Airbnb. 2\. Klik tombol "Daftar". 3\. Pilih opsi "Lanjutkan dengan Google" (atau Facebook, Apple). 4\. Ikuti alur otentikasi dari penyedia pihak ketiga. 5\. Setujui izin yang diminta Airbnb. | Akun berhasil dibuat menggunakan detail dari akun pihak ketiga. Pengguna diarahkan ke halaman profil atau halaman utama dalam keadaan login. |  |  |  | FALSE |  |

   

      2. ### ***Test Item: Masuk akun*** {#test-item:-masuk-akun}

   Scope: Sistem harus memungkinkan pengguna untuk masuk (login) ke akun mereka.

   Scenario: Login Pengguna

   

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result |
| ----- | ----- | ----- | ----- | ----- |
| Test Item: Masuk akun |  |  |  |  |
| TC-USR-B-01 | Masuk dengan email dan kata sandi yang valid. | 1\. Buka halaman utama Airbnb. 2\. Klik tombol "Masuk". 3\. Masukkan email yang terdaftar dan valid. 4\. Masukkan kata sandi yang benar. 5\. Klik tombol "Lanjutkan" atau "Masuk". | Pengguna berhasil masuk. Pengguna diarahkan ke halaman utama atau dashboard. Profil pengguna (nama/foto) ditampilkan. |  |
| TC-USR-B-02 | Masuk dengan email valid tetapi kata sandi salah. | 1\. Buka halaman utama Airbnb. 2\. Klik tombol "Masuk". 3\. Masukkan email yang terdaftar dan valid. 4\. Masukkan kata sandi yang salah. 5\. Klik tombol "Masuk". | Sistem menampilkan pesan error "Kata sandi salah" atau "Email atau kata sandi Anda salah." Pengguna tetap di halaman masuk. |  |
| TC-USR-B-03 | Masuk dengan email tidak terdaftar. | 1\. Buka halaman utama Airbnb. 2\. Klik tombol "Masuk". 3\. Masukkan email yang tidak terdaftar. 4\. Masukkan kata sandi acak. 5\. Klik tombol "Masuk". | Sistem menampilkan pesan error "Tidak ada akun yang cocok dengan email ini" atau "Email atau kata sandi Anda salah." Pengguna tetap di halaman masuk. |  |
| TC-USR-B-04 | Masuk dengan membiarkan kolom email kosong. | 1\. Buka halaman utama Airbnb. 2\. Klik tombol "Masuk". 3\. Biarkan kolom email kosong. 4\. Masukkan kata sandi. 5\. Klik tombol "Masuk". | Sistem menampilkan pesan error yang meminta pengguna untuk memasukkan email. Tombol "Masuk" mungkin nonaktif. |  |
| TC-USR-B-05 | Masuk dengan membiarkan kolom kata sandi kosong. | 1\. Buka halaman utama Airbnb. 2\. Klik tombol "Masuk". 3\. Masukkan email yang valid. 4\. Biarkan kolom kata sandi kosong. 5\. Klik tombol "Masuk". | Sistem menampilkan pesan error yang meminta pengguna untuk memasukkan kata sandi. Tombol "Masuk" mungkin nonaktif. |  |
| TC-USR-B-06 | Masuk menggunakan akun pihak ketiga (misalnya Google/Facebook). | 1\. Buka halaman utama Airbnb. 2\. Klik tombol "Masuk". 3\. Pilih opsi "Lanjutkan dengan Google" (atau Facebook, Apple). 4\. Ikuti alur otentikasi dari penyedia pihak ketiga. | Pengguna berhasil masuk menggunakan akun pihak ketiga. Pengguna diarahkan ke halaman utama atau dashboard. |  |
| TC-USR-B-07 | Percobaan masuk berulang kali dengan kredensial salah (uji penguncian akun). | 1\. Buka halaman utama Airbnb. 2\. Klik tombol "Masuk". 3\. Masukkan email valid dan kata sandi salah secara berulang (misalnya 5-10 kali). 4\. Klik tombol "Masuk" setiap kali. | Setelah beberapa kali percobaan gagal, sistem mungkin menampilkan CAPTCHA, pesan tentang terlalu banyak percobaan gagal, atau mengunci akun untuk sementara waktu. |  |

   

      3. ### ***Test Item: Lupa kata sandi*** {#test-item:-lupa-kata-sandi}

   Scope: Sistem harus menyediakan fitur "Lupa Kata Sandi" untuk reset kata sandi.

   Scenario: Lupa Kata Sandi

   

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date |
| ----- | ----- | ----- | ----- | ----- | ----- |
| Test Item: Lupa kata sandi |  |  |  |  |  |
| TC-USR-C-01 | Meminta reset kata sandi dengan email terdaftar yang valid. | 1\. Buka halaman masuk Airbnb. 2\. Klik tautan "Lupa kata sandi?". 3\. Masukkan alamat email yang terdaftar. 4\. Klik tombol "Kirim tautan pengaturan ulang" atau sejenisnya. | Sistem menampilkan pesan konfirmasi bahwa email untuk mengatur ulang kata sandi telah dikirim. Pengguna menerima email berisi tautan atau kode untuk mengatur ulang kata sandi. |  |  |
| TC-USR-C-02 | Meminta reset kata sandi dengan email yang tidak terdaftar. | 1\. Buka halaman masuk Airbnb. 2\. Klik tautan "Lupa kata sandi?". 3\. Masukkan alamat email yang tidak terdaftar. 4\. Klik tombol "Kirim tautan pengaturan ulang". | Sistem menampilkan pesan error bahwa email tidak ditemukan atau tidak ada akun yang terkait dengan email tersebut. Tidak ada email yang dikirim. |  |  |
| TC-USR-C-03 | Membiarkan kolom email kosong saat meminta reset kata sandi. | 1\. Buka halaman masuk Airbnb. 2\. Klik tautan "Lupa kata sandi?". 3\. Jangan isi kolom email. 4\. Klik tombol "Kirim tautan pengaturan ulang". | Sistem menampilkan pesan error yang meminta pengguna untuk memasukkan alamat email. |  |  |
| TC-USR-C-04 | Mengikuti tautan reset kata sandi dan mengatur kata sandi baru yang valid. | 1\. Pengguna telah menerima email reset kata sandi (dari TC\_FORGOT\_001). 2\. Klik tautan reset kata sandi di email. 3\. Pengguna diarahkan ke halaman pengaturan ulang kata sandi. 4\. Masukkan kata sandi baru yang valid dan memenuhi syarat. 5\. Konfirmasi kata sandi baru. 6\. Klik "Atur Ulang Kata Sandi". | Kata sandi berhasil diubah. Pengguna dapat login menggunakan kata sandi baru. Sistem menampilkan pesan sukses. |  |  |
| TC-USR-C-05 | Mengikuti tautan reset kata sandi yang sudah kedaluwarsa atau tidak valid. | 1\. Pengguna memiliki tautan reset kata sandi yang sudah kedaluwarsa atau digunakan sebelumnya. 2\. Klik tautan tersebut. | Sistem menampilkan pesan error bahwa tautan tidak valid, kedaluwarsa, atau sudah digunakan. Pengguna mungkin disarankan untuk meminta tautan reset baru. |  |  |
| TC-USR-C-06 | Mengatur kata sandi baru yang tidak memenuhi syarat saat reset. | 1\. Pengguna berada di halaman pengaturan ulang kata sandi (dari TC\_FORGOT\_004, langkah 3). 2\. Masukkan kata sandi baru yang terlalu pendek atau tidak memenuhi syarat. 3\. Konfirmasi kata sandi baru. 4\. Klik "Atur Ulang Kata Sandi". | Sistem menampilkan pesan error yang menjelaskan persyaratan kata sandi. Kata sandi tidak diubah. |  |  |
| TC-USR-C-07 | Kata sandi baru tidak cocok dengan konfirmasi kata sandi saat reset. | 1\. Pengguna berada di halaman pengaturan ulang kata sandi. 2\. Masukkan kata sandi baru yang valid. 3\. Masukkan kata sandi yang berbeda di kolom konfirmasi. 4\. Klik "Atur Ulang Kata Sandi". | Sistem menampilkan pesan error bahwa kata sandi dan konfirmasi kata sandi tidak cocok. Kata sandi tidak diubah. |  |  |

   

      4. ### ***Test Item: Pengeditan profil*** {#test-item:-pengeditan-profil}

   Scope: Sistem harus memungkinkan pengguna untuk mengedit profil mereka (nama, foto profil, deskripsi diri, nomor telepon).

   Scenario: Edit Profil Pengguna

   

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date |
| ----- | ----- | ----- | ----- | ----- | ----- |
| Test Item: Pengeditan profil |  |  |  |  |  |
| TC-USR-D-07 | Mengedit informasi pribadi (misalnya, Nama, Tanggal Lahir, Jenis Kelamin) dengan data valid. | 1\. Pengguna sudah login. 2\. Navigasi ke halaman "Akun" atau "Profil". 3\. Pilih "Informasi pribadi". 4\. Klik "Edit" pada bagian yang ingin diubah (misalnya, Nama). 5\. Ubah informasi dengan data valid. 6\. Klik "Simpan". | Sistem menampilkan pesan error bahwa Nama Depan wajib diisi. Perubahan tidak disimpan. |  |  |
| TC-USR-D-08 | Mencoba mengedit informasi pribadi dengan data tidak valid (misalnya, nama kosong). | 1\. Pengguna sudah login dan berada di halaman edit informasi pribadi. 2\. Hapus isi kolom Nama Depan. 3\. Klik "Simpan". | Sistem menampilkan pesan error bahwa Nama Depan wajib diisi. Perubahan tidak disimpan. |  |  |
| TC-USR-D-09 | Mengubah alamat email dengan email baru yang valid dan belum terdaftar. | 1\. Pengguna sudah login dan berada di halaman edit informasi pribadi. 2\. Klik "Edit" pada bagian alamat email. 3\. Masukkan alamat email baru yang valid dan belum terdaftar. 4\. Mungkin diminta memasukkan kata sandi saat ini. 5\. Klik "Simpan" atau "Lanjutkan". | Perubahan email berhasil disimpan. Sistem mungkin mengirim email verifikasi ke alamat email baru. Setelah verifikasi (jika ada), email di profil diperbarui. |  |  |
| TC-USR-D-10 | Mencoba mengubah alamat email dengan email yang sudah terdaftar. | 1\. Pengguna sudah login dan berada di halaman edit informasi pribadi. 2\. Klik "Edit" pada bagian alamat email. 3\. Masukkan alamat email yang sudah digunakan oleh akun Airbnb lain. 4\. Klik "Simpan". | Sistem menampilkan pesan error bahwa alamat email tersebut sudah digunakan. Perubahan tidak disimpan. |  |  |
| TC-USR-D-11 | Mengubah nomor telepon dengan nomor yang valid. | 1\. Pengguna sudah login dan berada di halaman edit informasi pribadi. 2\. Klik "Tambah" atau "Edit" pada bagian nomor telepon. 3\. Masukkan nomor telepon yang valid. 4\. Mungkin ada proses verifikasi via SMS. 5\. Klik "Simpan" atau "Verifikasi". | Nomor telepon berhasil ditambahkan/diperbarui dan diverifikasi (jika ada). Nomor telepon ditampilkan di profil. |  |  |
| TC-USR-D-12 | Mencoba menyimpan nomor telepon dengan format tidak valid. | 1\. Pengguna sudah login dan berada di halaman edit nomor telepon. 2\. Masukkan nomor telepon dengan format salah (misalnya, "abcde" atau terlalu banyak/sedikit digit). 3\. Klik "Simpan". | Sistem menampilkan pesan error bahwa format nomor telepon tidak valid. Perubahan tidak disimpan. |  |  |
| TC-USR-D-13 | Mengunggah atau mengubah foto profil. | 1\. Pengguna sudah login dan berada di halaman "Profil" atau "Akun". 2\. Klik opsi untuk mengedit atau menambah foto profil. 3\. Pilih file gambar dengan format yang didukung (JPG, PNG) dan ukuran sesuai. 4\. Unggah dan sesuaikan (jika ada opsi crop). 5\. Simpan. | Foto profil berhasil diunggah/diperbarui dan ditampilkan di halaman profil pengguna dan di tempat lain yang relevan (misalnya, ulasan). |  |  |
| TC-USR-D-14 | Mencoba mengunggah foto profil dengan format tidak didukung atau ukuran terlalu besar. | 1\. Pengguna sudah login dan berada di halaman edit foto profil. 2\. Coba unggah file dengan format tidak didukung (misalnya, .txt, .gif jika tidak didukung) atau file gambar yang ukurannya melebihi batas. | Sistem menampilkan pesan error bahwa format file tidak didukung atau ukuran file terlalu besar. Foto tidak terunggah. |  |  |
| TC-USR-D-15 | Menambahkan atau mengedit bagian "Tentang Saya". | 1\. Pengguna sudah login dan berada di halaman "Profil". 2\. Klik "Edit profil". 3\. Cari bagian "Tentang Saya" atau bio. 4\. Masukkan atau edit teks deskripsi diri. 5\. Klik "Simpan". | Informasi "Tentang Saya" berhasil disimpan dan ditampilkan di profil publik pengguna. |  |  |

   

      5. ### ***Test Item: Pengelolaan metode pembayaran*** {#test-item:-pengelolaan-metode-pembayaran}

   Scope: Sistem harus memungkinkan pengguna untuk menambahkan dan mengelola metode pembayaran yang valid.

   Scenario: Manajemen Metode Pembayaran

   

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date |
| ----- | ----- | ----- | ----- | ----- | ----- |
| Test Item: Pengelolaan metode pembayaran |  |  |  |  |  |
| TC-USR-E-07 | Menambahkan metode pembayaran baru (kartu kredit) dengan detail valid. | 1\. Pengguna sudah login. 2\. Navigasi ke "Akun" \-\> "Pembayaran & payout". 3\. Klik "Tambahkan metode pembayaran". 4\. Pilih "Kartu kredit atau debit". 5\. Masukkan detail kartu yang valid (nomor kartu, tanggal kedaluwarsa, CVV, nama pada kartu, alamat penagihan). 6\. Klik "Tambahkan kartu". | Metode pembayaran berhasil ditambahkan dan muncul di daftar metode pembayaran pengguna. Mungkin ada verifikasi kecil (otorisasi sejumlah kecil). |  |  |
| TC-USR-E-08 | Mencoba menambahkan kartu kredit dengan nomor kartu tidak valid. | 1\. Pengguna sudah login dan berada di halaman tambah metode pembayaran. 2\. Masukkan nomor kartu kredit yang tidak valid (misalnya, kurang digit, format salah). 3\. Isi detail lain. 4\. Klik "Tambahkan kartu". | Sistem menampilkan pesan error bahwa nomor kartu tidak valid. Metode pembayaran tidak ditambahkan. |  |  |
| TC-USR-E-09 | Mencoba menambahkan kartu kredit dengan tanggal kedaluwarsa di masa lalu. | 1\. Pengguna sudah login dan berada di halaman tambah metode pembayaran. 2\. Masukkan tanggal kedaluwarsa kartu yang sudah lewat. 3\. Isi detail lain. 4\. Klik "Tambahkan kartu". | Sistem menampilkan pesan error bahwa tanggal kedaluwarsa tidak valid atau kartu sudah kedaluwarsa. Metode pembayaran tidak ditambahkan. |  |  |
| TC-USR-E-10 | Mencoba menambahkan kartu kredit dengan CVV tidak valid (misalnya, string). | 1\. Pengguna sudah login dan berada di halaman tambah metode pembayaran. 2\. Masukkan CVV berupa string "abc" (jika input memungkinkan) atau jumlah digit salah. 3\. Isi detail lain. 4\. Klik "Tambahkan kartu". | Sistem menampilkan pesan error bahwa CVV tidak valid. Metode pembayaran tidak ditambahkan. Input field CVV seharusnya hanya menerima angka. |  |  |
| TC-USR-E-11 | Menghapus metode pembayaran yang sudah ada. | 1\. Pengguna sudah login dan berada di "Pembayaran & payout". 2\. Temukan metode pembayaran yang ingin dihapus. 3\. Klik opsi "Hapus" atau ikon titik tiga lalu "Hapus". 4\. Konfirmasi penghapusan. | Metode pembayaran berhasil dihapus dari daftar. |  |  |
| TC-USR-E-12 | Mengatur satu metode pembayaran sebagai metode default (jika ada fitur). | 1\. Pengguna sudah login dan memiliki lebih dari satu metode pembayaran. 2\. Navigasi ke "Pembayaran & payout". 3\. Pilih metode pembayaran yang ingin dijadikan default. 4\. Klik opsi "Jadikan default". | Metode pembayaran yang dipilih berhasil ditetapkan sebagai default dan ditandai demikian. |  |  |
| TC-USR-E-13 | Mencoba menghapus metode pembayaran yang sedang terkait dengan pemesanan aktif atau langganan. | 1\. Pengguna sudah login. 2\. Memiliki metode pembayaran yang terhubung ke pemesanan mendatang. 3\. Coba hapus metode pembayaran tersebut. | Sistem mungkin menampilkan pesan peringatan bahwa metode pembayaran tidak dapat dihapus karena terkait dengan pemesanan aktif, atau meminta untuk menambahkan metode pembayaran lain terlebih dahulu. |  |  |

   

      6. ### ***Test Item: Riwayat pemesanan pengguna*** {#test-item:-riwayat-pemesanan-pengguna}

   Sistem harus menampilkan riwayat pemesanan pengguna (aktif, selesai, dibatalkan).

   Riwayat Pemesanan

   

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date |
| ----- | ----- | ----- | ----- | ----- | ----- |
| Test Item: Riwayat pemesanan pengguna |  |  |  |  |  |
| TC-USR-F-07 | Melihat daftar riwayat pemesanan (Perjalanan). | 1\. Pengguna sudah login. 2\. Klik menu "Perjalanan" atau navigasi ke bagian riwayat pemesanan. | Halaman "Perjalanan" ditampilkan, memperlihatkan daftar pemesanan yang akan datang, sebelumnya, dan dibatalkan (jika ada). Informasi ringkas setiap pemesanan (destinasi, tanggal, status) terlihat. |  |  |
| TC-USR-F-08 | Melihat detail pemesanan dari riwayat (pemesanan selesai). | 1\. Pengguna sudah login dan berada di halaman "Perjalanan". 2\. Pilih salah satu pemesanan yang sudah selesai ("Sebelumnya"). 3\. Klik untuk melihat detail. | Halaman detail pemesanan ditampilkan, berisi semua informasi terkait pemesanan tersebut (detail properti, tuan rumah, harga, tamu, tanda terima). |  |  |
| TC-USR-F-09 | Melihat detail pemesanan yang akan datang. | 1\. Pengguna sudah login dan berada di halaman "Perjalanan". 2\. Pilih salah satu pemesanan yang "Akan Datang". 3\. Klik untuk melihat detail. | Halaman detail pemesanan ditampilkan, berisi informasi relevan untuk perjalanan mendatang (alamat, info check-in, kontak tuan rumah, opsi untuk mengubah/membatalkan jika berlaku). |  |  |
| TC-USR-F-10 | Melihat riwayat pemesanan saat pengguna tidak memiliki pemesanan. | 1\. Pengguna baru sudah login dan belum pernah melakukan pemesanan. 2\. Navigasi ke halaman "Perjalanan". | Halaman "Perjalanan" menampilkan pesan bahwa pengguna belum memiliki perjalanan atau saran untuk mulai mencari tempat menginap. |  |  |
| TC-USR-F-11 | Memfilter riwayat pemesanan (jika ada filter, misalnya berdasarkan tahun). | 1\. Pengguna sudah login dan berada di halaman "Perjalanan" dengan banyak riwayat. 2\. Jika ada filter (misalnya, "Tahun"), pilih salah satu filter. | Daftar riwayat pemesanan diperbarui sesuai dengan filter yang dipilih. |  |  |
| TC-USR-F-12 | Mengakses tanda terima atau faktur dari riwayat pemesanan. | 1\. Pengguna sudah login dan berada di detail pemesanan yang sudah selesai. 2\. Cari opsi untuk melihat "Tanda Terima" atau "Faktur". 3\. Klik opsi tersebut. | Tanda terima atau faktur untuk pemesanan tersebut ditampilkan atau dapat diunduh, berisi rincian biaya. |  |  |

   

      7. ### ***Test Item: Pengelolaan notifikasi*** {#test-item:-pengelolaan-notifikasi}

   Scope: Sistem harus memungkinkan pengguna untuk mengelola preferensi notifikasi mereka.

   Scenario: Preferensi Notifikasi

   

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Test Item: Pengelolaan notifikasi |  |  |  |  |  |  |
| TC-USR-G-07 | Mengakses halaman pengaturan notifikasi. | 1\. Pengguna sudah login. 2\. Navigasi ke "Akun" \-\> "Notifikasi" atau "Pengaturan Notifikasi". | Halaman pengaturan notifikasi ditampilkan, memperlihatkan berbagai jenis notifikasi (misalnya, Email, SMS, Push) dan preferensi untuk masing-masing. |  |  |  |
| TC-USR-G-08 | Mengubah preferensi notifikasi email (misalnya, mengaktifkan/menonaktifkan notifikasi promosi). | 1\. Pengguna sudah login dan berada di halaman pengaturan notifikasi. 2\. Temukan bagian notifikasi Email. 3\. Cari opsi untuk "Promosi dan tips". 4\. Ubah statusnya (misalnya, dari aktif ke nonaktif). 5\. Simpan perubahan (jika ada tombol simpan, atau perubahan disimpan otomatis). | Preferensi notifikasi email untuk promosi berhasil diubah. Sistem akan berhenti (atau mulai) mengirim email promosi sesuai pengaturan. |  |  |  |

   

   3. ## **Detail Properti** {#detail-properti}

   

   

      1. ### ***Test Item: Penampilan galeri foto properti*** {#test-item:-penampilan-galeri-foto-properti}

   Scope: Sistem harus menampilkan galeri foto dari properti.

   Scenario: Detail Galeri Foto Properti

   

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result | Automated | Note |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Detail Properti |  |  |  |  |  |  |  |  |
| Test Item: Penampilan galeri foto properti |  |  |  |  |  |  |  |  |
| TC-DP-A-01 | Melihat galeri foto dengan beberapa gambar. | 1\. Pengguna sudah melakukan pencarian dan memilih satu properti dari hasil pencarian. 2\. Pengguna berada di halaman detail properti. 3\. Amati bagian galeri foto. 4\. Klik pada salah satu foto untuk membuka tampilan galeri penuh. 5\. Gunakan navigasi (panah/geser) untuk melihat foto berikutnya/sebelumnya. 6\. Tutup tampilan galeri penuh. | Galeri foto utama ditampilkan dengan jelas. Saat diklik, galeri tampilan penuh terbuka. Navigasi antar foto berfungsi dengan baik. Foto ditampilkan dengan kualitas baik. |  |  |  | FALSE |  |
| TC-DP-A-02 | Melihat galeri foto properti yang hanya memiliki satu gambar. | 1\. Temukan dan buka halaman detail properti yang diketahui hanya memiliki satu foto. 2\. Amati bagian galeri foto. 3\. Klik pada foto tersebut. | Satu foto ditampilkan. Saat diklik, foto tersebut mungkin ditampilkan lebih besar, tetapi tidak ada opsi navigasi ke foto lain. |  |  |  | FALSE |  |
| TC-DP-A-03 | Penampilan halaman detail properti yang tidak memiliki foto (jika dimungkinkan oleh sistem). | 1\. Temukan (jika ada) atau simulasikan kondisi properti tanpa foto di database. 2\. Buka halaman detail properti tersebut. | Sistem menampilkan placeholder standar untuk gambar, atau pesan "Tidak ada foto tersedia", atau area galeri foto tidak ditampilkan sama sekali. Halaman tetap termuat tanpa error. |  |  |  | FALSE |  |

   

      2. ### ***Test Item: Penampilan deskripsi lengkap properti*** {#test-item:-penampilan-deskripsi-lengkap-properti}

   Scope: Sistem harus menampilkan deskripsi lengkap properti yang disediakan oleh tuan rumah.

   Scenario: Deskripsi Properti

   

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date |
| ----- | ----- | ----- | ----- | ----- | ----- |
| Test Item: Penampilan deskripsi lengkap properti |  |  |  |  |  |
| TC-DP-B-01 | Menampilkan deskripsi properti yang lengkap. | 1\. Buka halaman detail properti. 2\. Cari bagian deskripsi properti. | Deskripsi properti yang ditulis oleh tuan rumah ditampilkan dengan jelas. |  |  |
| TC-DP-B-02 | Interaksi dengan "Baca selengkapnya" jika deskripsi panjang. | 1\. Buka halaman detail properti yang memiliki deskripsi panjang. 2\. Perhatikan apakah ada ringkasan deskripsi dan tautan/tombol "Baca selengkapnya" atau "Lihat lebih banyak". 3\. Klik tautan/tombol tersebut. | Awalnya, ringkasan deskripsi ditampilkan. Setelah mengklik "Baca selengkapnya", seluruh deskripsi properti akan terlihat. Mungkin ada opsi untuk "Tampilkan lebih sedikit" setelahnya. |  |  |
| TC-DP-B-03 | Penampilan deskripsi properti yang sangat pendek. | 1\. Temukan atau simulasikan properti dengan deskripsi sangat pendek (misalnya satu kalimat). 2\. Buka halaman detail properti tersebut. | Deskripsi pendek tersebut ditampilkan dengan benar tanpa masalah tata letak. Tautan "Baca selengkapnya" mungkin tidak ada jika deskripsi sudah sepenuhnya terlihat. |  |  |
| TC-DP-B-04 | Penampilan deskripsi properti yang tidak diisi oleh tuan rumah (kosong). | 1\. Temukan atau simulasikan properti dimana tuan rumah tidak mengisi deskripsi. 2\. Buka halaman detail properti tersebut. | Bagian deskripsi mungkin menampilkan pesan seperti "Tuan rumah belum memberikan deskripsi" atau bagian tersebut tidak ditampilkan sama sekali. Halaman tetap berfungsi tanpa error. |  |  |
| TC-DP-B-05 | Penampilan deskripsi properti dengan format khusus (paragraf, daftar poin). | 1\. Buka halaman detail properti yang deskripsinya menggunakan format seperti paragraf baru atau daftar poin. | Pemformatan teks (paragraf, daftar poin jika didukung) dalam deskripsi ditampilkan dengan benar, meningkatkan keterbacaan. |  |  |
| TC-DP-B-06 | Penampilan deskripsi yang berisi karakter spesial atau multibahasa. | 1\. Temukan atau simulasikan properti dengan deskripsi yang mengandung karakter spesial (misalnya &, é, ñ, @) atau teks dalam berbagai bahasa. 2\. Buka halaman detail properti. | Semua karakter spesial dan teks multibahasa ditampilkan dengan benar tanpa ada karakter yang rusak atau hilang. |  |  |

   

      3. ### ***Test Item: Penampilan detail spesifik properti*** {#test-item:-penampilan-detail-spesifik-properti}

   Scope: Sistem harus menampilkan detail spesifik properti (jumlah kamar tidur, kamar mandi, jenis tempat tidur).

   Scenario: Detail Spesifik Properti

   

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Test Item: Penampilan detail spesifik properti |  |  |  |  |  |  |
| TC-DP-C-01 | Menampilkan jumlah tamu, kamar tidur, tempat tidur, dan kamar mandi yang benar. | 1\. Buka halaman detail properti. 2\. Cari bagian ringkasan detail properti (biasanya di bagian atas atau di bawah judul). | Informasi akurat mengenai kapasitas tamu, jumlah kamar tidur, jumlah tempat tidur, dan jumlah kamar mandi ditampilkan dengan jelas (misalnya, "4 tamu · 2 kamar tidur · 2 tempat tidur · 1,5 kamar mandi"). |  |  |  |
| TC-DP-C-02 | Penampilan detail spesifik untuk properti tipe studio. | 1\. Buka halaman detail properti yang bertipe Studio. | Detail spesifik harus secara akurat mencerminkan tata letak studio (misalnya, "1 kamar tidur" atau "Studio", "1 tempat tidur", "1 kamar mandi"). |  |  |  |
| TC-DP-C-03 | Penampilan detail spesifik jika tuan rumah tidak mengisi semua informasi (misalnya, jenis tempat tidur). | 1\. Temukan atau simulasikan properti dimana tuan rumah tidak merinci jenis tempat tidur. 2\. Buka halaman detail properti. | mandi").TC\_DP\_SPEC\_003Penampilan detail spesifik jika tuan rumah tidak mengisi semua informasi (misalnya, jenis tempat tidur).1. Temukan atau simulasikan properti dimana tuan rumah tidak merinci jenis tempat tidur. 2\. Buka halaman detail properti.Sistem menangani data yang hilang dengan baik, misalnya dengan tidak menampilkan bagian "jenis tempat tidur" atau menampilkan pesan default seperti "Informasi tidak tersedia", tanpa menyebabkan error. |  |  |  |
| TC-DP-C-04 | Verifikasi konsistensi detail spesifik dengan informasi di filter pencarian. | 1\. Catat detail spesifik (misalnya, 2 kamar tidur) dari filter pencarian yang digunakan untuk menemukan properti. 2\. Buka halaman detail properti. 3\. Bandingkan detail spesifik yang ditampilkan dengan yang ada di filter. | Detail spesifik (jumlah kamar tidur, dll.) yang ditampilkan di halaman detail properti harus konsisten dengan kriteria yang digunakan saat pencarian dan yang ditampilkan di kartu properti pada hasil pencarian. |  |  |  |

   

      4. ### ***Test Item: Penampilan daftar fasilitas*** {#test-item:-penampilan-daftar-fasilitas}

   Scope: Sistem harus menampilkan daftar lengkap fasilitas yang tersedia di properti.

   Scenario: Daftar Fasilitas

   

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Test Item: Penampilan daftar fasilitas |  |  |  |  |  |  |
| TC-DP-D-01 | Menampilkan daftar fasilitas yang umum (misalnya, Wi-Fi, Dapur, AC). | 1\. Buka halaman detail properti. 2\. Cari bagian "Fasilitas" atau "Yang ditawarkan tempat ini". | Daftar fasilitas yang disediakan oleh tuan rumah ditampilkan. Ikon dan nama fasilitas jelas dan mudah dimengerti. |  |  |  |
| TC-DP-D-02 | Verifikasi ikon fasilitas sesuai dengan deskripsinya. | 1\. Buka halaman detail properti. 2\. Amati beberapa fasilitas yang tercantum beserta ikonnya. | Ikon yang ditampilkan di sebelah nama fasilitas harus relevan dan secara visual mewakili fasilitas tersebut (misalnya, ikon sinyal untuk Wi-Fi, ikon kepingan salju untuk AC). |  |  |  |

   

      5. ### ***Test Item: Penampilan kalender ketersediaan*** {#test-item:-penampilan-kalender-ketersediaan}

   Scope: Sistem harus menampilkan kalender ketersediaan properti secara real-time.

   Scenario: Kalender Ketersediaan

   

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result | Automated |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | :---: |
| Test Item: Penampilan kalender ketersediaan |  |  |  |  |  |  |  |
| TC-DP-E-01 | Menampilkan kalender ketersediaan dengan tanggal yang tersedia dan tidak tersedia. | 1\. Buka halaman detail properti. 2\. Cari bagian kalender ketersediaan. | Kalender ditampilkan dengan jelas. Tanggal yang tersedia dapat dipilih, sementara tanggal yang sudah dipesan atau diblokir oleh tuan rumah ditandai berbeda (misalnya, dicoret, berwarna abu-abu) dan tidak dapat dipilih. |  |  |  | FALSE |
| TC-DP-E-02 | Navigasi ke bulan berikutnya/sebelumnya pada kalender. | 1\. Buka halaman detail properti dan lihat kalender. 2\. Klik tombol panah untuk navigasi ke bulan berikutnya. 3\. Klik tombol panah untuk navigasi ke bulan sebelumnya. | Kalender berhasil menampilkan bulan berikutnya dan sebelumnya. Status ketersediaan tanggal di bulan-bulan tersebut juga ditampilkan dengan benar. |  |  |  | FALSE |
| TC-DP-E-03 | Penampilan kalender untuk properti yang sepenuhnya dipesan dalam waktu dekat. | 1\. Temukan properti yang diketahui sepenuhnya dipesan untuk beberapa bulan ke depan. 2\. Buka halaman detail properti dan lihat kalender. | Kalender menunjukkan semua tanggal dalam periode tersebut sebagai tidak tersedia. Pengguna masih bisa navigasi ke bulan-bulan berikutnya untuk mencari ketersediaan di masa mendatang. |  |  |  | FALSE |
| TC-DP-E-04 | Penampilan kalender untuk properti yang baru atau selalu tersedia. | 1\. Temukan properti yang baru atau memiliki ketersediaan luas. 2\. Buka halaman detail properti dan lihat kalender. | Sebagian besar atau semua tanggal di kalender ditampilkan sebagai tersedia. |  |  |  | FALSE |
| TC-DP-E-05 | Memilih rentang tanggal yang valid pada kalender untuk melihat harga. | 1\. Buka halaman detail properti. 2\. Di kalender, pilih tanggal check-in yang tersedia. 3\. Pilih tanggal check-out yang tersedia setelah tanggal check-in. | Tanggal yang dipilih disorot. Bagian rincian harga (jika ada di dekat kalender) diperbarui untuk mencerminkan total harga untuk rentang tanggal yang dipilih. |  |  |  | FALSE |
| TC-DP-E-06 | Mencoba memilih tanggal check-out sebelum tanggal check-in. | 1\. Buka halaman detail properti. 2\. Di kalender, pilih tanggal check-in yang tersedia. 3\. Coba pilih tanggal check-out sebelum tanggal check-in yang sudah dipilih. | Sistem seharusnya mencegah pemilihan ini. Tanggal sebelum check-in mungkin tidak aktif atau pesan error kecil muncul. |  |  |  | FALSE |
| TC-DP-E-07 | Mencoba memilih tanggal yang sudah tidak tersedia sebagai check-in atau check-out. | 1\. Buka halaman detail properti. 2\. Di kalender, identifikasi tanggal yang ditandai tidak tersedia. 3\. Coba klik tanggal yang tidak tersedia tersebut. | Tanggal yang tidak tersedia tidak dapat dipilih. Tidak ada perubahan pada rincian harga atau status pemesanan. |  |  |  | FALSE |

   

      6. ### ***Test Item: Penampilan total harga*** {#test-item:-penampilan-total-harga}

   Scope: Sistem harus menghitung dan menampilkan total harga untuk tanggal yang dipilih, termasuk harga per malam, biaya kebersihan, dan biaya layanan.

   Scenario: Perhitungan Harga Total

   

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Test Item: Penampilan total harga |  |  |  |  |  |  |
| TC-DP-F-01 | Menampilkan rincian harga setelah memilih tanggal dan jumlah tamu yang valid. | 1\. Buka halaman detail properti. 2\. Pilih tanggal check-in dan check-out yang valid dan tersedia dari kalender. 3\. Pastikan jumlah tamu sudah sesuai (jika bisa diubah di halaman ini). 4\. Amati bagian rincian harga. | Bagian rincian harga ditampilkan, mencakup: \- Harga per malam x jumlah malam. \- Biaya kebersihan (jika ada). \- Biaya layanan Airbnb. \- Pajak (jika berlaku). \- Total harga keseluruhan. Semua angka ditampilkan dengan benar. |  |  |  |
| TC-DP-F-02 | Rincian harga tidak ditampilkan atau menunjukkan pesan jika tanggal belum dipilih. | 1\. Buka halaman detail properti. 2\. Jangan pilih tanggal check-in atau check-out. 3\. Amati bagian rincian harga. | Bagian rincian harga mungkin menampilkan harga per malam dasar atau pesan yang meminta pengguna untuk memilih tanggal untuk melihat harga total. |  |  |  |
| TC-DP-F-03 | Perubahan harga total saat jumlah malam diubah. | 1\. Pilih tanggal check-in dan check-out awal (misalnya, 2 malam), catat total harga. 2\. Ubah tanggal check-out untuk menambah jumlah malam (misalnya, menjadi 4 malam). 3\. Amati kembali rincian harga. | Total harga diperbarui secara dinamis dan akurat berdasarkan perubahan jumlah malam. Komponen harga per malam x jumlah malam harus berubah sesuai. |  |  |  |
| TC-DP-F-04 | Penampilan harga jika ada diskon mingguan atau bulanan yang diterapkan. | 1\. Pilih rentang tanggal yang cukup panjang untuk memicu diskon mingguan/bulanan (jika properti menawarkannya). 2\. Amati rincian harga | Rincian harga harus secara jelas menunjukkan diskon yang diterapkan (misalnya, "Diskon mingguan \-RpXXX.XXX") dan total harga akhir sudah dikurangi diskon. |  |  |  |

   

      7. ### ***Test Item: Penampilan aturan rumah*** {#test-item:-penampilan-aturan-rumah}

   Scope: Sistem harus menampilkan aturan rumah yang ditetapkan oleh tuan rumah.

   Scenario: Aturan Rumah

   

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Test Item: Penampilan aturan rumah |  |  |  |  |  |  |
| TC-DP-G-01 | Menampilkan daftar aturan rumah yang ditetapkan tuan rumah. | 1\. Buka halaman detail properti. 2\. Cari bagian "Aturan Rumah" atau "Hal yang perlu diketahui". | Daftar aturan rumah ditampilkan dengan jelas (misalnya, "Dilarang merokok", "Tidak cocok untuk hewan peliharaan", "Pesta atau acara tidak diizinkan", "Waktu tenang setelah pukul 22:00"). |  |  |  |
| TC-DP-G-02 | Penampilan jika tuan rumah tidak menetapkan aturan rumah spesifik. | 1\. Temukan atau simulasikan properti dimana tuan rumah tidak menambahkan aturan rumah khusus (mungkin hanya aturan standar Airbnb). 2\. Buka halaman detail properti tersebut. | Bagian aturan rumah mungkin menampilkan aturan standar Airbnb atau pesan "Tuan rumah tidak menambahkan aturan khusus lainnya", atau hanya menampilkan aturan yang memang ada (misal jam check-in/check-out). Halaman tetap valid. |  |  |  |
| TC-DP-G-03 | Penampilan aturan terkait check-in/check-out. | 1\. Buka halaman detail properti. 2\. Verifikasi informasi jam check-in dan jam check-out di bagian aturan rumah atau sekitarnya. | Waktu spesifik untuk check-in (misalnya, "Setelah 15:00") dan check-out (misalnya, "Sebelum 11:00") ditampilkan dengan jelas. |  |  |  |

   

      8. ### ***Test Item: Penampilan kebijakan pembatalan properti***  {#test-item:-penampilan-kebijakan-pembatalan-properti}

   Scope: Sistem harus menampilkan kebijakan pembatalan properti.

   Scenario: Kebijakan Pembatalan

   

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Test Item: Penampilan kebijakan pembatalan properti |  |  |  |  |  |  |
| TC-DP-H-01 | Menampilkan ringkasan kebijakan pembatalan sebelum tanggal tertentu. | 1\. Buka halaman detail properti. 2\. Cari bagian "Kebijakan Pembatalan". 3\. Pilih tanggal check-in dan check-out (jika diperlukan agar kebijakan spesifik muncul). | Ringkasan kebijakan pembatalan yang berlaku untuk properti tersebut ditampilkan. Contoh: "Batalkan sebelum \[Tanggal & Waktu\] untuk mendapatkan pengembalian dana penuh." atau "Fleksibel", "Moderat", "Ketat" dengan penjelasan singkat. |  |  |  |
| TC-DP-H-02 | Mengklik untuk melihat detail lengkap kebijakan pembatalan. | 1\. Di bagian Kebijakan Pembatalan, klik tautan "Pelajari lebih lanjut" atau "Lihat detail" atau pada nama kebijakan itu sendiri. | Modal atau halaman baru/bagian yang diperluas terbuka, menampilkan penjelasan lengkap mengenai kebijakan pembatalan yang dipilih oleh tuan rumah, termasuk skenario pengembalian dana berdasarkan waktu pembatalan. |  |  |  |

   

      9. ### ***Test Item: Penampilan lokasi properti di peta*** {#test-item:-penampilan-lokasi-properti-di-peta}

   Scope: Sistem harus menampilkan lokasi properti di peta.

   Scenario: Lokasi Properti di Peta

   

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Test Item: Penampilan lokasi properti di peta |  |  |  |  |  |  |
| TC-DP-I-01 | Menampilkan peta dengan penanda perkiraan lokasi properti. | 1\. Buka halaman detail properti. 2\. Scroll ke bagian "Lokasi" atau "Temukan lokasi properti ini di peta". | Peta interaktif ditampilkan dengan area umum atau penanda yang menunjukkan perkiraan lokasi properti. Untuk alasan privasi, alamat pasti biasanya tidak ditampilkan sebelum pemesanan dikonfirmasi. |  |  |  |
| TC-DP-I-02 | Interaksi dengan peta (zoom in, zoom out, geser). | 1\. Di bagian peta, gunakan kontrol zoom (+/-) atau gestur pinch-to-zoom. 2\. Klik dan seret peta untuk menggeser tampilan. | Fungsi zoom in, zoom out, dan menggeser peta bekerja dengan lancar. |  |  |  |

   

      10. ### ***Test Item: Penampilan informasi profil tuan rumah*** {#test-item:-penampilan-informasi-profil-tuan-rumah}

   Scope: Sistem harus menampilkan informasi profil tuan rumah (nama, foto, rating, jumlah ulasan).

   Scenario: Informasi Profil Host

   

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Test Item: Penampilan informasi profil tuan rumah |  |  |  |  |  |  |
| TC-DP-J-01 | Menampilkan nama, foto profil, dan status Superhost (jika ada) tuan rumah. | 1\. Buka halaman detail properti. 2\. Cari bagian "Dikelola oleh \[Nama Tuan Rumah\]" atau "Tuan Rumah Anda". | Nama (biasanya nama depan) dan foto profil tuan rumah ditampilkan. Jika tuan rumah adalah Superhost, lencana Superhost juga ditampilkan dengan jelas. |  |  |  |
| TC-DP-J-02 | Menampilkan rating rata-rata dan jumlah ulasan untuk tuan rumah. | 1\. Di bagian informasi tuan rumah, perhatikan rating dan jumlah ulasan. | Rating bintang rata-rata tuan rumah (jika ada) dan total jumlah ulasan yang diterima tuan rumah ditampilkan (misalnya, "⭐ 4.92 · 150 Ulasan"). |  |  |  |
| TC-DP-J-03 | Mengklik nama atau foto tuan rumah untuk melihat profil lengkap tuan rumah. | 1\. Klik pada nama atau foto profil tuan rumah di halaman detail properti. | Pengguna diarahkan ke halaman profil publik lengkap tuan rumah, yang berisi informasi lebih detail seperti deskripsi diri tuan rumah, properti lain yang dikelola, dan semua ulasan tentang tuan rumah. |  |  |  |

   

      11. ### ***Test Item: Penampilan semua ulasan properti***  {#test-item:-penampilan-semua-ulasan-properti}

   Scope: Sistem harus menampilkan semua ulasan tamu untuk properti (teks ulasan, rating, nama tamu, tanggal).

   Scenario: Ulasan Tamu

   

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Test Item: Penampilan semua ulasan properti |  |  |  |  |  |  |
| TC-DP-K-01 | Menampilkan ringkasan rating keseluruhan dan rating per kategori (Kebersihan, Akurasi, dll.). | 1\. Buka halaman detail properti. 2\. Cari bagian "Ulasan" atau rating bintang di atas. | Rating bintang keseluruhan untuk properti ditampilkan (misalnya, "⭐ 4.87 · 230 ulasan"). Seringkali diikuti oleh rincian rating untuk kategori spesifik seperti Kebersihan, Akurasi, Check-in, Komunikasi, Lokasi, dan Nilai. |  |  |  |
| TC-DP-K-02 | Menampilkan daftar ulasan individual dari tamu. | 1\. Scroll ke bawah ke bagian ulasan. | Daftar ulasan dari tamu sebelumnya ditampilkan, masing-masing biasanya mencakup: \- Foto profil dan nama depan tamu. \- Tanggal ulasan. \- Teks ulasan. \- Rating bintang yang diberikan tamu tersebut (kadang-kadang). |  |  |  |
| TC-DP-K-03 | Penampilan properti yang belum memiliki ulasan. | 1\. Temukan atau simulasikan properti baru yang belum menerima ulasan. 2\. Buka halaman detail properti dan lihat bagian ulasan. | Bagian ulasan menampilkan pesan seperti "Belum ada ulasan" atau "Jadilah yang pertama mengulas tempat ini\!". |  |  |  |
| TC-DP-K-04 | Penampilan ulasan yang berisi balasan dari tuan rumah. | 1\. Cari ulasan yang memiliki balasan dari tuan rumah. | Jika tuan rumah membalas ulasan tamu, balasan tersebut ditampilkan di bawah ulasan tamu terkait, dengan identifikasi yang jelas bahwa itu adalah balasan dari tuan rumah. |  |  |  |

   

   

   4. ## **Review dan Rating** {#review-dan-rating}

      1. ### ***Test Item: Pemberian ulasan dan rating tamu*** {#test-item:-pemberian-ulasan-dan-rating-tamu}

   Scope: Sistem harus memungkinkan tamu untuk memberikan ulasan dan rating (bintang) untuk properti yang mereka inapi setelah check-out.

   Scenario: Ulasan dan Rating Tamu

   

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result | Automated | Note |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Review dan Rating |  |  |  |  |  |  |  |  |
| Test Item: Pemberian ulasan dan rating tamu |  |  |  |  |  |  |  |  |
| TC-RR-A-01 | Tamu memberikan ulasan publik, ulasan pribadi, dan rating bintang keseluruhan yang valid setelah check-out. | 1\. Tamu sudah login dan telah menyelesaikan masa inap di properti. 2\. Dalam periode waktu yang ditentukan (biasanya 14 hari setelah check-out), tamu menerima notifikasi atau membuka bagian "Ulasan Anda" / "Perjalanan". 3\. Pilih properti yang ingin diulas. 4\. Berikan rating bintang keseluruhan (misalnya 5 bintang). 5\. Tulis ulasan publik yang konstruktif. 6\. (Jika ada) Tulis catatan pribadi untuk tuan rumah. 7\. Berikan rating bintang untuk kategori spesifik (Kebersihan, Akurasi, dll.). 8\. Klik "Kirim Ulasan". | Ulasan dan rating berhasil dikirim. Sistem menampilkan pesan konfirmasi. Ulasan akan dipublikasikan sesuai aturan (misalnya, setelah tuan rumah juga mengulas atau setelah periode ulasan berakhir). Tamu tidak bisa mengedit ulasan publik setelah dikirim (tergantung kebijakan Airbnb). |  |  |  | FALSE |  |
| TC-RR-A-02 | memberikan ulasan tanpa memberikan rating bintang keseluruhan. | 1\. Ikuti langkah 1-3 pada TC\_REV\_GUEST\_001. 2\. Jangan pilih rating bintang keseluruhan. 3\. Isi kolom ulasan publik. 4\. Klik "Kirim Ulasan". | Sistem menampilkan pesan error yang menyatakan bahwa rating bintang keseluruhan wajib diisi. Ulasan tidak terkirim. |  |  |  | FALSE |  |
| TC-RR-A-03 | Tamu mencoba memberikan ulasan dengan teks ulasan publik kosong. | 1\. Ikuti langkah 1-3 pada TC\_REV\_GUEST\_001. 2\. Berikan rating bintang keseluruhan. 3\. Biarkan kolom ulasan publik kosong. 4\. Klik "Kirim Ulasan". | Sistem menampilkan pesan error yang menyatakan bahwa ulasan publik wajib diisi (atau memiliki panjang minimum). Ulasan tidak terkirim. |  |  |  | FALSE |  |

   

      2. ### ***Test Item: Pemberian ulasan dan rating tamu host*** {#test-item:-pemberian-ulasan-dan-rating-tamu-host}

   Scope: Sistem harus memungkinkan tuan rumah untuk memberikan ulasan dan rating untuk tamu setelah check-out.

   Scenario: Ulasan dan Rating Host

   

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Test Item: Pemberian ulasan dan rating tamu host |  |  |  |  |  |  |
| TC-RR-B-01 | Tuan rumah memberikan ulasan dan rating bintang keseluruhan yang valid untuk tamu. | 1\. Tuan rumah sudah login dan tamu telah check-out dari properti. 2\. Dalam periode waktu yang ditentukan (biasanya 14 hari setelah check-out tamu), tuan rumah menerima notifikasi atau membuka bagian "Ulasan Anda" / "Reservasi". 3\. Pilih tamu yang ingin diulas. 4\. Berikan rating bintang keseluruhan untuk tamu. 5\. Tulis ulasan tentang tamu. 6\. Jawab pertanyaan tambahan (misalnya, "Apakah Anda akan menerima tamu ini lagi?"). 7\. Klik "Kirim Ulasan". | Ulasan dan rating berhasil dikirim. Sistem menampilkan pesan konfirmasi. Ulasan akan dipublikasikan sesuai aturan (misalnya, setelah tamu juga mengulas atau setelah periode ulasan berakhir). Tuan rumah tidak bisa mengedit ulasan setelah dikirim (tergantung kebijakan Airbnb). |  |  |  |
| TC-RR-B-02 | Tuan rumah mencoba memberikan ulasan tanpa memberikan rating bintang keseluruhan untuk tamu. | 1\. Ikuti langkah 1-3 pada TC\_REV\_HOST\_001. 2\. Jangan pilih rating bintang keseluruhan. 3\. Isi kolom ulasan. 4\. Klik "Kirim Ulasan". | Sistem menampilkan pesan error yang menyatakan bahwa rating bintang keseluruhan wajib diisi. Ulasan tidak terkirim. |  |  |  |
| TC-RR-B-03 | Tuan rumah mencoba memberikan ulasan dengan teks ulasan kosong. | 1\. Ikuti langkah 1-3 pada TC\_REV\_HOST\_001. 2\. Berikan rating bintang keseluruhan. 3\. Biarkan kolom ulasan kosong. 4\. Klik "Kirim Ulasan". | Sistem menampilkan pesan error yang menyatakan bahwa ulasan wajib diisi (atau memiliki panjang minimum). Ulasan tidak terkirim. |  |  |  |

   

      3. ### ***Test Item: Publikasi ulasan dan rating*** {#test-item:-publikasi-ulasan-dan-rating}

   Scope: Sistem harus mempublikasikan ulasan setelah kedua belah pihak memberikan ulasan atau setelah periode waktu tertentu.

   Scenario: Publikasi Ulasan Setelah Kedua Belah Pihak Memberikan Ulasan

   

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Test Item: Publikasi ulasan dan rating |  |  |  |  |  |  |
| TC-RR-C-01 | Kedua belah pihak (tamu dan tuan rumah) memberikan ulasan dalam periode waktu yang ditentukan. | 1\. Tamu memberikan ulasan untuk properti dalam 14 hari setelah check-out. 2\. Tuan rumah memberikan ulasan untuk tamu dalam 14 hari setelah check-out tamu. 3\. Amati profil properti dan profil tamu setelah kedua ulasan dikirim. | Segera setelah kedua belah pihak mengirimkan ulasan mereka, kedua ulasan tersebut dipublikasikan secara bersamaan di profil properti (ulasan tamu) dan di profil tamu (ulasan tuan rumah). |  |  |  |
| TC-RR-C-02 | Tidak ada pihak yang memberikan ulasan dalam periode waktu yang ditentukan. | 1\. Tamu TIDAK memberikan ulasan untuk properti dalam 14 hari setelah check-out. 2\. Tuan rumah TIDAK memberikan ulasan untuk tamu dalam periode 14 hari. 3\. Amati profil properti dan profil tamu setelah periode 14 hari berakhir. | Tidak ada ulasan baru yang dipublikasikan di profil properti maupun di profil tamu terkait penginapan tersebut. |  |  |  |

5. ## **Customer Support** {#customer-support}

   1. ### ***Test Item: Pusat bantuan/FAQ*** {#test-item:-pusat-bantuan/faq}

   Scope: Sistem harus menyediakan pusat bantuan/FAQ yang komprehensif.

   Scenario: Dukungan Pelanggan 

   

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result | Automated | Note |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Customer Support |  |  |  |  |  |  |  |  |
| Test Item: Pusat bantuan/FAQ |  |  |  |  |  |  |  |  |
| TC-CS-A-01 | Mencari artikel bantuan menggunakan kata kunci yang relevan. | 1\. Di halaman Pusat Bantuan, masukkan kata kunci yang relevan di kotak pencarian (misalnya, "kebijakan pembatalan", "cara mengubah reservasi"). 2\. Tekan Enter atau klik tombol cari. | Halaman hasil pencarian ditampilkan, berisi daftar artikel bantuan yang relevan dengan kata kunci. Artikel yang paling relevan muncul di bagian atas. |  |  |  | FALSE |  |
| TC-CS-A-02 | Mencari artikel bantuan menggunakan kata kunci yang tidak relevan atau salah eja. | 1\. Di halaman Pusat Bantuan, masukkan kata kunci yang tidak relevan (misalnya, "resep kue") atau salah eja (misalnya, "pembataln"). 2\. Tekan Enter atau klik tombol cari. | Sistem menampilkan pesan "Tidak ada hasil ditemukan untuk '\[kata kunci\]'" atau menyarankan kata kunci alternatif/artikel yang mungkin mirip. Jika ada fitur koreksi ejaan, sistem mungkin menampilkan hasil untuk ejaan yang benar. |  |  |  | FALSE |  |
| TC-CS-A-03 | Membuka dan membaca artikel bantuan. | 1\. Dari hasil pencarian atau daftar kategori, klik judul salah satu artikel bantuan. | Isi lengkap artikel bantuan ditampilkan dengan jelas dan terstruktur (judul, paragraf, mungkin daftar poin atau gambar). Informasi mudah dibaca dan dipahami. |  |  |  | FALSE |  |
| TC-CS-A-04 | Mencoba mencari dengan kolom pencarian kosong. | 1\. Di halaman Pusat Bantuan, jangan masukkan teks apa pun di kolom pencarian. 2\. Klik tombol cari. | Tombol cari mungkin nonaktif, atau jika diklik, tidak ada tindakan yang terjadi, atau halaman menampilkan kembali saran pencarian umum/kategori populer. Tidak boleh ada error. |  |  |  | FALSE |  |

   

**Revision History**

| Version | Date | Summary of Changes | Handled by | Revision Marks(Yes/No) |
| ----- | ----- | ----- | ----- | ----- |
| 0.1 | 31/05/2025 | Initial creation | Kelompok F4 |  |
|  |  |  |  |  |
|  |  |  |  |  |

