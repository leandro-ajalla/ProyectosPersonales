numero = int(input("ingrese un numero: "))
factorial = 1
cant = 1

while cant <= numero:
    factorial = factorial * cant
    cant = cant + 1
print ("el factorial de", numero, "es", factorial)