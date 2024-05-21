import tkinter as tk
from funcione_GUI_Cambio import *

ventana = tk.Tk()
ventana.title("cambio de material")
ventana.geometry("800x400")
ventana["bg"] = "#C3CDC0"

etiqueta = tk.Label(ventana, text="Cambio de material a tec-colones",  font=("Helvetica", 20), bg="#8DC67E")
etiqueta.config(width=50, height=2)
etiqueta.pack()

label = tk.Label(ventana, text="seleccione el centro al que pertenece")
label.place(x=40, y=80)
options = conseguir_centro()
variable = tk.StringVar(ventana)
# Verifica que options no esté vacío
if options:
    variable.set(options[0])
else:
    options = ["No hay centros disponibles"]
    variable.set(options[0])
dropdown_menu = tk.OptionMenu(ventana, variable, *options)
dropdown_menu.place(x=40, y=105)

label1 = tk.Label(ventana, text="ingrese el caarnet del estudiante")
label1.place(x=40, y=140)
entry_carnet = tk.Entry(ventana, width=40)
entry_carnet.place(x=40, y=160)


label2 = tk.Label(ventana, text="seleccione el material traido")
label2.place(x=40, y=185)
options = ["Cartago","San Jose", "Puntarenas", "Guanacaste", "Limón","Heredia", "Alajuela"]
variable = tk.StringVar(ventana)
variable.set(options[0])
dropdown_menu = tk.OptionMenu(ventana, variable, *options)
dropdown_menu.place(x=40, y=210)

label3 = tk.Label(ventana, text="ingrese la cantidad traida")
label3.place(x=40, y=245)
entry_cantidad = tk.Entry(ventana, width=40)
entry_cantidad.place(x=40, y=265)

boton_añadir = tk.Button(ventana, text="añadir material")
boton_añadir.place(x=40, y=290)




label3 = tk.Label(ventana, text="sedes creadas")
label3.place(x=350, y=80)
ventana.mainloop()