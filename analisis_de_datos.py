import matplotlib.pyplot as plt
import numpy as np
import csv
import os
#MATPLOTLIB

def maquinita_de_ayuda():
    """ Nos sirve para el grafico de torta. Trae la informacion de los archivos 'datos' y la pasa a un diccionario que luego sera leido por graficar_torta_llamadas.

    Returns:
        data (dict): Diccionario con la informacion para el grafico de barra. 
    """
    data = {}
    ruta_archivo = os.path.join('datos', 'llamadas.csv')
    if not os.path.exists(ruta_archivo):
        return None
    try:
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
    except:
        print("Hubo un error al leer el archivo de llamadas.")
    return None


# import matplotlib.pyplot as plt
# import numpy as np

def graficar_torta_llamadas(diccionario_con_data):
    """Grafica de Torta para poner en porcentajes la cantidad de llamadas agrupadas por las duraciones (en min) de estas

    Args:
        data (dict): Diccionario con la informacion para el grafico de barra.
    """
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
    """_summary_

    Args:
        data (dict): Diccionario con la informacion para el grafico de barra.
    """
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
        
# import numpy as np
# import matplotlib.pyplot as plt

# # Suponiendo que cargamos los datos desde el archivo CSV
# # Los datos se leen y estructuran con numpy
# import csv

# Leer archivo CSV
def grafica_de_apps():
    data = []
    try:
        with open("Play Store Data.csv", "r", encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                data.append(row)
    except FileExistsError:
        print("No se encontró el archivo Play Store Data.csv.")

    # Convertir a arrays NumPy para facilitar el procesamiento
    tipo_apps = np.array([row[6] for row in data])
    rating_apps = np.array([float(row[2]) for row in data])
    categorias = np.array([row[1] for row in data])
    instalaciones = np.array([float((row[5][:-1]).replace(',','')) for row in data])

    # Filtrar datos para 'free' y 'pago'
    categorias_unicas = np.unique(categorias)
    instalaciones_rating_alto = []
    instalaciones_rating_bajo = []

    for categoria in categorias_unicas:
        # Sumar instalaciones por categoría y tipo de app
        suma_rating_alto = np.sum(instalaciones[(categorias == categoria) & (rating_apps >= 4.5)])
        suma_rating_bajo = np.sum(instalaciones[(categorias == categoria) & (rating_apps < 4.5)])
        instalaciones_rating_alto.append(suma_rating_alto)
        instalaciones_rating_bajo.append(suma_rating_bajo)

    # Convertir listas a arrays para graficar
    instalaciones_rating_alto = np.array(instalaciones_rating_alto)
    instalaciones_rating_bajo = np.array(instalaciones_rating_bajo)

    # Crear gráfico de barras agrupadas
    x = np.arange(len(categorias_unicas))
    width = 0.4

    plt.bar(x - width/2, instalaciones_rating_alto, width, label="Rating mayor a 4", color="skyblue")
    plt.bar(x + width/2, instalaciones_rating_bajo, width, label="Rating menor a 4", color="orange")

    # Configuración del gráfico
    plt.xlabel("Categorías")
    plt.ylabel("Instalaciones")
    plt.title("Instalaciones por Categoría y Tipo de App")
    plt.xticks(x, categorias_unicas, rotation=45, ha="right")
    plt.legend()

    # Mostrar el gráfico
    plt.tight_layout()
    plt.show()