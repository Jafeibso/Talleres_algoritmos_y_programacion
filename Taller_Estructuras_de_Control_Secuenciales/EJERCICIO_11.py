#ENTRADAS
nombre=str(input("Ingrese nombre del empleado: "))
ht=int(input("Ingrese el numero de horas trabajadas: "))
ph=float(input("Ingrese el valor de pago: "))
he=int(input("Ingrese el numero de horas extras trabajadas: "))
hj=int(input("Ingrese la cantidad de hijos: "))
#CAJA NEGRA
sb=(ht*ph)
d=(sb*0.05)+(sb*0.02)+(sb*0.07)
a=sb+250000+(173000*hj)+180000+(((ph*0.25)+ph)*he)
sn=a-d
#SALIDA
print("Las asignaciones al empleado son:", a)
print("Las deducciones al empleado son:", d)
print("El salario neto a pagar al empleado son:", sn)