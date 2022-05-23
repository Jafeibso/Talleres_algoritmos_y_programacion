dicc={'Mikel': 3, 'Ane': 8, 'Amaia': 12, 'Unai': 5, 'Jon': 8, 'Ainhoa': 7, 'Maite': 5}
lista=dicc.values()
print(lista)
lista_A=[]
for i in lista:
    if i not in lista_A:
        lista_A.append(i)
print(lista_A)