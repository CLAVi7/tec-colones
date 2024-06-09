from funciones.Materiales import *
import json
import tkinter as tk
from tkinter import messagebox
from funciones.carga_descarga_materiales import *


listbox_materiales = None

def main():
    # Crear ventana principal
    ventana = tk.Tk()
    ventana.title("Añadir materiales")
    ventana.geometry("850x450")
    ventana["bg"] = "#C3CDC0"

    # Etiqueta principal
    etiqueta = tk.Label(ventana, text="Añadir material de reciclaje",  font=("Helvetica", 20), bg="#8DC67E")
    etiqueta.config(width=60, height=2)
    etiqueta.pack()

    # Posiciones y espaciado para los elementos de la GUI
    pos_y = 120
    spacing_y = 25

    # Entrada para el nombre del material
    entry_nombre = tk.Entry(ventana, width=40)
    entry_nombre.place(x=40, y=pos_y)
    label = tk.Label(ventana, text="Nombre del material")
    label.place(x=40, y=pos_y - spacing_y)

    # Menú desplegable para las unidades
    label1 = tk.Label(ventana, text="Unidades")
    label1.place(x=40, y=pos_y + spacing_y)
    options = ["Kilogramo", "Unidad", "Litro"]
    variable = tk.StringVar(ventana)
    variable.set(options[0])
    dropdown_menu = tk.OptionMenu(ventana, variable, *options)
    dropdown_menu.place(x=40, y=pos_y + 2*spacing_y)

    # Entrada para el valor del material
    label2 = tk.Label(ventana, text="Valor de tec-colones")
    label2.place(x=40, y=pos_y + 3*spacing_y + 20)
    entry_valor = tk.Entry(ventana, width=40)
    entry_valor.place(x=40, y=pos_y + 4*spacing_y + 20)

    # Entrada para la descripción (opcional)
    label3 = tk.Label(ventana, text="Descripción (opcional)")
    label3.place(x=40, y=pos_y + 5*spacing_y + 20)
    text_descripcion = tk.Text(ventana, height=5, width=40)
    text_descripcion.place(x=40, y=pos_y + 6 * spacing_y + 20)

    # Etiqueta para mostrar los materiales creados
    label4 = tk.Label(ventana, text="Materiales Creados")
    label4.place(x=400, y=pos_y - spacing_y)


    def llamar_cargar_listbox():
        """
        Carga y muestra los materiales en un Listbox. Utiliza la variable global 'listbox_materiales' para mantener y actualizar el Listbox.
        """
        global listbox_materiales
        listbox_materiales = cargar_y_mostrar_materiales_listbox(ventana, listbox_materiales)


    # Llamar a la función para cargar y mostrar los materiales
    llamar_cargar_listbox()



    def llamar_modificar_materiales():
        """
        Llama a la función 'modificar_materiales' para actualizar o añadir materiales en la lista, utilizando variables globales y actualizando el 'listbox_materiales'.
        """
        global listbox_materiales
        listbox_materiales = modificar_materiales(entry_nombre, variable, entry_valor, checkbox_var, text_descripcion, ventana, options, listbox_materiales)
        entry_nombre.delete(0, tk.END)
        variable.set(options[0])
        entry_valor.delete(0, tk.END)
        text_descripcion.delete("1.0", tk.END)
        if not checkbox_var.get():
            checkbox_var.set(True)

    def llamar_detalles():
        """
        Muestra los detalles del material seleccionado desde 'listbox_materiales'.
        """
        mostrar_datos_seleccionados(listbox_materiales)


    def llamar_cambiar_estado():
        """
        Cambia el estado del material seleccionado en el Listbox 'listbox_materiales', y actualiza el Listbox para reflejar los cambios.
        """
        cambiar_estado_listbox(ventana, listbox_materiales)


    # Botón para añadir material
    boton_anadir = tk.Button(ventana, text="Añadir material", command=llamar_modificar_materiales)
    boton_anadir.place(x=192, y=pos_y + 7*spacing_y + 90)

    # Botón para mostrar detalles del material seleccionado
    boton_mostrar = tk.Button(ventana, text="Detalles", command=llamar_detalles)
    boton_mostrar.place(x=400, y=pos_y + 7*spacing_y + 20)

    # Botón para cambiar el estado del material seleccionado
    cambiar_estado_boton = tk.Button(ventana, text="Cambiar estado", command=llamar_cambiar_estado)
    cambiar_estado_boton.place(x=465, y=pos_y + 7*spacing_y + 20)

    # Checkbox para el estado del material
    checkbox_var = tk.BooleanVar()
    checkbox_var.set(True)
    checkbox = tk.Checkbutton(ventana, text="Activo", variable=checkbox_var)
    checkbox.place(x=40, y=pos_y + 7*spacing_y + 90)

    # Ejecutar la ventana principal
    ventana.mainloop()
main()


