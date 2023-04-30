import tkinter as tk

def nombre_primero():
    nombre_completo = str (nombre.get())
    apellido_completo= str (apellido.get()) 
    txtnomb_ape.configure(state='normal')
    txtnomb_ape.delete(0,"end")
    txtnomb_ape.insert(0,nombre_completo + ", " + apellido_completo )
    txtnomb_ape.configure(state='disabled')
    txtnombre.focus_set()

def apellido_primero():
    nombre_completo = str (nombre.get())
    apellido_completo= str (apellido.get()) 
    txtnomb_ape.configure(state='normal')
    txtnomb_ape.delete(0,"end")
    txtnomb_ape.insert(0, apellido_completo + ", " + nombre_completo )
    txtnomb_ape.configure(state='disabled')
    txtnombre.focus_set()

principal = tk.Tk()

lblnombre = tk.Label(principal, text = "Nombre:")
lblapellido = tk.Label(principal, text = "Apellido:")

nombre = tk.StringVar() 
txtnombre = tk.Entry(principal, textvariable = nombre)

apellido = tk.StringVar() 
txtapellido = tk.Entry(principal, textvariable = apellido)

txtnomb_ape = tk.Entry(principal, state = "disabled", disabledforeground = "red")



btnnombre_primero = tk.Button(principal,
                        text="Nombre primero",
                        command = nombre_primero)
btnapellido_primero = tk.Button(principal,
                        text="Apellido primero",
                        command = apellido_primero)

lblnombre.grid(row = 0 , column = 0, sticky="W")
lblapellido.grid(row = 2 , column = 0, sticky ="W")

txtnombre.grid (row = 1, column= 0,
                columnspan = 2,
                sticky = "WE")
txtapellido.grid (row = 3, column= 0,
                  columnspan = 2,
                  sticky = "WE")
txtnomb_ape.grid (row = 5, column= 0,
                  columnspan = 2,
                  sticky = "WE",pady= 10)

btnnombre_primero.grid (row=4,
                 column=0,sticky ="WE")

btnapellido_primero.grid (row=4,
                 column=1,sticky ="WE")

principal.mainloop()