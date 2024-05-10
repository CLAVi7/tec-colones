import tkinter as tk
import json_sedes

ventana = tk.Tk()
ventana.title("sedes")
ventana.geometry("800x400")
ventana["bg"] = "#C3CDC0"

etiqueta = tk.Label(ventana, text="Configuración sedes",  font=("Helvetica", 20), bg="#8DC67E")
etiqueta.config(width=50, height=2)
etiqueta.pack()

label = tk.Label(ventana, text="Ingresar nombre de la sede")
label.place(x=40, y=80)

entry_nombre = tk.Entry(ventana, width=40)
entry_nombre.place(x=40, y=105)

label1 = tk.Label(ventana, text="provincia a la que pertenece")
label1.place(x=40, y=130)
options = ["Cartago","San Jose", "Puntarenas", "Guanacaste", "Limón","Heredia", "Alajuela"]
variable = tk.StringVar(ventana)
variable.set(options[0])
dropdown_menu = tk.OptionMenu(ventana, variable, *options)
dropdown_menu.place(x=40, y=155)

label2 = tk.Label(ventana, text="numero de contacto")
label2.place(x=40, y=190)

entry_contacto = tk.Entry(ventana, width=40)
entry_contacto.place(x=40, y=215)

checkbox_var = tk.BooleanVar()
checkbox_var.set(True)
checkbox = tk.Checkbutton(ventana, text="Activo", variable=checkbox_var)
checkbox.place(x=40, y=240)



label3 = tk.Label(ventana, text="sedes creadas")
label3.place(x=350, y=80)

listbox_sedes = None
def cargar_y_mostrar_centros_listbox():
    global listbox_sedes

    if listbox_sedes is None:
        listbox_sedes = tk.Listbox(ventana, height=12, width=70)
        listbox_sedes.place(x=350, y=105)
    else:
        listbox_sedes.delete(0, tk.END)

    lista_centros = cargar_sedes("Sedes_y_centros_de_acopio/sedes.json")

    for sede in lista_sede:
        texto = (f"Nombre: {sede.nombre}"
                 f" - Ubicacion: {sede.provincia}
                 f" - numero_contacto: {sede.numero_contacto}"
                 f" - estado: {'Activo' if sede.estado else 'Inactivo'}")
        listbox_sedes.insert(tk.END, texto)


cargar_y_mostrar_sedes_listbox()


def comprobaciones():
    if not (5 <= len(entry_nombre.get()) <= 30):
        raise ValueError("El nombre debe tener entre 5 y 30 caracteres.")
    if not (1 <= len(variable.get())):
        raise ValueError("Debe seleccionar una provincia para las sedes.")
    # Verificamos si la longitud del número limpio es igual a la longitud esperada
    if not (len(entry_contacto.get()) == 8):
        raise ValueError("El número de contacto debe tener 8 dígitos.")



boton_anadir = tk.Button(ventana, text="Añadir sede")
boton_anadir.place(x=213, y=280)

boton_detalles = tk.Button(ventana, text="detalles")
boton_detalles.place(x=350, y=320)

boton_detalles = tk.Button(ventana, text="cambiar estado")
boton_detalles.place(x=420, y=320)
ventana.mainloop()
