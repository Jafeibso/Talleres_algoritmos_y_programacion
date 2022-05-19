usuarios={ 
    "iperurena": {
        "nombre": "Iñaki",
            "apellido": "Perurena",
            "password": "123123"
        },
        "fmuguruza": {
        "nombre": "Fermín", 
            "apellido": "Muguruza",
            "password": "654321"
        }, 
        "aolaizola": {
            "nombre": "Aimar", 
            "apellido": "Olaizola", 
            "password": "123456"
        } 
    }
c=3
for x in range (c):
    u=input("Ingrese su usuario: ")
    p=input("Ingrese su password: ")
    for i in usuarios:
        if(i==u and usuarios[i]["password"]==p):
            print(usuarios[i]["nombre"], usuarios[i]["apellido"])
            break