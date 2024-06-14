from datetime import datetime
from funciones.generador_id import generar_id_unico


class Material:
    """
    Representa un material con atributos para su identificación, valoración y estado.

    Atributos:
    id (str): Identificador único generado automáticamente para el material.
    nombre (str): Nombre del material.
    unidad (str): Unidad de medida del material.
    valor_unitario (float): Valor unitario del material en Tec-Colones.
    estado (bool): Estado actual del material (Activo/Inactivo).
    fecha_creacion (datetime): Fecha y hora de creación del material.
    descripcion (str, opcional): Descripción adicional del material.
    """
    def __init__(self, nombre, unidad, valor_unitario, estado, descripcion=None):
        """
        Inicializa un nuevo material con los detalles proporcionados y genera un identificador único.

        Parámetros:
        nombre (str): Nombre del material.
        unidad (str): Unidad de medida del material.
        valor_unitario (float): Valor unitario del material en Tec-Colones.
        estado (bool): Estado inicial del material (Activo/Inactivo).
        descripcion (str, opcional): Descripción adicional del material.
        """
        self.id = generar_id_unico("M")
        self.nombre = nombre
        self.unidad = unidad
        self.valor_unitario = valor_unitario
        self.estado = estado
        self.fecha_creacion = datetime.now()
        self.descripcion = descripcion


    #Retorna una representación en forma de cadena del material
    def __str__(self):
        """
        Devuelve una representación en forma de cadena de la información del material.

        Retorna:
        str: Cadena que representa al material con sus detalles.
        """
        return (f"ID: {self.id}\n"
                f"Material: {self.nombre}\n"
                f"Unidad: {self.unidad}\n"
                f"Valor Unitario: {self.valor_unitario} Tec-Colones\n"
                f"Estado: {'Activo' if self.estado else 'Inactivo'}\n"
                f"Fecha de Creación: {self.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"Descripción: {self.descripcion if self.descripcion else 'N/A'}")


    #Convierte los atributos de los objetos en un diccionario
    def to_dict(self):
        """
        Convierte los atributos del material en un diccionario, adecuado para serialización.

        Retorna:
        dict: Diccionario que contiene los atributos del material.
        """
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
        """
        Cambia el estado del material de Activo a Inactivo o viceversa.
        """
        self.estado = not self.estado
