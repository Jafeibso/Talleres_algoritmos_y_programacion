suma=0
contador=0
for k in range(1,1000):
    suma=round(suma+((k**2)+1)/k,2)
    if suma<=1000:
        contador=contador+1
    else:
        break
print(contador)

