teman_teman = {
    "cup" : "ucup surucup",
    "tong" : "otong surotong",
    "dung" : "dudung surudung",
    "sep" : "sep si kasyep",
    "cuy" : "cuy surucuy"
}

friends = teman_teman.copy()

print(f"teman-teman = {teman_teman}\n")
print(f"friends = {friends}\n")

teman_teman["cup"] = "ucup si kweren"
print(f"teman-teman = {teman_teman}\n")
print(f"friens = {friends}\n")

# POP DICTIONARY (BERDASARKAN KEY)
dataAsep = friends.pop("sep")
print(f"data asep = {dataAsep}\n")
print(f"friends = {friends}\n")

# POPITEM DICTIONARY (MENGHAPUS DATA TERAKHIR)
dataTerakhir = friends.popitem()
print(f"data terakhir = {dataTerakhir}\n")
print(f"friends = {friends}]\n")

