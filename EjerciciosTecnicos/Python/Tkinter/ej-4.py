import tkinter as tk

def nombre_saludo():
    nombre_completo = nombre.get()
    saludo.set("Hola "+ nombre_completo +"!")

saluda = tk.Tk()
saluda.title("saluda")

lblnombre = tk.Label(saluda, text = "Ingresa tu nombre:")

saludo = tk.StringVar()
lblsaludo = tk.Label(saluda, textvariable = saludo,
                     font ="Arial 20 bold")

nombre = tk.StringVar() 
txtnombre = tk.Entry(saluda, textvariable = nombre, width = 40)

btnsaludar = tk.Button(saluda,
                        text="Saludar",
                        command = nombre_saludo)

lblnombre.grid(row = 0 , column = 0, sticky="W")
txtnombre.grid (row = 1, column= 0,
                columnspan = 2,
                sticky = "WE")
btnsaludar.grid (row=2,
                 column=0,sticky ="WE",
                 pady=(5,15), padx=(10,10))

lblsaludo.grid(row = 3 , column = 0,
               sticky="W", pady= 15)

saluda.mainloop()