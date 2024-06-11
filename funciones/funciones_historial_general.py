import funciones.generador_id
from funciones.rutas import *
from funciones.clase_recibo import *
from funciones.funciones_cambio_material import *


def realizar_devolucion(id_recibo_original):
    fecha = datetime.today().date().isoformat()

    # Cargar historial de recibos
    historial = cargar_historial(ruta_historial_recibos)

    # Buscar el recibo original en el historial
    recibo_original = next((recibo for recibo in historial if recibo.id == id_recibo_original), None)
    if recibo_original is None:
        messagebox.showerror("Recibo original no encontrado en el historial")

    # Crear total para la devolución
    total = -recibo_original.total  # Negativo para la devolución
    carnet = recibo_original.carnet

    # Guardar en el historial
    id = generar_id_unico("D")
    nuevo_recibo = recibo_centro(id, fecha, recibo_original.centro, None, carnet, recibo_original.text, total)
    historial.append(nuevo_recibo)
    guardar_historial(historial, ruta_historial_recibos)

    # Guardar en el historial por carnet
    historial_por_carnet = cargar_historial_por_carnet(ruta_historial_por_carnet)

    if carnet in historial_por_carnet:
        historial_por_carnet[carnet].append(nuevo_recibo.to_dict())
    else:
        historial_por_carnet[carnet] = [nuevo_recibo.to_dict()]

    guardar_historial_por_carnet(historial_por_carnet, ruta_historial_por_carnet)
