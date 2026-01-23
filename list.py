# LIST 

# KUMPULAN DATA NUMBERS
data_angka = [1, 5, 2, 3]
print(data_angka)

# KUMPULAN DATA STRING
data_string = ["ucup", "otong", "odah"]
print(data_string)

# KUMPULAN DATA BOOLEAN
data_boolean = [True, False, True, True]
print(data_boolean)

# KUMPULAN DATA CAMPURAN
data_campuran = [1, "bala-bala", 2, "cireng", "ucup", True, "odah"]
print(data_campuran)

## CARA ALTERNATIF MEMBUAT LIST
data_range = range(0, 10, 2) # range(start, stop, step)
print(data_range)
data_list = list(data_range)
print(data_list)

# MEMBUAT LIST DENGAN FOR LOOP, LIST COMPREHENSION
list_pake_for = [i**2 for i in range(0, 10)]
print(list_pake_for)

# MEMBUAT LIST PAKE FOR PAKE IF
list_pake_for_if = [i for i in range(0, 10) if i != 5]
print(list_pake_for_if)

# MEMBUAT LIST PAKE FOR PAKE IF UNTUK BILANGAN GENAP
list_pake_for_if_genap = [i for i in range(0, 10) if i % 2 == 0]
print(list_pake_for_if_genap)

# MEMBUAT LIST PAKE FOR PAKE IF UNTUK BILANGAN GANJIL
list_pake_for_if_ganjil = [i for i in range(0, 10) if i % 2 != 0]
print(list_pake_for_if_ganjil)