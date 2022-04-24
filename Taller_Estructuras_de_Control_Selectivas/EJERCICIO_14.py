la=float(input("Ingrese la lectura anterior: "))
l=float(input("Ingrese la lectura actual: "))
kw=l-la
if kw>=0 and kw<=100:
    c=4600
    print("El costo de la factura es de: ",(kw*c)," COP")
if kw>100 and kw<=300:
    c=80000
    print("El costo de la factura es de: ",(kw*c)," COP")
if kw>300 and kw<=500:
    c=100000
    print("El costo de la factura es de: ",(kw*c)," COP")
if kw>500:
    c=120000
    print("El costo de la factura es de: ",(kw*c)," COP")