# LATIHAN KONVERSI SATUAN TEMPERATURE
# CELCIUS KE :
#   - REAMUR        = 4 / 5 * C
#   - FAHRENHEIT    = 9 / 5 * C + 32
#   - KELVIN        = C + 273
# REAMUR KE :
#   - CELCIUS       = 5 / 4 * R
#   - FAHRENHEIT    = 4 / 9 * (F - 32)
#   - KELVIN        = 5 / 4 * K + 273
# FAHRENHEIT KE :
#   - CELCIUS       = 5 / 9 * (F - 32)
#   - REAMUR        = 4 / 9 * (F - 32)
# KELVIN KE :
#   - CELCIUS       = K - 273
#   - REAMUR        = 4 / 5 (K - 273)

# PROGRAM KONVERSI CELCIUS KE SATUAN LAIN
# PRINT TITLE
print("===KONVERSI CELCIUS KE SATUAN YANG LAIN===\n")

# INPUT USER DAN CASTING KE FLOAT/INT
celcius = float(input("Masukan suhu dalam Celcius \t: "))
print("Suhu yang akan di konversi adalah ", celcius, " Celcius" )

# CALCULATE
reamur = 4 / 5 * celcius
fahrenheit = 9 / 5 * celcius + 32
kelvin = celcius + 273

# PILIHAN KONVERSI KE
print("\nHasil konversi anda adalah : ")
print("1. Reamur = ", reamur, "R \n2. Fahrenheit = ", fahrenheit, "F \n3. Kelvin = ", kelvin, " K")



