"""2-Mostrar una lista ordenada de los números
que ingresan por teclado (se termina de ingresar
datos ingresando un número negativo) """

lista = []

while True:
    numero = input("> ").replace(" ","")
    if numero == "" or numero.isalpha():
        print("ingrese un n°")
    else:
        numero = int(numero)
        if numero < 0:
            break
        else:
            lista.append(numero)
      
#muestra la lista de menor a mayor
print (sorted(lista))
