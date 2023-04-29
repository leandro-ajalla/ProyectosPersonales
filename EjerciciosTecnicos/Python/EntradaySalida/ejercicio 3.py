print ("ingrese los segundos:")
segundos = int(input()) 
minutos = segundos // 60
segundosresto = segundos % 60
horas = minutos // 60
minutosresto = minutos % 60
dias = horas // 24
horasresto = horas % 24
print (segundos,"segundos son", dias, "dias", horasresto, "horas", minutosresto, "minutos", segundosresto,"segundos")
    