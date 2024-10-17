
from telefono import *
from aplicaciones import *
from contactos import *

class AppStore:
    """
    Representa una tienda de aplicaciones donde los teléfonos pueden descargar apps.
    """
    def __init__(self):
        self.aplicaciones_disponibles = {
            "Teléfono": AppTelefono(),
            "Mensajes": AppSMS(),
            "Correo": Aplicacion("Correo"),
            "Configuración": Aplicacion("Configuración")
        }

    def mostrar_aplicaciones(self):
        """
        Muestra las aplicaciones disponibles para descargar.
        """
        print("Aplicaciones disponibles en la tienda:")
        for nombre, app in self.aplicaciones_disponibles.items():
            print(f"- {nombre}")

    def descargar_aplicacion(self, Telefono, nombre_aplicacion):
        """
        Permite que un teléfono descargue una aplicación.
        """
        if nombre_aplicacion in self.aplicaciones_disponibles:
            nueva_app = self.aplicaciones_disponibles[nombre_aplicacion]
            Telefono.instalar_aplicacion(nueva_app)
            print(f"Se ha descargado la aplicación {nombre_aplicacion}.")
        else:
            print(f"La aplicación {nombre_aplicacion} no está disponible en la tienda.")
