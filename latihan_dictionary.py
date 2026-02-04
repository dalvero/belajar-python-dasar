# LATIHAN CRUD DATA MAHASISWA MENGGUNAKAN DICTIONARY 
# 1. TANPA FUNCTION ATAU CLASS 
# 2. TANPA VALIDATION INPUT MENU
# Senin, 2 Feb 2026, Yunseong

# IMPORT MODULE PENDUKUNG
import datetime as dt
import utility as util
import string as str # UNTUK MENGHASILKAN KEY RANDOM
import random as rd # UNTUK MENGHASILKAN KEY RANDOM
import time as tm

# MAIN MENU PROGRAM
main_menu = [
    "Lihat Data Mahasiswa",
    "Tambah Data Mahasiswa",
    "Ubah Data Mahasiswa",
    "Hapus Data Mahasiswa",
    "Keluar Program"
]

# EXIT VARIABLE
isExit = False

# DATA TEMPLATE
mahasiswa_template = {
    'nama' : 'nama',
    'nim' : 'nim',
    'sks_lulus' : 0,
    'lahir' : dt.datetime(1111, 1, 11)
}

# DICTIONARY UNTUK MENAMPUNG DATA MAHASISWA (SIMPLE REPOSITORY)
data_mahasiswa = {}

# LOOPING PROGRAM

while not isExit : 
    # CLEAR SCREEN
    util.clear_screen()

    # PRINT TITLE
    util.print_divider("=")
    util.print_title("Selamat Datang di Program", " ")
    util.print_title("CRUD Data Mahasiswa", " ")
    util.print_divider("=")

    # PRINT MENU
    no = 1
    for menu in main_menu :
        print(f"{no}. {menu}") 
        no += 1
        # BUAT PILIHAN TERAKHIR (Keluar Program) MENJADI PILIHAN NO 0
        if no == len(main_menu) :
            no = 0
    
    # INPUT USER
    util.print_divider("=")
    pilihan = int(input(f"> Masukan pilihan 1-{len(main_menu) - 1} : "))
    
    # VALIDATION BATASAN PILIHAN MENU
    if pilihan <= len(main_menu) - 1 and pilihan >= 0 :
        # KONDISI PILIHAN PROGRAM
        if pilihan == 1 :
            # LIHAT DATA MAHASISWA
            
            # PRINT TITLE
            util.clear_screen()
            util.print_divider("=")
            util.print_title("Lihat Data Mahasiswa", " ")            
            util.print_divider("=")

            # CEK DATA MAHASISWA ADA / TIDAK
            if len(data_mahasiswa) == 0 :
                print("> Data Mahasiswa Tidak Ditemukan")
                print("> Silahkan Tambah Data Mahasiswa Terlebih Dahulu")
            else :
                # PRINT HEADER TABLE                
                print(f"{'No':^3} | {'Key ID':^6} | {'Nama':<20} | {'SKS':^5} | {'Tanggal Lahir':<12}")
                util.print_divider("-")

                # PRINT DATA MAHASISWA
                no = 1
                for mahasiswa in data_mahasiswa :
                    KEY = mahasiswa
                    NAMA = data_mahasiswa[KEY]['nama']
                    SKS = data_mahasiswa[KEY]['sks_lulus']
                    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%d-%m-%y")
    
                    print(f"{no:^3} | {KEY:^6} | {NAMA:<20} | {SKS:^5} | {LAHIR:<12}")
                    no += 1

                util.print_divider("=")

            # WAITING PROCCESS
            tm.sleep(2)
            pass
        elif pilihan == 2 :
            # TAMBAH DATA MAHASISWA

            # PRINT TITLE
            util.clear_screen()
            util.print_divider("=")
            util.print_title("Tambah Data Mahasiswa", " ")            
            util.print_divider("=")

            # INPUT DATA MAHASISWA
            KEY = ''.join((rd.choice(str.ascii_uppercase) for i in range(6))) # GENERATE KEY RANDOM
            data_temp = dict.fromkeys(mahasiswa_template.keys()) # COPY KEY DARI TEMPLATE
            data_temp['nama'] = input("1. Masukan Nama Mahasiswa\t: ")
            data_temp['nim'] = input("2. Masukan NIM Mahasiswa\t: ")
            data_temp['sks_lulus'] = int(input("3. SKS Lulus\t: "))
            TAHUN_LAHIR = int(input("3. Tanggal Lahir :\n\t> Tahun Lahir (YYYY)\t\t: "))
            BULAN_LAHIR = int(input("\t> Bulan Lahir (1 - 12)\t\t: "))
            TANGGAL_LAHIR = int(input("\t> Tanggal Lahir (1 - 31)\t: "))
            data_temp['lahir'] = dt.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)

            data_mahasiswa.update({KEY:data_temp})
            print("> Data Mahasiswa Berhasil Ditambahkan.")            
            tm.sleep(2)
            pass
        elif pilihan == 3 :
            # UBAH DATA MAHASISWA

            # PRINT TITLE
            util.clear_screen()
            util.print_divider("=")
            util.print_title("Ubah Data Mahasiswa", " ")            
            util.print_divider("=")

            # CEK DATA MAHASISWA ADA / TIDAK
            if len(data_mahasiswa) == 0 :
                print("> Data Mahasiswa Tidak Ditemukan")
                print("> Silahkan Tambah Data Mahasiswa Terlebih Dahulu")
                tm.sleep(2)
                pass
            else :
                # PRINT HEADER TABLE                
                print(f"{'No':^3} | {'Key ID':^6} | {'Nama':<20} | {'SKS':^5} | {'Tanggal Lahir':<12}")
                util.print_divider("-")

                # PRINT DATA MAHASISWA
                no = 1
                for mahasiswa in data_mahasiswa :
                    KEY = mahasiswa
                    NAMA = data_mahasiswa[KEY]['nama']
                    SKS = data_mahasiswa[KEY]['sks_lulus']
                    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%d-%m-%y")

                    print(f"{no:^3} | {KEY:^6} | {NAMA:<20} | {SKS:^5} | {LAHIR:<12}")
                    no += 1
                util.print_divider("=")

                # INPUT KEY MAHASISWA YANG INGIN DIUBAH
                key_mahasiswa = input("> Masukan Key ID Mahasiswa yang ingin dihapus\t: ")  
                # CEK KEY EXIST ATAU TIDAK
                isExist = key_mahasiswa in data_mahasiswa
                if isExist :
                    # JIKA KEY DITEMUKAN, CEK DATA MAHASISWA BERDASARKAN KEY
                    print("> Data Mahasiswa ditemukan. Silahkan ubah data dibawah ini :")
                    data_to_update = data_mahasiswa[key_mahasiswa]
                    data_to_update['nama'] = input(f"1. Ubah Nama Mahasiswa ({data_to_update['nama']})\t: ") or data_to_update['nama']
                    data_to_update['nim'] = input(f"2. Ubah NIM Mahasiswa ({data_to_update['nim']})\t: ") or data_to_update['nim']
                    data_to_update['sks_lulus'] = int(input(f"3. Ubah SKS Lulus ({data_to_update['sks_lulus']})\t: ")) or data_to_update['sks_lulus']
                    TAHUN_LAHIR = input(f"4. Ubah Tahun Lahir ({data_to_update['lahir'].year})\t: ") or data_to_update['lahir'].year
                    BULAN_LAHIR = input(f"   Ubah Bulan Lahir ({data_to_update['lahir'].month})\t: ") or data_to_update['lahir'].month
                    TANGGAL_LAHIR = input(f"   Ubah Tanggal Lahir ({data_to_update['lahir'].day})\t: ") or data_to_update['lahir'].day
                    data_to_update['lahir'] = dt.datetime(int(TAHUN_LAHIR), int(BULAN_LAHIR), int(TANGGAL_LAHIR))
                    data_mahasiswa.update({key_mahasiswa:data_to_update})
                    print("> Data Mahasiswa Berhasil Diubah.")
                else :
                    print("> Key ID Mahasiswa tidak ditemukan.\n> Silahkan ulangi kembali.")
                tm.sleep(2)
                pass
        elif pilihan == 4 :
            # HAPUS DATA MAHASISWA

            # PRINT TITLE
            util.clear_screen()
            util.print_divider("=")
            util.print_title("Hapus Data Mahasiswa", " ")            
            util.print_divider("=")
            # CEK DATA MAHASISWA ADA / TIDAK
            if len(data_mahasiswa) == 0 :
                print("> Data Mahasiswa Tidak Ditemukan")
                print("> Silahkan Tambah Data Mahasiswa Terlebih Dahulu")
                tm.sleep(2)
                pass
            else :
                # PRINT HEADER TABLE                
                print(f"{'No':^3} | {'Key ID':^6} | {'Nama':<20} | {'SKS':^5} | {'Tanggal Lahir':<12}")
                util.print_divider("-")

                # PRINT DATA MAHASISWA
                no = 1
                for mahasiswa in data_mahasiswa :
                    KEY = mahasiswa
                    NAMA = data_mahasiswa[KEY]['nama']
                    SKS = data_mahasiswa[KEY]['sks_lulus']
                    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%d-%m-%y")

                    print(f"{no:^3} | {KEY:^6} | {NAMA:<20} | {SKS:^5} | {LAHIR:<12}")
                    np += 1

                util.print_divider("=")

                # INPUT KEY MAHASISWA YANG INGIN DIUBAH
                key_mahasiswa = input("> Masukan Key ID Mahasiswa yang ingin dihapus\t: ")

                # CEK KEY EXIST ATAU TIDAK
                isExist = key_mahasiswa in data_mahasiswa
                if isExist :
                    # JIKA KEY DITEMUKAN, HAPUS DATA MAHASISWA BERDASARKAN KEY
                    del data_mahasiswa[key_mahasiswa]
                    print("> Data Mahasiswa Berhasil Dihapus.")
                else :
                    print("> Key ID Mahasiswa tidak ditemukan.\n> Silahkan ulangi kembali.")
                tm.sleep(2)
                pass
        elif pilihan == 0 :
            print("Keluar Program")
            tm.sleep(2)
            isExit = True
    else :
        print("> Pilihan tidak ditemukan.\n> Silahkan ulangi")
        tm.sleep(2)
        isExit = False

    