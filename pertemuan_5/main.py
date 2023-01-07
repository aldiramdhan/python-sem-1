#PERTEMUAN 5
#inputan user
nama = input("Masukan nama anda: ")
password = input("Masukan Password:")
# nama2 = input("Masukan nama yang benar:")

# IF Inline
#kondisi:aksi
#if nama == "rey":print("kamu ganteng")

# IF Indentation
#kondisi:
#    aksi
# if nama == "nopal":
#     print("kamu nopal")
#     print("kamu juga ganteng")

# Else Statement
# if nama == "nopal":
#     print("kamu nopal")
#     print("kamu juga ganteng")
# else:
#     print("kamu bukan nopal")
#     print("nama2")

# Else IF Statement
# kondisi:
#   aksi
# kondisi2:
#   aksi
# kondisi3:
#   aksi
# if nama == "nopal":
#     print("kamu nopal")
#     print("kamu juga ganteng")
# elif nama == "caca":
#     print("kamu caca")
#     print("kamu cantik")
# else:
#     print("kamu gk terkenal, skip")

if nama == "nopal" and password == "admin12345678":
    print("kamu berhasil login")
else:
    print("nama atau password salah")