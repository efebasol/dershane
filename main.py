# mongodb
from typing_extensions import Self
import pymongo
mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
mongoDB = mongoClient["test"]

sayi = 0
def secim():
    while sayi < 1:
        secim = input("secim: ")
        if secim == "1":
            sinif = input("Sınıf :")
            isim = input("İsim: ")
            soyisim = input("Soyad: ")
            numara = input("Numara :")
            ogrenci = Ogrenci(sinif, isim, soyisim, numara)
            ogrenci.kayit()
        elif secim == "2":
            sinif = input("Sınıf: ")
            numara = input("Numara: ")
            ogrenci = Ogrenci(sinif, None, None, numara)
            ogrenci.sil()
        elif secim == "3":
            sinif = input("Sınıf: ")
            numara = input("Numara: ")
            ogrenci = Ogrenci(sinif, None, None, numara)
            ogrenci.gorntuleme()
        elif secim == "cikis":
            break

class Ogrenci:
    def __init__(self, sinif, isim, soyisim, numara):
        self.sinif = sinif
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara

    def kayit(self):
        if self.sinif == "m":
            mongoCol = mongoDB["m"]
            data = {
                '_id': self.numara,
                'ad': self.isim,
                'soyad': self.soyisim
            }
            mongoCol.insert_one(data)
            print(f"{self.numara}'lı öğrenci kayıt edildi!")

    def coklu_kayit(self):
        pass

    def sil(self):
        if self.sinif == "m":
            mongoCol = mongoDB["m"]
            data = {
                '_id': self.numara
            }
            mongoCol.delete_one(data)
            print(f"{self.numara}'lı öğrenci silindi!")

    def gorntuleme(self):
        if self.sinif == "m":
            mongoCol = mongoDB["m"]
            data = {
                '_id': self.numara
            }
            x = mongoCol.find_one(data)
            print(x)
class Sinav:
    pass


secim()