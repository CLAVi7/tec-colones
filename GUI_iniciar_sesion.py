import tkinter as tk
from tkinter import *
from tkinter import messagebox
from funciones.funciones_iniciar_sesion import *

def configuracion_iniciar_sesion():
    ventana = Tk()
    ventana.title("Iniciar Sesión")
    ventana.geometry("800x400")
    ventana["bg"] = "#C3CDC0"

    etiqueta = tk.Label(ventana, text="Iniciar Sesión", font=("Helvetica", 20), bg="#8DC67E")
    etiqueta.config(width=50, height=2)
    etiqueta.pack()

    label = tk.Label(ventana, text="Correo Institucional @tec.ac.cr", font=("Helvetica", 16))
    label.place(x=270, y=95)

    entry_correo = tk.Entry(ventana, width=43)
    entry_correo.place(x=270, y=130)


    label = tk.Label(ventana, text="Contraseña", font=("Helvetica", 16))
    label.place(x=340, y=175)

    entry_contrasena = tk.Entry(ventana, width=40)
    entry_contrasena.place(x=275, y=210)

    def llamar_comprobar_usuario():
        """
        Carga y muestra la historial en un Listbox. Utiliza la variable global 'listbox_historial' para mantener y actualizar el Listbox.
        """
        comprobaciones(entry_correo, entry_contrasena)
   
    boton_iniciar_sesion = tk.Button(ventana, text="Iniciar Sesión", command=llamar_comprobar_usuario)
    boton_iniciar_sesion.place(x=362, y=265)

    
    ventana.mainloop()
configuracion_iniciar_sesion()