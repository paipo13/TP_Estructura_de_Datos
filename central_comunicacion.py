# La clase de Central manejará la comunicación entre teléfonos, verificando si están registrados y 
# disponibles para realizar llamadas o enviar mensajes.

from telefono import *
from contactos import *
from listas_enlazadas import *
import csv
from datetime import datetime
import os

class Central:
    """
    La clase Central es responsable de mediar las comunicaciones entre dispositivos.
    """
    def __init__(self):
        self.dispositivos_registrados = set()  # Usamos un set para almacenar los dispositivos registrados

    def registrar_dispositivo(self, telefono):
        """
        Registra un dispositivo en la central.
        """
        self.dispositivos_registrados.add(telefono)
        
    def baja_dispositivo(self, telefono):
        """
        Desregistra un dispositivo en la central.
        """
        self.dispositivos_registrados.discard(telefono)

    def verificar_disponibilidad(self, telefono):
        """
        Verifica si un teléfono está registrado y disponible para recibir llamadas o mensajes.
        """
        if telefono in self.dispositivos_registrados:
            return True
        else:
            return False

    def registrar_llamada(self, tipo, emisor, receptor, duracion):
        """
        Registra una comunicación (llamada o SMS) en un archivo CSV.
        """
        if not os.path.exists('llamadas.csv'):
            with open('llamadas.csv', mode='w', newline='') as archivo_csv:
                pass  # Create the file but don't write anything to it
        with open('llamadas.csv', mode='a', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            escritor_csv.writerow([fecha_hora, tipo, emisor, receptor, duracion])
            
    def registrar_mensaje(self, tipo, emisor, receptor, mensaje):
        """
        Registra una comunicación (llamada o SMS) en un archivo CSV.
        """
        if not os.path.exists('mensajes.csv'):
            with open('mensajes.csv', mode='w', newline='') as archivo_csv:
                pass  # Create the file but don't write anything to it
        with open('mensajes.csv', mode='a', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            escritor_csv.writerow([fecha_hora, tipo, emisor, receptor, mensaje])

        print(f"Registro guardado: {tipo} de {emisor} a {receptor} - {mensaje}")

    def establecer_llamada(self, emisor, numero_destino):
        """
        Establece una llamada entre dos dispositivos si ambos están disponibles.
        """
        
        if not self.verificar_disponibilidad(emisor):
            print(f"El teléfono {emisor.numero_telefono} no está disponible para realizar llamadas.")
            return

        receptor = self.buscar_dispositivo_por_numero_telefono(numero_destino)
        if receptor is None:
            print(f"El teléfono {numero_destino} no está disponible para recibir llamadas.")
            return

        print(f"Llamada establecida de {emisor.numero_telefono} a {numero_destino}.")
        self.registrar_llamada("Llamada", emisor.numero_telefono, numero_destino, "Conectada")

    def enviar_mensaje(self, emisor, numero_destino, mensaje):
        """
        Envía un mensaje de un teléfono a otro a través de la central.
        """
        receptor = self.buscar_dispositivo_por_numero_telefono(numero_destino)
        if receptor is None or not self.verificar_disponibilidad(receptor):
            print(f"El teléfono {numero_destino} no está disponible para recibir mensajes.")
            return

        print(f"Mensaje enviado de {emisor.numero_telefono} a {numero_destino}: {mensaje.contenido}")
        self.registrar_mensaje("Mensaje", emisor.numero_telefono, numero_destino, mensaje.contenido)
    

    def buscar_dispositivo_por_numero_telefono(self, numero_destino):
        """
        Busca un dispositivo en la central por su número telefónico.
        """
        for dispositivo in self.dispositivos_registrados:
            if dispositivo.numero_telefono == numero_destino:
                return dispositivo
        return None

    def generar_reporte_comunicaciones(self):
        """
        Genera un reporte de las comunicaciones registradas en el archivo CSV.
        """
        lista_llamadas = []
        lista_mensajes = []
        try:
            with open('llamadas.csv', mode='r') as archivo_csv:
                lector_csv = csv.reader(archivo_csv)
                for fila in lector_csv:
                    lista_llamadas.append(fila)
            with open('mensajes.csv', mode='r') as archivo_csv:
                lector_csv = csv.reader(archivo_csv)
                for fila in lector_csv:
                    lista_mensajes.append(fila)

            print("\n--- Reporte de Comunicaciones ---")
            print("\nLlamadas")
            for llamada in lista_llamadas:
                fecha_hora, tipo, emisor, receptor, detalle = llamada
                print(f"{fecha_hora} | {tipo} de {emisor} a {receptor} - {detalle}")
            print("\nMensajes")
            for msj in lista_mensajes:
                fecha_hora, tipo, emisor, receptor, detalle = msj
                print(f"{fecha_hora} | {tipo} de {emisor} a {receptor} - {detalle}")
        except FileNotFoundError:
            print("No hay camunicaciones registradas")
            