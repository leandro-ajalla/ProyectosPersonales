print ("Igrese los dias:")
dias = int(input())
print ("Ingrese las horas:")
horas = int(input())
print ("Ingrese los minutos:")
minutos = int(input())
print ("Ingrese los segundos:")
segundos = int(input())
diasseg = dias * 24 * 60 * 60
horasseg = horas * 60 * 60
minutosseg = minutos * 60
totalseg = diasseg + horasseg + minutosseg + segundos
print (dias, "dias",horas, "horas", minutos, "minutos", segundos, "segundos", "son" ,totalseg, "segundos")