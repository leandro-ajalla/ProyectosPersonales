print ("Ingrese botellas:")
vidrio = int(input("vidrio: "))
plastico = int(input("plastico: "))
devolvidrio = vidrio * 1.50
devolplastico = plastico * 2.00
totalbotella = plastico + vidrio
totalprecio = devolvidrio + devolplastico
print ("Devolucion de botellas")
print ("======================")
print ("plastico", plastico, devolplastico, sep ="   ")
print ("vidrio ", vidrio, devolvidrio, sep ="    ")
print ("----------------------")
print ("total", totalbotella, totalprecio, sep="    ")