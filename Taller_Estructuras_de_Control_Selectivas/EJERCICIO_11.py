F=float(input("Ingrese la temperatura en Fahrenheit: "))
d=" "
if (F>85 and F<=120):
    d="Natación"
elif (70<F and F<=85):
    d="Tenis"
elif (32<F and F<=70):
    d="Golf"
elif (10<F and F<=32):
    d="Esquí"
elif (F<=10 and F>0):
    d="Marcha"
else:
    d="La temperatura no corresponde a ningún deporte"
print("El deporte a practicar es: ",d)