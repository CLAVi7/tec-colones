class recibo_centro:
    """
    Representa un recibo de centro de acopio, con atributos para registrar la transacción.

    Atributos:
    fecha (str): Fecha de la transacción.
    centro (centro): Nombre del centro de acopio.
    funcionario (str): Nombre del funcionario encargado.
    carnet (int): Número de carnet del funcionario.
    material (material): Material recibido.
    cantidad (float): Cantidad de material recibido.
    tec_colones (float): Valor en tec colones del material recibido.
    """
    def __init__(self, id, fecha, centro, funcionario, carnet, material, tec_colones):
        """
        Inicializa un nuevo recibo de centro de acopio con los detalles proporcionados.

        Parámetros:
        fecha (str): Fecha de la transacción.
        centro (centro): Nombre del centro de acopio.
        funcionario (str): Nombre del funcionario encargado.
        carnet (int): Número de carnet del funcionario.
        material (material): Material recibido.
        tec_colones (float): Valor en tec colones del material recibido.
        """
        self.id = id
        self.fecha = fecha
        self.centro = centro
        self.funcionario = funcionario
        self.carnet = carnet
        self.material = material
        self.tec_colones = tec_colones

    def to_dict(self):
        """
        Convierte la instancia de recibo_centro en un diccionario.

        Retorna:
        dict: Un diccionario que contiene todos los atributos del recibo.
        """
        return {
            "id": self.id,
            "fecha": self.fecha,
            "centro": self.centro,
            "funcionario": self.funcionario,
            "carnet": self.carnet,
            "material": self.material,
            "tec_colones": self.tec_colones
        }
