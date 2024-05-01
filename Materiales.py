import random
from datetime import datetime


class Material:
#Función que crea un nuevo material con los parámetros de la clase
    def __init__(self, nombre, unidad, valor_unitario, estado, descripcion=None):
        self.id = self.generar_id_unico()
        self.nombre = nombre
        self.unidad = unidad
        self.valor_unitario = valor_unitario
        self.estado = estado
        self.fecha_creacion = datetime.now()
        self.descripcion = descripcion

    @staticmethod
#Función que crea un ID único compuesto por 12 caracteres despues de M-
    def generar_id_unico():
        caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        id_aleatorio = ''.join(random.choice(caracteres) for _ in range(12))
        return f"M-{id_aleatorio}"


#Retorna una representación en forma de cadena del material
    def __str__(self):
        return (f"ID: {self.id}\n"
                f"Material: {self.nombre}\n"
                f"Unidad: {self.unidad}\n"
                f"Valor Unitario: {self.valor_unitario} Tec-Colones\n"
                f"Estado: {'Activo' if self.estado else 'Inactivo'}\n"
                f"Fecha de Creación: {self.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"Descripción: {self.descripcion if self.descripcion else 'N/A'}")

#Convierte los atributos de los objetos en un diccionario
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

# Función que cambia el estado del material a activo o inactivo
    def cambioEstado(self):
        self.estado = not self.estado
