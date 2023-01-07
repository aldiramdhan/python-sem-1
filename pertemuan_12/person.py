'''
Inheritance (pewarisan) adalah suatu proses untuk memperoleh suatu class yang baru dari suatu class dasar (baseclass/superclass) atau class yang telah ada. 
'''

class Person:
    nama = ""
    gender = ""
    umur = 0
    
    def __init__(self, nama, gender, umur) -> None:
        self.nama = nama
        self.gender = gender
        self.umur = umur

    def cetak(self):
        print(
        "\n-------------------------------"
        "\nNama \t\t:", self.nama,
        "\nJenis Kelamin\t:", self.gender,
        "\nUmur\t\t:", self.umur, "tahun")