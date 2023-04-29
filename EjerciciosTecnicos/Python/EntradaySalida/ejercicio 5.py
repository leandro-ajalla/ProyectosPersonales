"""Convertir una distancia en Km a
metros, pulgadas, yardas y millas."""

km = int(input("Ingresar una distancia (km): ")) 

"""formula para obtener km
a metros, pulgadas, yardas y millas"""

metros = km * 1000
pulgadas = round (km * 39370.1, 3)
yardas = round(km * 1093.61, 3)
millas = round(km * 0.621371, 3)

print (km, "km son", metros, "metros")
print (km, "km son", pulgadas, "pulgadas")
print (km, "km son", yardas, "yardas")
print (km, "km son",  millas, "millas")