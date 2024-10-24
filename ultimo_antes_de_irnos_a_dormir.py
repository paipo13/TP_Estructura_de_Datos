



















import os
from datetime import datetime, timedelta
import csv

# Estructuras de datos
class Nodo:
    def __init__(self, dato=None, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
    
    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
    
    def __iter__(self):
        actual = self.cabeza
        while actual:
            yield actual.dato
            actual = actual.siguiente

class Pila:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def esta_vacia(self):
        return len(self.items) == 0

class Cola:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        return self.items.pop()
    
    def esta_vacia(self):
        return len(self.items) == 0

class Telefono:
    def __init__(self, id, nombre, modelo, sistema_operativo, version, ram, almacenamiento, numero):
        self.id = id
        self.nombre = nombre
        self.modelo = modelo
        self.sistema_operativo = sistema_operativo
        self.version = version
        self.ram = ram
        self.almacenamiento = almacenamiento
        self.numero = numero
        self.encendido = False
        self.bloqueado = True
        self.red_movil_activa = False
        self.datos_activos = False
        self.modo_avion = False
        
        # Inicializar componentes internos
        self.contactos = set()
        self.bandeja_entrada_sms = Cola()
        self.historial_sms_enviados = Pila()
        self.emails = ListaEnlazada()
        self.historial_llamadas = ListaEnlazada()
        self.apps_instaladas = set(["Contactos", "Mensajeria", "Email", "Telefono", "AppStore", "Configuracion"])
    
    def encender(self):
        self.encendido = True
        self.activar_red_movil()
    
    def apagar(self):
        self.encendido = False
        self.red_movil_activa = False
        self.datos_activos = False
    
    def bloquear(self):
        self.bloqueado = True
    
    def desbloquear(self):
        self.bloqueado = False
    
    def activar_red_movil(self):
        if self.encendido and not self.modo_avion:
            self.red_movil_activa = True
    
    def desactivar_red_movil(self):
        self.red_movil_activa = False
    
    def activar_datos(self):
        if self.encendido and not self.modo_avion:
            self.datos_activos = True
            self.red_movil_activa = True  # Aseguramos que la red móvil esté activa
        else:
            raise ValueError("No se pueden activar los datos. El teléfono debe estar encendido y no en modo avión.")
    
    def desactivar_datos(self):
        self.datos_activos = False
    
    def activar_modo_avion(self):
        self.modo_avion = True
        self.red_movil_activa = False
        self.datos_activos = False
    
    def desactivar_modo_avion(self):
        self.modo_avion = False
        self.activar_red_movil()
    
    def abrir_aplicacion(self, nombre_app):
        if self.validar_encendido() and self.validar_desbloqueado():
            if nombre_app in self.apps_instaladas:
                return f"Abriendo {nombre_app}"
            else:
                raise ValueError("Aplicación no encontrada")
        else:
            raise ValueError("El teléfono debe estar encendido y desbloqueado para abrir aplicaciones")
    
    def agregar_contacto(self, nombre, numero):
        if self.validar_numero_telefono(numero):
            self.contactos.add((nombre, numero))
        else:
            raise ValueError("Número de teléfono inválido")
    
    def actualizar_contacto(self, nombre, nuevo_numero):
        for contacto in self.contactos:
            if contacto[0] == nombre:
                self.contactos.remove(contacto)
                self.agregar_contacto(nombre, nuevo_numero)
                return
        raise ValueError("Contacto no encontrado")
    
    def enviar_mensaje(self, destino, contenido):
        if self.validar_encendido() and self.validar_desbloqueado() and self.red_movil_activa:
            self.historial_sms_enviados.push((destino, contenido, datetime.now()))
            return True
        return False
    
    def recibir_mensaje(self, origen, contenido):
        self.bandeja_entrada_sms.enqueue((origen, contenido, datetime.now()))
    
    def eliminar_mensaje(self):
        if not self.bandeja_entrada_sms.esta_vacia():
            return self.bandeja_entrada_sms.dequeue()
        else:
            raise ValueError("No hay mensajes para eliminar")
    
    def realizar_llamada(self, numero):
        if self.validar_encendido() and self.validar_desbloqueado() and self.red_movil_activa:
            self.historial_llamadas.insertar((numero, datetime.now(), "saliente"))
            return True
        return False
    
    def recibir_llamada(self, numero):
        self.historial_llamadas.insertar((numero, datetime.now(), "entrante"))
    
    def descargar_app(self, nombre_app):
        if self.validar_encendido() and self.validar_desbloqueado() and self.datos_activos:
            self.apps_instaladas.add(nombre_app)
        else:
            raise ValueError("El teléfono debe estar encendido, desbloqueado y con datos activos para descargar aplicaciones")
    
    def eliminar_app(self, nombre_app):
        if nombre_app in self.apps_instaladas:
            self.apps_instaladas.remove(nombre_app)
        else:
            raise ValueError("La aplicación no está instalada")
    
    def ver_historial_llamadas(self):
        return list(self.historial_llamadas)
    
    def ver_bandeja_entrada_sms(self):
        return list(self.bandeja_entrada_sms.items)
    
    def ver_historial_sms_enviados(self):
        return list(self.historial_sms_enviados.items)
    
    def validar_encendido(self):
        return self.encendido
    
    def validar_desbloqueado(self):
        return not self.bloqueado
    
    def validar_numero_telefono(self, numero):
        return len(str(numero)) == 10  # Ejemplo simple de validación
    
    def recibir_email(self, remitente, asunto, contenido, fecha):
        self.emails.insertar((remitente, asunto, contenido, fecha))
    
    def ver_emails(self, orden="no leídos primeros"):
        emails = list(self.emails)
        if orden == "no leídos primeros":
            return sorted(emails, key=lambda x: x[3], reverse=True)
        elif orden == "por fecha":
            return sorted(emails, key=lambda x: x[3])
        else:
            raise ValueError("Orden no válido")

class Configuracion:
    def __init__(self):
        self.nombre_telefono = ""
        self.codigo_desbloqueo = ""
    
    def configurar_nombre(self, nombre):
        self.nombre_telefono = nombre
    
    def configurar_codigo_desbloqueo(self, codigo):
        self.codigo_desbloqueo = codigo

class Central:
    def __init__(self):
        self.telefonos_registrados = {}
        self.telefono_modo_avion = {}
        self.inicializar_archivos()
    
    def inicializar_archivos(self):
        if not os.path.exists('datos'):
            os.makedirs('datos')
        
        for archivo in ['llamadas.csv', 'mensajes.csv']:
            ruta_archivo = os.path.join('datos', archivo)
            if not os.path.exists(ruta_archivo):
                with open(ruta_archivo, 'w', newline='') as file:
                    writer = csv.writer(file)
                    if archivo == 'llamadas.csv':
                        writer.writerow(['origen', 'destino', 'duracion', 'tiempo', 'estado'])
                    else:
                        writer.writerow(['origen', 'destino', 'contenido', 'tiempo'])
    
    def registrar_telefono(self, telefono):
        self.telefonos_registrados[telefono.numero] = telefono
        self.telefono_modo_avion[telefono.numero] = False
    
    def desregistrar_telefono(self, telefono):
        if telefono.numero in self.telefonos_registrados:
            del self.telefonos_registrados[telefono.numero]
            del self.telefono_modo_avion[telefono.numero]
    
    def actualizar_modo_avion(self, numero, estado):
        if numero in self.telefono_modo_avion:
            self.telefono_modo_avion[numero] = estado
    
    def validar_llamada(self, origen, destino):
        if (origen in self.telefonos_registrados and destino in self.telefonos_registrados and
            not self.telefono_modo_avion[origen] and not self.telefono_modo_avion[destino] and
            self.telefonos_registrados[origen].validar_encendido() and
            self.telefonos_registrados[origen].validar_desbloqueado() and
            self.telefonos_registrados[destino].validar_encendido()):
            return True
        return False
    
    def validar_mensaje(self, origen, destino):
        if (origen in self.telefonos_registrados and destino in self.telefonos_registrados and
            not self.telefono_modo_avion[origen] and not self.telefono_modo_avion[destino] and
            self.telefonos_registrados[origen].validar_encendido() and
            self.telefonos_registrados[origen].validar_desbloqueado()):
            return True
        return False
    
    def realizar_llamada(self, origen, destino, duracion):
        if self.validar_llamada(origen, destino):
            tiempo = datetime.now()
            estado = self.determinar_estado_llamada(destino, tiempo)
            self.registrar_llamada(origen, destino, duracion, tiempo, estado)
            self.telefonos_registrados[origen].realizar_llamada(destino)
            self.telefonos_registrados[destino].recibir_llamada(origen)
            return True
        return False
    
    def enviar_mensaje(self, origen, destino, contenido):
        if self.validar_mensaje(origen, destino):
            tiempo = datetime.now()
            self.registrar_mensaje(origen, destino, contenido, tiempo)
            self.telefonos_registrados[origen].enviar_mensaje(destino, contenido)
            self.telefonos_registrados[destino].recibir_mensaje(origen, contenido)
            return True
        return False
    
    def determinar_estado_llamada(self, destino, tiempo_actual):
        ultima_llamada = self.obtener_ultima_llamada(destino)
        if ultima_llamada:
            tiempo_ultima_llamada, duracion_ultima_llamada = ultima_llamada
            tiempo_fin_ultima_llamada = tiempo_ultima_llamada + timedelta(seconds=duracion_ultima_llamada)
            if tiempo_fin_ultima_llamada >= tiempo_actual:
                return "ocupado"
        return "conectado"
    
    def obtener_ultima_llamada(self, numero):
        ruta_archivo = os.path.join('datos', 'llamadas.csv')
        if not os.path.exists(ruta_archivo):
            return None
        with open(ruta_archivo, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Saltar la fila de encabezados
            llamadas = list(reader)
            for llamada in reversed(llamadas):
                if llamada[1] == str(numero):  # Si el número es el destino de la llamada
                    tiempo = datetime.strptime(llamada[3], '%Y-%m-%d %H:%M:%S.%f')
                    duracion = int(llamada[2])
                    return tiempo, duracion
        return None
    
    def registrar_llamada(self, origen, destino, duracion, tiempo, estado):
        ruta_archivo = os.path.join('datos', 'llamadas.csv')
        with open(ruta_archivo, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([origen, destino, duracion, tiempo, estado])
    
    def registrar_mensaje(self, origen, destino, contenido, tiempo):
        ruta_archivo = os.path.join('datos', 'mensajes.csv')
        with open(ruta_archivo, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([origen, destino, contenido, tiempo])
    
    def mostrar_registros(self):
        print("Registro de llamadas:")
        ruta_archivo = os.path.join('datos', 'llamadas.csv')
        with open(ruta_archivo, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
        
        print("\nRegistro de mensajes:")
        ruta_archivo = os.path.join('datos', 'mensajes.csv')
        with open(ruta_archivo, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

def main():
    central = Central()
    
    # Crear teléfonos
    telefono1 = Telefono(1, "iPhone", "12 Pro", "iOS", "14.5", 6, 128, 1234567890)
    telefono2 = Telefono(2, "Samsung", "Galaxy S21", "Android", "11", 8, 256, 9876543210)
    telefono3 = Telefono(3, "Google", "Pixel 5", "Android", "12", 8, 128, 5555555555)
    telefono4 = Telefono(4, "Xiaomi", "Mi 11", "Android", "11", 8, 256, 1112223333)
    
    # Registrar teléfonos en la central
    for telefono in [telefono1, telefono2, telefono3, telefono4]:
        central.registrar_telefono(telefono)
        print(f"Teléfono registrado: {telefono.nombre} {telefono.modelo} ({telefono.numero})")
    print()

    # Encender y desbloquear teléfonos
    for telefono in [telefono1, telefono2, telefono3, telefono4]:
        telefono.encender()
        telefono.desbloquear()
        print(f"{telefono.nombre} {telefono.modelo} encendido y desbloqueado.")
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
        print(f"Contacto {nombre} agregado a {telefono.nombre}")
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
        if central.realizar_llamada(origen.numero, destino.numero, duracion):
            print(f"Llamada de {origen.nombre} a {destino.nombre} realizada con éxito (duración: {duracion}s)")
        else:
            print(f"No se pudo realizar la llamada de {origen.nombre} a {destino.nombre}")
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
            print(f"Mensaje de {origen.nombre} a {destino.nombre} enviado con éxito")
        else:
            print(f"No se pudo enviar el mensaje de {origen.nombre} a {destino.nombre}")
    print()

    # Mostrar historial de llamadas y mensajes
    for telefono in [telefono1, telefono2, telefono3, telefono4]:
        print(f"Historial de llamadas de {telefono.nombre}:")
        print(telefono.ver_historial_llamadas())
        print(f"Bandeja de entrada de SMS de {telefono.nombre}:")
        print(telefono.ver_bandeja_entrada_sms())
        print()

    # Activar modo avión en un teléfono
    telefono2.activar_modo_avion()
    central.actualizar_modo_avion(telefono2.numero, True)
    print(f"Modo avión activado en {telefono2.nombre}")
    print()

    # Intentar llamar a un teléfono en modo avión
    print(f"Intentando llamar a {telefono2.nombre} (en modo avión):")
    if central.realizar_llamada(telefono1.numero, telefono2.numero, 45):
        print("Llamada realizada con éxito (esto no debería ocurrir)")
    else:
        print("No se pudo realizar la llamada (comportamiento esperado)")
    print()

    # Desactivar modo avión
    telefono2.desactivar_modo_avion()
    central.actualizar_modo_avion(telefono2.numero, False)
    print(f"Modo avión desactivado en {telefono2.nombre}")
    print()

    # Activar datos en los teléfonos
    print("Activando datos en los teléfonos:")
    for telefono in [telefono1, telefono2, telefono3, telefono4]:
        try:
            telefono.activar_datos()
            print(f"Datos activados en {telefono.nombre}")
        except ValueError as e:
            print(f"Error al activar datos en {telefono.nombre}: {e}")
    print()

    # Descargar una nueva aplicación
    nueva_app = "Instagram"
    for telefono in [telefono1, telefono3]:
        try:
            telefono.descargar_app(nueva_app)
            print(f"{nueva_app} descargada en {telefono.nombre}")
        except ValueError as e:
            print(f"Error al descargar {nueva_app} en {telefono.nombre}: {e}")
    print()

    # Configurar teléfonos
    telefono1.configuracion = Configuracion()
    telefono1.configuracion.configurar_nombre("iPhone de Juan")
    telefono1.configuracion.configurar_codigo_desbloqueo("1234")
    print(f"Configuración actualizada para {telefono1.nombre}")
    print()

    # Simular una llamada ocupada
    print("Simulando una llamada ocupada:")
    central.realizar_llamada(telefono3.numero, telefono4.numero, 120)  # Llamada larga en curso
    if central.realizar_llamada(telefono1.numero, telefono4.numero, 30):
        print(f"Llamada de {telefono1.nombre} a {telefono4.nombre} realizada con éxito (esto no debería ocurrir)")
    else:
        print(f"No se pudo realizar la llamada de {telefono1.nombre} a {telefono4.nombre} (teléfono ocupado)")
    print()

    # Mostrar emails (simulado)
    print(f"Emails de {telefono1.nombre}:")
    emails_simulados = [
        ("sender1@example.com", "Asunto 1", "Contenido del email 1", datetime.now() - timedelta(days=1)),
        ("sender2@example.com", "Asunto 2", "Contenido del email 2", datetime.now() - timedelta(hours=5)),
        ("sender3@example.com", "Asunto 3", "Contenido del email 3", datetime.now() - timedelta(minutes=30))
    ]
    for email in emails_simulados:
        telefono1.recibir_email(*email)
    print(telefono1.ver_emails("no leídos primeros"))
    print(telefono1.ver_emails("por fecha"))
    print()

    # Mostrar registros de la central
    print("Registros de la central:")
    central.mostrar_registros()

if __name__ == "__main__":
    main()
    