
class Kopek:

  def konus(self):
    print("Hav!")

  def otur(self):
    print("Köpek oturdu.")

doggo = Kopek()
doggo.konus()
doggo.otur()



class Kopek:

  def __init__(self, isim, yas):
    self.isim = isim
    self.yas = yas

  def konus(self):
    print("Hav!")

  def otur(self):
    print("Köpek oturdu.")

  def yasHesapla(self):
    print("Kopeğin insan yıllarındaki yaşı: " + str(self.yas * 7))


dog = Kopek("köpek",21)
dog2 = Kopek("kangal",11)

print(dog.isim)
print(dog.yas)

class Kopek:

  def __init__(self, isim, yas):
    self.isim = isim
    self.yas = yas

  def konus(self):
    print("Hav!")

  def kendini_tanit(self):
    print(f'Benim ismim {self.isim} ve {self.yas} yasindayim')

doggy = Kopek("swastika",2)
doggy.kendini_tanit()

class Ogrenci:


    def __init__(self, isim, yas, puan):

        #attribute
        self.isim = isim
        self.yas = yas
        self.puan = puan # 1 - 100

import math
class Ders:

    # method
    def __init__(self, ders):
        self.ders = ders
        self.ogrenci_arr = []

    def ekle(self, ogrenci):
        self.ogrenci_arr.append(ogrenci)

    def ortalama(self):
        val = 0
        for ogrenci in self.ogrenci_arr:
            val += ogrenci.puan
        return val / len(self.ogrenci_arr)

    def std(self):
        m = self.ortalama()
        k = 0
        for ogrenci in self.ogrenci_arr:
            k +=((ogrenci.puan - m)**2)
        k /= len(self.ogrenci_arr)
        return math.sqrt(k)


st1 = Ogrenci("Ahmet",20,85)
st2 = Ogrenci("Dogukan",20,5)
st3 = Ogrenci("Metin Evrim Ulu",19,100)
st4 = Ogrenci("Batuhan",20,70)

calculus = Ders("Calculus")
calculus.ekle(st1)
calculus.ekle(st2)
calculus.ekle(st3)
calculus.ekle(st4)

print(calculus.ortalama())
print(calculus.std())

class Arac():

  def __init__(self, fiyat, benzin):
    self.fiyat = fiyat
    self.benzin = benzin 
  
  def benzinDoldur(self):
    self.benzin = 100

  def depoyuBosalt(self):
    self.benzin = 0



class Tofas(Arac):

  def driftAt(self):
    print("Mutheşem bir drift atıldı")

class Kamyon(Arac):
  def __init__(self, fiyat, benzin, agirlik):
    super().__init__(self, fiyat, benzin)
    self.agirlik = agirlik

  def yükleriIndir(self):
    print("agirliklar indirildi.")

  def korna(self):
    print("HOOOONK!")

class Arac():

  def __init__(self, fiyat, benzin):
    self.fiyat = fiyat
    self.benzin = benzin 
  
  def benzinDoldur(self):
    self.benzin = 100

  def depoyuBosalt(self):
    self.benzin = 0

  def korna(self):
    print("beep")



class Tofas(Arac):

  def driftAt(self):
    print("Mutheşem bir drift atıldı")

class Kamyon(Arac):
  def __init__(self, fiyat, benzin, agirlik):
    super().__init__(fiyat, benzin)
    self.agirlik = agirlik # ton

  def yükleriIndir(self):
    print("agirliklar indirildi.")

  def korna(self):
    print("HOOOONK!")


tofas = Tofas(6000,30)
tofas.driftAt()
tofas.korna()

kamyon = Kamyon(50000, 100, 10)
kamyon.korna()

