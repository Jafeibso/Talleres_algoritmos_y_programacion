r=1
while r>=1:
    numero=int(input(""))
    r=numero
    lista=[]
    lista.insert(0,str(numero))
    if numero!=0:
        while r>1:
            r=r-1
            lista.append(str(r))
        lista.reverse()
        a=" ".join(lista)
        print(a)


