numero = 1
par = 0
contador = 0
impar = 0
contpar = 0
while contador < 10:
    numero = int(input("ingrese un numero: "))
    contador += 1
    if numero % 2 == 0:
        par += numero
        contpar += 1
        promedio = par / contpar
    else:
        impar += numero

print ("la suma de los impares es:", impar)
print("el promedio de los pares es:", promedio)
    
    
    