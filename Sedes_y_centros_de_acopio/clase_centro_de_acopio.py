from generador_id import generar_id_unico

class centro_de_acopio:
    def __init__(self, nombre, ubicacion, sede, numero_de_contacto, estado):
        self.id = generar_id_unico("C")
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.sede = sede
        self.numero_de_contacto = numero_de_contacto
        self.estado = estado

# Función que cambia el estado del material a activo o inactivo
    def cambioEstado(self):
        self.estado = not self.estado

#Retorna una representación en forma de cadena del material
    def __str__(self):
        return (f"ID:{self.id}\n"
                f"Centro_de acopio: {self.nombre}\n"
                f"Ubicacion: {self.ubicacion}\n"
                f"Sede: {self.sede}\n" #esto probablemente cambie a causa de no saber que es exactamente sede
                f"Numero de contacto: {self.numero_de_contacto}\n"
                f"Estado: {'Activo' if self.estado else 'Inactivo'}\n")

    #Convierte los atributos de los objetos en un diccionario
    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "ubicacion": self.ubicacion,
            "sede": self.sede,
            "estado": "Activo" if self.estado else "Inactivo",
            "numero_de_contacto": self.numero_de_contacto,
        }
