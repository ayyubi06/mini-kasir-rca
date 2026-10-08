# Mini Kasir — Test Case Design & Unit Test

Mini program **Sistem Kasir Sederhana** (Python CLI) untuk mata kuliah
**Analisis & Pengujian Sistem**.

- **Tugas Pertemuan 3**: membuat mini program, menemukan defect/fault, dan
  menyusun Root Cause Analysis (RCA). Versi ber-fault tersimpan di riwayat
  commit — lihat [RCA.md](RCA.md) untuk analisis lengkapnya.
- **Tugas Pertemuan 4** (versi saat ini): Test Case Design format Slide 14
  (Myers, 2012) + unit test otomatis (pytest). Keempat fault dari Tugas 3
  sudah diperbaiki; test membuktikan perbaikannya.

## Persyaratan

- Python 3.x
- pytest (`pip install pytest`) — hanya untuk menjalankan test

## Cara menjalankan

```bash
# 1. Clone repo ini
git clone https://github.com/ayyubi06/mini-kasir-rca.git

# 2. Masuk ke foldernya
cd mini-kasir-rca

# 3. Jalankan programnya
python3 kasir.py

# 4. Jalankan unit test-nya
python3 -m pytest test_kasir.py -v
```

> Pengguna Windows: ganti `python3` dengan `python`.

## Contoh sesi penggunaan

```
====== SISTEM KASIR SEDERHANA ======
=== INPUT BARANG (ketik 'selesai' untuk selesai) ===
Nama barang: Beras
Harga satuan (Rp): 50000
Jumlah: 2
Nama barang: selesai
Total Rp99,900. Bayar (Rp): 150000

========== STRUK BELANJA ==========
Beras x2 @ Rp50,000 = Rp100,000
----------------------------------
Subtotal   : Rp100,000
Diskon     : Rp10,000
Pajak (11%): Rp9,900
TOTAL      : Rp99,900
Bayar      : Rp150,000
Kembalian  : Rp50,100
==================================
```

## Spesifikasi

- **Diskon 10%** jika subtotal **>=** Rp100.000
- **Pajak (PPN) 11%** dihitung dari total **setelah** diskon
- **Kembalian** = bayar − total
- Input harga dan jumlah harus angka dan tidak negatif
  (non-angka dan negatif ditolak dengan pesan yang jelas)

## Test Case Design & Unit Test (Tugas 4)

Desain test case memakai teknik *equivalence partitioning* dan
*boundary value analysis*, didokumentasikan format Slide 14
(Test case | Input | Expected output):

→ [**TEST_CASE_DESIGN.md**](TEST_CASE_DESIGN.md)

Otomatisasi: `test_kasir.py` — 11 test (pytest), mencakup 4 fungsi
(`hitung_subtotal`, `hitung_diskon`, `hitung_pajak`, `susun_struk`)
dan `input_barang` via mock. Dijalankan terhadap kode ber-fault,
5 test gagal tepat pada keempat fault — sesudah perbaikan, 11/11 lolos.

## Fault yang dulu ada (Tugas 3)

| # | Fault | Status |
|---|-------|--------|
| 1 | Diskon 1%, seharusnya 10% | Diperbaiki |
| 2 | Tepat Rp100.000 tidak dapat diskon (`>` vs `>=`) | Diperbaiki |
| 3 | Pajak dihitung sebelum diskon | Diperbaiki |
| 4 | Input non-angka crash, harga negatif diterima | Diperbaiki |

Analisis akar masalah tiap fault (metode 5 Whys):

→ [**RCA.md**](RCA.md)

## Isi repo

| File | Keterangan |
|------|------------|
| `kasir.py` | Mini program sistem kasir |
| `test_kasir.py` | Unit test otomatis (pytest) — Tugas 4 |
| `TEST_CASE_DESIGN.md` | Tabel test case format Slide 14 — Tugas 4 |
| `RCA.md` | Root Cause Analysis tiap fault — Tugas 3 |
| `README.md` | Panduan ini |
