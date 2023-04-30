import tkinter as tk
from tkinter import messagebox

def calcular_importe():
    dias_total = int(dias.get())
    km_total = float(km.get())
    precio = 500
    a_pagar = precio * dias_total + 45 * km_total
    messagebox.showinfo("Resultado", "A pagar: $ " + str(a_pagar))
   

principal = tk.Tk()

lbldias = tk.Label(principal, text = "dias")
lblkm = tk.Label(principal, text = "km recorridos")

dias = tk.StringVar() 
txtdias = tk.Entry(principal, textvariable = dias)

km = tk.StringVar() 
txtkm = tk.Entry(principal, textvariable = km)


btncalcular = tk.Button(principal,
                        text="Calcular",
                        command = calcular_importe)

lbldias.grid(row = 0 , column = 0)
lblkm.grid(row = 1 , column = 0)
txtdias.grid (row = 0, column= 1)
txtkm.grid (row = 1, column= 1)
btncalcular.grid (row=2,
                 column=0,
                 columnspan=2)

principal.mainloop()

