import tkinter as tk
from tkinter import *
from tkinter import messagebox
from json_centro_acopio import *


ventana = Tk()
ventana.title("Centros de Acopio")
ventana.geometry("800x400")
ventana["bg"] = "#C3CDC0"

etiqueta = tk.Label(ventana, text="Configuración Centros de Acopio",  font=("Helvetica", 20), bg="#8DC67E")
etiqueta.config(width=50, height=2)
etiqueta.pack()

label = tk.Label(ventana, text="Ingresar Centro de Acopio")
label.place(x=40, y=80)

entry_nombre = tk.Entry(ventana, width=40)
entry_nombre.place(x=40, y=105)

label = tk.Label(ventana, text="Ubicación del Centro de Acopio")
label.place(x=40, y=135)

entry_ubicacion = tk.Entry(ventana, width=40)
entry_ubicacion.place(x=40, y=160)

label1 = tk.Label(ventana, text="Sede a la que Pertenece el Centro de Acopio")
label1.place(x=40, y=190)

options = conseguir_sedes()
print("las sedes son")
print(options)
variable = tk.StringVar(ventana)
variable.set(options[0])
dropdown_menu = tk.OptionMenu(ventana, variable, *options)
dropdown_menu.place(x=40, y=215)

label = tk.Label(ventana, text="Número de Contacto")
label.place(x=40, y=255)

entry_contacto = tk.Entry(ventana, width=40)
entry_contacto.place(x=40, y=280)

label = tk.Label(ventana, text="ID del centro de acopio")
label.place(x=40, y=310)

entry_id = tk.Entry(ventana, width=40)
entry_id.place(x=40, y=280+55)

label4 = tk.Label(ventana, text="Centros de Acopio Creados")
label4.place(x=350, y=80)

listbox_centros = None


def llamar_cargar_listbox():
    """
    Carga y muestra los centros de acopio en un Listbox. Utiliza la variable global 'listbox_centros' para mantener y actualizar el Listbox.
    """
    global listbox_centros
    listbox_centros = cargar_y_mostrar_centros_listbox(ventana, listbox_centros)


llamar_cargar_listbox()


def llamar_modificar_centros():
    """
    Llama a la función 'Modificar_centros' para actualizar o añadir centros de acopio en la lista, utilizando variables globales y actualizando el 'listbox_centros'.
    """
    global listbox_centros
    listbox_centros = Modificar_centros(entry_nombre, entry_ubicacion, variable, entry_contacto, checkbox_var, ventana, listbox_centros, options, entry_id)


def llamar_detalles():
    """
    Muestra los detalles del centro de acopio seleccionado desde 'listbox_centros'.
    """
    mostrar_datos_seleccionados(listbox_centros)


def llamar_cambiar_estado():
    """
    Cambia el estado del centro de acopio seleccionado en el Listbox 'listbox_centros', y actualiza el Listbox para reflejar los cambios.
    """
    cambiar_estdo_listbox(ventana, listbox_centros)


boton_anadir = tk.Button(ventana, text="Añadir Centro de Acopio", command=llamar_modificar_centros)
boton_anadir.place(x=143, y=365)

boton_mostrar = tk.Button(ventana, text="Detalles", command=llamar_detalles)
boton_mostrar.place(x=350, y=310)

cambiar_estado_boton = tk.Button(ventana, text="Cambiar estado", command=llamar_cambiar_estado)
cambiar_estado_boton.place(x=415, y=310)

checkbox_var = tk.BooleanVar()
checkbox_var.set(True)
checkbox = tk.Checkbutton(ventana, text="Activo", variable=checkbox_var)
checkbox.place(x=40, y=365)

ventana.mainloop()
