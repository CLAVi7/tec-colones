import tkinter as tk
from clase_recibo_centro import *


def cargar_y_mostrar_recibos(listbox, ruta_archivo):
    lista_recibos = cargar_json_desde_archivo(ruta_archivo)
    for recibo in lista_recibos:
        texto = (f"Fecha: {recibo.fecha} - Centro: {recibo.centro} - Funcionario: {recibo.funcionario} "
                 f"- Carnet: {recibo.carnet} - Material: {recibo.material} - Cantidad: {recibo.cantidad} "
                 f"- Tec-colones: {recibo.tec_colones}")
        listbox.insert(tk.END, texto)