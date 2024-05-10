import tkinter as tk
from tkinter import *
from tkinter import messagebox
from json_centro_acopio import *

ventana = Tk()
ventana.title("Centros de Acopio")
ventana.geometry("800x400")
ventana["bg"] = "#C3CDC0"

etiqueta = tk.Label(ventana, text="Configuración Centros de Acopio",  font=("Helvetica", 20), bg="#8DC67E")
etiqueta.config(width=50, height=2)
etiqueta.pack()

label = tk.Label(ventana, text="Ingresar Centro de Acopio")
label.place(x=40, y=80)

entry_nombre = tk.Entry(ventana, width=40)
entry_nombre.place(x=40, y=105)

label = tk.Label(ventana, text="Ubicación del Centro de Acopio")
label.place(x=40, y=135)

entry_ubicacion = tk.Entry(ventana, width=40)
entry_ubicacion.place(x=40, y=160)

label1 = tk.Label(ventana, text="Sede a la que Pertenece el Centro de Acopio")
label1.place(x=40, y=190)
options = ["Seleccionar1", "Seleccionar2"]
variable = tk.StringVar(ventana)
variable.set(options[0])
dropdown_menu = tk.OptionMenu(ventana, variable, *options)
dropdown_menu.place(x=40, y=215)

label = tk.Label(ventana, text="Número de Contacto")
label.place(x=40, y=255)

entry_contacto = tk.Entry(ventana, width=40)
entry_contacto.place(x=40, y=280)

label4 = tk.Label(ventana, text="Centros de Acopio Creados")
label4.place(x=350, y=80)

listbox_centros = None


def cargar_y_mostrar_centros_listbox():
    
    global listbox_centros

    if listbox_centros is None:
        listbox_centros = tk.Listbox(ventana, height=12, width=70)
        listbox_centros.place(x=350, y=105)
    else:
        listbox_centros.delete(0, tk.END)

    lista_centros = cargar_centros("Sedes_y_centros_de_acopio/centros.json")

    for centro in lista_centros:
        texto = (f"Nombre: {centro.nombre}"
                 f" - Ubicacion: {centro.ubicacion}"
                 f" - Sede: {centro.sede}"
                 f" - numero_de_contacto: {centro.numero_de_contacto}"
                 f" - Estado: {'Activo' if centro.estado else 'Inactivo'}")
        listbox_centros.insert(tk.END, texto)


cargar_y_mostrar_centros_listbox()


def comprobaciones():
    
    if not (5 <= len(entry_nombre.get()) <= 30):
        raise ValueError("El nombre debe tener entre 5 y 30 caracteres.")
    if not (1 <= len(entry_ubicacion.get()) <= 100):
        raise ValueError("El nombre debe tener máximo 100 caracteres.")
    if not (1 <= len(entry_contacto.get()) <= 8):
        raise ValueError("El numero debe tener máximo 8 caracteres.")
    if not (1 <= len(variable.get())):
        raise ValueError("Debe ingresar un valor para las sedes.")


def Modificar_centros():


    try:
        comprobaciones()
        nuevo_centro = centro_de_acopio(nombre=entry_nombre.get(),
                                  ubicacion=entry_ubicacion.get(),
                                  sede=variable.get(),
                                  numero_de_contacto=entry_contacto.get(),
                                  estado=checkbox_var.get(),)

        lista_centros = cargar_centros("Sedes_y_centros_de_acopio/centros.json")
        if nuevo_centro not in lista_centros:
            lista_centros.append(nuevo_centro)
            guardar_centros(lista_centros, "Sedes_y_centros_de_acopio/centros.json")
            cargar_y_mostrar_centros_listbox()

            entry_nombre.delete(0, tk.END)
            variable.set(options[0])
            entry_ubicacion.delete(0, tk.END)
            entry_contacto.delete(0, tk.END)
            if not checkbox_var.get():
                checkbox_var.set(True)

        else:
            messagebox.showwarning("Duplicado", "El centro ya existe en la lista.")

    except ValueError as error:
        messagebox.showerror("Error de Comprobación", str(error))
    except TypeError as error:
        messagebox.showerror("Error de Tipo", str(error))#Por que se muestra este error?


def mostrar_datos_seleccionados():
    # Muestra los detalles del material seleccionado en la Listbox.

    seleccion = listbox_centros.curselection()
    if len(seleccion) == 0:
        messagebox.showinfo("Error", "Por favor, seleccione un centro de la lista.")
        return

    indice = seleccion[0]
    lista_centros = cargar_centros("Sedes_y_centros_de_acopio/centros.json")
    centro = lista_centros[indice]
    mensaje = f"{centro.__str__()}"
    messagebox.showinfo("Centro", mensaje)


def cambiar_estdo_listbox():
    # Cambia el estado del material seleccionado en la Listbox.

    seleccion = listbox_centros.curselection()
    if len(seleccion) == 0:
        messagebox.showinfo("Error", "Por favor, seleccione un elemento de la lista.")
        return

    indice = seleccion[0]
    lista_centros = cargar_centros("Sedes_y_centros_de_acopio/centros.json")
    lista_centros[indice].estado = not lista_centros[indice].estado
    guardar_centros(lista_centros, "Sedes_y_centros_de_acopio/centros.json")
    cargar_y_mostrar_centros_listbox()



boton_anadir = tk.Button(ventana, text="Añadir Centro de Acopio", command=Modificar_centros)
boton_anadir.place(x=143, y=310)

boton_mostrar = tk.Button(ventana, text="Detalles", command=mostrar_datos_seleccionados)
boton_mostrar.place(x=350, y=310)

cambiar_estado_boton = tk.Button(ventana, text="Cambiar estado", command=cambiar_estdo_listbox)
cambiar_estado_boton.place(x=415, y=310)

checkbox_var = tk.BooleanVar()
checkbox_var.set(True)
checkbox = tk.Checkbutton(ventana, text="Activo", variable=checkbox_var)
checkbox.place(x=40, y=310)

ventana.mainloop()
