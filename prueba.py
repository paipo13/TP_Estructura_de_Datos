import uuid
from analisis_de_datos import *
from aplicaciones import *
from central import *
from estructuras_de_datos import *
from telefono_final import *

telefono1 = Telefono(1, "iPhone", "12 Pro", "iOS", "14.5", 6, 128, 1234567890)
telefono2 = Telefono(2, "Samsung", "Galaxy S21", "Android", "11", 8, 256, 9876543210)
telefono3 = Telefono(3, "Google", "Pixel 5", "Android", "12", 8, 128, 5555555555)
telefono4 = Telefono(4, "Xiaomi", "Mi 11", "Android", "11", 8, 256, 1112223333)
    

    #cambio nombre telefono 
print(telefono1.nombre_telefono())
telefono1.cambiar_nombre_telefono("iphone_de_nico")
telefono1.encender()
telefono1.desbloquear()
telefono1.cambiar_nombre_telefono("iphone_de_nico")
print(telefono1.nombre_telefono())

id = uuid.uuid4()
id1 = uuid.uuid4()
id2 = uuid.uuid4()
print(id1 , id2, id)
if id == id1 or id == id2:
    print("Los ids son iguales")
else:
    print("Los ids son diferentes")
