d=input("Ingrese los datos de esta manera A,B,C,D (separados con una coma): ")
a,b,c,d=d.split(",")
a=int(a)
b=int(b)
c=int(c)
d=int(d)
if(d==0):
    o1=(a-c)**2
    print("El resultado es: ",o1)
elif(d>0):
    o2=((a-b)**3)/d
    print("El resultado es: ",o2)