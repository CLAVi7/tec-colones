import sys
import os
import tkinter as tk
from cargar import cargar_json
import json

# Añadir el directorio 'Sedes_y_centros_de_acopio' al PATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Sedes_y_centros_de_acopio')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'crear_nuevo_material')))


from json_centro_acopio import cargar_centros
from carga_descarga_materiales import cargar_materiales
from clase_carrito import *

#from json_centro_acopio import cargar_centros
#from carga_descarga_materiales import cargar_materiales


#from Sedes_y_centros_de_acopio.json_centro_acopio import *
#from crear_nuevo_material.carga_descarga_materiales import *



def conseguir_centro():
    """
    Carga las sedes desde un archivo JSON y las retorna como una lista de nombres de sedes.

    Retorna:
    list: Lista de nombres de las sedes disponibles.
    """
    lista_centros = cargar_centros(os.path.join(os.path.dirname(__file__), '..', 'Sedes_y_centros_de_acopio', 'centros.json'))
    options = []
    for centro_de_acopio in lista_centros:
        options.append(centro_de_acopio.id)
    return options

def conseguir_materiales():
    """
    Carga los materiales desde un archivo JSON y los retorna como una lista de tuplas con nombres de materiales, su unidad y valor.

    Retorna:
    list: Lista de tuplas con nombres de materiales, su unidad y valor.
    """
    lista_materiales = cargar_materiales(os.path.join(os.path.dirname(__file__), '..', 'crear_nuevo_material', 'materiales.json'))
    options = []
    for material in lista_materiales:
        options.append((material.nombre, material.unidad, material.valor_unitario))
    return options


def guardar_carrito(lista_carrito, archivo):
    """
    Guarda una lista de sedes en un archivo JSON.

    Parámetros:
    sedes (list): Lista de objetos sedes para ser guardados.
    archivo (str): Ruta del archivo donde se guardarán los datos.
    """
    with open(archivo, 'w') as f:
        json.dump([carrito.to_dict() for carrito in lista_carrito], f, ensure_ascii=False, indent=4)

def cargar_carrito(archivo):
    """
    Carga centros de acopio desde un archivo JSON.

    Parámetros:
    archivo (str): Ruta del archivo JSON de donde se cargarán los centros.

    Retorna:
    list: Lista de objetos CentroDeAcopio cargados.
    """
    data = cargar_json(archivo)
    lista_carrito = []
    for item in data:
        carrito = Carrito(
            nombre=item['nombre'],
            cantidad=item['cantidad'],
            tec_colones=item['tec_colones']
        )
        lista_carrito.append(carrito)
    return lista_carrito


def comprobaciones(listbox_carrito, entry_cantidad, variable_materiales):
    return None

def modificar_carrito(listbox_carrito, entry_cantidad, variable_materiales):

    #Comprobaciones_resultado = comprobaciones(entry_ubicacion, entry_contacto, variable, entry_id)
    #if Comprobaciones_resultado:
    #    messagebox.showerror("Error de Comprobación", Comprobaciones_resultado)
    #    return

    opciones = variable_materiales.get()
    resultado = opciones.split(" - ")
    nombre_material = resultado[0]
    unidad = resultado[1]
    valor = resultado[2]

    nuevo_carrito = Carrito(nombre=nombre_material,
                              cantidad=entry_cantidad.get() + " " + unidad,
                              tec_colones=(float(valor)*float(entry_cantidad.get())))

    lista_carrito = cargar_carrito("carrito.json")

    if nuevo_carrito not in lista_carrito:
        lista_carrito.append(nuevo_carrito)
        guardar_carrito(lista_carrito, "carrito.json")
        listbox_carrito = cargar_y_mostrar_carrito_listbox(listbox_carrito)

    return listbox_carrito


def cargar_y_mostrar_carrito_listbox(listbox_carrito):
    # Vaciar el listbox antes de insertar nuevos elementos
    listbox_carrito.delete(0, tk.END)

    lista_carrito = cargar_carrito("carrito.json")

    for carrito in lista_carrito:
        texto = (f"Nombre: {carrito.nombre}"
                 f" - Cantidad: {carrito.cantidad}"
                 f" - Tec-colones: {carrito.tec_colones}")
        listbox_carrito.insert(tk.END, texto)

    return listbox_carrito


def suma_tec_colones():
    tec_colones_total = 0
    lista_carrito = cargar_carrito("carrito.json")

    for carrito in lista_carrito:
        tec_colones_total += carrito.tec_colones

    return tec_colones_total
    
    

