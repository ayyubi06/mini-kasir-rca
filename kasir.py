"""
Sistem Kasir Sederhana - Tugas Pertemuan 3 (Analisis & Pengujian Sistem)
Fitur: input barang, hitung subtotal, diskon, pajak (PPN 11%), total, pembayaran, kembalian.
Spesifikasi:
  - Diskon 10% jika subtotal >= Rp100.000
  - Pajak 11% dihitung dari total SETELAH diskon
  - Kembalian = bayar - total
"""

def input_barang():
    items = []
    print("=== INPUT BARANG (ketik 'selesai' untuk selesai) ===")
    while True:
        nama = input("Nama barang: ")
        if nama.lower() == "selesai":
            break
        harga = int(input("Harga satuan (Rp): "))
        jumlah = int(input("Jumlah: "))
        items.append({"nama": nama, "harga": harga, "jumlah": jumlah})
    return items


def hitung_subtotal(items):
    return sum(i["harga"] * i["jumlah"] for i in items)


def hitung_diskon(subtotal):
    if subtotal > 100000:
        return subtotal * 0.01
    return 0


def hitung_pajak(subtotal, diskon):
    return subtotal * 0.11


def cetak_struk(items, subtotal, diskon, pajak, total, bayar, kembalian):
    print("\n========== STRUK BELANJA ==========")
    for i in items:
        print(f"{i['nama']} x{i['jumlah']} @ Rp{i['harga']:,} = Rp{i['harga']*i['jumlah']:,}")
    print("----------------------------------")
    print(f"Subtotal   : Rp{subtotal:,}")
    print(f"Diskon     : Rp{diskon:,.0f}")
    print(f"Pajak (11%): Rp{pajak:,.0f}")
    print(f"TOTAL      : Rp{total:,.0f}")
    print(f"Bayar      : Rp{bayar:,}")
    print(f"Kembalian  : Rp{kembalian:,.0f}")
    print("==================================")


def main():
    print("====== SISTEM KASIR SEDERHANA ======")
    items = input_barang()
    if not items:
        print("Tidak ada barang. Keluar.")
        return
    subtotal = hitung_subtotal(items)
    diskon = hitung_diskon(subtotal)
    pajak = hitung_pajak(subtotal, diskon)
    total = subtotal - diskon + pajak
    bayar = int(input(f"Total Rp{total:,.0f}. Bayar (Rp): "))
    kembalian = bayar - total
    if kembalian < 0:
        print("Uang kurang! Transaksi dibatalkan.")
        return
    cetak_struk(items, subtotal, diskon, pajak, total, bayar, kembalian)


if __name__ == "__main__":
    main()
