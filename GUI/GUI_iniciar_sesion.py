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

    label = tk.Label(ventana, text="Correo Institucional @xTec")
    label.place(x=328, y=100)

    entry_correo = tk.Entry(ventana, width=40)
    entry_correo.place(x=275, y=130)


    label = tk.Label(ventana, text="Contraseña")
    label.place(x=370, y=180)

    entry_contraseña = tk.Entry(ventana, width=40)
    entry_contraseña.place(x=275, y=210)
   
    boton_iniciar_sesion = tk.Button(ventana, text="Iniciar Sesión")
    boton_iniciar_sesion.place(x=362, y=265)

    ventana.mainloop()
configuracion_iniciar_sesion()