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

# Crear la ventana principal
root = tk.Tk()
root.title("Verificador de Correo y Contraseña")

# Crear un marco para el contenido
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Etiqueta de instrucciones para el correo
label_correo = tk.Label(frame, text="Ingrese su correo electrónico:")
label_correo.pack(padx=5, pady=5)

# Campo de entrada para el correo electrónico
entry_correo = tk.Entry(frame, width=40)
entry_correo.pack(padx=5, pady=5)

# Etiqueta de instrucciones para la contraseña
label_contraseña = tk.Label(frame, text="Ingrese su contraseña:")
label_contraseña.pack(padx=5, pady=5)

# Campo de entrada para la contraseña
entry_contraseña = tk.Entry(frame, width=40)
entry_contraseña.pack(padx=5, pady=5)

# Botón para verificar el correo y la contraseña
button = tk.Button(frame, text="Verificar", command=verificacion)
button.pack(padx=5, pady=5)

# Ejecutar la aplicación
root.mainloop()
