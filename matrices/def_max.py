
M=[[8, 14, -6], 
    [12,7,4], 
    [-11,3,21]]
def dibujaMatriz(M):
    for i in range(len(M)):
    print ('[')
    for j in range(len(M[i])):
    print ('{:>3s}'.format(str(M[i][j]))), print (']')
dibujaMatriz(M)