#ENTRADA
kv=float(input("Ingrese el costo por kilovatio: "))
lan=int(input("Ingrese el valor de la lectura anterior: "))
lac=int(input("Ingrese el valor de la lectura actual: "))
#CAJA NEGRA
costo=(lac-lan)*kv
#SALIDA
print("El monto a pagar por energía en el mes es de:", costo)