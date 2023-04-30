frase = input("ingrese frase: ")
mayuscula= 0
minuscula= 0
vocal = 0
consonante = 0
vocales = "AEIOUÁÉÍÓÚ"
consonantes = "bcdfghjklmnñpqrstvwxyz"

# recorre con un for la frase
# utilizando un if verificamos si cada caracter
# es mayuscula o minuscula
# lo suma a su respectivo contador
for i in frase:
    if i.isupper(): 
        mayuscula += 1
    elif i.islower():
        minuscula +=1

# rocorre las vocales
# utilizando el metodo count
for x in vocales:
    vocal= vocal + frase.upper().count(x)

#recorre las consonantes
#utilizando el metodo count
for y in consonantes:
    consonante = consonante + frase.lower().count(y)
    
print("longitud: ", len(frase))
print("mayuscula: ", mayuscula)
print("minuscula: ", minuscula)
print("vocales: ", vocal)
print("consonantes: ", consonante)
