

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

**[1\. Introduction	3](#introduction)**

[**2\. Scope	3**](#scope)

[**3\. Related Document	3**](#related-document)

[**4\. Traceability Matrix	3**](#traceability-matrix)

[**5\. Test Cases	5**](#test-cases)

[Ringkasan Pengujian	5](#ringkasan-pengujian)

[5.1 Pencarian dan Penemuan Properti (Search & Discovery)	6](#pencarian-dan-penemuan-properti-\(search-&-discovery\))

[5.1.1 Test Item: Pencarian properti berdasarkan lokasi	6](#test-item:-pencarian-properti-berdasarkan-lokasi)

[5.1.2 Test Item: Pencarian properti dengan filter tanggal	7](#test-item:-pencarian-properti-dengan-filter-tanggal)

[5.1.3 Test Item: Pencarian properti dengan filter jumlah dan jenis tamu	7](#test-item:-pencarian-properti-dengan-filter-jumlah-dan-jenis-tamu)

[5.1.4 Test Item: Pencarian properti dengan filter jenis properti	8](#test-item:-pencarian-properti-dengan-filter-jenis-properti)

[5.1.5 Test Item: Pencarian properti dengan filter rentang harga	8](#test-item:-pencarian-properti-dengan-filter-rentang-harga)

[5.1.6 Test Item: Pencarian properti dengan filter fasilitas	9](#test-item:-pencarian-properti-dengan-filter-fasilitas)

[5.1.7 Test Item: Pencarian properti dengan filter karakteristik khusus tambahan	9](#test-item:-pencarian-properti-dengan-filter-karakteristik-khusus-tambahan)

[5.1.8 Test Item: Pencarian properti dengan filter jumlah kamar tidur dan kamar mandi	10](#test-item:-pencarian-properti-dengan-filter-jumlah-kamar-tidur-dan-kamar-mandi)

[5.1.9 Test Item: Daftar keinginan pengguna	10](#heading=h.9ax789jbbis5)

[5.2 User Management	12](#user-management)

[5.2.1 Test Item: Pendaftaran akun	12](#test-item:-pendaftaran-akun)

[5.2.2 Test Item: Masuk akun	13](#test-item:-masuk-akun)

[5.2.3 Test Item: Lupa kata sandi	15](#heading=h.sk1wmlzdulx1)

[5.2.4 Test Item: Pengeditan profil	16](#test-item:-pengeditan-profil)

[5.2.5 Test Item: Pengelolaan metode pembayaran	18](#test-item:-pengelolaan-metode-pembayaran)

[5.2.6 Test Item: Riwayat pemesanan pengguna	19](#test-item:-riwayat-pemesanan-pengguna)

[5.2.7 Test Item: Pengelolaan notifikasi	20](#test-item:-pengelolaan-notifikasi)

[5.3 Detail Properti	22](#detail-properti)

[5.3.1 Test Item: Penampilan galeri foto properti	22](#test-item:-penampilan-galeri-foto-properti)

[5.3.2 Test Item: Penampilan deskripsi lengkap properti	22](#test-item:-penampilan-deskripsi-lengkap-properti)

[5.3.3 Test Item: Penampilan detail spesifik properti	23](#test-item:-penampilan-detail-spesifik-properti)

[5.3.4 Test Item: Penampilan daftar fasilitas	24](#test-item:-penampilan-daftar-fasilitas)

[5.3.5 Test Item: Penampilan kalender ketersediaan	25](#test-item:-penampilan-kalender-ketersediaan)

[5.3.6 Test Item: Penampilan total harga	26](#test-item:-penampilan-total-harga)

[5.3.7 Test Item: Penampilan aturan rumah	27](#test-item:-penampilan-aturan-rumah)

[5.3.8 Test Item: Penampilan kebijakan pembatalan properti	28](#test-item:-penampilan-kebijakan-pembatalan-properti)

[5.3.9 Test Item: Penampilan lokasi properti di peta	28](#test-item:-penampilan-lokasi-properti-di-peta)

[5.3.10 Test Item: Penampilan informasi profil tuan rumah	29](#test-item:-penampilan-informasi-profil-tuan-rumah)

[5.3.11 Test Item: Penampilan semua ulasan properti	30](#test-item:-penampilan-semua-ulasan-properti)

[5.3.12 Test Item: Publikasi ulasan dan rating	32](#heading=h.g2kwmg82ojtx)

[5.4 Customer Support	33](#customer-support)

[5.4.1 Test Item: Pusat bantuan/FAQ	33](#test-item:-pusat-bantuan/faq)

**Airbnb Test Case**

1. # **Introduction** {#introduction}

   Tujuan dari dokumen *Test Case* ini adalah guna menentukan dan mengomunikasikan kondisi spesifik yang perlu divalidasi untuk memungkinkan penilaian sistem. *Test Case* didasari oleh banyak hal tetapi mostly mencakup *Use Case*, *performance characteristics*, dan risiko yang menjadi perhatian proyek.

2. # **Scope** {#scope}

   Pengujian ditujukan untuk memverifikasi bahwa fitur-fitur pada website Airbnb bekerja dengan sesuai. Fitur-fitur pada website Airbnb yang akan dites adalah:

1. Pencarian dan Penemuan Properti (Search & Discovery)  
2. User Management  
3. Detail Properti  
4. Customer Support

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
| FR-CS01 | Test item 5.4.1 |
| FR-CS02 | Test item 5.4.2 |
| FR-CS03 | Test item 5.4.3 |

   

5. # **Test Cases** {#test-cases}

## Ringkasan Pengujian {#ringkasan-pengujian}

| Airbnb TEST CASE |  |  |  |
| ----- | ----- | :---: | :---: |
| System Name | Airbnb 25.22 |  |  |
| Document ID | TCE01 \- Export to excel |  |  |
| Test Case | SUMMARY OF ALL |  |  |
| Pass | 43 | Pending | 10 |
| Fail | 3 | Number of test cases: | 80 |
| Test Case | Pencarian dan Penemuan Properti (Search & Discovery) |  |  |
| Pass | 0 | Pending | 0 |
| Fail | 0 | Number of test cases: | 0 |
| Test Case | User Management |  |  |
| Pass | 0 | Pending | 0 |
| Fail | 0 | Number of test cases: | 0 |
| Test Case | Detail Properti |  |  |
| Pass | 0 | Pending | 0 |
| Fail | 0 | Number of test cases: | 0 |
| Test Case | Customer Support |  |  |
| Pass | 0 | Pending | 0 |
| Fail | 0 | Number of test cases: | 0 |

1. ## **Pencarian dan Penemuan Properti (Search & Discovery)** {#pencarian-dan-penemuan-properti-(search-&-discovery)}

| Airbnb TEST CASE |  |  |  |
| ----- | ----- | :---: | ----: |
| System Name | Airbnb 25.22 |  |  |
| Document ID | TCE01 \- Export to excel |  |  |
| Test Case | Pencarian dan Penemuan Properti (Search & Discovery) |  |  |
| Pass | 12 | Pending | 0 |
| Fail | 1 | Number of test cases: | 16 |

   1. ### ***Test Item: Pencarian properti berdasarkan lokasi*** {#test-item:-pencarian-properti-berdasarkan-lokasi}

   Scope: Sistem harus memungkinkan pengguna untuk mencari properti berdasarkan lokasi (kota, negara bagian, negara, alamat spesifik, atau penunjuk di peta).

   Scenario: Pencarian Properti Berdasarkan Lokasi

   

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result | Automated | Note |
| ----- | ----- | ----- | ----- | ----- | :---: | :---: | :---: | ----- |
| Test Item: Pencarian properti berdasarkan lokasi |  |  |  |  |  |  |  |  |
| TC-CP-A-01 | Pencarian properti dengan nama kota yang valid. | 1\. Buka halaman utama Airbnb. 2\. Masukkan "Bandung" di kolom "Ke mana?" 3\. Klik tombol "Cari". | Sistem menampilkan daftar properti yang tersedia di Kyoto. | Hasil pencarian di kota Bandung | 02/06/2025 | Pass | TRUE |  |
| TC-CP-A-02 | Pencarian properti dengan nama negara yang valid. | 1\. Buka halaman utama Airbnb. 2\. Masukkan "Malaysia" di kolom "Ke mana?". 3\. Klik tombol "Cari". | Sistem menampilkan daftar properti yang tersedia di berbagai kota di Italia, atau peta Italia dengan penanda properti. | Hasil pencarian di negara Malaysia | 02/06/2025 | Pass | TRUE |  |
| TC-CP-A-05 | Pencarian properti dengan input kosong pada kolom lokasi. | 1\. Buka halaman utama Airbnb. 2\. Biarkan kolom "Ke mana?" kosong. 3\. Klik tombol "Cari" (jika aktif). | Tombol "Cari" nonaktif, atau muncul pesan error yang meminta pengguna memasukkan destinasi. | Hasil pencarian ditampilkan tanpa kata kunci apapun | 02/06/2025 | Pass | TRUE |  |

   

      2. ### ***Test Item: Pencarian properti dengan filter tanggal*** {#test-item:-pencarian-properti-dengan-filter-tanggal}

   Scope: Sistem harus memungkinkan pengguna untuk memfilter hasil pencarian berdasarkan tanggal check-in dan check-out.

   Scenario: Filter Tanggal Check-in dan Check-out

   

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result | Automated | Note |
| ----- | ----- | ----- | ----- | ----- | :---: | :---: | :---: | ----- |
| Test Item: Pencarian properti dengan filter tanggal |  |  |  |  |  |  |  |  |
| TC-CP-B-01 | Filter pencarian dengan rentang tanggal check-in dan check-out yang valid. | 1\. Lakukan pencarian awal berdasarkan lokasi (misalnya "Bali"). 2\. Di halaman hasil pencarian, klik filter tanggal. 3\. Pilih tanggal check-in dan check-out yang valid dan tersedia. 4\. Klik "Terapkan" atau "Simpan". | Hasil pencarian diperbarui, hanya menampilkan properti yang tersedia pada rentang tanggal yang dipilih. | Hasil pencarian dengan properti yang tersedia | 02/06/2025 | Pass | TRUE |  |

   

      3. ### ***Test Item: Pencarian properti dengan filter jumlah dan jenis tamu*** {#test-item:-pencarian-properti-dengan-filter-jumlah-dan-jenis-tamu}

   Scope: Sistem harus memungkinkan pengguna untuk memfilter berdasarkan jumlah tamu (dewasa, anak-anak, bayi).

   Scenario: Filter Jumlah Tamu

   

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result | Automated | Note |
| ----- | ----- | ----- | ----- | ----- | :---: | :---: | :---: | ----- |
| Test Item: Pencarian properti dengan filter jumlah dan jenis tamu |  |  |  |  |  |  |  |  |
| TC-CP-C-02 | Filter dengan jumlah dewasa, anak-anak, dan bayi yang valid. | 1\. Lakukan pencarian awal. 2\. Klik filter "Tamu". 3\. Atur jumlah dewasa "2", anak-anak "1", bayi "1". 4\. Klik "Terapkan". | Hasil pencarian diperbarui, menampilkan properti yang dapat mengakomodasi kombinasi tamu tersebut. | Hasil pencarian ditampilkan dengan filter properti yang tersedia untuk dewasa, anak-anak, dan bayi | 02/06/2025 | Pass | TRUE |  |
| TC-CP-C-05 | Menambah jumlah bayi tanpa adanya tamu dewasa. | 1\. Lakukan pencarian awal. 2\. Klik filter "Tamu". 3\. Atur jumlah dewasa menjadi "0" (jika memungkinkan) atau biarkan "1" lalu coba kurangi. 4\. Atur jumlah bayi menjadi "1". 5\. Klik "Terapkan". | Sistem seharusnya mensyaratkan minimal satu tamu dewasa jika ada bayi atau anak-anak. Pesan error ditampilkan. | Filter akan menambahkan secara otomatis bagian orang dewasa sebanyak 1 orang | 02/06/2025 | Pass | TRUE |  |

   

      4. ### ***Test Item: Pencarian properti dengan filter jenis properti*** {#test-item:-pencarian-properti-dengan-filter-jenis-properti}

   Scope: Sistem harus memungkinkan pengguna untuk memfilter berdasarkan jenis properti (seluruh rumah/apartemen, kamar pribadi, kamar bersama).

   Scenario: Filter Jenis Properti

   

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result | Automated | Note |
| ----- | ----- | ----- | ----- | ----- | :---: | :---: | :---: | ----- |
| Test Item: Pencarian properti dengan filter jenis properti |  |  |  |  |  |  |  |  |
| TC-CP-D-02 | Filter dengan memilih beberapa jenis properti (misalnya, "Rumah" dan "Apartemen"). | 1\. Lakukan pencarian awal. 2\. Klik filter "Jenis Tempat". 3\. Pilih "Rumah". 4\. Pilih "Apartemen". 5\. Klik "Tampilkan hasil". | Hasil pencarian diperbarui dan menampilkan properti yang berjenis "Rumah" ATAU "Vila". | Hasil pencarian ditampilkan dengan filter properti rumah dan apartemen | 02/06/2025 | Pass | TRUE |  |

   

      5. ### ***Test Item: Pencarian properti dengan filter rentang harga*** {#test-item:-pencarian-properti-dengan-filter-rentang-harga}

   Scope: Sistem harus memungkinkan pengguna untuk memfilter berdasarkan rentang harga per malam.

   Scenario: Filter Rentang Harga

   

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result | Automated | Note |
| ----- | ----- | ----- | ----- | ----- | :---: | :---: | :---: | ----- |
| Test Item: Pencarian properti dengan filter rentang harga |  |  |  |  |  |  |  |  |
| TC-CP-E-02 | Filter dengan rentang harga minimum dan maksimum yang valid. | 1\. Lakukan pencarian awal. 2\. Klik filter "Harga". 3\. Atur harga minimum (misalnya Rp 500.000). 4\. Atur harga maksimum (misalnya Rp 1.000.000). 5\. Klik "Tampilkan hasil" atau "Simpan". | Hasil pencarian diperbarui, hanya menampilkan properti dengan harga per malam dalam rentang yang dipilih. | Hasil pencarian ditampilkan properti dengan rentang harga 500.000 hingga 1000000 | 02/06/2025 | Pass | TRUE |  |
| TC-CP-E-04 | Filter hanya dengan harga minimum. | 1\. Lakukan pencarian awal. 2\. Klik filter "Harga". 3\. Atur harga minimum (misalnya Rp 500.000). 4\. Biarkan harga maksimum pada nilai default tertinggi atau kosong. 5\. Klik "Tampilkan hasil". | Hasil pencarian diperbarui, menampilkan properti dengan harga per malam sama dengan atau lebih besar dari harga minimum yang dipilih. | Hasil pencarian ditampilkan properti dengan harga minimal 500.000 | 02/06/2025 | Pass | TRUE |  |

   

      6. ### ***Test Item: Pencarian properti dengan filter fasilitas*** {#test-item:-pencarian-properti-dengan-filter-fasilitas}

   Scope: Sistem harus memungkinkan pengguna untuk memfilter berdasarkan fasilitas (misalnya, Wi-Fi, dapur, kolam renang, parkir gratis, AC, mesin cuci).

   Scenario: Filter Fasilitas

   

| Test Item: Pencarian properti dengan filter fasilitas |  |  |  |  |  |  |  |  |
| ----- | ----- | ----- | ----- | ----- | :---: | :---: | :---: | ----- |
| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result | Automated | Note |
| TC-CP-F-01 | Filter dengan memilih satu fasilitas penting (misalnya, "Wi-Fi"). | 1\. Lakukan pencarian awal. 2\. Buka bagian filter, temukan "Fasilitas". 3\. Pilih "Wi-Fi". 4\. Klik "Tampilkan hasil". | Hasil pencarian diperbarui dan hanya menampilkan properti yang menyediakan fasilitas Wi-Fi. | Hasil pencarian ditampilkan properti dengan fasilitas wifi | 02/06/2025 | Pass | TRUE |  |

   

      7. ### ***Test Item: Pencarian properti dengan filter karakteristik khusus tambahan*** {#test-item:-pencarian-properti-dengan-filter-karakteristik-khusus-tambahan}

   Scope: Sistem harus memungkinkan pengguna untuk memfilter berdasarkan karakteristik khusus (misalnya, ramah hewan peliharaan, aksesibilitas kursi roda, sarapan gratis).

   Scenario: Filter Karakteristik Khusus

   

| Test Item: Pencarian properti dengan filter karakteristik khusus tambahan |  |  |  |  |  |  |  |  |
| ----- | ----- | ----- | ----- | ----- | :---: | :---: | :---: | ----- |
| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result | Automated | Note |
| TC-CP-G-01 | Filter dengan memilih satu karakteristik khusus (misalnya, "Boleh bawa hewan peliharaan") | 1\. Lakukan pencarian awal. 2\. Buka bagian filter, temukan opsi seperti "Aturan Rumah" atau "Fitur Tambahan". 3\. Pilih "Boleh bawa hewan peliharaan". 4\. Klik "Tampilkan hasil". | Hasil pencarian diperbarui dan hanya menampilkan properti yang memperbolehkan hewan peliharaan. | Hasil pencarian ditampilkan properti dengan fasilitas "Boleh bawa hewan peliharaan" | 02/06/2025 | Pass | TRUE |  |

   

      8. ### ***Test Item: Pencarian properti dengan filter jumlah kamar tidur dan kamar mandi*** {#test-item:-pencarian-properti-dengan-filter-jumlah-kamar-tidur-dan-kamar-mandi}

   Scope: Sistem harus memungkinkan pengguna untuk memfilter berdasarkan jumlah kamar tidur dan kamar mandi.

   Scenario: Filter Jumlah Kamar Tidur dan Kamar Mandi

   

| Test Item: Pencarian properti dengan filter jumlah kamar tidur dan kamar mandi |  |  |  |  |  |  |  |  |
| ----- | ----- | ----- | ----- | ----- | :---: | :---: | :---: | ----- |
| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result | Automated | Note |
| TC-CP-H-03 | Filter dengan jumlah kamar tidur dan kamar mandi tertentu. | 1\. Lakukan pencarian awal. 2\. Buka filter relevan. 3\. Pilih "2" untuk kamar tidur. 4\. Klik "Tampilkan hasil". | Hasil pencarian diperbarui, menampilkan properti dengan minimal 2 kamar tidur. | Hasil pencarian ditampilkan properti yang menyediakan 2 kamar tidur | 02/06/2025 | Pass | TRUE |  |

   

      9. ### ***Test Item: Pencarian properti dalam bentuk daftar dan peta***

   Scope: Sistem harus menampilkan pencarian properti dalam bentuk daftar dan peta.

   Scenario: 

   

| Test Item: Pencarian properti dalam bentuk daftar dan peta |  |  |  |  |  |  |  |  |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | :---: | ----- |
| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result | Automated | Note |
| TC-CP-I-01 | Verifikasi tampilan peta dari daftar hasil pencarian standar. | 1\. Lakukan pencarian properti dengan kriteria apa pun. 2\. lihat dalam bentuk peta | Menampilkan peta dengan titik lokasi-lokasi penginapan | Menampilkan peta dengan titik lokasi-lokasi penginapan | 06/06/2025 | Pass | TRUE |  |
| TC-CP-I-02 | Verifikasi pagination pada tampilan daftar (jika hasil banyak). | 1\. Lakukan pencarian yang menghasilkan banyak properti. 2\. Scroll ke bawah halaman. 3\. Cari dan klik tombol "Berikutnya" atau nomor halaman. | Daftar properti di halaman berikutnya ditampilkan. Tombol pagination berfungsi dengan benar (maju, mundur, ke halaman spesifik). | daftar ditampilkan sesuai filter, tombol pagination berfungsi | 06/06/2025 | Pass | TRUE |  |

   

      10. ### ***Test Item: Penampilan informasi pencarian ringkas***

   Scope: Sistem harus menampilkan informasi yang sesuai pada card, termasuk gambar utama, lokasi, harga per malam, rating ulasan, jumlah ulasan

   Scenario:

   

| Test Item: Penampilan informasi pencarian ringkas |  |  |  |  |  |  |  |  |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | :---: | ----- |
| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result | Automated | Note |
| TC-CP-J-01 | Verifikasi tampilan gambar utama, lokasi, harga per malam, rating ulasan, jumlah ulasan | 1\. Lakukan pencarian properti. 2\. Amati setiap item daftar di hasil pencarian. | Setiap item daftar menampilkan setidaknya satu foto utama properti yang representatif. | Setiap card menampilkan foto, nama, harga, lokasi, namun tidak ada rating | 06/06/2025 | Fail | TRUE |  |

   

      11. ### ***Test Item: Daftar keinginan pengguna***

   Scope: Sistem harus menyediakan fitur "Daftar Keinginan" (Wishlist) agar pengguna dapat menyimpan properti.

   Scenario: Fitur Daftar Keinginan (Wishlist)

   

| Test Item: Daftar keinginan pengguna |  |  |  |  |  |  |  |  |
| ----- | ----- | ----- | ----- | ----- | :---: | :---: | :---: | ----- |
| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result | Automated | Note |
| TC-CP-K-01 | Menambahkan properti ke daftar keinginan baru dari halaman hasil pencarian. | 1\. Pengguna sudah login. 2\. Lakukan pencarian properti. 3\. Pada salah satu item properti di hasil pencarian, klik ikon hati (❤) atau "Simpan". 4\. Saat diminta membuat daftar keinginan baru, masukkan nama "Liburan Impian". 5\. Klik "Buat". | Properti berhasil ditambahkan ke daftar keinginan baru "Liburan Impian". Ikon hati menjadi terisi. Notifikasi sukses muncul. | Berhasil membuat list "Liburan Impian" dan menambahkan properti yang ditandai ke list "Liburan Impian" | 02/06/2025 | Pass | TRUE |  |
| TC-CP-K-02 | Menambahkan properti ke daftar keinginan yang sudah ada. | 1\. Pengguna sudah login dan memiliki setidaknya satu daftar keinginan. 2\. Lakukan pencarian properti. 3\. Klik ikon hati pada properti lain. 4\. Pilih daftar keinginan yang sudah ada dari daftar yang muncul. | Properti berhasil ditambahkan ke daftar keinginan yang dipilih. Ikon hati menjadi terisi. | Berhasil menambah properti ke list "Liburan Impian" | 02/06/2025 | Pass | TRUE |  |
| TC-CP-K-03 | Melihat daftar keinginan. | 1\. Pengguna sudah login. 2\. Klik menu profil pengguna. 3\. Pilih opsi "Daftar Keinginan" atau "Simpanan". | Halaman daftar keinginan ditampilkan, memperlihatkan semua daftar keinginan yang telah dibuat pengguna beserta properti di dalamnya. | Berhasil melihat isi list "Liburan Impian | 02/06/2025 | Pass | TRUE |  |

   

   

   

   

   

   

   

   2. ## **User Management** {#user-management}

| Airbnb TEST CASE |  |  |  |
| ----- | ----- | :---: | ----: |
| System Name | Airbnb 25.22 |  |  |
| Document ID | TCE01 \- Export to excel |  |  |
| Test Case | User Management |  |  |
| Pass | 21 | Pending | 10 |
| Fail | 1 | Number of test cases: | 32 |

      1. ### ***Test Item: Pendaftaran akun*** {#test-item:-pendaftaran-akun}

   Scope: Sistem harus memungkinkan pengguna untuk mendaftar akun baru menggunakan email, Google, Facebook, atau Apple ID.

   Scenario: Registrasi Pengguna baru

   

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result | Automated | Note |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| User Management |  |  |  |  |  |  |  |  |
| Test Item: Pendaftaran akun |  |  |  |  |  |  |  |  |
| TC-USR-A-01 | Pendaftaran akun baru dengan semua informasi valid. | 1\. Buka halaman utama Airbnb. 2\. Klik tombol "Daftar". 3\. Pilih metode pendaftaran (misalnya, "Lanjutkan dengan email"). 4\. Isi semua kolom wajib (Nama Depan, Nama Belakang, Tanggal Lahir, Email, Kata Sandi) dengan data yang valid dan unik. 5\. Setujui Syarat & Ketentuan. 6\. Klik tombol "Setuju dan lanjutkan" atau "Daftar". | Pengguna berhasil masuk. Pengguna diarahkan ke halaman utama atau dashboard. Profil pengguna (nama/foto) ditampilkan. | Mendapatkan notifikasi berhasil mendaftar Akun | 2025/6/2 | Pass | TRUE |  |
| TC-USR-A-02 | Pendaftaran akun dengan email yang sudah terdaftar. | 1\. Buka halaman utama Airbnb. 2\. Klik tombol "Daftar". 3\. Pilih metode pendaftaran dengan email. 4\. Isi semua kolom wajib dengan data valid, namun gunakan alamat email yang sudah terdaftar di Airbnb. 5\. Klik tombol "Daftar". | Sistem menampilkan pesan error "Kata sandi salah" atau "Email atau kata sandi Anda salah." Pengguna tetap di halaman masuk. | Mendapatkan notifikasi berhasil mendaftar Akun | 2025/6/3 | Pass | TRUE |  |
| TC-USR-A-03 | Pendaftaran akun dengan kolom wajib tidak diisi. | 1\. Buka halaman utama Airbnb. 2\. Klik tombol "Daftar". 3\. Pilih metode pendaftaran dengan email. 4\. Biarkan salah satu kolom wajib (misalnya, Nama Belakang) kosong. 5\. Isi kolom lainnya. 6\. Klik tombol "Daftar". | Sistem menampilkan pesan error yang menunjukkan bahwa kolom tersebut wajib diisi. Pendaftaran gagal. | Berhasil mendaftar walaupun Lastname tidak di isi | 2025/6/4 | Pass | TRUE |  |
| TC-USR-A-06 | Pendaftaran menggunakan akun pihak ketiga (misalnya Google/Facebook). | 1\. Buka halaman utama Airbnb. 2\. Klik tombol "Daftar". 3\. Pilih opsi "Lanjutkan dengan Google" (atau Facebook, Apple). 4\. Ikuti alur otentikasi dari penyedia pihak ketiga. 5\. Setujui izin yang diminta Airbnb. | Akun berhasil dibuat menggunakan detail dari akun pihak ketiga. Pengguna diarahkan ke halaman profil atau halaman utama dalam keadaan login. | Dapat mendaftar dengan akun pihak ketiga seperti google | 2025/6/5 | Pass | TRUE |  |

   

   

      2. ### ***Test Item: Masuk akun*** {#test-item:-masuk-akun}

   Scope: Sistem harus memungkinkan pengguna untuk masuk (login) ke akun mereka.

   Scenario: Login Pengguna

   

   

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result |
| ----- | ----- | ----- | ----- | ----- |
| Test Item: Masuk akun |  |  |  |  |
| TC-USR-B-01 | Masuk dengan no telepon dan kata sandi yang valid. | 1\. Buka halaman utama Airbnb. 2\. Klik tombol "Masuk". 3\. Pilih opsi "Masuk dengan nomor telepon". 4\. Masukkan nomor telepon yang terdaftar dan valid. 5\. Klik tombol "Lanjutkan". 6\. Masukkan kode OTP yang dikirim melalui SMS. 7\. Klik tombol "Verifikasi". | Pengguna berhasil masuk. Pengguna diarahkan ke halaman utama atau dashboard.. | Pengguna berhasil masuk. Pengguna diarahkan ke halaman utama atau dashboard.. |
| TC-USR-B-02 | Masuk dengan nomor telepon valid tetapi OTP salah | 1\. Buka halaman utama Airbnb. 2\. Klik tombol "Masuk". 3\. Pilih opsi "Masuk dengan nomor telepon". 4\. Masukkan nomor telepon yang terdaftar dan valid. 5\. Klik tombol "Lanjutkan". 6\. Masukkan kode OTP yang salah. 7\. Klik tombol "Verifikasi". | Sistem menampilkan pesan error seperti "Kode OTP salah" atau "Kode verifikasi tidak valid." Pengguna tetap di halaman verifikasi OTP. | Menampilkan pesan eror karena kode otp tidak sesuai |
| TC-USR-B-03 | Masuk dengan nomor telepon yang tidak terdaftar | 1\. Buka halaman utama Airbnb. 2\. Klik tombol "Masuk". 3\. Pilih opsi "Masuk dengan nomor telepon". 4\. Masukkan nomor telepon yang tidak terdaftar. 5\. Klik tombol "Lanjutkan". | Sistem menampilkan pesan error seperti "Nomor telepon tidak terdaftar". Pengguna tidak menerima OTP dan tetap di halaman login. | Tetap bisa masuk dan menerima kode OTP |
| TC-USR-B-04 | Masuk dengan membiarkan kolom no telepon kosong. | 1\. Buka halaman utama Airbnb. 2\. Klik tombol "Masuk". 3\. Pilih opsi "Masuk dengan nomor telepon". 4\. Biarkan kolom nomor telepon kosong. 5\. Klik tombol "Lanjutkan". | Sistem menampilkan pesan error "Silakan masukkan nomor telepon". Tombol mungkin dinonaktifkan sampai nomor diisi.  | pesan error "Silakan masukkan nomor telepon" |
| TC-USR-B-06 | Masuk menggunakan akun pihak ketiga (misalnya Google/Facebook). | 1\. Buka halaman utama Airbnb. 2\. Klik tombol "Masuk". 3\. Pilih opsi "Lanjutkan dengan Google", Facebook, atau Apple. 4\. Ikuti proses otentikasi dari penyedia pihak ketiga. | Pengguna berhasil masuk menggunakan akun pihak ketiga. Pengguna diarahkan ke halaman utama atau dashboard. | Dapat masuk dengan akun pihak ketiga seperti google |

      3. ### ***Test Item: Pengeditan profil*** {#test-item:-pengeditan-profil}

   Scope: Sistem harus memungkinkan pengguna untuk mengedit profil mereka (nama, foto profil, deskripsi diri, nomor telepon).

   Scenario: Edit Profil Pengguna

   

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date |
| ----- | ----- | ----- | ----- | ----- | ----- |
| Test Item: Pengeditan profil |  |  |  |  |  |
| TC-USR-C-07 | Mengedit informasi pribadi (misalnya, Nama, Tanggal Lahir, Jenis Kelamin) dengan data valid. | 1\. Pengguna sudah login. 2\. Navigasi ke halaman "Akun" atau "Profil". 3\. Pilih "Informasi pribadi". 4\. Klik "Edit" pada bagian yang ingin diubah (misalnya, Nama). 5\. Ubah informasi dengan data valid. 6\. Klik "Simpan". | Sistem menampilkan pesan error bahwa Nama Depan wajib diisi. Perubahan tidak disimpan. | Berhasil mengedit data pribadi |  |
| TC-USR-D-08 | Mencoba mengedit informasi pribadi dengan data tidak valid (misalnya, nama kosong). | 1\. Pengguna sudah login dan berada di halaman edit informasi pribadi. 2\. Hapus isi kolom Nama Depan. 3\. Klik "Simpan". | Sistem menampilkan pesan error bahwa Nama Depan wajib diisi. Perubahan tidak disimpan. | Berhasil menyimpan walaupun isian kosong |  |
| TC-USR-D-09 | Mengubah alamat email dengan email baru yang valid dan belum terdaftar. | 1\. Pengguna sudah login dan berada di halaman edit informasi pribadi. 2\. Klik "Edit" pada bagian alamat email. 3\. Masukkan alamat email baru yang valid dan belum terdaftar. 4\. Mungkin diminta memasukkan kata sandi saat ini. 5\. Klik "Simpan" atau "Lanjutkan". | Perubahan email berhasil disimpan. Sistem mungkin mengirim email verifikasi ke alamat email baru. Setelah verifikasi (jika ada), email di profil diperbarui. | Berhasil Mengubah alamat email dengan email baru yang valid dan belum terdaftar. |  |
| TC-USR-D-10 | Mencoba mengubah alamat email dengan email yang sudah terdaftar. | 1\. Pengguna sudah login dan berada di halaman edit informasi pribadi. 2\. Klik "Edit" pada bagian alamat email. 3\. Masukkan alamat email yang sudah digunakan oleh akun Airbnb lain. 4\. Klik "Simpan". | Sistem menampilkan pesan error bahwa alamat email tersebut sudah digunakan. Perubahan tidak disimpan. | Gagal Mencoba mengubah alamat email dengan email yang sudah terdaftar. |  |
| TC-USR-D-11 | Mengubah nomor telepon dengan nomor yang valid. | 1\. Pengguna sudah login dan berada di halaman edit informasi pribadi. 2\. Klik "Tambah" atau "Edit" pada bagian nomor telepon. 3\. Masukkan nomor telepon yang valid. 4\. Mungkin ada proses verifikasi via SMS. 5\. Klik "Simpan" atau "Verifikasi". | Nomor telepon berhasil ditambahkan/diperbarui dan diverifikasi (jika ada). Nomor telepon ditampilkan di profil. | Berhasil Mengubah nomor telepon dengan nomor yang valid. |  |
| TC-USR-D-12 | Mencoba menyimpan nomor telepon dengan format tidak valid. | 1\. Pengguna sudah login dan berada di halaman edit nomor telepon. 2\. Masukkan nomor telepon dengan format salah (misalnya, "abcde" atau terlalu banyak/sedikit digit). 3\. Klik "Simpan". | Sistem menampilkan pesan error bahwa format nomor telepon tidak valid. Perubahan tidak disimpan. | Mmeberikan pesannomor telepon dengan format tidak valid. |  |
| TC-USR-D-13 | Mengunggah atau mengubah foto profil. | 1\. Pengguna sudah login dan berada di halaman "Profil" atau "Akun". 2\. Klik opsi untuk mengedit atau menambah foto profil. 3\. Pilih file gambar dengan format yang didukung (JPG, PNG) dan ukuran sesuai. 4\. Unggah dan sesuaikan (jika ada opsi crop). 5\. Simpan. | Foto profil berhasil diunggah/diperbarui dan ditampilkan di halaman profil pengguna dan di tempat lain yang relevan (misalnya, ulasan). | Berhasil menambahkan foto profil |  |
| TC-USR-D-14 | Mencoba mengunggah foto profil dengan format tidak didukung atau ukuran terlalu besar. | 1\. Pengguna sudah login dan berada di halaman edit foto profil. 2\. Coba unggah file dengan format tidak didukung (misalnya, .txt, .gif jika tidak didukung) atau file gambar yang ukurannya melebihi batas. | Sistem menampilkan pesan error bahwa format file tidak didukung atau ukuran file terlalu besar. Foto tidak terunggah. | Sistem hanya mengenali file dengan format yang mendukung |  |
| TC-USR-D-15 | Menambahkan atau mengedit bagian "Tentang Saya". | 1\. Pengguna sudah login dan berada di halaman "Profil". 2\. Klik "Edit profil". 3\. Cari bagian "Tentang Saya" atau bio. 4\. Masukkan atau edit teks deskripsi diri. 5\. Klik "Simpan". | Informasi "Tentang Saya" berhasil disimpan dan ditampilkan di profil publik pengguna. | Bisa mengedit atau menambahkan about |  |

   

      4. ### ***Test Item: Pengelolaan metode pembayaran*** {#test-item:-pengelolaan-metode-pembayaran}

   Scope: Sistem harus memungkinkan pengguna untuk menambahkan dan mengelola metode pembayaran yang valid.

   Scenario: Manajemen Metode Pembayaran

   

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date |
| ----- | ----- | ----- | ----- | ----- | ----- |
| Test Item: Pengelolaan metode pembayaran |  |  |  |  |  |
| TC-USR-D-07 | Menambahkan metode pembayaran baru (kartu kredit) dengan detail valid. | 1\. Pengguna sudah login. 2\. Navigasi ke "Akun" \-\> "Pembayaran & payout". 3\. Klik "Tambahkan metode pembayaran". 4\. Pilih "Kartu kredit atau debit". 5\. Masukkan detail kartu yang valid (nomor kartu, tanggal kedaluwarsa, CVV, nama pada kartu, alamat penagihan). 6\. Klik "Tambahkan kartu". | Metode pembayaran berhasil ditambahkan dan muncul di daftar metode pembayaran pengguna. Mungkin ada verifikasi kecil (otorisasi sejumlah kecil). |  |  |
| TC-USR-E-08 | Mencoba menambahkan kartu kredit dengan nomor kartu tidak valid. | 1\. Pengguna sudah login dan berada di halaman tambah metode pembayaran. 2\. Masukkan nomor kartu kredit yang tidak valid (misalnya, kurang digit, format salah). 3\. Isi detail lain. 4\. Klik "Tambahkan kartu". | Sistem menampilkan pesan error bahwa nomor kartu tidak valid. Metode pembayaran tidak ditambahkan. | Memberkan pesan eror There was an error adding your payment method. |  |
| TC-USR-E-09 | Mencoba menambahkan kartu kredit dengan tanggal kedaluwarsa di masa lalu. | 1\. Pengguna sudah login dan berada di halaman tambah metode pembayaran. 2\. Masukkan tanggal kedaluwarsa kartu yang sudah lewat. 3\. Isi detail lain. 4\. Klik "Tambahkan kartu". | Sistem menampilkan pesan error bahwa tanggal kedaluwarsa tidak valid atau kartu sudah kedaluwarsa. Metode pembayaran tidak ditambahkan. | Menampilkan pesan eror untuk mengecek kemabli tanggal kartu |  |
| TC-USR-E-10 | Mencoba menambahkan kartu kredit dengan CVV tidak valid (misalnya, string). | 1\. Pengguna sudah login dan berada di halaman tambah metode pembayaran. 2\. Masukkan CVV berupa string "abc" (jika input memungkinkan) atau jumlah digit salah. 3\. Isi detail lain. 4\. Klik "Tambahkan kartu". | Sistem menampilkan pesan error bahwa CVV tidak valid. Metode pembayaran tidak ditambahkan. Input field CVV seharusnya hanya menerima angka. | Tidak bisa memasukan string harus angka |  |
| TC-USR-E-11 | Menghapus metode pembayaran yang sudah ada. | 1\. Pengguna sudah login dan berada di "Pembayaran & payout". 2\. Temukan metode pembayaran yang ingin dihapus. 3\. Klik opsi "Hapus" atau ikon titik tiga lalu "Hapus". 4\. Konfirmasi penghapusan. | Metode pembayaran berhasil dihapus dari daftar. |  |  |
| TC-USR-E-12 | Mengatur satu metode pembayaran sebagai metode default (jika ada fitur). | 1\. Pengguna sudah login dan memiliki lebih dari satu metode pembayaran. 2\. Navigasi ke "Pembayaran & payout". 3\. Pilih metode pembayaran yang ingin dijadikan default. 4\. Klik opsi "Jadikan default". | Metode pembayaran yang dipilih berhasil ditetapkan sebagai default dan ditandai demikian. |  |  |
| TC-USR-E-13 | Mencoba menghapus metode pembayaran yang sedang terkait dengan pemesanan aktif atau langganan. | 1\. Pengguna sudah login. 2\. Memiliki metode pembayaran yang terhubung ke pemesanan mendatang. 3\. Coba hapus metode pembayaran tersebut. | Sistem mungkin menampilkan pesan peringatan bahwa metode pembayaran tidak dapat dihapus karena terkait dengan pemesanan aktif, atau meminta untuk menambahkan metode pembayaran lain terlebih dahulu. |  |  |

   

      5. ### ***Test Item: Riwayat pemesanan pengguna*** {#test-item:-riwayat-pemesanan-pengguna}

   Sistem harus menampilkan riwayat pemesanan pengguna (aktif, selesai, dibatalkan).

   Riwayat Pemesanan

   

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date |
| ----- | ----- | ----- | ----- | ----- | ----- |
| Test Item: Riwayat pemesanan pengguna |  |  |  |  |  |
| TC-USR-E-07 | Melihat daftar riwayat pemesanan (Perjalanan). | 1\. Pengguna sudah login. 2\. Klik menu "Perjalanan" atau navigasi ke bagian riwayat pemesanan. | Halaman "Perjalanan" ditampilkan, memperlihatkan daftar pemesanan yang akan datang, sebelumnya, dan dibatalkan (jika ada). Informasi ringkas setiap pemesanan (destinasi, tanggal, status) terlihat. |  |  |
| TC-USR-F-08 | Melihat detail pemesanan dari riwayat (pemesanan selesai). | 1\. Pengguna sudah login dan berada di halaman "Perjalanan". 2\. Pilih salah satu pemesanan yang sudah selesai ("Sebelumnya"). 3\. Klik untuk melihat detail. | Halaman detail pemesanan ditampilkan, berisi semua informasi terkait pemesanan tersebut (detail properti, tuan rumah, harga, tamu, tanda terima). |  |  |
| TC-USR-F-09 | Melihat detail pemesanan yang akan datang. | 1\. Pengguna sudah login dan berada di halaman "Perjalanan". 2\. Pilih salah satu pemesanan yang "Akan Datang". 3\. Klik untuk melihat detail. | Halaman detail pemesanan ditampilkan, berisi informasi relevan untuk perjalanan mendatang (alamat, info check-in, kontak tuan rumah, opsi untuk mengubah/membatalkan jika berlaku). |  |  |
| TC-USR-F-10 | Melihat riwayat pemesanan saat pengguna tidak memiliki pemesanan. | 1\. Pengguna baru sudah login dan belum pernah melakukan pemesanan. 2\. Navigasi ke halaman "Perjalanan". | Halaman "Perjalanan" menampilkan pesan bahwa pengguna belum memiliki perjalanan atau saran untuk mulai mencari tempat menginap. |  |  |
| TC-USR-F-11 | Memfilter riwayat pemesanan (jika ada filter, misalnya berdasarkan tahun). | 1\. Pengguna sudah login dan berada di halaman "Perjalanan" dengan banyak riwayat. 2\. Jika ada filter (misalnya, "Tahun"), pilih salah satu filter. | Daftar riwayat pemesanan diperbarui sesuai dengan filter yang dipilih. |  |  |
| TC-USR-F-12 | Mengakses tanda terima atau faktur dari riwayat pemesanan. | 1\. Pengguna sudah login dan berada di detail pemesanan yang sudah selesai. 2\. Cari opsi untuk melihat "Tanda Terima" atau "Faktur". 3\. Klik opsi tersebut. | Tanda terima atau faktur untuk pemesanan tersebut ditampilkan atau dapat diunduh, berisi rincian biaya. |  |  |

   

      6. ### ***Test Item: Pengelolaan notifikasi*** {#test-item:-pengelolaan-notifikasi}

   Scope: Sistem harus memungkinkan pengguna untuk mengelola preferensi notifikasi mereka.

   Scenario: Preferensi Notifikasi

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result |
| ----- | ----- | ----- | ----- | ----- | ----- | :---: |
| Test Item: Pengelolaan notifikasi |  |  |  |  |  |  |
| TC-USR-F-07 | Mengakses halaman pengaturan notifikasi. | 1\. Pengguna sudah login. 2\. Navigasi ke "Akun" \-\> "Notifikasi" atau "Pengaturan Notifikasi". | Halaman pengaturan notifikasi ditampilkan, memperlihatkan berbagai jenis notifikasi (misalnya, Email, SMS, Push) dan preferensi untuk masing-masing. | Pengguna berhasil masuk pada halaman notifikasi | 2025/6/9 | Pass |

   

   

   

   3. ## **Detail Properti** {#detail-properti}

| Airbnb TEST CASE |  |  |  |
| ----- | ----- | :---: | ----: |
| System Name | Airbnb 25.22 |  |  |
| Document ID | TCE01 \- Export to excel |  |  |
| Test Case | Detail Properti |  |  |
| Pass | 27 | Pending | 0 |
| Fail | 1 | Number of test cases: | 28 |

      1. ### ***Test Item: Penampilan galeri foto properti*** {#test-item:-penampilan-galeri-foto-properti}

   Scope: Sistem harus menampilkan galeri foto dari properti.

   Scenario: Detail Galeri Foto Properti

   

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result | Automated | Note |
| ----- | ----- | ----- | ----- | ----- | :---: | :---: | :---: | ----- |
| Detail Properti |  |  |  |  |  |  |  |  |
| Test Item: Penampilan galeri foto properti |  |  |  |  |  |  |  |  |
| TC-DP-A-01 | Melihat galeri foto dengan beberapa gambar. | 1\. Pengguna sudah memilih satu properti . 2\. Pengguna berada di halaman detail properti. 3\. Amati bagian galeri foto. 4\. Klik pada salah satu foto untuk membuka tampilan galeri penuh. 5\. Gunakan navigasi (panah/geser) untuk melihat foto berikutnya/sebelumnya. 6\. Tutup tampilan galeri penuh. | Galeri foto utama ditampilkan dengan jelas. Saat diklik, galeri tampilan penuh terbuka. Navigasi antar foto berfungsi dengan baik. Foto ditampilkan dengan kualitas baik. | menampilkan seluruh galeri foto | 02/06/25 | Pass | TRUE |  |

   

      2. ### ***Test Item: Penampilan deskripsi lengkap properti*** {#test-item:-penampilan-deskripsi-lengkap-properti}

   Scope: Sistem harus menampilkan deskripsi lengkap properti yang disediakan oleh tuan rumah.

   Scenario: Deskripsi Properti

   

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result | Automated | Note |
| ----- | ----- | ----- | ----- | ----- | :---: | :---: | :---: | ----- |
| Test Item: Penampilan deskripsi lengkap properti |  |  |  |  |  |  |  |  |
| TC-DP-B-01 | Menampilkan deskripsi properti yang lengkap. | 1\. Buka halaman detail properti. 2\. Cari bagian deskripsi properti. | Deskripsi properti yang ditulis oleh tuan rumah ditampilkan dengan jelas. | deskripsi lengkap | 02/06/25 | Pass | TRUE |  |
| TC-DP-B-02 | Interaksi dengan "Baca selengkapnya" jika deskripsi panjang. | 1\. Buka halaman detail properti yang memiliki deskripsi panjang. 2\. Perhatikan apakah ada ringkasan deskripsi dan tautan/tombol "Baca selengkapnya" atau "Lihat lebih banyak". 3\. Klik tautan/tombol tersebut. | Awalnya, ringkasan deskripsi ditampilkan. Setelah mengklik "Baca selengkapnya", seluruh deskripsi properti akan terlihat. Mungkin ada opsi untuk "Tampilkan lebih sedikit" setelahnya. | menampilkan detail ketika klik tampilkan lebih banyak | 02/07/25 | Pass | TRUE |  |
| TC-DP-B-03 | Penampilan deskripsi properti dengan format khusus (paragraf, daftar poin). | 1\. Buka halaman detail properti yang deskripsinya menggunakan format seperti paragraf baru atau daftar poin. | Pemformatan teks (paragraf, daftar poin jika didukung) dalam deskripsi ditampilkan dengan benar, meningkatkan keterbacaan. | menampilkan deskripsi dengan format khusus tanpa typo | 02/08/25 | Pass | TRUE |  |
| TC-DP-B-04 | Penampilan deskripsi yang berisi karakter spesial atau multibahasa. | 1\. Temukan atau simulasikan properti dengan deskripsi yang mengandung karakter spesial (misalnya &, é, ñ, @) atau teks dalam berbagai bahasa. 2\. Buka halaman detail properti. | Semua karakter spesial dan teks multibahasa ditampilkan dengan benar tanpa ada karakter yang rusak atau hilang. | menampilkan laman dengan bahasa asli | 02/09/25 | Pass | TRUE |  |

   

      3. ### ***Test Item: Penampilan detail spesifik properti*** {#test-item:-penampilan-detail-spesifik-properti}

   Scope: Sistem harus menampilkan detail spesifik properti (jumlah kamar tidur, kamar mandi, jenis tempat tidur).

   Scenario: Detail Spesifik Properti

   

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result | Automated | Note |
| ----- | ----- | ----- | ----- | ----- | :---: | :---: | :---: | ----- |
| Test Item: Penampilan detail spesifik properti |  |  |  |  |  |  |  |  |
| TC-DP-C-01 | Menampilkan jumlah tamu, kamar tidur, tempat tidur, dan kamar mandi yang benar. | 1\. Buka halaman detail properti. 2\. Cari bagian ringkasan detail properti (biasanya di bagian atas atau di bawah judul). | Informasi akurat mengenai kapasitas tamu, jumlah kamar tidur, jumlah tempat tidur, dan jumlah kamar mandi ditampilkan dengan jelas (misalnya, "4 tamu · 2 kamar tidur · 2 tempat tidur · kamar mandi bebas"). | detail spesifik properti ditampilkan | 02/10/25 | Pass | TRUE |  |
| TC-DP-C-02 | Verifikasi konsistensi detail spesifik dengan informasi di filter pencarian. | 1\. Catat detail spesifik (misalnya, 2 kamar tidur) dari filter pencarian yang digunakan untuk menemukan properti. 2\. Buka halaman detail properti. 3\. Bandingkan detail spesifik yang ditampilkan dengan yang ada di filter. | Detail spesifik (jumlah kamar tidur, dll.) yang ditampilkan di halaman detail properti harus konsisten dengan kriteria yang digunakan saat pencarian dan yang ditampilkan di kartu properti pada hasil pencarian. | menampilkan properti dengan jumlah 2 kamar tidur, 2 tempat tidur (seharusnya filter 4 tempat tidur) | 02/09/25 | Fail | TRUE |  |

   

      4. ### ***Test Item: Penampilan daftar fasilitas*** {#test-item:-penampilan-daftar-fasilitas}

   Scope: Sistem harus menampilkan daftar lengkap fasilitas yang tersedia di properti.

   Scenario: Daftar Fasilitas

   

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result | Automated | Note |
| ----- | ----- | ----- | ----- | ----- | :---: | :---: | :---: | ----- |
| Test Item: Penampilan daftar fasilitas |  |  |  |  |  |  |  |  |
| TC-DP-D-01 | Menampilkan daftar fasilitas yang umum (misalnya, Wi-Fi, Dapur, AC). | 1\. Buka halaman detail properti. 2\. Cari bagian "Fasilitas" atau "Yang ditawarkan tempat ini". | Daftar fasilitas yang disediakan oleh tuan rumah ditampilkan. Ikon dan nama fasilitas jelas dan mudah dimengerti. | fasilitas umum tertampil dengan baik | 02/09/25 | Pass | TRUE |  |
| TC-DP-D-02 | Verifikasi ikon fasilitas sesuai dengan deskripsinya. | 1\. Buka halaman detail properti. 2\. Amati beberapa fasilitas yang tercantum beserta ikonnya. | Ikon yang ditampilkan di sebelah nama fasilitas harus relevan dan secara visual mewakili fasilitas tersebut (misalnya, ikon sinyal untuk Wi-Fi, ikon kepingan salju untuk AC). | icon yang digunakan menggambarkan dan sesuai | 02/10/25 | Pass | TRUE |  |

   

      5. ### ***Test Item: Penampilan kalender ketersediaan*** {#test-item:-penampilan-kalender-ketersediaan}

   Scope: Sistem harus menampilkan kalender ketersediaan properti secara real-time.

   Scenario: Kalender Ketersediaan

   

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result | Automated | Note |
| ----- | ----- | ----- | ----- | ----- | :---: | :---: | :---: | ----- |
| Test Item: Penampilan kalender ketersediaan |  |  |  |  |  |  |  |  |
| TC-DP-E-01 | Menampilkan kalender ketersediaan dengan tanggal yang tersedia dan tidak tersedia. | 1\. Buka halaman detail properti. 2\. Cari bagian kalender ketersediaan. | Kalender ditampilkan dengan jelas. Tanggal yang tersedia dapat dipilih, sementara tanggal yang sudah dipesan atau diblokir oleh tuan rumah ditandai berbeda (misalnya, dicoret, berwarna abu-abu) dan tidak dapat dipilih. | kalender menampilkan tanggal yang tersedia dan tidak | 02/09/25 | Pass | TRUE |  |
| TC-DP-E-02 | Navigasi ke bulan berikutnya/sebelumnya pada kalender. | 1\. Buka halaman detail properti dan lihat kalender. 2\. Klik tombol panah untuk navigasi ke bulan berikutnya. 3\. Klik tombol panah untuk navigasi ke bulan sebelumnya. | Kalender berhasil menampilkan bulan berikutnya dan sebelumnya. Status ketersediaan tanggal di bulan-bulan tersebut juga ditampilkan dengan benar. | bisa melakukan navigasi ke bulan berikutnya dan sebelumnya | 02/10/25 | Pass | TRUE |  |
| TC-DP-E-05 | Memilih rentang tanggal yang valid pada kalender untuk melihat harga. | 1\. Buka halaman detail properti. 2\. Di kalender, pilih tanggal check-in yang tersedia. 3\. Pilih tanggal check-out yang tersedia setelah tanggal check-in. | Tanggal yang dipilih disorot. Bagian rincian harga (jika ada di dekat kalender) diperbarui untuk mencerminkan total harga untuk rentang tanggal yang dipilih. | tanggal yang dipilih punya warna berbeda | 02/11/25 | Pass | TRUE |  |
| TC-DP-E-06 | Mencoba memilih tanggal check-out sebelum tanggal check-in. | 1\. Buka halaman detail properti. 2\. Di kalender, pilih tanggal check-in yang tersedia. 3\. Coba pilih tanggal check-out sebelum tanggal check-in yang sudah dipilih. | Sistem seharusnya mencegah pemilihan ini. Tanggal sebelum check-in mungkin tidak aktif atau pesan error kecil muncul. | memiliki isian default, sehingga tanggal check-in selalu ada dan diberi "minimum 2 malam" jarak dari tanggal checkin | 02/12/25 | Pass | TRUE |  |
| TC-DP-E-07 | Mencoba memilih tanggal yang sudah tidak tersedia sebagai check-in atau check-out. | 1\. Buka halaman detail properti. 2\. Di kalender, identifikasi tanggal yang ditandai tidak tersedia. 3\. Coba klik tanggal yang tidak tersedia tersebut. | Tanggal yang tidak tersedia tidak dapat dipilih. Tidak ada perubahan pada rincian harga atau status pemesanan. | tanggal tidak tersedia tidak bisa di klik | 02/13/25 | Pass | TRUE |  |

   

      6. ### ***Test Item: Penampilan total harga*** {#test-item:-penampilan-total-harga}

   Scope: Sistem harus menghitung dan menampilkan total harga untuk tanggal yang dipilih, termasuk harga per malam, biaya kebersihan, dan biaya layanan.

   Scenario: Perhitungan Harga Total

   

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result | Automated | Note |
| ----- | ----- | ----- | ----- | ----- | :---: | :---: | :---: | ----- |
| Test Item: Penampilan total harga |  |  |  |  |  |  |  |  |
| TC-DP-F-01 | Menampilkan rincian harga setelah memilih tanggal dan jumlah tamu yang valid. | 1\. Buka halaman detail properti. 2\. Pilih tanggal check-in dan check-out yang valid dan tersedia dari kalender. 3\. Pastikan jumlah tamu sudah sesuai (jika bisa diubah di halaman ini). 4\. Amati bagian rincian harga. | Bagian rincian harga ditampilkan, mencakup: \- Harga per malam x jumlah malam. \- Biaya kebersihan (jika ada). \- Biaya layanan Airbnb. \- Pajak (jika berlaku). \- Total harga keseluruhan. Semua angka ditampilkan dengan benar. | harga muncul pada laman berikutnya setelah tanggal dan jumlah diisi | 02/09/25 | Pass | TRUE |  |
| TC-DP-F-02 | Rincian harga tidak ditampilkan atau menunjukkan pesan jika tanggal belum dipilih. | 1\. Buka halaman detail properti. 2\. Jangan pilih tanggal check-in atau check-out. 3\. Amati bagian rincian harga. | Bagian rincian harga mungkin menampilkan harga per malam dasar atau pesan yang meminta pengguna untuk memilih tanggal untuk melihat harga total. | selalu ada tanggal default sehingga harga langsung munul | 02/10/25 | Pass | TRUE |  |
| TC-DP-F-03 | Perubahan harga total saat jumlah malam diubah. | 1\. Pilih tanggal check-in dan check-out awal (misalnya, 2 malam), catat total harga. 2\. Ubah tanggal check-out untuk menambah jumlah malam (misalnya, menjadi 4 malam). 3\. Amati kembali rincian harga. | Total harga diperbarui secara dinamis dan akurat berdasarkan perubahan jumlah malam. Komponen harga per malam x jumlah malam harus berubah sesuai. | harga berubah ketika jumlah inap berubah | 02/11/25 | Pass | TRUE |  |

   

   

      7. ### ***Test Item: Penampilan aturan rumah*** {#test-item:-penampilan-aturan-rumah}

   Scope: Sistem harus menampilkan aturan rumah yang ditetapkan oleh tuan rumah.

   Scenario: Aturan Rumah

   

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result | Automated | Note |
| ----- | ----- | ----- | ----- | ----- | :---: | :---: | :---: | ----- |
| Test Item: Penampilan aturan rumah |  |  |  |  |  |  |  |  |
| TC-DP-G-01 | Menampilkan daftar aturan rumah yang ditetapkan tuan rumah. | 1\. Buka halaman detail properti. 2\. Cari bagian "Aturan Rumah" atau "Hal yang perlu diketahui". | Daftar aturan rumah ditampilkan dengan jelas (misalnya, "Dilarang merokok", "Tidak cocok untuk hewan peliharaan", "Pesta atau acara tidak diizinkan", "Waktu tenang setelah pukul 22:00"). | menampilkan peraturan rumah oleh host pada akhir laman | 02/11/25 | Pass | TRUE |  |
| TC-DP-G-03 | Penampilan aturan terkait check-in/check-out. | 1\. Buka halaman detail properti. 2\. Verifikasi informasi jam check-in dan jam check-out di bagian aturan rumah atau sekitarnya. | Waktu spesifik untuk check-in (misalnya, "Setelah 15:00") dan check-out (misalnya, "Sebelum 11:00") ditampilkan dengan jelas. | terdapat pada peraturan rumah | 02/12/25 | Pass | TRUE |  |

   

      8. ### ***Test Item: Penampilan kebijakan pembatalan properti***  {#test-item:-penampilan-kebijakan-pembatalan-properti}

   Scope: Sistem harus menampilkan kebijakan pembatalan properti.

   Scenario: Kebijakan Pembatalan

   

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result | Automated | Note |
| ----- | ----- | ----- | ----- | ----- | :---: | :---: | :---: | ----- |
| Test Item: Penampilan kebijakan pembatalan properti |  |  |  |  |  |  |  |  |
| TC-DP-H-01 | Menampilkan ringkasan kebijakan pembatalan sebelum tanggal tertentu. | 1\. Buka halaman detail properti. 2\. Cari bagian "Kebijakan Pembatalan". 3\. Pilih tanggal check-in dan check-out (jika diperlukan agar kebijakan spesifik muncul). | Ringkasan kebijakan pembatalan yang berlaku untuk properti tersebut ditampilkan. Contoh: "Batalkan sebelum \[Tanggal & Waktu\] untuk mendapatkan pengembalian dana penuh." atau "Fleksibel", "Moderat", "Ketat" dengan penjelasan singkat. | kebijakan pembatan ditampilkan melalui pop up | 02/12/25 | Pass | TRUE |  |
| TC-DP-H-02 | Mengklik untuk melihat detail lengkap kebijakan pembatalan. | 1\. Di bagian Kebijakan Pembatalan, klik tautan "Pelajari lebih lanjut" atau "Lihat detail" atau pada nama kebijakan itu sendiri. | Modal atau halaman baru/bagian yang diperluas terbuka, menampilkan penjelasan lengkap mengenai kebijakan pembatalan yang dipilih oleh tuan rumah, termasuk skenario pengembalian dana berdasarkan waktu pembatalan. | tombol detail berfungsi | 02/13/25 | Pass | TRUE |  |

   

      9. ### ***Test Item: Penampilan lokasi properti di peta*** {#test-item:-penampilan-lokasi-properti-di-peta}

   Scope: Sistem harus menampilkan lokasi properti di peta.

   Scenario: Lokasi Properti di Peta

   

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result | Automated | Note |
| ----- | ----- | ----- | ----- | ----- | :---: | :---: | :---: | ----- |
| Test Item: Penampilan lokasi properti di peta |  |  |  |  |  |  |  |  |
| TC-DP-I-01 | Menampilkan peta dengan penanda perkiraan lokasi properti. | 1\. Buka halaman detail properti. 2\. Scroll ke bagian "Lokasi" atau "Temukan lokasi properti ini di peta". | Peta interaktif ditampilkan dengan area umum atau penanda yang menunjukkan perkiraan lokasi properti. Untuk alasan privasi, alamat pasti biasanya tidak ditampilkan sebelum pemesanan dikonfirmasi. | lokasi properti ditampilkan di peta dengan tepat | 02/12/25 | Pass | TRUE |  |
| TC-DP-I-02 | Interaksi dengan peta (zoom in, zoom out, geser). | 1\. Di bagian peta, gunakan kontrol zoom (+/-) atau gestur pinch-to-zoom. 2\. Klik dan seret peta untuk menggeser tampilan. | Fungsi zoom in, zoom out, dan menggeser peta bekerja dengan lancar. | peta dapat di geser, zoom in, dan zoom out | 02/13/25 | Pass | TRUE |  |

   

      10. ### ***Test Item: Penampilan informasi profil tuan rumah*** {#test-item:-penampilan-informasi-profil-tuan-rumah}

   Scope: Sistem harus menampilkan informasi profil tuan rumah (nama, foto, rating, jumlah ulasan).

   Scenario: Informasi Profil Host

   

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result | Automated | Note |
| ----- | ----- | ----- | ----- | ----- | :---: | :---: | :---: | ----- |
| Test Item: Penampilan informasi profil tuan rumah |  |  |  |  |  |  |  |  |
| TC-DP-J-01 | Menampilkan nama, foto profil, dan status Superhost (jika ada) tuan rumah. | 1\. Buka halaman detail properti. 2\. Cari bagian "Dikelola oleh \[Nama Tuan Rumah\]" atau "Tuan Rumah Anda". | Nama (biasanya nama depan) dan foto profil tuan rumah ditampilkan. Jika tuan rumah adalah Superhost, lencana Superhost juga ditampilkan dengan jelas. | informasi nama dan foto profil tuan rumah (immanuel) tertampil | 02/12/25 | Pass | TRUE |  |
| TC-DP-J-02 | Menampilkan rating rata-rata dan jumlah ulasan untuk tuan rumah. | 1\. Di bagian informasi tuan rumah, perhatikan rating dan jumlah ulasan. | Rating bintang rata-rata tuan rumah (jika ada) dan total jumlah ulasan yang diterima tuan rumah ditampilkan (misalnya, "⭐ 4.92 · 150 Ulasan"). | rating rata-rata dan bintang untuktuan rumah tertampil | 02/13/25 | Pass | TRUE |  |
| TC-DP-J-03 | Mengklik nama atau foto tuan rumah untuk melihat profil lengkap tuan rumah. | 1\. Klik pada nama atau foto profil tuan rumah di halaman detail properti. | Pengguna diarahkan ke halaman profil publik lengkap tuan rumah, yang berisi informasi lebih detail seperti deskripsi diri tuan rumah, properti lain yang dikelola, dan semua ulasan tentang tuan rumah. | pindah ke halaman profil tuan rumah ketika foto di klik | 02/14/25 | Pass | TRUE |  |

   

      11. ### ***Test Item: Penampilan semua ulasan properti***  {#test-item:-penampilan-semua-ulasan-properti}

   Scope: Sistem harus menampilkan semua ulasan tamu untuk properti (teks ulasan, rating, nama tamu, tanggal).

   Scenario: Ulasan Tamu

   

| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result | Automated | Note |
| ----- | ----- | ----- | ----- | ----- | :---: | :---: | :---: | ----- |
| Test Item: Penampilan semua ulasan properti |  |  |  |  |  |  |  |  |
| TC-DP-K-01 | Menampilkan ringkasan rating keseluruhan dan rating per kategori (Kebersihan, Akurasi, dll.). | 1\. Buka halaman detail properti. 2\. Cari bagian "Ulasan" atau rating bintang di atas. | Rating bintang keseluruhan untuk properti ditampilkan (misalnya, "⭐ 4.87 · 230 ulasan"). Seringkali diikuti oleh rincian rating untuk kategori spesifik seperti Kebersihan, Akurasi, Check-in, Komunikasi, Lokasi, dan Nilai. | rating umum dan rating per kategori ditampilkan | 02/14/25 | Pass | TRUE |  |
| TC-DP-K-02 | Menampilkan daftar ulasan individual dari tamu. | 1\. Scroll ke bawah ke bagian ulasan. | Daftar ulasan dari tamu sebelumnya ditampilkan, masing-masing biasanya mencakup: \- Foto profil dan nama depan tamu. \- Tanggal ulasan. \- Teks ulasan. \- Rating bintang yang diberikan tamu tersebut (kadang-kadang). | daftar ulasan individu tamu tertampil dalam berntuk card list | 02/14/25 | Pass | TRUE |  |

   

   

 


 


4. ## **Customer Support** {#customer-support}

   1. ### ***Test Item: Pusat bantuan/FAQ*** {#test-item:-pusat-bantuan/faq}

   Scope: Sistem harus menyediakan pusat bantuan/FAQ yang komprehensif.

   Scenario: Dukungan Pelanggan 

   

| Test Case | Customer Support |  |  |  |  |  |  |  |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Pass | 4 | Pending | 0 |  |  |  |  |  |
| Fail | 0 | Number of test cases: | 4 |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
| ID | Test Case Description | Test Case Procedure | Expected Result | Actual Result | Test date | Result | Automated | Note |
| Customer Support |  |  |  |  |  |  |  |  |
| Test Item: Pusat bantuan/FAQ |  |  |  |  |  |  |  |  |
| TC-CS-A-01 | Mencari artikel bantuan menggunakan kata kunci yang relevan. | 1\. Di halaman Pusat Bantuan, masukkan kata kunci yang relevan di kotak pencarian (misalnya, "kebijakan pembatalan", "cara mengubah reservasi"). 2\. Tekan Enter atau klik tombol cari. | Halaman hasil pencarian ditampilkan, berisi daftar artikel bantuan yang relevan dengan kata kunci. Artikel yang paling relevan muncul di bagian atas. | menampilkan artikel sesuai kunci | 02/06/25 | Pass | TRUE |  |
| TC-CS-A-02 | Mencari artikel bantuan menggunakan kata kunci yang tidak relevan atau salah eja. | 1\. Di halaman Pusat Bantuan, masukkan kata kunci yang tidak relevan (misalnya, "resevvai date") atau salah eja (misalnya, "pembataln"). 2\. Tekan Enter atau klik tombol cari. | Sistem menampilkan pesan "Tidak ada hasil ditemukan untuk '\[kata kunci\]'" atau menyarankan kata kunci alternatif/artikel yang mungkin mirip | menampilkan artikel yang mirip | 02/07/25 | Pass | TRUE |  |
| TC-CS-A-03 | Membuka dan membaca artikel bantuan. | 1\. Dari hasil pencarian atau daftar kategori, klik judul salah satu artikel bantuan. | Isi lengkap artikel bantuan ditampilkan dengan jelas dan terstruktur (judul, paragraf, mungkin daftar poin atau gambar). Informasi mudah dibaca dan dipahami. | menampilkan artikel sesuai judul yang di klik | 02/08/25 | Pass | TRUE |  |
| TC-CS-A-04 | Mencoba mencari dengan kolom pencarian kosong. | 1\. Di halaman Pusat Bantuan, jangan masukkan teks apa pun di kolom pencarian. 2\. Klik tombol cari. | Tombol cari mungkin nonaktif, atau jika diklik, tidak ada tindakan yang terjadi, atau halaman menampilkan kembali saran pencarian umum/kategori populer. Tidak boleh ada error. | menampilkan pesan "Cari kata kunci untuk mendapatkan bantuan" | 02/09/25 | Pass | TRUE |  |

   

**Revision History**

| Version | Date | Summary of Changes | Handled by | Revision Marks(Yes/No) |
| ----- | ----- | ----- | ----- | ----- |
| 0.1 | 31/05/2025 | Initial creation | Kelompok F4 |  |
| 0.2 | 02/06/2025 | Input testing result | Kelompok F4 |  |
| 0.3 | 06/06/2025 | Input testing result | Kelompok F4 |  |

