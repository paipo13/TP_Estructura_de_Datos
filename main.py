#Main
from telefono import *
from aplicaciones import *
from listas_enlazadas import *
from contactos import *
from listas_enlazadas import * 
from central_comunicacion import *
from appstore import *

if __name__ == "__main__":
    # Crear dispositivos
    telefono1 = Telefono(1, "Teléfono1", "ModeloX", "Android", "12.0", 4, 64, "123456789")
    telefono2 = Telefono(2, "Teléfono2", "ModeloY", "Android", "12.0", 4, 64, "987654321")

    # Crear central de comunicaciones
    central = Central()

    # Registrar dispositivos
    central.registrar_dispositivo(telefono1)
    central.registrar_dispositivo(telefono2)

    # Pruebas de encendido y apagado
    telefono1.encender()
    telefono1.bloquear()
    telefono1.desbloquear()
    telefono1.activar_red_movil()
    telefono2.encender()
    telefono2.activar_red_movil()
    # Activar red móvil y realizar llamada
    telefono1.realizar_llamada(telefono2, central)

    # Enviar un mensaje
    telefono1.enviar_sms(telefono2, "Hola, ¿cómo estás?", central)

    # Apagar el teléfono y tratar de enviar otro mensaje
    telefono1.apagar()
    telefono1.enviar_sms(telefono2, "Esto no debería enviarse", central)

    # Crear App Store y mostrar aplicaciones disponibles
    app_store = AppStore()
    app_store.mostrar_aplicaciones()

    # Descargar aplicación "Correo"
    app_store.descargar_aplicacion(telefono1, "Correo")

    # Pruebas de encendido, red móvil, y realizar una llamada
    telefono1.encender()
    telefono1.activar_red_movil()
    telefono1.realizar_llamada("987654321", central)

    # Enviar un mensaje y registrar en CSV
    print(central.dispositivos_registrados)
    for i in central.dispositivos_registrados:
        print(i.numero_telefono)
    #print(type(telefono2.numero_telefono))
    telefono1.enviar_sms("987654321", "Hola, ¿cómo estás?", central)

    # Generar un reporte de las comunicaciones

    central.generar_reporte_comunicaciones()


