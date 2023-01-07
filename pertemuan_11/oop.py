'''
OOP atau Oriented Object Programming adalah paradigma pemrograman yang menekankan pada penggunaan objek dalam pembuatan program.

Dalam bahasa Python, OOP dapat diterapkan dengan menggunakan konsep class. Class merupakan blueprint atau rancangan untuk membuat objek.
'''

print("="*10 + "{OOP}" + "="*10)

class Kendaraan:#*template atau class yang membuat object
    def __init__(self, merk, tipe):#*merk dan tipe merupakan sebuah attribute atau karakteristik
        self.merk = merk
        self.tipe = tipe
    
    def jalankan(self):#*method atau behaviour dari object yang dideklarasikan dengan fungsi
        print(f"{self.merk} {self.tipe} sedang berjalan")

mobil = Kendaraan("Toyota", "Avanza")#!Mengisi value dari attribute object
mobil.jalankan()

print("="*20)

# TODO:Membuat Class
# !class nama_class

class Hero:
    # *attribute
    nama = "Kadita"
    hp = 1000

    # *Method
    def dive(self):
        print("Menyelam")


# TODO:Membuat object
hero1 = Hero()
print("Nama hero:", hero1.nama)
print("HP:", hero1.hp)
hero1.dive()
    
print("="*20)

class Calculator:
    brand = "Xiaomi"

    def tambah(self, a, b):
        return a + b

# TODO: Create Object
my_calcu = Calculator()
hasil = my_calcu.tambah(10,5)
print("Hasil dari 10 + 5 =", hasil)

print("="*20)

class Bank:
    account_balance = 1000000

    # *Method tampil saldo
    def get_balance(self):
        return self.account_balance

    # *Method narik Tabungan
    def withdraw(self, uang):
        return self.account_balance - uang

# TODO:Membuat object 
my_account = Bank()
saldo = my_account.get_balance()
print("Rp.", saldo)
saldoSekarang = my_account.withdraw(5000)
print("Rp.", saldoSekarang)


print("="*20)


class Hero:
   
    # *Constructor
    def __init__(self, name, atk, armor):
        self.name = name
        self.atk = atk
        self.armor = armor
        self.hp = 10000

# *Buat Object
hero1 = Hero("Kadita", 450, 1000 )
hero2 = Hero("Zilong", 999, 500 )
print(hero2.name)

print("="*20)

class Hero:
   
    # *Constructor
    def __init__(self, name, atk, armor):
        self.name = name
        self.atk = atk
        self.armor = armor
        self.hp = 10000
        self.items = []

    def buy_item(self, item):
        # Attribute Instance
        self.items.append(item)

# *Buat Object
hero1 = Hero("Kadita", 450, 1000 )
hero2 = Hero("Zilong", 999, 500 )

hero1.buy_item("Demon Shoes")
print(hero1.items)
hero2.buy_item("Blade Of Despair")
print(hero2.items)