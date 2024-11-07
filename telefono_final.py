import datetime
from estructuras_de_datos import *
from aplicaciones import *
import uuid

class Telefono:
    """Clase que representa un telefono celular con sus acciones incorporadas.
    """
    def __init__(self, nombre, modelo, sistema_operativo, version, ram, almacenamiento, numero):
        """Inicializa un telefono con un numero y atributos proporcionados.

        Args:
            nombre (str): El nombre del telefono.
            modelo (str): El modelo del telefono.
            sistema_operativo (str): El sistema operativo del telefono.
            version (str): La version del telefono.
            ram (int): La ram del telefono.
            almacenamiento (int): El almacenamiento del telefono.
            numero (int): El numero del telefono.
        """
        self.id = uuid.uuid4()
        self.nombre = nombre
        self.modelo = modelo
        self.sistema_operativo = sistema_operativo
        self.version = version
        self.ram = ram
        self.almacenamiento = almacenamiento
        self.numero = numero
        self.encendido = False
        self.bloqueado = True
        
        # Y Nuestros componentes internos (del telefono) van a ser...
        self.contactos = set()
        self.bandeja_entrada_sms = Cola()
        self.historial_sms_enviados = Pila()
        self.emails = ListaEnlazada()
        self.historial_llamadas = ListaEnlazada()
        self.appstore=Appstore()
        self.configuracion = Configuracion(self.nombre)
        self.mail = Mail()

    def encendido_y_desbloqueado(self):   # devuelve True si el teléfono está encendido y desbloqueado
        """Devuelve el estado encendido y desbloqueado juntos.

        Returns:
            bool: True si el telefono está encendido y desbloqueado, False de lo contrario.
        """
        if not self.encendido:
            print("El teléfono está apagado")
        if self.bloqueado:
            print("El teléfono está bloqueado")
        return self.encendido and not self.bloqueado
    # def encender(self,central):
    #     """Enciende el teléfono y activa la red móvil."""
    #     if not self.encendido:
    #         self.encendido = True
    #         self.desactivar_modo_avion
    #         print(f"{self.nombre} ha sido encendido.")
    #         central.registrar_dispositivo(self)
    #     else:
    #         print(f"{self.nombre} ya está encendido.")
            

    # def apagar(self,central):
    #     """Apaga el teléfono y desactiva todas las conexiones."""
    #     if self.encendido:
    #         self.encendido = False
    #         self.activar_modo_avion
    #         self.bloqueado = True
    #         print(f"{self.nombre} ha sido apagado.")
    #         central.baja_dispositivo(self)
    #     else:
    #         print(f"{self.nombre} ya está apagado.")

    # def bloquear(self):
    #     """Bloquea el teléfono."""
    #     if not self.bloqueado:
    #         self.bloqueado = True
    #         print(f"{self.nombre} ha sido bloqueado.")
    #     else:
    #         print(f"{self.nombre} ya está bloqueado.")

    # def desbloquear(self):
    #     """Desbloquea el teléfono."""
    #     if self.bloqueado:
    #         self.bloqueado = False
    #         print(f"{self.nombre} ha sido desbloqueado.")
    #     else:
    #         print(f"{self.nombre} ya está desbloqueado.")
    def encender(self):
        """Simula el encencido del telefono. Al encenderlo se activa la red.
        
        Devuelve: None
        """
        self.encendido = True
        self.activar_red_movil()
    
    def apagar(self):
        """Simula el apagado del telefono. Al apagarlo se desactivan la red y datos.
        
        Devuelve: None
        """
        self.encendido = False
        self.red_movil_activa = False
        self.datos_activos = False
    
    def bloquear(self):
        """Simula el bloqueo del telefono.
        
        Devuelve: None
        """
        self.bloqueado = True
    
    def desbloquear(self):
        """
        Simula el desbloqueo del telefono. 
        
        Devuelve: None
        """
        self.bloqueado = False
    
    def activar_red_movil(self):
        if self.encendido and not self.configuracion.modo_avion:
            self.red_movil_activa = True
    
    def desactivar_red_movil(self):
        self.red_movil_activa = False
    
    def activar_modo_avion(self):
        """Activa el modo avión. Desactiva la red móvil y, si está activado, desactiva los datos.
        
            Devuelve: None
        """
        if self.encendido_y_desbloqueado():
            self.configuracion.activar_modo_avion()
    def desactivar_modo_avion(self):
        """
        Desactiva el modo avión. Activa la red móvil.

        Devuelve: None
        """
        if self.encendido_y_desbloqueado():
            self.configuracion.desactivar_modo_avion()
    def activar_datos(self):
        """
        Activa los datos móviles. Solo se pueden activar si la red móvil está activada, y el telefono encendido y desbloqueado.

        Devuelve: None
        """
        if self.encendido_y_desbloqueado():
            self.configuracion.activar_datos()
    def desactivar_datos(self):
        """Desactiva los datos moviles.
        
        Devuelve: None
        """
        if self.encendido_y_desbloqueado():
            self.configuracion.desactivar_datos()
            
    def modo_avion(self):
       return self.configuracion.modo_avion()    
   
    def datos_activos(self):
        return self.configuracion.datos_activos()
    # def activar_datos(self):

    #     if self.encendido_y_desbloqueado():
    #         self.configuracion.activar_datos()
    #         self.red_movil_activa = True  # Aseguramos que la red móvil esté activa
    #     else:
    #         raise ValueError("No se pueden activar los datos. El teléfono debe estar encendido y no en modo avión.")
    
    # def desactivar_datos(self):

    #     if self.encendido_y_desbloqueado():
    #         self.configuracion.desactivar_datos()
    
    # def activar_modo_avion(self):

    #     if self.encendido_y_desbloqueado():
    #         self.configuracion.activar_modo_avion()
    #         self.red_movil_activa = False
    
    # def desactivar_modo_avion(self):

    #     if self.encendido_y_desbloqueado():
    #         self.configuracion.desactivar_modo_avion()
    #         self.activar_red_movil()
    
    def abrir_aplicacion(self, nombre_app):
        if self.encendido_y_desbloqueado():
            if nombre_app in self.appstore.apps_descargadas:
                return f"Abriendo {nombre_app}"
            else:
                print ("Aplicación no encontrada")
        else:
            print ("El teléfono debe estar encendido y desbloqueado para abrir aplicaciones")
    
    def agregar_contacto(self, nombre, numero):
        """Agrega un contacto a los contactos del telefono.

        Args:
            nombre (str): El nombre del contacto.
            numero (int): El numero de telefono del contacto.
        
        Devuelve: None
        """
        if self.validar_numero_telefono(numero):
            self.contactos.add((nombre, numero)) #Al estar trabajando con cantactos = set(), si el contacto ya existe no saltara ningun error al tratar de agregar un contacto ya existente ni tampoco se agregara dos veces. Lo que pasara es nada. Solo tendremos un vez dicho contacto en el set().
        else:
            print ("Número de teléfono inválido")
    
    def actualizar_contacto(self, nombre, nuevo_numero): #Metodo para actualizar un contacto, es decir actualizar el numero de un usuario.
        """Actualiza el numero de telefono de un contacto si esta dentro se los contactos del telefono.

        Args:
            nombre (str): Nombre del contacto a modificar su numero.
            nuevo_numero (int): Nuevo numero de telefono.
        
        Devuelve: None
        """
        for contacto in self.contactos:
            if contacto[0] == nombre:
                self.contactos.remove(contacto)
                self.agregar_contacto(nombre, nuevo_numero)
                return
        print ("Contacto no encontrado")
    
    def enviar_mensaje(self, destino, contenido):
        """Simula enviado de mensaje a otro telefono. 

        Args:
            destino (int): Numero de destino.
            contenido (int): Numero de contenido.

        Returns:
            bool: True si se pudo enviar el mensaje, False de lo contrario.
        """
        if self.encendido_y_desbloqueado and not self.modo_avion:
            self.historial_sms_enviados.push((destino, contenido, datetime.now()))
            return True
        return False
    
    def recibir_mensaje(self, origen, contenido):
        """Simula el recibimiento de un mensaje. 

        Args:
            origen (int): Telefono de origen del mensaje.
            contenido (str): Contenido del mensaje.
            
        Devuelve: None
        """
        self.bandeja_entrada_sms.enqueue((origen, contenido, datetime.now()))
    
    def eliminar_mensaje(self):
        ################################################################CHEQUEAR ESTO 
        if not self.bandeja_entrada_sms.esta_vacia():
            return self.bandeja_entrada_sms.dequeue()
        else:
            print ("No hay mensajes para eliminar")
    
    def realizar_llamada(self, numero):
        """Simula la realizacion de una llamada.

        Args:
            numero (int): Numero al que se le realiza la llamada.

        Returns:
            bool: True si se realizo la llamada, False de lo contrario.
        """
        if self.encendido_y_desbloqueado and not self.modo_avion:
            self.historial_llamadas.insertar((numero, datetime.now(), "saliente"))
            return True
        return False
    
    def recibir_llamada(self, numero):
        """Simula el recibimiento de una llamada.

        Args:
            numero (int): Numero del cual recibo la llamada.
            
        Returns: None.
        """
        self.historial_llamadas.insertar((numero, datetime.now(), "entrante"))
        
    def descargar_app(self,name):
        """Simula el descargado de una app en el telefono usando la appstore.

        Args:
            name (str): El nombre de la app a descargar.
            
        Returns: None.
        """
        if self.datos_activos and self.encendido_y_desbloqueado():
            self.appstore.descargar_app(name)
        elif not self.datos_activos:
            print('No tiene datos para descargar aplicaciones')
    def eliminar_app(self,name):
        """Simula la eliminacion de una app dentro del telefono. 

        Args:
            name (str): El nombre de la app a eliminar.
            
        Returns: None.
        """
        if self.encendido_y_desbloqueado():
            self.appstore.eliminar_app(name)
        else:
            print('No se han podido mostrar mails, debe tener telefono encendido y desbloqueado.')
    
    # def descargar_app(self, nombre_app):
    #     # if self.validar_encendido() and self.validar_desbloqueado() and self.configuracion.datos_activos:
    #     #     self.apps_instaladas.add(nombre_app)
    #     if self.configuracion.datos_activos and self.encendido_y_desbloqueado():
    #         self.appstore.descargar_app(nombre_app)

    #     else:
    #         raise ValueError("El teléfono debe estar encendido, desbloqueado y con datos activos para descargar aplicaciones")
    
    # def eliminar_app(self, nombre_app):
    #     if nombre_app in self.apps_instaladas:
    #         # self.apps_instaladas.remove(nombre_app)
    #         self.appstore.eliminar_app(nombre_app)
    #     else:
    #         raise ValueError("La aplicación no está instalada")
    
    def ver_historial_llamadas(self):
        """Devuelve el historial de llamadas del telefono como lista.

        Returns:
            list: Una lista con historial de llamadas.
        """
        return list(self.historial_llamadas)
    
    def ver_bandeja_entrada_sms(self):
        """Devuelve la bandeja de entrada de sms como lista. 

        Returns:
            list: Una lista con todos los mensajes recibidos de sms.
        """
        return list(self.bandeja_entrada_sms.items)
    
    def ver_historial_sms_enviados(self):
        """Devuelve el historial de mensajes sms enviados como lista.

        Returns:
            list: Una lista con todos los mensajes enviados de sms.
        """
        return list(self.historial_sms_enviados.items)
    
    def validar_encendido(self):
        return self.encendido
    
    def validar_desbloqueado(self):
        return not self.bloqueado
    
    def validar_numero_telefono(self, numero):
        return len(str(numero)) == 10  # Ejemplo simple de validación
    
    def ver_mails(self, orden="no leídos primeros"):
        """Muestra los mails que tiene el telefono por pantalla teniendo en cuenta un orden.

        Args:
            orden (str): Orden con el que se van a imprimir los mails. Defaults to "no leídos primeros".
            
        Returns: None.
        """
        if self.encendido_y_desbloqueado:
            self.mail.ver_mails(orden)
        else:
            print ("El teléfono debe estar encendido y desbloqueado para ver los mails")

    def cambiar_nombre_telefono(self,nuevo_nombre_telefono):
        """Cambia el nombre del telefono.

        Args:
            nuevo_nombre_telefono (str): El nuevo nombre de telefono.
            
        Returns: None.
        """
        if self.encendido_y_desbloqueado():
            self.configuracion.cambiar_nombre(nuevo_nombre_telefono)
        else:
            print ("El teléfono debe estar encendido y desbloqueado para cambiar el nombre")
    
    def nombre_telefono(self):
        return self.configuracion.nombre_telefono
    
    

