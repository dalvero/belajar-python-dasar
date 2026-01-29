# LATIHAN PROGRAM LIST BUKU (MENAMBAHKAN)

import utility as util

# NESTED LIST BUKU DAN PENULIS 
buku = []

# LOOPING PROGRAM
isExit = False

while isExit == False :
    util.clear_screen()
    util.print_title("PROGRAM LIST BUKU")

    # VALIDASI ISI LIST BUKU
    if len(buku) == 0 :
        print("Kamu tidak punya list buku")
    else :
        print(f"List buku kamu saat ini ada {len(buku)} buku.")

    # USER INPUT
    print("Tambahkan list buku :")
    input_buku = input("Judul buku\t: ")
    penulis_buku = input("Penulis buku\t: ")

    # VALIDATION BUKU YANG SUDAH ADA
    isExist = False
    for listBook in buku :
        if input_buku.lower() == listBook[0].lower() :
            isExist = True
            print(f"Buku dengan judul '{input_buku}' sudah ada di list buku kamu")
            print("Tidak dapat menambahkan buku yang sama")
            print("Silahkan coba lagi")
            break

    # JIKA BUKU BELUM ADA, MASUKAN KE LIST BUKU
    if not isExist :
        # MEMASUKAN DATA BUKU KE LIST BUKU
        info_buku = [input_buku, penulis_buku]
        buku.append(info_buku)
        print("Buku berhasil ditambahkan")
    
    # PRINT LIST BUKU
    util.print_divider()
    util.print_title("LIST BUKU", " ")
    util.print_divider()
    
    # PRINT TABLE BUKU
    print(f"|{'No'.center(6)}|{'Judul Buku'.center(25)}|{'Penulis Buku'.center(25)}|") # HEADER TABLE
    util.print_divider()
    number = 1
    for listBook in buku :
        print(f"|{str(number).center(6)}|{str(listBook[0]).center(25)}|{str(listBook[1]).center(25)}|")
        number+=1
    util.print_divider()

    # IS AGAIN
    isAgain = input("Ingin tambah buku lagi? (y/n)\t: ")
    
    # VALIDATION EXIT / AGAIN
    if isAgain == "y" or isAgain == "Y":
        isExit = False
    elif isAgain == "n" or isAgain == "N":
        print("Program Berakhir")
        isExit = True
    else :
        print("Input tidak diketahui")
        isExit = True
    
