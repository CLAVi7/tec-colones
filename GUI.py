import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Funciones_json import modificar_materiales


ventana = Tk()
ventana.title("añadir materiales")
ventana.geometry("800x400")
ventana["bg"] = "#C3CDC0"

etiqueta = tk.Label(ventana, text="añadir material de reciclaje",  font=("Helvetica", 20), bg="#8DC67E")
etiqueta.config(width=50, height=2)
etiqueta.pack()

entry_nombre = tk.Entry(ventana, width=40)
entry_nombre.place(x=40, y=100)

label = tk.Label(ventana, text="nombre del material")
label.place(x=40, y=80)

label1 = tk.Label(ventana, text="Unidades")
label1.place(x=40, y=120)

entry_unidades = tk.Entry(ventana, width=40)
entry_unidades.place(x=40, y=140)

label2 = tk.Label(ventana, text="valor de tec-colones")
label2.place(x=40, y=160)

entry_valor = tk.Entry(ventana, width=40)
entry_valor.place(x=40, y=180)

label3 = tk.Label(ventana, text="descripción (opcional)")
label3.place(x=40, y=200)

entry_descripcion = tk.Entry(ventana, width=40)
entry_descripcion.place(x=40, y=220)


class Switch:
    def __init__(self, master, on_text="inactivo", off_text=" activo", **kwargs):
        self.var = tk.BooleanVar()
        self.var.set(True)  # Inicialmente encendido

        self.on_text = on_text
        self.off_text = off_text

        self.button = tk.Button(master, text=self.off_text, command=self.toggle, **kwargs)
        self.button.place(x=120, y=240)

    def toggle(self):
        self.var.set(not self.var.get())
        if self.var.get():
            self.button.config(text=self.on_text)
            print("material activo")
        else:
            self.button.config(text=self.off_text)
            print("material inactivo")


switch = Switch(ventana, width=10, height=2)

label4 = tk.Label(ventana, text="Materiales Creados")
label4.place(x=500, y=80)

listbox = tk.Listbox()
listbox.insert(0)
listbox.place(x=500, y=100)

cambiar_estado_boton = tk.Button(ventana, text="cambiar estado")
cambiar_estado_boton.place(x=500, y=300)


def comprobaciones():
    if not (5 <= len(entry_nombre.get()) <= 30):
        raise ValueError("El nombre debe tener entre 5 y 30 caracteres.")
    if entry_descripcion.get() and len(entry_descripcion.get()) > 1000:
        raise ValueError("La descripción no puede tener más de 1000 caracteres.")
    if not isinstance(entry_nombre.get(), str) or not isinstance(entry_unidades.get(), str) or not isinstance(
            entry_descripcion.get(), str):
        raise TypeError("El nombre, la unidad y la descripción deben ser cadenas de texto.")
    try:
        valor_numerico = float(entry_valor.get())
        if not (0 <= valor_numerico <= 100000):
            raise ValueError("El valor debe estar entre 0 y 100000.")
    except ValueError:
        raise ValueError("El valor debe ser un número válido.")


def Modificar_materiales():
    try:
        comprobaciones()
        modificar_materiales(entry_nombre.get(), entry_unidades.get(), entry_valor.get(), switch.var,
                             entry_descripcion.get())
        limpiar_entrys()
    except ValueError as error:
        messagebox.showerror("Error de Comprobación", str(error))
    except TypeError as error:
        messagebox.showerror("Error de Tipo", str(error))


def limpiar_entrys():
    entry_nombre.delete(0, tk.END)
    entry_unidades.delete(0, tk.END)
    entry_valor.delete(0, tk.END)
    switch.var.set(True)
    entry_descripcion.delete(0, tk.END)


boton_anadir = tk.Button(ventana, text="añadir material", command=Modificar_materiales)
boton_anadir.place(x=300, y=160)

ventana.mainloop()
