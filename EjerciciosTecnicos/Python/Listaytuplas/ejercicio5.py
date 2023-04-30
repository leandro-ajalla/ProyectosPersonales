lista = []
mensaje = input("> ").replace(" ","")

for x in mensaje.lower():
    if x not in lista:
        lista.append(x)
print (sorted(lista))