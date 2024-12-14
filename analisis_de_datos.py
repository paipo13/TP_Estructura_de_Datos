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

def grafica_de_apps():
    data = []
    try:
        with open("Play Store Data.csv", "r", encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print("No se encontró el archivo Play Store Data.csv.")
        return

    versiones_validas = {"4.0.3 and up", "4.0 and up", "4.1 and up", "4.3 and up", "4.4 and up"}

    categorias = []
    ratings = []
    versiones_android = []

    for row in data:
        try:
            categoria = row[1]
            rating = row[2]
            version = row[12]
            
            if isinstance(rating, str) and rating.lower() == "nan":
                continue
            rating = float(rating)
            if version in versiones_validas:
                categorias.append(categoria)
                ratings.append(rating)
                versiones_android.append(version)
        except (ValueError, IndexError):
            continue

    categorias = np.array(categorias)
    ratings = np.array(ratings)
    versiones_android = np.array(versiones_android)

    ratings = ratings[~np.isnan(ratings)]  

    categorias_unicas = np.unique(categorias)
    promedios_rating = []
    version_frecuente = []

    for categoria in categorias_unicas:
        indices = (categorias == categoria)
        ratings_categoria = ratings[indices]
        versiones_categoria = versiones_android[indices]
        
        if len(ratings_categoria) > 0:
            promedio = np.mean(ratings_categoria)
            promedios_rating.append(promedio)
        else:
            promedios_rating.append(0)

        if len(versiones_categoria) > 0:
            version_comun = np.unique(versiones_categoria, return_counts=True)
            version_frecuente.append(version_comun[0][np.argmax(version_comun[1])])
        else:
            version_frecuente.append("N/A")

    version_frecuente = [version.replace(" and up", "") for version in version_frecuente]

    # Creamos el gráfico de barras
    x = np.arange(len(categorias_unicas))
    
    plt.bar(x, promedios_rating, color=plt.cm.Paired(np.linspace(0, 1, len(categorias_unicas))), edgecolor="black")

    plt.title("Promedio de Rating por Categoría de Aplicaciones\n(en versiones de Android 4.0 y superiores)", fontsize=16, fontweight='bold', color='darkblue')
    plt.xticks(x, categorias_unicas, rotation=75, ha="right", fontsize=10)
    plt.yticks(fontsize=10)
    plt.xlabel("Categorías", fontsize=12, fontweight='bold')
    plt.ylabel("Promedio de Rating", fontsize=12, fontweight='bold')

    # Añado la versión más frecuente de Android en las etiquetas
    for i, v in enumerate(version_frecuente):
        if promedios_rating[i] > 0:
            plt.text(i, promedios_rating[i] + 0.1, v, ha="center", fontsize=8, color='darkgreen', fontweight='bold')

    
    plt.ylim(0, 5)
    # Ajusto el espaciado
    plt.tight_layout(pad=2.0)
    plt.show()

