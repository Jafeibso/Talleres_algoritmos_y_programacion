n=input("Ingrese nombre del cliente:")
c=float(input("Ingrese el valor de la compra (COP): "))
if c<50000:
    print("No hay decuento","El valor a pagar es de: ",c, " COP")
    print("El cliente",n,"tiene un descuento de 0%","debe pagar:",c,"COP")
if c>=50000 and c<=100000:
    d1=c*0.05
    print("El cliente",n,"tiene un descuento del 5%",".El valor descontado de su compra de",c,"es de",d1,".El valor a pagar es de: ",c-d1, " COP")
if c>100000 and c<=700000:
    d2=c*0.11
    print("El cliente",n,"tiene un descuento del 11%",".El valor descontado de su compra de",c,"es de",d2,".El valor a pagar es de: ",c-d2, " COP")
if c>700000 and c<=1500000:
    d3=c*0.18
    print("El cliente",n,"tiene un descuento del 18%",".El valor descontado de su compra de",c,"es de",d3,".El valor a pagar es de: ",c-d3, " COP")
if c>1500000:
    d4=c*0.25
    print("El cliente",n,"tiene un descuento del 25%",".El valor descontado de su compra de",c,"es de",d4,".El valor a pagar es de: ",c-d4, " COP")