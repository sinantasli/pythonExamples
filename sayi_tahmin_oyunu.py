import random
import time

print("""
***********************************

1 ile 40 arasında sayı tahmin oyunu

***********************************
""")

random_sayi=random.randint(1,40)

tahmin_hakkı=7

while True:
    tahmin=input("tahmin ettiğiniz sayıyı girin ..")
    tahmin =int(tahmin)
    if(tahmin>random_sayi):
        print("bilgiler alınıyor ...")
        time.sleep(1)
        print("daha küçük bir sayı girin ..")
        tahmin_hakkı -=1
    elif (tahmin<random_sayi):
        print("bilgiler alınıyor...")
        time.sleep(1)
        print("daha büyük bir sayı girin..")
        tahmin_hakkı-=1
    else:
        print("bilgiler alınıyor..")
        time.sleep(1)
        print("tebrikler doğru tahmin ettiniz ..")
        print("sayı ",random_sayi)
        break
    if(tahmin_hakkı==0):
        print("tahmin hakkınız kalmadı..")
        print("sayı " ,random_sayi)
        break
