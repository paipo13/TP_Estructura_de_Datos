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

    def registrar_dispositivo(self, Telefono):
        """
        Registra un dispositivo en la central.
        """
        self.dispositivos_registrados.add(Telefono)

    def verificar_disponibilidad(self, Telefono):
        """
        Verifica si un teléfono está registrado y disponible para recibir llamadas o mensajes.
        """
        if Telefono.numero_telefono in self.dispositivos_registrados and Telefono.encendido:
            return True
        else:
            return False

    def registrar_comunicacion(self, tipo, emisor, receptor, detalles):
        """
        Registra una comunicación (llamada o SMS) en un archivo CSV.
        """
        if not os.path.exists('comunicaciones.csv'):
            with open('comunicaciones.csv', mode='w', newline='') as archivo_csv:
                pass  # Create the file but don't write anything to it
        with open('comunicaciones.csv', mode='a', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            escritor_csv.writerow([fecha_hora, tipo, emisor, receptor, detalles])

        print(f"Registro guardado: {tipo} de {emisor} a {receptor} - {detalles}")

    def establecer_llamada(self, emisor, numero_destino):
        """
        Establece una llamada entre dos dispositivos si ambos están disponibles.
        """
        
        if not self.verificar_disponibilidad(emisor):
            print(f"El teléfono {emisor.numero_telefono} no está disponible para realizar llamadas.")
            return

        receptor = self.buscar_dispositivo_por_numero_telefono(numero_destino)
        if receptor is None or not self.verificar_disponibilidad(receptor):
            print(f"El teléfono {numero_destino} no está disponible para recibir llamadas.")
            return

        print(f"Llamada establecida de {emisor.numero_telefono} a {numero_destino}.")
        self.registrar_comunicacion("Llamada", emisor.numero_telefono, numero_destino, "Conectada")

    def enviar_mensaje(self, emisor, numero_destino, mensaje):
        """
        Envía un mensaje de un teléfono a otro a través de la central.
        """
        receptor = self.buscar_dispositivo_por_numero_telefono(numero_destino)
        if receptor is None or not self.verificar_disponibilidad(receptor):
            print(f"El teléfono {numero_destino} no está disponible para recibir mensajes.")
            return

        print(f"Mensaje enviado de {emisor.numero_telefono} a {numero_destino}: {mensaje.contenido}")
        self.registrar_comunicacion("Mensaje", emisor.numero_telefono, numero_destino, mensaje.contenido)
    

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
        comunicaciones = []
        try:
            with open('comunicaciones.csv', mode='r') as archivo_csv:
                lector_csv = csv.reader(archivo_csv)
                for fila in lector_csv:
                    comunicaciones.append(fila)

            print("\n--- Reporte de Comunicaciones ---")
            for comunicacion in comunicaciones:
                fecha_hora, tipo, emisor, receptor, detalles = comunicacion
                print(f"{fecha_hora} | {tipo} de {emisor} a {receptor} - {detalles}")
        except FileNotFoundError:
            print("No hay camunicaciones registradas")