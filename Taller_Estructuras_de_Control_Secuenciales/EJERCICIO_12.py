#ENTRADA
em=float(input("Ingrese nota examen matematicas: "))
tm1=float(input("Ingrese nota tarea 1 matematicas: "))
tm2=float(input("Ingrese nota tarea 2 matematicas: "))
tm3=float(input("Ingrese nota tarea 3 matematicas: "))
ef=float(input("Ingrese nota examen física: "))
tf1=float(input("Ingrese nota tarea 1 física: "))
tf2=float(input("Ingrese nota tarea 2 física: "))
eq=float(input("Ingrese nota examen química: "))
tq1=float(input("Ingrese nota tarea 1 química: "))
tq2=float(input("Ingrese nota tarea 2 química: "))
tq3=float(input("Ingrese nota tarea 3 química: "))
#CAJA NEGRA
cfm=round((em*0.90)+(((tm1+tm2+tm3)/3)*0.10),2)
cff=round((ef*0.80)+(((tf1+tf2)/2)*0.20),2)
cfq=round((eq*0.85)+(((tq1+tq2+tq3)/3)*0.15),2)
pg=(cfm+cff+cfq)/3
#SALIDA
print("El promedio general del estudiantes es:", pg)