class Configuracion:
    def __init__(self):
        self.red_movil = False
        self.datos = False
    
    def activar_red_movil(self):
        if self.red_movil==False:
            self.red_movil = True
            print("Modo avion activado")
            if self.datos==True:
                self.datos = False
                print("Datos desactivados")
        else:
            print("Ya se encuentra en modo avion")
    def desactivar_red_movil(self):
        if self.red_movil==True:
            self.red_movil = False
            print("Modo avion desactivado")
        else:
            print("No se encuentra en modo avion")
            
    def activar_datos(self):
        if self.red_movil==True:
            print("No puedes activar los datos en modo avion")
        elif self.datos==False:
            self.datos = True
            print("Datos activados")   
        else:
            print("Ya se encuentran los datos activos")
    def desactivar_datos(self):
        if self.datos==True:
            self.datos = False
            print("Datos desactivados")
        else:
            print("Los datos ya estan desactivados")