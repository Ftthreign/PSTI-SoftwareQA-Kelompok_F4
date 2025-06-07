# Test Scenario  
**Airbnb 25.22**  
**Kelompok F4**  

| Informasi           | Detail                                      |
|---------------------|---------------------------------------------|
| Owner              | Airbnb Inc                                  |
| Scope              | Functional testing of the Airbnb application version 25.22 |
| Originator         |                                             |
| Status             | Draft/In Process/Approved                   |
| Document ID        | TSC001                                      |
| Location           | San Francisco, California, United States    |

---

## 1. TEST SCENARIO FUNCTIONAL AIRBNB
### 1.1 Test Basis

| Document                     | Author   | Date       | Version |
|------------------------------|----------|------------|---------|
| Spesifikasi Fungsional Airbnb | Tim F4   | 30/5/2025  | 25.22   |

### 1.2 Prerequisites
**Untuk memulai eksekusi tes:**
- Dokumen Spesifikasi Fungsional Airbnb Versi 25.22  
- Akses ke lingkungan pengujian (D/T/A/P)  

**Minimal system requirements:**
- Perangkat dengan akses internet  
- Browser web versi terbaru (Chrome, Firefox, Safari)  

**System configuration:**
- Konfigurasi sistem sesuai lingkungan pengujian  
- Akses ke database Airbnb  
- Akses ke layanan terkait aplikasi  
- Workstation yang telah dikonfigurasi  

### 1.3 Product Risks
1. **Fungsi pencarian tidak akurat**  
   Hasil pencarian tidak sesuai kriteria (lokasi, tanggal, harga, fasilitas).  
2. **Proses pemesanan gagal**  
   Error saat pembayaran/konfirmasi tidak terkirim.  
3. **Fitur pesan tidak berfungsi**  
   Gagal mengirim/menerima pesan dengan host/tamu.  
4. **Manajemen profil pengguna bermasalah**  
   Gagal memperbarui profil, foto, atau preferensi.  
5. **Ulasan dan rating tidak ditampilkan dengan benar**  
   Ulasan tidak muncul atau rating tidak akurat.  

---

## 2. TEST SCENARIO
### 2.1 Intake Test Environment
**Test environment:** D/T/A/P  

| Platform          | Name  | Auth Request | Applicant | Manager | Auth Delivered | Username       | Valid From/To     | Works Correctly? |
|-------------------|-------|--------------|-----------|---------|----------------|----------------|-------------------|------------------|
| Pre-migration     | TIM F4| 2025-05-30   | TIM F4    | -       | -              | 085377361121   | 2025-05-31/Ongoing| Yes              |

---

### 2.2 Pretest
| Item                         | Detail                                                                 |
|------------------------------|------------------------------------------------------------------------|
| Test Script                  | Pretest - Verifikasi Akses dan Fungsi Dasar Airbnb Web                 |
| Test Cases                   | Akses Halaman Utama, Pencarian Sederhana, Lihat Detail Properti, dll. |
| Tested Product Risks         | Fungsi pencarian tidak akurat, Akses halaman web                       |
| Date Execution               | 2025-06-01                                                            |
| Defects                      | (Ditemukan selama pengujian)                                           |
| Go/No Go                     | Go                                                                     |

**Defects & Solutions:**  
- 🐞 Halaman tidak dapat diakses → Periksa koneksi internet  
- 🐞 Gambar tidak muncul → Gunakan browser lain  
- 🐞 Login gagal → Verifikasi username/password  

---

### 2.3 Test Round 1 (Versi 25.22)
| No | Test Script                          | Test Level | Tests                                                                 | Product Risks                                                                 | Start Date  | End Date    | % Done | Defects |
|----|--------------------------------------|------------|-----------------------------------------------------------------------|-------------------------------------------------------------------------------|-------------|-------------|--------|---------|
| 1  | Registrasi Pengguna Baru             | Fungsional | Isi formulir, verifikasi akun dibuat                                 | Manajemen profil bermasalah (registrasi)                                      | 2025-06-02  | 2025-06-02  | 100%   | 0       |
| 2  | Login Pengguna                       | Fungsional | Masukkan kredensial valid, verifikasi login                          | Manajemen profil bermasalah (login)                                           | 2025-06-02  | 2025-06-02  | 100%   | 0       |
| 3  | Lupa Kata Sandi                      | Fungsional | Gunakan fitur reset, verifikasi email terkirim                       | Manajemen profil bermasalah (reset password)                                  | 2025-06-03  | 2025-06-03  | 0%     | **1**   |
| ...| [...]                                | ...        | ...                                                                   | ...                                                                           | ...         | ...         | ...    | ...     |
| 18 | Fitur Daftar Keinginan (Wishlist)    | Fungsional | Tambahkan properti ke wishlist, verifikasi tersimpan                 | Manajemen profil bermasalah (wishlist)                                        | 2025-06-10  | 2025-06-10  | 100%   | 0       |

> **Keterangan Tabel:**  
> - `Tested Product Risks`: Risiko produk yang diuji  
> - `% Done`: Persentase penyelesaian skenario  
> - `Defects`: Jumlah defect yang ditemukan  

---

### 2.4 Test Round 2 (Versi 25.22)
| No | Test Script                      | Test Level | Tests                     | Product Risks                          | Start Date  | End Date    | % Done | Defects |
|----|----------------------------------|------------|---------------------------|----------------------------------------|-------------|-------------|--------|---------|
| 1  | Detail Galeri Foto Properti      | Fungsional | Periksa tampilan foto     | Tampilan foto tidak benar              | 2025-06-11  | 2025-06-11  | 100%   | 0       |
| 2  | Deskripsi Properti               | Fungsional | Baca deskripsi lengkap    | Deskripsi tidak sesuai                 | 2025-06-11  | 2025-06-11  | 100%   | 0       |
| ...| [...]                            | ...        | ...                       | ...                                    | ...         | ...         | ...    | ...     |
| 14 | Dukungan Pelanggan               | Fungsional | Hubungi dukungan          | Dukungan tidak responsif               | 2025-06-22  | 2025-06-23  | 0%     | **1**   |

---

## Release Advice  
**Lanjutkan rilis dengan:**  
1. Perbaikan bug pada fitur *"Lupa Kata Sandi"* (FR-USR03)  
2. Penyelesaian pengujian fitur notifikasi & dukungan pelanggan (harus mencapai 100%)  
3. Setelah poin di atas selesai, versi **25.22 siap dirilis untuk publik**.  

> *Dokumen lengkap: 13 halaman | Versi: 31 Mei 2025*  
