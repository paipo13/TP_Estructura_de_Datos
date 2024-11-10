import csv
from estructuras_de_datos import *
from datetime import datetime
from collections import deque
import random
class App():
    """
    Clase que representa una colección de aplicaciones.
    """
    def __init__(self,nombre_app,Category,Rating,Reviews,Size,Installs,Type,Price,Content_Rating,Genres,Last_Updated,Current_Ver,Android_Ver):
        """
        Inicializa una app con un nombre y atributos proporcionados.

        Parámetros:
            nombre_app (str): El nombre de la app.
            Category (str): La categoría de la app.
            Rating (float): La calificación de la app.
            Reviews (int): La cantidad de reseñas de la app.
            Size (str): El tamaño de la app.
            Installs (int): La cantidad de instalaciones de la app.
            Type (str): El tipo de la app (gratis o paga).
            Price (float): El precio de la app (solo si es de paga).
            Content_Rating (str): La clasificación de contenido de la app.
            Genres (str): Los géneros de la app.
            Last_Updated (str): La fecha de la última actualización de la app.
            Current_Ver (str): La versión actual de la app.
            Android_Ver (str): La versión mínima de Android requerida para la app.
        """
        self.nombre_app= nombre_app
        self.category = Category
        self.rating = Rating
        self.reviews = Reviews
        self.size = Size
        self.installs = Installs
        self.type = Type
        self.price = Price
        self.content_rating = Content_Rating
        self.genres = Genres
        self.last_updated = Last_Updated
        self.current_ver = Current_Ver
        self.android_ver = Android_Ver
    def __str__(self):
        """
        Devuelve una representación de cadena de la app.

        Devuelve:
            str: El nombre de la app.
        """
        return self.nombre_app

class Appstore():
    """
    Clase que representa un appstore, que gestiona y proporciona aplicaciones.
    """
    def __init__(self, nombre_app='Appstore', archivo_data='Play Store Data.csv'):
        """
        Inicializa el Appstore con un nombre y carga aplicaciones desde un archivo CSV.

        Parámetros:
            nombre_app (str): El nombre del appstore.
            archivo_data (str): La ruta al archivo CSV que contiene los datos de las aplicaciones.
        """
        self.nombre_app=nombre_app
        self.apps=dict()                  #Los diccoinarois facilitan la buisqueda de apps por nombre.
        self.apps_descargadas=dict() 
        titulo=True
        with open(archivo_data, mode='r', encoding='utf-8') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            for fila in lector_csv:
                if titulo:
                    titulo=False
                else:
                    object=App(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8],fila[9],fila[10],fila[11],fila[12])
                    self.apps[object.nombre_app]=object
    def descargar_app(self, nombre_app):
        """
        Descarga una aplicación del appstore.

        Parámetros:
            nombre_app (str): El nombre de la aplicación a descargar.

        Devuelve:
            None
        """
        contenido=None
        if nombre_app not in self.apps:
            print("No existe la app deseada.")      
        elif nombre_app not in self.apps_descargadas:
            contenido=self.apps[nombre_app]
            self.apps_descargadas[nombre_app]=contenido
            print(f"Descargada la app {nombre_app}")
        else:
            print(f"La app {nombre_app} ya se encuentra descargada.")
            
    def eliminar_app(self, nombre_app):
        """
        Elimina una aplicación descargada de la appstore.

        Parámetros:
            nombre_app (str): El nombre de la aplicación a eliminar.

        Devuelve:
            None
        """
        if nombre_app not in self.apps_descargadas:
            print(f"La app {nombre_app} a eliminar no esta descargada.")
        else:
            del self.apps_descargadas[nombre_app]
            print(f"Fue eliminada la app {nombre_app}")

class Configuracion():
    """
    Clase que representa la configuración del teléfono.
    """
    def __init__(self,nombre):
        """
        Inicializa la configuración con un nombre y establece la red móvil y los datos activos en False.

        Parámetros:
            nombre (str): El nombre del teléfono.
        """
        self.red_movil = True
        self.datos_activos = False
        self.nombre_telefono = nombre
    
    def activar_modo_avion(self):
        """
        Activa el modo avión. Desactiva la red móvil y, si está activado, desactiva los datos.

        Devuelve:
            None
        """
        if self.red_movil==True:
            self.red_movil = False
            print("Modo avion activado")
            if self.datos_activos==True:
                self.desactivar_datos
        else:
            print("Ya se encuentra en modo avion")
    def desactivar_modo_avion(self):
        """
        Desactiva el modo avión. Activa la red móvil.

        Devuelve:
            None
        """
        if self.red_movil==False:
            self.red_movil = True
            print("Modo avion desactivado")
        else:
            print("No se encuentra en modo avion")
            
    def activar_datos(self):
        """
        Activa los datos móviles. Solo se puede activar si la red móvil está desactivada.

        Devuelve:
            None
        """
        if self.red_movil==False:
            print("No puedes activar los datos en modo avion(red desactivada)")
        elif self.datos_activos==False:
            self.datos_activos = True
            print("Datos activados")   
        else:
            print("Ya se encuentran los datos activos")
    def desactivar_datos(self):
        """
        Desactiva los datos móviles.

        Devuelve:
            None
        """
        if self.datos_activos==True:
            self.datos_activos = False
            print("Datos desactivados")
        else:
            print("Los datos ya estan desactivados")
    
    def modo_avion(self):
        """
        Devuelve el estado del modo avión.

        Devuelve:
            bool: True si está en modo avión, False en caso contrario.
        """
        return not self.red_movil
    
    def datos_activos_conf(self):
        """
        Devuelve el estado de los datos activos.
        
        Devuelve:
            bool: True si están activos, False en caso contrario."""
        return self.datos_activos

    def cambiar_nombre(self,nuevo_nombre):
        """
        Cambia el nombre del teléfono.

        Parámetros:
            nuevo_nombre (str): El nuevo nombre del teléfono.

        Devuelve:
            None
        """
        self.nombre_telefono = nuevo_nombre
        print(f"Nombre cambiado a {self.nombre_telefono}")

class Mail():
    """
    Clase que representa un correo electrónico.
    """
    def __init__(self):
        """
        Inicializa el correo con una lista vacía de mensajes.
        """
        self.bandeja = []
    def ver_mails(self,orden):
        """Visualiza los mails por pantalla.

        Parametros:
            orden (str): El orden segun se quieren visualizar los mails.
        """
        if orden == 'no leidos primero':
            print('Correos ordenados segun no leidos primero:')
            correos =  sorted(self.bandeja, key=lambda x: (x[2]), reverse=True)
            for cosa in correos:
                cosa[1] = cosa[1].strftime("%Y-%m-%d %H:%M") 
                print(cosa)
        elif orden == 'por fecha':
            print('Correos ordenados segun fecha:')
            correos =  sorted(self.bandeja, key=lambda x: (x[1]), reverse=True)
            for cosa in correos:
                print((cosa))
                
class Llamada:
    """
    Clase que representa una app de llamadas.
    """
    def __init__(self):
        self.historial_llamadas = ListaEnlazada()
    def realizar_llamada(self, numero):
        """Simula la realizacion de una llamada.

        Args:
            numero (int): Numero al que se le realiza la llamada.
        
        Returns: None.
        """
        self.historial_llamadas.insertar((numero, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "saliente"))
    
    def recibir_llamada(self, numero):
        """Simula el recibimiento de una llamada.

        Args:
            numero (int): Numero del cual recibo la llamada.
            
        Returns: None.
        """
        self.historial_llamadas.insertar((numero, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "entrante"))
        
    def ver_historial_llamadas(self):
        """Devuelve el historial de llamadas del telefono como lista.

        Returns:
            list: Una lista con historial de llamadas.
        """
        return list(self.historial_llamadas)
    
class Mensajeria:
    """
    Clase que representa una app de mensajes.
    """
    def __init__(self):
        self.bandeja_entrada_sms = deque()    ### cola -- añade al final, sale el primero 
        self.historial_sms_enviados = deque()   ### pila -- añade al final, sale el ultimo
    
    def enviar_mensaje(self, destino, contenido):
        """Simula enviado de mensaje a otro telefono. 

        Args:
            destino (int): Numero de destino.
            contenido (int): Numero de contenido.
        
        Returns: None.
        """
        self.historial_sms_enviados.append((destino, contenido, datetime.now()))
        
    def recibir_mensaje(self, origen, contenido):
        """Simula el recibimiento de un mensaje. 

        Args:
            origen (int): Telefono de origen del mensaje.
            contenido (str): Contenido del mensaje.
            
        Devuelve: None
        """
        self.bandeja_entrada_sms.append((origen, contenido, datetime.now().strftime("%Y-%m-%d %H:%M:%S") ))
        
    def eliminar_mensaje(self, posicion):
        """Elimina un mensaje de sms del telefono ingresando como parametro la posicion de ese mensaje.

        Args:
            posicion (int): La posicion del mensaje que se quiere eliminar.
            
        Returns: None 
        """
        lista = list(self.bandeja_entrada_sms)
        if posicion < len(lista):
        
            for i in range(len(lista)):
                if i == posicion:
                    print(f"El mensaje {lista[i]} ha sido eliminado")
                    del lista[i]
            self.bandeja_entrada_sms = deque(lista)
        else:
            print(f"No se puede eliminar un mensaje en la posicion {posicion}, esa posicion no existe.")
            
    def ver_bandeja_entrada_sms(self):
        """Devuelve la bandeja de entrada de sms como lista. 

        Returns:
            list: Una lista con todos los mensajes recibidos de sms.
        """
        return list(self.bandeja_entrada_sms)
    
    def ver_historial_sms_enviados(self):
        """Devuelve el historial de mensajes sms enviados como lista.

        Returns:
            list: Una lista con todos los mensajes enviados de sms.
        """
        return list(self.historial_sms_enviado)

