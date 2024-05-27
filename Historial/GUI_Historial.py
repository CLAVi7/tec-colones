import tkinter as tk
from tkcalendar import DateEntry
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

ventana.mainloop()
