archivo = open('/Users/javieribarra/Downloads/Talleres_algoritmos_y_programacion/Taller Estructura de Control For/paises.txt', 'r')
#imprima la posicion de colombia
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Colombia: Bogotá\n"):
    break
  lista=[]   
print(c)
"""
#Imprima todos los paises
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""
#Imprima todas las Capitales
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""  
#Imprimir todos los paises que inicien con la letra C
"""
lista=[]
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
for i in paises:
  if(i[0]=="C"):
    print(i)
"""  
#imprima todas las capitales que inicien con la leta B
"""
lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
  if(i[0]=="B"):
    print(i)  
"""
#Cuente e imprima cuantas ciudades inician con la latra M  
""""
lista=[]
ciudad=[]
contador=0
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)-1):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista.clear()
for i in ciudad:
  if(i[0]=="M"):
    contador=contador+1
    print(i)  
print(contador)
"""
#Imprima todos los paises y capitales, cuyo inicio sea con la letra U
"""
for i in archivo:
  if(i[0]=="U"):
    a=i.index(":")
    if (i[a+2]=="U"):
      print(i)
    else:
      print("No hay paises que cumplan con la condición")
      break
"""

#Cuente e imprima cuantos paises que hay en el archivo
"""
lista=[]
contador=0
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  contador=contador+1
  lista=[]
print(contador)
"""
#Busque e imprima la ciudad de Singapur
"""
lista=[]
ciudad=[]
contador=0
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)-1):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista.clear()
for i in ciudad:
  if(i[0]=="S"):
    if(i=="Singapur"):
      print(i)
"""
#Busque e imprima el pais de Venezuela y su capital
"""
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  if(a=="Venezuela: Caracas\n"):
    break
  lista=[]   
print(a)
"""
#Cuente e imprima las ciudades que su pais inicie con la letra E
"""
lista=[]
ciudad=[]
contador=0
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)-1):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista.clear()
for i in ciudad:
  if(i[0]=="E"):
    contador=contador+1
    print(i)  
print(contador)
"""
#Busque e imprima la Capiltal de Colombia
"""
lista=[]
capital=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  if (a=="Colombia"):
    a=i.index(":")
    for r in range(a+2,len(i)):
      capital.append(i[r])
      a="".join(capital)
    print(a)
  lista=[]
"""


#imprima la posicion del pais de Uganda
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Uganda: Kampala\n"):
    break
  lista=[]   
print(c)
"""
#imprima la posicion del pais de Mexico
"""
c=0
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  lista=[]
  c=c+1
  if (a=="México"):
    print(c)
"""
"""
El alcalde de Antananarivo contrato a algunos alumnos de la Universidad Ean para corregir el archivo de países.txt, ya que la capital de Madagascar NO es rey julien es Antananarivo, espero que el alcalde se vaya contento por su trabajo. Utilice un For para cambiar ese Dato
"""
#Agregue un país que no esté en la lista 
"""
archivo=open("/Users/javieribarra/Downloads/Talleres_algoritmos_y_programacion/Taller Estructura de Control For/paises.txt","a")
archivo.write("\nUniland: Ean")
"""
archivo.close()
