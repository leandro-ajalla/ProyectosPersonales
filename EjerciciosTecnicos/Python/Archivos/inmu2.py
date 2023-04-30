# cuantas operaciones realiza carmen

f = open("inmuebles.csv", "r")

q= 0
for linea in f:
    if linea.split(";")[-1] == '"Carmen"\n':
        q += 1
    
print (q)

f.close()