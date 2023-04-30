# cuantas operaciones realiza carmen

f = open("inmuebles.csv", "r")
q= 0

for linea in f:
    if "Carmen" in linea:
        q += 1




print(q)
f.close()