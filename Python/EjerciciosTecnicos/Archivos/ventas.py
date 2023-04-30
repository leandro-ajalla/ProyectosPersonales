# $$$ ventas de carmen


f = open("inmuebles.csv", "r")
g = open("carmen2.csv", "w")

q= 0
guita = 0

for linea in f:
    linea_tmp = linea.split(";")
    if linea_tmp[-1] == '"Carmen"\n':
        if linea_tmp[3] == '"Venta"':
            q += 1
            guita += float(linea_tmp[6])

            g.write(linea)

print (q, guita)

g.close()
f.close()

import _csv
listaventa = []
liestavend = []
listafinal=[]

with open("C:/Users/Nacho y Vane/Desktop/final/ventas.csv") as ventas:
    entradaventa = _csv.reader(ventas, delimiter= ";")
    listaventa = list(entradaventa)

with open("C:/Users/Nacho y Vane/Desktop/final/vendedores.csv") as vendedores:
    entradavend = _csv.reader(vendedores, delimiter= ";")
    listavend = list(entradavend)