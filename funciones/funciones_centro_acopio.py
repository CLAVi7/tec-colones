from funciones.clase_centro_de_acopio import *
import json
import tkinter as tk
from tkinter import messagebox
from funciones.funciones_sedes import cargar_sedes
from funciones.rutas import *


def guardar_centros(centros, archivo):
    """
    Guarda una lista de centros de acopio en un archivo JSON.

    Parámetros:
    centros (list): Lista de objetos CentroDeAcopio.
    archivo (str): Ruta del archivo donde se guardarán los centros.
    """
    with open(archivo, 'w') as f:
        json.dump([centro.to_dict() for centro in centros], f, ensure_ascii=False, indent=4)


def cargar_centros(archivo):
    """
    Carga centros de acopio desde un archivo JSON.

    Parámetros:
    archivo (str): Ruta del archivo JSON de donde se cargarán los centros.

    Retorna:
    list: Lista de objetos CentroDeAcopio cargados.
    """
    lista_centros = []
    try:
        with open(archivo, 'r') as f:
            data = json.load(f)
            for item in data:
                centro = centro_de_acopio(
                    ubicacion=item['ubicacion'],
                    sede=item['sede'],
                    numero_de_contacto=item['numero_de_contacto'],
                    estado=item['estado'] == 'Activo',
                    id=item["id"]
                )
                lista_centros.append(centro)
    except FileNotFoundError:
        return lista_centros
    except json.JSONDecodeError:
        return lista_centros
    return lista_centros


def cargar_y_mostrar_centros_listbox(ventana, listbox_centros):
    """
    Carga centros de acopio desde un archivo y los muestra en un Listbox.

    Parámetros:
    ventana (Tk): Ventana de la aplicación.
    listbox_centros (Listbox): Listbox donde se mostrarán los centros.

    Retorna:
    Listbox: Listbox actualizado con los centros cargados.
    """
    if listbox_centros is None:
        listbox_centros = tk.Listbox(ventana, height=12, width=70)
        listbox_centros.place(x=350, y=105)
    else:
        listbox_centros.delete(0, tk.END)

    lista_centros = cargar_centros(ruta_centros)
    if not lista_centros:
        print("No se cargaron centros. Verifique el archivo JSON.")

    for centro in lista_centros:
        texto = (f"ID: {centro.id}"
                 f" - Sede: {centro.sede}"
                 f" - Estado: {'Activo' if centro.estado else 'Inactivo'}")
        listbox_centros.insert(tk.END, texto)

    return listbox_centros


def comprobaciones( entry_ubicacion, entry_contacto, variable, entry_id):
    """
     Realiza comprobaciones de validación para los datos de entrada de un centro de acopio.

     Parámetros:
     entry_nombre, entry_ubicacion, entry_contacto (Entry): Entradas de texto con los datos del centro.
     variable (Variable): Variable de Tkinter que contiene la sede seleccionada.
     entry_id (Entry): Entrada de texto con el ID del centro.

     Excepciones:
     ValueError: Se lanza si alguna comprobación falla.
     """

    if not (1 <= len(entry_ubicacion.get()) <= 100):
        return"El ubicacion debe tener máximo 100 caracteres."
    if not (len(entry_contacto.get()) == 8):
        return"El numero debe ser de 8 caracteres."
    if not (1 <= len(variable.get())):
        return"Debe ingresar un valor para las sedes."
    if not (len(entry_id.get()) == 12):
        return "El id es un codigo alfanumerico de 12 caracteres"



def Modificar_centros(entry_ubicacion, variable, entry_contacto, checkbox_var, ventana, listbox_centros, entry_id):
    """
    Modifica la lista de centros de acopio o agrega un nuevo centro si no existe en la lista.

    Parámetros:
    entry_nombre, entry_ubicacion, entry_contacto, entry_id (Entry): Entradas de texto con los datos del centro.
    variable (Variable): Variable de Tkinter que contiene la sede seleccionada.
    checkbox_var (BooleanVar): Variable de Tkinter que indica el estado del centro.
    ventana (Tk): Ventana de la aplicación.
    listbox_centros (Listbox): Listbox donde se mostrarán los centros.
    options (list): Lista de opciones para el dropdown de sedes.

    Excepciones:
    ValueError, TypeError: Se lanza si las comprobaciones de datos o tipos fallan.
    """
    Comprobaciones = comprobaciones( entry_ubicacion, entry_contacto, variable, entry_id)
    if Comprobaciones:
        messagebox.showinfo("Error", Comprobaciones)
        return

    nuevo_centro = centro_de_acopio(
                              ubicacion=entry_ubicacion.get(),
                              sede=variable.get(),
                              numero_de_contacto=entry_contacto.get(),
                              estado=checkbox_var.get(),
                              id="C-" + entry_id.get())

    lista_centros = cargar_centros(ruta_centros)
    if not any(centro.id == nuevo_centro.id for centro in lista_centros):
        lista_centros.append(nuevo_centro)
        guardar_centros(lista_centros, ruta_centros)
        cargar_y_mostrar_centros_listbox(ventana, listbox_centros)

    else:
        messagebox.showwarning("Duplicado", "El centro ya existe en la lista.")


def mostrar_datos_seleccionados(listbox_centros):
    """
    Muestra los detalles de un centro de acopio seleccionado de un Listbox en un mensaje de información.

    Parámetros:
    listbox_centros (Listbox): Listbox de donde se selecciona el centro.
    """

    seleccion = listbox_centros.curselection()
    if len(seleccion) == 0:
        messagebox.showinfo("Error", "Por favor, seleccione un centro de la lista.")
        return

    indice = seleccion[0]
    lista_centros = cargar_centros(ruta_centros)
    centro = lista_centros[indice]
    mensaje = f"{centro.__str__()}"
    messagebox.showinfo("Centro", mensaje)


def cambiar_estdo_listbox(ventana, listbox_centros):
    """
    Cambia el estado de un centro de acopio seleccionado en el Listbox.

    Parámetros:
    ventana (Tk): Ventana de la aplicación.
    listbox_centros (Listbox): Listbox donde se muestran los centros.
    """
    # Cambia el estado del material seleccionado en la Listbox.
    seleccion = listbox_centros.curselection()
    if len(seleccion) == 0:
        messagebox.showinfo("Error", "Por favor, seleccione un elemento de la lista.")
        return

    indice = seleccion[0]
    lista_centros = cargar_centros(ruta_centros)
    lista_centros[indice].estado = not lista_centros[indice].estado
    guardar_centros(lista_centros, ruta_centros)
    cargar_y_mostrar_centros_listbox(ventana, listbox_centros)


def conseguir_sedes():
    """
    Carga las sedes desde un archivo JSON y las retorna como una lista de nombres de sedes.

    Retorna:
    list: Lista de nombres de las sedes disponibles.
    """
    lista_sedes = cargar_sedes(ruta_sedes)
    options = []
    for sede in lista_sedes:
        options.append(sede.nombre)
    return options
