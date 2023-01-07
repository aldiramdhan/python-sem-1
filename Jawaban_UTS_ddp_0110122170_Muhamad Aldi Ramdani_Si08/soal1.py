s1 = {
    "nama" : "Budi",
    "nilai" : 75,
    "matpel" : "Matematika"
    }
s2 = {
    "nama" : "Dewi",
    "nilai" : 55,
    "matpel" : "IPA"
    }
s3 = {
    "nama" : "Ani",
    "nilai" : 95,
    "matpel" : "IPS"
    }
s4 = {
    "nama" : "Bedu",
    "nilai" : 30,
    "matpel" : "Agama"
    }
s5 = {
    "nama" : "Ahmad",
    "nilai" : 83,
    "matpel" : "Bahasa Inggris"
    }

ar_siswa = [s1,s2,s3,s4,s5]

for siswa in ar_siswa:
    for data in siswa.items():
        nama = siswa["nama"]
        nilai = siswa["nilai"]
        matpel = siswa["matpel"]

        keterangan = ("Lulus","Gagal")[nilai <= 60]

        if (siswa["nilai"] >=85):
            grade = "A"
            predikat = "Memuaskan"
        elif (siswa["nilai"] >=75 <=85):
            grade = "B"
            predikat = "Bagus"
        elif (siswa["nilai"] >=60 <=75):
            grade = "c"
            predikat = "Cukup"
        elif (siswa["nilai"] >=30 <=60):
            grade = "D"
            predikat = "Kurang"
        elif (siswa["nilai"] >=0 <=30):
            grade = "E"
            predikat = "Buruk"
        else:
            grade = ""
            predikat = ""

        data_siswa = f"Nama : {nama} \nNilai : {nilai:.2f} \nMatpel : {matpel}"
    print(data_siswa)
    print("Keterangan : %s \nGrade : %s \nPredikat : %s \n========================= "%(keterangan,grade,predikat))