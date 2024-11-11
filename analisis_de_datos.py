import matplotlib.pyplot as plt
import numpy as np
import csv
import os
#MATPLOTLIB

def maquinita_de_ayuda():
    data = {}
    ruta_archivo = os.path.join('datos', 'llamadas.csv')
    if not os.path.exists(ruta_archivo):
        return None
    with open(ruta_archivo, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Saltar la fila de encabezados
        llamadas = list(reader)
        for llamada in (llamadas): 
             estado = llamada[4]
             duracion_en_min = ((int(llamada[2]))//60) + 1 #Ej: Si una llamada dura 61 segundo la tomo como dos minutos, redondeo todo para arriba.
             if estado == "conectado":
                agregar_datos_diccionario(data, duracion_en_min)
        return data
    return None


# import matplotlib.pyplot as plt
# import numpy as np

def graficar_torta_llamadas(diccionario_con_data):
    duraciones = list(diccionario_con_data.keys())
    cantidades = list(diccionario_con_data.values())
    # Validamos que ambas listas tengan la misma longitud
    if len(cantidades) != len(duraciones):
        print("Error: Las listas de cantidades y duraciones deben tener la misma longitud.")
        return

    # Crear etiquetas para los sectores de la torta
    etiquetas = [f'Llamadas de {c} minuto/s' for c in duraciones]

    # Normalizar las duraciones para el color (escala de 0 a 1)
    try:
        norm_duraciones = np.array(duraciones) / max(duraciones)
    except:
        print("Hubo un error con el grafico de torta.")

    # Crear el gráfico de torta
    plt.pie(cantidades, labels=etiquetas, autopct='%1.1f%%', startangle=90, colors=plt.cm.viridis(norm_duraciones))

    # Asegurar que el gráfico sea circular
    plt.axis('equal')

    # Título
    plt.title('Proporcion de cantidad de llamados por minuto/s')

    # Mostrar el gráfico
    plt.show()

def grafico_barras(data):
    # data debería ser un diccionario con sistemas operativos como clave y cantidad como valor
    sistemas = list(data.keys())
    cantidades = list(data.values())

    plt.bar(sistemas, cantidades, color='skyblue')
    plt.title('Cantidad de Teléfonos por Sistema Operativo')
    plt.xlabel('Sistema Operativo')
    plt.ylabel('Cantidad')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def agregar_datos_diccionario(diccionario, clave):
    if clave in diccionario:
        diccionario[clave] += 1
    else:
        diccionario[clave] = 1