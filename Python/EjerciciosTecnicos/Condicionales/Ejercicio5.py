mes = str(input("ingrese el mes: "))
año = int(input("ingrese el año: "))
if mes == "enero" or mes == "marzo" or mes == "julio" or mes == "agosto" or mes == "octubre" or mes == "diciembre":
    print ("31 dias")
elif mes == "febrero":
    if año % 4 == 0:
        if año % 100 != 0 or año % 400 == 0:
            print ("29 dias")
        else:
            print ("28 dias")
    else:
        print ("28 dias")
else:
    print ("30dias")
    