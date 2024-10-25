# telefono.py
from datetime import datetime

class Telefono:
    def __init__(self, id, nombre, modelo, sistema_operativo, version_so, ram, almacenamiento, numero_telefono, central):
        self.id = id
        self.nombre = nombre
        self.modelo = modelo
        self.sistema_operativo = sistema_operativo
        self.version_so = version_so
        self.ram = ram
        self.almacenamiento = almacenamiento
        self.numero_telefono = numero_telefono
        self.encendido = False
        self.bloqueado = True
        self.red_movil_activa = False
        self.datos_activos = False
        self.modo_avion = False
        self.central = central
        self.central.registrar_dispositivo(self)
        
    def prender(self):
        self.encendido = True
        self.activar_red_movil()
        print(f"Teléfono {self.nombre} encendido.")
        
    def apagar(self):
        self.encendido = False
        self.red_movil_activa = False
        self.datos_activos = False
        print(f"Teléfono {self.nombre} apagado.")
        
    def bloquear(self):
        self.bloqueado = True
        print(f"Teléfono {self.nombre} bloqueado.")
        
    def desbloquear(self):
        self.bloqueado = False
        print(f"Teléfono {self.nombre} desbloqueado.")
            
    def activar_red_movil(self):
        if self.encendido and not self.modo_avion:
            self.red_movil_activa = True
            print("Red móvil activada.")
        else:
            print("El teléfono debe estar encendido y no en modo avión para activar la red móvil.")
            
    def desactivar_red_movil(self):
        self.red_movil_activa = False
        print("Red móvil desactivada.")
        
    def activar_datos(self):
        if self.red_movil_activa and not self.modo_avion:
            self.datos_activos = True
            print("Datos móviles activados.")
        else:
            print("La red móvil debe estar activa y el teléfono no debe estar en modo avión para activar los datos.")
            
    def desactivar_datos(self):
        self.datos_activos = False
        print("Datos móviles desactivados.")
        
    def activar_modo_avion(self):
        self.modo_avion = True
        self.red_movil_activa = False
        self.datos_activos = False
        self.central.actualizar_modo_avion(self.numero_telefono, True)
        print("Modo avión activado.")
        
    def desactivar_modo_avion(self):
        self.modo_avion = False
        self.central.actualizar_modo_avion(self.numero_telefono, False)
        print("Modo avión desactivado.")
        
    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
        print(f"Nombre del teléfono cambiado a: {self.nombre}")
    def realizar_llamada(self, numero_destino):
        if not self.encendido or self.modo_avion or not self.red_movil_activa:
            print("No se puede realizar la llamada en este momento.")
            return

        telefono_destino = self.central.buscar_telefono(numero_destino)
        if telefono_destino and telefono_destino.puede_recibir_llamadas():
            telefono_destino.recibir_llamada(self.numero)
            self.central.registrar_llamada(self.numero, numero_destino, 60)  # Duración ficticia de 60 segundos
            print(f"Llamada realizada a {numero_destino}")
        else:
            print(f"No se pudo realizar la llamada a {numero_destino}")
   
    
    def recibir_llamada(self, numero_origen):
        self.llamadas_recibidas.append(numero_origen)
        print(f"Llamada recibida de {numero_origen}")

    def enviar_sms(self, numero_destino, mensaje):
        if not self.encendido or self.modo_avion or not self.red_movil_activa:
            print("No se puede enviar el mensaje en este momento.")
            return

        telefono_destino = self.central.buscar_telefono(numero_destino)
        if telefono_destino and telefono_destino.puede_recibir_mensajes():
            telefono_destino.recibir_sms(self.numero, mensaje)
            self.central.registrar_mensaje(self.numero, numero_destino, mensaje)
            print(f"Mensaje enviado a {numero_destino}: {mensaje}")
        else:
            print(f"No se pudo enviar el mensaje a {numero_destino}")
    def puede_recibir_mensajes(self):
        return self.encendido and not self.modo_avion and self.red_movil_activa

    def puede_recibir_llamadas(self):
        return self.encendido and not self.modo_avion and self.red_movil_activa

    def mostrar_mensajes_recibidos(self):
        if not self.mensajes_recibidos:
            print("No hay mensajes recibidos")
        else:
            for numero, mensaje in self.mensajes_recibidos:
                print(f"De: {numero} - Mensaje: {mensaje}")

    def mostrar_llamadas_recibidas(self):
        if not self.llamadas_recibidas:
            print("No hay llamadas recibidas")
        else:
            for numero in self.llamadas_recibidas:
                print(f"Llamada recibida de: {numero}")