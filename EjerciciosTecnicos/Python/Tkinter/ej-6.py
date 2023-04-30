import tkinter as tk
from tkinter import messagebox

def calcula_porcion():
    peso_mascota = float(peso.get())
    porcion_perro = 7.56
    if es_gato.get() == 1:
        if peso_mascota >= 2:
            porcion_gato = 15
            porcion_gato = porcion_gato * peso_mascota
            messagebox.showinfo("Resultado", "La porcion diaria es de " + str(porcion_gato)+"g")
        else:
            porcion_gato = 30
            porcion_gato = porcion_gato * peso_mascota
            messagebox.showinfo("Resultado", "La porcion diaria es de " + str(porcion_gato)+"g")
    if es_perro.get() == 1:
        porcion_perro = porcion_perro * peso_mascota + 110
        messagebox.showinfo("Resultado", "La porcion diaria es de " + str(porcion_perro)+"g")
        

principal = tk.Tk()

lblpeso = tk.Label(principal, text = "Peso (kg):")

peso = tk.StringVar() 
txtpeso = tk.Entry(principal, textvariable = peso)

es_gato = tk.IntVar()
chkgato = tk.Checkbutton(principal,
                               text = "Gato",
                               variable = es_gato)
es_perro = tk.IntVar()
chkperro = tk.Checkbutton(principal,
                            text ="Perro",
                            variable = es_perro)

btncalcular = tk.Button(principal,
                        text="Calcular",
                        command =calcula_porcion)

lblpeso.grid(row = 0 , column = 0)
txtpeso.grid(row = 0 , column = 1)
chkgato.grid(row=1, column=1, sticky ="W")
chkperro.grid(row= 2, column=1, sticky ="W")
btncalcular.grid (row=3,
                 column=0,
                 columnspan=2)

principal.mainloop()

