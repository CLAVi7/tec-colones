import random

# Función que crea un ID único compuesto por 12 caracteres despues de M-
def generar_id_unico(lugar):
    """
    Genera un identificador único combinando un prefijo con una cadena aleatoria de caracteres alfanuméricos.

    Parámetros:
    lugar (str): Prefijo que indica el tipo de objeto para el cual se genera el ID (por ejemplo, 'M' para materiales, 'S' para sedes).

    Retorna:
    str: Un identificador único en el formato 'prefijo-cadena_aleatoria'.
    """
    caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    id_aleatorio = ''.join(random.choice(caracteres) for _ in range(12))
    return f"{lugar}-{id_aleatorio}"
