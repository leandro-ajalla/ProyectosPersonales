categoria = str(input("ingrese categoria (A/B/C): "))
horas = int(input("ingrese horas: "))
dias = int(input("ingrese dias: "))
promedio = horas / dias
if categoria == "A" and promedio >= 4:
    montovariable = horas * 100
    montofijo = 30 * 100
    montototal = montovariable + montofijo
    print ("monto fijo: $", montofijo)
    print ("monto variable: $", montovariable)
    print ("monto total: $", montototal)
elif promedio < 4:
    if categoria == "A":
        montofijo = 0
        montovariable = horas * 100
        montototal = montovariable + montofijo
        print ("monto fijo: $", montofijo, "- trabaja menos de 4hs promedio")
        print ("monto variable: $", montovariable)
        print ("monto total: $", montototal)
    else:
        if categoria == "B":
            montofijo = 0
            montovariable = horas * 80
            montototal = montovariable + montofijo
            print ("monto fijo: $", montofijo, "- trabaja menos de 4hs promedio")
            print ("monto variable: $", montovariable)
            print ("monto total: $", montototal)
        else:
            if categoria == "C":
                montofijo = 0
                montovariable = horas * 60
                montototal = montovariable + montofijo
                print ("monto fijo: $", montofijo, "- trabaja menos de 4hs promedio")
                print ("monto variable: $", montovariable)
                print ("monto total: $", montototal)

if categoria == "B" and promedio >= 4:
    montovariable = horas * 80
    montofijo = 24 * 100
    montototal = montovariable + montofijo
    print ("monto fijo: $", montofijo)
    print ("monto variable: $", montovariable)
    print ("monto total: $", montototal)

if categoria == "C" and promedio >= 4:
    montovariable = horas * 60
    montofijo = 20 * 50
    montototal = montovariable + montofijo
    print ("monto fijo: $", montofijo)
    print ("monto variable: $", montovariable)
    print ("monto total: $", montototal)

       

    

    
    
