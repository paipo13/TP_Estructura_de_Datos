import os
import csv
import matplotlib.pyplot as plt
import numpy as np
cantidad_llamadas = []
duracion_llamadas = []

# def agregar_datos_listas_grafica_lineal_llamadas(estado, duracion):
#     if estado == "conectado":
#         duracion_en_minutos = ((int(duracion))//60) + 1 #Ej: Si una llamada dura 61 segundo la tomo como dos minutos, redondeo todo para arriva.
#         if duracion_en_minutos in duracion_llamadas:
#             pos = duracion_llamadas.index(duracion_en_minutos)
#             cantidad_llamadas[pos] += 1
#         else:
#             duracion_llamadas.append(duracion_en_minutos)
#             pos_recien_agregado = duracion_llamadas.index(duracion_en_minutos)
#             cantidad_llamadas.append(1)
#     # return False
# datos_frafica_lineal = [
#     ("conectado",123),
#     ("conectado",63),
#     ("conectado",59),
#     ("ocupado",14),
#     ("ocupado",800),
#     ("conectado", 133),
#     ("conectado", 143),
#     ("conectado",63)
# ]
# for dato in datos_frafica_lineal:
#     agregar_datos_listas_grafica_lineal_llamadas(dato[0], dato[1])
def agregar_datos_diccionario(diccionario, clave):
    if clave in diccionario:
        diccionario[clave] += 1
    else:
        diccionario[clave] = 1
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


import matplotlib.pyplot as plt
import numpy as np

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
    norm_duraciones = np.array(duraciones) / max(duraciones)

    # Crear el gráfico de torta
    plt.pie(cantidades, labels=etiquetas, autopct='%1.1f%%', startangle=90, colors=plt.cm.viridis(norm_duraciones))

    # Asegurar que el gráfico sea circular
    plt.axis('equal')

    # Título
    plt.title('Proporcion de cantidad de llamados por minuto/s')

    # Mostrar el gráfico
    plt.show()

# Ejemplo de uso

dic_con_info = maquinita_de_ayuda()
graficar_torta_llamadas(dic_con_info)
