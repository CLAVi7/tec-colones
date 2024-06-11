import tkinter as tk
ventana = tk.Tk()
ventana.title("estudiante")
ventana.geometry("800x400")
ventana["bg"] = "#C3CDC0"

etiqueta = tk.Label(ventana, text="bienvenido al sistema de tec-colones",  font=("Helvetica", 20), bg="#8DC67E")
etiqueta.config(width=50, height=2)
etiqueta.pack()
ventana.mainloop()