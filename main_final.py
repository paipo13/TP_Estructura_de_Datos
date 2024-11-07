from analisis_de_datos import *
from aplicaciones import *
from central import *
from estructuras_de_datos import *
from telefono_final import *

import random , datetime

def generar_correos():
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
    
    # Crear teléfonos
    telefono1 = Telefono( "iPhone", "12 Pro", "iOS", "14.5", 6, 128, 1234567890)
    telefono2 = Telefono( "Samsung", "Galaxy S21", "Android", "11", 8, 256, 9876543210)
    telefono3 = Telefono( "Google", "Pixel 5", "Android", "12", 8, 128, 5555555555)
    telefono4 = Telefono( "Xiaomi", "Mi 11", "Android", "11", 8, 256, 1112223333)
    

    #cambio nombre telefono 
    print(telefono1.nombre_telefono())
    telefono1.cambiar_nombre_telefono("iphone_de_nico")
    telefono1.encender()
    telefono1.desbloquear()
    telefono1.cambiar_nombre_telefono("iphone_de_nico")
    print(telefono1.nombre_telefono())

    print(telefono1.id)
    # Data para graficos de Matplotlib
    diccionario_grafico = {}
    for telefono in [telefono1, telefono2, telefono3, telefono4]:
        agregar_datos_diccionario(diccionario_grafico,telefono.sistema_operativo)


    # Registrar teléfonos en la central
    for telefono in [telefono1, telefono2, telefono3, telefono4]:
        central.registrar_telefono(telefono)
        print(f"Teléfono registrado: {telefono.nombre_telefono()} {telefono.modelo} ({telefono.numero})")
    print()

    # Encender y desbloquear teléfonos
    for telefono in [telefono1, telefono2, telefono3, telefono4]:
        telefono.encender()
        telefono.desbloquear()
        print(f"{telefono.nombre_telefono()} {telefono.modelo} encendido y desbloqueado.")
    print()
    
    # Agregar contactos
    contactos = [
        (telefono1, "Alice", 9876543210),
        (telefono1, "Bob", 5555555555),
        (telefono2, "Charlie", 1234567890),
        (telefono3, "David", 1112223333),
        (telefono4, "Eve", 1234567890)
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
        if central.realizar_llamada(origen.numero, destino.numero, duracion) == True:
            print(f"Llamada de {origen.nombre_telefono()} a {destino.nombre_telefono()} realizada con éxito (duración: {duracion}s)")
        else:
            print(f"No se pudo realizar la llamada de {origen.nombre_telefono()} a {destino.nombre_telefono()}")
    print()

    # Enviar mensajes
    mensajes = [
        (telefono1, telefono2, "Hola, ¿cómo estás?"),
        (telefono2, telefono3, "¿Nos vemos luego?"),
        (telefono3, telefono4, "Recuerda la reunión de mañana"),
        (telefono4, telefono1, "Gracias por la información")
    ]
    print("Enviando mensajes:")
    for origen, destino, contenido in mensajes:
        if central.enviar_mensaje(origen.numero, destino.numero, contenido):
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
        print()

    # Activar modo avión en un teléfono
    telefono2.activar_modo_avion()
    central.actualizar_modo_avion(telefono2.numero, True)
    print(f"Modo avión activado en {telefono2.nombre_telefono()}")
    print()

    # Intentar llamar a un teléfono en modo avión
    print(f"Intentando llamar a {telefono2.nombre_telefono()} (en modo avión):")
    if central.realizar_llamada(telefono1.numero, telefono2.numero, 45):
        print("Llamada realizada con éxito (esto no debería ocurrir)")
    else:
        print("No se pudo realizar la llamada (comportamiento esperado)")
    print()

    # Desactivar modo avión
    telefono2.desactivar_modo_avion()
    central.actualizar_modo_avion(telefono2.numero, False)
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
    #ACA HAY QUE HACER ALGO CON LAS APLICACIONES. 
    #
    # Descargar una nueva aplicación
    # nueva_app = "Instagram"
    # for telefono in [telefono1, telefono3]:
    #     try:
    #         telefono.descargar_app(nueva_app)
    #         print(f"{nueva_app} descargada en {telefono.nombre}")
    #     except ValueError as e:
    #         print(f"Error al descargar {nueva_app} en {telefono.nombre}: {e}")
    # print()

    # Simular una llamada ocupada
    print("Simulando una llamada ocupada:")
    central.realizar_llamada(telefono3.numero, telefono4.numero, 120)  # Llamada larga en curso
    if central.realizar_llamada(telefono1.numero, telefono4.numero, 30):
        print(f"Llamada de {telefono1.nombre_telefono()} a {telefono4.nombre_telefono()} realizada con éxito (esto no debería ocurrir)")
    else:
        print(f"No se pudo realizar la llamada de {telefono1.nombre_telefono()} a {telefono4.nombre_telefono()} (teléfono ocupado)")
    print()

    # # Mostrar emails (simulado)
    # print(f"Emails de {telefono1.nombre_telefono()}:")
    # emails_simulados = [
    #     ("sender1@example.com", "Asunto 1", "Contenido del email 1", datetime.now() - timedelta(days=1)),
    #     ("sender2@example.com", "Asunto 2", "Contenido del email 2", datetime.now() - timedelta(hours=5)),
    #     ("sender3@example.com", "Asunto 3", "Contenido del email 3", datetime.now() - timedelta(minutes=30))
    # ]
    # for email in emails_simulados:
    #     telefono1.recibir_email(*email)
    # print(telefono1.ver_emails("no leídos primeros"))
    # print(telefono1.ver_emails("por fecha"))
    # print()

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
