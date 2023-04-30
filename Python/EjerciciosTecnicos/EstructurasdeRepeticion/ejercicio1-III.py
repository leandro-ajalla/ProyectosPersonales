"""Mostrar los números pares entre dos números que ingresan
tras los números pares entre dos números que
ingresan por teclado."""


inicial = int(input("ingrese nro. inicial: "))
final = int(input("ingrese nro. final: "))
while inicial <= final:
    if (inicial % 2 == 0):
        print (inicial)
        inicial = inicial + 2
        
    
    else:
        print(inicial+1)
        inicial +=1
       
        
    
       
       
        
    


