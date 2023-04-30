superficie = int(input("Ingrese la supercie: "))
lata = 20 * 3
otro = superficie / lata
cant = superficie % lata
if cant > 0:
    otro = int (otro + 1)
print ("Necitas comprar", otro, "latas")
