import random
contador = 0
lista = []
listapares = []
listaimpares = []

while contador < 20:
    num = random.randint(1, 99)
    lista.append(num)
    contador += 1
for x in lista:
    if (x % 2) == 0:
        listapares.append(x)
    else:
        listaimpares.append(x)

print(sorted(lista))
print(sorted(listapares))
print(sorted(listaimpares))