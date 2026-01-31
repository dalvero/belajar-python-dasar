# OPERATOR DICTIONARY

data_dict = {
    "cup" : "ucup surucup",
    "tong" : "otong surotong",
    "dung" : "dudung surudung",
}

# PANJANG DICTIONARY
LENDICT = len(data_dict)
print(f"Panjang dictionary\t: {LENDICT}")

# MENGECEK KEY EXIST ATAU TIDAK
KEY = "cup"
CHECKEY = KEY in data_dict
print(f"Apakah {KEY} ada di data_dict\t: {CHECKEY}")

# MENGAKSES VALUE (READ) DENGAN GET
print(data_dict["cup"])
print(data_dict.get("cup"))
# CEK VALUE DENGAN TAMBAHAN KONDISI TIDAK DITEMUKAN
print(data_dict.get("kis", "Key tidak ditemukan")) 

# MENGUPDATE DATA
data_dict["cup"] = "ucup si ganteng"
print(data_dict)
data_dict["sep"] = "asep si kasyep"
print(data_dict)

data_dict.update({"cup": "ucup surucup"})
print(data_dict)
data_dict.update({"faqih": "faqihza si kweren"}) # KALAU KEY TIDAK DITEMUKAN OTOMATIS DITAMBAHKAN
print(data_dict)

# MENDELETE DATA PADA DICTIONARY
del data_dict["faqih"]
print(data_dict)
