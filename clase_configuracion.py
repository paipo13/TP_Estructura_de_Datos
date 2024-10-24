class Configuracion:
    def __init__(self):
        self.modo_avion = False
        self.datos = False
    
    def activar_modo_avion(self):
        if self.modo_avion==False:
            self.modo_avion = True
            print("Modo avion activado")
            if self.datos==True:
                self.datos = False
                print("Datos desactivados")
        else:
            print("Ya se encuentra en modo avion")
    def desactivar_modo_avion(self):
        if self.modo_avion==True:
            self.modo_avion = False
            print("Modo avion desactivado")
        else:
            print("No se encuentra en modo avion")
            
    def activar_datos(self):
        if self.modo_avion==True:
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