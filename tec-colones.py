import tkinter as tk
from tkinter import *
from datetime import datetime
import random

lista_materiales = []

class Material:
    def __init__(self, nombre="", unidad="", valor_unitario=0, estado=False, descripcion=None):
        self.id = self.generar_id_unico()
        self.nombre = nombre
        self.unidad = unidad
        self.valor_unitario = valor_unitario
        self.estado = estado
        self.fecha_creacion = datetime.now()
        self.descripcion = descripcion

    def generar_id_unico(self):
        caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        id_aleatorio = ''.join(random.choice(caracteres) for _ in range(12))
        return f"M-{id_aleatorio}"

    def __str__(self):
        return (f"ID: {self.id}\n"
                f"Material: {self.nombre}\n"
                f"Unidad: {self.unidad}\n"
                f"Valor Unitario: {self.valor_unitario} Tec-Colones\n"
                f"Estado: {'Activo' if self.estado else 'Inactivo'}\n"
                f"Fecha de Creación: {self.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"Descripción: {self.descripcion if self.descripcion else 'N/A'}")

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

def agregar_material():
    nombre = entry_nombre.get()
    unidad = entry_unidades.get()
    valor_unitario = float(entry_valor.get())
    estado = switch.var.get()  # Obtener el estado del switch
    descripcion = entry_descripcion.get()

    material = Material(nombre, unidad, valor_unitario, estado, descripcion)
    lista_materiales.append(material)  # Agregar el nuevo material a la lista

    # Agregar el nombre y la unidad del material a la Listbox
    listbox_materiales.insert(tk.END, f"{material.nombre} - {material.unidad} - {material.valor_unitario}- {'Activo' if material.estado else 'Inactivo'}")

    # Limpiar los cuadros de entrada
    entry_nombre.delete(0, tk.END)
    entry_unidades.delete(0, tk.END)
    entry_valor.delete(0, tk.END)
    entry_descripcion.delete(0, tk.END)

def cambiar_estado_material():
    # Obtener el índice seleccionado en la Listbox
    seleccion = listbox_materiales.curselection()
    if seleccion:
        indice = seleccion[0]  # Solo tomamos el primer índice seleccionado
        # Obtener el material seleccionado de la lista
        material = lista_materiales[indice]
        # Cambiar el estado del material
        material.estado = not material.estado
        # Actualizar la presentación en la Listbox
        listbox_materiales.delete(indice)  # Eliminar el material anterior
        listbox_materiales.insert(indice, f"{material.nombre} - {material.unidad} - {material.valor_unitario}- {'Activo' if material.estado else 'Inactivo'}")

ventana = Tk()
ventana.title("Añadir Materiales")
ventana.geometry("800x400")
ventana["bg"] = "#C3CDC0"

etiqueta = tk.Label(ventana, text="Añadir Material de Reciclaje", font=("Helvetica", 20), bg="#8DC67E")
etiqueta.config(width=50, height=2)
etiqueta.pack()

entry_nombre = tk.Entry(ventana, width=40)
entry_nombre.place(x=40, y=100)

label = tk.Label(ventana, text="Nombre del Material")
label.place(x=40, y=80)

label1 = tk.Label(ventana, text="Unidades")
label1.place(x=40, y=120)
entry_unidades = tk.Entry(ventana, width=40)
entry_unidades.place(x=40, y=140)

label2 = tk.Label(ventana, text="Valor de Tec-Colones")
label2.place(x=40, y=160)
entry_valor = tk.Entry(ventana, width=40)
entry_valor.place(x=40, y=180)

label3 = tk.Label(ventana, text="Descripción (Opcional)")
label3.place(x=40, y=200)
entry_descripcion = tk.Entry(ventana, width=40)
entry_descripcion.place(x=40, y=220)

switch = Switch(ventana, width=10, height=2)
switch.button.place(x=120, y=240)

boton_añadir = tk.Button(ventana, text="Añadir Material", command=agregar_material)
boton_añadir.place(x=300, y=160)

label4 = tk.Label(ventana, text="Materiales Creados")
label4.place(x=500, y=80)

cambiar_estado_boton = tk.Button(ventana, text="Cambiar Estado", command=cambiar_estado_material)
cambiar_estado_boton.place(x=500, y=300)

listbox_materiales = tk.Listbox(ventana, height=10, width=50)
listbox_materiales.place(x=500, y=100)

ventana.mainloop()