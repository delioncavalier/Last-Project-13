import time
# import pandas as pd
import os
import csv
"""
- menu daftar:
1. daftar sebagai admin
2. daftar sebagai petani
3. daftar sebagai pembeli
4. daftar pembeli tipe apa: Ibu Rumah Tangga, Anak Kosan, Pelaku Industri

- menu khusus admin:
1. menambah dan melihat data barang yang diinput petani (sm kaya menu petani)
2. melihat riwayat pembelian
3. melihat laporan penjualan
4. melihat laporan data barang (sm kek no 1)
5. melihat barang yang kurang diminati
6. melihat barang yang paling diminati
7. view data akun (nampilin akun2 dari csvnya)

- menu khusus pembeli:
1. input username, password, dan tipe pembeli
2. melihat produk di display oleh penjual berdasarkan tipe pembeli (Ibu Rumah Tangga, Anak Kosan, Pelaku Industri)
3. menambah produk yang ingin dibeli ke keranjang belanja
4. melakukan checkout
5. melakukan top up saldo
6. melakukan cek salldo
7. dapat melihat struk pembayaran (nama barang, jumlah barang, dan total harga barang yang dibeli)

- menu khusus petani(penjual):
1. crud barang, bisa nama, harga, dan stok barang
2. bisa memantau laporan penjualan, stok barang, pembelian, dll mirip kek admin
"""
data_semua_pengguna = "CSV/Data Pengguna/akun_admin.csv"
stok_data_barang = "CSV\Stok\data_barang.csv"
utama_data_jual_beli = "CSV\\Utama\\riwayat_jual_beli.csv"
data_pengguna = {}


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def cek_data_pengguna():
    if not data_pengguna:
        print("Belum ada pengguna yang terdaftar")
    else:
        print("\nList Data Pengguna Terdaftar:")
        for username, password in data_pengguna.items():
            print(f"Username: {username}, Password: {password}")
    
def validasi_username():
    while True:
        clear()
        username = input("Buat username (min. 4 karakter dan maks. 12 karakter): ").strip().lower()
        if len(username) < 4:
            print(f"Username terlalu pendek! Minimal {4} karakter.")
        elif len(username) > 12:
            print(f"Username terlalu panjang! Maksimal {12} karakter")
        else:
            return username


def validasi_password():
    while True:
        clear()
        password = input("Buat password (min. 6 karakter dan maks. 8 karakter): ").strip()
        if len(password) < 6:
            print(f"Paaword terlalu pendek! Minimal {6} karakter.")
        elif len(password) > 8:
            print(f"Password terlalu panjang! Maksimal {8} karakter.")
        else:
            konfirmasi_password = input("Konfirmasi password: ")
            if konfirmasi_password != password:
                print("Password tidak cocok!")
            else:
                return password

# validasi_password()

def pilih_tipe_user():
    """
    Sama aja, pecahan kek sebelume
    """
    print("\nPilih Tipe User:\n1. Admin\n2. Petani\n3. Pembeli")
    while True:
        """
        coba ini
        """
        tipe_user = input("Yuk dipilih! (1/2/3): ")
        clear()
        if tipe_user in ["1", "2", "3", "4"]:
            return tipe_user
        else:
            print(f"Pilihan {tipe_user} tidak valid. Silahkan pilih (1/2/3)!")
            pilih_tipe_user()
            input("Tekan enter untuk mencoba lagi...")
            


""""
pembeli, anak kos, irt, pelaku industri
pembeli, anak kos

with open("CSV\Data Pengguna\\akun_admin.csv", 'r') as apaja:
    writer = csv.writer(apaja)
    writer.writerow([tipe_pembeli])

n
"""
def pilih_tipe_pembeli():
    """fungsi milih pembeli bcz dipecah jd 3"""
    """
    pakai dicti katanya mas fauzan
    gabisa pakai "." wanjerrr
    dictionary tu unik, jadie hapus "."
    """
    list_tipe_pembeli = {
        "1" : "Anak Kosan",
        "2" : "Pembeli Warungan",
        "3" : "Pelaku Industri"
    }
    print("Yuk kak, mau jadi pembeli yang mana?: ")
    for tipe_pembeli, data in list_tipe_pembeli.items():
        print(f"{tipe_pembeli}. {data}")
    while True:
        tipe_pembeli = input("Yuk dipilih (1/2/3): ")
        if tipe_pembeli in list_tipe_pembeli:
            return list_tipe_pembeli[tipe_pembeli]
        else:
            print(f"Hey, pilihan {tipe_pembeli} tidak ada! Silahkan pilih (1/2/3)!")

def daftar():
    while True:
        clear()
        print("Halo, Selamat Datang di BumbuIn! Ayo Daftar Dulu!")
        username = validasi_username()
        if username in data_pengguna:
            input("Username sudah terdaftar! Silahkan gunakan username lain!")
            print("Daftar username yang tersedia: ")
            for nama_pengguna in data_pengguna:
                print(f"{nama_pengguna}")
        else:
            break
        
    password = validasi_password()
    data_pengguna[username] = password
    with open("CSV\\Data Pengguna\data_semuapengguna.csv", 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])
    print(f"\nHalo {username}!\nSilahkan pilih tipe user terlebih dahulu.")
    time.sleep(1)
    tipe_user = pilih_tipe_user()
    if not tipe_user:
        print("Tipe user tidak boleh kosong!")
        input("Tekan enter untuk mencoba lagi...")
        # return
    elif tipe_user == "3": #pembeli
        print(f"Halo {username}! Silahkan pilih tipe pembeli terlebih dahulu")
        time.sleep(1)
        tipe_pembeli = pilih_tipe_pembeli()
        print(f"Halo {username}! Kamu terdaftar sebagai {tipe_pembeli}")
    elif tipe_user == "2": #petani
        print(f"Halo {username}! Kamu terdaftar sebagai Petani")
    elif tipe_user == "1": #admin
        print(f"Halo {username}! Kamu terdaftar sebagai Admin")
    else:
        print("Tipe user yang kamu pilih tidak ada!")
        input("Tekan enter untuk mencoba lagi...")
        
def menu_admin(username):
    while True:
        clear()
        print(f"\nHalo {username}! mau ngapain di menu admin?")
        print("1. Tambah/Lihat Barang")
        print("2. Lihat Riwayat Pembelian")
        print("3. Lihat Laporan Penjualan")
        print("4. Lihat Stok Barang")
        print("5. Barang Kurang Diminati")
        print("6. Barang Paling Diminati")
        print("7. Ubah Password")
        print("8. Logout")
        
        admin_memilih = input("Yuk dipilih! (1-8)): ").strip()
        
        if admin_memilih == "1":
            pass
        elif admin_memilih == "2":
            pass
        elif admin_memilih == "3":
            pass
        elif admin_memilih == "4":
            pass
        elif admin_memilih == "5":
            pass
        elif admin_memilih == "6":
            pass
        elif admin_memilih == "7":
            pass
        elif admin_memilih == "8":
            return
        else:
            print("Wah, pilihan kamu tidak ada. Pilih ulang yaa!")
            
def menu_petani(username):
    while True:
        clear()
        print(f"\nHalo {username}! mau ngapain di menu petani?")
        print("1. Input Barang")
        print("2. Hapus Barang")
        print("3. Ubah Harga Barang")
        print("4. Laporan Penjualan")
        print("5. Laporan Stok Barang")
        print("6. Logout")
        
        petani_memilih = input("Yuk dipilih! (1-6): ").strip()
        if petani_memilih == "1": #input barang
            pass
        elif petani_memilih == "2": #hapus barang
            pass
        elif petani_memilih == "3": #ubah harga
            pass
        elif petani_memilih == "4": #laporan penjualan
            pass
        elif petani_memilih == "5": #laporan stok
            pass
        elif petani_memilih == "6": #logout (kembali ke menu utama)
            return


def menu_pembeli(username, tipe_pembeli):
    while True:
        clear()
        print(f"\nHalo {username}! Kamu mau ngapain sebagai {tipe_pembeli}?")
        print("1. Lihat produk sesuai kategori")
        print("2. Tambah produk ke keranjang")
        print("3. Checkout belanja")
        print("4. Top up saldo")
        print("5. Cek saldo")
        print("6. Lihat struk pembayaran")
        print("0. Keluar")
        pembeli_memilih = input("Yuk dipilih! (1-6): ").strip()
        if pembeli_memilih == "1":
            pass
        elif pembeli_memilih == "2":
            pass
        elif pembeli_memilih == "3":
            pass
        elif pembeli_memilih == "4":
            pass
        elif pembeli_memilih == "5":
            pass
        elif pembeli_memilih == "6":
            pass
        elif pembeli_memilih == "0":
            return
        else:
            print("Wah, pilihan kamu tidak ada. Pilih ulang yaa!")
            
def login():      
    """
    login coy
    """
    while True:
        clear()
        panjang_tabel = 40
        print(f"+{"="*panjang_tabel}+")
        print(f"|{'Selamat Datang di Login Menu Bumbuln':^{panjang_tabel}}|")
        print(f"|{'Silahkan login terlebih dahulu.':^{panjang_tabel}}|")
        print(f"+{"="*panjang_tabel}+")
        # print("\nSelamat Datang di Login Menu Bumbuln\nSilahkan login terlebih dahulu.")
        username = input("Masukkan username: ").strip().title()
        password = input("Masukkan password: ").strip()
        
        
        if not username or not password:
            print("Username atau password tidak boleh kosong!")
            input("Tekan enter untuk mencoba lagi...")
            # time.sleep(2)
            continue
        """
        validasi 2
        """
        if username in data_pengguna:
            if data_pengguna[username] == password:
                print(f"Halo, {username}! Kamu berhasil login.")
                # time.sleep(1)
                return username
            else:
                print("Password salah!")
                input("Tekan enter untuk mencoba lagi...")
                # time.sleep(2)
        else:
            print("Username tidak ditemukan.")
            input("Silahkan daftar terlebih dahulu...")
            daftar()
            return
            # time.sleep(2)
                
def menu_utama():
    while True:
        clear()
        try:
            nama_aplikasi = "Selamat Datang di BumbuIn"
            panjang_tabel = len(nama_aplikasi) + 20
            print(f"\n{"=" * panjang_tabel}")
            print(f"| {nama_aplikasi.center(panjang_tabel-4)} |")
            print(f"{"=" * panjang_tabel}")
            
            print(f"+{"="*4}+{"="*(panjang_tabel-6)}+")
            print(f"| {"No":<2} | {"Menu":<{panjang_tabel-8}} |")
            print(f"+{"="*4}+{"="*(panjang_tabel-6)}+")
            
            print(f"| {"1":<2} | {"Daftar":<{panjang_tabel-8}} |")
            print(f"| {"2":<2} | {"Login":<{panjang_tabel-8}} |")
            print(f"| {"0":<2} | {"Keluar":<{panjang_tabel-8}} |")
            print(f"+{"="*4}+{"="*(panjang_tabel-6)}+")
        
            pilih_awal = input("Silahkan pilih menu yang sesuai (0/1/2): ")
            if pilih_awal == "1":
                daftar()
            elif pilih_awal == "2":
                username, tipe_pembeli = login()
                if tipe_pembeli == "Admin":
                    menu_admin(username)
                elif tipe_pembeli == "Petani":
                    menu_petani(username)
                elif tipe_pembeli in ["Anak Kosan", "Pembeli Warungan", "Pelaku Industri"]:
                    menu_pembeli(username, tipe_pembeli)
                else:
                    print("Waduh, tipe pembeli tidak ditemukan!")
                    input("Tekan enter untuk mencoba lagi...")
            elif pilih_awal == "0":
                print("Terima kasih sudah berbelanja!\nProgram akan berhenti dalam hitungan...")
                for i in reversed(range(3)):
                    i += 1
                    print(f"{i}...")
                    time.sleep(1)
                break
            else:
                print("Angka yang kamu masukkan tidak sesuai! Silahkan pilih ulang")
                time.sleep(2)
                continue
        except KeyboardInterrupt:
            print("\nProgram dihentikan oleh pengguna!")
            break
            
menu_utama()
