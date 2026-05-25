
username_tersimpan = ""
password_tersimpan = ""


def register():
    global username_tersimpan  
    global password_tersimpan

    print("\n REGISTER ")

    username_tersimpan = input("Buat Username : ")
    password_tersimpan = input("Buat Password : ")

    print("Register berhasil!")


def login():
    global username_tersimpan
    global password_tersimpan

    if username_tersimpan == "":
        print("\nBelum ada akun! Silakan register dulu.")
        return

    kesempatan = 3

    while kesempatan > 0:
        print("\n LOGIN ")

        username = input("Username : ")
        password = input("Password : ")

        if username == username_tersimpan and password == password_tersimpan:
            print("Login berhasil!")
            return
        else:
            kesempatan -= 1
            print(f"Username / Password salah!")
            print(f"Sisa percobaan: {kesempatan}")

    print("Login gagal 3x!")


def menu():
    while True:
        print("\n LOGIN SYSTEM ")
        print("1. Register")
        print("2. Login")
        print("3. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            register()

        elif pilihan == "2":
            login()

        elif pilihan == "3":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid!")


menu()