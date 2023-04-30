"""Indique si un número ingresado es
par o impar y si es divisible o no por 3"""


numero = int(input("ingrese un numero: "))
if numero % 2 == 0:
    print ("el numero", numero, "es par")
elif numero % 3 == 0:
    print ("el numero", numero, "es impar y multiplo de 3")
else:
    print ("el numero", numero, "es impar")
        