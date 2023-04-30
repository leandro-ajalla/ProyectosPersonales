"""Determinar si un año ingresado por teclado es o no bisiesto"""


año = int(input("Año: "))

"""verifica si el año es o no bisiesto
Un año es bisiesto si es múltiplo de 4
Los años múltiplos de 100 no son bisiesto,
salvo si ellos también son múltiplo de 400"""
if año < 0 :
    print("año no valido")
else:
    if año % 4 == 0 and año % 100 != 0 or año % 400 == 0:
        print ("bisiesto")
    else:
        print ("no bisiesto")

