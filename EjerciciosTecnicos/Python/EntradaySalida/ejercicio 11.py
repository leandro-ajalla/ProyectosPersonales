numero = int(input("Ingrese un numero de cuatro cifras: "))
n1 = int ((numero - (numero % 100)) / 1000)
n2 = int ((numero % 1000) / 100)
n3 = int ((numero % 100) / 10)
n4 = numero % 10
suma = n1 + n2 + n3 + n4
print ("La suma de los digitos de", numero, "es", suma, "(", n1, "+", n2, "+", n3, "+", n4,")")