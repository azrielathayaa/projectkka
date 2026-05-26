# Login System Python

## Deskripsi
Program ini adalah sistem login sederhana menggunakan bahasa Python.

Fitur yang tersedia:
- Register akun
- Login akun
- Validasi username dan password
- Batas percobaan login 3 kali
- Menu interaktif sederhana

---

## Code Program

```python
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
```

---

## Cara Menjalankan Program

### 1. Install Python
Download Python di website resmi:

https://www.python.org/

---

### 2. Simpan File
Contoh nama file:

```bash
login_system.py
```

---

### 3. Jalankan Program

Buka terminal lalu ketik:

```bash
python login_system.py
```

---

## Contoh Output

```text
LOGIN SYSTEM
1. Register
2. Login
3. Keluar

Pilih menu: 1

REGISTER
Buat Username : admin
Buat Password : 123

Register berhasil!
```

---

## Penjelasan Function

### `register()`
Function untuk membuat akun baru.

### `login()`
Function untuk login menggunakan akun yang sudah dibuat.

### `menu()`
Function utama untuk menampilkan menu program.

---

## Materi Python yang Digunakan
- Variable
- Function
- Global Variable
- If Else
- While Loop
- Input Output

---

## Kekurangan Program
Program ini masih sederhana karena:
- Data belum tersimpan permanen
- Password belum dienkripsi
- Hanya bisa menyimpan 1 akun
- Belum menggunakan database

---

## Author
Dibuat menggunakan Python.
