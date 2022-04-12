#ENTRADAS
precio=float(input("Ingrese el precio del productos a vender: "))
cuota=int(input("Ingrese el valor mensual de las cuotas: "))
#CAJA NEGRA
pcuotas=cuota*12
recargo=pcuotas-precio
porcentajerecargo=(recargo*100)/precio
#SALIDAS
print("El valor a pagar de contadao es:", precio)
print("El valor a pagar a cuotas es:", pcuotas)
print("El porcentaje de recargo por el pago a cuotas es de:", porcentajerecargo, "%")