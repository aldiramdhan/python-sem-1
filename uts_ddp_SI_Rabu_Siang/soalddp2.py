p1 = {"nama":"Budi","jabatan":"manager","agama":"islam","status":"menikah"}
p2 = {"nama":"Siti","jabatan":"asisten manager","agama":"islam","status":"menikah"}
p3 = {"nama":"I Gede","jabatan":"supervisor","agama":"hindu","status":"menikah"}
p4 = {"nama":"Joko","jabatan":"staff","agama":"islam","status":"belum menikah"}
p5 = {"nama":"Alex","jabatan":"staff","agama":"kristen protestan","status":"belum menikah"}

ar_pegawai = [p1, p2, p3, p4, p5]
for pegawai in ar_pegawai:
    for key, data in pegawai.items():

        gaji = pegawai["jabatan"]
        if gaji == "manager":
            gajipokok = 15000000
        elif gaji == "asisten manager":
            gajipokok = 10000000
        elif gaji == "supervisor":
            gajipokok = 7000000
        else:
            gajipokok = 4000000

        tunjangan_jabatan = 0.3 * gajipokok
        bpjs = 0.10 * gajipokok
        tunjangan_keluarga = pegawai["status"]
        keterangan = (0,gajipokok * 0.10)[tunjangan_keluarga == "menikah"]
        gaji_kotor = gajipokok + tunjangan_jabatan + bpjs + keterangan
        zakprof = pegawai["agama"]
        zakat_profesi = (0, 0.025 * gaji_kotor)[gaji_kotor >=7000000 and zakprof == "islam"]
        gaji_bersih = gaji_kotor - zakat_profesi
        print(key,":",data)
    print(
        "gaji pokok :",gajipokok,
        "\nTunjangan Jabatan :",tunjangan_jabatan,
        "\nBPJS :",bpjs,
        "\nTunjangan Keluarga :",keterangan,
        "\nGaji Kotor :",gaji_kotor,
        "\nZakat Profesi :",zakat_profesi,
        "\nGaji Bersih :",gaji_bersih,
        "\n======================================")
        