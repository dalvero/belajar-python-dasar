# LATIHAN PROGRAM FUNGSI MENGHITUNG LUAS DAN KELILING BANGUN DATAR
# 1. PERSEGI 
# 2. PERSEGI PANJANG
# 3. SEGITIGA
# 4. LINGKARAN

# IMPORT LIBRARY
import utility as util
import time as tm

# LIST MENU
main_menu = [
    "Persegi",
    "Persegi Panjang",
    "Segitiga Sama Sisi",
    "Lingkaran",
    "Keluar"
]

# FUNCTION DISPLAY MENU
def display_menu(list_menu):
    # PRINT MENU
    no = 1
    for menu in main_menu :
        print(f"{no}. {menu}") 
        no += 1
        # BUAT PILIHAN TERAKHIR (Keluar Program) MENJADI PILIHAN NO 0
        if no == len(main_menu) :
            no = 0

# VALIDATION INPUT USER
def input_validation(user_input, list_menu):
    # VALIDATION INT TYPE
    try : 
        option = int(user_input)

        if option >= 0 and option < len(list_menu):
            return True, user_input
        else :
            print("> Input tidak ditemukan, silahkan ulangi!")
            return False, user_input        
    except :
        print("> Input tidak sesuai, silahkan ulangi!")
        return False, user_input
    
# PERSEGI
def persegi():
    util.clear_screen()

    # PRINT TITLE     
    util.print_divider("=")    
    util.print_title("Hitung Luas dan Keliling Persegi", " ")    
    util.print_divider("=")

    # ERROR HANDLING & USER INPUT
    try :
        sisi = int(input("1. Masukan sisi persegi\t: "))
        util.print_divider("-")
        print(f"> Hasil keliling persegi\t: {sisi * 4}")
        print(f"> Hasil luas persegi\t\t: {sisi * sisi}")        
    except :
        util.print_divider("-")
        print("> Input tidak sesuai, silahkan ulangi")
        print("> Hasil tidak ditemukan.")   

    util.print_divider("=")
    tm.sleep(3)

# PERSEGI PANJANG
def persegi_panjang():
    util.clear_screen()

    # PRINT TITLE     
    util.print_divider("=")    
    util.print_title("Hitung Luas dan Keliling Persegi Panjang", " ")    
    util.print_divider("=")

    # ERROR HANDLING & USER INPUT
    try :
        panjang = int(input("1. Masukan panjang persegi panjang\t: "))
        lebar = int(input("2. Masukan lebar persegi panjang\t: "))
        util.print_divider("-")
        print(f"> Hasil keliling perseg panjangi\t: {2 * (panjang * lebar)}")
        print(f"> Hasil luas persegi panjang\t\t: {panjang * lebar}")        
    except :
        util.print_divider("-")
        print("> Input tidak sesuai, silahkan ulangi")
        print("> Hasil tidak ditemukan.")   

    util.print_divider("=")
    tm.sleep(3)

# SEGITIGA
def segitiga():
    util.clear_screen()

    # PRINT TITLE     
    util.print_divider("=")    
    util.print_title("Hitung Luas dan Keliling Segitiga Sama Sisi", " ")    
    util.print_divider("=")

    # ERROR HANDLING & USER INPUT
    try :
        sisi = int(input("1. Masukan sisi segitiga sama sisi\t: "))
        tinggi = int(input("2. Masukan tinggi segitiga sama sisi\t: "))        
        util.print_divider("-")
        print(f"> Hasil keliling segitiga sama sisi\t: {sisi + sisi + sisi}")
        print(f"> Hasil luas segitiga sama sisi\t\t: {float((sisi * tinggi) / 2)}")        
    except :
        util.print_divider("-")
        print("> Input tidak sesuai, silahkan ulangi")
        print("> Hasil tidak ditemukan.")   

    util.print_divider("=")
    tm.sleep(3)

def lingkaran():
    util.clear_screen()

    # PRINT TITLE     
    util.print_divider("=")    
    util.print_title("Hitung Luas dan Keliling Lingkaran", " ")    
    util.print_divider("=")

    PHI = 22 / 7

    # ERROR HANDLING & USER INPUT
    try :
        jari_jari = float(input("1. Masukan jari-jari lingkaran\t: "))        
        util.print_divider("-")
        print(f"> Hasil keliling lingkaran\t: {float(2 * PHI * jari_jari):.2f}")
        print(f"> Hasil luas lingkaran\t\t: {float(PHI * (jari_jari * jari_jari)):.2f}")        
    except :
        util.print_divider("-")
        print("> Input tidak sesuai, silahkan ulangi")
        print("> Hasil tidak ditemukan.")   

    util.print_divider("=")
    tm.sleep(3)

# IS EXIT
isExit = False

# PROGRAM LOOPING
while not isExit :
    util.clear_screen()

    # PRINT TITLE     
    util.print_divider("=")
    util.print_title("Selamat Datang di Program", " ")
    util.print_title("Hitung Luas dan Keliling Bangun Datar", " ")    
    util.print_divider("=")

    # PRINT MENU
    display_menu(main_menu)

    # USER INPUT
    util.print_divider("=")
    user_input = input("> Silahkan pilih bangun datar (1-4) : ")

    # VALIDATION USER INPUT
    isValid, user_option = input_validation(user_input, main_menu)

    if isValid :        
        # CONDITION
        if int(user_option) == 1 :
            persegi()
            tm.sleep(2)
        elif int(user_option) == 2 :
            persegi_panjang()
            tm.sleep(2)
        elif int(user_option) == 3 :
            segitiga()
            tm.sleep(2)
        elif int(user_option) == 4 :
            lingkaran()
            tm.sleep(2)
        elif int(user_option) == 0 :
            print(f"> Anda telah keluar dari program.")
            tm.sleep(2)
            isExit = True
    elif not isValid :
        isExit = False
        tm.sleep(2)    
    else :
        print("Terjadi kesalah di dalam program ini")    

