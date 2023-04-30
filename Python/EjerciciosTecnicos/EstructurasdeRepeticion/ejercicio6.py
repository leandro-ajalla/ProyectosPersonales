
n1 = int(input("ingrese un numero"))
n2 = int(input("ingrese otro numero"))
cantidad = 0
multiplo = n1 + 1

while True:    
    if multiplo % n1 == 0:
        multiplo += 1
        cantidad +=1
    else:
        multiplo +=1
        if multiplo > n2:
            break
print ("mulmenores(", n1,",", n2, ")->", cantidad)