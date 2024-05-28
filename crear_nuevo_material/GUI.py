from Materiales import *
import json
import tkinter as tk
from tkinter import messagebox


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

=======

#Función que guarda una lista de objetos de material en un archivo JSON.
def guardar_materiales(materiales, archivo):
    """
    Guarda una lista de objetos de material en un archivo JSON.

    Parámetros:
    materiales (list): Lista de objetos Material para ser guardados.
    archivo (str): Ruta del archivo donde se guardarán los datos.
    """
    with open(archivo, 'w') as f:
        json.dump([material.to_dict() for material in materiales], f, ensure_ascii=False, indent=4)


#Carga la mediante una lista los materiales guardados desde el archivo JSON.
def cargar_materiales(archivo):
    """
    Carga materiales desde un archivo JSON y los retorna en una lista.

    Parámetros:
    archivo (str): Ruta del archivo JSON de donde se cargarán los materiales.

    Retorna:
    list: Lista de objetos Material cargados desde el archivo.
    """
    lista_materiales = []
    try:
        with open(archivo, 'r') as f:
            data = json.load(f)
            for item in data:
                material = Material(
                    nombre=item['nombre'],
                    unidad=item['unidad'],
                    valor_unitario=item['valor_unitario'],
                    estado=item['estado'] == 'Activo',  # Convertir 'Activo'/'Inactivo' a booleano
                    descripcion=item['descripcion'] if 'descripcion' in item else None
                )
                material.fecha_creacion = datetime.strptime(item['fecha_creacion'], '%Y-%m-%d %H:%M:%S')
                material.id = item['id']
                lista_materiales.append(material)
    except FileNotFoundError:
        return
    except json.JSONDecodeError:
        print()
    return lista_materiales


# Mostrar materiales en un Listbox
def cargar_y_mostrar_materiales_listbox(ventana, listbox_materiales):
    """
    Carga materiales desde un archivo y los muestra en un Listbox.

    Parámetros:
    ventana (Tk): Ventana de la aplicación.
    listbox_materiales (Listbox): Listbox donde se mostrarán los materiales.

    Retorna:
    Listbox: Listbox actualizado con los materiales cargados.
    """
    if listbox_materiales is None:
        listbox_materiales = tk.Listbox(ventana, height=12, width=70)
        listbox_materiales.place(x=400, y=115)
    else:
        listbox_materiales.delete(0, tk.END)

    lista_materiales = cargar_materiales("materiales.json")
    for material in lista_materiales:
        texto = f"Nombre: {material.nombre} - Unidad: {material.unidad} - Valor: {material.valor_unitario} - Estado: {'Activo' if material.estado else 'Inactivo'}"
        listbox_materiales.insert(tk.END, texto)
    return listbox_materiales


# Validación de entradas
def comprobaciones(entry_nombre, variable, entry_valor):
    """
    Realiza comprobaciones de validación para los datos de entrada de un material.

    Parámetros:
    entry_nombre (Entry): Entrada de texto con el nombre del material.
    variable (Variable): Variable de Tkinter que contiene la unidad seleccionada.
    entry_valor (Entry): Entrada de texto con el valor unitario del material.

    Excepciones:
    ValueError: Se lanza si alguna comprobación falla.
    """
    nombre = entry_nombre.get()
    valor_unitario = entry_valor.get()

    if not (5 <= len(nombre) <= 30):
        raise ValueError("El nombre debe tener entre 5 y 30 caracteres.")
    if not variable.get():
        raise ValueError("Debe seleccionar una unidad.")
    if not valor_unitario.replace('.', '', 1).isdigit():
        raise ValueError("El valor debe ser un número válido.")
    valor = float(valor_unitario)
    if not (0 <= valor <= 100000):
        raise ValueError("El valor debe estar entre 0 y 100,000.")



# Función para modificar materiales
def modificar_materiales(entry_nombre, variable, entry_valor, checkbox_var, text_descripcion, ventana, options, listbox_materiales):
    """
    Modifica la lista de materiales o agrega un nuevo material si no existe en la lista.

    Parámetros:
    entry_nombre, entry_valor (Entry): Entradas de texto con los datos del material.
    variable (Variable): Variable de Tkinter que contiene la unidad seleccionada.
    checkbox_var (BooleanVar): Variable de Tkinter que indica el estado del material.
    text_descripcion (Text): Campo de texto con la descripción del material.
    ventana (Tk): Ventana de la aplicación.
    options (list): Lista de opciones para el dropdown de unidades.
    listbox_materiales (Listbox): Listbox donde se mostrarán los materiales.

    Excepciones:
    ValueError: Se lanza si las comprobaciones de datos fallan.
    """
    try:
        comprobaciones(entry_nombre, variable, entry_valor)
        nuevo_material = Material(
            nombre=entry_nombre.get(),
            unidad=variable.get(),
            valor_unitario=entry_valor.get(),
            estado=checkbox_var.get(),
            descripcion=text_descripcion.get("1.0", tk.END)
        )

        lista_materiales = cargar_materiales("materiales.json")
        if nuevo_material not in lista_materiales:
            lista_materiales.append(nuevo_material)
            guardar_materiales(lista_materiales, "materiales.json")
            cargar_y_mostrar_materiales_listbox(ventana, listbox_materiales)

        else:
            messagebox.showwarning("Duplicado", "El material ya existe en la lista.")
    except ValueError as e:
        messagebox.showerror("Error de validación", str(e))

    return listbox_materiales


# Función para mostrar detalles del material seleccionado
def mostrar_datos_seleccionados(listbox_materiales):
    """
    Muestra los detalles de un material seleccionado de un Listbox en un mensaje de información.

    Parámetros:
    listbox_materiales (Listbox): Listbox de donde se selecciona el material.
    """

    seleccion = listbox_materiales.curselection()
    if len(seleccion) == 0:
        messagebox.showinfo("Error", "Por favor, seleccione un elemento de la lista.")
        return

    indice = seleccion[0]
    lista_materiales = cargar_materiales('materiales.json')
    Material = lista_materiales[indice]
    mensaje = f"{Material.__str__()}"
    messagebox.showinfo("Material", mensaje)


def cambiar_estado_listbox(ventana, listbox_materiales):
    """
    Cambia el estado de un material seleccionado en el Listbox.

    Parámetros:
    ventana (Tk): Ventana de la aplicación.
    listbox_materiales (Listbox): Listbox donde se muestran los materiales.
    """
    seleccion = listbox_materiales.curselection()
    if len(seleccion) == 0:
        messagebox.showinfo("Error", "Por favor, seleccione un elemento de la lista.")
        return

    indice = seleccion[0]
    lista_materiales = cargar_materiales("materiales.json")
    lista_materiales[indice].estado = not lista_materiales[indice].estado  # Cambiar el estado
    guardar_materiales(lista_materiales, "materiales.json")  # Guardar cambios
    cargar_y_mostrar_materiales_listbox(ventana, listbox_materiales)  # Actualizar la lista
