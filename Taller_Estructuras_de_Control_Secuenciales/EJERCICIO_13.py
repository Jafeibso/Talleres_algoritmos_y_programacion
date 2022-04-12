#ENTRADA
b50000=int(input("Ingrese cantidad de billetes de 50000: "))
b20000=int(input("Ingrese cantidad de billetes de 20000: "))
b10000=int(input("Ingrese cantidad de billetes de 10000: "))
b5000=int(input("Ingrese cantidad de billetes de 5000: "))
b2000=int(input("Ingrese cantidad de billetes de 2000: "))
b1000=int(input("Ingrese cantidad de billetes de 1000: "))
b500=int(input("Ingrese cantidad de billetes de 500: "))
b100=int(input("Ingrese cantidad de billetes de 100: "))
#CAJA NEGRA
dinero=(b50000*50000)+(b20000*20000)+(b10000*10000)+(b5000*5000)+(b2000*2000)+(b1000*1000)+(b500*500)+(b100*100)
#SALIDA
print("El banco contiene la siguiente cantidad de dinero:", dinero)