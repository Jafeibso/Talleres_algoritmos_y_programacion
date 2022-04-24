m=int(input("Ingrese edad del paciente en meses: "))
s=input("Ingrese el sexo del paciente: ")
h=float(input("Ingrese nivel de hemoglobina del paciente: "))
a=m/12
if m>=0 and m<=1:
    if h<13:
        print("El resultado del paciente es positivo. Tiene Anemia")
    else:
        print("El resultado del paciente es negativo. No tiene Anemia")
if m>1 and m<=6:
    if h<10:
        print("El resultado del paciente es positivo. Tiene Anemia")
    else:
        print("El resultado del paciente es negativo. No tiene Anemia")
if m>6 and m<=12:
    if h<11:
        print("El resultado del paciente es positivo. Tiene Anemia")
    else:
        print("El resultado del paciente es negativo. No tiene Anemia")
if a>1 and a<=5:
    if h<11.5:
        print("El resultado del paciente es positivo. Tiene Anemia")
    else:
        print("El resultado del paciente es negativo. No tiene Anemia")
if a>5 and a<=10:
    if h<12.6:
        print("El resultado del paciente es positivo. Tiene Anemia")
    else:
        print("El resultado del paciente es negativo. No tiene Anemia")
if a>10 and a<=15:
    if h<13:
        print("El resultado del paciente es positivo. Tiene Anemia")
    else:
        print("El resultado del paciente es negativo. No tiene Anemia")
if s=="mujer" and a>15:
    if h<12:
        print("El resultado del paciente es positivo. Tiene Anemia")
    else:
        print("El resultado del paciente es negativo. No tiene Anemia")
if s=="hombre" and a>15:
    if h<14:
        print("El resultado del paciente es positivo. Tiene Anemia")
    else:
        print("El resultado del paciente es negativo. No tiene Anemia")