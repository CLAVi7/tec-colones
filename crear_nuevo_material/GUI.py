import tkinter as tk
from tkinter import messagebox
from carga_descarga_materiales import *

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

listbox_materiales = None

# Función para cargar y mostrar materiales en la listbox
def cargar_y_mostrar_materiales_listbox():

    # Carga los materiales desde el archivo JSON y los muestra en la Listbox.

    global listbox_materiales

    if listbox_materiales is None:
        listbox_materiales = tk.Listbox(ventana, height=11, width=70)
        listbox_materiales.place(x=400, y=pos_y)
    else:
        listbox_materiales.delete(0, tk.END)

    lista_materiales = cargar_materiales('crear_nuevo_material/materiales.json')
    for material in lista_materiales:
        texto = (f"Nombre: {material.nombre} - Unidad: {material.unidad} - Valor Unitario: {material.valor_unitario}"
                 f" - Estado: {'Activo' if material.estado else 'Inactivo'}")
        listbox_materiales.insert(tk.END, texto)


# Llamar a la función para cargar y mostrar los materiales
cargar_y_mostrar_materiales_listbox()

# Función para realizar comprobaciones antes de modificar los materiales
def comprobaciones():
    
    # Realiza comprobaciones sobre los datos ingresados por el usuario.
    
    if not (5 <= len(entry_nombre.get()) <= 30):
        raise ValueError("El nombre debe tener entre 5 y 30 caracteres.")
    if not (1 <= len(variable.get())):
        raise ValueError("Debe ingresar un valor para las unidades.")
    if text_descripcion.get("1.0", "end-1c") and len(text_descripcion.get("1.0", "end-1c")) > 1000:
        raise ValueError("La descripción no puede tener más de 1000 caracteres.")
    if (not isinstance(entry_nombre.get(), str) or not isinstance(variable.get(), str) or
            not isinstance(text_descripcion.get("1.0", "end-1c"), str)):
        raise TypeError("El nombre, la unidad y la descripción deben ser cadenas de texto.")
    try:
        valor_numerico = float(entry_valor.get())
        if not (0 <= valor_numerico <= 100000):
            raise ValueError("El valor debe estar entre 0 y 100000.")
    except ValueError:
        raise ValueError("El valor debe ser un número válido.")

# Función para modificar materiales
def Modificar_materiales():
    
    # Modifica los materiales según los datos ingresados por el usuario.
    
    try:
        comprobaciones()
        nuevo_material = Material(nombre=entry_nombre.get(),
                                  unidad=variable.get(),
                                  valor_unitario=entry_valor.get(),
                                  estado=checkbox_var.get(),
                                  descripcion=text_descripcion.get("1.0", "end-1c"))

        lista_materiales = cargar_materiales('crear_nuevo_material/materiales.json')
        if nuevo_material not in lista_materiales:
            lista_materiales.append(nuevo_material)
            guardar_materiales(lista_materiales, 'crear_nuevo_material/materiales.json')
            cargar_y_mostrar_materiales_listbox()

            entry_nombre.delete(0, tk.END)
            variable.set(options[0])
            entry_valor.delete(0, tk.END)
            text_descripcion.delete("1.0", tk.END)
            if not checkbox_var.get():
                checkbox_var.set(True)

        else:
            messagebox.showwarning("Duplicado", "El material ya existe en la lista.")

    except ValueError as error:
        messagebox.showerror("Error de Comprobación", str(error))
    except TypeError as error:
        messagebox.showerror("Error de Tipo", str(error))

# Función para mostrar detalles del material seleccionado
def mostrar_datos_seleccionados():
    
    # Muestra los detalles del material seleccionado en la Listbox.
    
    seleccion = listbox_centros.curselection()
    if len(seleccion) == 0:
        messagebox.showinfo("Error", "Por favor, seleccione un elemento de la lista.")
        return

    indice = seleccion[0]
    lista_materiales = cargar_materiales('crear_nuevo_material/materiales.json')
    Material = lista_materiales[indice]
    mensaje = f"{Material.__str__()}"
    messagebox.showinfo("Material", mensaje)

# Función para cambiar el estado del material seleccionado
def cambiar_estdo_listbox():
    
    # Cambia el estado del material seleccionado en la Listbox.
    
    seleccion = listbox_centros.curselection()
    if len(seleccion) == 0:
        messagebox.showinfo("Error", "Por favor, seleccione un elemento de la lista.")
        return

    indice = seleccion[0]
    lista_materiales = cargar_materiales('crear_nuevo_material/materiales.json')
    lista_materiales[indice].estado = not lista_materiales[indice].estado
    guardar_materiales(lista_materiales, 'crear_nuevo_material/materiales.json')
    cargar_y_mostrar_materiales_listbox()

# Botón para añadir material
boton_anadir = tk.Button(ventana, text="Añadir material", command=Modificar_materiales)
boton_anadir.place(x=192, y=pos_y + 7*spacing_y + 90)

# Botón para mostrar detalles del material seleccionado
boton_mostrar = tk.Button(ventana, text="Detalles", command=mostrar_datos_seleccionados)
boton_mostrar.place(x=400, y=pos_y + 7*spacing_y + 20)

# Botón para cambiar el estado del material seleccionado
cambiar_estado_boton = tk.Button(ventana, text="Cambiar estado", command=cambiar_estdo_listbox)
cambiar_estado_boton.place(x=465, y=pos_y + 7*spacing_y + 20)

# Checkbox para el estado del material
checkbox_var = tk.BooleanVar()
checkbox_var.set(True)
checkbox = tk.Checkbutton(ventana, text="Activo", variable=checkbox_var)
checkbox.place(x=40, y=pos_y + 7*spacing_y + 90)

# Ejecutar la ventana principal
ventana.mainloop()
