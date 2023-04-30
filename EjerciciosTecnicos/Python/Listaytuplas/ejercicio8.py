lista = []
listamenores = []
listamayores = []
listaiguales = []
suma = 0
cantidad = 0

while True:
    numero = input("> ")
    if numero == "":
        break
    if numero.isdigit():
        numero = int(numero)
        lista.append(numero)
        suma = sum (lista)
        promedio = suma / len(lista)

for x in lista:
    if x < promedio:
        listamenores.append(x)
    elif x > promedio:
        listamayores.append(x)
    else:
        listaiguales.append(x)

print("promedio: ", promedio)
print("cantidad: ", len(lista))
print("menor al promedio: ", listamenores)
print("mayor al promedio: ", listamayores)
print("igual al promedio: ", listaiguales)
        
        
            