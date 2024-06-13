import tkinter as tk
from tkinter import messagebox

def comprobaciones():
    correo = entry_correo.get()
    contraseña = entry_contraseña.get()
    
    if not correo.endswith('@xTec'):
        raise ValueError("El correo no tiene @xTec como dominio")
    if not (6 <= len(contraseña) <= 12):
        raise ValueError("La contraseña debe tener entre 6 y 12 caracteres")
    if not contraseña.isalnum():
        raise ValueError("La contraseña debe ser alfanumérica")
    messagebox.showinfo("Éxito", "El correo y la contraseña son válidos")
def verificacion():
    try:
        comprobaciones()
    except ValueError as e:
        messagebox.showerror("Error", str(e))
