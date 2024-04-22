import random
from datetime import datetime
import json




class Material:
    def __init__(self, nombre, unidad, valor_unitario, estado, descripcion=None):
        self.id = self.generar_id_unico()
        self.nombre = nombre
        self.unidad = unidad
        self.valor_unitario = valor_unitario
        self.estado = estado
        self.fecha_creacion = datetime.now()
        self.descripcion = descripcion

    def generar_id_unico(self):
        caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        id_aleatorio = ''.join(random.choice(caracteres) for _ in range(12))
        return f"M-{id_aleatorio}"

    def __str__(self):
        return (f"ID: {self.id}\n"
                f"Material: {self.nombre}\n"
                f"Unidad: {self.unidad}\n"
                f"Valor Unitario: {self.valor_unitario} Tec-Colones\n"
                f"Estado: {'Activo' if self.estado else 'Inactivo'}\n"
                f"Fecha de Creación: {self.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"Descripción: {self.descripcion if self.descripcion else 'N/A'}")

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "unidad": self.unidad,
            "valor_unitario": self.valor_unitario,
            "estado": "Activo" if self.estado else "Inactivo",
            "fecha_creacion": self.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S'),
            "descripcion": self.descripcion if self.descripcion else "N/A"
        }

    def cambioEstado (self):
        self.estado = not self.estado


########################################################################################################################
def guardar_materiales(materiales, archivo):
    with open(archivo, 'w') as f:
        json.dump([material.to_dict() for material in materiales], f, ensure_ascii=False, indent=4)

lista_materiales = [Material("plastico", "kg", 500, True, "plastico:D")]


# Guardar la lista de materiales en un archivo JSON
guardar_materiales(lista_materiales, 'materiales.json')




