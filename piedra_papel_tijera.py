from tkinter import *
import os
from tkinter import messagebox
import random 


# Base
ventana_principal = Tk()
ventana_principal.title("Piedra Papel Tijera")        
ventana_principal.geometry("800x500")      
ventana_principal.resizable(0, 0)           
ventana_principal.config(bg="Black") 

# Variables 
AI = 0
Jugador = 0
# funciones
def Papel():
    AI = random.randint(1, 3)
    Jugador = 1
    if AI < Jugador:
        ganaste = "ganastes "
        t_resultado.insert(INSERT, ganaste)
        print("Ganastes")
    else:
        print("Prediste")
        t_resultado.insert(INSERT, "Perdiste ")
        t_resultado.insert(INSERT, "")
    if AI == Jugador:
     t_resultado.insert(INSERT, "Empate ")
    
    pass


    
#
def Piedra():
    AI = random.randint(1, 3)
    Jugador = 2
    if AI < Jugador:
        ganaste = "Ganaste "
        t_resultado.insert(INSERT, ganaste)
        print("Ganaste")
    else:
        print("Perdiste")
        t_resultado.insert(INSERT, "Perdiste ")
        t_resultado.insert(INSERT, "")
    if AI == Jugador:
     t_resultado.insert(INSERT, "Empate ")
    pass
def Tijera():
    AI = random.randint(1, 3)
    Jugador = 3
    if AI < Jugador:
        ganaste = "ganastes "
        t_resultado.insert(INSERT, ganaste)
        print("Ganastes")
    else:
        print("Prediste")
        t_resultado.insert(INSERT, "Perdiste ")
        t_resultado.insert(INSERT, "")
    if AI == Jugador:
     t_resultado.insert(INSERT, "Empate ")
    pass

print(Jugador)


# Primer
Frame_1 = Frame(ventana_principal)          
Frame_1.config(bg="blue", width=780, height=240)
Frame_1.place(x=10, y=10) 


Frame_2 = Frame(ventana_principal)        
Frame_2.config(bg="yellow", width=780, height=120) 
Frame_2.place(x=10, y=260) 

Frame_3 = Frame(ventana_principal)
Frame_3.config(bg="ivory3", width=780, height=100)  
Frame_3.place(x=10, y=390) 

# Logo
logo = PhotoImage(file = "img/logo.png")
label_logo = Label(Frame_1, image=logo)
label_logo.place(x=180, y=10)


titulo2 = Label(Frame_2, text = "Seleccione: ")
titulo2.config(bg="ivory2", fg="blue", font=("Arial", 16))
titulo2.place(x=10, y= 10) 


# Botones

# Papel
img_bt_papel= PhotoImage(file = "img/bt_papel.png")
bt_papel = Button(Frame_2, image = img_bt_papel, width = 105, height = 105, command=Papel)
bt_papel.place(x=180, y=7)

# Piedra 
img_bt_piedra = PhotoImage(file = "img/bt_piedra.png")
bt_piedra = Button(Frame_2, image = img_bt_piedra, width = 105, height = 105, command=Piedra)
bt_piedra.place(x=340, y=7)

# Tijera 
img_bt_tijera = PhotoImage(file = "img/bt_tijera.png")
bt_tijera = Button(Frame_2, image = img_bt_tijera, width = 105, height = 105, command=Piedra)
bt_tijera.place(x=500, y=7)


# Area resultado
t_resultado = Text(Frame_3, width =50, height =3)
t_resultado.config(bg="yellow", fg="black", font= ("Courier", 20))
t_resultado.pack()






# Fin
ventana_principal.mainloop()