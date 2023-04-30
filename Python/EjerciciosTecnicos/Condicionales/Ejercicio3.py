"""Hacer un conversor de temperaturas que funcione con °C, K, y °F ;
El usuario ingresa una temperatura y la unidad en la que se encuentra
y el programa informa la temperatura en las tres unidades.
f = Fahrenheit
c = centigrados
k = kelvin
"""
while True:
    temperatura = float(input("ingrese temperatura: "))
    unidad = str(input("esta en (K, F, o C) : "))

    """verifica en que unidad seleccionada esta la temperatura ingresada
    y realiza su respectiva formula conversor."""

    
   
    if unidad.upper() == "C":
        """formula de grados centigrados a faranheit y kelvin"""
        f = round(temperatura * 9/5 + 32, 2)
        k = round(temperatura + 273.15, 2)
        print (temperatura, "°C =",f, "°F =",k, "K")

    else:
        if unidad.upper() == "F":
            """formula de grados faranheit a centigrados y kelvin"""
            c = round((temperatura - 32) / 1.8,2)
            k = round(c + 273.15,2)
            print (temperatura, "°F =",c, "°C =",k, "K")

        else:
            if unidad.upper() == "K":
                """formula de grados kelvin a centigrados y faranheit"""
                c = round(temperatura - 273.15,2)
                f = round(c * 1.8 + 32, 2)
                print (temperatura, "K =",c, "°C =",f, "°F")
            else:
                if unidad != "K" or unidad != "F" or unidad != "C":
                    print ("seleccion de unidad no disponible")
                    break