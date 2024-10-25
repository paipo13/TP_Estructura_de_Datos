from pe_nuevo_telefono import Telefono
from pe_nuevo_central import Central

def main():
    central = Central()
    
    telefono1 = Telefono(1, "Teléfono 1", "Modelo X", "Android", "10.0", "4GB", "64GB", "123456789", central)
    telefono2 = Telefono(2, "Teléfono 2", "Modelo Y", "iOS", "14.0", "6GB", "128GB", "987654321", central)
    
    # Encender ambos teléfonos
    telefono1.prender()
    telefono2.prender()
    
    print("Escenario 1: Teléfono 1 envía SMS a Teléfono 2")
    telefono1.enviar_sms("987654321", "Hola, ¿cómo estás?")
    print("SMS enviado desde Teléfono 1")
    print("Estado de Teléfono 2:")
    telefono2.mostrar_mensajes_recibidos()
    
    print("\nEscenario 2: Teléfono 2 no puede enviar SMS a Teléfono 1")
    # Desactivar la red móvil de Teléfono 1 para que no pueda recibir mensajes
    telefono1.desactivar_datos()
    try:
        telefono2.enviar_sms("123456789", "Este mensaje no debería llegar")
    except Exception as e:
        print(f"Error al enviar SMS: {e}")
    print("Estado de Teléfono 1:")
    telefono1.mostrar_mensajes_recibidos()
    
    print("\nEscenario 3: Llamada de Teléfono 1 a Teléfono 2")
    # Reactivar la red móvil de Teléfono 1
    telefono1.activar_datos()
    telefono1.realizar_llamada("987654321")
    print("Llamada realizada desde Teléfono 1")
    print("Estado de Teléfono 2:")
    telefono2.mostrar_llamadas_recibidas()
    
    # Mostrar registros de la central
    print("\nRegistros de la central:")
    central.mostrar_registros()

if __name__ == "__main__":
    main()