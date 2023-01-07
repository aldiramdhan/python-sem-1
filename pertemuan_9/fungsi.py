'''
Function

adalah sebuah kumpulan kode program yang terorganisir yang dibentuk untuk menjalankan sebuah tugas/perintah tertentu.

Return

adalah kata kunci untuk mengembalikan sebuah nilai dari fungsi yang telah dipanggil

Anonymous function atau lambda 
adalah sebuah fungsi yang tidak perlu mendefinisikan nama.

'''
# TODO:Buaat nama fungsi
def adab_belajar():
    # *badan fungsi(isi fungsi)
    print("1.Diam")
    print("2.Doa")
    print("3.Fokus")
    print("4. Tawakal")

# TODO:Memanggil Fungsi
adab_belajar()

print("="*20) #!batas

# *fungsi dengan argument
def mahasiswa(nama,nim):
    print(f"Nama: {nama}\nNim: {nim}")

        # !parameter function
mahasiswa("rey", "01110")

print("="*20) #!batas

# TODO:function dengan return
def tambah(angka_1,angka_2):
    hasil = angka_1+angka_2
    # !return hasil
    print(hasil)

            # !parameter function
print(tambah(5,1))

def kuadrat(angka):
    print(angka**2)

kuadrat(2)

print("="*20) #!batas

# *Fungsi dapat dipanggil berkali kali untuk mempersingkat kode program yang dipanggil

def sikat_gigi():
    print("masuk kamar mandi")
    print("sikat gigi")

def berangkat_kuliah():
    print("nyalain motor")
    print("pamit")
    print("berangkat")

def keseharian():
    sikat_gigi()
    berangkat_kuliah()

keseharian()

print("="*20) #!batas

# *function lambda
# *lambda = def
# *lambda -> paarameter -> return ....
a = lambda angka_1, angka_2 : angka_1 + angka_2
print(a(5,1))

print("="*20) #!batas

# TODO:membuat fungsi operasi matematika:

def operasi_mtk (angka1, angka2):
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    kali = angka1 * angka2
    bagi = angka1 / angka2
    pangkat = angka1 ** angka2
    return tambah, kurang, kali, bagi, pangkat

angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))
a, b, c, d, e = operasi_mtk(angka1, angka2);

print(f"Hasil dari {angka1} + {angka2}: {a}")
print(f"Hasil dari {angka1} - {angka2}: {b}")
print(f"Hasil dari {angka1} * {angka2}: {c}")
print(f"Hasil dari {angka1} / {angka2}: {d}")
print(f"Hasil dari {angka1} ** {angka2}: {e}")