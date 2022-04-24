c=float(input("Ingrese el monto a invertir "))
i=float(input("Ingrese el porcentaje de interes (en %): "))
di=c*(i/100)
dt=c+di
if(di>100000):
    print("El dinero total por los intereses es: ", di)
    print("Se debe reinvertir")
elif(di<=100000):
    print("El dinero total por los intereses es: ", di)
    print("No se debe reinvertir")