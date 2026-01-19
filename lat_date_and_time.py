# DATE AND TIME (LATIHAN)

# PROGRAM
# 1. MENDETEKSI HARI LAHIR USER BERDASARKANG TANGGAL LAHIR YANG DIINPUT
# 2. UMUR

import datetime as dt

# PRINT TITLE
title = "PROGRAM DETEKSI HARI LAHIR"
print(title.center(60, "="))

# USER INPUT
date = input("Masukan tanggal lahir kamu (DD/MM/YYY) : ")

# SPLIT DATE
split_date = date.split("/")

# ASSIGNMENT TO BIRTH DATE
birth_date = dt.date(int(split_date[2]),int(split_date[1]),int(split_date[0]))

# PRINT HARI LAHIR DAN UMUR
print(f"Hari lahir mu pada tanggal {birth_date} adalah hari {birth_date:%A}")
print(f"Umurmu adalah {(dt.date.today() - birth_date).days // 365} tahun {((dt.date.today() - birth_date).days % 365) // 30} bulan")


