hp_prices = [["iphone", 15000000], ["samsung", 2000000], ["vivo", 500000], ["oppo", 80000], ["xiamomi", 900000] ]


def lihat_data():
    print('\n Menu:')
    print('1. Add a new product')
    print('2. Add product')
    print('3. Delete a product')
    print('4. Out the program')

def lihat_produk():
    print("\nData harga hp:")

    if not hp_prices:
        print("tidak ada data harga hp")
        return
    
    for hp, harga in hp_prices:
        print(f"- {hp}: - Rp{harga:,}")

def main():
    while True:
        lihat_data()
        choice = input("pilih menu (1-4): ")

        if choice == '1':
            lihat_produk()
        elif choice == '2':
            print(input("input the product "))
        elif choice == '4':
            print("terima kasih program selesai.")
            break
        else:
            print("pilihan tidak valid, silahkan pilih lagi")

main()