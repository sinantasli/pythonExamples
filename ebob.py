def ebob(a,b):
    a=int(a)
    b=int(b)
    ek=0
    ebb=0
    if(a<=b):
        ek=a
    else:
        ek=b
    for i in range(1,ek+1):
        if(a%i==0 and b%i==0):
            ebb=i
    return ebb
while True:
    sayı1=input("birinci sayıyı giriniz")
    sayı2=input("ikinci sayıyı giriniz")
    if(sayı1=="q" or sayı2=="q"):
        print("programdan çıkılıyor")
        break
    else:
        print(" en büyük ortak bölen {}".format(ebob(sayı1,sayı2)))


