# Root Cause Analysis (RCA) — Sistem Kasir Sederhana

**Program:** Sistem Kasir Sederhana (Python CLI) — `kasir.py`
**Repository:** `mini-kasir-rca` (github.com/ayyubi06) — *menunggu instalasi GitHub App*
**Metode analisis:** 5 Whys per defect
**Tanggal:** 6 Oktober 2026

---

## Fault 1 — Nilai diskon salah (1%, seharusnya 10%)

**Gejala:** Belanja Rp200.000 hanya mendapat diskon Rp2.000. Seharusnya Rp20.000 (10%).

**Langkah reproduksi:**
1. Jalankan `python3 kasir.py`
2. Input 1 barang: harga 200.000, jumlah 1 → subtotal Rp200.000
3. Lihat struk: Diskon tercetak Rp2.000

**Analisis 5 Whys:**
1. Kenapa diskon hanya Rp2.000? → Karena kode mengalikan subtotal dengan 0.01
2. Kenapa dikali 0.01? → Programmer menulis `subtotal * 0.01` di fungsi `hitung_diskon`
3. Kenapa 0.01 bukan 0.1? → Salah konversi persen ke desimal saat coding (10% = 0.1, bukan 0.01)
4. Kenapa tidak ketahuan saat coding? → Tidak ada unit test untuk fungsi `hitung_diskon`
5. Kenapa tidak ada unit test? → Tidak ada standar/proses testing yang mewajibkan test untuk fungsi perhitungan

**Root cause:** Human error saat implementasi (salah konversi persen) yang lolos karena tidak ada unit test.

**Dampak:** Kerugian finansial — toko memberi diskon 10x lebih kecil dari yang dijanjikan ke pelanggan; potensi komplain.

**Rekomendasi perbaikan:** Ubah `0.01` menjadi `0.1`; definisikan konstanta bernama `DISKON_RATE = 0.10` agar maksudnya jelas.

**Rekomendasi pencegahan:** Wajibkan unit test untuk setiap fungsi perhitungan bisnis; lakukan code review dengan checklist "magic number".

---

## Fault 2 — Batas threshold diskon salah (tepat Rp100.000 tidak dapat diskon)

**Gejala:** Belanja tepat Rp100.000 tidak mendapat diskon. Spesifikasi: diskon berlaku jika subtotal **>=** Rp100.000.

**Langkah reproduksi:**
1. Jalankan `python3 kasir.py`
2. Input 1 barang: harga 100.000, jumlah 1 → subtotal tepat Rp100.000
3. Lihat struk: Diskon tercetak Rp0 (seharusnya Rp10.000)

**Analisis 5 Whys:**
1. Kenapa tidak dapat diskon? → Kondisi di kode memakai `subtotal > 100000` (strictly greater)
2. Kenapa memakai `>` bukan `>=`? → Programmer mengabaikan kata "sama dengan" pada spesifikasi
3. Kenapa spesifikasi diabaikan? → Tidak ada boundary value analysis saat perancangan test
4. Kenapa tidak ada boundary analysis? → Test hanya memakai nilai tengah (misal 200.000), tidak pernah menguji nilai batas
5. Kenapa nilai batas tidak diuji? → Tidak ada test case design technique yang diterapkan secara sistematis

**Root cause:** Off-by-one / boundary condition error — implementasi tidak mencakup nilai batas, dan tidak ada pengujian batas.

**Dampak:** Pelanggan yang belanja tepat Rp100.000 dirugikan; inkonsistensi dengan brosur/promo yang dijanjikan.

**Rekomendasi perbaikan:** Ubah kondisi menjadi `subtotal >= 100000`.

**Rekomendasi pencegahan:** Terapkan boundary value analysis untuk setiap kondisi threshold; buat test case untuk nilai batas (99.999 / 100.000 / 100.001).

---

## Fault 3 — Pajak dihitung dari subtotal sebelum diskon

**Gejala:** Belanja Rp200.000 (diskon Rp20.000 setelah Fault 1 diperbaiki) dikenai pajak Rp22.000 = 11% × 200.000. Seharusnya 11% × (200.000 − 20.000) = Rp19.800.

**Langkah reproduksi:**
1. Jalankan `python3 kasir.py`
2. Input barang hingga subtotal Rp200.000
3. Lihat struk: Pajak tercetak Rp22.000, padahal dasar pengenaan seharusnya Rp180.000

**Analisis 5 Whys:**
1. Kenapa pajak Rp22.000? → Fungsi `hitung_pajak` memakai `subtotal` mentah, bukan `subtotal - diskon`
2. Kenapa memakai subtotal mentah? → Parameter `diskon` diterima fungsi tetapi tidak dipakai dalam rumus
3. Kenapa tidak dipakai? → Programmer berasumsi pajak dihitung sebelum diskon (atau tidak membaca urutan perhitungan di spesifikasi)
4. Kenapa asumsi tidak diverifikasi? → Spesifikasi "pajak dihitung dari total setelah diskon" tidak ditelusuri ke implementasi (tidak ada traceability)
5. Kenapa tidak ada traceability? → Tidak ada review spesifikasi-vs-kode sebelum rilis

**Root cause:** Salah interpretasi urutan perhitungan bisnis (requirement misunderstanding) — diskon harus mengurangi dasar pajak terlebih dahulu.

**Dampak:** Pelanggan membayar pajak lebih besar dari seharusnya; masalah kepatuhan/keuangan jika diaudit.

**Rekomendasi perbaikan:** Ubah rumus menjadi `(subtotal - diskon) * 0.11`.

**Rekomendasi pencegahan:** Buat requirement traceability matrix (setiap aturan bisnis dipetakan ke fungsi + test case); libatkan domain expert saat review.

---

## Fault 4 — Tidak ada validasi input

**Gejala (a):** Input harga "abc" membuat program crash dengan `ValueError: invalid literal for int()`.
**Gejala (b):** Harga negatif (Rp-5.000) diterima → total dan kembalian menjadi negatif/absurd.

**Langkah reproduksi:**
1. Jalankan `python3 kasir.py`
2. Pada prompt harga, ketik `abc` → program crash (traceback)
3. Ulangi, masukkan harga `-5000`, jumlah `2` → struk mencetak total Rp-11.100

**Analisis 5 Whys:**
1. Kenapa crash / data absurd? → `int(input(...))` langsung dipakai tanpa try-except; tidak ada pengecekan `harga > 0`
2. Kenapa tidak ada pengecekan? → Programmer berasumsi pengguna selalu memasukkan data benar (happy path only)
3. Kenapa hanya happy path? → Tidak ada analisis "apa yang bisa salah" (negative testing) saat desain
4. Kenapa tidak ada negative testing? → Test plan hanya mencakup skenario normal
5. Kenapa test plan sempit? → Tidak ada standar input validation sebagai bagian dari definition of done

**Root cause:** Missing input validation — tidak ada defensive programming dan tidak ada negative test cases.

**Dampak:** Crash mengganggu operasional kasir; data negatif merusak laporan keuangan dan bisa dimanfaatkan untuk fraud (kembalian fiktif).

**Rekomendasi perbaikan:** Bungkus `int(input())` dengan try-except + loop hingga valid; tolak harga ≤ 0 dan jumlah ≤ 0 dengan pesan error yang jelas.

**Rekomendasi pencegahan:** Jadikan validasi input sebagai checklist wajib code review; tambahkan negative test cases (input non-angka, nol, negatif) di setiap form input.

---

## Ringkasan Temuan

| # | Fault | Kategori | Root Cause | Severity |
|---|-------|----------|------------|----------|
| 1 | Diskon 1% (seharusnya 10%) | Logic error | Salah konversi persen + tanpa unit test | Tinggi |
| 2 | Batas 100rb tidak dapat diskon | Boundary error | `>` vs `>=` + tanpa boundary testing | Sedang |
| 3 | Pajak dari subtotal sebelum diskon | Requirement misunderstanding | Urutan perhitungan salah + tanpa traceability | Tinggi |
| 4 | Tanpa validasi input | Missing validation | Happy-path only + tanpa negative test | Tinggi |

**Pola umum:** keempat fault berakar pada tidak adanya testing yang sistematis (unit test, boundary analysis, negative testing) dan tidak adanya code review. Rekomendasi pencegahan lintas-fault: adopsi test plan minimal (positive + negative + boundary) dan checklist code review sebelum setiap rilis.
