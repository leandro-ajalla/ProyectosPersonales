# $$$ ventas de carmen
# agregas los alquilers de carmen

f = open("inmuebles.csv", "r")
g = open("carmen.csv", "a")

q= 0
guita = 0

for linea in f:
    linea_tmp = linea.split(";")
    if linea_tmp[-1] == '"Carmen"\n':
        if linea_tmp[3] == '"Alquiler"':
            q += 1
            guita += float(linea_tmp[6])

            g.write(linea)

print (q, guita)

g.close()
f.close()