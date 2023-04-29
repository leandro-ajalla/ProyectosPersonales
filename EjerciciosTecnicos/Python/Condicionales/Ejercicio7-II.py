"""Ingresar tres números y representarlos gráficamente
ordenados de mayor a menor en forma horizontal"""



n1 = int(input("ingrese n1: "))
n2 = int(input("ingrese n2: "))
n3 = int(input("ingrese n3: "))
if n1 > n2 and n1 > n3:
    print ( "*" * 20, n1)
    if n2 > n3:
        print ( "*" * 10, n2)
        print ( "*" * 5, n3)
    else:
        print ( "*" * 10, n3)
        print ( "*" * 5, n2)
        
if n2 > n1 and n2 > n3:
    print ( "*" * 20, n2)
    if n1 > n3:
        print ( "*" * 10, n1)
        print ( "*" * 5, n3)
    else:
        print ( "*" * 10, n3)
        print ( "*" * 5, n1)

if n3 > n1 and n3 > n2:
    print ( "*" * 20, n3)
    if n2 > n1:
        print ( "*" * 10, n2)
        print ( "*" * 5, n1)
    else:
        print ( "*" * 10, n1)
        print ( "*" * 5, n2)

    
