#ENTRADAS
salariobase=float(input("Ingrese el valor de su salario base: "))
venta1=float(input("Ingrese el valor de su venta 1: "))
venta2=float(input("Ingrese el valor de su venta 2: "))
venta3=float(input("Ingrese el valor de su venta 3: "))
#CAJA NEGRA
ventastotales=venta1+venta2+venta3
comision=ventastotales*0.10
sbcc=salariobase+comision
#SALIDA
print("El vendedor realiza una comisión de:", comision, "Y este mes va a recibir un salario total de:", sbcc)