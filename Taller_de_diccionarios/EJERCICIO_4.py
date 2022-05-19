dicc={}
for i in range (10):
    na=input("Ingrese nombre del estudiante: ")
    no=float(input("Ingrese nota: "))
    dicc.update({i+1:{"nombre":na, "nota":no}})
aprobados=[]
suspendidos=[]
suma=0
for t in dicc:
    suma=int(dicc[t]["nota"])+suma
    if dicc[t]["nota"]>=6:
        aprobados.append(dicc[t])
    else:
        suspendidos.append(dicc[t])
print("Los estudiantes aprobados son: ", aprobados)
print("Los estudiantes suspendidos son: ", suspendidos)
print("La nota media de los estudiantes es: ", round(suma/10,2))
