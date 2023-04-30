"""Informar superficie y perímetro de un rectángulo

Nota:
superficie = ladoMayor * ladoMenor
perímetro = ladoMayor * 2 + ladoMenor * 2"""



print ("ingresar medidad de un lado: ")
ladomayor = int(input())
print ("ingresar medida del otro lado: ")
ladomenor = int(input())
superficie = ladomayor * ladomenor
perimetro = (ladomayor * 2) + (ladomenor * 2)
print ("la superficie es: ", superficie)
print ("el perimetro es: ", perimetro)