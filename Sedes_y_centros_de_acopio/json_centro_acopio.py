from clase_centro_de_acopio import *
import json


def guardar_centros(centros, archivo):
    with open(archivo, 'w') as f:
        json.dump([centro.to_dict() for centro in centros], f, ensure_ascii=False, indent=4)


def cargar_centros(archivo):
    lista_centros = []
    try:
        with open(archivo, 'r') as f:
            data = json.load(f)
            for item in data:
                centro = centro_de_acopio(
                    nombre=item['nombre'],
                    ubicacion=item['ubicacion'],
                    sede=item['sede'],
                    numero_de_contacto=item['numero_de_contacto'],
                    estado=item['estado'] == 'Activo'
                )
                centro.id = item['id']
                lista_centros.append(centro)
    except FileNotFoundError:
        return lista_centros
    except json.JSONDecodeError:
        return lista_centros
    return lista_centros


