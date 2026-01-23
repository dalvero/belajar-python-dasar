# LATIHAN PERCABANGAN IF ELSE KALKULATOR SEDERHANA 

# PRINT TIITLE
title = "PROGRAM KALKULATOR SEDERHANA"
print(title.center(60, "="))

# INPUT USER
num_1 = float(input("Masukan angka pertama\t\t\t: "))
operator = input("Masukan operator (+ | - | * | /)\t: ")
num_2 = float(input("Masukan angka kedua\t\t\t: "))

# CALCULATE CONDITION
hasil = 0

if operator == "+" : hasil = num_1 + num_2
elif operator == "-" : hasil = num_1 - num_2
elif operator == "*" : hasil = num_1 * num_2
elif operator == "/" : hasil = num_1 / num_2
else : 
    warning = "Operator tidak ditemukan"
    print(warning.center(60, "-"))
    hasil = 0

# PRINT HASIL
print("-" * 60)
print(f"Hasil\t\t\t\t\t: {hasil}")
ending = "PROGRAM BERAKHIR"
print(ending.center(60, "="))