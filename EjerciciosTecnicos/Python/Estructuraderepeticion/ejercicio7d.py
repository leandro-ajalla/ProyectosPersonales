altura =int(input("ingrese altura: "))
cant = 0
while cant < altura:
    espacios = altura - cant -1
    asteriscos = 1 + cant * 2
    print (" " * espacios + "*" * asteriscos)
    cant = cant + 1
            