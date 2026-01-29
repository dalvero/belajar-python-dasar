## OPERASI

# INDEX 0(-3), 1(-2), 2(-1)
data = ["Ucup", "Otong", "Dudung"]

# MENGAMBIL DATA DARI LIST INI
data_0 = data[0]
print(f"Data pertama (index 0) = {data-0}")

data_terakhir = data[-1]
print(f"Data terakhir adalah = {data_terakhir}")

data_ucup = data[-3]
print(f"Data ucup = {data_ucup}")

# MENGAMBIL INFO JUMLAH DATA DALAM LIST
panjang_data = len(data)
print(f"Panjang data = {panjang_data}")

## MANIMPULASI DATA

# MENAMBAHKAN ITEM PADA LIST SESUAI POSISI
print(f"Data sebelum ditambah = \n{data}")

data.insert(1, "Asep")
print(f"Data sesudah ditambah = \n{data}")

# MENAMBAH DI AKHIR LIST
data.append("Jajang")
print(f"Data ditambah lagi = \n{data}")

# MENAMBAH LIST DENGAN LIST
data_baru = ["Ujang", "Usep", "Dadang"]
data.extend(data_baru)
print(f"Data gabungan = \n{data}")

# MERUBAH DATA
# MERUBAH DATA 2 MENJADI MICHAEL
data[2] = "Michael"
print(f"Data rubah = \n{data}")

# MEREMOVE DATA
data.remove("Ujang")
print(f"Data remove = \n{data}")
# data.remove("usep") AKAN ERROR KARENA DATA TIDAK SAMA

# MEREMOVE DATA PALING BELAKANG
data_akhir = data.pop()
print(f"Data akhir = \n{data}")

print(data_akhir)
