# LATIHAN PALINDROME

import utility as util

# PROGRAM LOOPING 
isExit = False
while isExit == False :
    # CLEAR SCREEN
    util.clear_screen()

    # PRINT TITLE
    util.print_title("PROGRAM PALINDROME")

    # INPUT USER
    user_string = input("Masukan kata atau kalimat\n> ")

    # HILANGKAN SPASI DI AWAL DAN AKHIR KALIMAT
    user_string.strip()

    # HILANGKAN SPASI DI TENGAH KALIAMAT
    no_space_string = []    
    clear_string = ""
    for i in user_string:
        if i == " ":        
            continue
        else :
            no_space_string += i # LIST HURUF DARI USER STRING
    
    # KALIMAT YANG SUDAH BERSIH
    for i in range(len(no_space_string) - 1, -1, -1):
        clear_string += no_space_string[i]

    # MEMBALIK KATA/KALIMAT
    reversed_string = ""
    for i in range(len(no_space_string) - 1, -1, -1):
        reversed_string += no_space_string[i]

    # PALINDROME CHECK
    isPalindrome = False
    result = ""
    if reversed_string == clear_string:
        isPalindrome = True
        result = f"Kata/kalimat anda adalah Palindrome."
    else :
        isPalindrome = True
        result = f"Kata/kalimat anda bukan Palindrome."

    # PRINT RESULT
    print(result)

    util.print_divider()

    # APAKAH ULANGI?
    isAgain = input("Apakah anda ingin mengulangi program (y/n)\t: ")

    if isAgain == "y" or isAgain == "Y" :
        isExit = False
    elif isAgain == "n" or isAgain == "N" :
        isExit = True

util.print_title("PROGRAM BERAKHIR")