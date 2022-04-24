k=int(input("Ingrese la cantidad de kilometros recorridos: "))
if(k<300):
    print("El valor a pagar es de 50000 COP")
if(k>=300 and k<1000):
    kr1=k-300
    ce=kr1*30000
    vp1=70000+ce
    print("El valor a pagar es de: ",vp1, " COP")
if(k>=1000):
    kr2=k-1000
    ce1=kr2*9000
    vp2=150000+ce1
    print("El valor a pagar es de: ",vp2, " COP")