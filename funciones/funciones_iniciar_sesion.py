import json
import tkinter as tk
from tkinter import messagebox
from GUI.GUI_administrador import admin
from GUI.GUI_estudiante import estudiante
from GUI.GUI_funcionario import funcionario


ruta_usuarios = "../base_de_datos/cuentas_usuarios.json"


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
            with open(ruta_usuarios, 'r') as archivo_json:
                # Cargamos el contenido del archivo JSON en una variable
                datos_json = json.load(archivo_json)
                user = correo.split('@')[0]

            encontrado = False

            for i in range(len(datos_json)):
                if datos_json[i]['correo'] == correo and datos_json[i]['contrasena'] == contrasena:
                    encontrado = True
                    user = datos_json[i]['user']  # Asumiendo que hay un campo 'user' en tu JSON
                    break

            if encontrado:
                # Redirigir a la página correcta
                if user == "admin":
                    admin()
                elif user == "centro":
                    funcionario()
                else:
                    estudiante()
            else:
                messagebox.showerror("Error", "El correo o la contraseña son inválidos")

    else:
        messagebox.showwarning("Error", "Campos vacíos")

