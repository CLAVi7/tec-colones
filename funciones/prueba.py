import tkinter as tk

# Crear la ventana
ventana = tk.Tk()
ventana.title("Selección de opciones")

# Opciones disponibles
opciones = ["Opción 1 ^", "Opción 2 ^", "Opción 3 ^"]

opcion_seleccionada = tk.StringVar(ventana)
opcion_seleccionada.set(opciones[0])  
menu_opciones = tk.OptionMenu(ventana, opcion_seleccionada, *opciones)
menu_opciones.place(x=3,y=5)
menu_opciones.pack()


# Ejecutar el bucle principal
ventana.mainloop()