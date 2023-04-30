import tkinter as tk
from tkinter import messagebox

def calcula_importe():
    peso_paquete = float(peso.get())
    precio= 250
    if peso_paquete > 10:
        precio= precio+(peso_paquete-10)*25    
    
    if es_particular.get() ==1:
        precio = precio * 0.85
    
    if es_urgente.get() ==1:
        precio = precio * 1.25
    
    messagebox.showinfo("Resultado", "A cobrar $ " + str(precio))


mw = tk.Tk()

lblPeso = tk.Label(mw, text = "Peso (Kg)")

peso = tk.StringVar() 
txtPeso = tk.Entry(mw, textvariable = peso)

es_particular = tk.IntVar()
chkParticular = tk.Checkbutton(mw,
                               text = "Particular",
                               variable = es_particular)
es_urgente = tk.IntVar()
chkUrgente = tk.Checkbutton(mw,
                            text ="Urgente",
                            variable = es_urgente)

btnCalcular = tk.Button(mw,
                        text="Calcular importe",
                        command =calcula_importe,
                        bg="green", fg="white",
                        font ="Arial 12 bold")


lblPeso.grid(row= 0, column= 0, padx =(10,5), pady=(10,5))
txtPeso.grid(row=0, column=1, padx=(0,10))
chkParticular.grid(row=1, column=1, sticky ="W")
chkUrgente.grid(row= 2, column=1, sticky ="W")
btnCalcular.grid(row=3,
                 column=0,
                 columnspan=2,
                 pady=(5,15), padx=(10,10),
                 sticky="WE")

mw.mainloop()