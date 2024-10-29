class Configuracion:
    def __init__(self):
        self.modo_avion = False
        self.datos = False

class prueba():
    def __init__(self):
        self.bloqueado = False
        self.encendido = True
        self.configuracion = Configuracion()

    def encendido_y_desbloqueado(self):   # devuelve True si el teléfono está encendido y desbloqueado
        if not self.encendido:
            print("El teléfono está apagado")
        if self.bloqueado:
            print("El teléfono está bloqueado")
        return self.encendido and not self.bloqueado
    
#prueba

prueba_objeto = prueba()
if prueba_objeto.encendido_y_desbloqueado() and not prueba_objeto.configuracion.modo_avion:
    print("El teléfono está encendido y desbloqueado")
