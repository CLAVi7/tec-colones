import random

# Función que crea un ID único compuesto por 12 caracteres despues de M-
def generar_id_unico(lugar):
    caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    id_aleatorio = ''.join(random.choice(caracteres) for _ in range(12))
    return f"{lugar}-{id_aleatorio}"
