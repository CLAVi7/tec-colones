

class centro_de_acopio:
    """
    Representa un centro de acopio, con atributos para su identificación y operación.

    Atributos:
    id (str): Identificador único del centro de acopio.
    ubicacion (str): Ubicación geográfica del centro.
    sede (str): Sede asociada al centro de acopio.
    numero_de_contacto (str): Número de teléfono de contacto.
    estado (bool): Estado operativo del centro (Activo/Inactivo).
    """
    def __init__(self, ubicacion, sede, numero_de_contacto, estado, id):
        """
        Inicializa un nuevo centro de acopio con los detalles proporcionados.

        Parámetros:
        ubicacion (str): Ubicación geográfica del centro.
        sede (str): Sede asociada al centro de acopio.
        numero_de_contacto (str): Número de teléfono de contacto.
        estado (bool): Estado operativo del centro (Activo/Inactivo).
        id (str): Identificador único del centro de acopio.
        """

        self.id = id
        self.ubicacion = ubicacion
        self.sede = sede
        self.numero_de_contacto = numero_de_contacto
        self.estado = estado

# Función que cambia el estado del material a activo o inactivo
    def cambioEstado(self):
        """
        Cambia el estado operativo del centro de acopio de Activo a Inactivo o viceversa.
        """
        self.estado = not self.estado

#Retorna una representación en forma de cadena del material
    def __str__(self):
        """
        Devuelve una representación en forma de cadena de la información del centro de acopio.

        Retorna:
        str: Cadena que representa al centro de acopio con sus detalles.
        """
        return (f"ID:{self.id}\n"
                f"Ubicacion: {self.ubicacion}\n"
                f"Sede: {self.sede}\n" #esto probablemente cambie a causa de no saber que es exactamente sede
                f"Numero de contacto: {self.numero_de_contacto}\n"
                f"Estado: {'Activo' if self.estado else 'Inactivo'}\n")

    #Convierte los atributos de los objetos en un diccionario
    def to_dict(self):
        """
        Convierte los atributos del centro de acopio en un diccionario, adecuado para serialización.

        Retorna:
        dict: Diccionario que contiene los atributos del centro de acopio.
        """
        return {
            "id": self.id,
            "ubicacion": self.ubicacion,
            "sede": self.sede,
            "estado": "Activo" if self.estado else "Inactivo",
            "numero_de_contacto": self.numero_de_contacto,
        }
