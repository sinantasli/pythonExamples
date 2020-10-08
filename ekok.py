def ekok(a,b):
    a=int(a)
    b=int(b)
    ekk=1
    liste=list()
    i = 2
    while True:
        if(a==1 and b==1):

            if(len(liste)>0):
                for l in liste:
                    ekk*=l

            break


        else:
            if(a%i==0 and b%i==0):
                a=a/i
                b=b/i
                liste.append(i)

            elif(a%i==0 or b%i==0):
                liste.append(i)
                if(a%i==0):
                    a = a / i

                else:
                    b = b / i

            else:
                i+=1

    return ekk


while True :
    sayı1=input("birinci sayıyı giriniz")
    sayı2=input("ikinci sayıyı giriniz")
    if(sayı1=="q" or sayı2=="q"):
        print("programdan çıkılıyor")
        break
    else:
        deger=ekok(sayı1,sayı2)
        print("ekok : {}".format(deger))