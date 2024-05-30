import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import datetime
import json
from cambio_material_teccolones.funcione_GUI_Cambio import conseguir_centro
from funciones_historial import *

# Función para cargar los datos del JSON desde un archivo
def cargar_recibos_desde_archivo(ruta):
    with open(ruta, 'r') as archivo:
        return json.load(archivo)

# Ruta del archivo JSON
ruta_json = 'historial_recibos.json'

# Cargar los datos de los recibos desde el archivo
recibos = cargar_recibos_desde_archivo(ruta_json)

ventana = tk.Tk()
ventana.title("Historial")
ventana.geometry("800x400")
ventana["bg"] = "#C3CDC0"

etiqueta = tk.Label(ventana, text="Ver Historial de Centro de Acopio",  font=("Helvetica", 20), bg="#8DC67E")
etiqueta.config(width=50, height=2)
etiqueta.pack()

fecha_inicial = tk.Label(ventana, text="Fecha inicial", font=("Helvetica", 12), width=16)
fecha_inicial.place(x=40, y=75)
calendario_inicial = DateEntry(ventana, width=16, font=("Helvetica", 11), background='#8DC67E', foreground='black', borderwidth=2)
calendario_inicial.place(x=40, y=100) 

fecha_final = tk.Label(ventana, text="Fecha final", font=("Helvetica", 12), width=16)
fecha_final.place(x=220, y=75)
calendario_final = DateEntry(ventana, width=16, font=("Helvetica", 11), background='#8DC67E', foreground='black', borderwidth=2)
calendario_final.place(x=220, y=100) 

def validar_fechas(event):
    fecha_inicial = calendario_inicial.get_date()
    fecha_final = calendario_final.get_date()
    if fecha_final < fecha_inicial:
        messagebox.showerror("Error de fecha", "La fecha final no puede ser menor que la fecha inicial.")
        calendario_final.set_date(fecha_inicial)  # Restablecer la fecha final a la fecha inicial

# Asociar el evento de selección de fecha a la función de validación
calendario_inicial.bind("<<DateEntrySelected>>", validar_fechas)
calendario_final.bind("<<DateEntrySelected>>", validar_fechas)

listbox = tk.Listbox(ventana, selectmode=tk.SINGLE)
listbox.place(x=50, y=150, width=700, height=170)

label_centro = tk.Label(ventana, text="Centro de Acopio", font=("Helvetica", 12))
label_centro.place(x=400, y=75)


centro = conseguir_centro()
variable = tk.StringVar(ventana)
variable.set(centro[0])
dropdown_menu = tk.OptionMenu(ventana, variable, *centro)
dropdown_menu.place(x=400, y=100)

listbox_historial = None
#listbox_historial = []

# def cargar_y_mostrar_historial_listbox():
#     """
#     Carga los recibos desde el JSON y los muestra en el Listbox.
#     """
#     global listbox_historial
#     listbox_historial = recibos
#     for recibo in recibos:
#         listbox.insert(tk.END, f"{recibo['fecha']} - {recibo['centro']} - {recibo['material']}")

def mostrar_detalle_recibo():
    global listbox_historial
    seleccion = listbox.curselection()
    if seleccion:
        index = seleccion[0]
        recibo = listbox_historial[index]
        detalles = f"ID: {recibo['id']}\nFecha: {recibo['fecha']}\nCentro: {recibo['centro']}\nCarnet: {recibo['carnet']}\nMaterial: {recibo['material']}\nTec Colones: {recibo['tec_colones']}"
        messagebox.showinfo("Detalle del Recibo", detalles)

def filtrar_recibos():
    global listbox_historial
    # Obtener las fechas seleccionadas
    fecha_inicio = calendario_inicial.get_date()
    fecha_fin = calendario_final.get_date()
    
    # Limpiar el listbox antes de agregar los elementos filtrados
    listbox_historial = None
    
    # Filtrar los recibos según las fechas seleccionadas
    for recibo in recibos:
        fecha_recibo = datetime.strptime(recibo['fecha'], "%Y-%m-%d").date()
        if fecha_inicio <= fecha_recibo <= fecha_fin:
            listbox_historial.insert(tk.END, f"{recibo['fecha']} - {recibo['centro']} - {recibo['material']}")


def llamar_cargar_listbox():
    """
    Carga y muestra la historial en un Listbox. Utiliza la variable global 'listbox_historial' para mantener y actualizar el Listbox.
    """
    global listbox_historial
    listbox_historial = cargar_y_mostrar_historial_listbox(ventana, listbox_historial)

llamar_cargar_listbox()


def mostrar_detalle_recibo():
    mostrar_dato_listbox(listbox_historial)

boton_anadir = tk.Button(ventana, text="Filtrar", font=("Helvetica", 11), command=filtrar_recibos)
boton_anadir.place(x=550, y=75)

boton_detalles = tk.Button(ventana, text="Detalles", font=("Helvetica", 11), command=mostrar_dato_listbox)
boton_detalles.place(x=40, y=340)

ventana.mainloop()
