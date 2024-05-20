import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

def obtener_fecha():
    fecha_seleccionada = calendario.get_date()
    print("Fecha seleccionada:", fecha_seleccionada)

# Crear la ventana principal
root = tk.Tk()
root.title("Selector de Fecha")

# Crear el widget de calendario
calendario = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
calendario.pack(pady=10)

# Botón para obtener la fecha seleccionada
boton_obtener_fecha = ttk.Button(root, text="Obtener Fecha", command=obtener_fecha)
boton_obtener_fecha.pack(pady=10)

# Iniciar el bucle principal de la ventana
root.mainloop()