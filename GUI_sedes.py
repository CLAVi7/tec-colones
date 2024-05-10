import tkinter as tk
from tkinter import messagebox

ventanaCSD = tk.Tk()
ventanaCSD.title("configuracion centros de acopio")
ventanaCSD.geometry("850x450")
ventanaCSD["bg"] = "#C3CDC0"

etiquetaCSD = tk.Label(ventanaCSD, text="configuracion de sedes",  font=("Helvetica", 20), bg="#8DC67E")
etiquetaCSD.config(width=60, height=2)
etiquetaCSD.pack()



entry_nombreCSD = tk.Entry(ventanaCSD, width=40)
entry_nombreCSD.place(x=40, y=110)
label = tk.Label(ventanaCSD, text="Nombre del centro de acopio")
label.place(x=40, y=85)



labelCSD = tk.Label(ventanaCSD, text="provincia a la que pertenece")
labelCSD.place(x=40, y=135)
options = ["Guanacaste", "alajuela", "cartago", "limon", "puntarenas", "heredia", "san jose"]
variable = tk.StringVar(ventanaCSD)
variable.set(options[0])
dropdown_menu = tk.OptionMenu(ventanaCSD, variable, *options)
dropdown_menu.place(x=40, y=160)


ventanaCSD.mainloop()