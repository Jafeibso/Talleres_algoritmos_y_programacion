#ENTRADA
pfp=int(input("Ingrese el precio final pagado por el producto: "))
pvp=int(input("Ingrese el precio de venta al público del producto: "))
#CAJA NEGRA
r3=(pfp*100)/pvp
descuento1=100-r3
descuento2=descuento1/100
descuento3=pvp*descuento2
#SALIDA
print("El valor del descuento aplicado es de:", descuento3, "$")
print("El descuento que se le ha aplicado es del:", descuento1, "%")