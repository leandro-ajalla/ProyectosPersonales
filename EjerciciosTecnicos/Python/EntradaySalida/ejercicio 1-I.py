"""ingresar dos números enteros y muestren
el resultado de las siguientes operaciones:

N1 + N2	
N1 - N2
N1 * N2
N1 / N2
N1 N2

"División entera" y resto. """

print ("Ingrese el primer numero: ")
n1 = int(input())
print ("Ingrese el segundo numero: ")
n2 = int(input())

suma = n1 + n2
resta = n1 - n2
producto = n1 * n2
division = n1 / n2
potencia = n1 ** n2
divisionentera = n1 // n2
resto = n1 % n2

print ("La suma es: ", suma)
print ("La resta es: ", resta)
print ("El producto es: ", producto)
print ("La division es: ", division)
print ("La potencia es: ", potencia)
print (n1, "dividido", n2, "es", divisionentera, "y sobran", resto)