import json
import tkinter as tk
from tkinter import messagebox

def comprobaciones(entry_correo, entry_contrasena):

    correo = entry_correo.get()
    contrasena = entry_contrasena.get()
    
    if correo != "" and contrasena != "":
        if not correo.endswith('@tec.ac.cr'):
            messagebox.showerror("Error", "El correo no tiene @tec.ac.cr como dominio")
        elif not (6 <= len(contrasena) <= 12):
            messagebox.showerror("Error", "La contrasena debe tener entre 6 y 12 caracteres")
        elif not contrasena.isalnum():
            messagebox.showerror("Error", "La contrasena debe ser alfanumerica")
        else:

            # Abrimos el archivo JSON en modo de lectura
            with open('C:/Users/jmars/Documents/GitHub/tec-colones/base_de_datos/cuentas_usuarios.json', 'r') as archivo_json:
                # Cargamos el contenido del archivo JSON en una variable
                datos_json = json.load(archivo_json)

            for i in range(0, len(datos_json)):
                if datos_json[i]['correo'] == correo and datos_json[i]['contrasena'] == contrasena:
                    #Quitar el messagebox y hacer un redirect a la pagina correcta
                    messagebox.showinfo("Exito", "El correo y la contrasena son validos")
                    break
                else:
                    messagebox.showerror("Error", "El correo o la contrasena son invalidos")
                    break
    else:
        messagebox.showwarning("Error", "Campos vacíos")


def verificacion():
    try:
        comprobaciones()
    except ValueError as e:
        messagebox.showerror("Error", str(e))
