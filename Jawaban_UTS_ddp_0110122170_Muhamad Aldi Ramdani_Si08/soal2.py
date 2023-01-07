ar_dataPegawai = []

print("------------Masukkan Data Pegawai------------")

for i in range(5):
    nama = str(input("Nama:"))
    jabatan = str(input("Jabatan:"))
    agama = str(input("Agama:"))
    status = str(input("status:"))

    ar_dataPegawai.append({"nama": nama, "jabatan": jabatan, "agama": agama, "status": status})
    print("==================================")

# Menampilkan data Pegawai
for pegawai in ar_dataPegawai:
    
    if (pegawai["jabatan"] == "Manager" or "manager"):
        gajiPokok = 15000000
    elif (pegawai["jabatan"] == "Asisten Manager" or "Asmen"):
        gajiPokok = 10000000
    elif (pegawai["jabatan"] == "Supervisor" or "supervisor"):
        gajiPokok = 7000000
    elif (pegawai["jabatan"] == "Staff" or "staff"):
        gajiPokok = 4000000

    tunjanganJabatan = 0.3 * gajiPokok
    tunjanganKeluarga = (0, 0.10 * gajiPokok)[pegawai["status"] == "Menikah"]
    gajiKotor = gajiPokok +tunjanganJabatan + tunjanganKeluarga
    zakatProfesi = (0, 0.025 * gajiPokok)[pegawai["agama"] == "Muslim" and gajiKotor >= 7000000]
    gajiBersih = gajiKotor - zakatProfesi

    print("Data Pegawai ke-1", ar_dataPegawai.index(pegawai)+1,
            "\n================================="
            "\nNama\t\t\t: %s"
            "\nJabatan\t\t\t: %s"
            "\nAgama\t\t\t: %s"
            "\nStatus\t\t\t: %s"
            "\nGaji\t\t\t: %i"
            "\nTunjangan Jabatan\t: %i"
            "\nTunjangan Keluarga\t: %i"
            "\nGaji Kotor\t\t: %i"
            "\nZakat Profesi\t\t: %i"
            "\nGaji Bersih\t\t: %i"
            %(pegawai["nama"], pegawai["jabatan"], pegawai["agama"], pegawai["status"], gajiPokok, tunjanganJabatan, tunjanganKeluarga, gajiKotor, zakatProfesi, gajiBersih)
            )

