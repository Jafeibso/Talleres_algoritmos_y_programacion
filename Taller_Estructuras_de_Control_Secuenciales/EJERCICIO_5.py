#ENTRADAS
cp1=float(input("Ingrese nota parcial 1: "))
cp2=float(input("Ingrese nota parcial 2: "))
cp3=float(input("Ingrese nota parcial 3: "))
ef=float(input("Ingrese examen final : "))
tf=float(input("Ingrese trabajo final : "))
#CAJA NEGRA
promcp=(cp1+cp2+cp3)/3
porc1=promcp*0.55
porc2=ef*0.30
porc3=tf*0.15
notafinal=porc1+porc2+porc3
#SALIDA
print("La nota final del estudiantes es:", notafinal)