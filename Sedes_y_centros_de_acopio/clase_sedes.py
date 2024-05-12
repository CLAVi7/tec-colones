import tkinter as tk
from tkinter import ttk
import json
from generador_id import generar_id_unico

class sedes:
    """
    Representa una sede con atributos para su identificación, ubicación y estado operativo.

    Atributos:
    id (str): Identificador único generado automáticamente para la sede.
    nombre (str): Nombre de la sede.
    provincia (str): Provincia donde se encuentra la sede.
    numero_contacto (str): Número de contacto de la sede.
    estado (bool): Estado operativo de la sede (Activo/Inactivo).
    """
    def __init__(self, nombre, provincia, numero_contacto, estado):
        """
        Inicializa una nueva sede con los detalles proporcionados y genera un identificador único.

        Parámetros:
        nombre (str): Nombre de la sede.
        provincia (str): Provincia donde se encuentra la sede.
        numero_contacto (str): Número de contacto de la sede.
        estado (bool): Estado inicial de la sede (Activo/Inactivo).
        """
        self.id = generar_id_unico("S")
        self.nombre = nombre
        self.provincia = provincia
        self.numero_contacto = numero_contacto
        self.estado = estado

    # Función que cambia el estado de la sede
    # def cambioEstado(self):
    #     self.estado = not self.estado

    # Retorna una representación en forma de cadena de la sede
    def __str__(self):
        """
        Devuelve una representación en forma de cadena de la información de la sede.

        Retorna:
        str: Cadena que representa a la sede con sus detalles.
        """
        return (f"ID: {self.id}\n"
                f"Nombre de sede: {self.nombre}\n"
                f"Provincia: {self.provincia}\n"
                f"Numero de contacto: {self.numero_contacto}\n"
                f"Estado: {'Activo' if self.estado else 'Inactivo'}\n")

    # #Convierte los atributos de los objetos en un diccionario
    def to_dict(self):
        """
        Convierte los atributos de la sede en un diccionario, adecuado para serialización.

        Retorna:
        dict: Diccionario que contiene los atributos de la sede.
        """
        return {
            "id": self.id,
            "nombre": self.nombre,
            "provincia": self.provincia,
            "numero_contacto": self.numero_contacto,
            "estado": "Activo" if self.estado else "Inactivo",
        }

    @classmethod
    def cargar_sedes_desde_json(cls, ruta_json):
        """
        Carga datos de sedes desde un archivo JSON y retorna una lista de estos datos.

        Parámetros:
        ruta_json (str): Ruta del archivo JSON desde donde se cargarán los datos de las sedes.

        Retorna:
        list: Lista de datos de sedes.
        """
        with open(ruta_json, 'r') as file:
            datos = json.load(file)
            return datos

    @classmethod
    def cargar_sedes_en_optionmenu(cls, option_menu, ruta_json):
        """
        Carga sedes desde un archivo JSON y las añade como opciones en un menú desplegable.

        Parámetros:
        option_menu (OptionMenu): Menú desplegable de Tkinter donde se añadirán las sedes.
        ruta_json (str): Ruta del archivo JSON desde donde se cargarán los datos de las sedes.
        """
        sedes = cls.cargar_sedes_desde_json(ruta_json)
        for sede in sedes:
            option_menu['menu'].add_command(label=sede["nombre"], 
                                             command=lambda value=sede["nombre"]: option_menu.config(text=value))

# # Ejemplo de uso
# import tkinter as tk

# ruta_json = "Sedes_y_centros_de_acopio/sedes.json"  # Ruta al archivo JSON
# root = tk.Tk()
# opcion_variable = tk.StringVar(root)
# opcion_variable.set("Seleccione una sede")

# option_menu = tk.OptionMenu(root, opcion_variable, "Seleccione una sede")
# option_menu.pack()

# sedes.cargar_sedes_en_optionmenu(option_menu, ruta_json)

# root.mainloop()
