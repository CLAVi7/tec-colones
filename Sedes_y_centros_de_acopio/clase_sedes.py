import tkinter as tk
from tkinter import ttk
import json
from generador_id import generar_id_unico

class sedes:
    def __init__(self, nombre, provincia, numero_contacto, estado):
        self.id = generar_id_unico("S")
        self.nombre = nombre
        self.provincia = provincia
        self.numero_contacto = numero_contacto
        self.estado = estado

    # Función que cambia el estado de la sede
    def cambioEstado(self):
        self.estado = not self.estado

    # Retorna una representación en forma de cadena de la sede
    def __str__(self):
        return (f"ID: {self.id}\n"
                f"Nombre de sede: {self.nombre}\n"
                f"Provincia: {self.provincia}\n"
                f"Numero de contacto: {self.numero_contacto}\n"
                f"Estado: {'Activo' if self.estado == 'Activo' else 'Inactivo'}\n")

    # #Convierte los atributos de los objetos en un diccionario
    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "provincia": self.provincia,
            "numero_contacto": self.numero_contacto,
            "estado": "Activo" if self.estado else "Inactivo",
        }

    @classmethod
    def cargar_sedes_desde_json(cls, ruta_json):
        with open(ruta_json, 'r') as file:
            datos = json.load(file)
            return datos

    @classmethod
    def cargar_sedes_en_optionmenu(cls, option_menu, ruta_json):
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
