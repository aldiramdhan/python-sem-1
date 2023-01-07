'''
p1 : nama=>Budi, produk=> TV, jumlah=>3

p2 : nama=>Ani, produk=> AC, jumlah=>4

p3 : nama=>Siti, produk=> Kulkas, jumlah=>2

p4 : nama=>Dewi, produk=> AC, jumlah=>5

p5 : nama=>Andi, produk=> Kulkas, jumlah=>7

p6 : nama=>Dedi, produk=> AC, jumlah=>1

p7 : nama=>Sri, produk=> TV, jumlah=>4

Semua pelanggan masukkan ke sebuah list dengan nama ar_pelanggan (Bobot Penilaian 5 Point)

Cetaklah Data Pembelian Pelanggan Menggunakan Nested Loop Dengan Data:

- Nama Pelanggan(Bobot Penilaian 5 Point)

- Produk Beli (Bobot Penilaian  5 Point)

- Jumlah Beli (Bobot Penilaian  10 Point)

- Harga Satuan: (Bobot Penilaian 20 Point)

  Gunakan kondisional if:

  (TV=>5 jt, AC=>6 jt, Kulkas=>7 jt)

- Harga Kotor => Jumlah Beli x Harga Satuan (Bobot Penilaian  10 Point)

- Diskon: (Bobot Penilaian 10 Point)

  Gunakan Tuple & List 

  Jika Beli Produk Kulkas minimal 3 pcs dapat diskon 20% dari harga kotor,

  Selain itu diskon hanya 5% dari harga kotor

- PPN => 11% x (Harga Kotor - Diskon) (Bobot Penilaian 10 Point)

- Harga Bayar => (Harga Kotor + PPN) - Diskon (Bobot Penilaian 5 Point)
'''

p1 = {
    "nama": "Budi",
    "produk": "TV",
    "jumlah": 3
}
p2 = {
    "nama": "Ani",
    "produk": "AC",
    "jumlah": 4
}
p3 = {
    "nama": "Siti",
    "produk": "Kulkas",
    "jumlah": 2
}
p4 = {
    "nama": "Dewi",
    "produk": "AC",
    "jumlah": 5
}
p5 = {
    "nama": "Andi",
    "produk": "Kulkas",
    "jumlah": 7
}
p6 = {
    "nama": "Dedi",
    "produk": "AC",
    "jumlah": 1
}
p7 = {
    "nama": "Sri",
    "produk": "TV",
    "jumlah": 4
}

ar_pelanggan = [p1, p2, p3, p4, p5, p6, p7]

for pelanggan in ar_pelanggan:
    print(f"nama: {pelanggan['nama']}")
    print(f"produk: {pelanggan['produk']}")
    print(f"jumlah: {pelanggan['jumlah']}")

    if (pelanggan["produk"] == "TV"):
        hargaSatuan = 5000000
    elif (pelanggan["produk"] == "AC"):
        hargaSatuan = 6000000
    elif (pelanggan["produk"] == "Kulkas"):
        hargaSatuan = 7000000 

    print("Harga Satuan : ", hargaSatuan)
    

    hargaKotor = pelanggan["jumlah"] * hargaSatuan
    print("Harga Kotor : ", hargaKotor)

    diskon = (hargaKotor * 0.05, hargaKotor * 0.2)[pelanggan["produk"] == "Kulkas" and pelanggan["jumlah"] >= 3]
    print("Diskon : ",diskon)

    ppn = 0.11 * (hargaKotor - diskon)
    print("PPN : ",ppn)

    harga_bayar = (hargaKotor + ppn) - diskon
    print("Harga Bayar : ",harga_bayar)

    print("==============================")