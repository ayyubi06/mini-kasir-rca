# Mini Kasir RCA

Mini program **Sistem Kasir Sederhana** (Python CLI) untuk Tugas Pertemuan 3
mata kuliah Analisis & Pengujian Sistem: menemukan defect/fault dan membuat
Root Cause Analysis (RCA).

## Cara menjalankan

```bash
python3 kasir.py
```

## Spesifikasi

- Diskon 10% jika subtotal **>=** Rp100.000
- Pajak (PPN) 11% dihitung dari total **setelah** diskon
- Kembalian = bayar − total

## Isi repo

| File | Keterangan |
|------|------------|
| `kasir.py` | Mini program sistem kasir |
| `RCA.md` | Root Cause Analysis untuk setiap fault yang ditemukan (metode 5 Whys) |

## Fault yang ditemukan

1. Diskon dihitung 1%, seharusnya 10%
2. Belanja tepat Rp100.000 tidak dapat diskon (`>` vs `>=`)
3. Pajak dihitung dari subtotal sebelum diskon
4. Tidak ada validasi input (crash pada input non-angka, harga negatif diterima)

Detail lengkap tiap fault, langkah reproduksi, analisis 5 Whys, dan rekomendasi
perbaikan/pencegahan ada di [`RCA.md`](RCA.md).
