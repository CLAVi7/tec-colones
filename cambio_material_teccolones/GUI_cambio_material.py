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
options_centros = conseguir_centro()
variable_centros = tk.StringVar(ventana)
if options_centros:
    variable_centros.set(options_centros[0])
else:
    options_centros = ["No hay centros disponibles"]
    variable_centros.set(options_centros[0])

dropdown_menu_centros = tk.OptionMenu(ventana, variable_centros, *options_centros)
dropdown_menu_centros.place(x=40, y=105)

label1 = tk.Label(ventana, text="ingrese el caarnet del estudiante")
label1.place(x=40, y=140)
entry_carnet = tk.Entry(ventana, width=40)
entry_carnet.place(x=40, y=160)


label2 = tk.Label(ventana, text="seleccione el material traido")
label2.place(x=40, y=185)
options_materiales = conseguir_materiales()
print("Los materiales son:")
print(options_materiales)

variable_materiales = tk.StringVar(ventana)

formatted_options = [f"{nombre} - {unidad} - {valor}" for nombre, unidad, valor in options_materiales]
if formatted_options:
    variable_materiales.set(formatted_options[0])
else:
    formatted_options = ["No hay materiales disponibles"]
    variable_materiales.set(formatted_options[0])

dropdown_menu_materiales = tk.OptionMenu(ventana, variable_materiales, *formatted_options)
dropdown_menu_materiales.place(x=40, y=210)

label3 = tk.Label(ventana, text="ingrese la cantidad traida")
label3.place(x=40, y=245)
entry_cantidad = tk.Entry(ventana, width=40)
entry_cantidad.place(x=40, y=265)

boton_añadir = tk.Button(ventana, text="añadir material")
boton_añadir.place(x=40, y=290)




label3 = tk.Label(ventana, text="sedes creadas")
label3.place(x=350, y=80)
ventana.mainloop()