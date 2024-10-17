from telefono import *
from aplicaciones import *
from listas_enlazadas import *
from contactos import *
from listas_enlazadas import * 
from central_comunicacion import *
from appstore import *

telefono1 = Telefono(1, "Teléfono1", "ModeloX", "Android", "12.0", 4, 64, "123456789")
telefono2 = Telefono(2, "Teléfono2", "ModeloY", "Android", "12.0", 4, 64, "987654321")
personal = Central()

telefono1.encender(personal)
telefono2.encender(personal)
print(personal.dispositivos_registrados)

telefono1.realizar_llamada("987654321",personal)
personal.generar_reporte_comunicaciones()

