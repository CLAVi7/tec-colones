import tkinter as tk
from GUI_cambio_material import cambio_material
from GUI_Historial import historial

ventana = tk.Tk()
ventana.title("funcionario de planta")
ventana.geometry("800x400")
ventana["bg"] = "#C3CDC0"

etiqueta = tk.Label(ventana, text="funcionario de planta",  font=("Helvetica", 20), bg="#8DC67E")
etiqueta.config(width=50, height=2)
etiqueta.pack()

boton_cambio = tk.Button(ventana, text="cambio de material", command=cambio_material)
boton_cambio.place(x=345, y=100)
boton_historial = tk.Button(ventana, text="ver historial", command=historial)
boton_historial.place(x=345, y=150)



ventana.mainloop()