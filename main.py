from analisis_de_datos import *
from aplicaciones import *
from central import *
from estructuras_de_datos import *
from telefono import *
import random , datetime

def generar_correos():
    """Genere una lista de 20 correos electronicos con el formato correspondiente.

    Returns:
        list: Una lista de listas con los 20 correos dentro.
    """
    correos = []  # Lista vacía para almacenar los correos
    for _ in range(20):
        mensaje = f"Mensaje {_ + 1}"  # Mensaje único
        estado = random.choice(['leido', 'no leido'])  # Estado aleatorio
        fecha = datetime.datetime(random.randint(1990,2024),random.randint(1,12), random.randint(1,25), random.randint(0,23), random.randint(0,59))
        correo = [mensaje, fecha, estado]  # Formato del correo
        correos.append(correo)
    return correos
def main():
    central = Central()
    
    # Crear teléfonos, Obs. Como indica el enunciado trabajaremos con una central...
    try:
        telefono1 = Telefono( "iPhone", "12 Pro", "iOS", "14.5", 6, 128, 1234567890, central)
    except ValueError as e:
        print(f"Error creando telefono: {e}")
    
    try:
        telefono2 = Telefono( "Samsung", "Galaxy S21", "Android", "11", 8, 256, 9876543210, central)
    except ValueError as e:
        print(f"Error creando telefono: {e}")
        
    try:
        telefono3 = Telefono( "Google", "Pixel 5", "Android", "12", 8, 128, 5555555555, central)
    except ValueError as e:
        print(f"Error creando telefono: {e}")
    
    try:
        telefono4 = Telefono( "Xiaomi", "Mi 11", "Android", "11", 8, 256, 1112223333, central)
    except ValueError as e:
        print(f"Error creando telefono: {e}")
    # Simulando error por numero de telefono ya existente.
    try:
        telefono5= Telefono("Motorola","M15", "Android","11", 8, 128, 5555555555, central)
    except ValueError as e:
        print(f"Error creando telefono: {e}")
    

    #cambio nombre telefono 
    print(telefono1.nombre_telefono())
    telefono1.cambiar_nombre_telefono("iphone_de_nico")
    telefono1.encender()
    telefono1.desbloquear()
    telefono1.cambiar_nombre_telefono("iphone_de_nico")
    print(telefono1.nombre_telefono())

    print(telefono1.id) #id generado con "uuid.uuid4()". Unico. Para fines practivos de todas formas estaremos refiriendonos a los telefonos por el numero.
    # Data para graficos de Matplotlib:
    diccionario_grafico = {}
    for telefono in [telefono1, telefono2, telefono3, telefono4]:
        agregar_datos_diccionario(diccionario_grafico,telefono.sistema_operativo) # Se usara mas abajo para el analisis de datos.


    # Registrar teléfonos en la central
    for telefono in [telefono1, telefono2, telefono3, telefono4]:
        central.registrar_telefono(telefono)
        print(f"Teléfono registrado: {telefono.nombre_telefono()} {telefono.modelo} ({telefono.numero})")
    print("Telefonos registrados en la central:\n",list(central.telefonos_registrados))
    print()

    # Encender y desbloquear teléfonos
    for telefono in [telefono1, telefono2, telefono3, telefono4]:
        telefono.encender()
        telefono.desbloquear()
        print(f"{telefono.nombre_telefono()} {telefono.modelo} encendido y desbloqueado.")
    print()
    
    # Agregar contactos
    contactos = [
        (telefono1, "Ninfa", 9876543210),
        (telefono1, "Franco", 5555555555),
        (telefono2, "Charlie", 1234567890),
        (telefono3, "Facu Lassarre ;)", 1112223333),
        (telefono4, "Gustavo", 1234567890)
    ]
    for telefono, nombre, numero in contactos:
        telefono.agregar_contacto(nombre, numero)
        print(f"Contacto {nombre} agregado a {telefono.nombre_telefono()}")
    print()
    # Realizar llamadas
    llamadas = [
        (telefono1, telefono2, 60),
        (telefono2, telefono3, 45),
        (telefono3, telefono4, 30),
        (telefono4, telefono1, 90)
    ]
    print("Realizando llamadas:")
    for origen, destino, duracion in llamadas:
        if central.realizar_llamada(origen.numero, destino.numero, datetime.datetime(2022, 5, 7, 15), duracion) == True:
            print(f"Llamada de {origen.nombre_telefono()} a {destino.nombre_telefono()} realizada con éxito (duración: {duracion}s)")
        else:
            print(f"No se pudo realizar la llamada de {origen.nombre_telefono()} a {destino.nombre_telefono()}")
    print()

    # Enviar mensajes
    mensajes = [
        (telefono1, telefono2, "Hola, ¿cómo estás?"),
        (telefono2, telefono3, "¿Nos vemos luego?"),
        (telefono3, telefono4, "Recuerda la reunión de mañana"),
        (telefono4, telefono1, "Gracias por la información"),
        (telefono2, telefono1, "Bien, vos?"),
        (telefono1, telefono2, "Bien, Hacemos algo mañana?"),
        (telefono2, telefono1, "DALEEE!!!"),
        (telefono1, telefono2, "Buenisimoooooooooooooooo")
    ]
    print("Enviando mensajes:")
    for origen, destino, contenido in mensajes:
        if central.enviar_mensaje(origen.numero, destino.numero, datetime.datetime(2024, 2, 1, 10, 30), contenido):
            print(f"Mensaje de {origen.nombre_telefono()} a {destino.nombre_telefono()} enviado con éxito")
        else:
            print(f"No se pudo enviar el mensaje de {origen.nombre_telefono()} a {destino.nombre_telefono()}")
    print()
    
    # Mostrar mails
    print("Mostrando mails:")
    for telefono in [telefono1, telefono2, telefono3, telefono4]:
        telefono.mail.bandeja  = generar_correos()
        print(f"Mails de {telefono.nombre_telefono()}:")
        telefono.ver_mails('no leidos primero')
        telefono.ver_mails('por fecha')
        print()
    
    # Mostrar historial de llamadas y mensajes
    for telefono in [telefono1, telefono2, telefono3, telefono4]:
        print(f"Historial de llamadas de {telefono.nombre_telefono()}:")
        print(telefono.ver_historial_llamadas())
        print(f"Bandeja de entrada de SMS de {telefono.nombre_telefono()}:")
        print(telefono.ver_bandeja_entrada_sms())
        print(f"Historial de mensajes enviados de {telefono.nombre_telefono()}:")
        print(telefono.ver_historial_sms_enviados())
        print()
        
    # Eliminacion de mensajes.
    print('Eliminacion de mensaje:')
    telefono4.eliminar_mensaje(50)
    telefono4.eliminar_mensaje(0)    
    print()
    
    # Activar modo avión en un teléfono
    telefono2.activar_modo_avion()
    # central.actualizar_modo_avion(telefono2.numero, True)
    print(f"Modo avión activado en {telefono2.nombre_telefono()}")
    print()

    # Intentar llamar a un teléfono en modo avión
    print(f"Intentando llamar a {telefono2.nombre_telefono()} (en modo avión):")
    if central.realizar_llamada(telefono1.numero, telefono2.numero,datetime.datetime(2024, 8, 8, 12, 20, 10), 45):
        print("Llamada realizada con éxito (esto no debería ocurrir)")
    else:
        print("No se pudo realizar la llamada (comportamiento esperado)")
    print()

    # Desactivar modo avión
    telefono2.desactivar_modo_avion()
    # central.actualizar_modo_avion(telefono2.numero, False)
    print(f"Modo avión desactivado en {telefono2.nombre_telefono()}")
    print()

    # Activar datos en los teléfonos
    print("Activando datos en los teléfonos:")
    for telefono in [telefono1, telefono2, telefono3, telefono4]:
        try:
            telefono.activar_datos()
            print(f"Datos activados en {telefono.nombre_telefono()}")
        except ValueError as e:
            print(f"Error al activar datos en {telefono.nombre_telefono()}: {e}")
    print()

    # Simular una llamada ocupada
    print("Simulando una llamada ocupada:")
    central.realizar_llamada(telefono3.numero, telefono4.numero, datetime.datetime(2023, 12, 25, 0, 1, 20), 120)  # Llamada larga en curso
    if central.realizar_llamada(telefono1.numero, telefono4.numero,datetime.datetime(2023, 12, 25, 0, 2, 20), 30):
        print(f"Llamada de {telefono1.nombre_telefono()} a {telefono4.nombre_telefono()} realizada con éxito (esto no debería ocurrir)")
    else:
        print(f"No se pudo realizar la llamada de {telefono1.nombre_telefono()} a {telefono4.nombre_telefono()} (teléfono ocupado)")
    print()

 
    telefono1.activar_datos()
    telefono2.desactivar_datos()
    #Descargar app exitosamente
    telefono1.descargar_app('Coloring book moana')
    print(f'Coloring book moana descargada en {telefono1.nombre_telefono()}')
    
    #Simular falla de descarga por ya tener la app descargada
    telefono1.descargar_app('Coloring book moana')
    
    #Simular falla de descarga por app inexistente
    telefono1.descargar_app('App_inexistente')
    
    #Simular falla de descarga por tener datos desacticados
    telefono2.descargar_app('Coloring book moana')
    
    #Eliminar app exitosamente
    telefono1.eliminar_app('Coloring book moana')
    
    #Simular falla de eliminar app por no tenerla instalada
    telefono1.eliminar_app('Infinite Painter')
    

    # Usar la app de Paint
    telefono1.usar_paint()
    
    # Mostrar registros de la central
    print("Registros de la central:")
    central.mostrar_registros()

    #Graficos con Matplotlib
    print(diccionario_grafico)
    grafico_barras(diccionario_grafico)

    dic_con_info = maquinita_de_ayuda()
    graficar_torta_llamadas(dic_con_info)
if __name__ == "__main__":
    main()
