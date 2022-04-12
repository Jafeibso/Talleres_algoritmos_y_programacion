#ENTRADAS
x=float(input("Ingrese la cantidad de naranjas que había en el lote: "))
y=float(input("Ingrese el costo de la docena de naranjas en Bs: "))
k=float(input("Ingrese el valor del dinero obtenido después de vender todas las naranjas en Bs: "))
#CAJA NEGRA
costo=(x/12)*y
ganancia=k-costo
porcentaje=(ganancia/costo)*100
#SALIDAS
print("El porcentaje de ganancia obtenida en la inversión es de:", porcentaje, "%")