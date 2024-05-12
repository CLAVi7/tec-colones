from Materiales import *
import json
import tkinter as tk
from tkinter import messagebox


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


# Mostrar materiales en un Listbox
def cargar_y_mostrar_materiales_listbox(ventana, listbox_materiales):
    if listbox_materiales is None:
        listbox_materiales = tk.Listbox(ventana, height=12, width=70)
        listbox_materiales.place(x=400, y=115)
    else:
        listbox_materiales.delete(0, tk.END)

    lista_materiales = cargar_materiales("materiales.json")
    for material in lista_materiales:
        texto = f"Nombre: {material.nombre} - Unidad: {material.unidad} - Valor: {material.valor_unitario} - Estado: {'Activo' if material.estado else 'Inactivo'}"
        listbox_materiales.insert(tk.END, texto)
    return listbox_materiales


# Validación de entradas
def comprobaciones(entry_nombre, variable, entry_valor):
    if not (5 <= len(entry_nombre.get()) <= 30):
        raise ValueError("El nombre debe tener entre 5 y 30 caracteres.")
    if not variable.get():
        raise ValueError("Debe seleccionar una unidad.")
    try:
        valor = float(entry_valor.get())
        if not (0 <= valor <= 100000):
            raise ValueError("El valor debe estar entre 0 y 100,000.")
    except ValueError:
        raise ValueError("El valor debe ser un número válido.")


# Función para modificar materiales
def modificar_materiales(entry_nombre, variable, entry_valor, checkbox_var, text_descripcion, ventana, options, listbox_materiales):
    try:
        comprobaciones(entry_nombre, variable, entry_valor)
        nuevo_material = Material(
            nombre=entry_nombre.get(),
            unidad=variable.get(),
            valor_unitario=entry_valor.get(),
            estado=checkbox_var.get(),
            descripcion=text_descripcion.get("1.0", tk.END)
        )

        lista_materiales = cargar_materiales("materiales.json")
        if nuevo_material not in lista_materiales:
            lista_materiales.append(nuevo_material)
            guardar_materiales(lista_materiales, "materiales.json")
            cargar_y_mostrar_materiales_listbox(ventana, listbox_materiales)

            entry_nombre.delete(0, tk.END)
            variable.set(options[0])
            entry_valor.delete(0, tk.END)
            text_descripcion.delete("1.0", tk.END)
            if not checkbox_var.get():
                checkbox_var.set(True)

        else:
            messagebox.showwarning("Duplicado", "El material ya existe en la lista.")
    except ValueError as e:
        messagebox.showerror("Error de validación", str(e))

    return listbox_materiales


# Función para mostrar detalles del material seleccionado
def mostrar_datos_seleccionados(listbox_materiales):
    # Muestra los detalles del material seleccionado en la Listbox.

    seleccion = listbox_materiales.curselection()
    if len(seleccion) == 0:
        messagebox.showinfo("Error", "Por favor, seleccione un elemento de la lista.")
        return

    indice = seleccion[0]
    lista_materiales = cargar_materiales('materiales.json')
    Material = lista_materiales[indice]
    mensaje = f"{Material.__str__()}"
    messagebox.showinfo("Material", mensaje)


def cambiar_estado_listbox(ventana, listbox_materiales):
    seleccion = listbox_materiales.curselection()
    if len(seleccion) == 0:
        messagebox.showinfo("Error", "Por favor, seleccione un elemento de la lista.")
        return

    indice = seleccion[0]
    lista_materiales = cargar_materiales("materiales.json")
    lista_materiales[indice].estado = not lista_materiales[indice].estado  # Cambiar el estado
    guardar_materiales(lista_materiales, "materiales.json")  # Guardar cambios
    cargar_y_mostrar_materiales_listbox(ventana, listbox_materiales)  # Actualizar la lista