from clase_recibo import *
import json
from cargar import cargar_json
from datetime import datetime
from cambio_material_teccolones.funcione_GUI_Cambio import *
import generador_id
import random



def guardar_historial(historial, archivo):
    """
    Guarda una lista de recibos en un archivo JSON.

    Parámetros:
    historial (list): Lista de objetos recibo_centro.
    archivo (str): Ruta del archivo donde se guardarán el historial.
    """
    with open(archivo, 'w') as f:
        json.dump([recibo.to_dict() for recibo in historial], f, ensure_ascii=False, indent=4)

def cargar_historial(archivo):
    """
    Carga el historial desde un archivo JSON.

    Parámetros:
    archivo (str): Ruta del archivo JSON de donde se cargarán el historial.

    Retorna:
    list: Lista de objetos recibo_centro cargados.
    """
    data = cargar_json(archivo)
    historial = []
    for item in data:
        recibo = recibo_centro(
            id=item["id"],
            fecha=item['fecha'],
            centro=item['centro'],
            funcionario=item['funcionario'],
            carnet=item['carnet'],
            material=item['material'],
            tec_colones=item["tec_colones"]
        )
        historial.append(recibo)
    return historial

def cargar_y_mostrar_historial_listbox(ventana, listbox_historial):
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
        listbox_historial.delete(0, tk.END)

    lista_historial = cargar_historial("historial_recibos.json")
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


def realizar_transaccion(variable_centros, carnet):
    fecha = datetime.today().date().isoformat()
    lista_carrito = cargar_carrito("carrito.json")
    text = ""
    for item in lista_carrito:
        text = text + item.cantidad + " de " + item.nombre + ", "

    total = suma_tec_colones()

    caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    id_aleatorio = ''.join(random.choice(caracteres) for _ in range(12))
    id = "R-" + id_aleatorio

    nuevo_recibo = recibo_centro(id, fecha, variable_centros, None, carnet, text, total)
    historial = cargar_historial(os.path.join(os.path.dirname(__file__), "..", "historial", "historial_recibos.json"))
    historial.append(nuevo_recibo)
    guardar_historial(historial, os.path.join(os.path.dirname(__file__), "..", "historial", "historial_recibos.json"))


def mostrar_dato_listbox(listbox_historial):

    seleccion = listbox_historial.curselection()
    if len(seleccion) == 0:
        messagebox.showinfo("Error", "Por favor, seleccione un elemento de la lista.")
        return

    indice = seleccion[0]
    lista_historial = cargar_historial("historial_recibos.json")
    recibo = lista_historial[indice]
    mensaje = f"{recibo.__str__()}"
    messagebox.showinfo("Recibo", mensaje)