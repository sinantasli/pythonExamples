onluk =["on ","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]
birlik=["bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"," "]
while True:
    girilen=input("iki basamaklı bir sayı giriniz")
    if(girilen=="q"):
        print("programdan çıkılıyor")
        break
    if(len(girilen)!=2):
        print("lütfen iki basamaklı bir sayı giriniz")
    else:
        liste=girilen
        a=liste[0]
        b=liste[1]
        a=int(a)
        b=int(b)
        print("girilen sayı {} {} ".format(onluk[a-1],birlik[b-1]))
