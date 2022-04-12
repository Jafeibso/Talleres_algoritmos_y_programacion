#Entradas
mujeres=int(input("Ingrese cantidad de mujeres: "))
hombres=int(input("Ingrese cantidad de hombres: "))
#Caja Negra
Estudiantes=mujeres+hombres
PM=(mujeres/Estudiantes)*100
PH=(hombres/Estudiantes)*100
#Salida
print("El porcentajes de estudiantes hombres es:",round(PH,2), "%")
print("El porcentajes de estudiantes mujeres es:",round(PM,2), "%")