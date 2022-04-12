#ENTRADAS
horas=int(input("Ingrese el valor de horas trabajadas: "))
precio=float(input("Ingrese el valor correspondiente al salario de una hora: "))
#CAJA NEGRA
pago=(horas*precio)*0.80
#SALIDA
print("El salario neto a pagar es de:", pago)