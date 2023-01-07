# -*- coding: utf-8 -*-
"""soal2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KHpJ5xiRchbgNwloRr_b8FS_T_5YfbPK
"""

m1 = {'nim':111,'nama':'Budi','nilai':77}
m2 = {'nim':112,'nama':'Siti','nilai':96}
m3 = {'nim':113,'nama':'I Gede','nilai':55}
m4 = {'nim':114,'nama':'Joko','nilai':25}
m5 = {'nim':115,'nama':'Ahmad','nilai':85}

ar_mahasiswa = [m1,m2,m3,m4,m5]

for mahasiswa in ar_mahasiswa:
  for data in mahasiswa.items():
    nilai = mahasiswa['nilai']
    nim = mahasiswa['nim']
    nama = mahasiswa['nama']
    ket = ('Lulus','Gagal')[nilai <= 60]

    if nilai >= 85 and nilai <= 100:
      grade = 'A'
      predikat = "Memuaskan"
    elif nilai >= 75 and nilai < 85:
      grade = 'B'
      predikat = "Bagus"
    elif nilai >= 60 and nilai < 75:
      grade = 'C'
      predikat = "Cukup"
    elif nilai >= 30 and nilai < 60:
      grade = 'D'
      predikat = "Kurang"
    elif nilai >= 0 and nilai < 30:
      grade = 'E'
      predikat = "Buruk"
    else:
      grade = ''
      predikat = '' 
    format_string = f"Nim : {nim:d} \nNama : {nama} \nNilai : {nilai:.1f}"
  print(format_string)
  print('Keterangan : %s \nGrade : %s \nPredikat : %s \n========= '%(ket,grade,predikat))