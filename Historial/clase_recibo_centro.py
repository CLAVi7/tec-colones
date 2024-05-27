import json

class recibo_centro:
    def __init__(self, fecha, centro, funcionario, carnet, material, cantidad, tec_colones):
        self.fecha = fecha
        self.centro = centro
        self.funcionario = funcionario
        self.carnet = carnet
        self.material = material
        self.cantidad = cantidad
        self.tec_colones = tec_colones

    def to_dict(self):
        return {
            'fecha': self.fecha,
            'centro': self.centro,
            'funcionario': self.funcionario,
            'carnet': self.carnet,
            'material': self.material,
            'cantidad': self.cantidad,
            'tec_colones': self.tec_colones
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            fecha=data['fecha'],
            centro=data['centro'],
            funcionario=data['funcionario'],
            carnet=data['carnet'],
            material=data['material'],
            cantidad=data['cantidad'],
            tec_colones=data['tec_colones']
        )

def json_a_lista(json_str):
    data = json.loads(json_str)
    lista_recibos = [recibo_centro.from_dict(item) for item in data]
    return lista_recibos

def cargar_json_desde_archivo(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as file:
        json_str = file.read()
    return json_a_lista(json_str)

# Ruta del archivo JSON
ruta_archivo_json = 'Historial/recibos.json'

# Cargar JSON y convertirlo a lista de objetos recibo_centro
lista_recibos = cargar_json_desde_archivo(ruta_archivo_json)

# Imprimir los objetos para verificar
for recibo in lista_recibos:
    print(recibo.to_dict())

