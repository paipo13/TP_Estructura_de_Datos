import csv
import os
from datetime import datetime, timedelta

class Central:
    """Clase que representa una central de red con sus funcionalidades.
    """
    def __init__(self):
        """Inicializa una central.
        """
        self.telefonos_registrados = {}
        self.telefono_modo_avion = {}
        self.inicializar_archivos()
    
    def inicializar_archivos(self):
        """Inicializa archivos de llamadas y mensajes en la central.
        
        Returns: None 
        """
        if not os.path.exists('datos'):
            os.makedirs('datos')
        
        for archivo in ['llamadas.csv', 'mensajes.csv']:
            ruta_archivo = os.path.join('datos', archivo)
            if not os.path.exists(ruta_archivo):
                with open(ruta_archivo, 'w', newline='') as file:
                    writer = csv.writer(file)
                    if archivo == 'llamadas.csv':
                        writer.writerow(['origen', 'destino', 'duracion', 'tiempo', 'estado'])
                    else:
                        writer.writerow(['origen', 'destino', 'contenido', 'tiempo'])
    
    def registrar_telefono(self, telefono):
        """Registra un telefono en la central.

        Args:
            telefono (int): El objeto telefono a registrar.
            
        Returns: None.
        """
        self.telefonos_registrados[telefono.numero] = telefono
        self.telefono_modo_avion[telefono.numero] = False
    
    def desregistrar_telefono(self, telefono):
        """Desregistra un telefono de la central 

        Args:
            telefono (int): El objeto telefono a desregistrar.
            
        Returns: None.
        """
        if telefono.numero in self.telefonos_registrados:
            del self.telefonos_registrados[telefono.numero]
            del self.telefono_modo_avion[telefono.numero]
    
    def actualizar_modo_avion(self, numero, estado):
        """Actualiza el estado de un telefono en el diccionario telefono_modo_avion.

        Args:
            numero (int): numero de telefono.
            estado (bool): True si quiero que el estado pase a true, sino False.
            
        Returns: None.
        """
        if numero in self.telefono_modo_avion:
            self.telefono_modo_avion[numero] = estado
    
    def validar_llamada(self, origen, destino):
        """Valida que una llamada tenga todos los requisitos para poder realizarse.

        Args:
            origen (int): Numero de telefono de origen de llamada.
            destino (int): Numero de telefono de destino de llamada.

        Returns:
            bool: True si se puede realizar la llamada, False si no se deberia poder realizar la llamada.
        """
        if (origen in self.telefonos_registrados and destino in self.telefonos_registrados and
            not self.telefono_modo_avion[origen] and not self.telefono_modo_avion[destino] and
            self.telefonos_registrados[origen].validar_encendido() and
            self.telefonos_registrados[origen].validar_desbloqueado() and
            self.telefonos_registrados[destino].validar_encendido()):
            return True
        return False
    
    def validar_mensaje(self, origen, destino):
        """Valida que al enviar un mensaje se cumplan los requisitos para que este se pueda enviar. 

        Args:
            origen (int): Numero de telefono de origen.
            destino (int): Numero de telefono de destino.

        Returns:
            bool: True si se puede enviar el mensaje, False si no deberia poderse.
        """
        if (origen in self.telefonos_registrados and destino in self.telefonos_registrados and
            not self.telefono_modo_avion[origen] and not self.telefono_modo_avion[destino] and
            self.telefonos_registrados[origen].validar_encendido() and
            self.telefonos_registrados[origen].validar_desbloqueado()):
            return True
        return False
    
    def realizar_llamada(self, origen, destino,tiempo, duracion): #Obs. Las llamadas que no re puedan concretar es decir que llamao y esta en llamada o quiero llamar y estoy en llamada se van a registrar con el estado "ocupado" mientras que si se cumplen todas las condiciones (mirar metodos) va a figurar el estado en el archivo de registro como "conectada"...
        """Simula la realizacion de una llamada desde la central.

        Args:
            origen (int): Numero de origen de llamada.
            destino (int): Numero de destino de llamada.
            duracion (int): Durecion de la llamada en segundos. 

        Returns:
            bool: True si se pudo realizar la llamada, False de lo contrario.
        """
        if self.validar_llamada(origen, destino):
            if Central.determinar_estado_llamada(self,destino, tiempo) == "ocupado": # Aca lo que pasa es que al numero que llamamos esta en llamada por lo que se realiza la llamada pero no se llega a conectar
                estado = "ocupado"
                self.telefonos_registrados[origen].realizar_llamada(destino)
                self.registrar_llamada(origen, destino, duracion, tiempo, estado)
                return False 
    
            if Central.determinar_estado_llamada(self,origen, tiempo) == "ocupado":
                estado = "ocupado"
                self.registrar_llamada(origen, destino, duracion, tiempo, estado)
                return False
            estado = self.determinar_estado_llamada(destino, tiempo)
            self.registrar_llamada(origen, destino, duracion, tiempo, estado)
            self.telefonos_registrados[origen].realizar_llamada(destino)
            self.telefonos_registrados[destino].recibir_llamada(origen)
            return True
        return False

    def enviar_mensaje(self, origen, destino, tiempo, contenido):
        """Simula el enviado de un mensaje desde la central.

        Args:
            origen (int): Numero de origen del mensaje.
            destino (int): Numero de destino del mensaje.
            contenido (str): Contenido del mensaje.

        Returns:
            bool: True si se pudo enviar el mensaje correctamente, False de lo contrario.
        """
        if self.validar_mensaje(origen, destino):
            self.registrar_mensaje(origen, destino, contenido, tiempo)
            self.telefonos_registrados[origen].enviar_mensaje(destino, contenido)
            self.telefonos_registrados[destino].recibir_mensaje(origen, contenido)
            return True
        return False
    
    def determinar_estado_llamada(self, destino, tiempo_actual):
        ultima_llamada = self.obtener_ultima_llamada(destino) #Obs.estamos trabajando con tumplas donde ultima_llamada = (tiempo,duracion)
        if ultima_llamada:
            tiempo_ultima_llamada, duracion_ultima_llamada, estado = ultima_llamada #Obs. desempaquetado de la tumpla donde asigno a tiempo_ultima_llamda el valor tiempo que tiene el tiempo en el que se realizo la ultima llamada del teleofno de destino y a la variable duracion_ultima_llamdad se le asigna el valor duracion que es la duracion (en seg) de la ultima llamda que realizo el numero al que estamos llamando, num de destino.
            tiempo_fin_ultima_llamada = tiempo_ultima_llamada + timedelta(seconds=duracion_ultima_llamada)
            if tiempo_fin_ultima_llamada >= tiempo_actual and estado == "conectado":
                return "ocupado"
        return "conectado" ###estamos en llamassss ;)
    
    def obtener_ultima_llamada(self, numero):
        ruta_archivo = os.path.join('datos', 'llamadas.csv')
        if not os.path.exists(ruta_archivo):
            return None
        with open(ruta_archivo, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Saltar la fila de encabezados
            llamadas = list(reader)
            for llamada in reversed(llamadas): #Da vuelta el ordenamiento
#                if llamada[1] == str(numero):  # Si el número es el destino de la llamada
                 if llamada[1] == str(numero) and llamada[4] == "conectado":
                    tiempo = datetime.strptime(llamada[3], '%Y-%m-%d %H:%M:%S')
                    duracion = int(llamada[2])
                    estado = llamada[4]
                    return tiempo, duracion , estado
        return None
    
    def registrar_llamada(self, origen, destino, duracion, tiempo, estado):
        ruta_archivo = os.path.join('datos', 'llamadas.csv')
        with open(ruta_archivo, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([origen, destino, duracion, tiempo, estado])
    
    def registrar_mensaje(self, origen, destino, contenido, tiempo):
        ruta_archivo = os.path.join('datos', 'mensajes.csv')
        with open(ruta_archivo, 'a', newline='', encoding= 'utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([origen, destino, contenido, tiempo])
    
    def mostrar_registros(self):
        print("Registro de llamadas:")
        ruta_archivo = os.path.join('datos', 'llamadas.csv')
        with open(ruta_archivo, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
        
        print("\nRegistro de mensajes:")
        ruta_archivo = os.path.join('datos', 'mensajes.csv')
        with open(ruta_archivo, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
