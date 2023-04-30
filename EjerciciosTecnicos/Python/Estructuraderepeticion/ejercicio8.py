total = int(input("poliza anual: "))

if total != 0:
    while total != 0:
        meses = int(input("meses adeudados: "))
        debe = (meses * total) / 12
        print("debe:", debe)
        total = int(input("poliza anual: "))

print("--fin--")
    
    
    


