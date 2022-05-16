import random
list=["hola", "ola", "delfin", "casa", "liberar", "trabajar", "estudiar"]
alet=random.choice(list)
v=len(alet)
c=v
while v>0:
    p=c-1
    p=v
    letra=int(input("Letras a al z: "))
    for letra in alet:
        print(letra)