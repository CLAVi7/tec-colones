

class Carrito:
    """
    Representa un centro de acopio, con atributos para su identificación y operación.

    Atributos:
    id (str): Identificador único del centro de acopio.
    ubicacion (str): Ubicación geográfica del centro.
    sede (str): Sede asociada al centro de acopio.
    numero_de_contacto (str): Número de teléfono de contacto.
    estado (bool): Estado operativo del centro (Activo/Inactivo).
    """
    def __init__(self, nombre, cantidad, tec_colones):
        """
        Inicializa un nuevo centro de acopio con los detalles proporcionados.

        Parámetros:
        ubicacion (str): Ubicación geográfica del centro.
        sede (str): Sede asociada al centro de acopio.
        numero_de_contacto (str): Número de teléfono de contacto.
        """

        self.nombre = nombre
        self.cantidad = cantidad
        self.tec_colones = tec_colones

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "tec_colones": self.tec_colones
        }
