import tkinter as tk

def calcular_importe():
    precio_unacuota = float(precio.get())
    cantidad_cuotas = int(cuotas.get())
    valor_cadacuota = precio_unacuota / cantidad_cuotas
    if cantidad_cuotas in range(0,3):
        total = precio_unacuota
        txtvalor.delete(0,"end")
        txtvalor.insert(0,valor_cadacuota)
        txtintereses.delete(0,"end")
        txtintereses.insert(0,"0")
        txttotal.delete(0,"end")
        txttotal.insert(0,total)
    if cantidad_cuotas in range(3,7):
        intereses = 10 * precio_unacuota / 100
        total = precio_unacuota + intereses
        interes_cuota = 10 * valor_cadacuota / 100
        valor_cadacuota += interes_cuota 
        txtvalor.delete(0,"end")
        txtvalor.insert(0,valor_cadacuota)
        txtintereses.delete(0,"end")
        txtintereses.insert(0,intereses)
        txttotal.delete(0,"end")
        txttotal.insert(0,total)
    if cantidad_cuotas in range(7,13):
        intereses = 20 * precio_unacuota / 100
        total = precio_unacuota + intereses
        interes_cuota = 20 * valor_cadacuota / 100
        valor_cadacuota += interes_cuota 
        txtvalor.delete(0,"end")
        txtvalor.insert(0,valor_cadacuota)
        txtintereses.delete(0,"end")
        txtintereses.insert(0,intereses)
        txttotal.delete(0,"end")
        txttotal.insert(0,total)
    if cantidad_cuotas in range(13,19):
        intereses = 30 * precio_unacuota / 100
        total = precio_unacuota + intereses
        interes_cuota = 30 * valor_cadacuota / 100
        valor_cadacuota += interes_cuota 
        txtvalor.delete(0,"end")
        txtvalor.insert(0,valor_cadacuota)
        txtintereses.delete(0,"end")
        txtintereses.insert(0,intereses)
        txttotal.delete(0,"end")
        txttotal.insert(0,total)
    

principal = tk.Tk()

lblprecio = tk.Label(principal, text = "Precio en una cuota: ")
lblcuotas = tk.Label(principal, text = "Cantidad de cuotas: ")
lblvalor = tk.Label(principal, text = "Valor de cada cuota: ")
lblintereses = tk.Label(principal, text = "Intereses: ")
lbltotal = tk.Label(principal, text = "Total a pagar: ")

precio = tk.StringVar() 
txtprecio = tk.Entry(principal, textvariable = precio)

cuotas = tk.StringVar() 
txtcuotas = tk.Entry(principal, textvariable = cuotas, width = 10)
 
txtvalor = tk.Entry(principal) 
txtintereses = tk.Entry(principal) 
txttotal = tk.Entry(principal)

btncalcular = tk.Button(principal,
                        text="Calcular",
                        command = calcular_importe)

lblprecio.grid(row = 0 , column = 0)
lblcuotas.grid(row = 1 , column = 0)
lblvalor.grid(row = 2 , column = 0)
lblintereses.grid(row = 3 , column = 0)
lbltotal.grid(row = 4 , column = 0)

txtprecio.grid (row = 0, column= 1)
txtcuotas.grid (row = 1, column= 1, sticky ="W")
txtvalor.grid (row = 2, column= 1)
txtintereses.grid (row = 3, column= 1)
txttotal.grid (row = 4, column= 1)

btncalcular.grid (row=5,
                 column=0,
                 columnspan=2)

principal.mainloop()