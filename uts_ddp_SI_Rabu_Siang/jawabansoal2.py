listPegawai = []

for i in range(2):
    nama = str(input("Masukkan Nama:"))
    jabatan = str(input("Jabatan:"))
    agama = str(input("Agama:"))
    status = str(input("Status:"))

    listPegawai.append({"nama": nama,
                        "jabatan": jabatan,
                        "agama": agama,
                        "status": status})

for x in range(len(listPegawai)):

    if (listPegawai[x]["jabatan"] == "manager" or "Manager"):
        gajiPokok = 15000000
        tunjanganJabatan = gajiPokok * 0.3
    elif (listPegawai[x]["jabatan"] == "asmen" or "Asmen" and "Asisten Manager"):
        gajiPokok = 10000000
        tunjanganJabatan = gajiPokok * 0.3
    elif (listPegawai[x]["jabatan"] == "supervisor" or "Supervisor"):
        gajiPokok = 7000000
        tunjanganJabatan = gajiPokok * 0.3
    elif (listPegawai[x]["jabatan"] == "staff" or "Staff" and "staf"):
        gajiPokok = 4000000
        tunjanganJabatan = gajiPokok * 0.3

        tunjangan_keluarga = x["status"]
        keterangan = (0,gajiPokok * 0.10)[tunjangan_keluarga == "menikah"]

    print("Data Pegawai ke-", x+1,
        "\nNama\t\t\t: %s"
        "\nJabatan\t\t\t: %s"
        "\nAgama\t\t\t: %s"
        "\nStatus\t\t\t: %s"
        "\nGaji Pokok\t\t: %i"
        "\nTunjangan Jabatan\t: %.2f"
        "\nTunjangan Keluarga\t: %.2f"
        # "\nGaji Kotor\t\t: %.2f"
        # "\nZakat Profesi\t\t: %.2f"
        # "\nGaji Bersih\t\t: %.2f"
        %(listPegawai[x]["nama"], listPegawai[x]["jabatan"], listPegawai[x]["agama"], listPegawai[x]["status"], gajiPokok, tunjanganJabatan, keterangan)
        # keterangan, gajiKotor, zakatProfesi, gajiBersih)
        )