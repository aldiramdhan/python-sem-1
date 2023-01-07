# Pertemuan ke 7 
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


# print("Hello",nama,"nim kamu adalah",nim,"nilai kamu adalah",nilai)

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

# Data Mahasiswa Keterangan, Grade, Predikat

dataMahasiswa = [m1, m2, m3, m4, m5]

namaInput = []
nimInput = []
nilaiInput = []

print("------Input Data Mahasiswa------")

for i in range (2):
    namaInput.append(str(input("Nama:")))
    nimInput.append(int(input("NIM:")))
    nilaiInput.append(int(input("Nilai:")))
    print("=====================")


print("---------Data Mahasiswa---------")

for mahasiswa in dataMahasiswa:
    nama = {m1,m2,m3,m4,m5["Nama"]}
    nim = {m1,m2,m3,m4,m5["Nim"]}
    nilai = {m1,m2,m3,m4,m5['Nilai']}

    if (mahasiswa["Nilai"] >= 60):
        ket = 'Lulus'
        
    elif (mahasiswa["Nilai"] <= 60):
        ket = 'Gagal'

    if (mahasiswa["Nilai"] >= 85):
        predikat = 'Memuaskan'
        grade = 'A'
    elif (mahasiswa["Nilai"] >= 85 <=100):
        predikat = 'Bagus'
        grade = 'B'
    elif (mahasiswa["Nilai"] >= 60 <=75):
        predikat = 'Cukup'
        grade = 'C'
    elif (mahasiswa["Nilai"] >=30 <=60):
        predikat = 'Kurang'
        grade = 'A'
    elif (mahasiswa["Nilai"] >=0 <=30):
        predikat = 'Buruk'
        grade = 'E'
    
    print("Nama Input\t : %s"
        "\nNIM Input\t : %i"
        "\nNilai Input\t : %i"
        "\nNama\t\t : %s"
        "\nNIM\t\t : %i"
        "\nNilai\t\t : %i"
        "\nKeterangan\t : %s"
        "\nGrade\t\t : %s"
        "\nPredikat\t : %s"
        %(namaInput,nimInput[0],nilaiInput[0],nama,nim,nilai,ket,grade,predikat) 
        )

    print("================================")