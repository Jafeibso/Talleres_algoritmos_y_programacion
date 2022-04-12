#ENTRADAS
chelines=float(input("Ingrese cantidad de Chelines austriacos: "))
dragmas=float(input("Ingrese cantidad de dracmas griegos: "))
pesetas=float(input("Ingrese cantidad de pesetas: "))
#CAJA NEGRA
chelin_peset=chelines*(956871/100)
drac_ff=dragmas*(88607/100)*(1/20110)
peset_doll=pesetas*(1/122499)
peset_li=pesetas*(100/9289)
#SALIDA
print(chelines, "chelines equivalen a:", round(chelin_peset,3), "pesetas")
print(dragmas, "dracmas griegos equivalen a:", round(drac_ff,3), "francos franceses")
print(pesetas, "pesetas equivalen a:", round(peset_doll,3), "dolares")
print(pesetas, "pesetas equivalen a:", round(peset_li,3), "liras italianas")