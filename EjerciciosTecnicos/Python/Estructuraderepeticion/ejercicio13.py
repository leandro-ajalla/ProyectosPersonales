"""Ingresar valores de temperatura (entre 10°C y 50°C)
Al finalizar el ingreso de datos mostrar: mayor, menor, promedio
y cantidad de valores ingresados
(finaliza ingresando -1. Evitar ingreso de valores incorrectos.)"""


print ("ingrese valores:")
cantidad = 0
suma = 0
promedio = 0
SALIR = -1
lista = []
RANGOMIN = 10
RANGOMAX = 50
menor = 0
mayor = 0
while True:
    valores = input("")
    
    if valores.lstrip("-").isdigit():
        valores = int(valores)
        if valores == SALIR: # Valor ingresado es -1, se termina el programa
                break
        
        if valores < RANGOMIN or valores > RANGOMAX:
            print ("valor fuera de rango, debe estar entre", RANGOMIN, "y", RANGOMAX)
        else:
            lista.append(valores) # se guardan los valores en un lista
            cantidad += 1 # cantidad de valores correctos ingresados
            suma += valores # suma de los valores entre 10 y 50
            promedio = suma / cantidad
            mayor = max (lista) 
            menor = min (lista) 
    else:
        print("ingrese un valor numerico")
    
if mayor == menor:
    print("mayor: 0")
    print("menor: 0")
    print("cantidad de valores: ",cantidad)
    print("promedio: ", promedio)
else:
    print("mayor: ", mayor)
    print("menor: ", menor)
    print("cantidad de valores: ", cantidad)
    print("promedio: ", promedio)
    
        