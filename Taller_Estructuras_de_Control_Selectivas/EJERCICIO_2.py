s=float(input("Ingrese el salario: "))
if(s<900000):
    a=(s*0.15)+s
else:
    a=(s*0.12)+s
print("El salario con aumento es: ",a)