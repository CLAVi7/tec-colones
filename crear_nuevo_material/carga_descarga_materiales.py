from Materiales import *
import json


#Función que guarda una lista de objetos de material en un archivo JSON.
def guardar_materiales(materiales, archivo):
    with open(archivo, 'w') as f:
        json.dump([material.to_dict() for material in materiales], f, ensure_ascii=False, indent=4)


#Carga la mediante una lista los materiales guardados desde el archivo JSON.
def cargar_materiales(archivo):
    lista_materiales = []
    try:
        with open(archivo, 'r') as f:
            data = json.load(f)
            for item in data:
                material = Material(
                    nombre=item['nombre'],
                    unidad=item['unidad'],
                    valor_unitario=item['valor_unitario'],
                    estado=item['estado'] == 'Activo',  # Convertir 'Activo'/'Inactivo' a booleano
                    descripcion=item['descripcion'] if 'descripcion' in item else None
                )
                material.fecha_creacion = datetime.strptime(item['fecha_creacion'], '%Y-%m-%d %H:%M:%S')
                material.id = item['id']
                lista_materiales.append(material)
    except FileNotFoundError:
        return
    except json.JSONDecodeError:
        print()
    return lista_materiales


