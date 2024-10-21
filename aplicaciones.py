#Las aplicaciones permiten realizar llamadas, enviar SMS, gestionar contactos, etc. 
#Definimos una clase base de aplicaciones y algunas subclases para el manejo de llamadas y mensajes.

from telefono import *

class Aplicacion:
    """
    Clase base para todas las aplicaciones.
    """
    def __init__(self, nombre):
        self.nombre = nombre

    def ejecutar(self):
        """
        Método que define la ejecución de la aplicación. Debe ser sobrescrito por subclases.
        """
        pass

class AppTelefono(Aplicacion):
    """
    Aplicación para realizar y recibir llamadas.
    """
    def __init__(self):
        super().__init__("Teléfono")

    def ejecutar(self):
        print("Aplicación Teléfono abierta. Puede realizar llamadas.")

class AppSMS(Aplicacion):
    """
    Aplicación para enviar y recibir mensajes SMS.
    """
    def __init__(self):
        super().__init__("Mensajes")

    def ejecutar(self):
        print("Aplicación de Mensajes SMS abierta. Puede enviar y recibir mensajes.")

from collections import deque
class AppMail:
    def __init__(self, owner:Telefono):
        self.owner = owner  # El teléfono al que pertenece la app
        self.bandeja_de_salida = []
        self.bandeja_de_entrada_noleidos = deque()  #creo pia
        self.bandeja_de_entrada_leidos = []

    def enviar_mail(self, destinatario : Telefono, mensaje):
        if destinatario.tiene_app():
            mail = f"De: {self.owner.numero_telefono}, Para: {destinatario.numero_telefono}, Mensaje: {mensaje}"
            destinatario.recibir_mail(mail)
            self.bandeja_de_salida.append(mail)
            print(f"Correo enviado a {destinatario.numero_telefono}")
        else:
            print(f"No se puede enviar el correo. {destinatario.numero_telefono} no tiene la app de mail.")

    def recibir_mail(self, mail):
        self.bandeja_de_entrada_noleidos.appendleft([mail,datetime.now().strftime("%Y-%m-%d %H:%M:%S")]) 
               
    def ver_mis_mails (self):
        copia = self.bandeja_de_entrada_leidos
        print('Correos NO leidos:')
        for cosa in self.bandeja_de_entrada_noleidos:
            print(cosa)
            self.bandeja_de_entrada_leidos.appendleft(cosa)
        print('Correos leidos:')
        for elemento in copia:
            print(elemento)
        
        self.bandeja_de_entrada_noleidos = deque()        
        
    
        
        
