#ENTRADAS
capital=float(input("Ingrese la cantidad del capital en bolivares: "))
tiempo=int(input("Ingrese la cantidad de tiempo (en años): "))
razon=float(input("Ingrese la cantidad de la razon pactada con el banco: "))
#CAJA NEGRA
Interes=(capital*tiempo*razon)/100
#SALIDAS
print("El por ciento anual es:" , Interes)