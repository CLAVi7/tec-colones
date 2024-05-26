from cambio_material_teccolones.funcione_GUI_Cambio import *
import json

ventana = tk.Tk()
ventana.title("cambio de material")
ventana.geometry("800x400")
ventana["bg"] = "#C3CDC0"

etiqueta = tk.Label(ventana, text="Cambio de material a tec-colones",  font=("Helvetica", 20), bg="#8DC67E")
etiqueta.config(width=50, height=2)
etiqueta.pack()

label = tk.Label(ventana, text="seleccione el centro al que pertenece")
label.place(x=40, y=80)
options_centros = conseguir_centro()
variable_centros = tk.StringVar(ventana)
if options_centros:
    variable_centros.set(options_centros[0])
else:
    options_centros = ["No hay centros disponibles"]
    variable_centros.set(options_centros[0])

dropdown_menu_centros = tk.OptionMenu(ventana, variable_centros, *options_centros)
dropdown_menu_centros.place(x=40, y=105)

label1 = tk.Label(ventana, text="ingrese el caarnet del estudiante")
label1.place(x=40, y=140)
entry_carnet = tk.Entry(ventana, width=40)
entry_carnet.place(x=40, y=160)


label2 = tk.Label(ventana, text="seleccione el material traido")
label2.place(x=40, y=185)
options_materiales = conseguir_materiales()
#print("Los materiales son:")
#print(options_materiales)

variable_materiales = tk.StringVar(ventana)

formatted_options = [f"{nombre} - {unidad} - {valor}" for nombre, unidad, valor in options_materiales]
if formatted_options:
    variable_materiales.set(formatted_options[0])
else:
    formatted_options = ["No hay materiales disponibles"]
    variable_materiales.set(formatted_options[0])

dropdown_menu_materiales = tk.OptionMenu(ventana, variable_materiales, *formatted_options)
dropdown_menu_materiales.place(x=40, y=210)


label3 = tk.Label(ventana, text="ingrese la cantidad traida")
label3.place(x=40, y=245)
entry_cantidad = tk.Entry(ventana, width=40)
entry_cantidad.place(x=40, y=265)

def llammar_modificar_carrito():

    modificar_carrito(listbox_carrito, entry_cantidad, variable_materiales, entry_carnet)
    cambiar_label()
    variable_centros.set(options_centros[0])
    variable_materiales.set(options_materiales[0])
    entry_cantidad.delete(0, tk.END)


boton_añadir = tk.Button(ventana, text="añadir material", command=llammar_modificar_carrito)
boton_añadir.place(x=40, y=290)


listbox_carrito = None
#nuevo_carrito = None

listbox_carrito = tk.Listbox(ventana, height=12, width=70)
listbox_carrito.place(x=350, y=105)


label3 = tk.Label(ventana, text="Carrito")
label3.place(x=350, y=80)

label4 = tk.Label(ventana, text="Llevas 0 tec-colones")
label4.place(x=350, y=315)

def cambiar_label():
    tec_colones = suma_tec_colones()
    label4.config(text = f"Llevas {tec_colones} tec-colones")


def vaciar_json_archivo(ruta_archivo):
    # Crea un JSON vacío
    contenido_vacio = {}

    # Abre el archivo en modo escritura para sobrescribir su contenido
    with open(ruta_archivo, 'w') as archivo:
        # Escribe el JSON vacío en el archivo
        json.dump(contenido_vacio, archivo, indent=4)


ruta_archivo = "carrito.json"
vaciar_json_archivo(ruta_archivo)

def vaciar_json_diccionario(diccionario_json):
    # Vacía el diccionario
    diccionario_json.clear()


mi_diccionario_json = {
    "clave1": "valor1",
    "clave2": "valor2"
}
vaciar_json_diccionario(mi_diccionario_json)



def llamar_cargar_listbox():
    
    cargar_y_mostrar_carrito_listbox(listbox_carrito)

llamar_cargar_listbox()


ventana.mainloop()