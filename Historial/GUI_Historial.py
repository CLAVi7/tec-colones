import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry 
from json_recibo import *
from funciones_historial import *

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

fecha_final = tk.Label(ventana, text="Fecha inicial", font=("Helvetica", 12), width=16)
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

centro = ["Centro 1", "Centro 2", "Centro 3"]
variable = tk.StringVar(ventana)
variable.set(centro[0])
dropdown_menu = tk.OptionMenu(ventana, variable, *centro)
dropdown_menu.place(x=400, y=100)

listbox_historial = None

def llamar_cargar_listbox():
    """
    Carga y muestra la historial en un Listbox. Utiliza la variable global 'listbox_historial' para mantener y actualizar el Listbox.
    """
    global listbox_historial
    listbox_historial = cargar_y_mostrar_historial_listbox(ventana, listbox_historial)



boton_anadir = tk.Button(ventana, text="Filtrar", font=("Helvetica", 11))
boton_anadir.place(x=550, y=75)

boton_detalles = tk.Button(ventana, text="Detalles", font=("Helvetica", 11))
boton_detalles.place(x=40, y=340)

cargar_y_mostrar_recibos(listbox, 'Historial/recibos.json')

ventana.mainloop()
