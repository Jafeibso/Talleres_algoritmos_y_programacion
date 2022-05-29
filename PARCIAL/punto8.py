cp=int(input(""))
c=0
list=[]
while cp>0:
    res=input("")
    #ganadas
    if res=="tijeras papel":
        cp=cp-1
        c=c+1
        print("Caso #", c,": ¡LaVidaEsdura!")

    if res=="papel piedra":
        cp=cp-1
        c=c+1
        print("Caso #", c,": ¡LaVidaEsdura!")

    if res=="piedra lagarto":
        cp=cp-1
        c=c+1
        print("Caso #", c,": ¡LaVidaEsdura!")

    if res=="lagarto Holk":
        cp=cp-1
        c=c+1
        print("Caso #", c,": ¡LaVidaEsdura!")

    if res=="Holk tijeras":
        cp=cp-1
        c=c+1
        print("Caso #", c,": ¡LaVidaEsdura!")

    if res=="tijeras lagarto":
        cp=cp-1
        print("Caso #", c,": ¡LaVidaEsdura!")

    if res=="lagarto papel":
        cp=cp-1
        c=c+1
        print("Caso #", c,": ¡LaVidaEsdura!")

    if res=="papel Holk":
        cp=cp-1
        c=c+1
        print("Caso #", c,": ¡LaVidaEsdura!")

    if res=="Holk piedra":
        cp=cp-1
        c=c+1
        print("Caso #", c,": ¡LaVidaEsdura!")

    if res=="piedra tijeras":
        cp=cp-1
        c=c+1
        print("Caso #", c,": ¡LaVidaEsdura!")
    
    #empate
    if res=="piedra piedra":
        cp=cp-1
        c=c+1
        print("Caso #", c,": ¡Otra vez!")
    
    if res=="papel papel":
        cp=cp-1
        c=c+1
        print("Caso #", c,": ¡Otra vez!")

    if res=="tijeras tijeras":
        cp=cp-1
        c=c+1
        print("Caso #", c,": ¡Otra vez!")
    
    if res=="Holk Holk":
        cp=cp-1
        c=c+1
        print("Caso #", c,": ¡Otra vez!")

    if res=="lagarto lagarto":
        cp=cp-1
        c=c+1
        print("Caso #", c,": ¡Otra vez!")

    #perdida

    if res=="papel tijeras":
        cp=cp-1
        c=c+1
        print("Caso #", c,": ¡Siempre hay un próximo semestre!")

    if res=="piedra papel":
        cp=cp-1
        c=c+1
        print("Caso #", c,": ¡Siempre hay un próximo semestre!")

    if res=="lagarto piedra":
        cp=cp-1
        c=c+1
        print("Caso #", c,": ¡Siempre hay un próximo semestre!")

    if res=="Holk lagarto":
        cp=cp-1
        c=c+1
        print("Caso #", c,": ¡Siempre hay un próximo semestre!")

    if res=="tijera Holk":
        cp=cp-1
        c=c+1
        print("Caso #", c,": ¡Siempre hay un próximo semestre!")

    if res=="lagarto tijeras":
        cp=cp-1
        c=c+1
        print("Caso #", c,": ¡Siempre hay un próximo semestre!")

    if res=="papel lagarto":
        cp=cp-1
        c=c+1
        print("Caso #", c,": ¡Siempre hay un próximo semestre!")

    if res=="Holk papel":
        cp=cp-1
        c=c+1
        print("Caso #", c,": ¡Siempre hay un próximo semestre!")

    if res=="piedra Holk":
        cp=cp-1
        c=c+1
        print("Caso #", c,": ¡Siempre hay un próximo semestre!")

    if res=="tijeras piedra":
        cp=cp-1
        c=c+1
        print("Caso #", c,": ¡Siempre hay un próximo semestre!")