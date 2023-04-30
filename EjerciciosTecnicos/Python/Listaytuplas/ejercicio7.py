"""Generar una lista de 25 valores aleatorios
entre dos valores que ingresa el usuario;
mostrarla y a continuación informar:
máximo, mínimo, promedio, sumatoria, diferencia
entre máximo y mínimo de los datos generados."""

# importa numeros aleatorios
import random



lista = []
contador=0
suma = 0

while True:
    valor1 = input("ingrese el rango minimo: ").replace(" ","")
    valor2 = input("ingrese el rango maximo: ").replace(" ","")    
    if valor1.strip("-").isdigit() and valor2.strip("-").isdigit():
        valor1 = int(valor1)
        valor2 = int(valor2)
        if valor1 >= valor2:
            print("ingreso incorrecto de los rangos")
        else:
            while contador < 25:
                num = random.randint(valor1, valor2)
                lista.append(num)
                contador +=1
                suma += num
                promedio = suma / 25
            print("25 valores random:", sorted(lista))
            print("valor maximo:", max(lista))
            print("valor minimo:", min(lista))
            print("promedio: ", promedio)
            print("sumatoria: ",suma)
            print("diferencia n° mayor y n° menor:" ,max(lista) - min(lista))
    else:
        print("solo se ingrese el rango en n°")
        break
    
    
      

 