import random
list=["hola", "ola", "delfin", "casa", "liberar", "trabajar", "estudiar"]
alet=random.choice(list)
t=len(alet)
print(alet)
print(t)
lista1=[alet]
print(lista1)
lista2=[]
ci=0
while True:
    try:
        if ci==t:
            print("Se acabaron los intentos")
            break
        letra=int(input("Letras a al z: "))
        if(letra in lista1):
            if(alet==num):
                print("Ganaste")
                break
            else:
                ci=ci+1
                print(f"Intento número {ci}")
        else:
                print("Debe ser entre 1 y 10")
    except:
        print("Debe ser un número entero")
