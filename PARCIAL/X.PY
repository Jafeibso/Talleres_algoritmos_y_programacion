banco=[[1,50000],[2,10000],[3,85000], [4,65000],[7,15000]]
cuenta_mayor=0
numero_cuenta=0
for fila in range(0,4) :
    if (banco[fila][1]<cuenta_mayor) :
        cuenta_mayor=banco[fila][0]
        numero_cuenta=banco[fila][1]
print("El numero de cuenta es:", numero_cuenta)