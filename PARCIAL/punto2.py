n=int(input(""))
m=int(input(""))
b2=2
b5=5
b10=10
b20=20
b50=50
b100=100
vueltas=m-n
if vueltas/(b2+b5)==1:
    print("possible")
elif vueltas/(b2+b5)==1:
    print("possible")
elif vueltas/(b2+b10)==1:
    print("possible")
elif vueltas/(b2+b20)==1:
    print("possible")
elif vueltas/(b2+b50)==1:
    print("possible")
elif vueltas/(b2+b100)==1:
    print("possible")
else:
    if vueltas/(b5+b10)==1:
        print("possible")
    elif vueltas/(b5+b20)==1:
        print("possible")
    elif vueltas/(b5+b50)==1:
        print("possible")
    elif vueltas/(b5+b100)==1:
        print("possible")
    else:
        if vueltas/(b10+b20)==1:
            print("possible")
        elif vueltas/(b10+b50)==1:
            print("possible")
        elif vueltas/(b10+b100)==1:
            print("possible")
        else:
            if vueltas/(b20+b50)==1:
                print("possible")
            elif vueltas/(b20+b100)==1:
                print("possible")
            else:
                if vueltas/(b50+b100)==1:
                    print("possible")
                else:
                    print("impossible")




