#Las clases Contacto y Mensaje encapsulan la información básica necesaria para gestionar la agenda y los SMS.

from telefono import *
from central_comunicacion import *
from listas_enlazadas import *

class Contacto:
    """
    Clase que representa un contacto de la agenda.
    """
    def __init__(self, nombre, numero):
        self.nombre = nombre
        self.numero = numero

    def __str__(self):
        return f"{self.nombre}: {self.numero}"

class Mensaje:
    """
    Clase que representa un SMS.
    """
    def __init__(self, remitente, destinatario, contenido):
        self.remitente = remitente
        self.destinatario = destinatario
        self.contenido = contenido
        self.leido = False

    def marcar_leido(self):
        self.leido = True

    def __str__(self):
        return f"De: {self.remitente}, Para: {self.destinatario}, Mensaje: {self.contenido}"

    def enviar(self):
        print(f"Enviando mensaje de {self.remitente} a {self.destinatario}: {self.contenido}")
        self.marcar_leido()

    