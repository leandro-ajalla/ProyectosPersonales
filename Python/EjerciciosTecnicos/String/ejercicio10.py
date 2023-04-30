frasemaslarga = ""
largoacumulado = 0
cantidadfrases = 0

frase = ""
while frase != "Q":
    frase = input("ingrese frase: ")
    
    if frase != "Q":
        cantidadfrases += 1
        largoacumulado += len(frase)
        
        if len(frase) > len(frasemaslarga):
            frasemaslarga = frase

print("la frase mas larga es:", frasemaslarga)
print(f"y tiene {len(frasemaslarga)} caracteres")
print("long. promedio: ", largoacumulado / cantidadfrases)