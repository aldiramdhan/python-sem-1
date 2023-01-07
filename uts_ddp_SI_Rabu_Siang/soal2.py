# Membuat List Kosong Untuk Menampung 5 Data Inputan
listPegawai = []

# Membuat Loop 5 kali untuk memasukan 5 Data Inputan
for i in range(1):
    nama = str(input("Masukkan Nama:"))
    jabatan = str(input("Jabatan:"))
    agama = str(input("Agama:"))
    status = str(input("Status:"))

    # Membuat Dictionary untuk Menambahkan ke dalam list (Append dictionary)
    listPegawai.append({"nama": nama,
                    "jabatan": jabatan,
                    "agama": agama,
                    "status": status
                    })

# Membuat for loop sesuai dengan data yang telah dimasukkan
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
    
    
# Membuat Tuple & List untuk Tunjangan Keluarga, Gaji Kotor, Zakat Profesi, Gaji Bersih.
        # tunjanganKeluarga = ("0", gajiPokok * 0.1)[listPegawai[x]["status"] == "Sudah Menikah" or "sudah menikah" ]
        # gajiKotor = gajiPokok + tunjanganJabatan + tunjanganKeluarga
        # zakatProfesi = (0, gajiPokok * 0.025)[listPegawai[x]["agama"] == "Muslim" or "muslim" and listPegawai[x]["jabatan"] >= 7000000]
        # gajiBersih = gajiKotor - zakatProfesi
        tunjanganJabatan = 0.3 * gajiPokok
        tunjangan_keluarga = listPegawai["status"]
        keterangan = (0, gajiPokok * 0.10)[tunjangan_keluarga == "menikah"]
        gajiKotor = gajiPokok + tunjanganJabatan + keterangan
        zakprof = listPegawai["agama"]
        zakatProfesi = (0, 0.025 * gajiKotor)[gajiKotor >= 7000000 and zakprof == "islam"]
        gajiBersih = gajiKotor - zakatProfesi

# print 5 Data Inputan Menggunakan format %s, %i, %.2f, dsb
    print("Data Pegawai ke-", x+1,
        "\nNama\t\t\t: %s"
        "\nJabatan\t\t\t: %s"
        "\nAgama\t\t\t: %s"
        "\nStatus\t\t\t: %s"
        "\nGaji Pokok\t\t: %i"
        "\nTunjangan Jabatan\t: %.2f"
        "\nTunjangan Keluarga\t: %.2f"
        "\nGaji Kotor\t\t: %.2f"
        "\nZakat Profesi\t\t: %.2f"
        "\nGaji Bersih\t\t: %.2f"
        %(listPegawai[x]["nama"], listPegawai[x]["jabatan"], listPegawai[x]["agama"], listPegawai[x]["status"], gajiPokok, tunjanganJabatan, 
        keterangan, gajiKotor, zakatProfesi, gajiBersih)
        )
