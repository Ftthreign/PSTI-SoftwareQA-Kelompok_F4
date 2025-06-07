

**Test Strategy**  
Airbnb 25.22  
Kelompok F4

| Owner | : Airbnb Inc |
| :---- | :---- |
| Scope | : To define overall approach and objectives of functional testing |
| Originator | :  |
| Status | : Draft/In Process/Approved |
| Document ID | : TCE001 |
| Location | : San Francisco, California, United States |

**Table of Contents**

**[1\. Introduction	3](#introduction)**

[**2\. Test Motivators	3**](#test-motivators)

[2.1 Memenuhi Kebutuhan Fungsional	3](#memenuhi-kebutuhan-fungsional)

[2.2 Menjamin Pengalaman Pengguna yang Konsisten	3](#menjamin-pengalaman-pengguna-yang-konsisten)

[**3\. Test Approach	3**](#test-approach)

[3.1 Mengidentifikasi Jenis Pengujian	4](#mengidentifikasi-jenis-pengujian)

[3.1.1 Manual Test	4](#manual-test)

[3.1.2 Automated Test	4](#automated-test)

[3.2 Measuring the Extent of Testing	4](#measuring-the-extent-of-testing)

[3.2.1 Syarat Memulai Pengujian	4](#syarat-memulai-pengujian)

[3.2.2 Syarat Selesai Pengujian	4](#syarat-selesai-pengujian)

[**4\. Dependencies, Assumptions, and Constraints	5**](#dependencies,-assumptions,-and-constraints)

**Airbnb Test Strategy**

1. # **Introduction** {#introduction}

   Dokumen Test Strategy ini disusun untuk menggambarkan pendekatan, ruang lingkup, dan rencana pelaksanaan pengujian fungsional pada website Airbnb. Pengujian dilakukan secara black-box, yakni tester tidak meninjau kode sumber, melainkan berfokus pada verifikasi end-to-end dari sisi antarmuka dan alur bisnis yang terlihat oleh pengguna akhir.

2. # **Test Motivators** {#test-motivators}

   1. ## **Memenuhi Kebutuhan Fungsional** {#memenuhi-kebutuhan-fungsional}

   Pengujian ditujukan untuk memverifikasi bahwa fitur-fitur pada website Airbnb bekerja dengan sesuai. Fitur-fitur pada website Airbnb yang akan dites adalah:

* Pencarian dan Penemuan Properti (Search & Discovery)  
* User Management  
* Detail Properti  
* Customer Support

  2. ## **Menjamin Pengalaman Pengguna yang Konsisten** {#menjamin-pengalaman-pengguna-yang-konsisten}

  Kebutuhan Fungsional

* Sistem harus memungkinkan pengguna untuk mencari properti berdasarkan lokasi, melakukan filter hasil pencarian, dan menampilkan hasil pencarian.  
* Sistem harus memungkinkan pengguna untuk mendaftarkan akun baru, masuk (login) menggunakan akun pengguna, mengelola preferensi pengguna, mengelola informasi pengguna, dan menampilkan riwayat pemesanan pengguna.  
* Sistem harus mampu menampilkan detail lengkap spesifik properti, kebijakan pembatalan properti, dan semua ulasan tamu untuk properti.  
* Sistem harus memungkinkan tuan rumah untuk mempublikasikan ulasan terhadap tamu setelah check-out dan memungkinkan pengguna untuk mempublikasikan ulasan dan rating properti.  
* Sistem harus menyediakan pusat bantuan/FAQ yang komprehensif, menyediakan fitur customer support, dan memiliki mekanisme untuk membantu mediasi sengketa antara tamu dan tuan rumah.

3. # **Test Approach** {#test-approach}

   

   Pendekatan pengujian mendefinisikan ruang lingkup dan arah umum upaya pengujian untuk website Airbnb (desktop). Bagian ini memberikan gambaran tingkat tinggi mengenai aspek-aspek penting yang akan diuraikan lebih lanjut dalam rencana pengujian dan skrip pengujian.

   

   1. ## **Mengidentifikasi Jenis Pengujian** {#mengidentifikasi-jenis-pengujian}

      1. ### **Manual Test** {#manual-test}

   Manual testing dilakukan untuk pemeriksaan visual dan interaktif antarmuka, alur pengguna, dan elemen UI. UI pada fitur-fitur yang dites adalah:

* Pencarian & Penemuan Properti  
* Manajemen Pengguna  
* Detail Properti  
* Customer Support

  2. ### **Automated Test** {#automated-test}

  Automated testing akan dilakukan menggunakan **Selenium** dan **Test Case Studio** di Google Chrome. Skrip-skrip ini dirancang untuk:

* Menjalankan skenario end-to-end pada keempat fitur kunci (Search & Discovery, User Management, Detail Properti, Customer Support).  
* Meningkatkan kecepatan dan konsistensi eksekusi pengujian rutin tanpa risiko human error.

  2. ## **Measuring the Extent of Testing** {#measuring-the-extent-of-testing}

     1. ### **Syarat Memulai Pengujian** {#syarat-memulai-pengujian}

  Adapun syarat untuk melakukan pengujian adalah sebagai berikut:

* Akun test (guest atau user) dan data dummy  
* Browser untuk mengakses website Airbnb  
* Tool pengujian Selenium dan Test Case Studio sudah terpasang

  2. ### **Syarat Selesai Pengujian** {#syarat-selesai-pengujian}

  Adapun syarat untuk menyelesaikan pengujian adalah sebagai berikut:

* Semua test case telah dijalankan.  
* Aplikasi/Website tidak mengalami crash selama pengujian.  
* Tingkat keberhasilan test case \> 85%

4. # **Dependencies, Assumptions, and Constraints** {#dependencies,-assumptions,-and-constraints}

Table 1: Dependencies

| Dependency  | Potential Impact of Dependency | Owners |
| :---- | :---- | :---- |
| Ketersediaan Akun untuk melakukan testing | Skenario end-to-end tidak bisa dieksekusi |  |
| Data dummy | Beberapa skenario tidak dapat dieksekusi tanpa data dummy |  |
|  |  |  |

Table 2: Assumptions

| Assumption  | Impact of Assumption  | Owners |
| :---- | :---- | :---- |
| Jaringan internet stabil selama pengujian | Beberapa test case gagal karena gangguan jaringan |  |
|  |  |  |
|  |  |  |

Table 3: Constraints

| Constraint On | Impact Constraint has on Test Effort | Owners |
| :---- | :---- | :---- |
| Durasi pengujian 7 hari | Perlu memprioritaskan test case dengan skenario yang kritis |  |
|  |  |  |
|  |  |  |

**Revision History**

| Version | Date | Summary of Changes | Author | Revision Marks(Yes/No) |
| :---- | :---- | :---- | :---- | :---- |
| 0.1 | 31/05/2025 | Initial revision. | Kelompok F4 |  |
|  |  |  |  |  |
|  |  |  |  |  |

