import time
import os
import csv

# File paths untuk menyimpan data
data_semua_pengguna = "CSV/Data Pengguna/akun_admin.csv"
stok_data_barang = "CSV\Stok\data_barang.csv"
utama_data_jual_beli = "CSV\\Utama\\riwayat_jual_beli.csv"


# Menyimpan data pengguna sementara
data_pengguna = {}

# Fungsi untuk membersihkan layar
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Fungsi untuk menampilkan semua pengguna terdaftar
def cek_data_pengguna():
    if not data_pengguna:
        print("Belum ada pengguna yang terdaftar.")
    else:
        print("\nList Data Pengguna Terdaftar:")
        for username, password in data_pengguna.items():
            print(f"Username: {username}, Password: {password}")

# Fungsi untuk memvalidasi username
def validasi_username():
    while True:
        # clear()
        username = input("Buat username (min. 4 karakter dan maks. 12 karakter): ").strip().lower()
        if len(username) < 4:
            print("Username terlalu pendek! Minimal 4 karakter.")
        elif len(username) > 12:
            print("Username terlalu panjang! Maksimal 12 karakter.")
        else:
            return username

# Fungsi untuk memvalidasi password
def validasi_password():
    while True:
        # clear()
        password = input("Buat password (min. 6 karakter dan maks. 8 karakter): ").strip()
        if len(password) < 6:
            print("Password terlalu pendek! Minimal 6 karakter.")
        elif len(password) > 8:
            print("Password terlalu panjang! Maksimal 8 karakter.")
        else:
            konfirmasi_password = input("Konfirmasi password: ")
            if konfirmasi_password != password:
                print("Password tidak cocok!")
            else:
                return password

# Fungsi untuk memilih tipe pengguna
def pilih_tipe_user():
    print("\nPilih Tipe User:\n1. Admin\n2. Petani\n3. Pembeli")
    while True:
        tipe_user = input("Yuk dipilih! (1/2/3): ")
        clear()
        if tipe_user in ["1", "2", "3"]:
            return tipe_user
        else:
            print(f"Pilihan {tipe_user} tidak valid. Silahkan pilih (1/2/3)!")

# Fungsi untuk memilih tipe pembeli
def pilih_tipe_pembeli():
    list_tipe_pembeli = {
        "1": "Anak Kosan",
        "2": "Pembeli Warungan",
        "3": "Pelaku Industri"
    }
    print("Yuk kak, mau jadi pembeli yang mana?:")
    for tipe_pembeli, data in list_tipe_pembeli.items():
        print(f"{tipe_pembeli}. {data}")
    while True:
        tipe_pembeli = input("Yuk dipilih (1/2/3): ")
        if tipe_pembeli in list_tipe_pembeli:
            return list_tipe_pembeli[tipe_pembeli]
        else:
            print(f"Hey, pilihan {tipe_pembeli} tidak ada! Silahkan pilih (1/2/3)!")

# Fungsi untuk pendaftaran pengguna baru
def daftar():
    while True:
        clear()
        print("Halo, Selamat Datang di BumbuIn! Ayo Daftar Dulu!")
        username = validasi_username()
        if username in data_pengguna:
            print("Username sudah terdaftar! Silahkan gunakan username lain.")
        else:
            break

    password = validasi_password()
    data_pengguna[username] = password

    # Menyimpan data pengguna ke file CSV
    with open("CSV/Data Pengguna/data_semuapengguna.csv", 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])

    print(f"\nHalo {username}! Silahkan pilih tipe user terlebih dahulu.")
    time.sleep(1)
    tipe_user = pilih_tipe_user()
    if tipe_user == "3":  # Pembeli
        tipe_pembeli = pilih_tipe_pembeli()
        print(f"Halo {username}! Kamu terdaftar sebagai {tipe_pembeli}")
    elif tipe_user == "2":  # Petani
        print(f"Halo {username}! Kamu terdaftar sebagai Petani")
    elif tipe_user == "1":  # Admin
        print(f"Halo {username}! Kamu terdaftar sebagai Admin")

# Fungsi untuk menu utama
def menu_utama():
    while True:
        clear()
        try:
            print("\nSelamat Datang di BumbuIn")
            print("1. Daftar")
            print("2. Login")
            print("0. Keluar")

            pilih_awal = input("Silahkan pilih menu yang sesuai (0/1/2): ")
            if pilih_awal == "1":
                daftar()
            elif pilih_awal == "2":
                print("Fungsi login belum diimplementasikan sepenuhnya.")
            elif pilih_awal == "0":
                print("Terima kasih sudah berbelanja!\nProgram akan berhenti...")
                for i in range(3, 0, -1):
                    print(f"{i}...")
                    time.sleep(1)
                break
            else:
                print("Pilihan tidak valid! Silahkan coba lagi.")
        except KeyboardInterrupt:
            print("\nProgram dihentikan oleh pengguna!")
            break

# Menjalankan program
if __name__ == "__main__":
    menu_utama()