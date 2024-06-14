import tkinter as tk
from GUI_nuevo_material import main
from GUI_sedes import configuracion_sedes
from GUI_Centro_de_Acopio import configuracion_centros


def admin():
    ventana = tk.Tk()
    ventana.title("administrador tec-colones")
    ventana.geometry("800x400")
    ventana["bg"] = "#C3CDC0"

    etiqueta = tk.Label(ventana, text="administrador tec-colones",  font=("Helvetica", 20), bg="#8DC67E")
    etiqueta.config(width=50, height=2)
    etiqueta.pack()

    boton_nuevo_material = tk.Button(ventana, text="nuevo material", command=main )
    boton_nuevo_material.place(x=345, y=100)
    boton_sedes = tk.Button(ventana, text="configuracion de sedes", command=configuracion_sedes)
    boton_sedes.place(x=345, y=150)
    boton_centros = tk.Button(ventana, text="configuracion de centros de acopio", command=configuracion_centros)
    boton_centros.place(x=345, y=200)
    boton_historial_general = tk.Button(ventana, text="ver historial general")
    boton_historial_general.place(x=345, y=250)

    ventana.mainloop()

