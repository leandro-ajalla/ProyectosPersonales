from tkinter import messagebox


def Salir(root):
    valor = messagebox.askquestion("Salir","Desea salir del programa")
    if valor == "yes":
        root.destroy()
        
    

    
def PrecioTotal():
    CantFritas = float(PapasFritas.get())
    CantPancho = float(Pancho.get())
    CantChoripan = float(Choripan.get())
    CantBurgerSim = float(BurgerSimple.get())
    CantBurgerCom = float(BurgerCompleta.get())
    CantLomito = float(Lomito.get())
    CantBondiola = float(Bondiola.get()) 
    CantAgua = float(Agua.get())
    CantAguaSab = float(AguaSaborizada.get())
    CantGaseosa = float(Gaseosa.get())
    CantCerveza = float(Cerveza.get())
    txtTotal.configure(state='normal')
    txtTotal.delete(0,"end")
    
    ListaPrecio= []
    PreciosComida = open("Precios.txt", "r")
    for linea in PreciosComida:
        ListaPrecio.append(linea)    
    
    Total = CantFritas + CantPancho + CantChoripan + CantBurgerSim + CantBurgerCom + CantLomito + CantBondiola + CantAgua + CantAguaSab + CantGaseosa + CantCerveza
    txtTotal.insert(0,"$"+ str(Total))
    txtTotal.configure(state='disabled')
    
    PreciosComida.close()
    