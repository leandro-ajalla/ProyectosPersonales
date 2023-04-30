def operaciones(f, g, vendedor, tipo):
    q = 0
    guita = 0

    for linea in f:
        linea_tmp = linea.split(";")
        if linea_tmp[-1] == '"{}"\n'.format(vendedor):
            if linea_tmp[3] == '"{}"'.format(tipo):
                q += 1
                guita += float(linea_tmp[6])

                g.write(linea)
    
    print(tipo, q, guita)

f = open("inmuebles.csv", "r")
g = open("carmen.csv", "w")

operaciones(f, g, 'Carmen', 'Alquiler')

g.close()
g = open("carmen.csv", "a")
f.seek(0)

operaciones(f, g, 'Carmen', 'Venta')

g.close()
f.close()



    
