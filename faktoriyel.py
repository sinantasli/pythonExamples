import time


def faktoriyell(a):
    a=int(a)
    count =1
    for i in range(1,a+1):
        count *=i
    return count
while True:
    sayı=input("lütfen bir sayı giriniz .")
    if(sayı=='q'):
        print("Programdan çıkılıyor ...")
        time.sleep(1)
        print("Program sonlandı.")
        break
    else:
        print("Hesaplanıyor ...")
        time.sleep(1)
        deger = faktoriyell(sayı)

        print("Sonuç : {}".format(deger))
