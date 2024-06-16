import requests
import json
from tkinter import messagebox


# Función que valida un carnet y devuelve un objeto JSON con la información del carnet
def validarCarnet(entry_carnet):
    # Creamos una cadena que contiene el JSON con la información del carnet
    datos = f'{{"carnet": "{entry_carnet}"}}'
    # Convertimos la cadena a un objeto JSON real utilizando json.loads()
    return json.loads(datos)


# Función que obtiene la respuesta de la API con la validación del carnet
def obtenerRespuesta(entry_carnet):
    # Llamamos a la función validarCarnet para obtener el objeto JSON con la información del carnet
    data = validarCarnet(entry_carnet)
    print("data", data)  # Imprimimos el objeto JSON para debugging

    # Realizamos la solicitud GET a la API con el objeto JSON como parámetro
    response = requests.get("https://cuentatec.azurewebsites.net/api/StudentValidator", json=data)

    # Obtenemos el cuerpo de la respuesta como un objeto JSON
    response_data = response.json()
    # Extraemos el código de respuesta y el mensaje del objeto JSON
    response_code = response_data['responseCode']
    message = response_data['message']
    respuestas = [response_code, message]

    return respuestas



# 2003200310
#obtenerRespuesta(2003200310)