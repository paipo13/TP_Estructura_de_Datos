#Clase Teléfono
#Encapsula las funcionalidades básicas del telefono, como encender, apagar, bloquear y desbloquear, 
# además de interactuar con las aplicaciones. 
#Validaremos su estado para evitar acciones inválidas (como hacer llamadas cuando está apagado)

from listas_enlazadas import *
from contactos import *
from central_comunicacion import *
class Telefono:
    def __init__(self, id, nombre, modelo, sistema_operativo, version, ram, almacenamiento, numero_telefono):
        """
        Inicializa un teléfono con los atributos básicos.
        """
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
        self.red_movil_activada = False
        self.datos_mobiles_activados = False
        self.contactos = ListaEnlazada()  # Usamos una lista enlazada para gestionar los contactos
        self.aplicaciones = ListaEnlazada()  # Aplicaciones instaladas

    def encender(self,central):
        """
        Enciende el teléfono y activa la red móvil.
        """
        if not self.encendido:
            self.encendido = True
            self.red_movil_activada = True  # Activar red móvil al encender
            print(f"{self.nombre} está encendido.")
            central.registrar_dispositivo(self)
        else:
            print(f"{self.nombre} ya está encendido.")
            

    def apagar(self,central):
        """
        Apaga el teléfono y desactiva todas las conexiones.
        """
        if self.encendido:
            self.encendido = False
            self.red_movil_activada = False
            self.datos_mobiles_activados = False
            print(f"{self.nombre} está apagado.")
            central.baja_dispositivo(self)
        else:
            print(f"{self.nombre} ya está apagado.")

    def bloquear(self):
        """
        Bloquea el teléfono.
        """
        if not self.bloqueado:
            self.bloqueado = True
            print(f"{self.nombre} está bloqueado.")
        else:
            print(f"{self.nombre} ya está bloqueado.")

    def desbloquear(self):
        """
        Desbloquea el teléfono.
        """
        if self.bloqueado:
            self.bloqueado = False
            print(f"{self.nombre} está desbloqueado.")
        else:
            print(f"{self.nombre} ya está desbloqueado.")

    def abrir_aplicacion(self, nombre_aplicacion):
        """
        Abre una aplicación instalada si el teléfono está encendido y desbloqueado.
        """
        if not self.encendido:
            print("El teléfono está apagado. No se puede abrir la aplicación.")
            return

        if self.bloqueado:
            print("El teléfono está bloqueado. Desbloquéelo para abrir la aplicación.")
            return

        for aplicacion in self.aplicaciones:
            if aplicacion.nombre == nombre_aplicacion:
                print(f"Abriendo {nombre_aplicacion}...")
                aplicacion.ejecutar()
                return

        print(f"La aplicación {nombre_aplicacion} no está instalada en el teléfono.")

    def realizar_llamada(self, numero_destino, Central):
        """
        Intenta realizar una llamada a otro número a través de la Central.
        """
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
        """
        Envía un mensaje SMS a través de la Central.
        """
        if not self.encendido:
            print("El teléfono está apagado. No puede enviar mensajes.")
            return

        if not self.red_movil_activada:
            print("La red móvil no está activada. Active la red móvil para enviar mensajes.")
            return

        # mensaje = Mensaje(self.numero_telefono, numero_destino, contenido)
        # Central.enviar_mensaje(self, numero_destino, mensaje)
        central.enviar_mensaje( self.numero_telefono, numero_destino, contenido)

#(self: Central, emisor: Any, numero_destino: Any, mensaje: Any)

    # Validaciones para situaciones que pueden provocar errores, 
    #como intentar enviar mensajes con el teléfono apagado o sin red móvil.

    def activar_red_movil(self):
        """
        Activa la red móvil si el teléfono está encendido.
        """
        if not self.encendido:
            print("El teléfono está apagado. No puede activar la red móvil.")
            return

        self.red_movil_activada = True
        print(f"Red móvil activada en {self.nombre}.")

    def desactivar_red_movil(self):
        """
        Desactiva la red móvil.
        """
        self.red_movil_activada = False
        print(f"Red móvil desactivada en {self.nombre}.")

    def activar_datos_mobiles(self):
        """
        Activa los datos móviles si la red móvil está activada.
        """
        if not self.red_movil_activada:
            print("La red móvil no está activada. No puede activar los datos móviles.")
            return

        self.datos_mobiles_activados = True
        print("Datos móviles activados.")

    def desactivar_datos_mobiles(self):
        """
        Desactiva los datos móviles.
        """
        self.datos_mobiles_activados = False
        print("Datos móviles desactivados.")

    # Instalar aplicaciones desde el AppStore

    def instalar_aplicacion(self, aplicacion):
        """
        Instala una aplicación en el teléfono si no está ya instalada.
        """
        # if aplicacion not in self.aplicaciones:
        #     self.aplicaciones.append(aplicacion)
        #     print(f"Aplicación {aplicacion.nombre} instalada con éxito.")
        # else:
        #     print(f"La aplicación {aplicacion.nombre} ya está instalada.")

        if self.aplicaciones.buscar_devuelve_True_or_False(aplicacion)==True:
            print(f"La aplicación {aplicacion.nombre} ya está instalada.")
        else:
            self.aplicaciones.agregar(aplicacion)
            print(f"Aplicación {aplicacion.nombre} instalada con éxito.")
