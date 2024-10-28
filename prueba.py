

cantidad_llamadas = []
duracion_llamadas = []

def agregar_datos_listas_grafica_lineal_llamadas(estado, duracion):
    
    if estado == "conectado":
        duracion_en_minutos = (int(duracion))//60
        if duracion_en_minutos in duracion_llamadas:
            pos = duracion_llamadas.index(duracion_en_minutos)
            cantidad_llamadas[pos] += 1
        else:
            duracion_llamadas.append(duracion_en_minutos)
            pos_recien_agregado = duracion_llamadas.index(duracion_en_minutos)
            cantidad_llamadas.append(1)


agregar_datos_listas_grafica_lineal_llamadas("conectado", 123)
agregar_datos_listas_grafica_lineal_llamadas("conectado",63)
agregar_datos_listas_grafica_lineal_llamadas("conectado",59)
agregar_datos_listas_grafica_lineal_llamadas("ocupado",14)
agregar_datos_listas_grafica_lineal_llamadas("ocupado",800)
agregar_datos_listas_grafica_lineal_llamadas("conectado", 133)
agregar_datos_listas_grafica_lineal_llamadas("conectado", 143)
agregar_datos_listas_grafica_lineal_llamadas("conectado",63)


import matplotlib.pyplot as plt
import numpy as np

def graficar_torta_llamadas(cantidades, duraciones):
    """
    Genera un gráfico de torta donde el tamaño de cada sector representa 
    la cantidad de llamadas y el color representa la duración de dichas llamadas.

    :param cantidades: Lista con las cantidades de llamadas.
    :param duraciones: Lista con las duraciones correspondientes (en minutos).
    """
    # Validamos que ambas listas tengan la misma longitud
    if len(cantidades) != len(duraciones):
        print("Error: Las listas de cantidades y duraciones deben tener la misma longitud.")
        return

    # Crear etiquetas para los sectores de la torta
    etiquetas = [f'Llamadas de {c} minuto/s' for c in cantidades]

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


graficar_torta_llamadas(cantidad_llamadas, duracion_llamadas)
