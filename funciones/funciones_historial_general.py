import funciones.generador_id
from funciones.rutas import *
from funciones.clase_recibo import *
from funciones.funciones_cambio_material import *
from funciones.funciones_historial import *


def realizar_devolucion(id_recibo_original, ventana, listbox_historial):
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

    messagebox.showinfo("Devolución exitosa",
                        "La transacción de devolución fue exitosa. Por favor, recargue la página.")


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

    button_anular = tk.Button(dialog, text="Anular", command=lambda: [realizar_devolucion(recibo.id, ventana, listbox_historial), dialog.destroy()])
    button_anular.pack(side=tk.RIGHT, padx=10, pady=10)

    dialog.transient(ventana)  # Para que la ventana sea modal
    dialog.grab_set()  # Para que se quede en primer plano
    ventana.wait_window(dialog)  # Espera hasta que la ventana se cierre


def cargar_y_mostrar_historial_listbox_general(ventana, listbox_historial):
    """
    Carga historial desde un archivo y los muestra en un Listbox.

    Parámetros:
    ventana (Tk): Ventana de la aplicación.
    listbox_historial (Listbox): Listbox donde se mostrarán el historial.

    Retorna:
    Listbox: Listbox actualizado con el historial.
    """
    if listbox_historial is None:
        listbox_historial = tk.Listbox(ventana, height=12, width=120)
        listbox_historial.place(x=40, y=130)
    else:
        listbox_historial.delete(0, tk.END)  # Limpiar el listbox antes de agregar los elementos filtrados

    lista_historial = cargar_historial(ruta_historial_recibos)
    if not lista_historial:
        print("No se cargó el historial. Verifique el archivo JSON.")

    for historial in lista_historial:
        texto = (
            f"Fecha: {historial.fecha}"
            f" - Id: {historial.id}"
            f" - Carnet: {historial.carnet}"
            f" - Materiales: {historial.material}"
            f" - Monto: {historial.tec_colones}")
        listbox_historial.insert(tk.END, texto)

    return listbox_historial