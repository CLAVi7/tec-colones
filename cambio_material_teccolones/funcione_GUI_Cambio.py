import sys
import os

# Añadir el directorio 'Sedes_y_centros_de_acopio' al PATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Sedes_y_centros_de_acopio')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'crear_nuevo_material')))


from json_centro_acopio import cargar_centros
from carga_descarga_materiales import cargar_materiales

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
