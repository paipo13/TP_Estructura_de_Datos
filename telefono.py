#Clase Teléfono
#Encapsula las funcionalidades básicas del telefono, como encender, apagar, bloquear y desbloquear, 
# además de interactuar con las aplicaciones. 
#Validaremos su estado para evitar acciones inválidas (como hacer llamadas cuando está apagado)
from aplicaciones import *
from listas_enlazadas import *
from contactos import *
from central_comunicacion import *
from clase_apps import *
from clase_configuracion import *
from collections import deque
class Telefono:
    def __init__(self, id, nombre, modelo, sistema_operativo, version, ram, almacenamiento, numero_telefono):
        """Inicializa un teléfono con los atributos básicos."""
        self.id = id
        self.nombre = nombre
        self.modelo = modelo
        self.sistema_operativo = sistema_operativo
        self.version = version
        self.ram = ram
        self.almacenamiento = almacenamiento
        self.numero_telefono = numero_telefono
        self.encendido = False
        self.bloqueado = True
        self.configuracion= Configuracion()
        self.contactos = ListaEnlazada()  # Usamos una lista enlazada para gestionar los contactos
        self.appstore=Appstore()
        self.mensajes=deque()

    def encender(self,central):
        """Enciende el teléfono y activa la red móvil."""
        if not self.encendido:
            self.encendido = True
            self.desactivar_modo_avion
            print(f"{self.nombre} ha sido encendido.")
            central.registrar_dispositivo(self)
        else:
            print(f"{self.nombre} ya está encendido.")
            

    def apagar(self,central):
        """Apaga el teléfono y desactiva todas las conexiones."""
        if self.encendido:
            self.encendido = False
            self.activar_modo_avion
            self.bloqueado = True
            print(f"{self.nombre} ha sido apagado.")
            central.baja_dispositivo(self)
        else:
            print(f"{self.nombre} ya está apagado.")

    def bloquear(self):
        """Bloquea el teléfono."""
        if not self.bloqueado:
            self.bloqueado = True
            print(f"{self.nombre} ha sido bloqueado.")
        else:
            print(f"{self.nombre} ya está bloqueado.")

    def desbloquear(self):
        """Desbloquea el teléfono."""
        if self.bloqueado:
            self.bloqueado = False
            print(f"{self.nombre} ha sido desbloqueado.")
        else:
            print(f"{self.nombre} ya está desbloqueado.")

    def realizar_llamada(self, numero_destino, Central):
        """Intenta realizar una llamada a otro número a través de la Central."""
        if not self.encendido:
            print("El teléfono está apagado. No puede realizar una llamada.")
            return
        
        if not self.red_movil_activada:
            print("La red móvil no está activada. Active la red móvil para realizar llamadas.")
            return

        Central.establecer_llamada(self, numero_destino)
    
    def finalizar_llamada(self, numero_destino, Central):
        pass

    def enviar_sms(self, numero_destino, contenido, central):
        """Envía un mensaje SMS a través de la Central."""
        if not self.encendido:
            print("El teléfono está apagado. No puede enviar mensajes.")
            return

        if not self.red_movil_activada:
            print("La red móvil no está activada. Active la red móvil para enviar mensajes.")
            return
        # mensaje = Mensaje(self.numero_telefono, numero_destino, contenido)
        # Central.enviar_mensaje(self, numero_destino, mensaje)
        central.enviar_mensaje( self, numero_destino, contenido)
    
    def recibir_sms(self, mensaje):
        self.mensajes.appendleft(mensaje)
#(self: Central, emisor: Any, numero_destino: Any, mensaje: Any)

    # Validaciones para situaciones que pueden provocar errores, 
    #como intentar enviar mensajes con el teléfono apagado o sin red móvil.
    def encendido_y_desbloqueado(self):   # devuelve True si el teléfono está encendido y desbloqueado
        if not self.encendido:
            print("El teléfono está apagado")
        if self.bloqueado:
            print("El teléfono está bloqueado")
        return self.encendido and not self.bloqueado
    # Instalar aplicaciones desde el AppStore
    def descargar_app(self,name):
        if self.configuracion.datos and self.encendido_y_desbloqueado():
            self.appstore.descargar_app(name)
        else:
            print('No tiene datos para descargar aplicaciones')
    def eliminar_app(self,name):
        if self.encendido_y_desbloqueado():
            self.appstore.eliminar_app(name)
    def activar_modo_avion(self):
        if self.encendido_y_desbloqueado():
            self.configuracion.activar_modo_avion()
    def desactivar_modo_avion(self):
        if self.encendido_y_desbloqueado():
            self.configuracion.desactivar_modo_avion()
    def activar_datos(self):
        if self.encendido_y_desbloqueado():
            self.configuracion.activar_datos()
    def desactivar_datos(self):
        if self.encendido_y_desbloqueado():
            self.configuracion.desactivar_datos()
    
