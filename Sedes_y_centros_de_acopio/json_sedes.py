from clase_sedes import *
import json


def guardar_sedes(sedes, archivo):
    with open(archivo, 'w') as f:
        json.dump([sedes.to_dict() for sedes in sedes], f, ensure_ascii=False, indent=4)


def cargar_sedes(archivo):
    lista_sedes = []
    try:
        with open(archivo, 'r') as f:
            data = json.load(f)
            for item in data:
                sede = sedes(
                    nombre=item['nombre'],
                    provincia=item['provincia'],
                    numero_contacto=item['numero_contacto'],
                    estado=item['estado'] == 'Activo'
                )
                sede.id = item['id']
                lista_sedes.append(sede)
    except FileNotFoundError:
        return lista_sedes
    except json.JSONDecodeError:
        return lista_sedes
    return lista_sedes