#Las aplicaciones permiten realizar llamadas, enviar SMS, gestionar contactos, etc. 
#Definimos una clase base de aplicaciones y algunas subclases para el manejo de llamadas y mensajes.



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
