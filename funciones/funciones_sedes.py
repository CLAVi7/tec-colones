from funciones.clase_sede import *
import json
import tkinter as tk
from tkinter import messagebox
from funciones.rutas import *


def guardar_sedes(sede, archivo):
    """
    Guarda una lista de sedes en un archivo JSON.

    Parámetros:
    sedes (list): Lista de objetos sedes para ser guardados.
    archivo (str): Ruta del archivo donde se guardarán los datos.
    """
    with open(archivo, 'w') as f:
        json.dump([sedes.to_dict() for sedes in sede], f, ensure_ascii=False, indent=4)


def cargar_sedes(archivo):
    """
    Carga sedes desde un archivo JSON y las retorna en una lista.

    Parámetros:
    archivo (str): Ruta del archivo JSON de donde se cargarán las sedes.

    Retorna:
    list: Lista de objetos sedes cargados desde el archivo.
    """
    lista_sedes = []
    try:
        with open(archivo, 'r') as f:
            data = json.load(f)
            for item in data:
                estado = item['estado']  # Guardar el estado leído del JSON
                if estado == 'Activo':
                    estado = True
                else:
                    estado = False
                sede = sedes(
                    nombre=item['nombre'],
                    provincia=item['provincia'],
                    numero_contacto=item['numero_contacto'],
                    estado=estado
                )
                sede.id = item['id']
                lista_sedes.append(sede)
    except FileNotFoundError:
        print("El archivo no fue encontrado.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON.")
    return lista_sedes


def cargar_y_mostrar_sedes_listbox(ventana, listbox_sedes):
    """
    Carga sedes desde un archivo y las muestra en un Listbox.

    Parámetros:
    ventana (Tk): Ventana de la aplicación.
    listbox_sedes (Listbox): Listbox donde se mostrarán las sedes.

    Retorna:
    Listbox: Listbox actualizado con las sedes cargadas.
    """
    if listbox_sedes is None:
        listbox_sedes = tk.Listbox(ventana, height=12, width=70)
        listbox_sedes.place(x=350, y=105)
    else:
        listbox_sedes.delete(0, tk.END)

    lista_sede = cargar_sedes(ruta_sedes)
    #print("La lista es: ", lista_sede[0])

    for sede in lista_sede:
        texto = (f"Nombre: {sede.nombre}"
                 f" - Ubicacion: {sede.provincia}"
                 f" - estado: {'Activo' if sede.estado else 'Inactivo'}")
        listbox_sedes.insert(tk.END, texto)

    return listbox_sedes


def comprobaciones(entry_nombre, variable, entry_contacto):
    """
    Realiza comprobaciones de validación para los datos de entrada de una sede.

    Parámetros:
    entry_nombre (Entry): Entrada de texto con el nombre de la sede.
    variable (Variable): Variable de Tkinter que contiene la provincia seleccionada.
    entry_contacto (Entry): Entrada de texto con el número de contacto.

    Excepciones:
    ValueError: Se lanza si alguna comprobación falla.
    """
    if not (5 <= len(entry_nombre.get()) <= 30):
        return "El nombre debe tener entre 5 y 30 caracteres."
    if not (1 <= len(variable.get())):
        return "Debe seleccionar una provincia para las sedes."
    
    contacto = entry_contacto.get()
    
    if not contacto.isdigit():
        return "El número de contacto debe ser un número entero."

    if len(contacto) != 8:
        return "El número de contacto debe tener exactamente 8 dígitos."


def Modificar_sedes(entry_nombre, variable, entry_contacto, checkbox_var, options, ventana, listbox_sedes):
    """
    Modifica la lista de sedes o agrega una nueva sede si no existe en la lista.

    Parámetros:
    entry_nombre, entry_contacto (Entry): Entradas de texto con los datos de la sede.
    variable (Variable): Variable de Tkinter que contiene la provincia seleccionada.
    checkbox_var (BooleanVar): Variable de Tkinter que indica el estado de la sede.
    options (list): Lista de opciones para el dropdown de provincias.
    ventana (Tk): Ventana de la aplicación.
    listbox_sedes (Listbox): Listbox donde se mostrarán las sedes.

    Excepciones:
    ValueError, TypeError: Se lanzan si las comprobaciones de datos o tipos fallan.
    """

    Comprobaciones = comprobaciones(entry_nombre, variable, entry_contacto)
    if Comprobaciones:
        messagebox.showerror("Error", Comprobaciones)
        return

    #print("Pasa por aqui")
    nuevo_sede = sedes(nombre=entry_nombre.get(),
                              provincia=variable.get(),
                              numero_contacto=entry_contacto.get(),
                              estado=checkbox_var.get())

    lista_sedes = cargar_sedes(ruta_sedes)
    if nuevo_sede not in lista_sedes:
        lista_sedes.append(nuevo_sede)
        guardar_sedes(lista_sedes, ruta_sedes)
        listbox_sedes = cargar_y_mostrar_sedes_listbox(ventana, listbox_sedes)

        entry_nombre.delete(0, tk.END)
        variable.set(options[0])
        entry_contacto.delete(0, tk.END)
        if not checkbox_var.get():
            checkbox_var.set(True)

    else:
        messagebox.showwarning("Duplicado", "la sede ya existe en la lista.")

    return listbox_sedes


# Función para mostrar detalles del material seleccionado
def mostrar_datos_seleccionados(listbox_sedes):
    """
    Muestra los detalles de una sede seleccionada de un Listbox en un mensaje de información.

    Parámetros:
    listbox_sedes (Listbox): Listbox de donde se selecciona la sede.
    """
    seleccion = listbox_sedes.curselection()
    if len(seleccion) == 0:
        messagebox.showinfo("Error", "Por favor, seleccione un elemento de la lista.")
        return

    indice = seleccion[0]
    lista_sedes = cargar_sedes(ruta_sedes)
    #print("lista_sedes:", lista_sedes[indice])
    sedes = lista_sedes[indice]
    #print("sedes: ", sedes)
    mensaje = f"{sedes.__str__()}"
    messagebox.showinfo("Sedes", mensaje)


def cambiar_estdo_listbox(ventana, listbox_sedes):
    """
    Cambia el estado de una sede seleccionada en el Listbox.

    Parámetros:
    ventana (Tk): Ventana de la aplicación.
    listbox_sedes (Listbox): Listbox donde se muestran las sedes.
    """
    seleccion = listbox_sedes.curselection()
    if len(seleccion) == 0:
        messagebox.showinfo("Error", "Por favor, seleccione un elemento de la lista.")
        return

    indice = seleccion[0]
    lista_sedes = cargar_sedes(ruta_sedes)
    lista_sedes[indice].estado = not lista_sedes[indice].estado
    guardar_sedes(lista_sedes, ruta_sedes)
    cargar_y_mostrar_sedes_listbox(ventana, listbox_sedes)
