import tkinter as tk
from tkinter import *

ventana = Tk()
ventana.title("añadir materiales")
ventana.geometry("800x400")
ventana["bg"] = "#C3CDC0"
etiqueta = tk.Label(ventana, text="añadir material de reciclaje",  font=("Helvetica", 20), bg="#8DC67E")
etiqueta.config(width=50, height=2)
etiqueta.pack()
entry_nombre = tk.Entry(ventana, width=40)
entry_nombre.place(x=40, y=100)
label=tk.Label(ventana, text="nombre del material")
label.place(x=40, y=80)
label1=tk.Label(ventana, text="Unidades")
label1.place(x=40, y=120)
entry_unidades = tk.Entry(ventana, width=40)
entry_unidades.place(x=40, y=140)
label2=tk.Label(ventana, text="valor de tec-colones")
label2.place(x=40, y=160)
entry_valor = tk.Entry(ventana, width=40)
entry_valor.place(x=40, y=180)
label3=tk.Label(ventana, text="descripción (opcional)")
label3.place(x=40, y=200)
entry_descripcion = tk.Entry(ventana, width=40)
entry_descripcion.place(x=40, y=220)

boton_añadir = tk.Button(ventana, text="añadir material")
boton_añadir.place(x=350, y=160)

class Switch:
    def __init__(self, master, on_text="activo", off_text="inactivo", **kwargs):
        self.var = tk.BooleanVar()
        self.var.set(False)  # Inicialmente apagado

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

ventana.mainloop()