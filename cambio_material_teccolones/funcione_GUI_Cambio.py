import sys
import os

# Añadir el directorio 'Sedes_y_centros_de_acopio' al PATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Sedes_y_centros_de_acopio')))

from json_centro_acopio import cargar_centros

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
