# Mini Kasir RCA

Mini program **Sistem Kasir Sederhana** (Python CLI) untuk Tugas Pertemuan 3
mata kuliah **Analisis & Pengujian Sistem**: membuat mini program, menemukan
defect/fault, dan menyusun Root Cause Analysis (RCA).

Program ini **sengaja mengandung beberapa fault** — bagian serunya adalah
menemukannya lewat pengujian. Lihat [RCA.md](RCA.md) untuk hasil analisis
lengkapnya (atau coba temukan sendiri dulu!).

## Persyaratan

- Python 3.x (tidak butuh library tambahan apa pun)
- Git (untuk clone repo)

## Cara menjalankan

```bash
# 1. Clone repo ini
git clone https://github.com/ayyubi06/mini-kasir-rca.git

# 2. Masuk ke foldernya
cd mini-kasir-rca

# 3. Jalankan programnya
python3 kasir.py
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
Total Rp111,000. Bayar (Rp): 150000

========== STRUK BELANJA ==========
Beras x2 @ Rp50,000 = Rp100,000
----------------------------------
Subtotal   : Rp100,000
Diskon     : Rp0
Pajak (11%): Rp11,000
TOTAL      : Rp111,000
Bayar      : Rp150,000
Kembalian  : Rp39,000
==================================
```

## Spesifikasi yang seharusnya

Program ini ditulis berdasarkan spesifikasi berikut:

- **Diskon 10%** jika subtotal **>=** Rp100.000
- **Pajak (PPN) 11%** dihitung dari total **setelah** diskon
- **Kembalian** = bayar − total
- Input harga dan jumlah harus angka positif

## Tantangan: coba temukan fault-nya!

Sebelum mengintip [RCA.md](RCA.md), coba uji programnya dengan skenario ini
dan bandingkan hasilnya dengan spesifikasi di atas:

| # | Skenario uji | Cara | Yang diharapkan | Yang terjadi |
|---|--------------|------|-----------------|--------------|
| 1 | Diskon belanja besar | Input 1 barang Rp200.000 × 1 | Diskon Rp20.000 (10%) | ??? |
| 2 | Batas tepat Rp100.000 | Input 1 barang Rp100.000 × 1 | Dapat diskon (syarat `>=`) | ??? |
| 3 | Dasar perhitungan pajak | Belanja Rp200.000, lihat pajak | 11% × (200.000 − diskon) | ??? |
| 4 | Input tidak valid | Isi harga dengan `abc`, lalu coba harga `-5000` | Pesan error yang jelas / ditolak | ??? |

## Hasil analisis

Analisis akar masalah tiap fault dengan metode **5 Whys**, lengkap dengan
langkah reproduksi, dampak, dan rekomendasi perbaikan/pencegahan:

→ [**RCA.md**](RCA.md)

## Isi repo

| File | Keterangan |
|------|------------|
| `kasir.py` | Mini program sistem kasir |
| `RCA.md` | Root Cause Analysis tiap fault (metode 5 Whys) |
| `README.md` | Panduan ini |
