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


nama = []
nim  = []
nilai = []

for i in range(1):
    nama.append (str(input("Nama:")))
    nim.append (int(input("NIM:")))
    nilai.append (int(input("Nilai:")))

    if (nilai >= [85] <= [100]):
        grade = 'A'
        predikat = 'Memuaskan'
    elif (nilai >= [75] <= [85]):
        grade = 'B'
        predikat = 'Bagus'
    elif (nilai >= [60] <= [75]):
        grade = 'C'
        predikat = 'Cukup'
    elif (nilai >= [30] <= [60]):
        grade = 'D'
        predikat = 'Kurang'
    elif (nilai >= [0] <= [30]):
        grade = 'E'
        predikat = 'Buruk'

    else:
        grade = ''
        predikat = ''

ket = [("Gagal", "Lulus")[nilai >= [60]]]

print("---------Data Mahasiswa----------")
print("Nama\t\t : {0}"
        "\nNIM\t\t : {1}"
        "\nNilai\t\t : {2}"
        "\nKeterangan\t : %s"
        "\nGrade\t\t : %s"
        "\nPredikat\t : %s"
        .format(nama,nim,nilai) 
        %(ket,grade,predikat))
print("=================================")

    