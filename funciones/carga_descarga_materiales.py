from funciones.Materiales import *
import json
import tkinter as tk
from tkinter import messagebox

ruta_carrito = "../base_de_datos/carrito.json"
ruta_centros = "../base_de_datos/centros.json"
ruta_historial_por_carnet = "../base_de_datos/historial_por_carnet.json"
ruta_historial_recibos = "../base_de_datos/historial_recibos.json"
ruta_materiales = "../base_de_datos/materiales.json"
ruta_sedes = "../base_de_datos/sedes.json"


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

    lista_materiales = cargar_materiales(ruta_materiales)
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

        lista_materiales = cargar_materiales(ruta_materiales)
        if nuevo_material not in lista_materiales:
            lista_materiales.append(nuevo_material)
            guardar_materiales(lista_materiales, ruta_materiales)
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
    lista_materiales = cargar_materiales(ruta_materiales)
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
    lista_materiales = cargar_materiales(ruta_materiales)
    lista_materiales[indice].estado = not lista_materiales[indice].estado  # Cambiar el estado
    guardar_materiales(lista_materiales, ruta_materiales)  # Guardar cambios
    cargar_y_mostrar_materiales_listbox(ventana, listbox_materiales)  # Actualizar la lista
