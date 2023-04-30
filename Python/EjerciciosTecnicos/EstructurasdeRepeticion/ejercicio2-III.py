"""Imprimir la tabla de multiplicar de un número
entero entre 1 y 10."""


multip = int(input("tabla de multiplicar de: "))
numero = 0
while numero <= 10:
    print (numero, " x ", multip, " = ", numero * multip)
    numero = numero + 1