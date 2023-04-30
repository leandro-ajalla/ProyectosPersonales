while True:
    palabra = input ("ingrese una palabra:")
    nueva = palabra.strip()
    if nueva.isalpha():
        
        print ("letras impares: ",nueva[1::2], end= "\n")
        print ("letras pares: ", nueva[::2], end = "\n")
    else:
        print ("fin, se ingresa solo una palabra con letras")
        break
        

    
        

    
