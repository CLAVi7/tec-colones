import json
def cargar_json(archivo):
    """
    Carga datos desde un archivo JSON y los retorna como una lista de diccionarios.

    Parámetros:
    archivo (str): Ruta del archivo JSON de donde se cargarán los datos.

    Retorna:
    list: Lista de diccionarios cargados desde el archivo.
    """
    try:
        with open(archivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("El archivo no fue encontrado.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON.")
    return []