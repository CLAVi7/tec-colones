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

listbox_sedes = None


def llamar_cargar_listbox():
    """
    Carga y muestra las sedes en un Listbox. Utiliza la variable global 'listbox_sedes' para mantener y actualizar el Listbox.
    """
    global listbox_sedes
    listbox_sedes = cargar_y_mostrar_sedes_listbox(ventana, listbox_sedes)


llamar_cargar_listbox()


def llamar_modificar_sedes():
    """
    Llama a la función 'Modificar_sedes' para actualizar o añadir sedes en la lista, utilizando variables globales y actualizando el 'listbox_sedes'.
    """
    global listbox_sedes
    listbox_sedes = Modificar_sedes(entry_nombre, variable, entry_contacto, checkbox_var, options, ventana, listbox_sedes)


def llamar_detalles():
    """
    Muestra los detalles de la sede seleccionada desde 'listbox_sedes'.
    """
    mostrar_datos_seleccionados(listbox_sedes)


def llamar_cambiar_estado():
    """
    Cambia el estado de la sede seleccionada en el Listbox 'listbox_sedes', y actualiza el Listbox para reflejar los cambios.
    """
    cambiar_estdo_listbox(ventana, listbox_sedes)
    variable.set(options[0])
    entry_ubicacion.delete(0, tk.END)
    entry_contacto.delete(0, tk.END)
    entry_id.delete(0,tk.END)
    if not checkbox_var.get():
        checkbox_var.set(True)

boton_anadir = tk.Button(ventana, text="Añadir sede", command=llamar_modificar_sedes)
boton_anadir.place(x=213, y=280)

boton_detalles = tk.Button(ventana, text="detalles", command=llamar_detalles)
boton_detalles.place(x=350, y=320)

boton_detalles = tk.Button(ventana, text="cambiar estado", command=llamar_cambiar_estado)
boton_detalles.place(x=420, y=320)
ventana.mainloop()
