**Kebutuhan Aplikasi**  
Airbnb 25.22  
Kelompok F4

1. **Kebutuhan Fungsional**

| No | Kode | Fungsional | Kebutuhan |
| :---: | ----- | ----- | ----- |
| 1 | FR-CP01 | Pencarian dan Penemuan Properti (Search & Discovery) | Sistem harus memungkinkan pengguna untuk mencari properti berdasarkan lokasi (kota, negara bagian, negara, alamat spesifik, atau penunjuk di peta). |
|  | FR-CP02 |  | Sistem harus memungkinkan pengguna untuk memfilter hasil pencarian berdasarkan tanggal check-in dan check-out. |
|  | FR-CP03 |  | Sistem harus memungkinkan pengguna untuk memfilter berdasarkan jumlah tamu (dewasa, anak-anak, bayi). |
|  | FR-CP04 |  | Sistem harus memungkinkan pengguna untuk memfilter berdasarkan jenis properti (seluruh rumah/apartemen, kamar pribadi, kamar bersama). |
|  | FR-CP05 |  | Sistem harus memungkinkan pengguna untuk memfilter berdasarkan rentang harga per malam. |
|  | FR-CP06 |  | Sistem harus memungkinkan pengguna untuk memfilter berdasarkan fasilitas (misalnya, Wi-Fi, dapur, kolam renang, parkir gratis, AC, mesin cuci). |
|  | FR-CP07 |  | Sistem harus memungkinkan pengguna untuk memfilter berdasarkan karakteristik khusus (misalnya, ramah hewan peliharaan, aksesibilitas kursi roda, sarapan gratis). |
|  | FR-CP08 |  | Sistem harus memungkinkan pengguna untuk memfilter berdasarkan jumlah kamar tidur dan kamar mandi. |
|  | FR-CP09 |  | Sistem harus menampilkan hasil pencarian dalam bentuk daftar dan peta interaktif. |
|  | FR-CP10 |  | Sistem harus menampilkan informasi ringkas untuk setiap properti di hasil pencarian (gambar utama, lokasi, harga per malam, rating ulasan, jumlah ulasan). |
|  | FR-CP11 |  | Sistem harus menyediakan fitur "Daftar Keinginan" (Wishlist) agar pengguna dapat menyimpan properti. |
| 2 | FR-USR01 | User Management | Sistem harus memungkinkan pengguna untuk mendaftar akun baru menggunakan email, Google, Facebook, atau Apple ID. |
|  | FR-USR02 |  | Sistem harus memungkinkan pengguna untuk masuk (login) ke akun mereka. |
|  | FR-USR03 |  | Sistem harus menyediakan fitur "Lupa Kata Sandi" untuk reset kata sandi. |
|  | FR-USR04 |  | Sistem harus memungkinkan pengguna untuk mengedit profil mereka (nama, foto profil, deskripsi diri, nomor telepon). |
|  | FR-USR05 |  | Sistem harus memungkinkan pengguna untuk menambahkan dan mengelola metode pembayaran yang valid. |
|  | FR-USR06 |  | Sistem harus menampilkan riwayat pemesanan pengguna (aktif, selesai, dibatalkan). |
|  | FR-USR07 |  | Sistem harus memungkinkan pengguna untuk mengelola preferensi notifikasi mereka. |
| 3 | FR-DP01 | Detail Properti | Sistem harus menampilkan galeri foto dari properti. |
|  | FR-DP02 |  | Sistem harus menampilkan deskripsi lengkap properti yang disediakan oleh tuan rumah. |
|  | FR-DP03 |  | Sistem harus menampilkan detail spesifik properti (jumlah kamar tidur, kamar mandi, jenis tempat tidur). |
|  | FR-DP04 |  | Sistem harus menampilkan daftar lengkap fasilitas yang tersedia di properti. |
|  | FR-DP05 |  | Sistem harus menampilkan kalender ketersediaan properti secara real-time. |
|  | FR-DP06 |  | Sistem harus menghitung dan menampilkan total harga untuk tanggal yang dipilih, termasuk harga per malam, biaya kebersihan, dan biaya layanan. |
|  | FR-DP07 |  | Sistem harus menampilkan aturan rumah yang ditetapkan oleh tuan rumah. |
|  | FR-DP08 |  | Sistem harus menampilkan kebijakan pembatalan properti. |
|  | FR-DP09 |  | Sistem harus menampilkan lokasi properti di peta. |
|  | FR-DP10 |  | Sistem harus menampilkan informasi profil tuan rumah (nama, foto, rating, jumlah ulasan). |
|  | FR-DP11 |  | Sistem harus menampilkan semua ulasan tamu untuk properti (teks ulasan, rating, nama tamu, tanggal). |
| 4 | FR-PP01 | Pemesanan dan Pembayaran | Sistem harus memungkinkan pengguna untuk memilih tanggal check-in dan check-out serta jumlah tamu pada halaman detail properti. |
|  | FR-PP02 |  | Sistem harus memungkinkan pengguna untuk meninjau detail pemesanan (tanggal, tamu, total harga, rincian biaya) sebelum konfirmasi. |
|  | FR-PP03 |  | Sistem harus mendukung dua jenis pemesanan: "Permintaan Pemesanan" (membutuhkan persetujuan tuan rumah) dan "Pemesanan Instan" (langsung dikonfirmasi). |
|  | FR-PP04 |  | Sistem harus memproses pembayaran dengan aman menggunakan berbagai metode pembayaran (kartu kredit/debit, PayPal, dll.). |
|  | FR-PP05 |  | Sistem harus mengirimkan konfirmasi pemesanan ke email pengguna dan menyimpannya di riwayat pemesanan pengguna. |
|  | FR-PP06 |  | Sistem harus memungkinkan pengguna untuk membatalkan pemesanan sesuai dengan kebijakan pembatalan properti. |
|  | FR-PP07 |  | Sistem harus memproses pengembalian dana sesuai dengan kebijakan pembatalan yang berlaku. |
| 5 | FR-KM01 | Komunikasi | Sistem harus menyediakan sistem pesan in-app untuk komunikasi antara tamu dan tuan rumah. |
|  | FR-KM02 |  | Sistem harus mengirimkan notifikasi (email/in-app) untuk pesan baru, status pemesanan, pengingat check-in/check-out. |
| 6 | FR-RR01 | Review dan Rating | Sistem harus memungkinkan tamu untuk memberikan ulasan dan rating (bintang) untuk properti yang mereka inapi setelah check-out. |
|  | FR-RR02 |  | Sistem harus memungkinkan tuan rumah untuk memberikan ulasan dan rating untuk tamu setelah check-out. |
|  | FR-RR03 |  | Sistem harus mempublikasikan ulasan setelah kedua belah pihak memberikan ulasan atau setelah periode waktu tertentu. |
| 7 | FR-HT01 | Fungsionalitas Host | Sistem harus memungkinkan tuan rumah untuk mendaftarkan properti baru (termasuk detail properti, fasilitas, aturan). |
|  | FR-HT02 |  | Sistem harus memungkinkan tuan rumah untuk mengunggah, mengelola, dan mengurutkan foto properti. |
|  | FR-HT03 |  | Sistem harus memungkinkan tuan rumah untuk mengatur dan memperbarui harga per malam, biaya kebersihan, dan biaya tambahan lainnya. |
|  | FR-HT04 |  | Sistem harus memungkinkan tuan rumah untuk mengelola kalender ketersediaan properti (memblokir tanggal, menandai tidak tersedia). |
|  | FR-HT05 |  | Sistem harus memungkinkan tuan rumah untuk mengatur kebijakan pembatalan untuk properti mereka. |
|  | FR-HT06 |  | Sistem harus memungkinkan tuan rumah untuk mengaktifkan atau menonaktifkan fitur "Pemesanan Instan". |
|  | FR-HT07 |  | Sistem harus menampilkan daftar permintaan pemesanan yang masuk kepada tuan rumah. |
|  | FR-HT08 |  | Sistem harus memungkinkan tuan rumah untuk menerima atau menolak permintaan pemesanan |
|  | FR-HT09 |  | Sistem harus menampilkan daftar pemesanan yang dikonfirmasi kepada tuan rumah. |
|  | FR-HT10 |  | Sistem harus menampilkan laporan penghasilan dan riwayat transaksi kepada tuan rumah. |
|  | FR-HT11 |  | Sistem harus memungkinkan tuan rumah untuk mengatur metode pembayaran untuk menerima pembayaran. |
| 8 | FR-CS01 | Customer Support | Sistem harus menyediakan pusat bantuan/FAQ yang komprehensif. |
|  | FR-CS02 |  | Sistem harus menyediakan fitur kontak dukungan (chat, email, atau telepon). |
|  | FR-CS03 |  | Sistem harus memiliki mekanisme untuk membantu mediasi sengketa antara tamu dan tuan rumah. |

2. **Kebutuhan Non-Fungsional**

| No | Kode | Non-Fungsional | Kebutuhan |
| :---: | ----- | ----- | ----- |
| 1 | NFR-PF01 | Performance | Waktu respons pencarian properti tidak boleh melebihi 3 detik untuk 95% permintaan. |
|  | NFR-PF02 |  | Waktu muat halaman detail properti tidak boleh melebihi 2 detik. |
|  | NFR-PF03 |  | Sistem harus mampu menangani 10.000 pengguna bersamaan tanpa penurunan kinerja yang signifikan. |
|  | NFR-PF04 |  | Waktu pemrosesan transaksi pembayaran tidak boleh melebihi 5 detik. |
| 2 | NFR-SC01 | Security | Semua data sensitif (informasi pembayaran, kredensial login) harus dienkripsi saat transit dan saat disimpan (at rest). |
|  | NFR-SC02 |  | Sistem harus menerapkan otentikasi multi-faktor (MFA) sebagai opsi untuk pengguna. |
|  | NFR-SC03 |  | Sistem harus mematuhi standar PCI DSS untuk pemrosesan pembayaran. |
|  | NFR-SC04 |  | Sistem harus memiliki mekanisme untuk mendeteksi dan mencegah serangan umum seperti SQL injection, XSS, dan CSRF. |
|  | NFR-SC05 |  | Akses ke data sensitif hanya boleh diberikan kepada pengguna yang berwenang dengan hak akses yang sesuai. |
|  | NFR-SC06 |  | Sistem harus memiliki kebijakan kata sandi yang kuat (misalnya, panjang minimum, kombinasi karakter). |
| 3 | NFR-RL01 | Reliability | Sistem harus memiliki tingkat ketersediaan (uptime) minimal 99.9% per bulan. |
|  | NFR-RL02 |  | Data pengguna dan properti harus dicadangkan secara teratur (setidaknya setiap 24 jam) dan dapat dipulihkan dalam waktu 4 jam. |
|  | NFR-RL03 |  | Sistem harus dapat pulih dari kegagalan server dalam waktu 30 menit. |
| 4 | NFR-SL01 | Scalability | Sistem harus mampu menangani peningkatan jumlah pengguna dan data (properti, pemesanan) seiring waktu tanpa memerlukan perombakan arsitektur besar-besaran. |
|  | NFR-SL02 |  | Sistem harus dapat ditingkatkan secara horizontal (menambahkan lebih banyak server) untuk mengakomodasi peningkatan beban. |
| 5 | NFR-US01 | Usability | Antarmuka pengguna (UI) harus intuitif dan mudah dipelajari oleh pengguna baru. |
|  | NFR-US02 |  | Navigasi sistem harus konsisten di seluruh platform. |
|  | NFR-US03 |  | Pesan kesalahan harus jelas, informatif, dan membantu pengguna untuk menyelesaikan masalah. |
|  | NFR-US04 |  | Desain harus responsif dan berfungsi dengan baik di berbagai perangkat (desktop, tablet, seluler). |
| 6 | NFR-PT01 | Portability | Sistem harus dapat berjalan di berbagai browser web modern (Chrome, Firefox, Safari, Edge). |
|  | NFR-PT02 |  | Aplikasi seluler (jika ada) harus kompatibel dengan versi terbaru iOS dan Android. |
| 7 | NFR-MT01 | Maintainability | Kode sistem harus terstruktur dengan baik dan mudah dimengerti untuk tujuan pemeliharaan dan pengembangan di masa mendatang. |
|  | NFR-MT02 |  | Dokumentasi teknis yang komprehensif harus tersedia untuk pengembang. |
|  | NFR-MT03 |  | Sistem harus dirancang dengan modularitas untuk memungkinkan pembaruan dan perbaikan komponen secara independen. |
| 8 | NFR-CP01 | Compliance | Sistem harus mematuhi peraturan perlindungan data yang relevan (misalnya, GDPR jika beroperasi di Eropa, atau undang-undang privasi data lokal lainnya). |
|  | NFR-CP02 |  | Sistem harus mematuhi undang-undang perpajakan yang berlaku untuk transaksi penyewaan. |

