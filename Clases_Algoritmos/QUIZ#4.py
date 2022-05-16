n=0
contador=0
for i in range (1,101):
    numero=int(input())
    contador=contador+1
    if(numero>=n):
        n=numero 
        cn=contador     
print(n)
print(cn)
