import tkinter as tk
from json_sedes import *
from clase_sedes import *

ventana = tk.Tk()
ventana.title("sedes")
ventana.geometry("800x400")
ventana["bg"] = "#C3CDC0"

etiqueta = tk.Label(ventana, text="Configuración sedes",  font=("Helvetica", 20), bg="#8DC67E")
etiqueta.config(width=50, height=2)
etiqueta.pack()

label = tk.Label(ventana, text="Ingresar nombre de la sede")
label.place(x=40, y=80)

entry_nombre = tk.Entry(ventana, width=40)
entry_nombre.place(x=40, y=105)

label1 = tk.Label(ventana, text="provincia a la que pertenece")
label1.place(x=40, y=130)
options = ["Cartago","San Jose", "Puntarenas", "Guanacaste", "Limón","Heredia", "Alajuela"]
variable = tk.StringVar(ventana)
variable.set(options[0])
dropdown_menu = tk.OptionMenu(ventana, variable, *options)
dropdown_menu.place(x=40, y=155)

label2 = tk.Label(ventana, text="numero de contacto")
label2.place(x=40, y=190)

entry_contacto = tk.Entry(ventana, width=40)
entry_contacto.place(x=40, y=215)

checkbox_var = tk.BooleanVar()
checkbox_var.set(True)
checkbox = tk.Checkbutton(ventana, text="Activo", variable=checkbox_var)
checkbox.place(x=40, y=240)

label3 = tk.Label(ventana, text="sedes creadas")
label3.place(x=350, y=80)

cargar_y_mostrar_sedes_listbox(ventana)

def llamar_modificar_sedes():
    Modificar_sedes(entry_nombre, variable, entry_contacto, checkbox_var, options, ventana)

boton_anadir = tk.Button(ventana, text="Añadir sede", command=llamar_modificar_sedes)
#boton_anadir = tk.Button(ventana, text="Añadir sede")
boton_anadir.place(x=213, y=280)

boton_detalles = tk.Button(ventana, text="detalles")
#boton_detalles = tk.Button(ventana, text="detalles", command=mostrar_datos_seleccionados(listbox_sedes))
boton_detalles.place(x=350, y=320)

boton_detalles = tk.Button(ventana, text="cambiar estado")
boton_detalles.place(x=420, y=320)
ventana.mainloop()
