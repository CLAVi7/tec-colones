import funciones.generador_id
from funciones.rutas import *
from funciones.clase_recibo import *
from funciones.funciones_cambio_material import *
from funciones.funciones_historial import *


def realizar_devolucion(id_recibo_original, ventana):
    fecha = datetime.today().date().isoformat()

    # Cargar historial de recibos
    historial = cargar_historial(ruta_historial_recibos)

    # Buscar el recibo original en el historial
    recibo_original = next((recibo for recibo in historial if recibo.id == id_recibo_original), None)
    if recibo_original is None:
        messagebox.showerror("Recibo original no encontrado en el historial")

    # Crear total para la devolución
    total = -recibo_original.tec_colones  # Negativo para la devolución
    carnet = recibo_original.carnet

    # Guardar en el historial
    id = generar_id_unico("A")
    nuevo_recibo = recibo_centro(id, fecha, recibo_original.centro, None, carnet, recibo_original.material, total)
    historial.append(nuevo_recibo)
    guardar_historial(historial, ruta_historial_recibos)

    # Guardar en el historial por carnet
    historial_por_carnet = cargar_historial_por_carnet(ruta_historial_por_carnet)

    if carnet in historial_por_carnet:
        historial_por_carnet[carnet].append(nuevo_recibo.to_dict())
    else:
        historial_por_carnet[carnet] = [nuevo_recibo.to_dict()]

    guardar_historial_por_carnet(historial_por_carnet, ruta_historial_por_carnet)

    cargar_y_mostrar_historial_listbox(ventana, listbox_historial)


def mostrar_dato_listbox_A(listbox_historial, ventana):
    seleccion = listbox_historial.curselection()
    if len(seleccion) == 0:
        messagebox.showinfo("Error", "Por favor, seleccione un elemento de la lista.")
        return

    indice = seleccion[0]
    lista_historial = cargar_historial(ruta_historial_recibos)
    recibo = lista_historial[indice]
    mensaje = f"{recibo.__str__()}"

    dialog = tk.Toplevel()
    dialog.title("Recibo")

    label = tk.Label(dialog, text=mensaje, justify=tk.LEFT)
    label.pack(padx=20, pady=10)

    button_aceptar = tk.Button(dialog, text="Aceptar", command=dialog.destroy)
    button_aceptar.pack(side=tk.LEFT, padx=10, pady=10)

    button_anular = tk.Button(dialog, text="Anular", command=lambda: [realizar_devolucion(recibo.id, ventana), dialog.destroy()])
    button_anular.pack(side=tk.RIGHT, padx=10, pady=10)

    dialog.transient(ventana)  # Para que la ventana sea modal
    dialog.grab_set()  # Para que se quede en primer plano
    ventana.wait_window(dialog)  # Espera hasta que la ventana se cierre
