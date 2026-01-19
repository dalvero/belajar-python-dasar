# LATIHAN KOMPARASI DAN LOGIKA
# MEMBUAT GABUNGAN AREA RENTANG DARI ANGKA 
# 1. x < 3 || x > 10
# 2. x > 3 && x < 10

# PROGRAM KOMPARASI DAN LOGIKA

# PRINT TITLE
print("\n===PROGRAM CEK ANGKA KOMPARASI===")

# INPUT USER
user_input = float(input("1. Masukan angka kurang dari 3 atau lebih dari 10\n>  "))

# LOGIKA KOMPARASI
is_kurang = user_input < 3 # FIRST VALIDATION
is_lebih =  user_input > 10 # SECOND VALIDATION
is_sesuai = is_kurang or is_lebih # FINAL VALIDATION

# PRINT RESULT
print("> Kurang dari 3 =", is_kurang)
print("> Lebih dari 10 =", is_lebih)
print("> Hasil akhir anda =",is_sesuai)

user_input = float(input("\n2. Masukan angka lebih dari 3 dan kurang dari 10\n>  "))

is_kurang = user_input < 10 # FIRST VALIDATION
is_lebih =  user_input > 3 # SECOND VALIDATION
is_sesuai = is_kurang and is_lebih # FINAL VALIDATION

# PRINT RESULT
print("> Lebih dari 3 =", is_lebih)
print("> Kurang dari 10 =", is_kurang)
print("> Hasil akhir anda adalah",is_sesuai)


