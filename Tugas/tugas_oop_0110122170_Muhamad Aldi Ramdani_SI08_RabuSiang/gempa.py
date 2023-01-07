'''
Running code di info_gempa.py untuk menampilkan output.
'''

class Gempa:
  
  def __init__(self, lokasi, skala):
    self.lokasi = lokasi
    self.skala = skala
  
  def dampak(self):
    if self.skala <= 2.0:
      print(f"Gempa berskala {self.skala} SR di {self.lokasi} menimbulkan dampak gempa yang tidak berasa.")
    elif self.skala >= 2.0 and self.skala < 4.0:
      print(f"Gempa berskala {self.skala} SR di {self.lokasi} menimbulkan dampak bangunan retak retak.")
    elif self.skala >= 4.0 and self.skala < 6.0:
      print(f"Gempa berskala {self.skala} SR di {self.lokasi} menimbulkan dampak bangunan roboh.")
    else:
      print(f"Gempa berskala {self.skala} SR di {self.lokasi} menimbulkan dampak bangunan roboh dan berpotensi tsunami.")