a=int(input())
b=int(input())
c=int(input())
d=int(input())
if d>=5:
    if c<9:
        print("El numero redondeado es:",str(a)+str(b)+str(c+1)+str(0))
    else:
        print("El numero redondeado es:",str(a)+str(b+1)+str(0)+str(0))
elif c>=5:
    if b<9:
        print("El numero redondeado es:",str(a)+str(b+1)+str(0)+str(0))
    else:
        print("El numero redondeado es:",str(a+1)+str(0)+str(0)+str(0))
elif b>=5:
    print("El numero redondeado es:",str(a+1)+str(0)+str(0)+str(0))
if d<5 and c<5 and b<5:
    print("El numero redondeado es: ",str(a)+str(b)+str(0)+str(0))