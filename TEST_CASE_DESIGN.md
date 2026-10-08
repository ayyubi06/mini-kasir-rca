# Test Case Design — Sistem Kasir (Tugas Pertemuan 4)

Format mengikuti Slide 14 materi (Myers, 2012, Fig 5.3):
kolom **Test case | Input | Expected output**.

Teknik yang dipakai: *equivalence partitioning* (kelas valid/invalid)
dan *boundary value analysis* (nilai di sekitar batas Rp100.000).

## Tabel Test Case

| Test case | Input | Expected output |
|---|---|---|
| TC-01 | `hitung_subtotal([{Indomie,3500,2},{Teh,5000,1}])` | `12000` |
| TC-02 | `hitung_subtotal([])` | `0` |
| TC-03 | `hitung_diskon(150000)` | `15000` (10%) |
| TC-04 | `hitung_diskon(100000)` — boundary, tepat di batas | `10000` (dapat diskon, spec: `>=`) |
| TC-05 | `hitung_diskon(99999)` — boundary, 1 di bawah batas | `0` |
| TC-06 | `hitung_diskon(50000)` — kelas invalid | `0` |
| TC-07 | `hitung_pajak(150000, 15000)` | `14850` (11% dari 135.000, setelah diskon) |
| TC-08 | `hitung_pajak(50000, 0)` | `5500` |
| TC-09 | `input_barang()` dengan input `Indomie, 3500, 2, selesai` | `[{nama: Indomie, harga: 3500, jumlah: 2}]` |
| TC-10 | `input_barang()` dengan input `Indomie, abc, 3500, 2, selesai` | `abc` ditolak, harga tercatat `3500` |
| TC-11 | `input_barang()` dengan input `Indomie, -5000, 3500, 2, selesai` | `-5000` ditolak, harga tercatat `3500` |
| TC-12 | `susun_struk(...)` lengkap | Struk memuat no. struk, item, dan `TOTAL : Rp7,770` |

## Pemetaan ke Fault Tugas 3

| Fault (Tugas 3) | Ditangkap oleh |
|---|---|
| #1 Diskon 1% (harusnya 10%) | TC-03 |
| #2 Tepat Rp100.000 tidak dapat diskon | TC-04 (boundary value) |
| #3 Pajak dihitung sebelum diskon | TC-07 |
| #4 Input non-angka crash / harga negatif diterima | TC-10, TC-11 |

## Hasil Eksekusi

Otomatisasi: `test_kasir.py` (pytest, 11 test).

- Sebelum perbaikan: **5 gagal** — TC-03, TC-04, TC-07, TC-10, TC-11
  (tepat menangkap keempat fault).
- Sesudah perbaikan: **11/11 lolos**.

Jalankan: `pytest test_kasir.py -v`
