# central.py
import csv
from datetime import datetime, timedelta
import os

class Central:
    def __init__(self):
        self.telefonos_registrados = {}
        self.telefono_modo_avion = {}
        
    def registrar_dispositivo(self, telefono):
        self.telefonos_registrados[telefono.numero_telefono] = telefono
        self.telefono_modo_avion[telefono.numero_telefono] = False
        print(f"Dispositivo {telefono.numero_telefono} registrado en la central.")
        
    def desregistrar_telefono(self, telefono):
        if telefono.numero_telefono in self.telefonos_registrados:
            del self.telefonos_registrados[telefono.numero_telefono]
            del self.telefono_modo_avion[telefono.numero_telefono]
            print(f"Dispositivo {telefono.numero_telefono} desregistrado de la central.")
        else:
            print(f"El dispositivo {telefono.numero_telefono} no está registrado en la central.")
    
    def actualizar_modo_avion(self, numero_telefono, estado):
        if numero_telefono in self.telefono_modo_avion:
            self.telefono_modo_avion[numero_telefono] = estado
            print(f"Modo avión actualizado para {numero_telefono}: {'Activado' if estado else 'Desactivado'}")
        else:
            print(f"El dispositivo {numero_telefono} no está registrado en la central.")
    
    def validar_llamada(self, origen, destino):
        if (origen in self.telefonos_registrados and destino in self.telefonos_registrados and
            not self.telefono_modo_avion[origen] and not self.telefono_modo_avion[destino]):
            telefono_origen = self.telefonos_registrados[origen]
            telefono_destino = self.telefonos_registrados[destino]
            if (telefono_origen.encendido and not telefono_origen.bloqueado and
                telefono_destino.encendido):
                return self.verificar_disponibilidad_llamada(destino)
        return False
    
    def validar_mensaje(self, origen, destino):
        if (origen in self.telefonos_registrados and destino in self.telefonos_registrados and
            not self.telefono_modo_avion[origen] and not self.telefono_modo_avion[destino]):
            telefono_origen = self.telefonos_registrados[origen]
            if telefono_origen.encendido and not telefono_origen.bloqueado:
                return True
        return False
    
    def verificar_disponibilidad_llamada(self, numero):
        tiempo_actual = datetime.now()
        with open('llamadas.csv', 'r') as archivo:
            lector = csv.reader(archivo)
            for fila in reversed(list(lector)):
                if fila[1] == numero:  # Si el número es el destino de la última llamada
                    tiempo_llamada = datetime.strptime(fila[3], "%Y-%m-%d %H:%M:%S")
                    duracion = int(fila[2])
                    if tiempo_llamada + timedelta(seconds=duracion) > tiempo_actual:
                        return False
                    break
        return True
    
    def registrar_llamada(self, origen, destino, duracion):
        tiempo = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        estado = "conectado" if self.verificar_disponibilidad_llamada(destino) else "ocupado"
        with open('llamadas.csv', 'a', newline='') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow([origen, destino, duracion, tiempo, estado])
    
    def registrar_mensaje(self, origen, destino, contenido):
        tiempo = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open('mensajes.csv', 'a', newline='') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow([origen, destino, contenido, tiempo])
    
    def mostrar_registros(self):
        if not os.path.exists('llamadas.csv'):
            # Si el archivo no existe, lo creamos vacío
            with open('llamadas.csv', 'w') as archivo:
                archivo.write("Origen,Destino,Duracion,Tiempo,Estado\n")
        if not os.path.exists('mensajes.csv'):
            with open('mensajes.csv', 'w') as archivo:
                archivo.write("Origen,Destino,Contenido,Tiempo\n")
        print("Registro de llamadas:")
        with open('llamadas.csv', 'r') as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                print(f"Origen: {fila[0]}, Destino: {fila[1]}, Duración: {fila[2]}, Tiempo: {fila[3]}, Estado: {fila[4]}")
        
        print("\nRegistro de mensajes:")
        with open('mensajes.csv', 'r') as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                print(f"Origen: {fila[0]}, Destino: {fila[1]}, Contenido: {fila[2]}, Tiempo: {fila[3]}")