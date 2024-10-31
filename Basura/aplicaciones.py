#Las aplicaciones permiten realizar llamadas, enviar SMS, gestionar contactos, etc. 
#Definimos una clase base de aplicaciones y algunas subclases para el manejo de llamadas y mensajes.

from telefono import *
from datetime import datetime
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
    def __init__(self, owner):   #owner es objeto Telefono 
        self.owner = owner  # El teléfono al que pertenece la app
        self.bandeja_de_salida = []
        self.bandeja_de_entrada_noleidos = deque()  #creo pila
        self.bandeja_de_entrada_leidos = deque()

    def enviar_mail(self, destinatario, mail_destinatario, mensaje): #destinatario es objeto Telefono 
        if destinatario.tiene_app('AppMail'):
            mail = f"De: {self.owner.numero_telefono}, Para: {destinatario.numero_telefono}, Mensaje: {mensaje}"
            mail_destinatario.recibir_mail(mail)
            self.bandeja_de_salida.append(mail)
            print(f"Correo enviado a {destinatario.numero_telefono}")
        else:
            print(f"No se puede enviar el correo. {destinatario.numero_telefono} no tiene la app de mail.")

    def recibir_mail(self, mail):
        self.bandeja_de_entrada_noleidos.appendleft([mail,datetime.now().strftime("%Y-%m-%d %H:%M:%S")]) ## OJO VER TEMA FECHA QUE SINO SON TODAS IGUALES
               
    def ver_mis_mails (self):
        eleccion = int(input('''Como desea ver sus mails?
    Opcion1: No leidos primero
    Opcion2: Por fecha mas reciente 
    '''))
        while eleccion != 1 and eleccion !=2 :
            eleccion = int(input('''ERROR. Debe ingresar un 1 o un 2.
        Como desea ver sus mails?
        Opcion1: No leidos primero
        Opcion2: Por fecha mas reciente'''))
        
        if eleccion == 1:
            print('Ha elegido la OPCION1: No leidos primero')
            copia = list(self.bandeja_de_entrada_leidos)
            copia.sort(key=lambda x: datetime.strptime(x[1], "%Y-%m-%d %H:%M:%S"), reverse=True) #para ordenar segun fecha
            print('Correos NO leidos:')
            for cosa in self.bandeja_de_entrada_noleidos:
                print(cosa)
                self.bandeja_de_entrada_leidos.appendleft(cosa)
            print('Correos leidos:')
            for elemento in copia:
                print(elemento)
            self.bandeja_de_entrada_noleidos = deque()   #vacio los noleidos ya que se leyo todo      
        else: 
            print('Ha elegido la OPCION2: Por fecha mas reciente')
            bandeja_completa = list(self.bandeja_de_entrada_leidos) + list(self.bandeja_de_entrada_noleidos)
            bandeja_completa.sort(key=lambda x: datetime.strptime(x[1], "%Y-%m-%d %H:%M:%S"), reverse=True) #ordeno segun fecha
            print('Correos:')
            for i in bandeja_completa:
                print(i)
            self.bandeja_de_entrada_noleidos = deque()   #vacio los noleidos ya que se leyo todo   
            
        
    
        
        
