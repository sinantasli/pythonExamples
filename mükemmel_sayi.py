def mükemmel_bul(sayı):
    toplam=0
    sayı=int(sayı)
    for i in range(1,sayı):
        if(sayı%i==0):
            toplam+=i
    return toplam==sayı
for i in range(1,1000):
    if(mükemmel_bul(i)):
        print(i)

