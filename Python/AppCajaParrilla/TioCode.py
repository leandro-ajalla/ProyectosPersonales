import tkinter as tk
from datetime import datetime
from functools import partial
import salir
import fecha
from PIL import ImageTk, Image

def btnClick(numeros):
    global operator
    operator = operator + str(numeros)
    text_Input.set(operator)
    
def btnBorrar():
    global operator
    text_Input.set("")
    
def btnIgual():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""
    
def Restablecer():
    PapasFritas.set("0")
    Pancho.set("0")
    Choripan.set("0")
    BurgerSimple.set("0")
    BurgerCompleta.set("0")
    Lomito.set("0")
    Bondiola.set("0")
    Agua.set("0")
    AguaSaborizada.set("0")
    Gaseosa.set("0")
    Cerveza.set("0")
    txtTotal.configure(state='normal')
    txtTotal.delete(0,"end")
    txtTotal.insert(0, "$0.0")
    txtTotal.configure(state='disabled')
    
    

def PrecioTotal ():
    d = {}
    with open("Precios.txt") as f:
        for line in f:
           (key, val) = line.split()
           d[(key)] = int(val)
    CantPapas = int(PapasFritas.get())
    CantPancho = int(Pancho.get())
    CantChori = int(Choripan.get())
    CantBs = int(BurgerSimple.get())
    CantBg = int(BurgerCompleta.get())
    CantLom = int(Lomito.get())
    CantBon = int(Bondiola.get())
    CantAgua = int(Agua.get())
    CantAsb = int(AguaSaborizada.get())
    CantGas = int(Gaseosa.get())
    CantCer = int(Cerveza.get())
    txtTotal.configure(state='normal')
    txtTotal.delete(0,"end")
    TotalPapas = d["PapasFritas"] * CantPapas
    TotalPancho = d["Pancho"] * CantPancho
    TotalChori = d["Choripan"] * CantChori
    TotalBs = d["HamburguesaSimple"] * CantBs
    TotalBg= d["HamburguesaCompleta"] * CantBg
    TotalLom = d["Lomito"] * CantLom
    TotalBon = d["Bondiola"] * CantBon
    TotalAgua = d["Agua"] * CantAgua
    TotalAsb = d["AguaSaborizada"] * CantAsb
    TotalGas = d["Gaseosa"] * CantGas
    TotalCer = d["Cerveza"] * CantCer
    TotalPedido = TotalPapas + TotalPancho + TotalChori + TotalBs + TotalBg + TotalLom + TotalBon + TotalAgua + TotalAsb + TotalGas + TotalCer
    txtTotal.insert(0,"$"+ str(TotalPedido))
    txtTotal.configure(state='disabled')
    f.close()
    
root = tk.Tk()
root.geometry("1400x700+0+0")
root.config(bg ="black")
root.title("Tio Code")
root.iconbitmap("parrilla.ico")

text_Input = tk.StringVar()
operator = "" 
imagen = Image.open("plato.png")
imagen = imagen.resize((100,100), Image.ANTIALIAS)
imagen_tk = ImageTk.PhotoImage(imagen)

Tops = tk.Frame(root, width = 1600, height = 50, bg = "black")
Tops.pack(side= tk.TOP)

f1 = tk.Frame(root, width= 800, height= 700, bg ="firebrick1",cursor="hand2")
f1.pack(side = tk.LEFT)

f2 = tk.Frame(root, width= 300, height= 700,cursor="hand2")
f2.pack(side = tk.RIGHT)

Fecha = datetime.now()

lblInfo = tk.Label(Tops, font=("arial", 50, "bold"), text = "Tio Code", fg = "firebrick1", bg="black", bd = 10, anchor = "w")
lblInfo.grid(row = 0, column = 0)

lblInfo = tk.Label(Tops, font=("arial", 20, "bold"), text = fecha.Fecha(Fecha), fg = "firebrick1", bg="black", bd = 10, anchor = "w")
lblInfo.grid(row = 1, column = 0)

lblFoto = tk.Label(Tops, image = imagen_tk)
lblFoto.grid(row= 0, column = 1)


textDisplay = tk.Entry(f2, font=("arial", 20, "bold"), textvariable= text_Input, bd = 30, insertwidth= 4, bg = "firebrick1", justify = "right")
textDisplay.grid(columnspan = 4)

btn7 = tk.Button(f2, padx = 16, pady = 16, bd=8, fg= "black", font=("arial", 20, "bold"), text= "7", bg="firebrick1", command = lambda: btnClick(7)).grid(row = 2, column=0)
btn8 = tk.Button(f2, padx = 16, pady = 16, bd=8, fg= "black", font=("arial", 20, "bold"), text= "8", bg="firebrick1", command = lambda: btnClick(8)).grid(row = 2, column=1)
btn9 = tk.Button(f2, padx = 16, pady = 16, bd=8, fg= "black", font=("arial", 20, "bold"), text= "9", bg="firebrick1", command = lambda: btnClick(9)).grid(row = 2, column=2)
Suma = tk.Button(f2, padx = 16, pady = 16, bd=8, fg= "black", font=("arial", 20, "bold"), text= "+", bg="firebrick1", command = lambda: btnClick("+")).grid(row = 2, column=3)

btn4 = tk.Button(f2, padx = 16, pady = 16, bd=8, fg= "black", font=("arial", 20, "bold"), text= "4", bg="firebrick1", command = lambda: btnClick(4)).grid(row = 3, column=0)
btn5 = tk.Button(f2, padx = 16, pady = 16, bd=8, fg= "black", font=("arial", 20, "bold"), text= "5", bg="firebrick1", command = lambda: btnClick(5)).grid(row = 3, column=1)
btn6 = tk.Button(f2, padx = 16, pady = 16, bd=8, fg= "black", font=("arial", 20, "bold"), text= "6", bg="firebrick1", command = lambda: btnClick(6)).grid(row = 3, column=2)
Resta = tk.Button(f2, padx = 16, pady = 16, bd=8, fg= "black", font=("arial", 20, "bold"), text= "-", bg="firebrick1", command = lambda: btnClick("-")).grid(row = 3, column=3)

btn1 = tk.Button(f2, padx = 16, pady = 16, bd=8, fg= "black", font=("arial", 20, "bold"), text= "1", bg="firebrick1", command = lambda: btnClick(1)).grid(row = 4, column=0)
btn2 = tk.Button(f2, padx = 16, pady = 16, bd=8, fg= "black", font=("arial", 20, "bold"), text= "2", bg="firebrick1", command = lambda: btnClick(2)).grid(row = 4, column=1)
btn3 = tk.Button(f2, padx = 16, pady = 16, bd=8, fg= "black", font=("arial", 20, "bold"), text= "3", bg="firebrick1", command = lambda: btnClick(3)).grid(row = 4, column=2)
Multiplicacion = tk.Button(f2, padx = 16, pady = 16, bd=8, fg= "black", font=("arial", 20, "bold"), text= "*", bg="firebrick1", command = lambda: btnClick("*")).grid(row = 4, column=3)

btn0 = tk.Button(f2, padx = 16, pady = 16, bd=8, fg= "black", font=("arial", 20, "bold"), text= "0", bg="firebrick1", command = lambda: btnClick(0)).grid(row = 5, column=0)
btnClear = tk.Button(f2, padx = 16, pady = 16, bd=8, fg= "black", font=("arial", 20, "bold"), text= "C", bg="firebrick1", command = btnBorrar).grid(row = 5, column=1)
btnIgual = tk.Button(f2, padx = 16, pady = 16, bd=8, fg= "black", font=("arial", 20, "bold"), text= "=", bg="firebrick1", command = btnIgual).grid(row = 5, column=2)
Divicion = tk.Button(f2, padx = 16, pady = 16, bd=8, fg= "black", font=("arial", 20, "bold"), text= "/", bg="firebrick1", command = lambda: btnClick("/")).grid(row = 5, column=3)

PapasFritas = tk.StringVar(value = 0)
Pancho = tk.StringVar(value = 0)
Choripan = tk.StringVar(value = 0)
BurgerSimple = tk.StringVar(value = 0)
BurgerCompleta = tk.StringVar(value = 0)
Lomito = tk.StringVar(value = 0)
Bondiola = tk.StringVar(value = 0)
Agua = tk.StringVar(value = 0)
AguaSaborizada = tk.StringVar(value = 0)
Gaseosa = tk.StringVar(value = 0)
Cerveza = tk.StringVar(value = 0)

lblPapasFritas = tk.Label(f1, font=("arial", 16, "bold"), text= "Papas Fritas", bg ="firebrick1",fg="black", anchor = "w")
lblPapasFritas.grid(row= 0, column= 0)
sbxPapasFritas = tk.Spinbox (f1, font=("arial", 16, "bold"), from_ = 0, to = 20, textvariable = PapasFritas, state ="readonly", wrap=True, bd= 10, insertwidth= 4, justify = "right")
sbxPapasFritas.grid(row=0, column=1)

lblPancho = tk.Label(f1, font=("arial", 16, "bold"), text= "Pancho", bg ="firebrick1",fg="black", anchor = "w")
lblPancho.grid(row= 1, column= 0)
sbxPancho = tk.Spinbox (f1, font=("arial", 16, "bold"),from_ = 0, to = 20, textvariable = Pancho, state ="readonly", wrap=True, bd= 10, insertwidth= 4, justify = "right")
sbxPancho.grid(row=1, column=1)

lblChoripan = tk.Label(f1, font=("arial", 16, "bold"), text= "Choripan", bg ="firebrick1",fg="black", anchor = "w")
lblChoripan.grid(row= 2, column= 0)
sbxChoripan = tk.Spinbox (f1, font=("arial", 16, "bold"),from_ = 0, to = 20, textvariable = Choripan, state ="readonly", wrap=True, bd= 10, insertwidth= 4, justify = "right")
sbxChoripan.grid(row=2, column=1)

lblBurgerSimple = tk.Label(f1, font=("arial", 16, "bold"), text= "Hamburgesa Simple", bg ="firebrick1",fg="black", anchor = "w")
lblBurgerSimple.grid(row= 3, column= 0)
sbxBurgerSimple = tk.Spinbox (f1, font=("arial", 16, "bold"), from_ = 0, to = 20, textvariable = BurgerSimple, state ="readonly", wrap=True, bd= 10, insertwidth= 4, justify = "right")
sbxBurgerSimple.grid(row=3, column=1)

lblBurgerCompleta = tk.Label(f1, font=("arial", 16, "bold"), text= "Hamburgesa Completa", bg ="firebrick1",fg="black", anchor = "w")
lblBurgerCompleta.grid(row= 4, column= 0)
sbxBurgerCompleta = tk.Spinbox (f1, font=("arial", 16, "bold"), from_ = 0, to = 20, textvariable = BurgerCompleta, state ="readonly", wrap=True, bd= 10, insertwidth= 4, justify = "right")
sbxBurgerCompleta.grid(row=4, column=1)

lblLomito = tk.Label(f1, font=("arial", 16, "bold"), text= "Lomito", bg ="firebrick1",fg="black", anchor = "w")
lblLomito.grid(row= 5, column= 0)
sbxLomito = tk.Spinbox (f1, font=("arial", 16, "bold"), from_ = 0, to = 20, textvariable = Lomito, state ="readonly", wrap=True, bd= 10, insertwidth= 4, justify = "right")
sbxLomito.grid(row=5, column=1)

lblBondiola = tk.Label(f1, font=("arial", 16, "bold"), text= "Bondiola", bg ="firebrick1",fg="black", anchor = "w")
lblBondiola.grid(row= 0, column= 2)
sbxBondiola = tk.Spinbox (f1, font=("arial", 16, "bold"), from_ = 0, to = 20, textvariable = Bondiola, state ="readonly", wrap=True, bd= 10, insertwidth= 4, justify = "right")
sbxBondiola.grid(row=0, column=3)

lblAgua = tk.Label(f1, font=("arial", 16, "bold"), text= "Agua", bg ="firebrick1",fg="black", anchor = "w")
lblAgua.grid(row= 1, column= 2)
sbxAgua = tk.Spinbox (f1, font=("arial", 16, "bold"), from_ = 0, to = 20, textvariable = Agua, state ="readonly", wrap=True, bd= 10, insertwidth= 4, justify = "right")
sbxAgua.grid(row=1, column=3)

lblAguaSaborizada = tk.Label(f1, font=("arial", 16, "bold"), text= "Agua Saborizada", bg ="firebrick1",fg="black", anchor = "w")
lblAguaSaborizada.grid(row= 2, column= 2)
sbxAguaSaborizada = tk.Spinbox (f1, font=("arial", 16, "bold"), from_ = 0, to = 20, textvariable = AguaSaborizada, state ="readonly", wrap=True, bd= 10, insertwidth= 4, justify = "right")
sbxAguaSaborizada.grid(row=2, column=3)

lblGaseosa = tk.Label(f1, font=("arial", 16, "bold"), text= "Gaseosa", bg ="firebrick1",fg="black", anchor = "w")
lblGaseosa.grid(row= 3, column= 2)
sbxGaseosa = tk.Spinbox (f1, font=("arial", 16, "bold"), from_ = 0, to = 20, textvariable = Gaseosa, state ="readonly", wrap=True, bd= 10, insertwidth= 4, justify = "right")
sbxGaseosa.grid(row=3, column=3)

lblCerveza = tk.Label(f1, font=("arial", 16, "bold"), text= "Cerveza", bg ="firebrick1",fg="black", anchor = "w")
lblCerveza.grid(row= 4, column= 2)
sbxCerveza = tk.Spinbox (f1, font=("arial", 16, "bold"), from_ = 0, to = 20, textvariable = Cerveza, state ="readonly", wrap=True, bd= 10, insertwidth= 4, justify = "right")
sbxCerveza.grid(row=4, column=3)

lblTotal = tk.Label(f1, font=("arial", 16, "bold"), text= "Costo Total", bg ="firebrick1",fg="black", anchor = "w")
lblTotal.grid(row= 5, column= 2)
txtTotal = tk.Entry(f1, font=("arial", 16, "bold"),disabledforeground = "red", bd= 10, insertwidth= 4, bg= "teal", justify = "right")
txtTotal.grid(row=5, column=3)
txtTotal.configure(state = "normal")
txtTotal.insert(0, "$0.0")
txtTotal.configure(state='disabled')

btnTotal = tk.Button(f1, padx = 16, pady = 8, bd= 15, fg = "black", font=("arial", 16, "bold"), width = 10, text = "Total", bg ="firebrick1", command= PrecioTotal).grid(row = 6 , column = 1)
btnRestablecer = tk.Button(f1, padx = 16, pady = 8, bd= 15, fg = "black", font=("arial", 16, "bold"), width = 10, text = "Restablecer", bg ="firebrick1",command = Restablecer).grid(row = 6, column = 2)
btnSalir = tk.Button(f1, padx = 16, pady = 8, bd= 15, fg = "black", font=("arial", 16, "bold"), width = 10, text = "Salir", bg ="firebrick1", command = partial(salir.Salir,root)).grid(row = 6, column = 3)

root.mainloop()