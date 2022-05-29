ajedrez=[[0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0],[0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0]]

c=0
for fila in range(0,8):
    for columna in range(0,8):
        if(ajedrez[fila][columna]==1):
            c=c+1
print(c)