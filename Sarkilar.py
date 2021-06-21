import sqlite3
import time
from functools import reduce


class SarkiBilgi():
    def __init__(self,sarkiadi,sanatci,album,produksiyon,sure):
        self.sarkiadi = sarkiadi
        self.sanatci = sanatci
        self.album = album
        self.produksiyon = produksiyon
        self.sure = sure
    def __str__(self):
         return "Şarkı İsmi: {} \nSanatçı: {} \nAlbüm: {} \nProdüksiyon: {} \nSüre: {}\n,".format(self.sarkiadi,self.sanatci,self.album,self.produksiyon,self.sure)

class Sarkilar():
    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("Sarkilar.db")
        self.cursor = self.baglanti.cursor()
        sorgu = "Create Table If not exists sarkilar (Şarkı_Adı TEXT,Sanatçı TEXT,Albüm TEXT,Produksiyon TEXT,Süre INT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()

    def baglanti_sonlandir(self):
        self.baglanti.close()
    
    def sarkilari_goster(self):
        sorgu = "Select * from sarkilar"
        self.cursor.execute(sorgu)
        sarkilar = self.cursor.fetchall()
        if len(sarkilar) == 0:
            print("Herhangi Bir Şarkı Bulunmuyor.")
        else:
            for i in sarkilar:
                sarkibilgi = SarkiBilgi(i[0],i[1],i[2],i[3],i[4])
                print(sarkibilgi)
        self.baglanti.commit()

    def sarki_ekle(self,SarkiBilgi):
        sorgu = "Insert into sarkilar Values(?,?,?,?,?)"
        self.cursor.execute(sorgu,(SarkiBilgi.sarkiadi,SarkiBilgi.sanatci,SarkiBilgi.album,SarkiBilgi.produksiyon,SarkiBilgi.sure,))
        self.baglanti.commit()

    def sarki_sil(self,sarkiadi):
        sorgu = "Delete from kitaplar where sarkiadi= ?"
        self.cursor.execute(sorgu,(sarkiadi,))
        self.baglanti.commit()

    def ToplamSureHesapla(self):
        sure = 0
        sorgu = "select Süre from sarkilar "
        self.cursor.execute(sorgu)
        data = self.cursor.fetchall()
        for i in data:
            a = reduce(lambda  x,y: x+y,data)
            b = reduce(lambda x,y: x+y, a)
           
        print(str(b) + " " + "Saniye")



