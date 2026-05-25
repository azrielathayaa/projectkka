menu = {
    1: {"nama": "Nasi Goreng", "harga": 15000},
    2: {"nama": "Mie Ayam", "harga": 12000},
    3: {"nama": "Es Teh", "harga": 5000},
    4: {"nama": "Jus Jeruk", "harga": 8000}
}

pesanan = []


def lihat_menu():
    
    print("\n===== DAFTAR MENU =====")
    for kode, item in menu.items():
        print(f"{kode}. {item['nama']} - Rp{item['harga']}")


def tambah_pesanan():
    lihat_menu()

    pilih = int(input("\nMasukkan nomor menu: "))
    jumlah = int(input("Masukkan jumlah: "))

    if pilih in menu:
        nama = menu[pilih]["nama"]
        harga = menu[pilih]["harga"]
        total = harga * jumlah

        pesanan.append({
            "nama": nama,
            "harga": harga,
            "jumlah": jumlah,
            "total": total
        })

        print(f"{nama} berhasil ditambahkan!")
    else:
        print("Menu tidak tersedia!")


def hitung_total():
    total_bayar = 0

    for item in pesanan:
        total_bayar += item["total"]

    diskon = 5000

    if total_bayar >= 50000:
        diskon = total_bayar * 0.1

    total_akhir = total_bayar - diskon

    return total_bayar, diskon, total_akhir


def cetak_struk():
    if len(pesanan) == 0:
        print("\nBelum ada pesanan!")
        return

    print("\n===== STRUK BELANJA =====")

    for item in pesanan:
        print(
            f"{item['nama']} x{item['jumlah']} = Rp{item['total']}"
        )

    total, diskon, akhir = hitung_total()

    print("-------------------------")
    print(f"Total   : Rp{total}")

    if diskon > 0:
        print(f"Diskon  : Rp{int(diskon)}")

    print(f"Bayar   : Rp{int(akhir)}")


while True:
    print("\n===== KASIR SEDERHANA =====")
    print("1. Lihat Menu")
    print("2. Tambah Pesanan")
    print("3. Cetak Struk")
    print("4. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        lihat_menu()

    elif pilihan == "2":
        tambah_pesanan()

    elif pilihan == "3":
        cetak_struk()

    elif pilihan == "4":
        print("Terima kasih sudah belanja!")
        break

    else:
        print("Pilihan tidak valid!")