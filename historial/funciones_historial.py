from clase_recibo import *
import json
from cargar import cargar_json
from datetime import datetime
from cambio_material_teccolones.funcione_GUI_Cambio import cargar_carrito
import generador_id

def guardar_historial(historial, archivo):
    """
    Guarda una lista de recibos en un archivo JSON.

    Parámetros:
    historial (list): Lista de objetos recibo_centro.
    archivo (str): Ruta del archivo donde se guardarán el historial.
    """
    with open(archivo, 'w') as f:
        json.dump([recibo.to_dict() for recibo in historial], f, ensure_ascii=False, indent=4)

def cargar_historial(archivo):
    """
    Carga el historial desde un archivo JSON.

    Parámetros:
    archivo (str): Ruta del archivo JSON de donde se cargarán el historial.

    Retorna:
    list: Lista de objetos recibo_centro cargados.
    """
    data = cargar_json(archivo)
    historial = []
    for item in data:
        recibo = recibo_centro(
            id=item["id"],
            fecha=item['fecha'],
            centro=item['centro'],
            funcionario=item['funcionario'],
            carnet=item['carnet'],
            material=item['material'],
            tec_colones=item["tec_colones"]
        )
        historial.append(recibo)
    return historial

def realizar_transaccion(variable_centros, carnet):
    fecha = datetime.today().date().isoformat()
    lista_carrito = cargar_carrito("carrito.json")
    text = ""
    for item in lista_carrito:
        text = text + item.cantidad + " de " + item.nombre + ", "

    total = suma_tec_colones()

    id = generador_id("R-")

    nuevo_recibo = recibo_centro(id, fecha, variable_centros, None, carnet, text, total)
    historial = cargar_historial(os.path.join(os.path.dirname(__file__), "..", "historial", "historial_recibos.json"))
    historial.append(nuevo_recibo)
    guardar_historial(historial, os.path.join(os.path.dirname(__file__), "..", "historial", "historial_recibos.json"))