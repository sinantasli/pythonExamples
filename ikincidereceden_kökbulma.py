
print("ax^2 + bx + c")

def kokbul(a,b,c):
    try:
        a=int(a)
        b=int(b)
        c=int(c)
    except Exception:
        print("lütfen sadece rakam giriniz !")
        return
    delta=b*b -4*a*c
    x1=None
    x2=None
    if(delta>0):
        print("Farklı iki reel kök vardır. (x1 != x2) ")
    elif(delta==0):
        print("Çakışık iki kök vardır. (x1=x2) ")
    else:
        print("Gerçel kökler yoktur .")

    if(a!= 0 and b!=0 and c!=0):
        x1=(-b + delta**(0.5))/2*a
        x2=(-b + delta**(0.5))/2*a
        print("girilen denklemin kökleri x1 ={} , x2 = {}".format(x1,x2))
    elif (b == 0 and c == 0):
        x1 = 0
        x2 = 0
        print("girilen denklemin kökleri x1 ={} , x2 = {}".format(x1, x2))
    elif(b==0):
        x1=(-c/a)**(0.5)
        x2=-x1
        print("girilen denklemin kökleri x1 ={} , x2 = {}".format(x1, x2))
    elif(c==0):
        x1=0
        x2=-b/a
        print("girilen denklemin kökleri x1 ={} , x2 = {}".format(x1, x2))


while True:
    sayı1=input("'a' değerini giriniz :" )
    sayı2=input("'b' değerini giriniz : ")
    sayı3=input("'c' değerini giriniz :")
    if(sayı1=='q' or sayı2=='q' or sayı3=='q'):
        print("programdan çıkılıyor .")
        break
    else:
        print(kokbul(sayı1,sayı2,sayı3))
