'''
Inputlah 5 data mahasiswa dengan data-data sebagai berikut
(GUNAKAN KONSEP I/0):
m1 : nim =>111, nama=>Budi, nilai=>77
m2 : nim =>112, nama=>Siti, nilai=>96
m3 : nim =>113, nama=>I Gede, nilai=>55
m4 : nim =>114, nama=>Joko, nilai=>25
m5 : nim =>115, nama=>Ahmad, nilai=>85

Cetaklah data nilai mahasiswa dengan data 
(Gunakan Format Print %s, %i, %.2f dsb):
- NIM
- Nama
- Nilai
- Keterangan = Lulus Jika nilai minimal 60, 
nilai di bawah 60 dinyatakan Gagal

- Grade = GUNAKAN IF MULTI KONDISI

Nilai 85 s/d 100, Grade => A
Nilai 75 s/d < 85, Grade => B
Nilai 60 s/d < 75, Grade => C
Nilai 30 s/d < 60, Grade => D
Nilai 0 s/d < 30, Grade => E

- Predikat = GUNAKAN IF MULTI KONDISI
Nilai 85 s/d 100, Grade => Memuaskan
Nilai 75 s/d < 85, Grade => Bagus
Nilai 60 s/d < 75, Grade => Cukup 
Nilai 30 s/d < 60, Grade => Kurang
Nilai 0 s/d < 30, Grade => Buruk
'''

m1 = {
    "Nim": 111,
    "Nama": "Budi",
    "Nilai": 77
}
m2 = {
    "Nim": 112,
    "Nama": "Siti",
    "Nilai": 96
}
m3 = {
    "Nim": 113,
    "Nama": "I Gede",
    "Nilai": 55
}
m4 = {
    "Nim": 114,
    "Nama": "Joko",
    "Nilai": 25
}
m5 = {
    "Nim": 115,
    "Nama": "Ahmad",
    "Nilai": 85
}

# for mahasiswa in range(2):

print("---------Data Mahasiswa---------")
# Data Mahasiswa 1
print("==========================")
print("Data Mahasiswa 1")
nama = str(input("Siapa nama kamu :  "))
nim = int(input("masukan nim kamu : "))
nilai = int(input ("berapa nilai kamu :  "))

# Data Mahasiswa 2
print("==========================")
print("Data Mahasiswa 2")
nama2 = str(input("Siapa nama kamu :  "))
nim2 = int(input("masukan nim kamu : "))
nilai2 = int(input ("berapa nilai kamu :  "))

# Data Mahasiswa 3
print("==========================")
print("Data Mahasiswa 3")
nama3 = str(input("Siapa nama kamu :  "))
nim3 = int(input("masukan nim kamu : "))
nilai3 = int(input ("berapa nilai kamu :  "))

# Data Mahasiswa 4
print("==========================")
print("Data Mahasiswa 4")
nama4 = str(input("Siapa nama kamu :  "))
nim4 = int(input("masukan nim kamu : "))
nilai4 = int(input ("berapa nilai kamu :  "))

# Data Mahasiswa 5
print("==========================")
print("Data Mahasiswa 5")
nama5 = str(input("Siapa nama kamu :  "))
nim5 = int(input("masukan nim kamu : "))
nilai5 = int(input ("berapa nilai kamu :  "))


# Data Mahasiswa
print("==========================")
print("Data Mahasiswa")
print("==========================")

print("Nama\t\t : %s"
       "\nNIM\t\t : %i"
       "\nNilai\t\t : %i"
       %(nama,nim,nilai,)
       )
print("==========================")
print("Nama\t\t : %s"
       "\nNIM\t\t : %i"
       "\nNilai\t\t : %i"
       %(nama2,nim2,nilai2,)
       )
print("==========================")
print("Nama\t\t : %s"
       "\nNIM\t\t : %i"
       "\nNilai\t\t : %i"
       %(nama3,nim3,nilai3,)
       )
print("==========================")
print("Nama\t\t : %s"
       "\nNIM\t\t : %i"
       "\nNilai\t\t : %i"
       %(nama4,nim4,nilai4,)
       )
print("==========================")
print("Nama\t\t : %s"
       "\nNIM\t\t : %i"
       "\nNilai\t\t : %i"
       %(nama5,nim5,nilai5,)
       )
