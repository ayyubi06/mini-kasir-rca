"""Unit test Sistem Kasir — Tugas Pertemuan 4 (Analisis & Pengujian Sistem).

Spesifikasi yang diuji (perilaku BENAR):
  - Diskon 10% jika subtotal >= Rp100.000
  - Pajak 11% dihitung dari total SETELAH diskon
  - Input harga/jumlah harus angka dan tidak negatif

Teknik desain: equivalence partitioning + boundary value analysis
(lihat TEST_CASE_DESIGN.md untuk tabel format Slide 14).

Jalankan:  pytest test_kasir.py -v
"""
import pytest
from unittest.mock import patch

from kasir import (
    hitung_subtotal,
    hitung_diskon,
    hitung_pajak,
    susun_struk,
    input_barang,
)


# ---------------- hitung_subtotal ----------------

def test_subtotal_normal():
    items = [
        {"nama": "Indomie", "harga": 3500, "jumlah": 2},
        {"nama": "Teh", "harga": 5000, "jumlah": 1},
    ]
    assert hitung_subtotal(items) == 12000


def test_subtotal_kosong():
    assert hitung_subtotal([]) == 0


# ---------------- hitung_diskon ----------------
# Fault Tugas 3 #1: diskon 1% (harusnya 10%)
# Fault Tugas 3 #2: tepat 100.000 tidak dapat diskon (harusnya >=)

def test_diskon_di_atas_threshold():
    assert hitung_diskon(150000) == 15000  # 10% dari 150.000


def test_diskon_tepat_threshold():
    # Boundary value: tepat 100.000 tetap dapat diskon (spec: >=)
    assert hitung_diskon(100000) == 10000


def test_diskon_di_bawah_threshold():
    assert hitung_diskon(99999) == 0
    assert hitung_diskon(50000) == 0


# ---------------- hitung_pajak ----------------
# Fault Tugas 3 #3: pajak dihitung dari subtotal sebelum diskon

def test_pajak_setelah_diskon():
    # 11% dari (150.000 - 15.000) = 14.850
    assert hitung_pajak(150000, 15000) == pytest.approx(14850.0)


def test_pajak_tanpa_diskon():
    assert hitung_pajak(50000, 0) == pytest.approx(5500.0)


# ---------------- susun_struk ----------------

def test_susun_struk_memuat_komponen():
    teks = susun_struk(
        "TRX-1", "08-10-2026 10:00:00",
        [{"nama": "Indomie", "harga": 3500, "jumlah": 2}],
        7000, 0, 770, 7770, 10000, 2230,
    )
    assert "TRX-1" in teks
    assert "Indomie" in teks
    assert "Rp7,770" in teks


# ---------------- input_barang (mock) ----------------
# Fault Tugas 3 #4: input non-angka crash, harga negatif diterima

def test_input_barang_valid():
    with patch("builtins.input", side_effect=["Indomie", "3500", "2", "selesai"]):
        items = input_barang()
    assert items == [{"nama": "Indomie", "harga": 3500, "jumlah": 2}]


def test_input_barang_tolak_nonangka():
    # "abc" harus ditolak, lalu input valid diterima
    with patch("builtins.input",
               side_effect=["Indomie", "abc", "3500", "2", "selesai"]):
        items = input_barang()
    assert items[0]["harga"] == 3500


def test_input_barang_tolak_negatif():
    # "-5000" harus ditolak, lalu input valid diterima
    with patch("builtins.input",
               side_effect=["Indomie", "-5000", "3500", "2", "selesai"]):
        items = input_barang()
    assert items[0]["harga"] == 3500
