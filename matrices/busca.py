import random
busca_minas=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
for i in range(10):
    fila=random.randint(0,7)
    columna=random.randint(0,7)
    busca_minas[fila][columna]=1
print(busca_minas)
intentos=1
while True:
    try:
        fila=int(input("Digite fila: "))
        columna=int(input("Digite fila: "))
        if(intentos==3):
            print("Ganaste!!")
            break
        if(fila>=0 and fila<=7 and columna>=0 and columna <=7):
            if(busca_minas[fila][columna]!=1):
                intentos=+1
            else:
                print("perdiste!!")
                break
        else:
            print("La fila y la columna deben estar dentro del rango 0..9")
    except:
        print("los numeros deben ser enteros")