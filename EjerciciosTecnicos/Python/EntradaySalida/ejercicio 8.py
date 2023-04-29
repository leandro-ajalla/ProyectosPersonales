"""Mostrar el % del total de ventas
de cada trimestre de un año."""


tri1 = int (input("Ingrese ventas del trimestre 1: "))
tri2 = int (input("Ingrese ventas del trimestre 2: "))
tri3 = int (input("Ingrese ventas del trimestre 3: "))
tri4 = int (input("Ingrese ventas del trimestre 4: "))


if tri1 < 0 or tri2 < 0 or tri3 < 0 or tri4 < 0:
    print(" Se ingreso ventas en negativo, no se puede continuar")
else:


    """Formula del total de ventas al año."""
    total = tri1 + tri2 + tri3 + tri4

    """formulas de porcentajes de cada trimestre."""
    porcentaje1 = round(tri1 * 100 / total, 1)
    porcentaje2 = round(tri2 * 100 / total, 1)
    porcentaje3 = round(tri3 * 100 / total, 1)
    porcentaje4 = round(tri4 * 100 / total, 1)

    print ("Ventas totales:", total)
    print ("T1: ",porcentaje1,"%")
    print ("T2: ",porcentaje2,"%")
    print ("T3: ",porcentaje3,"%")
    print ("T4: ",porcentaje4,"%")
            