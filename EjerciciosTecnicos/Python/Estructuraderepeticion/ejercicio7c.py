altura =int(input("ingrese altura: "))
cant = 1
while cant <= altura:
    espacios = altura - cant
    print (" " * espacios + "*" * cant)
    cant = cant + 1
            