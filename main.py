# kütüphaneler
from ipaddress import ip_address
from openpyxl import load_workbook
import pymongo
# mongodb bağlantı
mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
mongoDB = mongoClient["test"]

# Başlangıçta hangi işlemin yapılmasını seçme menüsü
sayi = 0
def secim():
    # menüyü sürekli açık tutma
    while sayi < 1:
        print('''
        (1) Öğrenci ekle
        (2) Toplu öğrenci ekle
        (3) Öğrenci sil
        (4) Öğrenci görüntüle
        (5) Çıkış     
        ''')
        secim = input('Secim yapınız: ')
        if secim == "1":
            sinif = input("Sınıf :")
            isim = input("İsim: ")
            soyisim = input("Soyad: ")
            numara = input("Numara :")
            ogrenci = Ogrenci(sinif, isim, soyisim, numara, None, None, None, None)
            ogrenci.kayit()
        #! KUllanma çalışmıyor (TODO:satır 65)
        elif secim == "2":
            pass
        elif secim == "3":
            sinif = input("Sınıf: ")
            numara = input("Numara: ")
            ogrenci = Ogrenci(sinif, None, None, numara, None, None, None, None)
            ogrenci.sil()
        elif secim == "4":
            sinif = input("Sınıf: ")
            numara = input("Numara: ")
            ogrenci = Ogrenci(sinif, None, None, numara, None, None, None, None)
            ogrenci.gorntuleme()
        elif secim == "5":
            break

#* Ogrenci ile ilgili tüm işlmeler
class Ogrenci:
    def __init__(self, sinif, isim, soyisim, numara):
        self.sinif = sinif
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        #* coklu_kayit fonksiyonu için gereken methodlar şimdilik kapalı classtan silindi
        #self.satir = satir
        #self.sutun = sutun
        #self.workbook = workbook
        #self.maxSatir = maxSatir

    # Ogrenci sinif, numara, isim, soyisim girerek öğrenci kaydetme (her seferinde sadece bir kişi kayıt edilebilir)
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

    #TODO: Çoklu kayıt yapılamadı en son tekrar dene
    def coklu_kayit(self):
        pass

    # Ogrenci numarsı ile öğrenci silme
    def sil(self):
        if self.sinif == "m":
            mongoCol = mongoDB["m"]
            data = {
                '_id': self.numara
            }
            mongoCol.delete_one(data)
            print(f"{self.numara}'lı öğrenci silindi!")

    # Ogrenci numarası ile öğrenci bilgilerini görme
    def gorntuleme(self):
        if self.sinif == "m":
            mongoCol = mongoDB["m"]
            data = {
                '_id': self.numara
            }
            x = mongoCol.find_one(data)
            print(x)   

def test():
    sinif = input("sinif: ")
    numara = input("numara: ")
    sinavAdi = input("Sınav adı: ")
    sinavPuani = input("Sinav puanı: ")
    sinav = Sinav(sinif, numara, sinavAdi, sinavPuani, None, None, None, None)
    sinav.sinavKayit()
class Sinav:
    def __init__(self, sinif, numara, sinavAdi, sinavPuan, sira, sutun, maxSatir, workbook):
        self.sinif = sinif
        self.numara = numara
        self.sinavAdi = sinavAdi
        self.sinavPuan = sinavPuan
        self.sira = sira
        self.sutun = sutun
        self.maxSatir = maxSatir
        self.workbook = workbook

    # tekli sınav kayıt (tek senerde bir öğrenci)
    def sinavKayit(self):
        if self.sinif == "m":
            mongoCol = mongoDB["m_sinav"]
            data = {
                '_id': self.numara,
                'sinavlar': 
                    {
                        self.sinavAdi: self.sinavPuan 
                    }
            }
            mongoCol.insert_one(data)
            print(f"{self.numara}'lı öğrencinin {self.sinavAdi} adlı sınavından {self.sinavPuan}'ı eklendi")

    # çoklu sınav kayıt gerekli parametreler ()
    def coklu_sinavKayit(self):
        pass

    # tek bir öprenciden tek bir sinav silme 
    def sinavSil(self):
        pass

    # belirli sınavların ortalamasını alarak sonuclarını excel dosyasına kayıt etme
    def sinavHesapla(self):
        pass


test()

# programı başlatan fonksiyon
#secim()