import datetime as dt
import utility as util

mahasiswa1 = {
    'nama' : 'Ucup Surucup',
    'nim' : '123456123',
    'sks_lulus' : 130,
    'beasiswa' : False,
    'lahir' : dt.datetime(2001, 4, 10)
}

mahasiswa2 = {
    'nama' : 'Otong Surotong',
    'nim' : '123654312',
    'sks_lulus' : 140,
    'beasiswa' : True,
    'lahir' : dt.datetime(2002, 10, 10)
} 

mahasiswa3 = {
    'nama' : 'Asep Si Kasyep',
    'nim' : '456123456',
    'sks_lulus' : 100,
    'beasiswa' : False,
    'lahir' : dt.datetime(2000, 2, 29)
} 

data_mahasiswa = {
    'MAH001' : mahasiswa1,
    'MAH002' : mahasiswa2,
    'MAH003' : mahasiswa3
}

util.clear_screen()
print("-" * 60)
print(f"{'KEY':<6} | {'Nama':<20} | {'SKS':<5} | {'Beasiswa':<9} | {'Lahir':<10}")
print("-" * 60)

for mahasiswa in data_mahasiswa :
    KEY = mahasiswa
    NAMA = data_mahasiswa[KEY]['nama']
    SKS = data_mahasiswa[KEY]['sks_lulus']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")
    print(f"{KEY:<6} | {NAMA:<20} | {SKS:<5} | {BEASISWA:^9} | {LAHIR:<10}")

print("-" * 60)


