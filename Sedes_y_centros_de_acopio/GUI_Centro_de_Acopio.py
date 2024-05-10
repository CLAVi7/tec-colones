import tkinter as tk
from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.title("Centros de Acopio")
ventana.geometry("800x400")
ventana["bg"] = "#C3CDC0"

etiqueta = tk.Label(ventana, text="Configuración Centros de Acopio",  font=("Helvetica", 20), bg="#8DC67E")
etiqueta.config(width=50, height=2)
etiqueta.pack()

label = tk.Label(ventana, text="Ingresar Centro de Acopio")
label.place(x=40, y=80)

entry_centro = tk.Entry(ventana, width=40)
entry_centro.place(x=40, y=105)

label = tk.Label(ventana, text="Ubicación del Centro de Acopio")
label.place(x=40, y=135)

entry_ubicacion = tk.Entry(ventana, width=40)
entry_ubicacion.place(x=40, y=160)

label1 = tk.Label(ventana, text="Sede a la que Pertenece el Centro de Acopio")
label1.place(x=40, y=190)
options = ["Seleccionar"]
variable = tk.StringVar(ventana)
variable.set(options[0])
dropdown_menu = tk.OptionMenu(ventana, variable, *options)
dropdown_menu.place(x=40, y=215)

label = tk.Label(ventana, text="Número de Contacto")
label.place(x=40, y=255)

entry_contacto = tk.Entry(ventana, width=40)
entry_contacto.place(x=40, y=280)

label4 = tk.Label(ventana, text="Centros de Acopio Creados")
label4.place(x=350, y=80)

listbox_materiales = None

def cargar_y_mostrar_materiales_listbox():
    
    global listbox_materiales

    if listbox_materiales is None:
        listbox_materiales = tk.Listbox(ventana, height=12, width=70)
        listbox_materiales.place(x=350, y=105)
    else:
        listbox_materiales.delete(0, tk.END)

cargar_y_mostrar_materiales_listbox()

def comprobaciones():
    
    if not (5 <= len(entry_nombre.get()) <= 30):
        raise ValueError("El nombre debe tener entre 5 y 30 caracteres.")
    if not (1 <= len(entry_ubicacion.get()) <= 100):
        raise ValueError("El nombre debe tener máximo 100 caracteres.")
    if not (1 <= len(entry_contacto.get()) < 8):
        raise ValueError("El nombre debe tener máximo 8 caracteres.")
    if not (1 <= len(variable.get())):
        raise ValueError("Debe ingresar un valor para las sedes.")
    if (not isinstance(entry_nombre.get(), str) or not isinstance(variable.get(), str) or
            not isinstance(text_descripcion.get("1.0", "end-1c"), str)):
        raise TypeError("El Centro de Acopio y la sede deben ser cadenas de texto.")
    try:
        valor_numerico = float(entry_valor.get())
        if not (0 <= valor_numerico <= 100000):
            raise ValueError("El valor debe estar entre 0 y 100000.")
    except ValueError:
        raise ValueError("El valor debe ser un número válido.")

boton_anadir = tk.Button(ventana, text="Añadir Centro de Acopio")
boton_anadir.place(x=143, y=310)

boton_mostrar = tk.Button(ventana, text="Detalles")
boton_mostrar.place(x=350, y=310)

cambiar_estado_boton = tk.Button(ventana, text="Cambiar estado")
cambiar_estado_boton.place(x=415, y=310)

checkbox_var = tk.BooleanVar()
checkbox_var.set(True)
checkbox = tk.Checkbutton(ventana, text="Activo", variable=checkbox_var)
checkbox.place(x=40, y=310)

ventana.mainloop()
