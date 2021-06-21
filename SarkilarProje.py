from Sarkilar import *
print("""
Şarkılar Programına Hoş Geldiniz.
İşlemler:
1- Şarkıları Göster
2- Şarkı Ekle
3- Şarkı Sil
4- Toplam Süreyi Göster

Çıkmak için 'q' ya basın.

""")
sarkilar = Sarkilar()

while True:
    islem = input("İşlem Seçiniz: ")
    if islem == "q":
        print("Program Sonlandırılıyor.")
        print("Yine Bekleriz")
        break
    elif islem == "1":
        sarkilar.sarkilari_goster()
    elif islem == "2":
        sarkiad = input("Şarkının Adını Giriniz: ")
        sanatci = input("Sanatçı Adını Giriniz: ")
        album = input("Albüm Adını Giriniz: ")
        produksiyon = input("Prodüksiyonun Adını Giriniz: ")
        sure = int(input("Süreyi Saniye cinsinden giriniz: "))
        yeni_sarki = SarkiBilgi(sarkiad,sanatci,album,produksiyon,sure)
        sarkilar.sarki_ekle(yeni_sarki)
    elif islem == "3":
        sarkiad = input("Silinecek Şarkının Adını Giriniz: ")
        sarkilar.sarki_sil(sarkiad)
    elif islem == "4":
        sarkilar.ToplamSureHesapla() 
    else:
        print("Geçersiz İşlem")
        break
