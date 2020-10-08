
def asal_bul(sayı):
    i=3
    count=0
    asal_sayilar=list()
    asal_sayilar.append(2)
    while (i<sayı):

        for j in range(2,i):
            if( i % j == 0):
                count +=1

        if(count == 0):
            asal_sayilar.append(i)

        count = 0

        i +=1

    print("Girilen sayıya kadar olan asal sayılar ")

    for i in asal_sayilar:
        print(i)

    print(" {}  tane ".format(len(asal_sayilar)) )






sayı=int(input("Sayı giriniz ."))

asal_bul(sayı)
