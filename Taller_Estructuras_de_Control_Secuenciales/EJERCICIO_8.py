import math
#Entrada
a=float(input("Ingrese lado a: "))
b=float(input("Ingrese lado b: "))
c=float(input("Ingrese lado c: "))
#Caja negra
s=(a+b+c)/2
Area=math.sqrt(s*(s-a)*(s-b)*(s-c))
#Salida
print("El área es:", round(Area,2))