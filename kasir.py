"""
Sistem Kasir Sederhana - Tugas Pertemuan 3 (Analisis & Pengujian Sistem)
Fitur: input barang, hitung subtotal, diskon, pajak (PPN 11%), total,
       pembayaran, kembalian, struk bernomor + timestamp, simpan riwayat.
Spesifikasi:
  - Diskon 10% jika subtotal >= Rp100.000
  - Pajak 11% dihitung dari total SETELAH diskon
  - Kembalian = bayar - total
"""
import datetime

RIWAYAT_FILE = "riwayat_transaksi.txt"


def buat_nomor_struk():
    return "TRX-" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")


def _input_angka_positif(prompt):
    """Minta input angka >= 0; tolak non-angka dan nilai negatif."""
    while True:
        try:
            nilai = int(input(prompt))
        except ValueError:
            print("Input harus berupa angka. Coba lagi.")
            continue
        if nilai < 0:
            print("Nilai tidak boleh negatif. Coba lagi.")
            continue
        return nilai


def input_barang():
    items = []
    print("=== INPUT BARANG (ketik 'selesai' untuk selesai) ===")
    while True:
        nama = input("Nama barang: ")
        if nama.lower() == "selesai":
            break
        harga = _input_angka_positif("Harga satuan (Rp): ")
        jumlah = _input_angka_positif("Jumlah: ")
        items.append({"nama": nama, "harga": harga, "jumlah": jumlah})
    return items


def hitung_subtotal(items):
    return sum(i["harga"] * i["jumlah"] for i in items)


def hitung_diskon(subtotal):
    if subtotal >= 100000:
        return subtotal * 0.10
    return 0


def hitung_pajak(subtotal, diskon):
    return (subtotal - diskon) * 0.11


def susun_struk(no_struk, waktu, items, subtotal, diskon, pajak, total, bayar, kembalian):
    baris = []
    baris.append("========== STRUK BELANJA ==========")
    baris.append(f"No. Struk : {no_struk}")
    baris.append(f"Tanggal   : {waktu}")
    baris.append("----------------------------------")
    for i in items:
        baris.append(f"{i['nama']} x{i['jumlah']} @ Rp{i['harga']:,} = Rp{i['harga']*i['jumlah']:,}")
    baris.append("----------------------------------")
    baris.append(f"Subtotal   : Rp{subtotal:,}")
    baris.append(f"Diskon     : Rp{diskon:,.0f}")
    baris.append(f"Pajak (11%): Rp{pajak:,.0f}")
    baris.append(f"TOTAL      : Rp{total:,.0f}")
    baris.append(f"Bayar      : Rp{bayar:,}")
    baris.append(f"Kembalian  : Rp{kembalian:,.0f}")
    baris.append("==================================")
    baris.append("   Terima kasih sudah berbelanja!   ")
    baris.append("==================================")
    return "\n".join(baris)


def simpan_riwayat(teks_struk):
    with open(RIWAYAT_FILE, "a") as f:
        f.write(teks_struk + "\n\n")


def main():
    print("====== SISTEM KASIR SEDERHANA ======")
    print("     -- Toko Kelontong Berkah --")
    items = input_barang()
    if not items:
        print("Tidak ada barang. Keluar.")
        return
    no_struk = buat_nomor_struk()
    waktu = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    subtotal = hitung_subtotal(items)
    diskon = hitung_diskon(subtotal)
    pajak = hitung_pajak(subtotal, diskon)
    total = subtotal - diskon + pajak
    bayar = int(input(f"Total Rp{total:,.0f}. Bayar (Rp): "))
    kembalian = bayar - total
    if kembalian < 0:
        print("Uang kurang! Transaksi dibatalkan.")
        return
    teks = susun_struk(no_struk, waktu, items, subtotal, diskon, pajak, total, bayar, kembalian)
    print()
    print(teks)
    simpan_riwayat(teks)
    print(f"\n[Struk {no_struk} tersimpan di {RIWAYAT_FILE}]")


if __name__ == "__main__":
    main()
