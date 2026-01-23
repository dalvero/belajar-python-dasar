# LATIHAN PERULANGAN SEGITIGA

import utility as util

isExit = False

while isExit == False :
    # CLEAR SCREEN
    util.clear_screen()

    # PRINT TITLE
    util.print_title("PROGRAM PERULANGAN SEGITIGA")
    
    # INPUT USER
    num = int(input("Masukan besar segitiga : "))

    # LINE SPACE
    print("")

    # LOGIC LOOPING
    util.print_title("SEGITIGA SIKU KIRI")

    # 1. SEGITIGA SIKU KIRI
    for i in range(1, num + 1):
        for j in range (i, 0, -1) :
            print("*", end ="")
        print("")
        
    util.print_title("SEGITIGA SAMA KAKI")

    # 2. SEGITIGA SAMA SISI
    for i in range(num+1, 1, -1):
        for j in range(i-1, 0, -1) :
            print(" ", end = "")
        for k in range(i - num , num - i + 3):
            print("*", end = "")
        print("")
        
    util.print_title("SEGITIGA SIKU KANAN")

    # 3. SEGITIGA SIKU KANAN
    for i in range(num+1, 1, -1):
        for j in range(i-1, 0, -1) :
            print(" ", end = "")
        for k in range(i - num + (num - 1), num + 1):    
            print("*", end = "")
        print("")

    util.print_divider()

    # APAKAH ULANGI?
    isAgain = input("Apakah anda ingin mengulangi program (y/n)?\t: ")
    if isAgain == "y" or isAgain == "Y" :
        isExit = False
        util.clear_screen()
    elif isAgain == "n" or isAgain == "N" :
        isExit = True
    else : 
        print("Input tidak dikenali, program akan dihentikan.")
        isExit = True

print("")        
# PRINT ENDING
ending = "PROGRAM BERAKHIR"
print(ending.center(60, "="))

