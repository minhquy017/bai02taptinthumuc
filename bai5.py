from random import randint
def tap_tin5():
    dem=0
    f=input("nhập đường dẫn : ")
    x=[randint(-1000,1000) for i in range(1000)]
    print(x)
    for i in x:
        if dem <9:
            x1=open(f,"a")
            nhap = str(i) + ","
            x1.write(nhap)
            x1.close()
            dem+=1
        else:
            x1=open(f,"a")
            nhap =str(i)+'\n'
            x1.write(nhap)
            x1.close()
            dem=0
    x1=open(f,"r")
    x2=x1.readlines()
    for i in x2:
        print(i.replace(",","\t"))
    x1.close()
tap_tin5()




