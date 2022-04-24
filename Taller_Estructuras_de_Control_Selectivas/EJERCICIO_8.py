p=int(input("Inserter el valor de P: "))
q=int(input("Inserter el valor de Q: "))
e=(p**3)+(q**4)-(2*(p**2))
if e>680:
    print("Los valores","P=",p,"y Q=",q,"satisfacen los valores",e,">680")
else:
    print("Los valores","P=",p,"y Q=",q,"no satisfacen los valores",e,"<680")