import math
import time

print("""
*******************************

 HESAP MAKİNESİ

1.Toplama işlemi 

2.Çıkarma işlemi

3.Çarpma işlemi 

4.Bölme işlemi

0.ÇIKIŞ

*******************************
""")
sonuç=None
while True:
    işlem=input("lütfen işlemi seçin.. ")
    işlem=int(işlem)
    if(işlem==1):
        sayı1=input("birinci sayıyı giriniz ..")
        sayı2=input("ikinci sayıyı giriniz ..")
        sayı1=float(sayı1)
        sayı2=float(sayı2)
        sonuç=sayı1+sayı2
        print("işlem yapııyor ..")
        time.sleep(1)
        print("Sonuç : ",sonuç)
    elif(işlem==2):
        sayı1=input("birinci sayıyı girin ..")
        sayı2=input("ikinci sayıyı girin ..")
        sayı1=float(sayı1)
        sayı2=float(sayı2)
        sonuç=sayı1-sayı2
        print("işlem yapılıyor...")
        time.sleep(1)
        print("sonnuç ",sonuç)
    elif(işlem==3):
        sayı1=input("birinci sayıyı girin ...")
        sayı2=input("ikinci sayıyı girin ..")
        sayı1=float(sayı1)
        sayı2=float(sayı2)
        sonuç=sayı1*sayı2
        print("işlem yapılıyor ...")
        time.sleep(1)
        print("sonuç ",sonuç)
    elif(işlem==4):
        sayı1=input("birinci sayıyı girin ..")
        sayı2=input("ikinci sayıyı girin ..")
        sayı1=float(sayı1)
        sayı2=float(sayı2)
        sonuç=sayı1/sayı2
        print("işlem yapılıyor ..")
        time.sleep(1)
        print("sonuç ",sonuç)
    else:
        print("yapmış olduğunuz seçim menümüzde bulunmamaktadır ..")

    if(işlem==0):
        print("programdan çıkılıyor ...")
        time.sleep(1)
        break











