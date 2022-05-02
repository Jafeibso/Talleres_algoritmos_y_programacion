e=int(input("Ingrese el numero de estudiantes: "))
p_a=0
p_b=100
c=0
sum=0
for i in range(1,e+1):
    n=input("Ingrese nombre: ")
    p=int(input("Ingrese puntaje del estudiante: "))
    sum=sum+p
    if p>=p_a:
        p_a=p
        n_a=n
    if p<=p_b:
        p_b=p
        n_b=n
x=round(sum/e,2)
print("El estudiante con mayor puntaje es: ",n_a)
print("El estudiante con menor puntaje es: ",n_b)
print("El puntaje maximo obtenido es:",p_a)
print("El puntaje menor es:",p_b)
print("El promedio de puntaje es:",x)
#Profesor el hallar los pocentajes de los estudiantes se deben realizar pasos que no hemos visto en clase.