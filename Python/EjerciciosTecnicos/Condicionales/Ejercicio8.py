plan = str(input("ingrese el plan A/B: "))
minutos = int(input("ingrese los minuto: "))
sms = int (input("ingrese los sms: "))
if plan == "A":
    if minutos > 1000 and sms > 200:
        montototal = 500 + 15 * (minutos // 1000) + 7.5 * ( minutos // 200)
        print ("total a abonar: $", montototal)
        
    