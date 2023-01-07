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
dataList = [] # Untuk menampung data 5 data inputan mahasiswa

print("--------Masukkan Data Mahasiswa--------")

for i in range(5): #Loop 5 data Input
    nama = str(input("Masukkan Nama:"))
    nim = int(input("Masukkan NIM:"))
    nilai = float(input("Masukkan Nilai:"))
    print("--------------------------")

    # Membuat dictionary dan menambahkan (Append) ke dalam list
    dataList.append({"nama": nama,
                    "nim": nim, 
                    "nilai": nilai })

#Loop list dari dataList dengan range sesuai dengan data yang dimasukan ke dalam list.
for jumlah in range(len(dataList)): 

     #kondisi Gagal/Lulus Menggunakan Tuple & List
    keterangan = ('Gagal', 'Lulus')[dataList[jumlah]["nilai"] >= 60]

# Kondisi if multi kondisi untuk Grade & Predikat
    if (dataList[jumlah]["nilai"] >= 85):
        grade = 'A'
        predikat = 'Memuaskan'
    elif (dataList[jumlah]["nilai"]>= 75 <=85):
        grade = 'B'
        predikat = 'Bagus'
    elif (dataList[jumlah]["nilai"]>= 60 <=75):
        grade = 'C'
        predikat = 'Cukup'
    elif (dataList[jumlah]["nilai"]>= 30 <=60):
        grade = 'D'
        predikat = 'Kurang'
    elif (dataList[jumlah]["nilai"]>= 0 <=30):
        grade = 'E'
        predikat = 'Buruk'

# format print menggunakan %s, %i, %.2f,dsb
    print("Data Mahasiswa ke-", jumlah+1,
        "\n============================="
        "\nNama\t\t: %s"
        "\nNIM\t\t: %i"
        "\nNilai\t\t: %.2f"
        "\nKeterangan\t: %s"
        "\nGrade\t\t: %s"
        "\nPredikat\t: %s"
        "\n============================="
        %(dataList[jumlah]["nama"], dataList[jumlah]["nim"], dataList[jumlah]["nilai"], keterangan, grade, predikat)
        )