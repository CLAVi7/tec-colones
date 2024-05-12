from clase_sedes import *
import json
import tkinter as tk
from tkinter import messagebox

def guardar_sedes(sedes, archivo):
    with open(archivo, 'w') as f:
        json.dump([sedes.to_dict() for sedes in sedes], f, ensure_ascii=False, indent=4)


def cargar_sedes(archivo):
    lista_sedes = []
    try:
        with open(archivo, 'r') as f:
            data = json.load(f)
            for item in data:
                estado = item['estado']  # Guardar el estado leído del JSON
                if estado == 'Activo':
                    estado = True
                else:
                    estado = False
                sede = sedes(
                    nombre=item['nombre'],
                    provincia=item['provincia'],
                    numero_contacto=item['numero_contacto'],
                    estado=estado
                )
                sede.id = item['id']
                lista_sedes.append(sede)
    except FileNotFoundError:
        print("El archivo no fue encontrado.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON.")
    return lista_sedes

listbox_sedes = None
def cargar_y_mostrar_sedes_listbox(ventana):
    global listbox_sedes

    if listbox_sedes is None:
        listbox_sedes = tk.Listbox(ventana, height=12, width=70)
        listbox_sedes.place(x=350, y=105)
    else:
        listbox_sedes.delete(0, tk.END)

    lista_sede = cargar_sedes("sedes.json")#Sedes_y_centros_de_acopio/sedes.json")
    #print("La lista es: ", lista_sede[0])

    for sede in lista_sede:
        texto = (f"Nombre: {sede.nombre}"
                 f" - Ubicacion: {sede.provincia}"
                 f" - estado: {'Activo' if sede.estado else 'Inactivo'}")
        listbox_sedes.insert(tk.END, texto)


def comprobaciones(entry_nombre, variable, entry_contacto):
    if not (5 <= len(entry_nombre.get()) <= 30):
        raise ValueError("El nombre debe tener entre 5 y 30 caracteres.")
    if not (1 <= len(variable.get())):
        raise ValueError("Debe seleccionar una provincia para las sedes.")
    
    contacto = entry_contacto.get()
    
    if not contacto.isdigit():
        raise ValueError("El número de contacto debe ser un número entero.")

    if len(contacto) != 8:
        raise ValueError("El número de contacto debe tener exactamente 8 dígitos.")



def Modificar_sedes(entry_nombre, variable, entry_contacto, checkbox_var, options, ventana):
    try:
        comprobaciones(entry_nombre, variable, entry_contacto)
        #print("Pasa por aqui")
        nuevo_sede = sedes(nombre=entry_nombre.get(),
                                  provincia=variable.get(),
                                  numero_contacto=entry_contacto.get(),
                                  estado=checkbox_var.get())

        lista_sedes = cargar_sedes("sedes.json")#Sedes_y_centros_de_acopio/sedes.json")
        if nuevo_sede not in lista_sedes:
            lista_sedes.append(nuevo_sede)
            guardar_sedes(lista_sedes, "sedes.json")#Sedes_y_centros_de_acopio/sedes.json")
            cargar_y_mostrar_sedes_listbox(ventana)

            entry_nombre.delete(0, tk.END)
            variable.set(options[0])
            entry_contacto.delete(0, tk.END)
            if not checkbox_var.get():
                checkbox_var.set(True)

        else:
            messagebox.showwarning("Duplicado", "la sede ya existe en la lista.")

    except ValueError as error:
        messagebox.showerror("Error de Comprobación", str(error))
    except TypeError as error:
        messagebox.showerror("Error de Tipo", str(error))


# Función para mostrar detalles del material seleccionado
def mostrar_datos_seleccionados():
    
    # Muestra los detalles del material seleccionado en la Listbox.
    
    seleccion = listbox_sedes.curselection()
    if len(seleccion) == 0:
        messagebox.showinfo("Error", "Por favor, seleccione un elemento de la lista.")
        return

    indice = seleccion[0]
    lista_sedes = cargar_sedes("sedes.json")#Sedes_y_centros_de_acopio/sedes.json")
    #print("lista_sedes:", lista_sedes[indice])
    sedes = lista_sedes[indice]
    #print("sedes: ", sedes)
    mensaje = f"{sedes.__str__()}"
    messagebox.showinfo("Sedes", mensaje)


def cambiar_estdo_listbox(ventana):
    # Cambia el estado del material seleccionado en la Listbox.
    seleccion = listbox_sedes.curselection()
    if len(seleccion) == 0:
        messagebox.showinfo("Error", "Por favor, seleccione un elemento de la lista.")
        return

    indice = seleccion[0]
    lista_sedes = cargar_sedes("sedes.json")#Sedes_y_centros_de_acopio/sedes.json")
    #print("lista_sedes:", lista_sedes[indice])
    lista_sedes[indice].estado = not lista_sedes[indice].estado
    #lista_sedes[indice].estado = sedes.cambioEstado(lista_sedes)
    #print("estado cambiado: ", lista_sedes[indice].estado)
    guardar_sedes(lista_sedes, "sedes.json")#Sedes_y_centros_de_acopio/sedes.json")
    cargar_y_mostrar_sedes_listbox(ventana)
