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

dataMahasiswa = [m1, m2, m3, m4, m5]
kodeMahasiswa = (str(input("Masukkan kode Mahasiswa:")))

if kodeMahasiswa == "m1":
    print(f"NIM : {m1['Nim']}")
    print(f"Nama : {m1['Nama']}")
    print(f"Nilai : {m1['Nilai']}")

elif kodeMahasiswa == "m2":
    print(f"NIM : {m2['Nim']}")
    print(f"Nama : {m2['Nama']}")
    print(f"Nilai : {m2['Nilai']}")

elif kodeMahasiswa == "m3":
    print(f"NIM : {m3['Nim']}")
    print(f"Nama : {m3['Nama']}")
    print(f"Nilai : {m3['Nilai']}")

elif kodeMahasiswa == "m4":
    print(f"NIM : {m4['Nim']}")
    print(f"Nama : {m4['Nama']}")
    print(f"Nilai : {m4['Nilai']}")

elif kodeMahasiswa == "m5":
    print(f"NIM : {m5['Nim']}")
    print(f"Nama : {m5['Nama']}")
    print(f"Nilai : {m5['Nilai']}")

else:
    print("kode yang anda masukkan salah")
