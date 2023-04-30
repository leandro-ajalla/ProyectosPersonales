"""Hacer un programa que genere un número de N cifras
y pregunte al usuario números hasta que lo adivine.
Mostrar la cantidad de intentos usados para adivinar
el número."""

import random
intentos = 1
rangomin = 0
rangomax = 10
magia = random.randint(rangomin, rangomax)

while True:
    numero = int(input(f"ingrese el numero entre {rangomin} y {rangomax}: "))
    if numero == magia:
        print("adivinaste el numero")
        break
    else:
        intentos += 1
        
print("intentos:", intentos)