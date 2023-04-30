
valor1 = int(input("ingrese el rango minimo: "))
valor2 = int(input("ingrese el rango maximo: "))

lista = []
contador=0
suma = 0

for numero in range(valor1, valor2):
    
    contador += 1
    suma += numero
    lista.append(numero)

print("25 valores random:", sorted(lista))
    